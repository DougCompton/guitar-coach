#!/usr/bin/env python3
import argparse
import re
from collections import Counter
from datetime import datetime, timedelta
from pathlib import Path

DATE_RE = re.compile(r"(\d{4}-\d{2}-\d{2})-guitar-practice\.md$")
RECOMMEND_RE = re.compile(r"Coach recommendation:\s*(.+)")
CURRENT_RE = re.compile(r"Current lesson:\s*(.+)")
GOAL_RE = re.compile(r"Practice goal:\s*(.+)")
ISSUE_RE = re.compile(r"Most common mistake:\s*(.+)")
WEAK_RE = re.compile(r"What still feels weak:\s*(.+)")
RATING_RE = re.compile(r"Overall rating \(1-10\):\s*(\d+)")


def find_logs(folder: Path, days: int):
    cutoff = datetime.today().date() - timedelta(days=days - 1)
    items = []
    for path in sorted(folder.glob('*-guitar-practice.md')):
        m = DATE_RE.search(path.name)
        if not m:
            continue
        day = datetime.strptime(m.group(1), '%Y-%m-%d').date()
        if day >= cutoff:
            items.append((day, path))
    return items


def extract(text: str, regex: re.Pattern[str]) -> str:
    m = regex.search(text)
    return m.group(1).strip() if m else ''


def main():
    parser = argparse.ArgumentParser(description='Summarize recent guitar practice logs into a weekly review.')
    parser.add_argument('--folder', required=True, help='Folder containing daily practice logs')
    parser.add_argument('--days', type=int, default=7, help='Lookback window in days')
    args = parser.parse_args()

    folder = Path(args.folder)
    logs = find_logs(folder, args.days)
    if not logs:
        raise SystemExit('No practice logs found in the requested time window.')

    lessons = Counter()
    goals = Counter()
    issues = Counter()
    recommendations = Counter()
    ratings = []

    for _, path in logs:
        text = path.read_text(encoding='utf-8')
        for value, bucket in [
            (extract(text, CURRENT_RE), lessons),
            (extract(text, GOAL_RE), goals),
            (extract(text, ISSUE_RE), issues),
            (extract(text, WEAK_RE), issues),
            (extract(text, RECOMMEND_RE), recommendations),
        ]:
            if value and value not in {'-', 'n/a', 'none'}:
                bucket[value] += 1
        rating = extract(text, RATING_RE)
        if rating.isdigit():
            ratings.append(int(rating))

    avg = sum(ratings) / len(ratings) if ratings else 0.0

    def top(counter: Counter, label: str) -> str:
        if not counter:
            return f'- {label}: none captured'
        item, count = counter.most_common(1)[0]
        return f'- {label}: {item} ({count}x)'

    print('# Weekly Guitar Review')
    print('')
    print(f'- Logs reviewed: {len(logs)}')
    print(f'- Date range: {logs[0][0].isoformat()} to {logs[-1][0].isoformat()}')
    if ratings:
        print(f'- Average overall rating: {avg:.1f}/10')
    print('')
    print('## Main Focus')
    print(top(lessons, 'Most practiced lesson'))
    print(top(goals, 'Main goal'))
    print('')
    print('## Recurring Weak Spots')
    print(top(issues, 'Top issue'))
    second = issues.most_common(2)
    if len(second) > 1:
        print(f"- Secondary issue: {second[1][0]} ({second[1][1]}x)")
    else:
        print('- Secondary issue: none captured')
    print('')
    print('## Recommendation Pattern')
    print(top(recommendations, 'Most common coach recommendation'))
    print('')
    print('## What should change next week?')
    strongest = goals.most_common(1)[0][0] if goals else (lessons.most_common(1)[0][0] if lessons else 'no clear area')
    lagging = issues.most_common(1)[0][0] if issues else 'no clear weak spot'
    print(f'- Improving fastest: {strongest}')
    print(f'- Lagging most: {lagging}')
    if recommendations:
        top_rec = recommendations.most_common(1)[0][0].lower()
        if 'simplify' in top_rec:
            print('- Overloaded area: current material is too hard or too dense.')
            print('- Reduce next week: tempo, chunk size, or number of simultaneous goals.')
            print('- Ready to advance: nothing yet until the simplified version becomes repeatable.')
        elif 'advance' in top_rec:
            print('- Overloaded area: none obvious from the current notes.')
            print('- Reduce next week: keep only one weak-spot repair block instead of adding more volume.')
            print('- Ready to advance: one lesson or song section that stayed clean in recent logs.')
        else:
            print('- Overloaded area: repeated friction point from the current lesson.')
            print('- Reduce next week: remove one variable and keep the mini-win narrower.')
            print('- Ready to advance: only small pieces that feel stable at current tempo.')
    else:
        print('- Overloaded area: not enough recommendation data yet.')
        print('- Reduce next week: keep the same workload until the logs are more specific.')
        print('- Ready to advance: only after two clean sessions in a row.')
    print('')
    print('## Coach Summary')
    print('- Build the next session around one weak-spot drill, one current-lesson block, one repertoire block, and one easy musical win.')


if __name__ == '__main__':
    main()
