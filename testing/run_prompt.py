#!/usr/bin/env python3
"""
CLI for running test prompts against audio using Voxtral.

Usage:
    python run_prompt.py list                    # List all prompts
    python run_prompt.py list <category>         # List prompts in category
    python run_prompt.py run <prompt_path>       # Run a specific prompt
    python run_prompt.py run <prompt_path> <audio>  # Run with custom audio
"""

import sys
import os
import time
from pathlib import Path
from datetime import datetime

# Paths - handle both local and container environments
SCRIPT_DIR = Path(__file__).parent
REPO_DIR = SCRIPT_DIR.parent

# In container: /app/test-prompts, locally: ../test-prompts
if Path("/app/test-prompts/prompts").exists():
    PROMPTS_DIR = Path("/app/test-prompts/prompts")
    DEFAULT_AUDIO = Path("/app/testing/audio/concept_1min.mp3")
    OUTPUT_DIR = Path("/app/benchmarks/results")
else:
    PROMPTS_DIR = REPO_DIR / "test-prompts" / "prompts"
    DEFAULT_AUDIO = REPO_DIR / "testing" / "audio" / "concept_1min.mp3"
    OUTPUT_DIR = REPO_DIR / "benchmarks" / "results"

# Model config
MODEL_ID = "mistralai/Voxtral-Mini-3B-2507"


def list_prompts(category=None):
    """List available prompts."""
    if not PROMPTS_DIR.exists():
        print(f"Prompts directory not found: {PROMPTS_DIR}")
        print("Run: git submodule update --init")
        return

    if category:
        cat_dir = PROMPTS_DIR / category
        if not cat_dir.exists():
            print(f"Category not found: {category}")
            return
        prompts = sorted(cat_dir.glob("**/*.md"))
        print(f"\n=== {category} ({len(prompts)} prompts) ===")
        for p in prompts:
            rel = p.relative_to(PROMPTS_DIR)
            print(f"  {rel}")
    else:
        # List categories
        categories = sorted([d.name for d in PROMPTS_DIR.iterdir() if d.is_dir()])
        print("\n=== Categories ===")
        for cat in categories:
            count = len(list((PROMPTS_DIR / cat).glob("**/*.md")))
            print(f"  {cat}/ ({count} prompts)")
        print(f"\nTotal: {len(list(PROMPTS_DIR.glob('**/*.md')))} prompts")
        print("\nUsage: python run_prompt.py list <category>")


def load_prompt(prompt_path: str) -> str:
    """Load prompt text from file."""
    # Handle relative paths
    if not prompt_path.endswith(".md"):
        prompt_path += ".md"

    full_path = PROMPTS_DIR / prompt_path
    if not full_path.exists():
        # Try direct path
        full_path = Path(prompt_path)

    if not full_path.exists():
        raise FileNotFoundError(f"Prompt not found: {prompt_path}")

    return full_path.read_text().strip(), full_path


def run_prompt(prompt_path: str, audio_path: str = None):
    """Run a prompt against audio using Voxtral."""
    import torch
    from transformers import VoxtralForConditionalGeneration, AutoProcessor

    # Load prompt
    prompt_text, prompt_file = load_prompt(prompt_path)
    print(f"Prompt: {prompt_file.relative_to(REPO_DIR)}")
    print(f"Content:\n{prompt_text[:200]}...")

    # Audio path
    audio = Path(audio_path) if audio_path else DEFAULT_AUDIO
    if not audio.exists():
        print(f"Audio not found: {audio}")
        return
    print(f"\nAudio: {audio}")

    # Load model
    print(f"\nLoading {MODEL_ID}...")
    processor = AutoProcessor.from_pretrained(MODEL_ID)
    model = VoxtralForConditionalGeneration.from_pretrained(
        MODEL_ID,
        torch_dtype=torch.bfloat16,
        device_map="cuda",
    )
    print(f"VRAM: {torch.cuda.memory_allocated() / 1e9:.1f} GB")

    # Prepare input
    print("\nProcessing...")
    inputs = processor.apply_chat_template(
        [{"role": "user", "content": [
            {"type": "audio", "path": str(audio)},
            {"type": "text", "text": prompt_text}
        ]}],
        tokenize=True,
        return_tensors="pt",
    ).to("cuda", dtype=torch.bfloat16)

    # Generate
    start = time.time()
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=2048,
            do_sample=False,
        )

    result = processor.batch_decode(
        outputs[:, inputs.input_ids.shape[1]:],
        skip_special_tokens=True
    )[0]

    elapsed = time.time() - start
    print(f"Inference: {elapsed:.1f}s")

    # Display result
    print("\n" + "="*60)
    print("RESULT")
    print("="*60)
    print(result)
    print("="*60)

    # Save output
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    prompt_name = prompt_file.stem
    output_file = OUTPUT_DIR / f"{prompt_name}_{timestamp}.md"

    with open(output_file, "w") as f:
        f.write(f"# {prompt_name}\n\n")
        f.write(f"**Prompt**: `{prompt_file.relative_to(REPO_DIR)}`\n")
        f.write(f"**Audio**: `{audio.name}`\n")
        f.write(f"**Model**: `{MODEL_ID}`\n")
        f.write(f"**Time**: {elapsed:.1f}s\n")
        f.write(f"**Date**: {datetime.now().isoformat()}\n\n")
        f.write("## Prompt\n\n")
        f.write(f"```\n{prompt_text}\n```\n\n")
        f.write("## Response\n\n")
        f.write(result)

    print(f"\nSaved: {output_file.relative_to(REPO_DIR)}")


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return

    cmd = sys.argv[1]

    if cmd == "list":
        category = sys.argv[2] if len(sys.argv) > 2 else None
        list_prompts(category)

    elif cmd == "run":
        if len(sys.argv) < 3:
            print("Usage: python run_prompt.py run <prompt_path> [audio_path]")
            return
        prompt_path = sys.argv[2]
        audio_path = sys.argv[3] if len(sys.argv) > 3 else None
        run_prompt(prompt_path, audio_path)

    else:
        print(f"Unknown command: {cmd}")
        print(__doc__)


if __name__ == "__main__":
    main()
