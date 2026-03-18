# Single-Issue Repair Session Prompt

**Purpose:** Generate a focused 3-drill progression to fix one specific technique problem — diagnosing the root cause rather than applying a pre-written drill template.

**Data flow:** Run `fix_one_thing.py` first (produces drill time allocation), then run `analyze_logs.py --logs 10` (for issue history and context), then read this prompt to generate the full repair session.

**Data required before calling this prompt:**
- Output of `fix_one_thing.py` (drill time allocation)
- Output of `analyze_logs.py --logs 10` (issue history — first seen, frequency, context)
- Current lesson from roadmap

---

## Prompt

```
You are a guitar coach designing a targeted repair session for one specific problem.

## The Problem
- Issue: {{issue_type}} (e.g., buzzing, chord-transitions, rhythm, string-noise, fingerstyle, picking)
- Specific symptom: {{symptom_description}} (free text — what exactly is going wrong)
- Root cause (if known): {{root_cause}}
- Related lesson: {{lesson_title}}
- History: first seen {{first_seen_date}}, appeared {{frequency}} times in last {{n}} logs

## Session Parameters
- Total time: {{total_minutes}} minutes
- Energy: {{energy}}/4
- Tension: {{tension}}/4

## Recent Log Context
{{relevant_log_excerpts}}

Design a 3-drill progression:

**Drill 1 — Isolation** (shortest, most focused):
- Targets the root cause at its smallest useful unit
- Example: if buzzing, isolate just the pressure on one finger for one note
- Duration: approximately 1/3 of total time (minimum 2 min)
- Success criterion: 5 consecutive clean reps
- Coaching cue: one thing to say out loud while doing it

**Drill 2 — Application** (medium):
- Bridges isolation to slightly larger musical context
- Example: the one-note fix applied to a full chord shape
- Duration: approximately 1/3 of total time
- Success criterion: measurable
- Coaching cue
- Fallback: if this feels too hard, return to Drill 1

**Drill 3 — Integration** (longest, most realistic):
- Applies the fix in full musical context (the actual song or passage)
- Duration: remaining time
- Success criterion: 3 clean reps in context
- Fallback: if this breaks down, which drill to return to and why

**Time allocation note:** If the student tends to master isolation but struggle to transfer to real music, weight more time toward Drills 2 and 3. If the root cause is still fragile, keep more time in Drill 1.

**Post-drill reflection:**
Suggest 2 questions to assess whether the fix is holding:
- One about execution (did it stay clean?)
- One about feel (did something shift in how it feels to play?)
```
