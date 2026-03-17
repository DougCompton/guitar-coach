#!/usr/bin/env python3
import argparse
import re
from collections import defaultdict
from pathlib import Path

DATE_GLOB = '*-guitar-practice.md'
RATING_RE = re.compile(r'Overall rating \(1-10\):\s*(\d+)')
TEXT_PATTERNS = {
    'chords': ['chord', 'transition', 'strumming'],
    'rhythm': ['rhythm', 'timing', 'pulse', 'metronome'],
    'scales': ['scale', 'finger exercise', 'alternate picking', 'position shift'],
    'fingerstyle': ['fingerstyle', 'travis', 'thumb', 'pattern'],
    'repertoire': ['song', 'application', 'verse', 'chorus', 'riff'],
    'fretboard-knowledge': ['interval', 'triad', 'theory', 'fretboard', 'construction'],
}


def clamp(v: int) -> int:
    return max(1, min(10, v))


def score_text(text: str) -> dict[str, int]:
    lower = text.lower()
    overall_match = RATING_RE.search(text)
    overall = int(overall_match.group(1)) if overall_match else 6
    scores = {k: [] for k in TEXT_PATTERNS}
    for area, terms in TEXT_PATTERNS.items():
        if any(term in lower for term in terms):
            value = overall
            if 'advance' in lower and area in lower:
                value += 1
            if 'simplify' in lower or 'too hard' in lower or 'pain' in lower:
                value -= 1
            if 'steady' in lower and area in ('rhythm', 'chords', 'repertoire'):
                value += 1
            if 'clean' in lower:
                value += 1
            if 'fell apart' in lower or 'lost pulse' in lower:
                value -= 2
            scores[area].append(clamp(value))
    return {k: round(sum(v)/len(v)) for k, v in scores.items() if v}


def main():
    parser = argparse.ArgumentParser(description='Estimate mastery scores by guitar skill type from recent logs.')
    parser.add_argument('--folder', required=True, help='Folder containing practice markdown files')
    parser.add_argument('--limit', type=int, default=12, help='Number of recent logs to inspect')
    args = parser.parse_args()

    folder = Path(args.folder)
    logs = sorted(folder.glob(DATE_GLOB))[-args.limit:]
    if not logs:
        raise SystemExit('No practice logs found.')

    totals = defaultdict(list)
    for path in logs:
        scores = score_text(path.read_text(encoding='utf-8'))
        for area, value in scores.items():
            totals[area].append(value)

    print('# Mastery Scorecard')
    print(f'- Logs scanned: {len(logs)}')
    print('- Scale: 1=fragile, 10=consistently usable')
    print('')
    for area in ['chords', 'rhythm', 'scales', 'fingerstyle', 'repertoire', 'fretboard-knowledge']:
        vals = totals.get(area, [])
        if vals:
            score = round(sum(vals) / len(vals), 1)
            status = 'build' if score < 5 else 'develop' if score < 7.5 else 'solid'
            print(f'- {area}: {score}/10 ({status})')
        else:
            print(f'- {area}: no recent evidence yet')

    print('')
    weakest = sorted([(sum(v)/len(v), k) for k, v in totals.items() if v])
    if weakest:
        print(f'- Lowest active area: {weakest[0][1]}')
    else:
        print('- Lowest active area: no data yet')

if __name__ == "__main__":
    main()
