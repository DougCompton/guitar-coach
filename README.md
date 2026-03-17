# Guitar Coach Skill

A structured AI guitar-practice coach for returning beginners. Tell it how much time you have and how you feel — it plans the session, runs the timers, tracks your progress, and tells you whether to repeat, simplify, or advance. You never run scripts manually; the coach handles all of that in the background.

---

## Installation

### Claude Code

1. Copy the `guitar-coach` folder into your Claude Code skills directory:

   **macOS / Linux (bash)**
   ```bash
   cp -r guitar-coach ~/.claude/skills/
   ```

   **Windows — PowerShell**
   ```powershell
   Copy-Item -Recurse guitar-coach "$env:USERPROFILE\.claude\skills\"
   ```

   **Windows — Command Prompt (cmd)**
   ```cmd
   xcopy /E /I guitar-coach "%USERPROFILE%\.claude\skills\guitar-coach"
   ```

2. Confirm the skill file is in place:

   **macOS / Linux**
   ```
   ~/.claude/skills/guitar-coach/SKILL.md
   ```

   **Windows**
   ```
   %USERPROFILE%\.claude\skills\guitar-coach\SKILL.md
   ```

3. Reload Claude Code (or start a new session). The skill is active when you see `guitar-coach` listed under available skills.

The coach triggers automatically when you talk about guitar practice. It does not need to be invoked by name.

---

### Any AI with a custom system prompt

If your AI tool supports a persistent system prompt or custom instructions:

1. Open `SKILL.md` in a text editor.
2. Copy everything from the first `#` heading to the end of the file (skip the YAML frontmatter block at the top between the `---` markers).
3. Paste it into your tool's system prompt or custom instructions field.
4. Save and start a new session.

Note: In this mode, the Python scripts in `scripts/` cannot be executed automatically. The coach will provide all coaching logic inline instead.

---

### OpenAI Actions / ChatGPT plugin

The `agents/openai.yaml` file is a placeholder for an OpenAI Actions spec. It is not yet a deployable plugin. To deploy as an OpenAI Action, expand that file with a full `openapi: 3.1.0` spec, an `auth` section, and action mappings to the `scripts/` endpoints. See the comment in that file for details.

---

## How to use it

Just talk to the coach in plain language. It reads your practice history, picks the right tools, and runs whatever is needed automatically.

### Starting a session

```
Let's practice. I have 30 minutes.
```
```
I want to practice. Energy is pretty good, focus is medium, no tension or pain.
```
```
Guitar time. 20 minutes max today.
```

The coach will confirm your active roadmap, today's lesson, warm-up, section plan, and the first timer prompt — no setup required.

---

### First time setup

Tell the coach where you want to store your notes:

```
Set up guitar practice in ~/guitar-notes
```

It will create your roadmap files, repertoire list, and notes folder automatically. After that, it remembers the folder for every future session.

---

### Low-energy and short sessions

```
I'm tired today. Short session.
```
```
Only have 10 minutes. What's the most useful thing to practice?
```
```
I'm frustrated and almost didn't show up. What do we do?
```

The coach switches to a fallback session — one easy win, one habit-keeping block, no pressure.

---

### Fixing a specific problem

```
I keep messing up the G to C chord change.
```
```
My timing falls apart whenever I try to strum and change chords at the same time.
```
```
Something is going wrong with my right hand when I pick.
```

The coach runs a targeted repair session focused on that one issue. If it's unclear whether the problem is the fretting or picking hand, it runs a diagnostic to separate them before assigning the drill.

---

### Checking progress and deciding what comes next

```
Am I ready to move on?
```
```
What have I been struggling with lately?
```
```
Show me how I've been doing this week.
```
```
I feel like I've been stuck on the same thing for weeks.
```

The coach reviews your recent logs, scores your mastery by skill type, checks for plateaus, and gives a clear repeat / simplify / advance recommendation with the reasoning.

---

### Repertoire and songs

