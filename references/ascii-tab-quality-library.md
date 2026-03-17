# ASCII Tab Quality Library

Use this reference together with `ascii-guitar-tab-rules.md` whenever producing playable tab.

## Timing alignment

- Keep beat counts aligned directly above the attack point.
- Use vertically aligned barlines across all six strings.
- When using double-digit fret numbers, remove hyphens on every string as needed to preserve alignment.
- Prefer one bar per line for dense rhythm material.
- For syncopation, show full counts such as `1 e & a 2 e & a` when needed.

Example:

```text
   1 e & a 2 e & a 3 & 4 &
e|---------------------------|
B|---------------------------|
G|---------------------------|
D|------2---2----------------|
A|--0-0---0---3---2----------|
E|-------------------3-------|
```

## Legato and expressive symbols

Use these symbols consistently:

- `h` hammer-on
- `p` pull-off
- `/` slide up
- `\\` slide down
- `b` bend
- `r` release bend
- `~` vibrato or sustain

Examples:

```text
e|----------------|
B|------5h7p5-----|
G|--4/6-------6\\4-|
D|----------------|
A|----------------|
E|----------------|
```

```text
e|--7b9r7~--------|
B|---------8-7----|
G|--------------7-|
D|----------------|
A|----------------|
E|----------------|
```

## Fingerpicking notation

When fingerstyle or hybrid picking matters, label the picking hand above the tab.

Use:

- `p` thumb
- `i` index
- `m` middle
- `a` ring

Example:

```text
   p   i   m   a   m   i
   1   &   2   &   3   &
e|--------0-----------0---|
B|------1---1-------1---1-|
G|----0-------0---0-------|
D|--2-----------2---------|
A|------------------------|
E|3-----------------------|
```

If the pattern repeats, say `repeat fingerpicking pattern 4x` instead of rewriting too much tab.

## Chord-name placement

- Put chord names above the first beat where the harmony changes.
- Leave enough horizontal space so the chord name clearly applies to the following beats.
- For strumming, combine chord names with counts and optional strum directions.
- Add tab voicings only when exact fingering matters.

Example:

```text
   G               C               D               G
   1 & 2 & 3 & 4 & 1 & 2 & 3 & 4 & 1 & 2 & 3 & 4 &
   D   D U   U D U D   D U   U D U D   D U   U D U
```

## Measure grouping

- Group short drills in 1- to 2-bar units.
- Group riffs in 2- to 4-bar phrases.
- Break longer passages into labeled systems: `Bar 1-4`, `Bar 5-8`.
- For practice material, readability beats compression.

Example:

```text
Bars 1-2
   1 & 2 & 3 & 4 & | 1 & 2 & 3 & 4 &
e|-----------------|-----------------|
B|-----------------|-----------------|
G|-----------------|-----------------|
D|------0-2--------|------0-2--------|
A|--0-2-----3-2----|--0-2-----3-2----|
E|-----------------|-----------------|
```

## Repeat signs and alternate endings

ASCII tab should prefer explicit text over clever shorthand.

Use:

- `repeat 2x`
- `Loop 4x`
- `1st ending`
- `2nd ending`

Example:

```text
Main riff - repeat 2x
   1 & 2 & 3 & 4 &
e|----------------|
B|----------------|
G|----------------|
D|------0-2-------|
A|--0-2-----3-2---|
E|----------------|

1st ending
   1 & 2 &
e|-----------|
B|-----------|
G|-----------|
D|------0----|
A|--3-2------|
E|-----------|

2nd ending
   1 & 2 &
e|-----------|
B|-----------|
G|-----------|
D|------2----|
A|--0--------|
E|-----------|
```

## Quality checklist

Before showing tab, verify:

- timing counts line up with the notes
- special techniques use standard symbols
- fingerpicking labels are present when relevant
- chord names sit above the correct beat
- measures are grouped into readable units
- repeats and endings are stated plainly
