#!/usr/bin/env python3
import argparse

MAP = {
    'major': {
        'lick': 'Use 1-2-3 on one string, then answer with 3-2-1 on the next string.',
        'riff': 'Build a 2-bar riff using scale degrees 1, 2, 3, and 5 only.',
        'improv': 'Improvise for 60 seconds over I-IV-V using only the first 5 notes of the scale.',
        'progression': 'Play over a I-V-vi-IV progression and target the root on each chord change.',
    },
    'minor-pentatonic': {
        'lick': 'Play a 4-note box-1 lick and end with a bend on the b3 or 4.',
        'riff': 'Create a repeating 1-bar riff using root, b3, 4, and b7.',
        'improv': 'Improvise for 60 seconds over a minor groove using only box 1.',
        'progression': 'Play over i-bVII-bVI-bVII and land on the root each bar.',
    },
    'major-pentatonic': {
        'lick': 'Use 1, 2, 3, 5, 6 for a bright 2-bar phrase with one slide.',
        'riff': 'Make a 1-bar hook from 1, 2, 3, and 5 only.',
        'improv': 'Improvise over a major vamp and avoid the 4th completely.',
        'progression': 'Play over I-IV with phrase endings on 3 or 6.',
    },
    'natural-minor': {
        'lick': 'Descend the scale from 8 to 5, pause, then resolve to 1.',
        'riff': 'Build a 2-bar riff using 1, b3, 4, 5, and b7.',
        'improv': 'Improvise for 60 seconds over i-bVII-bVI using all 7 scale tones.',
        'progression': 'Play over i-iv-bVII-i and target chord tones on beats 1 and 3.',
    },
    'blues': {
        'lick': 'Play minor pentatonic box 1 and add the b5 as a passing tone between 4 and 5.',
        'riff': 'Create a 1-bar riff using root, b3, 4, b5, 5, and b7 — emphasize the b5 as a bend.',
        'improv': 'Improvise over a 12-bar blues and use the b5 as a chromatic surprise, not a landing note.',
        'progression': 'Play over I7-IV7-V7 and resolve phrases to the root or 5th of each chord.',
    },
    'dorian': {
        'lick': 'Use 1, 2, b3, 4 ascending then resolve down to 1 — notice the raised 6th (natural 6).',
        'riff': 'Make a groove riff using 1, b3, 5, and 6 — the raised 6 is the dorian signature.',
        'improv': 'Improvise over a i-IV vamp and feature the natural 6 to emphasize the dorian sound.',
        'progression': 'Play over i-IV (minor i, major IV built on b7) — classic dorian home.',
    },
    'mixolydian': {
        'lick': 'Descend from 8 through b7, 6, 5 — the b7 is the mixolydian color note.',
        'riff': 'Build a 2-bar riff on 1, 3, 5, b7 — like a dominant 7 chord brought to life.',
        'improv': 'Improvise over a I7 chord for 60 seconds and resolve phrases to 1 or 5.',
        'progression': 'Play over I7-bVII-IV-I — a classic rock and blues-rock mixolydian move.',
    },
}


def main():
    p = argparse.ArgumentParser(description='Turn scale practice into musical application.')
    p.add_argument('--scale', required=True,
                   help='major, minor-pentatonic, major-pentatonic, natural-minor, blues, dorian, mixolydian')
    args = p.parse_args()
    key = args.scale.lower()
    data = MAP.get(key)
    if not data:
        raise SystemExit(f'Unsupported scale: {args.scale}')
    print(f'# Scale-to-Music Integration: {args.scale}')
    print(f'- Lick: {data["lick"]}')
    print(f'- Riff fragment: {data["riff"]}')
    print(f'- Short improv prompt: {data["improv"]}')
    print(f'- Chord progression: {data["progression"]}')


if __name__ == '__main__':
    main()
