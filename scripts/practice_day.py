#!/usr/bin/env python3
import argparse
import re
from datetime import date
from pathlib import Path

from start_here import choose_current_lesson, pick_repertoire, scan_weak_spots, warmup_for, theory_prompt, allocate
from readiness_check import choose_session

SLUG_RE = re.compile(r'[^a-z0-9]+')


def slugify(text: str) -> str:
    return SLUG_RE.sub('-', text.strip().lower()).strip('-') or 'lesson'


def status_from_session(session_type: str) -> str:
    return 'repeat' if session_type in {'review-only', 'low-friction', 'recovery'} else 'advance'


def create_log(folder: Path, active: str, lesson_title: str, minutes: int, repertoire: str, weak_spots, session_type: str, sections):
    today = date.today().isoformat()
    path = folder / f'{today}-guitar-practice.md'
    lesson_slug = slugify(lesson_title)
    tags = [f'#roadmap/{active}', f'#lesson/{lesson_slug}', f'#status/{status_from_session(session_type)}']
    for issue, _count in weak_spots[:2]:
        tags.append(f'#issue/{slugify(issue)}')
    skills = ['#skill/chords', '#skill/rhythm']
    if active == 'fingerstyle':
        skills.append('#skill/fingerstyle')
    body = [
        f'# Guitar Practice Log - {today}',
        '',
        '## Summary',
        f'- Total planned time: {minutes}',
        '- Total actual time: ',
        f'- Active roadmap: {active}',
        f'- Current lesson: {lesson_title}',
        f'- Repertoire lane target: {repertoire}',
        f'- Practice goal: {lesson_title}',
        '',
        '## Tags',
        ' '.join(tags + skills),
        '',
        '## Sections',
    ]
    for idx, sec in enumerate(sections, start=1):
        body.extend([
            f'### {idx}. {sec[0]}',
            f'- Minutes: {sec[1]}',
            f'- What I practiced: {sec[2]}',
            f'- Mini-win target: {sec[3]}',
            '- Result: ',
            '- Reflection: ',
            '',
        ])
    body.extend([
        '## Mastery Signals',
        '- Chords: ',
        '- Rhythm: ',
        '- Scales: ',
        '- Fingerstyle: ',
        '- Repertoire: ',
        '- Fretboard knowledge: ',
        '',
        '## Tension / Pain Check',
        '- Rating: ',
        '- Notes: ',
        '',
        '## Coach Recommendation',
        '- Repeat, simplify, or advance: ',
        '- Next session priority: ',
        '',
    ])
    path.write_text('\n'.join(body), encoding='utf-8')
    return path


def main():
    p = argparse.ArgumentParser(description='Run the one-command practice day planner.')
    p.add_argument('--folder', required=True)
    p.add_argument('--minutes', type=int, default=30)
    p.add_argument('--energy', type=int, default=3)
    p.add_argument('--focus', type=int, default=3)
    p.add_argument('--tension', type=int, default=1)
    p.add_argument('--pain', type=int, default=1)
    args = p.parse_args()
    folder = Path(args.folder)
    folder.mkdir(parents=True, exist_ok=True)
    logs_folder = folder / 'logs'
    logs_folder.mkdir(parents=True, exist_ok=True)

    session_type, reason = choose_session(args.minutes, args.energy, args.focus, args.tension, args.pain)
    active, roadmap_path, lesson = choose_current_lesson(folder)
    lesson_title = lesson.title
    repertoire = pick_repertoire(folder)
    weak_spots = scan_weak_spots(logs_folder, 8)
    warm_name, warm_win = warmup_for(active, lesson)
    theory_name, theory_win = theory_prompt(active, lesson)
    raw_sections = allocate(args.minutes, len(weak_spots))
    sections = []
    for name, mins in raw_sections:
        if name == 'Warm-up':
            sections.append((name, mins, warm_name, warm_win))
        elif name == 'Lesson Focus':
            sections.append((name, mins, lesson_title, f'Complete one clean, repeatable win inside {mins} minutes.'))
        elif name == 'Technique':
            sections.append((name, mins, 'Tempo ladder or finger exercise', 'Stay relaxed and complete 3 clean reps before moving up.'))
        elif name == 'Weak-Spot Drill':
            issue = weak_spots[0][0] if weak_spots else 'cleanup'
            sections.append((name, mins, issue, f'Correct the issue with one small clean success before the block ends.'))
        elif name == 'Song / Application':
            sections.append((name, mins, repertoire, 'Play one phrase or loop cleanly in context 3 times in a row.'))
        elif name in {'Theory / Ear', 'Theory / Fretboard'}:
            sections.append((name, mins, theory_name, theory_win))
        else:
            sections.append((name, mins, 'Wrap-up reflection', 'Write one next-step note and one status tag.'))

    if session_type == 'recovery':
        sections = [s for s in sections if s[0] in {'Warm-up', 'Technique', 'Wrap-up'}]
    elif session_type == 'review-only':
        sections = [s for s in sections if s[0] in {'Warm-up', 'Weak-Spot Drill', 'Song / Application', 'Wrap-up'}]

    log_path = create_log(logs_folder, active, lesson_title, args.minutes, repertoire, weak_spots, session_type, sections)

    print('# Practice Day')
    print(f'- Session type: {session_type}')
    print(f'- Why: {reason}')
    print(f'- Active roadmap: {active}')
    print(f'- Current lesson: {lesson_title}')
    print(f'- Repertoire: {repertoire}')
    print(f'- Weak spots: {", ".join(issue for issue, _ in weak_spots[:2]) if weak_spots else "none found"}')
    print(f'- Daily log: {log_path}')
    print('')
    for idx, sec in enumerate(sections, start=1):
        print(f'## {idx}. {sec[0]} ({sec[1]} min)')
        print(f'- Practice: {sec[2]}')
        print(f'- Mini-win: {sec[3]}')


if __name__ == '__main__':
    main()
