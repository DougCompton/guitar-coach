#!/usr/bin/env python3
import argparse

LIB = {
    'open': {
        'C': ['x32010'],
        'A': ['x02220'],
        'G': ['320003', '320033'],
        'E': ['022100'],
        'D': ['xx0232'],
        'Am': ['x02210'],
        'Em': ['022000'],
        'Dm': ['xx0231'],
    },
    'barre-e': {
        'major-root-6': ['133211', '355433'],
        'minor-root-6': ['133111', '355333'],
    },
    'barre-a': {
        'major-root-5': ['x35553', 'x57775'],
        'minor-root-5': ['x35543', 'x57765'],
    },
    'triads-top-3': {
        'major-set-1': ['xx9987', 'xx121210'],
        'minor-set-1': ['xx9886', 'xx121110'],
    },
}

FAMILIES = {
    'c': 'I C | ii Dm | iii Em | IV F | V G | vi Am',
    'g': 'I G | ii Am | iii Bm | IV C | V D | vi Em',
    'd': 'I D | ii Em | iii F#m | IV G | V A | vi Bm',
    'a': 'I A | ii Bm | iii C#m | IV D | V E | vi F#m',
    'e': 'I E | ii F#m | iii G#m | IV A | V B | vi C#m',
}


def main():
    p = argparse.ArgumentParser(description='Show guitar chord shapes and chord-family references.')
    p.add_argument('--group', choices=['open', 'barre-e', 'barre-a', 'triads-top-3', 'all'], default='all')
    p.add_argument('--key', help='Show common diatonic chord family for a key, e.g. G')
    args = p.parse_args()

    print('# Chord Library + Shape Families')
    groups = LIB.keys() if args.group == 'all' else [args.group]
    for group in groups:
        print(f'## {group}')
        for name, shapes in LIB[group].items():
            print(f'- {name}: {", ".join(shapes)}')
    if args.key:
        fam = FAMILIES.get(args.key.lower())
        if fam:
            print('')
            print(f'## Common chord family in {args.key.upper()}')
            print(f'- {fam}')
        else:
            print('')
            print(f'- No built-in family map for {args.key}')


if __name__ == '__main__':
    main()
