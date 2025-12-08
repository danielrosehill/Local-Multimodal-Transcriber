#!/usr/bin/env python3
"""
Benchmark script with GPU/VRAM monitoring.
"""

import sys
import time
import threading
from pathlib import Path
from datetime import datetime

import torch

# Paths
if Path("/app/test-prompts/prompts").exists():
    PROMPTS_DIR = Path("/app/test-prompts/prompts")
    DEFAULT_AUDIO = Path("/app/testing/audio/concept_1min.mp3")
    OUTPUT_DIR = Path("/app/benchmarks/results")
else:
    SCRIPT_DIR = Path(__file__).parent
    REPO_DIR = SCRIPT_DIR.parent
    PROMPTS_DIR = REPO_DIR / "test-prompts" / "prompts"
    DEFAULT_AUDIO = REPO_DIR / "testing" / "audio" / "concept_1min.mp3"
    OUTPUT_DIR = REPO_DIR / "benchmarks" / "results"

MODEL_ID = "mistralai/Voxtral-Mini-3B-2507"


class GPUMonitor:
    """Monitor GPU metrics during inference."""

    def __init__(self):
        self.running = False
        self.samples = []
        self.thread = None

    def _sample(self):
        while self.running:
            if torch.cuda.is_available():
                allocated = torch.cuda.memory_allocated() / 1e9
                reserved = torch.cuda.memory_reserved() / 1e9
                self.samples.append({
                    'time': time.time(),
                    'allocated_gb': allocated,
                    'reserved_gb': reserved,
                })
            time.sleep(0.1)  # Sample every 100ms

    def start(self):
        self.running = True
        self.samples = []
        self.thread = threading.Thread(target=self._sample)
        self.thread.start()

    def stop(self):
        self.running = False
        if self.thread:
            self.thread.join()

    def report(self):
        if not self.samples:
            return {}

        allocated = [s['allocated_gb'] for s in self.samples]
        reserved = [s['reserved_gb'] for s in self.samples]

        return {
            'samples': len(self.samples),
            'vram_allocated_min_gb': min(allocated),
            'vram_allocated_max_gb': max(allocated),
            'vram_allocated_avg_gb': sum(allocated) / len(allocated),
            'vram_reserved_max_gb': max(reserved),
        }


def load_prompt(prompt_path: str) -> tuple:
    if not prompt_path.endswith(".md"):
        prompt_path += ".md"
    full_path = PROMPTS_DIR / prompt_path
    if not full_path.exists():
        full_path = Path(prompt_path)
    if not full_path.exists():
        raise FileNotFoundError(f"Prompt not found: {prompt_path}")
    return full_path.read_text().strip(), full_path


