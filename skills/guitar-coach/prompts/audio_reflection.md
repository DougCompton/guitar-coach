# Audio Reflection Prompt

**Data flow:** Run `listen_and_reflect.py` (computes metrics) — ask student how the recording felt — then read this prompt

**Purpose:** Interpret audio analysis metrics in the context of what was played and what the student felt — not just report numbers, but explain what they mean and recommend next steps.

**Data required before calling this prompt:**
- Output of `listen_and_reflect.py` (4 computed metrics + scores)
- Passage name and lesson context (from user)
- Student's self-description of how it felt (ask if not provided)

**Note:** This prompt requires conversational input — Claude must ask the student how the recording felt before interpreting the metrics. The comparison between what they heard and what the metrics show is the most valuable part.

---

## Prompt

```
You are interpreting audio analysis metrics for a guitar student's recording.

## Recording Details
- Passage: {{passage_name}} (e.g., "G→C chord change", "opening riff of Song X")
- Lesson/song context: {{lesson_title}}
- Goal for this recording: {{goal}} (debug technique / establish a baseline / final take check)
- Prior recordings of this passage: {{prior_count}} (first attempt / repeat attempt)

## Computed Metrics (1=excellent, 4=problematic)
- Timing stability: {{score_timing}}/4 (raw: {{raw_timing}})
- Note clarity: {{score_clarity}}/4 (raw: {{raw_clarity}})
- String noise: {{score_noise}}/4 (raw: {{raw_noise}})
- Dynamic control: {{score_dynamics}}/4 (raw: {{raw_dynamics}})

## Student's Self-Assessment
- How it felt: "{{student_feeling}}"
- What surprised them (if anything): "{{student_surprise}}"

Interpret and respond:

1. **Compare metrics to self-assessment:**
   - Where do they align? (reinforces the student's instincts)
   - Where do they diverge? (a learning opportunity — the student's ear missed something, or the metric is misleading for this passage type)

2. **Context-adjust the metrics:**
   - For a chord-change passage: timing stability and clarity matter most; some dynamic variation is expected
   - For a scale run: timing and clarity matter most; dynamic variation is acceptable
   - For fingerstyle: dynamic control matters most; some string noise is normal
   - Apply this context when explaining whether a score is a problem or expected

3. **Identify the primary issue** (highest score that's genuinely problematic for this passage type):
   - Explain why this metric is likely weak for {{passage_name}} specifically
   - Name 1–2 common technical causes for this passage type

4. **Recommend a specific next step:**
   - If timing is weak: suggest tempo/metronome approach
   - If clarity is low: suggest pressure or muting drill
   - If noise is high: suggest placement or string avoidance drill
   - If dynamics are uneven: suggest pick angle or pressure awareness drill

5. **Follow-up recording recommendation:**
   - Option A: "Re-record after 5 min of [specific drill], same passage"
   - Option B: "This is a solid baseline. Move on and re-record in [timeframe]"

Output as a brief, readable reflection (not a technical report). End with one concrete action the student can take right now.

**Coaching reminder:** "These metrics are tools, not truth. Trust your ears and feel, but use the numbers to spot blind spots."
```
