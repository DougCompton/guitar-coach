#!/usr/bin/env python3
"""
analyze_logs.py — extract structured data from guitar practice logs.

Outputs two parts:
  Part 1: Markdown table — one row per log with key fields
  Part 2: Narrative section — full free-text fields per log

Usage:
  python analyze_logs.py --folder ~/guitar-notes/logs
  python analyze_logs.py --folder ~/guitar-notes/logs --logs 10
  python analyze_logs.py --folder ~/guitar-notes/logs --days 7
"""

import argparse
import re
from datetime import datetime, timedelta
from pathlib import Path

# --- Regex patterns targeting the Unified Practice Log Format ---

DATE_FILENAME_RE = re.compile(r"(\d{4}-\d{2}-\d{2})-guitar-practice\.md$")

# Session Start block
SESSION_TYPE_RE   = re.compile(r"^- Session type:\s*(.+)", re.M)

# Summary block
CURRENT_LESSON_RE = re.compile(r"^- Current lesson:\s*(.+)", re.M)
PRACTICE_GOAL_RE  = re.compile(r"^- Practice goal:\s*(.+)", re.M)

# Tags line (the single line of tags that follows "## Tags")
TAGS_LINE_RE      = re.compile(r"^## Tags\s*\n(.+)", re.M)
STATUS_TAG_RE     = re.compile(r"#status/(\S+)")
ISSUE_TAG_RE      = re.compile(r"#issue/(\S+)")

# End of Session Reflection
OVERALL_RATING_RE = re.compile(r"^- Overall rating \(1-10\):\s*(\d+)", re.M)
CONFIDENCE_RE     = re.compile(r"^- Confidence level \(1-10\):\s*(\d+)", re.M)
ADVANCE_RE        = re.compile(r"^- Ready to advance\?:\s*(.+)", re.M)
COACH_REC_RE      = re.compile(r"^- Coach recommendation:\s*(.+)", re.M)

# Reflection narrative fields
IMPROVED_RE       = re.compile(r"^- What improved today:\s*(.+)", re.M)
STILL_WEAK_RE     = re.compile(r"^- What still feels weak:\s*(.+)", re.M)
MISTAKE_RE        = re.compile(r"^- Most common mistake:\s*(.+)", re.M)
NEXT_PRIORITY_RE  = re.compile(r"^- Next session priority:\s*(.+)", re.M)

# Mastery Signals section (full block)
MASTERY_RE        = re.compile(r"## Mastery Signals\n(.*?)(?=\n## |\Z)", re.S)

# Issue Log — one block per ### Issue:
ISSUE_BLOCK_RE    = re.compile(r"### Issue: (.+?)\n(.*?)(?=\n### Issue:|\n## |\Z)", re.S)
TRAJECTORY_RE     = re.compile(r"^- Trajectory:\s*(.+)", re.M)
CONTEXT_RE        = re.compile(r"^- Context:\s*(.+)", re.M)
ERROR_FREQ_RE     = re.compile(r"^- Error frequency:\s*(.+)", re.M)

# Per-section blocks (## Section N - Name)
SECTION_BLOCK_RE  = re.compile(r"^## (Section \d+ - .+?)\n(.*?)(?=\n## |\Z)", re.M | re.S)
WHAT_PRACTICED_RE = re.compile(r"^- What I practiced:\s*(.+)", re.M)
SELF_RATING_RE    = re.compile(r"^- Self-rating \(1-10\):\s*(.+)", re.M)
TEMPO_RE          = re.compile(r"^- Tempo:\s*(.+)", re.M)
DIFFICULTY_RE     = re.compile(r"^- Difficulty notes:\s*(.+)", re.M)
TENSION_PAIN_RE   = re.compile(r"^- Tension or pain:\s*(.+)", re.M)


def find_logs(folder: Path, logs_n: int = None, days_n: int = None):
    """Return (date, path) pairs sorted oldest to newest, filtered by --logs or --days."""
    all_logs = []
    for path in folder.glob("*-guitar-practice.md"):
        m = DATE_FILENAME_RE.search(path.name)
        if not m:
            continue
        date = datetime.strptime(m.group(1), "%Y-%m-%d").date()
        all_logs.append((date, path))
    all_logs.sort()

    if days_n is not None:
        cutoff = datetime.today().date() - timedelta(days=days_n - 1)
        all_logs = [(d, p) for d, p in all_logs if d >= cutoff]
    elif logs_n is not None:
        all_logs = all_logs[-logs_n:]

    return all_logs


def _get(text: str, pattern: re.Pattern) -> str:
    m = pattern.search(text)
    return m.group(1).strip() if m else ""


def _get_all(text: str, pattern: re.Pattern) -> list:
    return [m.group(1).strip() for m in pattern.finditer(text)]


