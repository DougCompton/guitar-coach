#!/usr/bin/env python3
import argparse
import random

PROMPTS = [
    'Improvise with 3 notes only and make two different rhythms.',
    'Strum one chord in 3 dynamics: soft, medium, strong.',
    'Keep the same chord pattern but change the feel from straight to swung.',
    'Create a 2-bar melody from one chord shape on the top 3 strings.',
    'Play one riff, then answer it with a quieter variation.',
    'Use one chord and make it sound different with accents only.',
]


def main():
    p = argparse.ArgumentParser(description='Generate a small creative musicality prompt.')
    p.add_argument('--count', type=int, default=1)
    args = p.parse_args()
    picks = random.sample(PROMPTS, k=min(args.count, len(PROMPTS)))
    print('# Random Musicality Prompts')
    for idx, item in enumerate(picks, start=1):
        print(f'{idx}. {item}')


if __name__ == '__main__':
    main()
