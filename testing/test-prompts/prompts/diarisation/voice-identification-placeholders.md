# Voice Identification with Placeholder Names

**Tests:** Speaker diarization, voice characterization, creative naming, consistent speaker tracking

---

Analyze this audio recording to identify all unique voices, characterize each one, and assign a contextually appropriate placeholder name for use in transcription.

## Analysis Requirements

### Voice Identification
1. Count all distinct speakers
2. Characterize each voice (gender, age range, tone)
3. Assign a placeholder name that reflects the voice characteristics or apparent role

### Naming Guidelines
Choose placeholder names that are:
- **Descriptive**: Reflect voice qualities or role (e.g., "Alex" for ambiguous gender, "Professor" for academic tone)
- **Distinct**: Easy to tell apart when reading a transcript
- **Neutral**: Not stereotyping based on voice characteristics
- **Memorable**: Help readers track who's who

### Suggested Naming Conventions

**By apparent role** (if discernible):
- Host, Guest, Interviewer, Caller, Narrator, Moderator

**By voice characteristic**:
- Use names that loosely match perceived characteristics
- Deep male voice: "Marcus", "James"
- High female voice: "Elena", "Sophie"
- Older voice: "Robert", "Margaret"
- Younger voice: "Jordan", "Casey"

**Neutral options**:
- Speaker A, Speaker B (if characteristics unclear)
- Alpha, Bravo (phonetic alphabet)
- Voice 1, Voice 2 (purely numeric)

### Output Format

```
Speakers Identified: N

Suggested Speaker Labels:

1. "[Placeholder Name]"
   - Voice: [Male/Female/Indeterminate], [age range]
   - Characteristics: [brief description]
   - Naming rationale: [why this name fits]

2. "[Placeholder Name]"
   - Voice: [description]
   - Characteristics: [description]
   - Naming rationale: [explanation]

...

Ready for diarized transcription using these labels.
```

## Guidelines

1. **Consistency**: Once assigned, the same voice always gets the same name.

2. **Cultural sensitivity**: Avoid names that stereotype based on accent or speech patterns.

3. **Practical utility**: Names should make the transcript easy to follow.

4. **Confidence notes**: If two voices are hard to distinguish, flag this.

The result should provide a ready-to-use speaker labeling scheme for transcription.
