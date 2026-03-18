# Guitar Coach — Development Notes

This file tracks suggested improvements, open TODOs, and the development roadmap for the Guitar Coach skill.

---

## Already implemented

- Daily "start here" mode
- Weak-spot memory and corrective drills
- Mastery score by skill type
- Tempo-based advancement rules
- Song / repertoire lane with learning, polishing, and maintenance states
- Spaced repetition for old lessons
- Technique safety checks through readiness and reflection prompts
- Mini-win practice design
- Bad-day fallback session
- Weekly review generator
- Theory tied to playing on the instrument
- Constraint-based practice modes through readiness and coaching modes
- Reference library for tab quality
- Practice-note tags for searchability
- Audio-aware reflection prompts
- One-command practice day
- Readiness check before session
- Fix-one-thing mode
- Plateau detector
- Progress charts from markdown logs
- Left-hand / right-hand diagnostic mode
- Chord library and shape families
- Scale-to-music integration
- Repertoire performance checklist
- Random musicality prompts
- Weekly "what should change?" coach review

---

## High-priority improvements not yet implemented

These are the most impactful missing features. Implement these first.

### Chord-change drill generator
Generate a focused, timed drill specifically for the hardest chord transitions in the current lesson. Should integrate with `chord_library.py` and `tempo_ladder.py` and be callable from the session plan builder. The drill should isolate the two-chord pair, set a slow BPM starting point, and define a clean-reps success target.

### Micro-loop generator
Break a hard passage into the smallest playable chunk (2 to 4 notes or beats) and build back out. Should be triggerable from any section when the user reports frequent mistakes on a specific spot. Integrates with `fix_one_thing.py` and `tempo_ladder.py`.

### Log summarizer (7-day lightweight)
A lighter-weight complement to `weekly_review.py` — a quick scan of the last 7 daily files that outputs: current lesson, top weak spot, how many sessions were completed, and the most recent repeat/simplify/advance call. Intended for the start of any session, not just the weekly review.

### Frustration detector
Detect overload signals from reflection answers (e.g., Q1 = 4 "Too hard" or Q4 = 4 "Pain" appearing two or more times in one session) and automatically trigger a `bad_day_session.py` or `fix_one_thing.py` recommendation. Currently the coach waits for the user to ask.

### Session variety control
Support named day types that shape the session structure:
- `technique` — prioritize finger exercises, scales, and drills
- `repertoire` — prioritize song practice in all three lane states
- `theory` — dedicate 40%+ of time to fretboard knowledge, intervals, and ear training
- `recovery` — short warmup + one easy win, nothing challenging
- `creative` — mostly musicality prompts, improv, and scale-to-music blocks

Triggerable via `practice_day.py --day-type <type>` and by user request.

### Technique prerequisite map
Before advancing, check whether the prerequisite skills for the next lesson are actually solid. Store a simple dependency tree in the roadmap format. Flag when the user is being moved to lesson N+1 without clean evidence on the prerequisites.

---

## Medium-priority improvements

### Micro-goal streak tracking
Track mini-win success across sessions. Show a streak count when the user lands the mini-win in consecutive sessions. Use as a motivation signal.

### Key-center training lane
A dedicated practice lane built around real musical keys. Works through common progressions, intervals, and chord families in a specific key across multiple sessions. Complements `theory-on-guitar.md` and `scale-to-music.py`.

### Fretboard navigation system
Structured lessons and drills for:
- String and fret note names
- Octave patterns
- Interval landmarks on adjacent strings
- Root-finding from chord shapes
- Triad location across all string sets

### "Show me exactly what to hear" prompts
After drills, give one targeted listening prompt: what the clean version of this skill should sound like. Sharpens aural feedback loop and complements `listen_and_reflect.py`.

### Compare planned vs. actual session analysis
Parse the daily log to compare planned section minutes versus actual minutes, and flag consistent overruns or underruns so future session plans are better calibrated.

### Adaptive difficulty engine
A unified interface that can:
- Simplify (slow tempo, fewer chords, shorter phrase)
- Isolate (one hand, one string, one beat)
- Expand back out step by step when success is confirmed

Currently simplification is described as a set of rules. This would make it an active, callable workflow.

### Lesson dependency graph
Store prerequisite, related, review, and next links per lesson in the roadmap format. Allows the coach to see whether the user's current weak spot is blocking future lessons, and to suggest targeted preparation.

### Personal technique profile
Build a rolling profile from log tags and reflection answers: what the user's tendencies are (rushing tempo, right-hand noise, left-hand tension, etc.) and use it to pre-load corrective guidance at the start of each session without requiring manual lookup.

### Performance readiness mode
Get a piece stable enough to play for someone else. Focused on:
- Full-speed run-through with no stopping
- Consistent dynamics
- Memory test (no looking at the tab)
- Recovery from small mistakes without breaking the flow

Scores readiness using `repertoire_checklist.py` and sets a clear "ready to perform" threshold.

---

## Nice-to-have future extensions

- Better song-performance preparation workflows
- More detailed hand-health and ergonomics guidance
- Deeper ear-training integration tied to current lessons
- Additional roadmap templates for more genres or playing styles
- Stronger visualization or dashboard output for long-term trends
- Genre-specific lick and riff libraries tied to roadmap tracks

---

## Known issues and maintenance notes

- `weekly_review.py` is referenced twice in SKILL.md responsibilities (items 13 and 30). These descriptions should be merged into one.
- The `agents/openai.yaml` file is a placeholder. Expand it with a proper OpenAI Actions spec if cross-platform deployment is needed.
- All scripts assume they are run with an absolute path (via `${CLAUDE_PLUGIN_ROOT}/skills/guitar-coach/scripts/`). The plugin conversion addressed this, but a `--root` flag could make standalone execution more explicit.
