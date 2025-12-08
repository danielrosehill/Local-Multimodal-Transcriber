# Local Multimodal Transcriber

> **Status: Work in Progress**

 This repository is a planning repository attempting to create a viable UI for multimodal audio AI on my local desktop environment (Linux, AMD).

Multimodal models offer very promising capabilities over traditional ASR tools, specifically in the transcription use case, combining the ability to generate accurate transcriptions with applying post processing text edits. 

Potential target models have been identified and the list will change over time. The basic implementation was validated in so far as gaining multimodal outputs based on audio and text inputs via local inference was possible. However, the challenge is finding a model that has a sufficiently small quantization for my current hardware. 

For those with more powerful local inference available (>12 GB VRAM), this constraint can be overcome.

This repository includes a submodule of test prompts that I created in order to validate audio understanding by challenging the model to identify emotional tone, accent, and conduct various text reformatting workloads (assessing for the text postprocessing capability).  That repository is available directly [here](https://github.com/danielrosehill/Audio-Understanding-Test-Prompts).

The various results in *this* repo, however, show that Voxtral is extremely capable of driving this workload!

## Concept

- **Input**: Audio recording (voice notes, dictation, etc.)
- **Output**: Cleaned transcript with punctuation, paragraphs, and filler words removed
- **Approach**: Multimodal LLM inference (audio + text prompt → formatted text)

## Target Hardware

- AMD GPU (RX 7700/7800 XT series)
- 12 GB VRAM
- ROCm acceleration via Docker

## Models

Potential models are:

- Multimodal "omni" models 
- Multimodal audio models (Hugging Face task: audio-text to text)

These include:

- Voxtral (Mistral) 
- Qwen 2 Audio 
- Qwen Omni 
- Microsoft Phi 4 Multimodal 

For a more complete list, see [here](https://github.com/danielrosehill/Audio-Multimodal-AI-Resources).

---

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
