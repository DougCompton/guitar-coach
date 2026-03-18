#!/usr/bin/env python3
import argparse

AREAS = {
    'left':  ['fretting-hand-pressure', 'finger-placement', 'thumb-independence'],
    'right': ['picking-hand-consistency', 'strumming-motion'],
}


def main():
    p = argparse.ArgumentParser(description='Identify the hand being diagnosed for technique analysis.')
    p.add_argument('--hand', choices=['left', 'right'], required=True)
    args = p.parse_args()

    print('## Hand Diagnostic Input')
    print(f'- Hand: {args.hand}')
    print(f'- Areas: {", ".join(AREAS[args.hand])}')


if __name__ == '__main__':
    main()