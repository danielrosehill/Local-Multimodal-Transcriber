# JSON Diarised Transcript

**Tests:** Structured diarization output, turn-level segmentation, JSON schema compliance

---

Produce a diarised transcript of this audio in JSON format with speaker turns as separate objects.

## Required Output Format

```json
{
  "speakers": [
    {
      "id": "speaker_1",
      "description": "Male voice, appears to be the host",
      "turn_count": 5,
      "estimated_speaking_percentage": 60
    },
    {
      "id": "speaker_2",
      "description": "Female voice, appears to be the guest",
      "turn_count": 4,
      "estimated_speaking_percentage": 40
    }
  ],
  "turns": [
    {
      "speaker": "speaker_1",
      "text": "First utterance from speaker 1",
      "turn_number": 1
    },
    {
      "speaker": "speaker_2",
      "text": "Response from speaker 2",
      "turn_number": 2
    }
  ],
  "metadata": {
    "total_turns": 9,
    "overlapping_speech_detected": false,
    "transcription_confidence": "high"
  }
}
```

## Field Requirements

1. **speakers**: Array of speaker objects with:
   - `id`: Unique identifier (speaker_1, speaker_2, etc.)
   - `description`: Brief voice description
   - `turn_count`: Number of speaking turns
   - `estimated_speaking_percentage`: Approximate % of dialogue

2. **turns**: Array of turn objects in chronological order with:
   - `speaker`: References speaker id
   - `text`: Cleaned transcript of that turn
   - `turn_number`: Sequential number

3. **metadata**: Object with:
   - `total_turns`: Sum of all turns
   - `overlapping_speech_detected`: Boolean
   - `transcription_confidence`: "high", "medium", "low"

Return ONLY valid JSON, no additional text.
