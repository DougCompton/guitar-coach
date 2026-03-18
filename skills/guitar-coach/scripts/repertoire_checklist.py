#!/usr/bin/env python3
import argparse
from pathlib import Path

TEMPLATE = """## Performance Checklist\n- Memorized: \n- Rhythm stable: \n- Clean transitions: \n- Expressive dynamics: \n- Full-speed ready: \n"""


def main():
    p = argparse.ArgumentParser(description='Print or append a repertoire performance checklist.')
    p.add_argument('--folder', help='Practice folder containing repertoire.md')
    p.add_argument('--song', help='Song name to print checklist for')
    p.add_argument('--append', action='store_true', help='Append checklist block to repertoire.md')
    args = p.parse_args()
    title = args.song or 'Song'
    block = f'### {title}\n' + TEMPLATE
    print('# Repertoire Performance Checklist')
    print(block.rstrip())
    if args.append:
        if not args.folder:
            raise SystemExit('--folder is required with --append')
        path = Path(args.folder) / 'repertoire.md'
        existing = path.read_text(encoding='utf-8') if path.exists() else '# Repertoire Lane\n\n'
        path.write_text(existing.rstrip() + '\n\n' + block, encoding='utf-8')
        print(f'\nAppended checklist to {path}')


if __name__ == '__main__':
    main()
