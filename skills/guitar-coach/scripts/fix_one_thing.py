#!/usr/bin/env python3
import argparse

# Base drill time ratios: isolation (shortest), application (medium), integration (longest)
BASE_DURATIONS = [3, 4, 5]


def main():
    p = argparse.ArgumentParser(description='Compute drill time allocation for a single-issue repair session.')
    p.add_argument('--issue', required=True, help='Issue type (e.g. buzzing, chord-transitions, rhythm)')
    p.add_argument('--minutes', type=int, default=12)
    args = p.parse_args()

    total = args.minutes
    base_total = sum(BASE_DURATIONS)
    scale = total / base_total

    adjusted = []
    used = 0
    for i, mins in enumerate(BASE_DURATIONS):
        new_mins = max(2, round(mins * scale))
        adjusted.append(new_mins)
        used += new_mins

    # Trim or pad to hit exact total
    while used > total:
        for i in range(len(adjusted) - 1, -1, -1):
            if adjusted[i] > 2 and used > total:
                adjusted[i] -= 1
                used -= 1
    while used < total:
        adjusted[-1] += 1
        used += 1

    print('## Drill Time Allocation')
    print(f'- Issue: {args.issue}')
    print(f'- Total: {total} minutes')
    print('')
    print(f'- Drill 1 (Isolation): {adjusted[0]} min')
    print(f'- Drill 2 (Application): {adjusted[1]} min')
    print(f'- Drill 3 (Integration): {adjusted[2]} min')


if __name__ == '__main__':
    main()