# Topic Segmentation

**Tests:** Topic boundary detection, thematic analysis, conversation structure mapping

---

Listen to this audio recording and segment it by topic, identifying when the conversation shifts focus.

## Segmentation Requirements

### Identify
- Major topic shifts
- Sub-topic explorations within major topics
- Transitions between topics (smooth vs abrupt)
- Topic returns (when conversation circles back)

### Output Format

```
TOPIC SEGMENTATION:

Segment 1: [Topic Title]
- Approximate timeframe: [Start] - [End] (or % of recording)
- Key points discussed:
  - Point 1
  - Point 2
- Speakers involved: [Who participated in this segment]

Segment 2: [Topic Title]
- Approximate timeframe: [Range]
- Key points discussed:
  - Point 1
  - Point 2
- Speakers involved: [Speakers]
- Transition type: [How the topic shifted - natural flow / abrupt change / callback]

...

TOPIC MAP:
1. [Topic A] → 2. [Topic B] → 3. [Topic C] → 4. [Return to A]

DOMINANT TOPICS:
- Most time spent on: [Topic]
- Most speakers engaged: [Topic]
```

## Guidelines

1. **Granularity**: Balance between too broad (one segment) and too granular (every sentence).

2. **Natural breaks**: Look for transition phrases, pauses, or explicit topic changes.

3. **Nested topics**: A discussion of "budget" might be a sub-topic of "project planning."

4. **Tangents**: Mark brief tangents that don't warrant a full segment.

5. **Unstructured conversation**: If conversation meanders, note this and do your best to identify themes.

The result should provide a structural map of the conversation's content flow.
