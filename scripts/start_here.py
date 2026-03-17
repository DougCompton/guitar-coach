#!/usr/bin/env python3
import argparse
import re
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

ISSUE_KEYWORDS = {
    'chord-transitions': ['chord change', 'switch', 'transition', 'fretting'],
    'rhythm-timing': ['timing', 'rhythm', 'pulse', 'rushed', 'dragged', 'strumming'],
    'string-noise': ['buzz', 'muted', 'string noise', 'clean notes'],
    'tension-posture': ['tension', 'pain', 'wrist', 'thumb', 'fatigue'],
    'picking-control': ['picking', 'alternate picking', 'right hand'],
    'memory-confidence': ['memory', 'forgot', 'confidence', 'ready'],
}

WEAK_DRILLS = {
    'chord-transitions': ('slow chord-pair changes', 'Play one chord pair cleanly 5 times in a row'),
    'rhythm-timing': ('clap-count-strum pulse drill', 'Keep the count steady for 2 straight minutes'),
    'string-noise': ('light-pressure clean-note test', 'Play the target string set with no extra noise 5 times'),
    'tension-posture': ('posture reset with extra-slow reps', 'Finish the block with loose shoulders and no pain'),
    'picking-control': ('open-string picking control drill', 'Complete 3 clean reps with tiny motion'),
    'memory-confidence': ('micro-loop recall drill', 'Restart the chunk cleanly 3 times from memory'),
}

CURRENT_RE = re.compile(r'- Current roadmap:\s*([\w-]+)', re.I)
LESSON_BLOCK_RE = re.compile(r'## Lesson\s+(\d+)\s+(.*?)(?=\n## Lesson\s+\d+|\Z)', re.S)
TITLE_RE = re.compile(r'- Title:\s*(.+)')
STATUS_RE = re.compile(r'- Status:\s*(.+)')
GOAL_RE = re.compile(r'- Goal:[ \t]*([^\n]*)')
APP_RE = re.compile(r'- Application:[ \t]*([^\n]*)')
FIELD_RE = re.compile(r'(Difficulty notes|Tension or pain|Coach note|Most common mistake|What still feels weak):\s*(.*)', re.I)
DATE_GLOB = '*-guitar-practice.md'

DEFAULT_REPERTOIRE = """# Repertoire Lane

## Learning
- Song: Two-chord groove in G
  - Status: learning
  - Focus: keep the pulse steady through changes
  - Current excerpt: 4-bar loop
  - Notes:

## Polishing
- Song: Simple open-chord song
  - Status: polishing
  - Focus: smoother transitions and cleaner strumming
  - Current excerpt: verse
  - Notes:

## Maintenance
- Song: Familiar chord loop review
  - Status: maintenance
  - Focus: easy musical win
  - Current excerpt: full loop
  - Notes:
"""

@dataclass
class Lesson:
    number: int
    title: str
    status: str
    goal: str
    application: str


def read_active_name(folder: Path) -> str:
    p = folder / 'active-roadmap.md'
    if not p.exists():
        return 'beginner'
    text = p.read_text(encoding='utf-8')
    m = CURRENT_RE.search(text)
    return m.group(1).strip().lower() if m else 'beginner'


def parse_lessons(roadmap_path: Path):
    text = roadmap_path.read_text(encoding='utf-8')
    lessons = []
    for num, block in LESSON_BLOCK_RE.findall(text):
        title = TITLE_RE.search(block)
        status = STATUS_RE.search(block)
        goal = GOAL_RE.search(block)
        app = APP_RE.search(block)
        lessons.append(Lesson(
            number=int(num),
            title=title.group(1).strip() if title else f'Lesson {num}',
            status=(status.group(1).strip().lower() if status else 'queued'),
            goal=goal.group(1).strip() if goal and goal.group(1).strip() not in {'', '-'} else '',
            application=app.group(1).strip() if app and app.group(1).strip() not in {'', '-'} else '',
        ))
    return lessons


