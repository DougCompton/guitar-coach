# Daily Session Plan Prompt

**Data flow:** Run `analyze_logs.py --folder PATH --logs 7` + `readiness_check.py` + read active roadmap file + read `repertoire.md` directly → then read this prompt

**Purpose:** Build a complete, personalized daily practice plan by reading the roadmap, repertoire, and recent log history — adapting structure to readiness and weak spots.

**Data required before calling this prompt:**
- Output of `analyze_logs.py --folder PATH --logs 7` (recent session summaries and issue tags)
- Active roadmap file read directly (for current lesson, lesson goal, lesson application, next lesson)
- `repertoire.md` read directly (for learning / polishing / maintenance songs)
- Session type from `readiness_check.py` output

---

## Prompt

```
You are a guitar coach creating today's practice plan.

## Student Context
- Roadmap: {{roadmap_name}}
- Current lesson: Lesson {{lesson_number}} — {{lesson_title}}
- Lesson goal: {{lesson_goal}}
- Lesson application: {{lesson_application}}
- Next lesson (for context): {{next_lesson_title}}

## Repertoire
- Learning: {{learning_song}}
- Polishing: {{polishing_song}}
- Maintenance: {{maintenance_song}}

## Readiness
- Energy: {{energy}}/4
- Focus: {{focus}}/4
- Tension: {{tension}}/4
- Pain: {{pain}}/4
- Session type: {{session_type}}
- Session goal: {{session_goal}} (mastery / maintenance / confidence / habit-preservation)
- Total time: {{minutes}} minutes

## Recent Weak Spots (last 8 sessions)
{{weak_spots_with_frequency_and_context}}

## Last 3 Session Summaries
{{recent_log_summaries}}

Design today's session:

1. **Assess the time:** Is {{minutes}} minutes realistic given today's readiness? If not, suggest a cut and justify it.

2. **Address the top weak spot first** (when focus is highest — usually after warm-up):
   - Identify the root cause from the log evidence, not just the keyword
   - Suggest a drill that addresses the root cause, not just the symptom
   - Duration: enough to make progress but not so long it dominates the session

3. **Structure sections** in this priority order (adjust based on session type):
   - Warm-up (always, even if short)
   - Weak-spot drill (while focus is high)
   - Lesson focus (core of the session)
   - Repertoire (one song — choose based on session goal)
   - Theory/fretboard (optional, only if time and energy allow)
   - Reflection (always, even if brief)

4. **For each section provide:**
   - Section name and duration
   - Exactly what to practice (reference the specific lesson or issue)
   - Mini-win target (concrete, measurable, achievable in the time)
   - One pivot if the section isn't working

5. **End with 2–3 reflection questions** targeted at today's specific lesson and goals

Output as a structured session plan ready to follow immediately.
```
