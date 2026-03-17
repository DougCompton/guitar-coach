#!/usr/bin/env python3
import argparse
from datetime import date, timedelta

INTERVALS = [2, 7, 14, 30]


def main():
    parser = argparse.ArgumentParser(description='Generate spaced repetition review dates for a guitar lesson.')
    parser.add_argument('--lesson', required=True, help='Lesson or skill name')
    parser.add_argument('--from-date', default=date.today().isoformat(), help='Start date YYYY-MM-DD')
    args = parser.parse_args()

    start = date.fromisoformat(args.from_date)
    print(f'# Spaced Repetition Plan: {args.lesson}')
    print(f'- Start date: {start.isoformat()}')
    print('')
    print('## Review Schedule')
    for days in INTERVALS:
        d = start + timedelta(days=days)
        print(f'- Day +{days}: {d.isoformat()} - quick review and accuracy check')
    print('')
    print('Rule: if a review feels unstable, repeat the same interval once before moving to the next one.')


if __name__ == '__main__':
    main()
