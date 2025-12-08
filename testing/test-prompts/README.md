# Audio Understanding Test Prompts

A bench of test prompts designed to assist those evaluating audio multimodal or omni-modal multimodal AI models.

Covering:

- **Transcription** - Verbatim, cleaned, filler-removed, and format-transformed transcriptions
- **Grammatical transformations** - Tense changes, perspective shifts, voice conversion
- **Obfuscation** - Privacy-preserving transcription with PII redaction
- **Diarisation** - Speaker identification, voice analysis, dialogue attribution
- **Extraction** - Action items, questions, quotes, topic segmentation
- **Analysis** - Sentiment tracking, agreement detection, speaker profiling
- **Summarization** - Executive summaries, bullet points, key takeaways
- **Boolean classification** - Yes/No questions about audio content type and characteristics
- **Language identification** - ISO 639 language codes, multilingual detection
- **Accent & speaker identification** - BCP 47 tags, accent analysis, phonological patterns, demographics
- **Emotional analysis** - Mood detection, stress indicators, sarcasm/irony recognition
- **Environmental awareness** - Scene detection, background sounds, audio quality assessment
- **Speech analysis** - Pacing, turn-taking dynamics, code-switching between languages
- **Contextual understanding** - Non-verbal cues, confidence levels, acoustic scene narration
- **Structured outputs** - JSON-formatted results for programmatic use

Prompt ideas (and some prompts): human (Daniel).
Prompt authoring: Claude Code

## Prompt Categories

### Transcription (`prompts/transcription/`)
- **verbatim-transcript** - Exact word-for-word transcription including all filler words
- **filler-words-removed** - Transcription with ums, uhs, and disfluencies removed
- **cleaned-transcript** - Polished, readable transcript with grammar cleanup
- **third-person-transcript** - Transcription converted to third person

#### Format Transformations (`prompts/transcription/`)
- **transcribe-as-email** - Convert spoken content into email format
- **transcribe-as-business-email** - Formal business email format
- **transcribe-as-casual-email** - Informal/casual email format
- **transcribe-as-social-media** - Social media post format
- **transcribe-as-diary-entry** - Personal diary/journal format
- **transcribe-as-meeting-minutes** - Formal meeting minutes
- **transcribe-as-meeting-agenda** - Meeting agenda format
- **transcribe-as-grocery-list** - Grocery list extraction
- **transcribe-as-task-list** - Task/todo list format
- **transcribe-as-calendar-notes** - Calendar entry format
- **transcribe-as-note-to-self** - Personal reminder format
- **transcribe-as-technical-docs** - Technical documentation format
- **transcribe-as-github-readme** - GitHub README format
- **transcribe-as-executive-brief** - Executive briefing format

#### Stylistic Variations (`prompts/transcription/stylistic/`)
- **business-formal** - Business formal tone
- **maximum-formality** - Highly formal/official tone
- **casual-informal** - Casual conversational tone
- **heightened-emotion** - Emotionally expressive style
- **minimal-emotion** - Neutral, emotion-reduced style
- **maximum-brevity** - Ultra-concise output
- **verbose** - Expanded, detailed output
- **added-metaphors** - Metaphor-enriched style
- **persuasive** - Persuasive writing style
- **assertive** - Direct, assertive tone
- **diplomatic** - Diplomatic, tactful phrasing
- **simplified** - Simplified language
- **jargon-removed** - Technical jargon eliminated
- **shakespearean** - Shakespearean English style
- **medieval-english** - Medieval English style

#### Grammatical Transformations (`prompts/transcription/grammatical/`)
- **past-tense-third-person** - Convert to past tense, third-person narrative
- **future-tense** - Convert all statements to future tense
- **passive-voice** - Convert active voice to passive voice

### Obfuscation (`prompts/obfuscation/`)
Privacy-preserving transcription with selective redaction:
- **maximum-obfuscation** - Redact all potentially identifying information (names, places, dates, organizations, etc.)
- **names-only-obfuscation** - Redact only person names with consistent placeholders
- **location-obfuscation** - Redact only geographic/location information

