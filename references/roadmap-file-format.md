# External Lesson Roadmap Files

Store lesson roadmaps as editable markdown files in the same folder as the daily practice logs.

## File names

Use one markdown file per roadmap:

- `roadmap-beginner.md`
- `roadmap-intermediate.md`
- `roadmap-fingerstyle.md`
- `roadmap-celtic.md`
- `roadmap-rock.md`
- `roadmap-blues.md`
- `roadmap-country.md`

Use lowercase names with hyphens.

## Active roadmap pointer

Track the currently selected roadmap in a simple markdown file:

`active-roadmap.md`

Contents:

```markdown
# Active Roadmap

- Current roadmap: beginner
- Roadmap file: roadmap-beginner.md
- Last updated: YYYY-MM-DD
```

If `active-roadmap.md` does not exist, default to `beginner`.

## Roadmap markdown structure

Use this format so the skill can read and update the roadmap consistently.

```markdown
# Roadmap: Beginner

## Overview
- Focus:
- Level:
- Goal:
- Current stage:
- Next review date:

## Lesson 1
- Title: Open-string reset and posture
- Status: current
- Goal: Play all open strings cleanly with relaxed picking
- Exit criteria:
  - 3 clean passes in a row
  - Tension rating 1 or 2
- Practice menu:
  - Open-string picking on all six strings
  - Slow string crossing
- Application:
  - Two-bar open-string rhythm drill
- Notes:

## Lesson 2
- Title: Basic chord shapes
- Status: queued
- Goal: Form Em, Am, C, G, and D cleanly
- Exit criteria:
  - 5 clean chord changes at slow tempo
  - Confidence 3 or 4
- Practice menu:
  - Shape formation
  - One-minute change drill
- Application:
  - Four-bar chord loop
- Notes:
```

## Status values

Use only these status values:

- `current`
- `queued`
- `review`
- `complete`
- `paused`

Exactly one lesson should normally be `current`.

## Editing rules

When the user edits roadmap files manually, trust the file contents as the source of truth.
When the skill updates roadmap files, preserve the user's lesson titles, order, custom notes, and extra sections.
Only change the minimum needed:

- status fields
- current stage
- next review date
- brief coach notes

## Switching roadmaps

To switch tracks, update `active-roadmap.md` and use the chosen roadmap file for planning.
Do not merge tracks unless the user explicitly asks.
