# cleaned-transcript

**Prompt**: `test-prompts/prompts/transcription/simple/cleaned-transcript.md`
**Audio**: `concept_1min.mp3`
**Model**: `mistralai/Voxtral-Mini-3B-2507`
**Time**: 19.5s
**Date**: 2025-12-08T12:53:21.937443

## Prompt

```
# Cleaned Transcript

**Tests:** Transcription with intelligent cleanup, grammar correction, readability optimization while preserving meaning

---

Transcribe this audio recording and clean it up for readability.

Apply the following cleanup:
- Remove all filler words and verbal disfluencies
- Fix grammatical errors and incomplete sentences
- Add proper punctuation and paragraph breaks
- Resolve false starts (use the corrected version only)
- Smooth out awkward phrasing while preserving meaning

Preserve:
- The speaker's intended meaning completely
- Key terminology and specific word choices that matter
- The speaker's voice and style where possible
- All factual content exactly as stated

Do NOT:
- Change the meaning or add information
- Over-formalize casual speech unnecessarily
- Remove meaningful repetition used for emphasis
- Alter technical terms, names, or quoted material

The result should be a polished, readable transcript that accurately represents what the speaker communicated, suitable for publication or documentation.
```

## Response

Okay, so the purpose of this voice recording is primarily to provide context data to the AI agent. And of course, if anyone happens to listen to this, another human, that would be cool. Hello, human. Hello, agent. I'm going to provide context data for what I'm trying to achieve in this repository and explain the idea and provide a sort of roadmap for the plan here. So, I've created a number of speech-to-text prototypes over the past year. And something I feel about speech transcription, having used it a lot, is that multimodal audio is, I think, where that's the way forward. Instead of providing an audio file to a speech-to-text model and then providing that transcription to a model, a large language model for cleanup, as it were, it's much easier to just upload something to a multimodal model that has audio understanding as a key capability.