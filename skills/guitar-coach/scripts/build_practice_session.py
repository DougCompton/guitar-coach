#!/usr/bin/env python3
import argparse
from dataclasses import dataclass
from typing import List


@dataclass
class Section:
    name: str
    minutes: int


def alloc_short(total: int, include_weak: bool) -> List[Section]:
    items = [
        Section('Warm-up', 3),
        Section('Lesson Focus', max(4, total - 8)),
        Section('Song / Application', 3),
        Section('Reflection', 2),
    ]
    if include_weak:
        items.insert(1, Section('Weak-Spot Drill', 3))
    return items


def alloc_default(total: int, include_weak: bool) -> List[Section]:
    items = [
        Section('Warm-up', 4),
        Section('Technique', 5),
    ]
    if include_weak:
        items.append(Section('Weak-Spot Drill', 4))
    items.extend([
        Section('Lesson Focus', 7),
        Section('Song / Application', 6),
        Section('Theory / Fretboard', 3),
        Section('Reflection', 1),
    ])
    return items


def alloc_long(total: int, include_weak: bool) -> List[Section]:
    sections = alloc_default(total, include_weak)
    extra = total - sum(s.minutes for s in sections)
    for name in ['Lesson Focus', 'Song / Application', 'Technique']:
        for s in sections:
            if s.name == name and extra > 0:
                bump = min(extra, 4)
                s.minutes += bump
                extra -= bump
    if extra > 0:
        sections.insert(4, Section('Repertoire Review', extra))
    return sections


def choose_sections(total: int, include_weak: bool) -> List[Section]:
    if total <= 20:
        sections = alloc_short(total, include_weak)
    elif total <= 35:
        sections = alloc_default(total, include_weak)
    else:
        sections = alloc_long(total, include_weak)
    delta = total - sum(s.minutes for s in sections)
    order = ['Lesson Focus', 'Song / Application', 'Technique', 'Weak-Spot Drill', 'Theory / Fretboard']
    if delta > 0:
        for name in order:
            for s in sections:
                if s.name == name and delta > 0:
                    s.minutes += 1
                    delta -= 1
    elif delta < 0:
        delta = -delta
        for name in ['Reflection', 'Theory / Fretboard', 'Song / Application']:
            for s in sections:
                if s.name == name and s.minutes > 1 and delta > 0:
                    cut = min(delta, s.minutes - 1)
                    s.minutes -= cut
                    delta -= cut
    return sections


def main():
    parser = argparse.ArgumentParser(description='Compute time allocation for a guitar practice session.')
    parser.add_argument('--minutes', type=int, required=True, help='Total session length in minutes')
    parser.add_argument('--weak-spot', default='', help='Main recurring issue (include to add Weak-Spot Drill block)')
    args = parser.parse_args()

    sections = choose_sections(args.minutes, include_weak=bool(args.weak_spot))
    total = sum(s.minutes for s in sections)

    print('## Session Time Allocation')
    print(f'- Total: {total} minutes')
    print('')
    print('| Section | Minutes |')
    print('|---|---|')
    for s in sections:
        print(f'| {s.name} | {s.minutes} |')


if __name__ == '__main__':
    main()