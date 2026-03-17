#!/usr/bin/env python3
import argparse

LEFT = {
    'fretting-hand-pressure': {
        'prompt': 'Left-hand pressure check',
        'q': 'Pressure: 1 light, 2 manageable, 3 squeezing, 4 painful',
        'drills': {
            1: 'Keep current touch. Play the phrase 5 times while keeping unused fingers relaxed.',
            2: 'Play at half speed and lift pressure between notes for 60 seconds.',
            3: 'Fret each note with the minimum pressure needed for a clean tone. Reset after every rep.',
            4: 'Stop the hard passage. Do open strings, slow placement, and posture reset only.'
        }
    },
    'finger-placement': {
        'prompt': 'Finger placement check',
        'q': 'Placement: 1 clean, 2 mostly clean, 3 frequent misses, 4 cannot land shape',
        'drills': {
            1: 'Keep the shape and add one-string-at-a-time accuracy reps.',
            2: 'Use slow silent landings before sounding the notes 5 times.',
            3: 'Break the shape into 2-note chunks and rebuild it slowly.',
            4: 'Simplify to one finger pair or one chord change only.'
        }
    },
    'thumb-independence': {
        'prompt': 'Thumb independence check',
        'q': 'Thumb independence: 1 steady, 2 slight drift, 3 unstable, 4 collapses pattern',
        'drills': {
            1: 'Keep the thumb pulse and add melody notes lightly.',
            2: 'Isolate thumb-only bass for 60 seconds, then re-add one upper note.',
            3: 'Alternate thumb on two bass strings while counting aloud.',
            4: 'Return to open-string thumb pulse only.'
        }
    },
}

RIGHT = {
    'picking-hand-consistency': {
        'prompt': 'Picking consistency check',
        'q': 'Consistency: 1 even, 2 small misses, 3 uneven attack, 4 frequent misses',
        'drills': {
            1: 'Keep current motion and add a 10-BPM tempo ladder.',
            2: 'Use open-string alternate picking with tiny motion for 90 seconds.',
            3: 'Play two notes only, repeating with matched attack and volume.',
            4: 'Stop the pattern and reset on one string only.'
        }
    },
    'strumming-motion': {
        'prompt': 'Strumming motion check',
        'q': 'Motion: 1 loose, 2 slightly tight, 3 rigid, 4 out of control',
        'drills': {
            1: 'Keep the groove and change only dynamics.',
            2: 'Use muted strings and count down-up evenly for 1 minute.',
            3: 'Strum one chord with smaller motion and slower count.',
            4: 'Strip back to quarter-note downstrokes on muted strings.'
        }
    },
}


def main():
    p = argparse.ArgumentParser(description='Run left-hand or right-hand guitar diagnostics.')
    p.add_argument('--hand', choices=['left', 'right'], required=True)
    args = p.parse_args()
    bank = LEFT if args.hand == 'left' else RIGHT

    print(f'# {args.hand.title()}-Hand Diagnostic Mode')
    print('Reply with numbers only, one per line item.')
    print('')
    for idx, (name, item) in enumerate(bank.items(), start=1):
        print(f'{idx}. {item["prompt"]}')
        print(f'   - Key: {name}')
        print(f'   - {item["q"]}')
    print('')
    print('## Drill map')
    for name, item in bank.items():
        print(f'- {name}')
        for score in [1, 2, 3, 4]:
            print(f'  - {score}: {item["drills"][score]}')


if __name__ == '__main__':
    main()
