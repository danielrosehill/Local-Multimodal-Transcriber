# Voice Count and Description

**Tests:** Speaker counting, voice characterization, acoustic feature analysis, demographic inference from voice

---

Analyze this audio recording to identify how many unique voices are present and provide a description for each.

## Analysis Requirements

### Voice Count
Determine the exact number of distinct speakers in the recording.

### Voice Descriptions
For each unique voice detected, provide:

1. **Apparent gender**: Male / Female / Indeterminate
2. **Apparent age range**: Child / Young adult / Middle-aged / Older adult
3. **Voice characteristics**:
   - Pitch: High / Medium / Low
   - Tone: Warm / Neutral / Sharp / Gravelly / Smooth
   - Pace: Fast / Moderate / Slow
   - Energy: Animated / Calm / Monotone
4. **Distinctive features**: Any notable accent, speech patterns, or vocal qualities
5. **Role inference** (if apparent): Host / Guest / Interviewer / Participant / etc.

### Output Format

```
Total unique voices detected: N

Voice 1:
- Gender: [Male/Female/Indeterminate]
- Estimated age: [range]
- Pitch: [High/Medium/Low]
- Tone: [description]
- Pace: [Fast/Moderate/Slow]
- Notable features: [any distinctive characteristics]
- Apparent role: [if determinable]

Voice 2:
[Same format]

...
```

## Guidelines

1. **Confidence indication**: If uncertain about any characteristic, indicate confidence level.

2. **Similar voices**: If voices are similar and difficult to distinguish, note this explicitly.

3. **Brief appearances**: Include voices that appear only briefly if they are distinct.

4. **Background voices**: Note if there are indistinct background voices that couldn't be characterized.

5. **Non-speech vocalizations**: If there are laughs, sighs, or other vocalizations that help characterize a voice, mention them.

The result should provide a clear "cast of characters" for the audio based purely on voice analysis.
