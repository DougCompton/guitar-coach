# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A Claude Code **skill** — a structured AI guitar-practice coach. Once installed at `~/.claude/skills/guitar-coach/` (or `%USERPROFILE%\.claude\skills\guitar-coach\` on Windows), it is loaded automatically when the user talks about guitar practice.

The behavioral specification lives in `SKILL.md`. All 17 Python helper scripts in `scripts/` are invoked by the coach at runtime — users never call them directly.

## Running scripts

All scripts use Python 3.9+ with only the standard library (no build step, no virtual environment required unless using the optional `sounddevice` package for audio reflection).

```bash
# Install optional audio dependency only
pip install sounddevice

# Run any script directly
python scripts/practice_timer.py --section "Warm-up" --minutes 4 --task "..." --success "..."
python scripts/build_practice_session.py --minutes 30
python scripts/build_practice_session.py --minutes 30 --weak-spot "chord-transitions"
python scripts/analyze_logs.py --folder ~/guitar-notes/logs --logs 7
python scripts/analyze_logs.py --folder ~/guitar-notes/logs --days 7
python scripts/readiness_check.py --minutes 30 --energy 3 --focus 3 --tension 1 --pain 1
python scripts/practice_end.py --folder ~/guitar-notes/logs
```

**Critical:** When the skill is running inside Claude Code, scripts must use the **absolute path** to the skill directory. Never use relative paths — the shell may be `cd`'d elsewhere. Use `--folder <notes-folder>` instead of `cd`-ing into the notes folder.

## Architecture

```
guitar-coach/
├── SKILL.md          ← Behavioral spec (the coach's rules, loaded as system context)
├── scripts/          ← 17 Python automation helpers (called by the coach at runtime)
├── references/       ← 20 Markdown reference docs (tab rules, roadmap formats, templates)
├── prompts/          ← 13 Markdown prompt files (coaching analysis templates)
├── agents/           ← Placeholder for future OpenAI Actions integration
└── requirements.txt  ← Python deps (stdlib only; sounddevice optional)
```

### Data flow at runtime

The skill runs against a user-owned **notes folder** (e.g., `~/guitar-notes/`) that lives *outside* this repo:

```
~/guitar-notes/
├── active-roadmap.md         ← which of the 7 tracks is currently active
├── roadmap-beginner.md       ← editable lesson sequences (user may modify these)
├── roadmap-{track}.md        ← (intermediate, fingerstyle, celtic, rock, blues, country)
├── repertoire.md             ← songs in learning / polishing / maintenance states
└── logs/
    ├── YYYY-MM-DD-guitar-practice.md   ← daily log (one per session)
    └── archive/YYYY/                   ← logs older than ~60 days
```

Scripts that read logs accept a `--folder` argument pointing at the `logs/` subfolder. Scripts that manage roadmaps accept `--folder` pointing at the notes root.

### Script categories

| Category | Scripts |
|---|---|
| Session planning & execution | `build_practice_session.py`, `practice_timer.py`, `practice_end.py` |
| Readiness & adaptation | `readiness_check.py`, `bad_day_session.py`, `fix_one_thing.py` |
| Progress tracking | `analyze_logs.py`, `progress_charts.py` |
| Content & libraries | `chord_library.py`, `scale_to_music.py`, `repertoire_checklist.py`, `musicality_prompt.py` |
| Lesson management | `manage_roadmap.py`, `manage_repertoire.py` |
| Advanced | `diagnose_hands.py`, `tempo_ladder.py`, `listen_and_reflect.py` |

### Reference documents

`references/` contains the formatting standards and coaching frameworks that both the skill and scripts depend on:

- **Tab and notation:** `ascii-guitar-tab-rules.md`, `ascii-tab-quality-library.md`, `chord-diagram-format.md`
- **Coaching logic:** `coaching-modes.md`, `mastery-score-rules.md`, `progression-rules.md`, `diagnostic-mode.md`, `audio-reflection-rules.md`
- **Content libraries:** `chord-library-and-families.md`, `scale-to-music.md`, `musicality-prompts.md`, `theory-on-guitar.md`
- **File formats:** `daily-log-template.md`, `roadmap-file-format.md`, `repertoire-file-format.md`, `default-roadmaps.md`, `repertoire-performance-checklist.md`, `multiple-choice-responses.md`, `student-profile-template.md`

## Key conventions

- **All playable examples use ASCII guitar tab** — formatted per `references/ascii-guitar-tab-rules.md`. Never use inline fret notation like `x32010`.
- **Chord shapes use vertical box diagrams** — per `references/chord-diagram-format.md`.
- **7 built-in roadmap tracks**: beginner, intermediate, fingerstyle, celtic, rock, blues, country. Each has 8 lessons. Tracks are created by `manage_roadmap.py --ensure-defaults`.
- **Log archiving trigger**: when `logs/` exceeds 60 files or a new calendar year starts. Always ask before moving files.
- **Pain protocol**: Stop immediately, log it, end the session — never push through pain.

## Development

See `DEVELOPMENT.md` for the open improvement backlog (35+ completed features, 20+ pending improvements).
