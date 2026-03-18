# Advanced ASCII Guitar Tab Rules

Use this reference whenever the skill displays riffs, exercises, licks, melodies, or song fragments. Prefer readable, standard six-line ASCII guitar tab.

## Core layout

Write tab from the highest string to the lowest string in this order:

```text
e|----------------|
B|----------------|
G|----------------|
D|----------------|
A|----------------|
E|----------------|
```

- `e` is the high E string.
- `E` is the low E string.
- Use monospaced alignment.
- Keep barlines vertically aligned across all six strings.
- Use hyphens `-` for time spacing between notes.
- Put fret numbers directly on the string where the note is played.
- Use double-digit fret numbers carefully so surrounding spacing stays aligned.

## Required display rules for this skill

1. Display all playable examples in ASCII guitar tab.
2. Put chord names or section labels above the tab when useful.
3. Keep examples short and practiceable unless the user asks for a longer passage.
4. When rhythm matters, add count markings above the tab.
5. When a passage is too dense for clean tab, split it into smaller phrases.
6. For chords or strumming, prefer a chord name line plus rhythmic slash guidance and optional tab voicing.
7. Do not switch to staff notation unless the user explicitly asks.

## Spacing and alignment

Good:

```text
   1 & 2 & 3 & 4 &
e|----------------|
B|----------------|
G|----------------|
D|--------0-2-----|
A|--0-2-3-----3-2-|
E|----------------|
```

Also acceptable for compact examples:

```text
e|----------------|
B|----------------|
G|----------------|
D|--------0-2-----|
A|--0-2-3-----3-2-|
E|----------------|
   1 & 2 & 3 & 4 &
```

Rules:

- Keep counts aligned with the attacks they describe.
- If a fret number has two digits, preserve timing alignment by reducing nearby hyphen counts on every string as needed.
- Do not let barlines drift.

## Common symbols

Use these standard symbols when needed:

- `h` hammer-on
- `p` pull-off
- `/` slide up
- `\\` slide down
- `b` bend
- `r` release bend
- `~` vibrato or sustain
- `x` muted note / dead note
- `PM----` palm mute marking above the affected region
- `let ring` above the affected region
- `N.H.` natural harmonic
- `< >` harmonic note heads when useful in text, though simple labels above the tab are often clearer
- `()` ghost note or optional note

Example:

```text
   1 & 2 & 3 & 4 &
e|------------------------|
B|------------------------|
G|--------5h7p5-----------|
D|----5h7-------7p5-------|
A|--5---------------7\5---|
E|------------------------|
```

## Bends and releases

Mark bends with the target interval if clarity helps.

```text
e|--7b9--7r--5-----------|
B|-------------7-5-------|
G|-----------------6-4---|
D|-----------------------|
A|-----------------------|
E|-----------------------|
```

For beginners, explain unusual symbols in one short sentence below the tab.

## Chord and strumming presentation

When showing rhythm guitar, use a chord line above the tab. If exact voicing matters, include the fretted shape in tab. If the goal is rhythm practice, counts and strum direction can be clearer than dense six-string notation.

Example with chord names and simple strum guidance:

```text
   G               C               D               G
   1 & 2 & 3 & 4 & 1 & 2 & 3 & 4 & 1 & 2 & 3 & 4 & 1 & 2 & 3 & 4 &
   D   D U   U D U D   D U   U D U D   D U   U D U D   D U   U D U
```

### Strum direction alignment

Each symbol in the D/U line aligns column-for-column with the count line directly above it. Place D or U in the same character position as the subdivision it falls on (1, &, e, a). Use a space in all other positions. The D/U line sits immediately below the count line with no blank line between them.

If voicing matters, add a tab voicing below:

```text
   G            C            D            G
e|--3------------0------------2------------3--|
B|--0------------1------------3------------0--|
G|--0------------0------------2------------0--|
D|--0------------2------------0------------0--|
A|--2------------3------------x------------2--|
E|--3------------x------------x------------3--|
```

## Repeats, sections, and phrasing

- Label sections clearly: `Intro`, `Verse riff`, `Exercise A`, `Loop 4x`.
- Use repeated barlines or explicit text like `repeat 4x` instead of trying to compress too much into one line.
- Break long examples across multiple systems of six lines.
- Keep each system readable rather than forcing everything into one block.

Example:

```text
Exercise A - repeat 4x
   1 & 2 & 3 & 4 &
e|----------------|
B|----------------|
G|----------------|
D|------0-2-------|
A|--0-2-----3-2---|
E|----------------|
```

## Technique annotations

When technique matters, add a short label above the tab, not a long paragraph.

Examples:

- `alternate pick throughout`
- `use fingers 1-2-3-4`
- `keep 3rd finger anchored`
- `shift at bar 2`
- `rest stroke on the downbeats`

## Beginner coaching rules for tab in this skill

When the user is a returning beginner:

1. Prefer short loops, one-bar to four-bar examples.
2. Show counts for rhythm-sensitive material.
3. Keep positions low on the neck unless the lesson specifically goes higher.
4. Explain one non-obvious symbol at a time.
5. Pair the tab with one success target, such as `play 4 clean loops at 60 BPM`.

## Error prevention checklist

Before showing tab, check:

- Are the strings in the correct order?
- Are barlines aligned vertically?
- Are fret numbers placed on the correct strings?
- Do counts align with note attacks?
- Is the example short enough to read without crowding?
- Are special symbols explained if the user is unlikely to know them?

## Recommended output pattern for this skill

Use this shape when presenting practice material:

```text
Exercise name
Goal: [one sentence]
Count: [if needed]
Tab:
e|----------------|
B|----------------|
G|----------------|
D|----------------|
A|----------------|
E|----------------|
Target: [one measurable result]
```

## Limits of ASCII tab

ASCII tab is excellent for fret/string placement but weaker than notation for exact rhythm, duration, and articulation detail. When rhythm is essential, add counts, barlines, chord names, and short text prompts so the user can play it correctly.
