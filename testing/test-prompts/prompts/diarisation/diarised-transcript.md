# Diarised Transcript (Unknown Speakers)

**Tests:** Speaker diarization, voice distinction, turn-taking detection, speaker consistency

---

Produce a diarised transcript of this audio recording, identifying and labeling each speaker based on voice analysis alone.

## Requirements

### Speaker Detection
- Identify each unique voice in the recording
- Assign consistent labels throughout (Speaker 1, Speaker 2, etc.)
- Note speaker changes accurately

### Transcript Format

```
[Speaker 1]: First utterance from speaker 1...

[Speaker 2]: Response from speaker 2...

[Speaker 1]: Speaker 1 continues...
```

### Guidelines

1. **No assumed names**: Do not guess speaker names unless explicitly stated in the audio.

2. **Consistent labeling**: Same voice = same label throughout.

3. **Overlapping speech**: If speakers talk simultaneously, indicate with:
   ```
   [Speaker 1]: Beginning of statement—
   [Speaker 2]: [overlapping] Interruption...
   [Speaker 1]: —continuation of statement
   ```

4. **Brief acknowledgments**: Include "mm-hmm", "yeah", "right" attributed to the correct speaker.

5. **Uncertain attribution**: If unsure which speaker said something:
   ```
   [Speaker ?]: Unclear attribution...
   ```

6. **Clean transcription**: Remove filler words unless they're meaningful to the exchange.

7. **Non-verbal sounds**: Note significant non-verbal sounds:
   ```
   [Speaker 1]: [laughs] That's funny...
   [Speaker 2]: [sighs] I suppose so...
   ```

The result should be a clear, attributed transcript that a reader can follow without prior knowledge of who the speakers are.
