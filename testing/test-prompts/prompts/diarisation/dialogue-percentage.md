# Dialogue Percentage Analysis

**Tests:** Speaker diarization, speech duration estimation, proportional calculation, multi-speaker tracking

---

Analyze this audio recording and compute the approximate percentage of dialogue spoken by each participant.

## Analysis Requirements

### Speaker Identification
First, identify all distinct speakers in the recording by voice characteristics.

### Percentage Calculation
For each identified speaker, estimate:
- Approximate percentage of total speech time
- Relative contribution to the conversation

### Output Format

```
Speaker Analysis:
- Speaker 1 [description]: ~XX%
- Speaker 2 [description]: ~XX%
- Speaker 3 [description]: ~XX%

Total speakers: N
Dominant speaker: [Speaker N]
Most balanced exchange between: [Speaker X and Speaker Y]
```

### Metrics to Include

1. **Raw percentages**: Approximate speaking time per speaker
2. **Dominance indicator**: Which speaker talked most
3. **Balance assessment**: Was the conversation balanced or one-sided?
4. **Silence/pause estimation**: Approximate percentage of non-speech time (if significant)

## Guidelines

1. **Overlapping speech**: If speakers talk over each other, note this and explain how it was handled in the calculation.

2. **Brief interjections**: Include acknowledgments ("mm-hmm", "yeah") in the count for that speaker.

3. **Accuracy caveat**: Note that percentages are estimates based on audio analysis, not precise measurements.

4. **Multiple speakers**: If more than 2 speakers, provide individual percentages and note any groupings or coalitions in the conversation.

The result should give a clear quantitative picture of who dominated the conversation and how balanced the dialogue was.