```
What songs am I working on?
```
```
I want to add Blackbird to my practice list.
```
```
Is Wonderwall ready to perform?
```
```
I want to spend today on songs, not drills.
```

The coach manages a separate repertoire lane with three states — learning, polishing, and maintenance — and picks the right song to work on based on where each one is.

---

### Theory and scales

```
Teach me something useful about the key of G.
```
```
Walk me through the pentatonic scale and make it musical.
```
```
I want to understand how chord shapes are related.
```

Theory is always taught through the guitar, not as abstract study. Scale work always ends with a lick, riff, or improv prompt so it stays musical.

---

### Uploading tabs, chord charts, or lesson notes

```
Here's a tab I found for the song I want to learn. [attach file]
```
```
My teacher gave me this exercise sheet. Can you build a session around it?
```

The coach reads the material, extracts the practical content, and builds a timed practice plan from it.

---

### Switching roadmap tracks

```
I want to try fingerstyle.
```
```
I'm interested in Irish folk music. Do you have anything for that?
```
```
I think I'm ready to move to intermediate.
```

The coach will recommend a track switch when the signal is clear, explain why, and ask for confirmation before switching. It never switches automatically.

---

### Weekly review

```
How did practice go this week?
```
```
What should I focus on next week?
```
```
What's improving and what's stalled?
```

The coach summarizes the week, answers what's improving fastest, what's lagging, what's overloaded, and what is ready to advance, then recommends specific roadmap changes.

---

### Audio reflection

```
I just recorded a short clip. Can you listen and give me feedback?
```
```
I want you to listen while I play this chord loop.
```

If microphone or audio file access is available, the coach runs a numeric audio reflection scoring timing stability, note clarity, unwanted string noise, and dynamic control. If audio access isn't available, it coaches from your self-ratings instead.

---

## What to expect during a session

Every section of every practice session follows the same structure:

1. **What to do** — specific, narrow task
2. **What good sounds or feels like** — one concrete quality target
3. **Timer prompt** — how long and what to focus on at each minute mark
4. **Success target (mini-win)** — one objective thing to achieve before moving on
5. **Reflection questions** — 4 to 5 short numbered questions; reply with digits only

Example reflection prompt:

```
Reply with numbers only: Q1, Q2, Q3, Q4

1. Difficulty   1. Very easy  2. Manageable  3. Challenging  4. Too hard
2. Accuracy     1. Clean      2. A few mistakes  3. Frequent  4. Fell apart
3. Timing       1. Steady     2. A little off    3. Unstable  4. Lost pulse
4. Tension      1. None       2. Mild            3. Noticeable  4. Pain — stop
```

If difficulty or accuracy is 3 or 4, the coach adds a fifth question to identify whether the fretting hand, picking hand, or both are causing the problem — so the next drill targets the right thing.

After each section, the coach updates your markdown log and decides what comes next.

---

## Daily practice log

The coach creates one markdown file per practice day in a `logs/` subfolder inside your notes folder:

```
~/guitar-notes/logs/2026-03-13-guitar-practice.md
```

Roadmap and repertoire files stay in the root of your notes folder so they are easy to find and edit. Logs stay in `logs/` so they don't clutter the root.

Each log records planned vs. actual time, self-ratings, coach notes, mini-win results, and searchable tags for roadmap, lesson, current issues, and session status. You can edit these files manually — the coach reads them and respects your edits.

### Archiving old logs

Over time `logs/` will grow. The coach watches the count and will suggest archiving when it exceeds 60 files (roughly two months of daily practice) or when a new calendar year starts.

When archiving, logs move into a year subfolder — nothing is deleted:

```
~/guitar-notes/logs/
├── 2026-03-13-guitar-practice.md   ← active logs (last ~60 days)
├── 2026-03-12-guitar-practice.md
└── archive/
    ├── 2025/                        ← full previous year
    └── 2024/
```

The coach will ask before moving any files. Most coaching tools only need the last 10–60 days of logs, so archiving older files does not affect normal practice sessions. For long-range trend analysis the coach can look into the archive folder as well.

---