def parse_log(date, path: Path) -> dict:
    text = path.read_text(encoding="utf-8")

    tags_line = _get(text, TAGS_LINE_RE)
    issues    = _get_all(tags_line, ISSUE_TAG_RE) if tags_line else []
    status    = _get(tags_line, STATUS_TAG_RE) if tags_line else ""

    sections = []
    for m in SECTION_BLOCK_RE.finditer(text):
        block = m.group(2)
        what = _get(block, WHAT_PRACTICED_RE)
        if not what:
            continue
        sections.append({
            "name":         m.group(1).strip(),
            "what":         what,
            "self_rating":  _get(block, SELF_RATING_RE),
            "tempo":        _get(block, TEMPO_RE),
            "difficulty":   _get(block, DIFFICULTY_RE),
            "tension_pain": _get(block, TENSION_PAIN_RE),
        })

    issue_log = []
    for m in ISSUE_BLOCK_RE.finditer(text):
        block = m.group(2)
        issue_log.append({
            "name":        m.group(1).strip(),
            "trajectory":  _get(block, TRAJECTORY_RE),
            "context":     _get(block, CONTEXT_RE),
            "frequency":   _get(block, ERROR_FREQ_RE),
        })

    mastery_m = MASTERY_RE.search(text)

    return {
        "date":           date.isoformat(),
        "session_type":   _get(text, SESSION_TYPE_RE),
        "lesson":         _get(text, CURRENT_LESSON_RE),
        "rating":         _get(text, OVERALL_RATING_RE),
        "status":         status,
        "issues":         ", ".join(issues),
        "confidence":     _get(text, CONFIDENCE_RE),
        "advance_ready":  _get(text, ADVANCE_RE),
        "recommendation": _get(text, COACH_REC_RE),
        # narrative
        "practice_goal":  _get(text, PRACTICE_GOAL_RE),
        "improved":       _get(text, IMPROVED_RE),
        "still_weak":     _get(text, STILL_WEAK_RE),
        "mistake":        _get(text, MISTAKE_RE),
        "next_priority":  _get(text, NEXT_PRIORITY_RE),
        "mastery":        mastery_m.group(1).strip() if mastery_m else "",
        "sections":       sections,
        "issue_log":      issue_log,
    }


def print_table(records: list):
    headers = ["Date", "Type", "Rating", "Lesson", "Status", "Issues", "Conf", "Advance?", "Recommendation"]

    def row_cells(r):
        return [
            r["date"],
            r["session_type"] or "—",
            r["rating"]       or "—",
            r["lesson"]       or "—",
            r["status"]       or "—",
            r["issues"]       or "—",
            r["confidence"]   or "—",
            r["advance_ready"]or "—",
            r["recommendation"]or "—",
        ]

    rows = [row_cells(r) for r in records]
    widths = [max(len(headers[i]), max(len(row[i]) for row in rows)) for i in range(len(headers))]

    def fmt(cells):
        return "| " + " | ".join(c.ljust(widths[i]) for i, c in enumerate(cells)) + " |"

    print(fmt(headers))
    print("|" + "|".join("-" * (w + 2) for w in widths) + "|")
    for row in rows:
        print(fmt(row))


def print_narrative(records: list):
    print("\n---\n")
    print("## Session Notes\n")
    for r in records:
        print(f"### {r['date']}")

        for label, key in [
            ("Goal",            "practice_goal"),
            ("Improved",        "improved"),
            ("Still weak",      "still_weak"),
            ("Common mistake",  "mistake"),
            ("Next priority",   "next_priority"),
        ]:
            if r[key]:
                print(f"**{label}:** {r[key]}")

        if r["sections"]:
            print("\n**Sections:**")
            for s in r["sections"]:
                extras = []
                if s["tempo"]:        extras.append(f"tempo {s['tempo']}")
                if s["self_rating"]:  extras.append(f"rated {s['self_rating']}/10")
                if s["difficulty"]:   extras.append(f"difficulty: {s['difficulty']}")
                if s["tension_pain"]: extras.append(f"tension/pain: {s['tension_pain']}")
                line = f"- {s['name']}: {s['what']}"
                if extras:
                    line += f" ({'; '.join(extras)})"
                print(line)

        if r["mastery"]:
            print(f"\n**Mastery signals:**\n{r['mastery']}")

        if r["issue_log"]:
            print("\n**Issue log:**")
            for issue in r["issue_log"]:
                parts = [f"- {issue['name']}"]
                if issue["trajectory"]: parts.append(f"trajectory: {issue['trajectory']}")
                if issue["context"]:    parts.append(f"context: {issue['context']}")
                if issue["frequency"]:  parts.append(f"frequency: {issue['frequency']}")
                print(" | ".join(parts))

        print()


def main():
    parser = argparse.ArgumentParser(
        description="Extract structured data from guitar practice logs."
    )
    parser.add_argument("--folder", required=True,
                        help="Folder containing daily practice logs")
    parser.add_argument("--logs", type=int, default=14,
                        help="Number of most recent logs to include (default: 14)")
    parser.add_argument("--days", type=int,
                        help="Lookback window in days — overrides --logs if both given")
    args = parser.parse_args()

    folder = Path(args.folder)
    if not folder.exists():
        raise SystemExit(f"Folder not found: {folder}")

    records_raw = find_logs(folder, logs_n=args.logs, days_n=args.days)
    if not records_raw:
        raise SystemExit("No practice logs found in the requested range.")

    records = [parse_log(date, path) for date, path in records_raw]

    print(f"## Practice Log Summary — {records[0]['date']} to {records[-1]['date']}")
    print(f"Logs: {len(records)}\n")
    print_table(records)
    print_narrative(records)


if __name__ == "__main__":
    main()