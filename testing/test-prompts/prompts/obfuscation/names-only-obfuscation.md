# Names-Only Obfuscation Transcript

**Tests:** Person name detection, entity consistency, minimal redaction with coherence preservation

---

Transcribe this audio recording with only person names obfuscated. Replace all mentioned names of people with placeholder values while preserving all other details.

## Obfuscation Requirements

### What to Obfuscate
- First names
- Last names
- Full names
- Nicknames and diminutives
- Titles with names (Dr. Smith → Dr. [PERSON_1])

### Placeholder Format
- Use [PERSON_1], [PERSON_2], [PERSON_3], etc.
- Maintain consistency: the same person always gets the same placeholder
- If a speaker refers to themselves by name, obfuscate it the same way

### What to Preserve
- All locations
- All dates and times
- All organizations and companies
- All other identifying information
- Context and meaning

## Guidelines

1. **Consistency tracking**: Keep track of which placeholder maps to which person throughout the transcript.

2. **Relationship preservation**: If relationships are mentioned ("my brother John"), preserve the relationship ("my brother [PERSON_1]").

3. **Pronoun handling**: Do NOT replace pronouns (he, she, they). Only replace actual names.

4. **Clean up**: Remove filler words during transcription.

5. **Ambiguous names**: Names that could also be common words (e.g., "Rose" the flower vs "Rose" the person) should be determined by context.

The result should be a readable transcript where only person names have been redacted.
