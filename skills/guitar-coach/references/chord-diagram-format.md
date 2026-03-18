# Chord Diagram Format

Use this reference whenever displaying a chord. Always use the vertical chord box format rather than inline fret notation (e.g. x32010) when teaching a new chord or reinforcing technique.

## Grid layout

- The **fret position row** sits directly below the chord name. It shows, left to right for each string (low E → A → D → G → B → high e): `x` for muted, `0` for open, or the fret number where that string is pressed.
- **Frets** run top to bottom inside the grid, starting at the nut
- The top border (`┌─┬─┬─┬─┬─┐`) represents the nut for first-position chords
- Show 3 fret rows by default; expand to 4 if the finger span requires it
- Each `│` on a row represents one string column. Replacing a `│` with a finger number shows where that finger is pressed.

## Symbols

### Fret position row (above the grid)

| Symbol | Meaning |
|--------|---------|
| `x`  | String is muted — do not play |
| `0`  | String is played open |
| `N`  | String is pressed at fret N |

### Grid (inside the box)

| Symbol | Meaning |
|--------|---------|
| `│`  | String column — no finger here |
| `1`  | Index finger |
| `2`  | Middle finger |
| `3`  | Ring finger |
| `4`  | Pinky finger |

## Format template

```
  [Chord Name]
x 0 0 0 0 0    ← fret position row: x, 0, or fret number per string
┌─┬─┬─┬─┬─┐
│ │ │ │ │ │  1st fret
├─┼─┼─┼─┼─┤
│ │ │ │ │ │  2nd fret
├─┼─┼─┼─┼─┤
│ │ │ │ │ │  3rd fret
└─┴─┴─┴─┴─┘
```

Replace any `│` with the finger number (1–4) where that finger presses. The fret position row above the grid shows `x`, `0`, or the pressed fret number for every string.

## Non-first-position chords

Add a fret number marker (`Nfr`) after the nut line and label each row with the actual fret number:

```
  [Chord Name]
x 0 5 5 5 0    ← fret position row using actual fret numbers
┌─┬─┬─┬─┬─┐  5fr
│ │ │ │ │ │  5th fret
├─┼─┼─┼─┼─┤
│ │ │ │ │ │  6th fret
├─┼─┼─┼─┼─┤
│ │ │ │ │ │  7th fret
└─┴─┴─┴─┴─┘
```

## Barre chords

Replace each `│` in the barred row with the barre finger number. For a full index-finger barre all six strings show `1`:

```
1 1 1 1 1 1  1st fret  ← full barre with index finger
```

For a partial barre, only replace the `│` on the strings being barred and leave the rest as `│`.

---

## Examples

### Em  (022000)

```
  Em
0 2 2 0 0 0
┌─┬─┬─┬─┬─┐
│ │ │ │ │ │  1st fret
├─┼─┼─┼─┼─┤
│ 1 2 │ │ │  2nd fret
├─┼─┼─┼─┼─┤
│ │ │ │ │ │  3rd fret
└─┴─┴─┴─┴─┘
```

*Index on A fret 2, middle on D fret 2. All six strings ring.*

---

### E Major  (022100)

```
  E Major
0 2 2 1 0 0
┌─┬─┬─┬─┬─┐
│ │ │ 1 │ │  1st fret
├─┼─┼─┼─┼─┤
│ 2 3 │ │ │  2nd fret
├─┼─┼─┼─┼─┤
│ │ │ │ │ │  3rd fret
└─┴─┴─┴─┴─┘
```

*Index on G fret 1, middle on A fret 2, ring on D fret 2.*

---

### A Major  (x02220)

```
  A Major
x 0 2 2 2 0
┌─┬─┬─┬─┬─┐
│ │ │ │ │ │  1st fret
├─┼─┼─┼─┼─┤
│ │ 1 2 3 │  2nd fret
├─┼─┼─┼─┼─┤
│ │ │ │ │ │  3rd fret
└─┴─┴─┴─┴─┘
```

*Index on D fret 2, middle on G fret 2, ring on B fret 2. Keep the open e string ringing.*

---

### D Major  (xx0232)

