# Contains Multiple Languages

**Tests:** Multilingual detection, code-switching identification, language boundary recognition

**Response type:** Boolean (Yes/No)

---

Does this audio recording contain speech in multiple languages spoken by the user?

Respond with only: **Yes** or **No**

Answer **Yes** if:
- The speaker switches between two or more languages during the recording
- The speaker code-switches (mixing languages within sentences or phrases)
- Distinct segments are spoken in different languages
- The speaker uses substantial phrases or sentences from multiple languages (not just isolated loanwords)

Answer **No** if:
- The entire recording is in a single language
- The only "foreign" words are common loanwords, brand names, or proper nouns integrated into the primary language
- Different speakers use different languages (this prompt focuses on a single speaker using multiple languages)
- Technical terms from another language are used but the speech is otherwise monolingual
