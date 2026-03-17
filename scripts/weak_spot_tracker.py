#!/usr/bin/env python3
import argparse
import re
from collections import Counter
from pathlib import Path

KEYWORDS = {
    'chord-transitions': ['chord change', 'switch', 'transition', 'fretting'],
    'rhythm-timing': ['timing', 'rhythm', 'pulse', 'rushed', 'dragged', 'strumming'],
    'string-noise': ['buzz', 'muted', 'string noise', 'clean notes'],
    'tension-posture': ['tension', 'pain', 'wrist', 'thumb', 'fatigue'],
    'picking-control': ['picking', 'alternate picking', 'right hand'],
    'memory-confidence': ['memory', 'forgot', 'confidence', 'ready'],
}

SECTION_RE = re.compile(r'## Section .*?(?=\n## |\Z)', re.S)
FIELD_RE = re.compile(r'(Difficulty notes|Tension or pain|Coach note):\s*(.*)')

DRILLS = {
    'chord-transitions': '2-minute slow chord-pair changes with no strumming, then 2 minutes with quarter-note strums',
    'rhythm-timing': '2-minute clap-and-count drill, then 3 minutes with metronome on one chord',
    'string-noise': '3-minute fretting pressure test: fret just hard enough for a clean note on each string',
    'tension-posture': '2-minute posture reset and shake-out, then 3 minutes of extra-slow reps with relaxed shoulders',
    'picking-control': '3-minute open-string alternate picking at a slow tempo with tiny motion',
    'memory-confidence': '2-minute chunk recall on one bar at a time, then 3 clean restarts from the same spot',
}


def analyze(folder: Path, limit: int):
    counts = Counter()
    logs = sorted(folder.glob('*-guitar-practice.md'))[-limit:]
    for path in logs:
        text = path.read_text(encoding='utf-8').lower()
        for match in SECTION_RE.finditer(text):
            block = match.group(0)
            notes = ' '.join(value for _, value in FIELD_RE.findall(block))
            for key, terms in KEYWORDS.items():
                if any(term in notes for term in terms):
                    counts[key] += 1
    return logs, counts


def main():
    parser = argparse.ArgumentParser(description='Find repeated weak spots in recent guitar practice logs.')
    parser.add_argument('--folder', required=True, help='Folder containing daily practice logs')
    parser.add_argument('--limit', type=int, default=10, help='Number of recent logs to inspect')
    args = parser.parse_args()

    logs, counts = analyze(Path(args.folder), args.limit)
    if not logs:
        raise SystemExit('No practice logs found.')

    print('# Weak Spot Review')
    print(f'- Logs scanned: {len(logs)}')
    if not counts:
        print('- No recurring weak spots found from the captured notes.')
        print('- Recommendation: continue the current lesson and keep logging specific errors.')
        return

    print('')
    print('## Recurring Problems')
    for issue, count in counts.most_common(5):
        print(f'- {issue}: {count} hits')
    print('')
    print('## Next Session Priorities')
    for issue, _ in counts.most_common(3):
        print(f'- {issue}: {DRILLS[issue]}')


if __name__ == '__main__':
    main()
