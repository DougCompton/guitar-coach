# Daily Log Template

Use this reference when creating or reviewing a daily practice log. The filename pattern is:

```
YYYY-MM-DD-guitar-practice.md       ← first session of the day
YYYY-MM-DD-guitar-practice-2.md     ← second session same day
YYYY-MM-DD-guitar-practice-3.md     ← third session same day
```

If a log already exists for today, increment the suffix (`-2`, `-3`, …). Session 1 never gets a suffix; its filename stays unchanged for backward compatibility.

---

## Writing timing

**At session START:** Create the log file and fill in only the `## Session Start` block. Leave everything else blank.

**At session END:** Append all remaining sections (Summary, Tags, Sections, Mastery Signals, Reflection, Issue Log). Then run `practice_end.py --folder <notes-folder>` to validate. Fix any reported issues before closing.

If the session is shorter, omit unused sections (e.g., Section 5, Issue Log) rather than leaving them blank.

---

## Required tags

| Tag | Rule |
|---|---|
| `#roadmap/<name>` | exactly one per log (e.g. `#roadmap/beginner`) |
| `#lesson/<slug>` | exactly one per log (e.g. `#lesson/chord-transitions`) |
| `#status/<value>` | exactly one: `repeat`, `advance`, or `simplify` |
| `#issue/<slug>` | zero or more; one per recurring issue noticed this session |
| `#review/<lesson-slug>` | add when this session is a spaced repetition review of a past lesson |

Optional skill tags: `#skill/chords`, `#skill/rhythm`, `#skill/scales`, `#skill/fingerstyle`, `#skill/repertoire`, `#skill/fretboard`

---

## Template

```markdown
# Guitar Practice Log - YYYY-MM-DD

## Session Start
- Date: YYYY-MM-DD
- Time: HH:MM
- Session type: full / low-friction / review-only / recovery / bad-day
- Session goal: mastery / maintenance / confidence / habit-preservation
- Energy (1-4):
- Focus (1-4):
- Tension (1-4):
- Pain (1-4):
- Context notes:

## Summary
- Active roadmap:
- Current lesson:
- Repertoire target:
- Practice goal:
- Total planned time:
- Total actual time:

## Tags
#roadmap/beginner #lesson/chord-transitions #issue/rhythm #status/repeat

## Section 1 - Warm-up
- Planned minutes:
- Actual minutes:
- What I practiced:
- Success target:
- Result:
- Self-rating (1-10):
- Tempo:
- Difficulty notes:
- Tension or pain:
- Coach note:

## Section 2 - Technique
- Planned minutes:
- Actual minutes:
- What I practiced:
- Success target:
- Result:
- Self-rating (1-10):
- Tempo:
- Difficulty notes:
- Tension or pain:
- Coach note:

## Section 3 - Lesson Focus
- Planned minutes:
- Actual minutes:
- What I practiced:
- Success target:
- Result:
- Self-rating (1-10):
- Tempo:
- Difficulty notes:
- Tension or pain:
- Coach note:

## Section 4 - Song / Application
- Planned minutes:
- Actual minutes:
- What I practiced:
- Success target:
- Result:
- Self-rating (1-10):
- Tempo:
- Difficulty notes:
- Tension or pain:
- Coach note:

## Section 5 - Theory / Ear Training
- Planned minutes:
- Actual minutes:
- What I practiced:
- Success target:
- Result:
- Self-rating (1-10):
- Tempo:
- Difficulty notes:
- Tension or pain:
- Coach note:

## Mastery Signals
- Chords:
- Rhythm:
- Scales:
- Fingerstyle:
- Repertoire:
- Fretboard knowledge:

## End of Session Reflection
- What improved today:
- What still feels weak:
- Most common mistake:
- Confidence level (1-10):
- Ready to advance?: yes / no / maybe
- Repeat, simplify, or advance:
- Next session priority:
- Overall rating (1-10):
- Coach recommendation:

## Issue Log
### Issue: [issue-name]
- Trajectory: improving / same / worse
- Context: isolation only / in-song / both
- Error frequency: rare / occasional / frequent / nearly every time
```

---

## Field guidance

**Session Start**
- `Session type`: chosen before practice begins based on readiness. `full` = standard session. `low-friction` = short habit-preservation session. `review-only` = familiar material only. `recovery` = slow technique, minimal volume. `bad-day` = preservation mode.
- `Session goal`: `mastery` = push a skill forward. `maintenance` = keep current skills sharp. `confidence` = play things that feel good. `habit-preservation` = just show up.
- Energy/Focus/Tension/Pain: 1=low/none, 2=mild/okay, 3=good/noticeable, 4=high. If Pain=4, stop immediately.
- `Context notes`: optional free text explaining why today's ratings are what they are.

**Per-section fields**
- `Success target`: what "clean" looks like for this section — specific, not vague.
- `Result`: did you hit the target? What actually happened.
- `Tempo`: BPM if the section is tempo-based; leave blank otherwise.
- `Difficulty notes`: what felt hard and why — free text.
- `Tension or pain`: any physical signals during this section — free text.
- `Coach note`: one thing to remember or change next time — free text.

**Mastery Signals**
Write a brief note per skill area only if there was observable evidence this session. Leave blank if the skill was not used. These are read by the mastery scorecard analysis.

**End of Session Reflection**
- `Repeat, simplify, or advance`: matches the `#status/` tag. The tag is machine-readable; this field is the text explanation.
- `Overall rating (1-10)`: rate the session as a whole, not a specific section.
- `Coach recommendation`: the most important thing to carry into the next session.

**Issue Log**
Add one `### Issue:` block per recurring problem noticed this session. Match the slug to the corresponding `#issue/` tag. Omit this section entirely if no issues arose.
- `Trajectory`: is this issue getting better, staying the same, or getting worse compared to previous sessions?
- `Context`: does this only happen when drilling in isolation, only in songs, or both?
- `Error frequency`: how often did the error occur within this section?

---

## Log archiving

Keep active logs in `logs/`. Archive older logs into `logs/archive/YYYY/` by year.

**Trigger — archive when either condition is met:**
- `logs/` contains more than 60 files (roughly two months of daily practice)
- A new calendar year starts and the previous year has any logs still in `logs/`

**What stays in `logs/`:** The most recent 60 days. This covers all real-time coaching tools — weak-spot tracking (last 10 sessions), plateau detection (last 6–8 sessions), weekly review (last 7 days), and mastery scoring (last 12 sessions).

**How to archive:**
```bash
mkdir -p ~/guitar-notes/logs/archive/2025
mv ~/guitar-notes/logs/2025-*.md ~/guitar-notes/logs/archive/2025/
```

**Scripts and archives:** Most scripts use `--limit` to cap how far back they look, so they work fine on just `logs/`. For long-range historical analysis, point `--folder` directly at the archive path:
```bash
python <skill-dir>/scripts/progress_charts.py --folder ~/guitar-notes/logs/archive/2025 --limit 60
```