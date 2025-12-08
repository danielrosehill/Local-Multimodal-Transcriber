# Transcribe as Calendar Notes

**Tests:** Format transformation, event extraction, temporal information parsing, scheduling detail capture

---

Listen to this audio recording and convert its content into calendar entries.

Transform the spoken content into calendar-ready format:

## Calendar Entry Structure

For each event or appointment mentioned:

### Event 1
- **Title**: [Clear, concise event name]
- **Date**: [Specific date or day of week]
- **Time**: [Start time - End time, or "All day"]
- **Location**: [Physical address or virtual meeting link placeholder]
- **Description**:
  - Purpose/agenda
  - Any preparation needed
  - Related context
- **Attendees**: [Names if mentioned]
- **Reminders**: [Suggested reminder times based on event type]
- **Recurrence**: [If this is a recurring event]

---

## Additional notes:

**Tentative/Unconfirmed events**: Mark clearly as "TENTATIVE" if the speaker expressed uncertainty.

**Scheduling conflicts**: Note if the speaker mentioned potential conflicts.

**Related tasks**: List any preparation tasks that should be done before the event.

**Travel time**: Note if significant travel is required (suggest calendar blocking).

## Formatting rules:

1. **Date parsing**: Convert relative dates ("next Tuesday", "in two weeks") to actual dates if possible
2. **Time zones**: Note if different time zones are mentioned
3. **Duration**: Estimate reasonable duration if not specified
4. **Buffer time**: Note if speaker mentioned needing prep or travel time

Preserve:
- All scheduling details exactly as stated
- Specific times, dates, and durations
- Location information and dial-in details
- Names of other participants

Adapt:
- Casual time references to calendar-standard format
- Scattered event details to structured entries
- Verbal context to concise calendar descriptions

The result should be ready to create calendar events from.
