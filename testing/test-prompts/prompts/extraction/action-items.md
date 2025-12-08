# Action Items Extraction

**Tests:** Task identification, commitment detection, assignment parsing, deadline recognition

---

Listen to this audio recording and extract all action items, tasks, and commitments mentioned.

## Extraction Requirements

### What Constitutes an Action Item
- Explicit commitments ("I will...", "I'll send you...")
- Assigned tasks ("Can you...", "Please handle...")
- Agreed deadlines ("By Friday...", "Next week...")
- Follow-up items ("Let's revisit...", "We need to...")
- Decisions requiring action ("We decided to...")

### Output Format

```
ACTION ITEMS EXTRACTED:

1. [Action description]
   - Assignee: [Person or "Unassigned"]
   - Deadline: [Date/timeframe or "Not specified"]
   - Context: [Brief context from conversation]

2. [Action description]
   - Assignee: [Person]
   - Deadline: [Date]
   - Context: [Context]

...

SUMMARY:
- Total action items: N
- Items with clear owners: N
- Items with deadlines: N
- Unassigned items requiring follow-up: N
```

## Guidelines

1. **Implicit vs explicit**: Capture both explicit tasks and implicit commitments inferred from context.

2. **Owner identification**: If the speaker commits to something, they are the owner. If they ask someone else, that person is the owner.

3. **Deadline parsing**: Convert relative deadlines ("next Tuesday") to absolute dates if possible, otherwise preserve as stated.

4. **Duplicate handling**: If the same task is mentioned multiple times, consolidate but note if details evolved.

5. **Conditional items**: Flag action items that are conditional ("If X happens, then we need to Y").

The result should be a clear, actionable task list derived from the conversation.
