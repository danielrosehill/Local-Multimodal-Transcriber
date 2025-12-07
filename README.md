# Local Multimodal Transcriber

> **Status: Work in Progress**

A local, GPU-accelerated speech-to-text system using multimodal audio models. Unlike traditional ASR pipelines that require separate transcription and cleanup steps, this tool uses models with native audio understanding to transcribe and format in a single pass.

## Concept

- **Input**: Audio recording (voice notes, dictation, etc.)
- **Output**: Cleaned transcript with punctuation, paragraphs, and filler words removed
- **Approach**: Multimodal LLM inference (audio + text prompt → formatted text)

## Target Hardware

- AMD GPU (RX 7700/7800 XT series)
- 12 GB VRAM
- ROCm acceleration via Docker

## Project Documentation

- [idea/](idea/) - Project concept and roadmap
- [planning/](planning/) - Model candidates and research
- [app/](app/) - Application prototype

## License

TBD
