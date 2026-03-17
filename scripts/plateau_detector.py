#!/usr/bin/env python3
import argparse
import re
from collections import Counter
from pathlib import Path

ISSUE_TAG_RE = re.compile(r'#issue/([a-z0-9\-]+)')
STATUS_RE = re.compile(r'#status/(repeat|advance|simplify)')
TEXT_KEYS = {
    'buzzing': ['buzz', 'string noise', 'clean notes'],
    'rhythm': ['timing', 'rhythm', 'pulse', 'rushed', 'dragged'],
    'chord-transitions': ['chord change', 'transition', 'switch'],
    'tension': ['tension', 'pain', 'fatigue', 'wrist'],
}


def main():
    p = argparse.ArgumentParser(description='Detect practice plateaus from recent logs.')
    p.add_argument('--folder', required=True)
    p.add_argument('--limit', type=int, default=8)
    args = p.parse_args()
    logs = sorted(Path(args.folder).glob('*-guitar-practice.md'))[-args.limit:]
    if len(logs) < 3:
        print('# Plateau Detector')
        print(f'- Logs scanned: {len(logs)}')
        print('')
        print('## Plateau status: not enough data')
        print('- Add at least one more practice log before making a confidence-based plateau call.')
        return

    issues = Counter()
    statuses = Counter()
    for path in logs:
        text = path.read_text(encoding='utf-8').lower()
        for issue in ISSUE_TAG_RE.findall(text):
            issues[issue] += 1
        for status in STATUS_RE.findall(text):
            statuses[status] += 1
        for key, terms in TEXT_KEYS.items():
            if any(term in text for term in terms):
                issues[key] += 1

    top_issue, top_count = issues.most_common(1)[0] if issues else ('none', 0)
    plateau = top_count >= max(3, len(logs) // 2) and statuses['advance'] <= 1

    print('# Plateau Detector')
    print(f'- Logs scanned: {len(logs)}')
    print(f'- Top repeated issue: {top_issue} ({top_count} hits)')
    print(f'- Repeat tags: {statuses["repeat"]}')
    print(f'- Simplify tags: {statuses["simplify"]}')
    print(f'- Advance tags: {statuses["advance"]}')
    print('')
    print(f'## Plateau status: {"yes" if plateau else "no"}')
    print('')
    print('## Coach action')
    if plateau:
        print('- Do not keep repeating the same full drill.')
        print('- Reduce tempo or range immediately.')
        print('- Shorten the loop to one bar or one transition.')
        print('- Switch the first session block to a fix-one-thing drill.')
        print('- Require one small clean win before re-expanding.')
    else:
        print('- Progress is still moving enough to stay with the current plan.')
        print('- Keep one weak-spot drill near the front and reassess after 2 more logs.')


if __name__ == '__main__':
    main()
