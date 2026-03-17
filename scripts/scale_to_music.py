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
}


def main():
    p = argparse.ArgumentParser(description='Turn scale practice into musical application.')
    p.add_argument('--scale', required=True, help='major, minor-pentatonic, major-pentatonic')
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
