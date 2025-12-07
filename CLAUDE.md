# CLAUDE.md - Local Multimodal Transcriber

## Project Overview

A local, GPU-accelerated multimodal audio transcription system that leverages audio-understanding LLMs to perform "cleanup transcription"—transcribing audio while simultaneously adding punctuation, paragraph breaks, and removing filler words.

## Core Concept

Instead of the traditional two-step pipeline (ASR → LLM cleanup), this project uses multimodal models that:
1. Accept audio input directly
2. Accept text prompts for transcription instructions
3. Return cleaned, formatted transcriptions in a single inference pass

See [idea/transcription.md](idea/transcription.md) for the full project context and roadmap.

## Hardware Constraints

- **GPU**: AMD Radeon RX 7700 XT / 7800 XT (Navi 32, gfx1101)
- **VRAM**: 12 GB
- **Acceleration**: ROCm with PyTorch
- **Docker**: PyTorch ROCm base image available

## Key Requirements

### Transcription Features (MVP)
- Filler word removal ("um", "uh", pauses)
- Punctuation restoration
- Paragraph spacing/breaks
- Single operation: transcribe + cleanup → text output

### GUI Requirements (POC)
- Record / Stop / Transcribe buttons
- Microphone selection
- Copy-to-clipboard for output
- No separate "raw transcription" mode—cleanup only

### Technical Requirements
- GPU-accelerated inference (ROCm)
- Docker-based deployment (stack layering on PyTorch ROCm)
- Easy mechanisms for bringing stack up/down during testing

## Current Status

**Phase**: Research & Planning

- Identifying multimodal audio models compatible with:
  - AMD GPU / ROCm
  - 12GB VRAM constraint
  - Reasonable context windows for ~5-10 minute recordings

## Project Structure

```
.
├── idea/              # Project concept and context
│   ├── concept.mp3    # Original voice note
│   └── transcription.md  # Transcribed roadmap
├── planning/          # Research and candidate analysis
├── app/               # Application prototype
└── README.md          # Public-facing documentation
```

## Development Notes

- Context window is a key concern—cloud models handle 45+ minutes, local may be limited to much shorter clips
- Audio tokenization efficiency varies by model
- May need to experiment with multiple candidates to find viable option
- Consider VAD (Voice Activity Detection) as a later enhancement, not MVP
