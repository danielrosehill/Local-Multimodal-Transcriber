# Location Obfuscation Transcript

**Tests:** Geographic entity detection, location hierarchy understanding, place name recognition

---

Transcribe this audio recording with all location references obfuscated while preserving all other details.

## Obfuscation Requirements

### What to Obfuscate
- City names → [CITY_1], [CITY_2], etc.
- Country names → [COUNTRY_1], [COUNTRY_2], etc.
- Street addresses → [ADDRESS]
- Neighborhoods → [NEIGHBORHOOD]
- Specific venues (restaurants, stores, landmarks) → [VENUE_1], [VENUE_2], etc.
- Geographic features (rivers, mountains) → [GEOGRAPHIC_FEATURE]
- Regions/states/provinces → [REGION]

### Placeholder Format
- Use incrementing numbers for each category
- Maintain consistency: same location always gets same placeholder
- Preserve hierarchical relationships where mentioned

### What to Preserve
- All person names
- All dates and times
- All organizations (unless the org name reveals location, e.g., "Bank of [CITY]")
- Directional/relative references ("downtown", "the office")

## Guidelines

1. **Consistency**: Same place = same placeholder throughout.

2. **Generic terms**: Keep generic terms like "the city", "downtown", "abroad" as-is.

3. **Embedded locations**: Handle location names embedded in other entities:
   - "New York Times" → "[CITY] Times"
   - "University of Michigan" → "University of [REGION]"

4. **Clean up**: Remove filler words during transcription.

The result should be a transcript where geographic tracking is impossible.
