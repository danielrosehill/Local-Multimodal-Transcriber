#!/bin/bash
# Voxtral CLI - run test prompts against audio
# Usage:
#   ./voxtral-cli.sh list                     # List all prompt categories
#   ./voxtral-cli.sh list emotion             # List prompts in category
#   ./voxtral-cli.sh run emotion/guess-my-mood  # Run a prompt

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_DIR="$(dirname "$SCRIPT_DIR")"

# Check for Docker GPU services
check_gpu() {
    local used=$(rocm-smi --showmeminfo vram 2>/dev/null | grep "Used" | awk '{print $NF}')
    local used_gb=$((used / 1000000000))
    if [[ $used_gb -gt 3 ]]; then
        echo "Warning: ${used_gb}GB VRAM in use. You may need to stop GPU services:"
        echo "  docker stop ollama-rocm whisper-rocm"
        read -p "Continue anyway? [y/N] " -n 1 -r
        echo
        [[ $REPLY =~ ^[Yy]$ ]] || exit 1
    fi
}

cd "$REPO_DIR/app"

case "${1:-help}" in
    list)
        # List doesn't need GPU
        docker compose run --rm \
            -v "$REPO_DIR/test-prompts:/app/test-prompts:ro" \
            -v "$SCRIPT_DIR:/app/testing:ro" \
            --entrypoint python \
            voxtral-test /app/testing/run_prompt.py list ${2:-}
        ;;
    run)
        if [[ -z "$2" ]]; then
            echo "Usage: ./voxtral-cli.sh run <prompt_path> [audio_file]"
            echo "Example: ./voxtral-cli.sh run emotion/guess-my-mood"
            exit 1
        fi
        check_gpu

        PROMPT="$2"
        AUDIO="${3:-}"

        # Build mount args
        EXTRA_MOUNTS=""
        AUDIO_ARG=""
        if [[ -n "$AUDIO" ]]; then
            AUDIO_ABS="$(realpath "$AUDIO")"
            EXTRA_MOUNTS="-v $AUDIO_ABS:/app/custom_audio:ro"
            AUDIO_ARG="/app/custom_audio"
        fi

        docker compose run --rm \
            -v "$REPO_DIR/test-prompts:/app/test-prompts:ro" \
            -v "$SCRIPT_DIR:/app/testing" \
            -v "$REPO_DIR/benchmarks:/app/benchmarks" \
            $EXTRA_MOUNTS \
            --entrypoint python \
            voxtral-test /app/testing/run_prompt.py run "$PROMPT" $AUDIO_ARG
        ;;
    help|*)
        echo "Voxtral CLI - Run test prompts against audio"
        echo ""
        echo "Usage:"
        echo "  ./voxtral-cli.sh list                      # List prompt categories"
        echo "  ./voxtral-cli.sh list <category>           # List prompts in category"
        echo "  ./voxtral-cli.sh run <prompt> [audio]      # Run a prompt"
        echo ""
        echo "Examples:"
        echo "  ./voxtral-cli.sh list emotion"
        echo "  ./voxtral-cli.sh run emotion/guess-my-mood"
        echo "  ./voxtral-cli.sh run transcription/simple/verbatim ./my_audio.mp3"
        ;;
esac
