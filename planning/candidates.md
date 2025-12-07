# Model Candidates for Local Multimodal Transcription

This document evaluates potential models for the local multimodal transcriber project, focusing on 12GB VRAM constraint and AMD ROCm compatibility.

## Approach Comparison

| Approach | Description | Pros | Cons |
|----------|-------------|------|------|
| **True Multimodal** | Single model understands audio + follows text prompts | Clean single-pass, natural cleanup | Larger models, newer/less tested |
| **ASR + LLM Pipeline** | Whisper → Small LLM for cleanup | Proven tech, more options | Two models, more complexity |

---

## True Multimodal Candidates

### 1. Qwen2-Audio-7B

**Source**: [Alibaba Qwen](https://github.com/QwenLM/Qwen2-Audio)

- **Architecture**: Audio encoder + LLM decoder
- **Capabilities**: Audio understanding, speech-to-text with instruction following
- **Size**: ~14GB FP16 (7B params)
- **VRAM**: ~17GB FP16, ~9-10GB quantized (4-bit)

**Assessment**:
- Native audio + text prompt input (exactly what we want)
- May fit in 12GB with 4-bit quantization
- ROCm compatibility: Likely works via transformers + PyTorch ROCm

**Risk**: Quantization may degrade cleanup quality

---

### 2. Qwen2.5-Omni-7B

**Source**: [GitHub](https://github.com/QwenLM/Qwen2.5-Omni)

- **Architecture**: "Thinker-Talker" multimodal model
- **Capabilities**: Text, images, audio, video input; text + speech output
- **Size**: 7B parameters
- **VRAM**: Similar to Qwen2-Audio, likely ~17GB FP16

**Assessment**:
- Most capable option (ranked #1 in MMSU benchmark)
- Newer, may have better audio understanding
- Same VRAM constraints as Qwen2-Audio

**Risk**: Newer model, less community testing

---

### 3. SALMONN

**Source**: [ByteDance/SALMONN](https://github.com/bytedance/SALMONN)

- **Architecture**: Dual encoder (Whisper + BEATs) → Vicuna LLM
- **Capabilities**: Speech, audio events, music understanding
- **Size**: Based on Vicuna 13B (larger) or 7B variants
- **VRAM**: 13B won't fit; 7B variant ~15-17GB FP16

**Assessment**:
- Proven architecture (Whisper encoder is excellent)
- Good for general audio understanding
- Vicuna backend is well-tested

**Risk**: May be more complex to set up; 13B variants won't fit

---

### 4. Baichuan-Omni-7B

**Source**: [Baichuan](https://www.marktechpost.com/2024/10/18/baichuan-omni-an-open-source-7b-multimodal-large-language-model-for-image-video-audio-and-text-processing/)

- **Architecture**: Multimodal (audio, images, video, text)
- **Capabilities**: Full multimodal processing
- **Size**: 7B parameters
- **VRAM**: ~14-17GB FP16

**Assessment**:
- Open source alternative to GPT-4o style models
- Less tested for pure audio transcription tasks

**Risk**: Jack of all trades, may not excel at audio specifically

---

## ASR + LLM Pipeline Candidates

If true multimodal models prove too large or unreliable, a two-stage pipeline may be more practical:

### Stage 1: ASR (Speech-to-Text)

| Model | VRAM | Speed | Notes |
|-------|------|-------|-------|
| **faster-whisper large-v3** | ~3GB | 4x faster than original | Best balance |
| **Distil-Whisper large-v2** | ~1.5GB | Fastest | Half the size, similar quality |
| **WhisperX** | <8GB | 70x realtime | Adds VAD, word timestamps |

**Recommendation**: faster-whisper with large-v3 or Distil-Whisper

### Stage 2: Cleanup LLM

| Model | VRAM (4-bit) | Notes |
|-------|--------------|-------|
| **Phi-3-mini (3.8B)** | ~3GB | Fast, good at instructions |
| **Qwen2.5-3B-Instruct** | ~3GB | Excellent instruction following |
| **Gemma-2-2B** | ~2GB | Smallest viable option |

**Combined VRAM**: ~6-8GB total, leaving headroom

---

## Feasibility Summary

### Option A: Quantized Multimodal (Ambitious)

```
Qwen2-Audio-7B (4-bit) → ~9-10GB VRAM
```
- Single inference pass
- Requires testing quantized quality
- Clean architecture

### Option B: ASR + Small LLM (Reliable)

```
faster-whisper large-v3 (~3GB) + Phi-3-mini (~3GB) → ~6-8GB VRAM
```
- Proven components
- More VRAM headroom
- Two inference passes

### Option C: SeamlessM4T (Alternative)

```
SeamlessM4T Large (~10.7GB)
```
- Meta's multimodal translation model
- Fits in 12GB
- Primary focus is translation, not cleanup

---

## Recommended Testing Order

1. **Qwen2-Audio-7B** (GPTQ/AWQ 4-bit) — test if cleanup quality holds
2. **faster-whisper + Phi-3-mini** — fallback if multimodal degrades too much
3. **Qwen2.5-Omni-7B** — if Qwen2-Audio works, try newer model

---

## ROCm Compatibility Notes

- PyTorch ROCm container is available and working
- vLLM has ROCm support for inference
- transformers library generally works on ROCm
- May need `HSA_OVERRIDE_GFX_VERSION=11.0.1` for gfx1101 GPU

## Context Window Considerations

| Model | Context | Audio Equivalent |
|-------|---------|------------------|
| Qwen2-Audio | 32K tokens | TBD (~5-10 min?) |
| Whisper large | 30 seconds chunks | Unlimited via chunking |

Audio tokenization is dense. Testing needed to determine practical limits.

---

## Next Steps

1. [ ] Set up test environment with PyTorch ROCm
2. [ ] Download Qwen2-Audio-7B quantized
3. [ ] Create 1-minute test audio with filler words
4. [ ] Benchmark inference time and quality
5. [ ] Compare with faster-whisper + LLM pipeline
