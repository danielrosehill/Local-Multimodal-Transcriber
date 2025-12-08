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

## Initial Findings: Voxtral Viability Assessment

The primary goal of this repository isn't to run comprehensive model evaluations, but rather to assess whether running multimodal audio-understanding models locally is a viable alternative to traditional pure-play ASR pipelines.

### Voxtral Benchmark Results

Tested GPU-accelerated Voxtral on the target hardware (RX 7700 XT, 12GB VRAM):

| Metric | Result |
|--------|--------|
| VRAM Usage | ~10 GB / 12 GB (83%) |
| System Impact | Significant lag during inference |
| Practical Viability | **Not viable** for this workload |

### Conclusion

While Voxtral demonstrates the capability of multimodal audio transcription, the ~83% VRAM utilization leaves insufficient headroom for other processes and caused noticeable system degradation. For hardware with 12GB VRAM, this model is not practical for regular use.

This establishes a baseline: viable local multimodal transcription will require either:
- Models with smaller memory footprints
- Hardware with more VRAM headroom
- Quantized model variants

See [benchmarks/](benchmarks/) for detailed test configurations and results.

## Project Documentation

- [idea/](idea/) - Project concept and roadmap
- [planning/](planning/) - Model candidates and research
- [app/](app/) - Application prototype

## License

TBD
