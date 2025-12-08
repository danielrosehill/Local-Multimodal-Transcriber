# Questions Extraction

**Tests:** Interrogative detection, question type classification, answer tracking

---

Listen to this audio recording and extract all questions asked by any speaker.

## Extraction Requirements

### Question Types to Identify
- **Direct questions**: Explicit interrogatives ("What is..?", "How do..?")
- **Indirect questions**: Embedded questions ("I wonder if...", "Can you tell me...")
- **Rhetorical questions**: Questions not expecting answers
- **Tag questions**: Confirmations ("...isn't it?", "...right?")
- **Clarifying questions**: Requests for clarification

### Output Format

```
QUESTIONS EXTRACTED:

1. "[Exact question as asked]"
   - Speaker: [Who asked]
   - Type: [Direct/Indirect/Rhetorical/Tag/Clarifying]
   - Answered: [Yes/No/Partially]
   - Answer summary: [Brief answer if provided]

2. "[Question]"
   - Speaker: [Speaker]
   - Type: [Type]
   - Answered: [Status]
   - Answer summary: [Summary]

...

SUMMARY:
- Total questions: N
- Answered: N
- Unanswered: N
- Questions by speaker:
  - [Speaker 1]: N questions
  - [Speaker 2]: N questions
```

## Guidelines

1. **Preserve wording**: Capture questions as closely as possible to how they were asked.

2. **Track answers**: Note whether each question received an answer in the recording.

3. **Question chains**: If one question leads to follow-up questions, note the relationship.

4. **Rhetorical identification**: Mark rhetorical questions that weren't meant to be answered.

5. **Interrupted questions**: If a question was cut off, note it as incomplete.

The result should provide a complete Q&A map of the conversation.
