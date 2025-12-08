# Test Configuration

## Model

| Parameter | Value |
|-----------|-------|
| Model | `mistralai/Voxtral-Mini-3B-2507` |
| Parameters | 3B |
| Precision | BF16 |
| Context Window | 32K tokens |
| Max Audio | 30 min transcription, 40 min understanding |

## Hardware

| Component | Specification |
|-----------|---------------|
| GPU | AMD Radeon RX 7700 XT / 7800 XT |
| GPU Architecture | RDNA 3 (Navi 32, gfx1101) |
| VRAM | 12 GB |
| CPU | Intel Core i7-12700F |
| RAM | 64 GB |

## Software

| Component | Version |
|-----------|---------|
| OS | Ubuntu 25.04 |
| ROCm | 6.4.4 |
| PyTorch | 2.7.1 |
| Transformers | ≥4.54.0 |
| Docker Base | `rocm/pytorch:rocm6.4.4_ubuntu24.04_py3.12_pytorch_release_2.7.1` |

## Environment Variables

```bash
HSA_OVERRIDE_GFX_VERSION=11.0.1
PYTORCH_ROCM_ARCH=gfx1101
```

## Test Audio

| File | Duration | Description |
|------|----------|-------------|
| `concept_1min.mp3` | 60s | Voice note about multimodal transcription project |

## Baseline Performance

Based on benchmark run (2025-12-08):

| Metric | Value |
|--------|-------|
| Model load time | ~23s |
| VRAM after load | 9.36 GB |
| VRAM peak (inference) | 10.78 GB |
| Tokens/sec | ~8.4 |
| Real-time factor | 0.48x (faster than real-time) |
