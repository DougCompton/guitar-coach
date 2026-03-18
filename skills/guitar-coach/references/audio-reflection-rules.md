# Audio Reflection Rules

Use this reference when the user wants quick, numeric feedback from a short recording or microphone capture.

## Purpose

Turn a brief practice excerpt into tighter multiple-choice reflection prompts for:

1. timing stability
2. note clarity
3. unwanted string noise
4. dynamic control

Keep the output numeric so the user can answer quickly.

## Important limits

- Treat audio analysis as a coaching aid, not ground truth.
- Prefer short single-focus recordings: one drill, one riff, one chord loop, or one fingerstyle pattern.
- The bundled script is strongest on clean, dry practice audio.
- Background noise, room echo, singing, backing tracks, and distortion reduce reliability.
- Live microphone capture only works when the script runs in a local environment with microphone access and the optional `sounddevice` package installed.
- If microphone access is unavailable, use a saved WAV recording instead.

## Standard questions

Always ask these as numeric multiple-choice prompts:

1. Timing stability
   1. Very steady
   2. Mostly steady
   3. Noticeably uneven
   4. Unstable
2. Note clarity
   1. Clear
   2. Mostly clear
   3. Muddy or noisy
   4. Very unclear
3. Unwanted string noise
   1. Minimal
   2. Some
   3. Frequent
   4. Dominant
4. Dynamic control
   1. Well controlled
   2. Usable
   3. Inconsistent
   4. Wildly uneven

Default reply format:

`Reply with numbers only: Q1, Q2, Q3, Q4`

## Good usage pattern

1. Capture 10 to 30 seconds.
2. Analyze one exercise only.
3. Show the four numeric prompts.
4. Add one short coaching recommendation tied to the weakest score.
5. Write the result into the daily log with issue tags when useful.

## Coaching follow-through

Map weak categories to immediate next actions:

- timing stability -> slow metronome or clap-count-strum drill
- note clarity -> slow clean-note test with lighter pressure
- unwanted string noise -> muting isolation or right-hand accuracy drill
- dynamic control -> accent pattern drill at slower tempo
