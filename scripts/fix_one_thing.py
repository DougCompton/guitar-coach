#!/usr/bin/env python3
import argparse

ISSUES = {
    'buzzing': {
        'focus': 'clean fretting pressure and fingertip placement',
        'drills': [
            ('Pressure test', 3, 'Fret one note per string using the lightest pressure that still sounds clean 5 times in a row.'),
            ('Chord freeze', 4, 'Form the problem chord, pluck each string slowly, then reset and repeat 4 clean rounds.'),
            ('Transition cleanup', 5, 'Move between the two problem shapes at half speed until 5 clean changes happen in a row.'),
        ],
    },
    'chord-transitions': {
        'focus': 'efficient movement between shapes',
        'drills': [
            ('Silent switches', 3, 'Switch between the two shapes without strumming until 8 relaxed changes are clean.'),
            ('Quarter-note changes', 4, 'Strum one beat per chord with a metronome and complete 6 clean changes.'),
            ('Two-bar loop', 5, 'Loop the transition in context without stopping for 3 full clean rounds.'),
        ],
    },
    'rhythm': {
        'focus': 'stable pulse and count awareness',
        'drills': [
            ('Clap and count', 2, 'Clap quarter notes and say counts out loud without drifting for 60 seconds.'),
            ('One-chord groove', 4, 'Play one strum pattern on one chord and keep time steady for 2 straight minutes.'),
            ('Context loop', 5, 'Apply the groove to the target progression for 3 clean loops.'),
        ],
    },
    'string-noise': {
        'focus': 'muting and contact control',
        'drills': [
            ('Isolation', 3, 'Play the target notes slowly and stop each unwanted ringing string 5 times cleanly.'),
            ('Slow loop', 4, 'Repeat the noisy passage at half speed with deliberate muting for 4 clean reps.'),
            ('Context rep', 5, 'Play the full passage and keep stray noise below one mistake per rep.'),
        ],
    },
    'fingerstyle': {
        'focus': 'thumb-finger independence and even tone',
        'drills': [
            ('Thumb pulse', 3, 'Keep the bass note steady for 60 seconds without breaking tempo.'),
            ('Add fingers', 4, 'Layer the treble pattern on top and keep all notes even for 4 clean passes.'),
            ('Bar loop', 5, 'Repeat one bar of the pattern until 3 clean bar-length reps happen in a row.'),
        ],
    },
    'picking': {
        'focus': 'small motion and string tracking',
        'drills': [
            ('Open-string alternate picking', 3, 'Keep motion tiny and even for 45 seconds per string.'),
            ('Crossing drill', 4, 'Alternate between two adjacent strings for 8 clean crossings.'),
            ('Phrase loop', 5, 'Play the problem picking fragment 5 times with no collapse in motion.'),
        ],
    },
}


def main():
    p = argparse.ArgumentParser(description='Generate a compact repair session for one guitar problem.')
    p.add_argument('--issue', required=True, choices=sorted(ISSUES))
    p.add_argument('--minutes', type=int, default=12)
    args = p.parse_args()

    data = ISSUES[args.issue]
    total = sum(m for _, m, _ in data['drills'])
    scale = args.minutes / total
    adjusted = []
    used = 0
    for i, (name, mins, goal) in enumerate(data['drills']):
        new_mins = max(2, round(mins * scale))
        adjusted.append((name, new_mins, goal))
        used += new_mins
    while used > args.minutes:
        for i in range(len(adjusted) - 1, -1, -1):
            name, mins, goal = adjusted[i]
            if mins > 2 and used > args.minutes:
                adjusted[i] = (name, mins - 1, goal)
                used -= 1
    while used < args.minutes:
        name, mins, goal = adjusted[-1]
        adjusted[-1] = (name, mins + 1, goal)
        used += 1

    print('# Fix One Thing Session')
    print(f'- Target issue: {args.issue}')
    print(f'- Main focus: {data["focus"]}')
    print(f'- Total time: {args.minutes} minutes')
    print('')
    for idx, (name, mins, goal) in enumerate(adjusted, start=1):
        print(f'## {idx}. {name} ({mins} min)')
        print(f'- Mini-win: {goal}')
    print('')
    print('Finish with one numeric reflection reply: difficulty, accuracy, tension, confidence.')


if __name__ == '__main__':
    main()
