#!/usr/bin/env python3
import argparse


def main():
    parser = argparse.ArgumentParser(description='Generate a low-friction fallback guitar session.')
    parser.add_argument('--minutes', type=int, default=10, help='Total session length, usually 8-15 minutes')
    parser.add_argument('--focus', default='one familiar chord loop or riff', help='Easy musical material to keep momentum')
    args = parser.parse_args()

    total = max(8, args.minutes)
    warm = 2
    easy = max(3, total // 3)
    focus = max(3, total // 3)
    reflect = total - warm - easy - focus
    if reflect < 1:
        focus -= 1
        reflect = 1

    print('## Bad-Day Practice Session')
    print('- Goal: keep the habit alive with clean, low-stress reps.')
    print('')
    print(f'1. Reset - {warm} min')
    print('   - Shake out hands, posture check, play open strings slowly.')
    print(f'2. Easy win - {easy} min')
    print(f'   - Play: {args.focus}')
    print('   - Success target: one clean loop with relaxed hands.')
    print(f'3. Tiny challenge - {focus} min')
    print('   - Practice only one micro-problem at half speed.')
    print('   - Success target: 3 clean reps in a row.')
    print(f'4. Reflection - {reflect} min')
    print('   - Reply with numbers only: 1) Easier now  2) Same  3) Hard  4) Stop for today')
    print('')
    print('Rule: do not add new material in this mode. Protect consistency first.')


if __name__ == '__main__':
    main()
