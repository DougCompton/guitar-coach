# Spaced Repetition Review Schedule Prompt

**Replaces:** `scripts/spaced_repetition_plan.py`

**Purpose:** Generate an adaptive review schedule for a learned skill — intervals based on skill type, difficulty, and recent performance rather than fixed 2/7/14/30 days.

**Data required before calling this prompt:**
- Skill name and start date (from CLI or user)
- Skill category and difficulty from roadmap
- Most recent performance quality (from last log entry or user input)

---

## Prompt

```
You are designing a custom spaced repetition schedule for a guitar student.

## Skill Details
- Skill: {{skill_name}}
- Category: {{skill_category}} (chord technique / picking pattern / fingerstyle / theory / rhythm)
- Difficulty: {{difficulty}}/5
- First practiced: {{first_practiced_date}}
- Most recent attempt: {{last_attempt_date}}, result: {{last_result}} (perfect / good / shaky / incomplete)
- Prior reviews completed: {{review_count}}
- Used in songs: {{song_list}}

## Interval Guidelines
Adjust base intervals based on:
- **Skill category:** Technical skills (chord shapes, picking) need shorter intervals (2, 5, 12, 28 days). Theory/conceptual skills can go longer (7, 14, 30, 60 days).
- **Recent performance:** If shaky → compress intervals. If perfect → extend them by 25–50%.
- **Prior reviews:** First time through → shorter intervals. After 3+ successful reviews → extend significantly.

Design a schedule with 4–5 review dates:

For each review date, provide:
- **Date** (absolute, not relative)
- **Warm-up:** What to practice for 2 min before the review to prime the skill
- **Readiness test:** A specific mini-win that confirms the skill is retained (not vague — exact criterion)
- **If weaker than expected:** What to do (drop back one interval and repeat, or drill a specific sub-component)

Also recommend:
- **One parallel skill** to review on the same days (a related skill that reinforces this one)
- **Songs to test in:** Which song from the student's repertoire is the best place to test this skill in context

Output as a dated review calendar with all details per session.

**Progression note:** If the skill remains shaky after the second review, suggest a specific remedial drill or prerequisite skill to work on first.
```
