# Weak Spot Drill Plan Prompt

**Replaces:** `scripts/weak_spot_tracker.py`

**Purpose:** Identify the most important recurring weak spots and prescribe targeted drills for the next session — not pre-written templates, but drills reasoned from the actual evidence.

**Data required before calling this prompt:**
- Run `analyze_logs.py --folder PATH --logs 10` to get the log table + session notes

---

## Prompt

```
You are a guitar coach analyzing recurring weak spots from recent practice.

## Recent Practice Logs (last 10 sessions, oldest to newest)
{{recent_log_texts}}

## Weak Spot Frequency Summary
{{weak_spots_with_counts_and_context}}
(derived from #issue/ tags, difficulty notes, tension/pain notes, and coach notes across logs)

For the top 3 weak spots, create a personalized drill plan for the next session.

For each weak spot:

1. **Understand the pattern:**
   - Is this recurring because it's genuinely unresolved, or because it's being actively drilled?
   - Is this weak spot a symptom of a deeper issue? (e.g., tension → string noise → timing issues — fix the root, not the symptom)
   - Is it a technical gap, a confidence gap, or a context gap (only happens in songs, only at tempo)?
   - Use trajectory field if present: improving / same / worse

2. **Assess severity and priority:**
   - Is this blocking progress on the current lesson or song?
   - Is it a "must fix now" or a "polish over time"?

3. **Recommend a specific drill:**
   - Exact steps (not vague)
   - Duration
   - Measurable success criterion — what "clean" looks like for this specific issue
   - Exit criterion — when to stop and move on
   - One coaching cue the student should say out loud while doing it

4. **Specify session placement:**
   - Should this go in the warm-up block, technique block, or before repertoire?
   - What order should the 3 drills go in?

Output as a structured drill plan with:
- Top 3 issues ranked by priority (not just frequency)
- Per-issue: specific drill, duration, success metric, session placement
- Integration note: which drill bridges naturally into the repertoire or lesson block
```