def run_benchmark(prompt_path: str, audio_path: str = None):
    from transformers import VoxtralForConditionalGeneration, AutoProcessor
    import librosa

    # Load prompt
    prompt_text, prompt_file = load_prompt(prompt_path)
    print(f"Prompt: {prompt_file.name}")

    # Audio
    audio = Path(audio_path) if audio_path else DEFAULT_AUDIO
    if not audio.exists():
        print(f"Audio not found: {audio}")
        return

    # Get audio duration
    audio_data, sr = librosa.load(str(audio), sr=16000)
    audio_duration = len(audio_data) / sr
    print(f"Audio: {audio.name} ({audio_duration:.1f}s)")

    # Initialize GPU monitor
    monitor = GPUMonitor()

    print("\n=== LOADING MODEL ===")
    load_start = time.time()

    processor = AutoProcessor.from_pretrained(MODEL_ID)
    model = VoxtralForConditionalGeneration.from_pretrained(
        MODEL_ID,
        torch_dtype=torch.bfloat16,
        device_map="cuda",
    )

    load_time = time.time() - load_start
    vram_after_load = torch.cuda.memory_allocated() / 1e9
    print(f"Model load time: {load_time:.2f}s")
    print(f"VRAM after load: {vram_after_load:.2f} GB")

    print("\n=== PREPARING INPUT ===")
    prep_start = time.time()

    inputs = processor.apply_chat_template(
        [{"role": "user", "content": [
            {"type": "audio", "path": str(audio)},
            {"type": "text", "text": prompt_text}
        ]}],
        tokenize=True,
        return_tensors="pt",
    ).to("cuda", dtype=torch.bfloat16)

    prep_time = time.time() - prep_start
    input_tokens = inputs.input_ids.shape[1]
    print(f"Prep time: {prep_time:.2f}s")
    print(f"Input tokens: {input_tokens}")

    print("\n=== INFERENCE ===")
    monitor.start()
    inference_start = time.time()

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=2048,
            do_sample=False,
        )

    inference_time = time.time() - inference_start
    monitor.stop()

    output_tokens = outputs.shape[1] - input_tokens
    tokens_per_sec = output_tokens / inference_time
    rtf = inference_time / audio_duration  # Real-time factor

    result = processor.batch_decode(
        outputs[:, inputs.input_ids.shape[1]:],
        skip_special_tokens=True
    )[0]

    gpu_stats = monitor.report()

    print(f"Inference time: {inference_time:.2f}s")
    print(f"Output tokens: {output_tokens}")
    print(f"Tokens/sec: {tokens_per_sec:.1f}")
    print(f"Real-time factor: {rtf:.2f}x")

    print("\n=== GPU METRICS ===")
    print(f"Samples collected: {gpu_stats.get('samples', 0)}")
    print(f"VRAM allocated (min): {gpu_stats.get('vram_allocated_min_gb', 0):.2f} GB")
    print(f"VRAM allocated (max): {gpu_stats.get('vram_allocated_max_gb', 0):.2f} GB")
    print(f"VRAM allocated (avg): {gpu_stats.get('vram_allocated_avg_gb', 0):.2f} GB")
    print(f"VRAM reserved (max): {gpu_stats.get('vram_reserved_max_gb', 0):.2f} GB")

    print("\n=== RESULT ===")
    print(result[:500] + "..." if len(result) > 500 else result)

    # Save detailed report
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_file = OUTPUT_DIR / f"benchmark_{prompt_file.stem}_{timestamp}.md"

    with open(report_file, "w") as f:
        f.write(f"# Benchmark: {prompt_file.stem}\n\n")
        f.write(f"**Date**: {datetime.now().isoformat()}\n")
        f.write(f"**Model**: `{MODEL_ID}`\n")
        f.write(f"**Audio**: `{audio.name}` ({audio_duration:.1f}s)\n\n")
        f.write("## Timing\n\n")
        f.write(f"| Metric | Value |\n")
        f.write(f"|--------|-------|\n")
        f.write(f"| Model load | {load_time:.2f}s |\n")
        f.write(f"| Input prep | {prep_time:.2f}s |\n")
        f.write(f"| Inference | {inference_time:.2f}s |\n")
        f.write(f"| **Total** | **{load_time + prep_time + inference_time:.2f}s** |\n\n")
        f.write("## Tokens\n\n")
        f.write(f"| Metric | Value |\n")
        f.write(f"|--------|-------|\n")
        f.write(f"| Input tokens | {input_tokens} |\n")
        f.write(f"| Output tokens | {output_tokens} |\n")
        f.write(f"| Tokens/sec | {tokens_per_sec:.1f} |\n")
        f.write(f"| Real-time factor | {rtf:.2f}x |\n\n")
        f.write("## GPU Memory\n\n")
        f.write(f"| Metric | Value |\n")
        f.write(f"|--------|-------|\n")
        f.write(f"| VRAM after load | {vram_after_load:.2f} GB |\n")
        f.write(f"| VRAM min (inference) | {gpu_stats.get('vram_allocated_min_gb', 0):.2f} GB |\n")
        f.write(f"| VRAM max (inference) | {gpu_stats.get('vram_allocated_max_gb', 0):.2f} GB |\n")
        f.write(f"| VRAM avg (inference) | {gpu_stats.get('vram_allocated_avg_gb', 0):.2f} GB |\n")
        f.write(f"| VRAM reserved max | {gpu_stats.get('vram_reserved_max_gb', 0):.2f} GB |\n\n")
        f.write("## Prompt\n\n")
        f.write(f"```\n{prompt_text}\n```\n\n")
        f.write("## Response\n\n")
        f.write(result)

    print(f"\nSaved: {report_file.name}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python run_benchmark.py <prompt_path> [audio_path]")
        print("Example: python run_benchmark.py emotion/guess-my-mood")
        return

    prompt_path = sys.argv[1]
    audio_path = sys.argv[2] if len(sys.argv) > 2 else None
    run_benchmark(prompt_path, audio_path)


if __name__ == "__main__":
    main()