def choose_current_lesson(folder: Path):
    active = read_active_name(folder)
    roadmap = folder / f'roadmap-{active}.md'
    if not roadmap.exists():
        raise SystemExit(f'Missing roadmap file: {roadmap.name}')
    lessons = parse_lessons(roadmap)
    current = next((x for x in lessons if x.status == 'current'), lessons[0] if lessons else None)
    if not current:
        raise SystemExit('No lessons found in roadmap.')
    return active, roadmap, current


def ensure_repertoire(folder: Path) -> Path:
    p = folder / 'repertoire.md'
    if not p.exists():
        p.write_text(DEFAULT_REPERTOIRE, encoding='utf-8')
    return p


def pick_repertoire(folder: Path) -> str:
    p = ensure_repertoire(folder)
    text = p.read_text(encoding='utf-8').splitlines()
    current_section = ''
    picks = []
    for line in text:
        line = line.rstrip()
        if line.startswith('## '):
            current_section = line[3:].strip().lower()
        elif line.lstrip().startswith('- Song:'):
            song = line.split(':', 1)[1].strip()
            picks.append((current_section, song))
    priority = ['learning', 'polishing', 'maintenance']
    for want in priority:
        for section, song in picks:
            if section == want:
                return f'{song} ({want})'
    return 'Use a familiar riff or chord loop (maintenance)'


def scan_weak_spots(folder: Path, limit: int):
    counts = Counter()
    logs = sorted(folder.glob(DATE_GLOB))[-limit:]
    for path in logs:
        text = path.read_text(encoding='utf-8').lower()
        notes = ' '.join(value for _, value in FIELD_RE.findall(text))
        for key, terms in ISSUE_KEYWORDS.items():
            if any(term in notes for term in terms):
                counts[key] += 1
    return counts.most_common(2)


def theory_prompt(active: str, lesson: Lesson) -> tuple[str, str]:
    title = lesson.title.lower()
    if 'triad' in title:
        return ('triads on top 3 strings', 'Name the triad quality and play one inversion cleanly 3 times')
    if 'scale' in title or 'modal' in title:
        return ('intervals on one string connected to today\'s scale', 'Name the interval before you play it 4 times correctly')
    if 'chord' in title or 'strumming' in title:
        return ('build today\'s chord from shapes you already know', 'Explain root-third-fifth while holding the shape once')
    if active == 'fingerstyle':
        return ('top-3-string triad plus thumb-bass connection', 'Play the shape and say which note is on top')
    return ('intervals on one string and chord construction from known shapes', 'Connect one theory fact directly to the fretboard')


def warmup_for(active: str, lesson: Lesson) -> tuple[str, str]:
    title = lesson.title.lower()
    if 'fingerstyle' in active:
        return ('thumb-index-middle-ring string assignment reset', 'Play the pattern evenly for 60 seconds')
    if 'celtic' in active:
        return ('open-string drone and ornament prep', 'Keep the drone ringing while adding one ornament cleanly')
    if 'scale' in title or 'picking' in title:
        return ('1-2-3-4 finger warmup on two strings', 'Complete 2 clean passes with relaxed shoulders')
    return ('slow open-chord reset with posture check', 'Make 5 clean fretting placements with no rushing')


