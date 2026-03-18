#!/usr/bin/env python3
import argparse
from pathlib import Path

DEFAULT = """# Repertoire Lane

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


def ensure(folder: Path) -> Path:
    folder.mkdir(parents=True, exist_ok=True)
    p = folder / 'repertoire.md'
    if not p.exists():
        p.write_text(DEFAULT, encoding='utf-8')
    return p


def main():
    parser = argparse.ArgumentParser(description='Create or inspect the external repertoire lane markdown file.')
    parser.add_argument('--folder', required=True, help='Folder containing practice files')
    parser.add_argument('--ensure-default', action='store_true', help='Create repertoire.md if missing')
    parser.add_argument('--show', action='store_true', help='Print the repertoire file path and contents')
    args = parser.parse_args()

    folder = Path(args.folder)
    path = ensure(folder) if args.ensure_default else folder / 'repertoire.md'
    if args.ensure_default:
        print(f'Repertoire file ready: {path.name}')
    if args.show:
        if not path.exists():
            raise SystemExit('repertoire.md does not exist.')
        print(f'# {path.name}')
        print(path.read_text(encoding='utf-8').rstrip())
    if not (args.ensure_default or args.show):
        parser.print_help()


if __name__ == '__main__':
    main()
