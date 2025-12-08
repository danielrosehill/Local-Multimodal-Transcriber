# Contains Embedded Instructions

**Tests:** Meta-command detection, editing instruction recognition, transcription directive identification

**Response type:** Boolean (Yes/No)

---

Does this audio message contain embedded instructions intended for editing rather than direct transcription?

Respond with only: **Yes** or **No**

Embedded instructions are verbal commands the speaker uses to control the transcription itself, such as:
- "Scratch that" / "Delete that" / "Strike that"
- "Go back and change..."
- "New paragraph" / "New line"
- "Period" / "Comma" / "Question mark" (when dictating punctuation)
- "Correction:" followed by replacement text
- "Insert [text] before/after..."
- "Spell that out" / "All caps"
- "Undo" / "Start over"

Answer **Yes** if:
- The speaker uses any verbal commands intended to modify the transcription
- There are meta-instructions about how to format or edit the text
- The speaker corrects themselves using editing language rather than just restating

Answer **No** if:
- The speaker simply restates or rephrases without editing commands
- All spoken content is intended to be transcribed as-is
- Natural speech corrections occur without explicit editing instructions
- The recording contains no transcription control language
