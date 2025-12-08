# JSON Transcript with Metadata

**Tests:** Structured output generation, metadata extraction, schema compliance

---

Transcribe this audio and return the result as a JSON object with metadata.

## Required Output Format

```json
{
  "transcript": {
    "text": "Full cleaned transcript text here",
    "word_count": 150,
    "duration_estimate": "2:30"
  },
  "speakers": {
    "count": 2,
    "identified": ["Speaker 1", "Speaker 2"]
  },
  "language": {
    "primary": "en",
    "confidence": 0.95,
    "other_detected": []
  },
  "audio_quality": {
    "rating": "good",
    "issues": []
  },
  "content": {
    "type": "conversation",
    "topics": ["topic1", "topic2"],
    "sentiment": "neutral"
  },
  "metadata": {
    "transcription_notes": "Any relevant notes about the transcription"
  }
}
```

## Field Requirements

1. **transcript.text**: Cleaned transcript, filler words removed
2. **transcript.word_count**: Approximate word count
3. **transcript.duration_estimate**: Estimated audio length
4. **speakers.count**: Number of distinct voices
5. **speakers.identified**: Labels for each speaker
6. **language.primary**: ISO 639-1 code
7. **language.confidence**: 0.0 to 1.0
8. **audio_quality.rating**: "excellent", "good", "fair", "poor"
9. **audio_quality.issues**: Array of issues (e.g., "background noise", "echo")
10. **content.type**: "monologue", "conversation", "presentation", "interview", etc.
11. **content.topics**: Main topics discussed
12. **content.sentiment**: "positive", "negative", "neutral", "mixed"

Return ONLY valid JSON, no additional text.
