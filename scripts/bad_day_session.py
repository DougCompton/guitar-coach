#!/usr/bin/env python3
import argparse


def main():
    parser = argparse.ArgumentParser(description='Compute time allocation for a preservation practice session.')
    parser.add_argument('--minutes', type=int, default=10, help='Total session length, usually 8-15 minutes')
    args = parser.parse_args()

    total = max(8, args.minutes)
    reset = 2
    easy = max(3, total // 3)
    challenge = max(3, total // 3)
    reflect = total - reset - easy - challenge
    if reflect < 1:
        challenge -= 1
        reflect = 1

    print('## Session Time Allocation')
    print(f'- Total: {total} minutes')
    print('')
    print(f'- Reset: {reset} min')
    print(f'- Easy win: {easy} min')
    print(f'- Tiny challenge: {challenge} min')
    print(f'- Reflection: {reflect} min')


if __name__ == '__main__':
    main()