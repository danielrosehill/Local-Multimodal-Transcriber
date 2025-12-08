# Agreement/Disagreement Detection

**Tests:** Stance detection, consensus tracking, conflict identification, negotiation dynamics

---

Analyze this audio recording to identify points of agreement and disagreement between speakers.

## Analysis Requirements

### Detect
- **Explicit agreement**: "I agree", "Exactly", "That's right"
- **Implicit agreement**: Building on others' points, supportive tone
- **Explicit disagreement**: "I disagree", "But...", "Actually..."
- **Implicit disagreement**: Counter-arguments, hedging, dismissive responses
- **Partial agreement**: "Yes, but...", "I see your point, however..."

### Output Format

```
AGREEMENT/DISAGREEMENT ANALYSIS:

POINTS OF AGREEMENT:

1. Topic: [What they agreed on]
   - Speakers: [Who agreed]
   - Type: [Explicit/Implicit]
   - Quote: "[Supporting statement]"

2. [Next agreement point]
...

POINTS OF DISAGREEMENT:

1. Topic: [What they disagreed about]
   - Speakers: [Who disagreed with whom]
   - Type: [Explicit/Implicit/Partial]
   - Position A: [Speaker]'s view - "[Summary]"
   - Position B: [Speaker]'s view - "[Summary]"
   - Resolution: [Resolved/Unresolved/Compromised]

2. [Next disagreement point]
...

CONSENSUS MAP:
- Full consensus topics: [List]
- Contested topics: [List]
- Unresolved disagreements: [List]

DYNAMICS:
- Most agreeable speaker: [Speaker]
- Most contrarian speaker: [Speaker]
- Overall alignment: [High/Medium/Low/Contentious]
```

## Guidelines

1. **Substance over politeness**: "That's interesting" may be dismissive, not agreement.

2. **Track evolution**: Note if disagreement turned to agreement (or vice versa).

3. **Power dynamics**: Consider if disagreement was suppressed due to hierarchy.

4. **Topic specificity**: Be clear about exactly what is agreed/disagreed upon.

5. **Non-verbal cues**: Sighs, pauses, tone shifts can indicate disagreement even without words.

The result should map the consensus and conflict landscape of the conversation.
