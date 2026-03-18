#!/usr/bin/env python3
"""
practice_end.py — validate a completed guitar practice log.

Checks that all required fields and tags are present after Claude
writes the end-of-session sections. Run this after the session ends.

Usage:
  python practice_end.py --folder ~/guitar-notes/logs
  python practice_end.py --folder ~/guitar-notes/logs --date 2026-03-17
"""

import argparse
import re
from datetime import date
from pathlib import Path

# Required fields (field name → human label)
REQUIRED_FIELDS = {
    r"^- Current lesson:\s*\S":          "Current lesson (Summary)",
    r"^- Practice goal:\s*\S":           "Practice goal (Summary)",
    r"^- Overall rating \(1-10\):\s*\d": "Overall rating (Reflection)",
    r"^- Repeat, simplify, or advance:\s*\S": "Repeat, simplify, or advance (Reflection)",
    r"^- Coach recommendation:\s*\S":    "Coach recommendation (Reflection)",
}

# Required tag patterns
TAG_RULES = [
    (re.compile(r"#roadmap/\S+"),  "one #roadmap/<name> tag"),
    (re.compile(r"#lesson/\S+"),   "one #lesson/<slug> tag"),
    (re.compile(r"#status/\S+"),   "one #status/<value> tag"),
]

VALID_STATUS   = {"repeat", "advance", "simplify"}
RATING_RE      = re.compile(r"^- Overall rating \(1-10\):\s*(\d+)", re.M)
STATUS_RE      = re.compile(r"#status/(\S+)")
ISSUE_LOG_RE   = re.compile(r"^## Issue Log", re.M)
ISSUE_TAG_RE   = re.compile(r"#issue/\S+")
SESSION_START_RE = re.compile(r"^## Session Start", re.M)
DATE_FILENAME_RE = re.compile(r"(\d{4}-\d{2}-\d{2})-guitar-practice\.md$")


def find_log(folder: Path, target_date: str = None) -> Path:
    if target_date:
        path = folder / f"{target_date}-guitar-practice.md"
        if not path.exists():
            raise SystemExit(f"Log not found: {path}")
        return path

    candidates = sorted(
        (p for p in folder.glob("*-guitar-practice.md") if DATE_FILENAME_RE.search(p.name)),
        key=lambda p: DATE_FILENAME_RE.search(p.name).group(1),
    )
    if not candidates:
        raise SystemExit("No practice logs found in folder.")
    return candidates[-1]


def validate(path: Path) -> list:
    errors = []
    text = path.read_text(encoding="utf-8")

    # Session Start block must be present
    if not SESSION_START_RE.search(text):
        errors.append("Missing ## Session Start block")

    # Required fields
    for pattern, label in REQUIRED_FIELDS.items():
        if not re.search(pattern, text, re.M):
            errors.append(f"Missing or empty: {label}")

    # Rating must be 1–10
    rating_m = RATING_RE.search(text)
    if rating_m:
        val = int(rating_m.group(1))
        if not 1 <= val <= 10:
            errors.append(f"Overall rating out of range: {val} (must be 1–10)")

    # Required tags
    tags_line_m = re.search(r"^## Tags\s*\n(.+)", text, re.M)
    tags_line = tags_line_m.group(1) if tags_line_m else ""

    if not tags_line:
        errors.append("Missing ## Tags section or empty tags line")
    else:
        for pattern, label in TAG_RULES:
            if not pattern.search(tags_line):
                errors.append(f"Missing tag: {label}")

        status_m = STATUS_RE.search(tags_line)
        if status_m and status_m.group(1) not in VALID_STATUS:
            errors.append(
                f"Invalid #status value: '{status_m.group(1)}' "
                f"(must be one of: {', '.join(sorted(VALID_STATUS))})"
            )

    # If Issue Log section exists, at least one #issue/ tag must be present
    if ISSUE_LOG_RE.search(text) and not ISSUE_TAG_RE.search(tags_line):
        errors.append("Issue Log section present but no #issue/<slug> tag found in Tags")

    return errors


def main():
    parser = argparse.ArgumentParser(
        description="Validate a completed guitar practice log."
    )
    parser.add_argument("--folder", required=True,
                        help="Folder containing daily practice logs")
    parser.add_argument("--date",
                        help="Date of the log to validate (YYYY-MM-DD). Defaults to most recent.")
    args = parser.parse_args()

    folder = Path(args.folder)
    if not folder.exists():
        raise SystemExit(f"Folder not found: {folder}")

    log_path = find_log(folder, args.date)
    errors = validate(log_path)

    print(f"Validating: {log_path.name}")
    if not errors:
        print("OK — all required fields and tags are present.")
    else:
        print(f"ISSUES FOUND ({len(errors)}):\n")
        for e in errors:
            print(f"  - {e}")
        raise SystemExit(1)


if __name__ == "__main__":
    main()