def allocate(total: int, weak_count: int) -> list[tuple[str, int]]:
    if total <= 12:
        base = [('Warm-up', 2), ('Lesson Focus', 4), ('Song / Application', 4), ('Reflection', 2)]
    elif total <= 20:
        base = [('Warm-up', 3), ('Weak-Spot Drill', 3 if weak_count else 0), ('Lesson Focus', 6), ('Song / Application', 5), ('Theory / Fretboard', 2), ('Reflection', 1)]
    else:
        base = [('Warm-up', 4), ('Weak-Spot Drill', 4 if weak_count else 0), ('Technique', 5), ('Lesson Focus', 7), ('Song / Application', 6), ('Theory / Fretboard', 3), ('Reflection', 1)]
    parts = [(name, mins) for name, mins in base if mins > 0]
    total_now = sum(m for _, m in parts)
    idx_order = ['Lesson Focus', 'Song / Application', 'Technique', 'Weak-Spot Drill']
    extra = total - total_now
    if extra > 0:
        for name in idx_order:
            for i, (n, m) in enumerate(parts):
                if n == name and extra > 0:
                    bump = min(extra, 2)
                    parts[i] = (n, m + bump)
                    extra -= bump
    elif extra < 0:
        extra = -extra
        for name in ['Reflection', 'Theory / Fretboard', 'Song / Application']:
            for i, (n, m) in enumerate(parts):
                if n == name and extra > 0 and m > 1:
                    cut = min(extra, m - 1)
                    parts[i] = (n, m - cut)
                    extra -= cut
    if extra > 0:
        for name in ['Lesson Focus', 'Song / Application', 'Technique', 'Weak-Spot Drill']:
            for i, (n, m) in enumerate(parts):
                if n == name and extra > 0:
                    parts[i] = (n, m + 1)
                    extra -= 1
    return parts


def main():
    parser = argparse.ArgumentParser(description='Create a daily start-here guitar practice plan.')
    parser.add_argument('--folder', required=True, help='Notes root folder containing roadmaps and repertoire')
    parser.add_argument('--minutes', type=int, default=30, help='Target practice duration')
    parser.add_argument('--log-limit', type=int, default=8, help='How many recent logs to scan for weak spots')
    args = parser.parse_args()

    folder = Path(args.folder)
    logs_folder = folder / 'logs'
    active, roadmap_path, lesson = choose_current_lesson(folder)
    repertoire = pick_repertoire(folder)
    weak_spots = scan_weak_spots(logs_folder, args.log_limit)
    warm_name, warm_win = warmup_for(active, lesson)
    theory_name, theory_win = theory_prompt(active, lesson)
    sections = allocate(args.minutes, len(weak_spots))

    print('# Start Here')
    print(f'- Active roadmap: {active}')
    print(f'- Roadmap file: {roadmap_path.name}')
    print(f'- Today\'s lesson: Lesson {lesson.number} - {lesson.title}')
    print(f'- Repertoire lane pick: {repertoire}')
    print('')
    print('## Top weak spots from recent logs')
    if weak_spots:
        for issue, count in weak_spots:
            drill, win = WEAK_DRILLS.get(issue, ('target the repeated issue', 'Reduce the repeated issue by the end of the block'))
            print(f'- {issue} ({count} hits): {drill} | mini-win: {win}')
    else:
        print('- None clearly repeated yet. Use the slot for easy review or tempo cleanup.')
    print('')
    print('## Session plan')
    for i, (name, mins) in enumerate(sections, start=1):
        if name == 'Warm-up':
            practice = warm_name
            mini = warm_win
        elif name == 'Weak-Spot Drill' and weak_spots:
            issue = weak_spots[0][0]
            practice, mini = WEAK_DRILLS.get(issue, ('fix the top issue', 'End with one clean rep'))
        elif name == 'Technique':
            practice = f'Technique linked to {lesson.title.lower()}'
            mini = 'Complete 3 clean reps without rushing or excess tension'
        elif name == 'Lesson Focus':
            practice = lesson.title
            mini = lesson.goal if lesson.goal and lesson.goal != '-' else 'Hit one clear target 5 clean times'
        elif name == 'Song / Application':
            practice = repertoire
            mini = lesson.application if lesson.application and lesson.application != '-' else 'Keep the music moving for one clean loop'
        elif name == 'Theory / Fretboard':
            practice = theory_name
            mini = theory_win
        else:
            practice = 'Log results and choose repeat, simplify, or advance'
            mini = 'Leave one precise next-step note'
        print(f'{i}. {name} - {mins} min')
        print(f'   - Practice: {practice}')
        print(f'   - Mini-win: {mini}')
    print('')
    print('Reply with: 1 to run this plan, 2 to shorten it, 3 to make it easier, 4 to switch roadmap.')


if __name__ == '__main__':
    main()