### Diarisation (`prompts/diarisation/`)
Speaker identification and analysis:
- **diarise** - Basic diarised transcript with known speaker names
- **diarised-transcript** - Diarised transcript with auto-detected speaker labels
- **dialogue-percentage** - Compute speaking time percentage per speaker
- **voice-count-description** - Count unique voices and describe each
- **voice-identification-placeholders** - Identify voices and suggest contextual placeholder names

### Extraction (`prompts/extraction/`)
Content extraction from audio:
- **action-items** - Extract tasks, commitments, and follow-ups with owners/deadlines
- **questions-asked** - Extract all questions with answer tracking
- **key-quotes** - Extract significant, quotable statements
- **topic-segments** - Segment recording by topic with transition analysis

### Analysis (`prompts/analysis/`)
Deeper conversation analysis:
- **sentiment-by-speaker** - Per-speaker sentiment analysis with trajectory tracking
- **agreement-disagreement** - Map points of consensus and conflict between speakers

### Summarization (`prompts/summarization/`)
- **executive-summary** - Concise summary for busy stakeholders
- **bullet-point-summary** - Hierarchical bullet-point notes

### Boolean Classification (`prompts/structured-outputs/boolean/`)
Yes/No questions for quick audio classification:
- **is-voice-transcript** - Is this human speech intended for transcription?
- **contains-multiple-languages** - Does the speaker use multiple languages?
- **is-shopping-list** - Is this a shopping list?
- **is-grocery-list** - Is this specifically a grocery list?
- **is-dictated-email** - Is the speaker dictating an email?
- **background-noise-impeding** - Does background noise impede transcription?
- **contains-embedded-instructions** - Are there editing commands like "scratch that"?
- **contains-profanity** - Does the audio contain profanity?

### Structured JSON Outputs (`prompts/structured-outputs/json/`)
Machine-readable outputs for programmatic use:
- **transcript-with-metadata** - Full transcript with metadata in JSON format
- **diarised-json** - Diarised transcript as JSON with speaker turns
- **speaker-analysis-json** - Comprehensive speaker analysis in JSON format

### Language Identification (`prompts/language-id/`)
- **iso639-identification** - Identify language by ISO 639-1/639-3 code
- **multilingual-iso639** - Identify multiple languages with ISO 639 codes (JSON output)
- **language-codeswitching** - Detect language switching patterns

### Accent Analysis (`prompts/accent-identification/`)
- **accent-identification** - Identify speaker accent with regional specificity
- **accent-description** - Detailed accent analysis with phonetic features
- **bcp47-accent-tag** - BCP 47 language tag for accent/regional variety
- **phonological-enunciation** - Technical phonological analysis of speech patterns

### Emotion Analysis (`prompts/emotion/`)
- **guess-my-mood** - Analyze emotional state from voice
- **sarcasm-irony-detection** - Detect sarcasm and irony
- **stress-indicators** - Identify stress in speech
- **confidence-level** - Assess speaker confidence

### Speech Parameters (`prompts/pacing/`, `prompts/speaker-parameters/`)
- **speech-pacing** - Analyze speech speed and rhythm
- **wpm-estimation** - Estimate words per minute
- **gender-identification** - Identify speaker gender

### Environmental & Quality (`prompts/context-identification/`, `prompts/audio-quality/`)
- **environment-detection** - Detect recording environment
- **audio-quality-assessment** - Assess recording quality
- **acoustic-scene-narration** - Describe the audio scene
- **non-verbal-context** - Interpret non-verbal cues

### Conversation Dynamics (`prompts/turn-identification/`, `prompts/reasoning/`)
- **turn-taking-dynamics** - Analyze conversation dynamics
- **demographic-estimation** - Estimate speaker demographics
- **who-is-this** - Speaker identification

## Usage

Use these prompts with audio input to test how well a model understands audio beyond simple transcription. Each prompt is designed to test specific capabilities:

1. **Basic comprehension**: Can the model accurately transcribe?
2. **Transformation ability**: Can it transform content to different formats/styles?
3. **Privacy awareness**: Can it identify and redact sensitive information?
4. **Speaker analysis**: Can it distinguish and characterize different voices?
5. **Content extraction**: Can it identify key information (actions, questions, quotes)?
6. **Analytical reasoning**: Can it assess sentiment, detect agreement, segment topics?
7. **Structured output**: Can it produce machine-readable JSON output?
