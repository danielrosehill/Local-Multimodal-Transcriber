#!/bin/bash
# Run Voxtral test container

set -e

cd "$(dirname "$0")"

# Build if needed
if [[ "$1" == "--build" ]] || [[ ! "$(docker images -q voxtral-test:latest 2>/dev/null)" ]]; then
    echo "Building container..."
    docker compose build
fi

# Create output directory
mkdir -p output

# Run options
case "${1:-test}" in
    test)
        # Run the test script
        echo "Running Voxtral test..."
        docker compose run --rm voxtral-test python test/test_voxtral.py
        ;;
    shell)
        # Interactive shell
        echo "Starting interactive shell..."
        docker compose run --rm voxtral-test bash
        ;;
    download)
        # Just download the model
        echo "Downloading Voxtral model..."
        docker compose run --rm voxtral-test python -c "
from transformers import AutoModel, AutoProcessor
print('Downloading processor...')
AutoProcessor.from_pretrained('mistralai/Voxtral-Mini-3B-2507')
print('Downloading model...')
AutoModel.from_pretrained('mistralai/Voxtral-Mini-3B-2507', torch_dtype='auto')
print('Done!')
"
        ;;
    *)
        # Custom audio file
        echo "Transcribing: $1"
        docker compose run --rm -v "$(realpath "$1"):/app/input_audio" voxtral-test \
            python test/test_voxtral.py /app/input_audio
        ;;
esac
