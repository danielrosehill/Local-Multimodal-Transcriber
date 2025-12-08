FROM rocm/pytorch:rocm6.4.4_ubuntu24.04_py3.12_pytorch_release_2.7.1

# Set ROCm environment for gfx1101 (Navi 32)
ENV HSA_OVERRIDE_GFX_VERSION=11.0.1
ENV PYTORCH_ROCM_ARCH=gfx1101

WORKDIR /app

# Install dependencies (torchvision already in base image)
RUN pip install --no-cache-dir \
    "transformers>=4.54.0" \
    accelerate \
    soundfile \
    librosa \
    "mistral-common[audio]>=1.8.1"

# Pre-download model (optional - comment out for faster builds during dev)
# RUN python -c "from transformers import AutoModel, AutoProcessor; \
#     AutoProcessor.from_pretrained('mistralai/Voxtral-Mini-3B-2507'); \
#     AutoModel.from_pretrained('mistralai/Voxtral-Mini-3B-2507', torch_dtype='auto')"

COPY . /app

CMD ["python", "test/test_voxtral.py"]