## Feature reference

### Core — active every session

| Feature | What it does |
|---|---|
| Session planning | Builds timed section plans with mini-wins for every block |
| Daily markdown log | Creates one `YYYY-MM-DD-guitar-practice.md` per day |
| Live practice coaching | Timer prompts, checkpoint cues, and section-by-section guidance |
| Numbered reflection | Post-section questions answered with digits only |
| Repeat / simplify / advance | Evidence-based recommendation after each session |
| ASCII guitar tab | All playable examples in clean, aligned tab |
| Theory on the instrument | Theory tied to fretboard shapes, not abstract study |
| Mini-win targets | Every section has one narrow, objective success target |
| Uploaded materials | Tabs, chord charts, PDFs, and lesson notes supported |

### Session helpers — used when relevant

| Feature | Triggered when |
|---|---|
| Start-here auto-planner | User wants the coach to choose everything |
| One-command practice day | User gives readiness ratings upfront |
| Readiness classifier | Coach picks session type from energy/focus/tension/pain |
| Weak-spot corrective drill | Recent logs show a recurring problem |
| Tempo-based progression | Rhythm or speed is the current advancement gate |
| Spaced repetition reviews | A learned skill is due for review |
| Bad-day fallback session | Low energy, low motivation, or frustration signals |
| Fix-one-thing repair session | One issue is dominating the session |
| Repertoire lane management | User asks about songs |
| Roadmap switching | User signals interest in a different style or level |
| Mastery scoring | Coach needs evidence before recommending advancement |
| Chord library and shapes | Chord questions or chord-based drills |
| Scale-to-music connection | Any scale practice |
| Repertoire performance checklist | Checking if a song is ready |
| Musicality prompts | Session is becoming too mechanical |
| Left/right hand diagnostic | Problem source is unclear |
| Audio-aware reflection | User has a recording or microphone access |

### Analytics and review — on demand

| Feature | Triggered when |
|---|---|
| Weekly review | User asks about the week or what to change |
| Plateau detection | Repeated logs show the same skill stalled |
| Progress charts | User asks about trends or motivation check-in |

---

## Notes folder layout

```
~/guitar-notes/                          ← notes root
├── active-roadmap.md                    ← which track is active
├── roadmap-beginner.md                  ← editable lesson sequences
├── roadmap-intermediate.md
├── roadmap-fingerstyle.md
├── roadmap-celtic.md
├── roadmap-rock.md
├── roadmap-blues.md
├── roadmap-country.md
├── repertoire.md                        ← songs in learning / polishing / maintenance
└── logs/                                ← daily practice logs
    ├── 2026-03-13-guitar-practice.md    ← active (last ~60 days)
    ├── 2026-03-12-guitar-practice.md
    └── archive/
        └── 2025/                        ← previous years, archived when prompted
```

The coach creates all of these on first use. Roadmap and repertoire files stay in the root so they are easy to find and edit. Logs live in `logs/` so the root stays clean.

---

## Files in this skill

| File / Folder | Purpose |
|---|---|
| `SKILL.md` | Skill behavior and coaching rules |
| `README.md` | This file |
| `DEVELOPMENT.md` | Open TODOs and suggested improvements |
| `agents/openai.yaml` | Reserved for OpenAI Actions metadata |
| `requirements.txt` | Python dependency list (standard library only; `sounddevice` optional) |
| `scripts/` | Automation helpers run automatically by the coach |
| `references/` | Tab rules, roadmap formats, templates, and coaching references |

---

## Notes and limitations

- Microphone listening requires local audio access and the optional `sounddevice` package (`pip install sounddevice`). If unavailable, the coach uses self-rated reflection instead.
- Audio reflection is a coaching aid, not a studio-grade analysis system.
- Practice logs and roadmap files are user-editable markdown. The coach preserves manual edits.
- ASCII guitar tab is the default format for all playable examples.

---

For the development roadmap, open TODOs, and suggested improvements, see [DEVELOPMENT.md](DEVELOPMENT.md).
