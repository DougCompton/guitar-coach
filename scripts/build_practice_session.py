#!/usr/bin/env python3
import argparse
from dataclasses import dataclass
from typing import List


@dataclass
class Section:
    name: str
    minutes: int
    task: str
    form: str
    success: str


def alloc_short(total: int, include_weak: bool) -> List[Section]:
    items = [
        Section('Warm-up', 3, 'Reset posture and play easy controlled movements', 'Keep shoulders loose and breathe normally', 'Place the hands calmly and get 5 clean notes or changes'),
        Section('Lesson Focus', max(4, total - 8), 'Work on the current lesson in short chunks', 'Stay below failure speed and isolate one variable if needed', 'Hit one mini-win 5 clean times'),
        Section('Song / Application', 3, 'Use the lesson in a simple musical loop or song excerpt', 'Keep the pulse moving even if the tempo is slow', 'Play one clean loop without stopping'),
        Section('Reflection', 2, 'Rate the section and choose repeat, simplify, or advance', 'Use digits only for fast feedback', 'Leave one exact next-step note'),
    ]
    if include_weak:
        items.insert(1, Section('Weak-Spot Drill', 3, 'Fix the top recurring issue from recent logs', 'Change only one thing: tempo, chunk size, or hand role', 'Make the repeated mistake happen less often by the end'))
    return items


def alloc_default(total: int, include_weak: bool) -> List[Section]:
    items = [
        Section('Warm-up', 4, 'Reset posture, mobility, and easy coordination', 'Move slowly enough to stay relaxed and precise', 'Finish with 5 clean notes or changes'),
        Section('Technique', 5, 'Use a scale or finger drill linked to the lesson', 'Use tiny motion and steady counting', 'Complete 3 clean reps without rushing'),
    ]
    if include_weak:
        items.append(Section('Weak-Spot Drill', 4, 'Fix the top recurring mistake from recent logs', 'Change one thing only: tempo, chunk size, or hand role', 'Reduce the repeated mistake by the end of the block'))
    items.extend([
        Section('Lesson Focus', 7, 'Primary lesson target in short repeatable chunks', 'Stay below failure speed and keep the motion relaxed', 'Hit the mini-win 5 clean times or reach the BPM rung cleanly'),
        Section('Song / Application', 6, 'Apply the target skill in real music', 'Prioritize groove and continuity over speed', 'Play the excerpt or loop musically without collapsing'),
        Section('Theory / Fretboard', 3, 'Connect the lesson to intervals, triads, or chord construction on the guitar', 'Say the concept before or while playing it', 'Prove the theory on the instrument, not only in words'),
        Section('Reflection', 1, 'Log results and pick the next action', 'Answer with digits only and note one correction', 'End with a clear next-step recommendation'),
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
        sections.insert(4, Section('Repertoire Review', extra, 'Review older material to keep it alive', 'Use easy wins to rebuild confidence', 'Play a previously learned piece cleanly once through'))
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


def reflection_block() -> str:
    return """Reply with numbers only: Q1, Q2, Q3, Q4\n1. Difficulty  1) Very easy  2) Manageable  3) Challenging  4) Too hard\n2. Accuracy    1) Clean  2) A few mistakes  3) Frequent mistakes  4) Fell apart\n3. Timing      1) Steady  2) Slightly off  3) Unstable  4) Lost pulse\n4. Tension     1) None  2) Mild  3) Noticeable  4) Pain"""


def main():
    parser = argparse.ArgumentParser(description='Generate a structured guitar practice session.')
    parser.add_argument('--minutes', type=int, required=True, help='Total session length in minutes')
    parser.add_argument('--lesson', required=True, help='Current lesson focus')
    parser.add_argument('--application', default='Use the lesson in a short riff, chord loop, or song section', help='Application focus')
    parser.add_argument('--technique', default='Use a matching scale, picking, or finger-independence drill', help='Technique focus')
    parser.add_argument('--theory', default='Connect the lesson to intervals on one string, top-3-string triads, or chord construction from known shapes', help='Theory or ear focus')
    parser.add_argument('--weak-spot', default='', help='Main recurring issue to target with a short corrective drill')
    args = parser.parse_args()

    sections = choose_sections(args.minutes, include_weak=bool(args.weak_spot))
    print("## Today's Goal")
    print(f'Build control and confidence around: {args.lesson}')
    if args.weak_spot:
        print(f'Secondary goal: reduce the recurring weak spot: {args.weak_spot}')
    print('')
    print('## Practice Plan')
    total = 0
    for idx, s in enumerate(sections, start=1):
        task = s.task
        if s.name == 'Lesson Focus':
            task = args.lesson
        elif s.name == 'Song / Application':
            task = args.application
        elif s.name == 'Technique':
            task = args.technique
        elif s.name == 'Theory / Fretboard':
            task = args.theory
        elif s.name == 'Weak-Spot Drill' and args.weak_spot:
            task = args.weak_spot
        print(f'{idx}. {s.name} - {s.minutes} min')
        print(f'   - Practice: {task}')
        print(f'   - Good form: {s.form}')
        print(f'   - Mini-win: {s.success}')
        total += s.minutes
    print('')
    print(f'Total scheduled time: {total} minutes')
    print('')
    print('## Start Section 1')
    first = sections[0]
    print(f'Section: {first.name}')
    print(f'Timer: Run practice_timer.py for {first.minutes} minutes')
    print(f'Reflection when done:\n{reflection_block()}')


if __name__ == '__main__':
    main()
