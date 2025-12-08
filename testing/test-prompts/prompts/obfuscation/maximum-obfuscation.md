# Maximum Obfuscation Transcript

**Tests:** PII detection, entity recognition, contextual anonymization, semantic preservation under redaction

---

Transcribe this audio recording with maximum privacy obfuscation. Replace all potentially identifying information with generic placeholders.

## Obfuscation Requirements

### People
- All person names → [PERSON_1], [PERSON_2], etc.
- Job titles → [JOB_TITLE]
- Relationships → [RELATIVE], [COLLEAGUE], etc.

### Organizations
- Company names → [COMPANY_1], [COMPANY_2], etc.
- Institution names → [INSTITUTION]
- Team/department names → [DEPARTMENT]

### Locations
- Cities → [CITY]
- Countries → [COUNTRY]
- Addresses → [ADDRESS]
- Specific places (restaurants, stores) → [LOCATION]

### Dates & Times
- Specific dates → [DATE]
- Years → [YEAR]
- Specific times → [TIME]
- Days of week → [DAY]

### Contact Information
- Phone numbers → [PHONE]
- Email addresses → [EMAIL]
- Social media handles → [HANDLE]
- Websites → [URL]

### Financial
- Monetary amounts → [AMOUNT]
- Account numbers → [ACCOUNT]
- Transaction details → [TRANSACTION]

### Identifiers
- ID numbers → [ID]
- License plates → [PLATE]
- Case/ticket numbers → [REFERENCE]

### Other Sensitive Data
- Medical information → [MEDICAL]
- Legal details → [LEGAL]
- Proprietary terms/products → [PRODUCT]

## Guidelines

1. **Consistency**: Use incrementing numbers for repeated entities of same type (PERSON_1, PERSON_2).

2. **Context preservation**: The transcript should remain coherent and understandable despite redactions.

3. **Clean up**: Remove filler words during transcription.

4. **Err on the side of caution**: If uncertain whether something is identifying, obfuscate it.

The result should be a readable transcript with no personally identifiable or sensitive information exposed.
