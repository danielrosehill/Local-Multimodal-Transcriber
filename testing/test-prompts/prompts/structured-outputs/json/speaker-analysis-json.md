# JSON Speaker Analysis

**Tests:** Multi-dimensional speaker analysis, structured demographic inference, JSON output

---

Analyze all speakers in this audio and return a detailed JSON profile for each.

## Required Output Format

```json
{
  "analysis_confidence": "high",
  "speaker_count": 2,
  "speakers": [
    {
      "id": "speaker_1",
      "demographics": {
        "gender": "male",
        "gender_confidence": 0.9,
        "age_range": "30-45",
        "age_confidence": 0.7
      },
      "voice_characteristics": {
        "pitch": "medium",
        "tone": "warm",
        "pace": "moderate",
        "energy": "animated",
        "notable_features": ["slight accent", "clear enunciation"]
      },
      "speech_patterns": {
        "filler_word_frequency": "low",
        "common_fillers": ["um"],
        "vocabulary_complexity": "moderate",
        "formality_level": "professional"
      },
      "emotional_indicators": {
        "overall_sentiment": "positive",
        "confidence_level": "high",
        "stress_indicators": false,
        "engagement_level": "high"
      },
      "role_inference": {
        "likely_role": "interviewer",
        "role_confidence": 0.8
      },
      "speaking_stats": {
        "turn_count": 10,
        "estimated_word_count": 450,
        "speaking_percentage": 55,
        "average_turn_length": "medium"
      }
    }
  ],
  "interaction_dynamics": {
    "dominant_speaker": "speaker_1",
    "conversation_balance": "slightly_unbalanced",
    "interruptions_detected": 2,
    "rapport_level": "good"
  }
}
```

## Field Requirements

All numeric confidence values should be between 0.0 and 1.0.

Return ONLY valid JSON, no additional text.
