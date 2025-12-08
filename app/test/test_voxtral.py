#!/usr/bin/env python3
"""
Test script for Voxtral-Mini-3B transcription with 30-second chunking.

Usage:
    python test_voxtral.py [audio_file]

If no audio file provided, uses the concept.mp3 from idea/ directory.
"""

import sys
import time
import tempfile
from pathlib import Path

import torch
import numpy as np
import soundfile as sf
from transformers import VoxtralForConditionalGeneration, AutoProcessor

# Model configuration
MODEL_ID = "mistralai/Voxtral-Mini-3B-2507"
CHUNK_SECONDS = 30
SAMPLE_RATE = 16000


def load_model():
    """Load Voxtral model and processor."""
    print(f"Loading {MODEL_ID}...")
    start = time.time()

    processor = AutoProcessor.from_pretrained(MODEL_ID)
    model = VoxtralForConditionalGeneration.from_pretrained(
        MODEL_ID,
        torch_dtype=torch.bfloat16,
        device_map="cuda",
    )

    print(f"Model loaded in {time.time() - start:.1f}s")
    print(f"Device: {next(model.parameters()).device}")
    return model, processor


def transcribe_chunk(model, processor, audio_array: np.ndarray, chunk_idx: int) -> str:
    """Transcribe a single audio chunk."""
    # Save chunk to temp file (processor expects a path)
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
        sf.write(f.name, audio_array, SAMPLE_RATE)
        temp_path = f.name

    try:
        inputs = processor.apply_transcription_request(
            audio=temp_path,
            language="en",
            model_id=MODEL_ID,
        )
        inputs = inputs.to("cuda", dtype=torch.bfloat16)

        with torch.no_grad():
            outputs = model.generate(
                **inputs,
                max_new_tokens=512,  # 30s chunk doesn't need many tokens
                do_sample=False,
            )

        transcription = processor.batch_decode(
            outputs[:, inputs.input_ids.shape[1]:],
            skip_special_tokens=True
        )[0]

        return transcription.strip()
    finally:
        Path(temp_path).unlink(missing_ok=True)


def transcribe(model, processor, audio_path: str) -> str:
    """Transcribe audio file with 30-second chunking."""
    import librosa

    print(f"\nLoading audio: {audio_path}")
    audio, sr = librosa.load(audio_path, sr=SAMPLE_RATE)
    duration = len(audio) / sr
    print(f"Audio duration: {duration:.1f}s ({duration/60:.1f} min)")

    # Calculate chunks
    chunk_samples = CHUNK_SECONDS * SAMPLE_RATE
    num_chunks = int(np.ceil(len(audio) / chunk_samples))
    print(f"Processing {num_chunks} chunks of {CHUNK_SECONDS}s each...")

    start = time.time()
    transcriptions = []

    for i in range(num_chunks):
        chunk_start = i * chunk_samples
        chunk_end = min((i + 1) * chunk_samples, len(audio))
        chunk = audio[chunk_start:chunk_end]

        chunk_duration = len(chunk) / SAMPLE_RATE
        print(f"  Chunk {i+1}/{num_chunks} ({chunk_duration:.1f}s)...", end=" ", flush=True)

        chunk_start_time = time.time()
        text = transcribe_chunk(model, processor, chunk, i)
        chunk_time = time.time() - chunk_start_time

        print(f"done in {chunk_time:.1f}s")
        transcriptions.append(text)

        # Clear CUDA cache between chunks
        torch.cuda.empty_cache()

    inference_time = time.time() - start
    print(f"\nTotal inference time: {inference_time:.1f}s")
    print(f"Real-time factor: {inference_time/duration:.2f}x")

    # Join transcriptions with space
    return " ".join(transcriptions)


def main():
    # Determine audio file
    if len(sys.argv) > 1:
        audio_path = sys.argv[1]
    else:
        # Default to concept.mp3
        audio_path = "/app/idea/concept.mp3"
        if not Path(audio_path).exists():
            audio_path = "../idea/concept.mp3"

    if not Path(audio_path).exists():
        print(f"Error: Audio file not found: {audio_path}")
        print("Usage: python test_voxtral.py <audio_file>")
        sys.exit(1)

    # Load model
    model, processor = load_model()

    # Check VRAM usage
    if torch.cuda.is_available():
        vram_gb = torch.cuda.memory_allocated() / 1e9
        print(f"VRAM used after model load: {vram_gb:.1f} GB")

    # Transcribe
    result = transcribe(model, processor, audio_path)

    print("\n" + "="*60)
    print("TRANSCRIPTION RESULT")
    print("="*60)
    print(result)
    print("="*60)

    # Save output
    output_path = "/app/output/" + Path(audio_path).stem + "_transcribed.txt"
    Path("/app/output").mkdir(exist_ok=True)
    with open(output_path, "w") as f:
        f.write(result)
    print(f"\nSaved to: {output_path}")


if __name__ == "__main__":
    main()
