# Progression Rules

Use this file when deciding whether the user should advance, repeat, or simplify.

## Decision order

1. Check for pain or excessive tension first.
2. Check whether the task is repeatable, not just occasionally successful.
3. Check whether the user can perform it with controlled rhythm.
4. Check confidence and consistency across multiple days.
5. Only then recommend advancement.

## Advance criteria

Recommend **advance** when most of these are true:

- the skill is performed cleanly at the current target speed or target tempo
- for tempo-based material, the top rung in the tempo ladder is passed with the required clean reps
- the user selects a high readiness or confidence option in at least 2 recent sessions
- the main error is occasional, not constant
- the skill remains repeatable across multiple attempts or days
- there is no meaningful pain or tension interfering with execution

## Keep practicing criteria

Recommend **keep practicing the current lesson** when any of these are true:

- mistakes are frequent or foundational
- tempo collapses when attention shifts
- chord changes or fingering remain inconsistent
- the user keeps choosing weak accuracy, timing, or readiness options repeatedly
- the skill works once but is not yet repeatable

## Simplify criteria

Recommend **simplify** when any of these are true:

- pain, strain, or excess tension appears
- the target tempo is too ambitious
- too many new variables were introduced at once
- the user cannot explain what success should sound or feel like

## Simplification menu

When a task is too hard, reduce one variable at a time:

- slower tempo
- fewer chords
- smaller chunk
- simpler strum
- shorter phrase
- fewer repetitions with better rest
- isolate fretting hand only
- isolate strumming hand only
- clap or count before playing

## Repeatable skill test

A skill is closer to learned when the user can:

- explain the goal clearly
- perform it more than once in a row
- recover after a mistake without falling apart
- keep the motion relaxed enough to continue
- produce roughly the same result across days

## Examples by topic

### Chord changes
Advance when chord switching is mostly clean at slow tempo and rhythm does not stop during the change.

### Strumming
Advance when down-up motion stays steady and the pattern survives a chord change.

### Scales and finger exercises
Advance when fingering stays consistent, notes are clear, and the user does not compensate with tension.

### Song sections
Advance when the user can play a short section musically and recover from small errors without restarting every time.

### Theory and ear training
Advance when the user answers accurately more often than not and can connect the concept to playing.

## Tempo-based milestones

For chord changes, scales, strumming, riffs, and songs with a target groove, prefer measurable BPM milestones.

Suggested rule:
- choose a clean starting BPM
- move up in small steps
- require at least 3 clean reps before advancing to the next rung
- do not count a rep as clean if rhythm breaks, notes buzz badly, or tension spikes

Use `${CLAUDE_PLUGIN_ROOT}/skills/guitar-coach/scripts/tempo_ladder.py` to build the ladder.

## Spaced repetition schedule

After a lesson becomes playable, keep it alive with review passes at +2, +7, +14, and +30 days.

Use `${CLAUDE_PLUGIN_ROOT}/skills/guitar-coach/prompts/review_schedule.md` when the user wants concrete dates — collect skill name, start date, last attempt, performance quality, and prior review count conversationally, then read that prompt to compute the schedule.