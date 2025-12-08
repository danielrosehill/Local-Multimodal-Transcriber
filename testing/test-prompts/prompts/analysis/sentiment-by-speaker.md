# Sentiment Analysis by Speaker

**Tests:** Per-speaker sentiment tracking, emotional trajectory, comparative tone analysis

---

Analyze this audio recording and provide sentiment analysis for each speaker throughout the conversation.

## Analysis Requirements

### For Each Speaker
- Overall sentiment: Positive / Negative / Neutral / Mixed
- Sentiment trajectory: Did it change during the conversation?
- Peak moments: Most positive and most negative points
- Tone indicators: What vocal/verbal cues informed the assessment?

### Output Format

```
SENTIMENT ANALYSIS BY SPEAKER:

[Speaker 1]:
- Overall sentiment: [Positive/Negative/Neutral/Mixed]
- Confidence: [High/Medium/Low]
- Trajectory: [Stable / Improving / Declining / Variable]
- Sentiment breakdown:
  - Beginning: [sentiment]
  - Middle: [sentiment]
  - End: [sentiment]
- Peak positive moment: "[Quote or description]"
- Peak negative moment: "[Quote or description]"
- Key indicators: [What cues informed this analysis]

[Speaker 2]:
[Same format]

...

COMPARATIVE ANALYSIS:
- Most positive speaker: [Speaker]
- Most negative speaker: [Speaker]
- Greatest sentiment shift: [Speaker] - [Description]
- Sentiment alignment: [Did speakers' sentiments align or diverge?]

CONVERSATION SENTIMENT:
- Overall tone: [Assessment of conversation as a whole]
- Tension points: [Any moments of conflicting sentiment]
- Resolution: [How did the conversation end emotionally?]
```

## Guidelines

1. **Multi-modal cues**: Consider both what is said (content) and how it's said (tone, pace, volume).

2. **Context sensitivity**: Sarcasm, irony, and cultural factors affect interpretation.

3. **Objective framing**: Report sentiment without judging whether feelings are justified.

4. **Nuance**: "Frustrated but professional" is more useful than just "negative."

5. **Uncertainty**: Flag when sentiment is ambiguous or hard to determine.

The result should reveal the emotional dynamics of the conversation.
