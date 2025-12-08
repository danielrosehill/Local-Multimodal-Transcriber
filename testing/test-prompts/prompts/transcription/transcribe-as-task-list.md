# Transcribe as Task List

**Tests:** Format transformation, action item extraction, priority inference, deadline identification

---

Listen to this audio recording and convert its content into an actionable task list.

Transform the spoken content into task list format:

## Task List Structure

### High Priority / Urgent
- [ ] Task description
  - Due: [date if mentioned]
  - Context: [brief note if needed]

### Medium Priority
- [ ] Task description
  - Due: [date if mentioned]
  - Context: [brief note if needed]

### Low Priority / Someday
- [ ] Task description
  - Context: [brief note if needed]

### Waiting On (blocked/dependent tasks)
- [ ] Task description
  - Waiting for: [person/event]

## Formatting rules:

1. **Actionable language**: Start each task with a verb (Call, Email, Review, Complete, Buy, Schedule, etc.)

2. **Specificity**: Include enough detail to act without remembering context
   - Bad: "Handle the thing with John"
   - Good: "Email John re: Q4 budget approval"

3. **Deadlines**: Extract and note any mentioned due dates or timeframes

4. **Dependencies**: Note if tasks must happen in sequence or are blocked

5. **Context tags**: Add helpful context like @phone, @computer, @errands, @home if inferable

Preserve:
- All tasks and action items mentioned
- Specific deadlines and time constraints
- People involved or responsible
- The speaker's sense of priority and urgency

Adapt:
- Vague intentions to concrete tasks
- "I should probably..." to actionable items
- Rambling context to brief task notes
- Implied priorities to explicit categorization

The result should be immediately usable as a working task list.
