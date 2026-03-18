#!/usr/bin/env python3
import argparse
import re
import sys
from pathlib import Path

# Reconfigure stdout to UTF-8 so sparkline characters print correctly on
# Windows cmd/PowerShell, which defaults to cp1252. errors='replace' falls
# back to '?' on terminals that cannot render the characters rather than
# raising UnicodeEncodeError.
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

DATE_RE = re.compile(r'(\d{4}-\d{2}-\d{2})-guitar-practice\.md$')
PLANNED_RE = re.compile(r'Total planned time:\s*(\d+)')
ACTUAL_RE = re.compile(r'Total actual time:\s*(\d+)')
SKILL_RE = re.compile(r'#skill/([a-z\-]+)')
STATUS_RE = re.compile(r'#status/(repeat|advance|simplify)')
RATING_RE = re.compile(r'Overall rating \(1-10\):\s*(\d+)')
SPARKS = '▁▂▃▄▅▆▇█'


def spark(values):
    if not values:
        return ''
    lo, hi = min(values), max(values)
    if lo == hi:
        return SPARKS[len(SPARKS)//2] * len(values)
    out = []
    for v in values:
        idx = round((v - lo) / (hi - lo) * (len(SPARKS) - 1))
        out.append(SPARKS[idx])
    return ''.join(out)


def extract_int(text, regex):
    m = regex.search(text)
    return int(m.group(1)) if m else 0


def main():
    p = argparse.ArgumentParser(description='Create simple progress charts from practice logs.')
    p.add_argument('--folder', required=True)
    p.add_argument('--limit', type=int, default=14)
    args = p.parse_args()

    rows = []
    for path in sorted(Path(args.folder).glob('*-guitar-practice.md'))[-args.limit:]:
        text = path.read_text(encoding='utf-8')
        m = DATE_RE.search(path.name)
        if not m:
            continue
        rows.append({
            'date': m.group(1),
            'planned': extract_int(text, PLANNED_RE),
            'actual': extract_int(text, ACTUAL_RE),
            'rating': extract_int(text, RATING_RE),
            'status': STATUS_RE.search(text).group(1) if STATUS_RE.search(text) else 'unknown',
            'skills': ','.join(sorted(set(SKILL_RE.findall(text)))) or 'none',
        })
    if not rows:
        raise SystemExit('No practice logs found.')

    actuals = [r['actual'] for r in rows]
    ratings = [r['rating'] for r in rows if r['rating']]
    advance_count = sum(1 for r in rows if r['status'] == 'advance')

    print('# Progress Charts')
    print('')
    print('## Practice minutes')
    print('Dates : ' + ' '.join(r['date'][5:] for r in rows))
    print('Actual: ' + spark(actuals))
    print('Values: ' + ' '.join(str(v) for v in actuals))
    print('')
    if ratings:
        print('## Overall rating trend')
        print('Trend : ' + spark(ratings))
        print('Values: ' + ' '.join(str(v) for v in ratings))
        print('')
    print('## Status summary')
    print(f'- Advance logs: {advance_count}/{len(rows)}')
    print(f'- Total minutes practiced: {sum(actuals)}')
    print('')
    print('## Recent log table')
    for r in rows:
        print(f"- {r['date']}: actual={r['actual']}m, status={r['status']}, skills={r['skills']}")


if __name__ == '__main__':
    main()