```
  D Major
x x 0 2 3 2
┌─┬─┬─┬─┬─┐
│ │ │ │ │ │  1st fret
├─┼─┼─┼─┼─┤
│ │ │ 2 │ 1  2nd fret
├─┼─┼─┼─┼─┤
│ │ │ │ 3 │  3rd fret
└─┴─┴─┴─┴─┘
```

*Index on high e fret 2, middle on G fret 2, ring on B fret 3. Mute both low strings.*

---

### G Major  (320003)

```
  G Major
3 2 0 0 0 3
┌─┬─┬─┬─┬─┐
│ │ │ │ │ │  1st fret
├─┼─┼─┼─┼─┤
│ 1 │ │ │ │  2nd fret
├─┼─┼─┼─┼─┤
2 │ │ │ │ 3  3rd fret
└─┴─┴─┴─┴─┘
```

*Index on A fret 2, middle on low E fret 3, ring on high e fret 3. Tip: use pinky on high e to make the C–G transition easier.*

---

### C Major  (x32010)

```
  C Major
x 3 2 0 1 0
┌─┬─┬─┬─┬─┐
│ │ │ │ 1 │  1st fret
├─┼─┼─┼─┼─┤
│ │ 2 │ │ │  2nd fret
├─┼─┼─┼─┼─┤
│ 3 │ │ │ │  3rd fret
└─┴─┴─┴─┴─┘
```

*Index on B fret 1, middle on D fret 2, ring on A fret 3. Keep the E string muted — a common mistake is accidentally strumming it.*

---

### Am  (x02210)

```
  Am
x 0 2 2 1 0
┌─┬─┬─┬─┬─┐
│ │ │ │ 1 │  1st fret
├─┼─┼─┼─┼─┤
│ │ 2 3 │ │  2nd fret
├─┼─┼─┼─┼─┤
│ │ │ │ │ │  3rd fret
└─┴─┴─┴─┴─┘
```

*Index on B fret 1, middle on D fret 2, ring on G fret 2.*

---

### Dm  (xx0231)

```
  Dm
x x 0 2 3 1
┌─┬─┬─┬─┬─┐
│ │ │ │ │ 1  1st fret
├─┼─┼─┼─┼─┤
│ │ │ 2 │ │  2nd fret
├─┼─┼─┼─┼─┤
│ │ │ │ 3 │  3rd fret
└─┴─┴─┴─┴─┘
```

*Index on high e fret 1, middle on G fret 2, ring on B fret 3. Compare with D major to hear the major/minor difference.*

---

### F Major — full barre at fret 1  (133211)

```
  F Major
1 3 3 2 1 1
┌─┬─┬─┬─┬─┐
1 1 1 1 1 1  1st fret  ← index barre all 6 strings
├─┼─┼─┼─┼─┤
│ │ │ 2 │ │  2nd fret
├─┼─┼─┼─┼─┤
│ 3 4 │ │ │  3rd fret
└─┴─┴─┴─┴─┘
```

*Index barres all 6 strings at fret 1. Middle on G fret 2, ring on A fret 3, pinky on D fret 3.*

---

### Bm — partial barre at fret 2  (x24432)

```
  Bm
x 2 4 4 3 2
┌─┬─┬─┬─┬─┐  2fr
│ 1 │ │ 1 1  2nd fret  ← index partial barre (A, B, e)
├─┼─┼─┼─┼─┤
│ │ │ │ 2 │  3rd fret
├─┼─┼─┼─┼─┤
│ │ 4 3 │ │  4th fret
└─┴─┴─┴─┴─┘
```

*Starts at fret 2. Index covers A, B, and high e. Middle on B fret 3, ring on G fret 4, pinky on D fret 4. Mute the low E string.*

---

## Display rules

1. Always show the chord name above the fret position row.
2. Always include the fret position row (`x`, `0`, or fret number for every string) directly below the chord name.
3. Always label each fret row with its fret number to the right.
4. Add `Nfr` after the nut line for chords that do not start at fret 1.
5. Always include a one-line fingering tip below each diagram.
6. For open chords, prefer the standard 3-finger voicing over barre alternatives until the user is past the beginner roadmap.
7. When multiple voicings exist, show the most beginner-accessible one first and mention alternatives in the tip line.
