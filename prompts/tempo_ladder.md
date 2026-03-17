# Tempo Ladder Prompt

**Replaces:** `scripts/tempo_ladder.py`

**Purpose:** Build a progressive BPM ladder for a passage with passage-specific success criteria, micro-adjustments for known stall points, and a contingency plan — not just arithmetic steps.

**Data required before calling this prompt:**
- Output of `tempo_ladder.py --start-bpm N --target-bpm N --step N --reps N` (the computed rungs)
- Passage name and type (from user or current lesson)
- Student's current ability on this passage (from user input or recent logs)

---

## Prompt

```
You are designing a tempo ladder for a guitar student.

## Passage Details
- Passage: {{passage_name}} (e.g., "G→C chord change" or "alternate picking scale run")
- Type: {{passage_type}} (chord change / scale run / fingerstyle pattern / strumming / other)
- Current comfortable BPM: {{current_bpm}} (where the student can play it cleanly)
- Target BPM: {{target_bpm}}
- Session time for this ladder: {{minutes}} minutes

## Computed Rungs
{{tempo_ladder_output}}
(from tempo_ladder.py: start={{start_bpm}}, target={{target_bpm}}, step={{step}}, reps={{reps}})

## Context
- Student's known stall point (if any): {{stall_bpm}} BPM
- Prior sessions on this passage: {{session_count}}
- Related lesson: {{lesson_title}}

Enhance the ladder:

1. **Define "clean" for THIS passage specifically** — not a generic definition:
   - What does a clean rep sound like/feel like for {{passage_name}}?
   - Example for chord change: "all strings ring clearly within half a beat of the change, no buzzing"
   - Example for scale run: "all notes audible, no accidental muting, consistent pick attack"

2. **For each rung, add:**
   - Rest duration between reps (shorter for easy rungs, longer near the stall point)
   - One red flag to watch for at this tempo (e.g., "fingers start rushing the setup", "wrist tension increases")
   - Adjustment: if the flag appears, what to do before the next rep

3. **Micro-adjustments around the stall point:**
   - If {{stall_bpm}} is known, add 1–2 intermediate rungs in that range
   - Suggest a specific sub-phrase to isolate if the full passage stalls

4. **Fallback strategy:**
   - If stuck on a rung for 2+ attempts: drop 1–2 rungs and rebuild
   - If accuracy collapses completely: return to {{start_bpm}} and do 3 clean reps before stopping

5. **Estimated time:** Is this ladder achievable in {{minutes}} minutes? If not, suggest which rungs to skip on first pass.

Output as a complete tempo ladder with per-rung details and an estimated completion timeline.
```
