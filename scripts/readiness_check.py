#!/usr/bin/env python3
import argparse


def choose_session(minutes: int, energy: int, focus: int, tension: int, pain: int):
    if pain >= 3:
        return 'recovery', 'Pain is elevated, so keep the guitar work light and technique-safe.'
    if tension >= 4:
        return 'recovery', 'Tension is high, so reduce difficulty and prioritize relaxation.'
    if minutes <= 12 or energy <= 2:
        return 'low-friction', 'Time or energy is limited, so preserve the habit with a compact win.'
    if focus <= 2:
        return 'review-only', 'Low focus means review and cleanup will work better than new material.'
    return 'full', 'You have enough time and readiness for a normal coaching session.'


def main():
    p = argparse.ArgumentParser(description='Convert numeric readiness ratings into a recommended session type.')
    p.add_argument('--minutes', type=int, required=True)
    p.add_argument('--energy', type=int, required=True, help='1 low, 2 okay, 3 good, 4 high')
    p.add_argument('--focus', type=int, required=True, help='1 scattered, 2 shaky, 3 steady, 4 locked in')
    p.add_argument('--tension', type=int, required=True, help='1 none, 2 mild, 3 noticeable, 4 high')
    p.add_argument('--pain', type=int, required=True, help='1 none, 2 mild, 3 concerning, 4 stop')
    args = p.parse_args()

    session_type, reason = choose_session(args.minutes, args.energy, args.focus, args.tension, args.pain)

    print('# Readiness Check')
    print(f'- Minutes available: {args.minutes}')
    print(f'- Energy: {args.energy}/4')
    print(f'- Focus: {args.focus}/4')
    print(f'- Tension: {args.tension}/4')
    print(f'- Pain: {args.pain}/4')
    print('')
    print(f'## Recommended session type: {session_type}')
    print(f'- Why: {reason}')
    print('')
    print('## Numeric prompts')
    print('1. Energy: 1 low, 2 okay, 3 good, 4 high')
    print('2. Focus: 1 scattered, 2 shaky, 3 steady, 4 locked in')
    print('3. Tension: 1 none, 2 mild, 3 noticeable, 4 high')
    print('4. Pain: 1 none, 2 mild, 3 concerning, 4 stop')


if __name__ == '__main__':
    main()
