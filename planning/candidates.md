# Model Candidates for Local Multimodal Transcription

This document evaluates potential models for the local multimodal transcriber project, focusing on 12GB VRAM constraint and AMD ROCm compatibility.

**HF Collection**: [danielrosehill/audio-multimodal-models](https://huggingface.co/collections/danielrosehill/audio-multimodal-models)

## Quick Summary (12GB VRAM Constraint)

| Model | Params | VRAM (BF16) | Max Audio | Fits? | Priority |
|-------|--------|-------------|-----------|-------|----------|
| Voxtral-Mini-3B | 3B | ~9.5GB | 30 min | Yes | 1st |
| Ultravox v0.5 1B | 1B | ~2GB | TBD | Yes | 3rd |
| Phi-4-Multimodal | 6B | ~12GB | TBD | Tight | 4th |
| Kimi-Audio-7B | 10B | TBD | TBD | Test needed | 2nd |
| Qwen2-Audio-7B | 8B | ~17GB | 30 sec | Needs quant | 5th |

## Approach Comparison

| Approach | Description | Pros | Cons |
|----------|-------------|------|------|
| **True Multimodal** | Single model understands audio + follows text prompts | Clean single-pass, natural cleanup | Larger models, newer/less tested |
| **ASR + LLM Pipeline** | Whisper → Small LLM for cleanup | Proven tech, more options | Two models, more complexity |

---

## Priority Candidates (Fits 12GB VRAM)

### 1. Voxtral-Mini-3B (TOP CANDIDATE)

**Source**: [mistralai/Voxtral-Mini-3B-2507](https://huggingface.co/mistralai/Voxtral-Mini-3B-2507)

- **Parameters**: 3B (built on Ministral 3B backbone)
- **VRAM**: ~9.5GB (BF16) — **fits with headroom**
- **Max Audio**: 30 min transcription, 40 min understanding
- **Context**: 32K tokens
- **License**: Apache 2.0

**Assessment**:
- Best fit for our constraints — small enough to run comfortably
- Long audio support (30 min) far exceeds our 5-10 min target
- Dedicated transcription mode with temperature=0.0
- 8 languages with auto-detection
- Note: System prompts not yet supported — cleanup instructions go in user prompt
- Note: ROCm not explicitly tested, but uses Transformers (should work)

**Test Priority**: 1st

---

### 2. Kimi-Audio-7B-Instruct

**Source**: [moonshotai/Kimi-Audio-7B-Instruct](https://huggingface.co/moonshotai/Kimi-Audio-7B-Instruct)

- **Parameters**: 10B (per HF metadata)
- **VRAM**: TBD — may need quantization for 12GB
- **Architecture**: Audio-Text-to-Text
- **License**: TBD

**Assessment**:
- From Moonshot AI (Kimi team)
- Instruct-tuned — good for following cleanup prompts
- Needs VRAM testing to confirm viability

**Test Priority**: 2nd (after confirming VRAM)

---

### 3. Ultravox v0.5 (Llama 3.2 1B)

**Source**: [fixie-ai/ultravox-v0_5-llama-3_2-1b](https://huggingface.co/fixie-ai/ultravox-v0_5-llama-3_2-1b)

- **Parameters**: ~1B
- **VRAM**: Very low — **easily fits**
- **Latency**: ~150ms TTFT (optimized for real-time)
- **License**: MIT

**Assessment**:
- Extremely lightweight — will definitely run
- Optimized for real-time voice, not batch transcription
- May lack capability for quality cleanup transcription
- Worth testing as a baseline

**Test Priority**: 3rd (quick test as baseline)

---

### 4. Phi-4-Multimodal-Instruct

**Source**: [microsoft/Phi-4-multimodal-instruct](https://huggingface.co/microsoft/Phi-4-multimodal-instruct)

- **Parameters**: 6B
- **VRAM**: ~12GB FP16 (tight fit), ~6-8GB quantized
- **Architecture**: ASR-focused multimodal
- **License**: MIT

**Assessment**:
- Microsoft's efficient multimodal approach
- Classified as ASR on HF — may be more transcription-focused
- MIT license is very permissive
- Tight VRAM fit — may need quantization

**Test Priority**: 4th

---

## Secondary Candidates (May Need Quantization)

### 5. Qwen2-Audio-7B

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

1. **Voxtral-Mini-3B** — best VRAM fit, 30min audio, dedicated transcription mode
2. **Kimi-Audio-7B-Instruct** — if VRAM allows, strong instruct-following
3. **Ultravox v0.5 1B** — quick baseline test (very small)
4. **Phi-4-Multimodal** — Microsoft's efficient approach
5. **Qwen2-Audio-7B** (4-bit quantized) — if above don't satisfy, test quantized
6. **faster-whisper + Phi-3-mini** — pipeline fallback if multimodal fails

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
