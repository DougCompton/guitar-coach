# Progression Rules

Use this file when deciding whether the user should advance, repeat, or simplify.

## Decision order

1. Check for pain or excessive tension first.
2. Check whether the task is repeatable, not just occasionally successful.
3. Check whether the user can perform it with controlled rhythm.
4. Check confidence and consistency across multiple days.
5. Only then recommend advancement.

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

## Simplification menu

When a task is too hard, choose one simplification:

- halve the tempo
- shrink the phrase to two beats or one bar
- use fewer chords
- isolate fretting hand only
- isolate strumming hand only
- clap or count before playing
- switch from full speed song play to looped micro-practice

## Tempo-based milestones

For chord changes, scales, strumming, riffs, and songs with a target groove, prefer measurable BPM milestones.

Suggested rule:
- choose a clean starting BPM
- move up in small steps
- require at least 3 clean reps before advancing to the next rung
- do not count a rep as clean if rhythm breaks, notes buzz badly, or tension spikes

Use `scripts/tempo_ladder.py` to build the ladder.

## Spaced repetition schedule

After a lesson becomes playable, keep it alive with review passes at +2, +7, +14, and +30 days.

Use `scripts/spaced_repetition_plan.py` when the user wants concrete dates.

