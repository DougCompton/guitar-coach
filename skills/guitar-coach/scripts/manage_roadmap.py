#!/usr/bin/env python3
import argparse
from pathlib import Path
from datetime import date

DEFAULTS = {
    "beginner": [
        "Open-string reset and posture",
        "Basic open chords: Em, Am, C, G, D",
        "Steady quarter-note and eighth-note strumming",
        "Clean chord changes in 2-chord loops",
        "Major scale pattern plus intervals on one string",
        "First complete song with open chords",
        "Chord construction from familiar open shapes",
        "Review and tempo growth",
    ],
    "intermediate": [
        "Barre-chord refresh and fret-hand efficiency",
        "Strumming control with accents and syncopation",
        "Alternate picking and position shifts",
        "Minor pentatonic phrasing and bends",
        "Triads on top strings",
        "Groove playing and rhythm precision with a metronome",
        "Song study with full-section transitions",
        "Review and consolidation",
    ],
    "fingerstyle": [
        "Thumb-index-middle-ring assignment reset",
        "Travis-picking basics",
        "Alternating bass with steady treble notes",
        "Chord melody fragments on top strings",
        "Right-hand independence and pattern changes",
        "Fingerstyle arrangement of a simple tune",
        "Triads inside fingerstyle chord shapes",
        "Review and repertoire polish",
    ],
    "celtic": [
        "DADGAD or standard-tuning drone concepts",
        "Modal scale shapes and ornament basics",
        "Open-string drones with melody fragments",
        "Reel and jig rhythm feel",
        "Hammer-ons, pull-offs, and cuts in context",
        "Celtic-style accompaniment patterns",
        "Learn a simple traditional tune in ASCII tab",
        "Review and phrasing polish",
    ],
    "rock": [
        "Power chords on E and A strings with correct muting",
        "Palm muting and pick-attack control",
        "Root-5 power chord movement and basic rock rhythm patterns",
        "Down-stroke riffing and string crossing at steady tempo",
        "Minor pentatonic scale box 1 and first simple lick",
        "Bending basics: half-step and whole-step bends in tune",
        "Riff-based song study using power chords and pentatonic ideas",
        "Review and tone: dynamics, muting clarity, and rhythmic tightness",
    ],
    "blues": [
        "12-bar blues structure with open E, A, and B7 chords",
        "Shuffle feel and swing eighth-note rhythm",
        "Minor pentatonic box 1 and the blues note (b5)",
        "Call-and-response phrasing over a 12-bar form",
        "Expressive bending and vibrato in context",
        "Simple blues lick library: turnarounds, rakes, and slides",
        "Playing a complete 12-bar blues from start to finish musically",
        "Review and improvisation: making choices, leaving space, and phrasing",
    ],
    "country": [
        "Open chord vocabulary with capo: common keys on capo 2 and capo 4",
        "Alternating bass pick: thumb-driven bass note with pick or fingers on treble strings",
        "Basic hybrid picking: pick and middle finger together on adjacent strings",
        "Chicken pickin' introduction: muted snap on treble strings with ring or middle finger",
        "Pedal-steel-style bends: whole-step bends in tune on the B and G strings",
        "Country rhythm feel: boom-chick pattern and shuffle subdivision",
        "Simple country lead over a I-IV-V progression",
        "Review and taste: clean tone, dynamics, and phrasing space",
    ],
}


def slug(name: str) -> str:
    return name.strip().lower().replace(" ", "-")


def roadmap_path(folder: Path, name: str) -> Path:
    return folder / f"roadmap-{slug(name)}.md"


def write_active(folder: Path, name: str):
    p = folder / "active-roadmap.md"
    p.write_text(
        "# Active Roadmap\n\n"
        f"- Current roadmap: {slug(name)}\n"
        f"- Roadmap file: roadmap-{slug(name)}.md\n"
        f"- Last updated: {date.today().isoformat()}\n",
        encoding="utf-8",
    )


def create_default(folder: Path, name: str):
    s = slug(name)
    lessons = DEFAULTS[s]
    p = roadmap_path(folder, s)
    lines = [f"# Roadmap: {name.title()}", "", "## Overview", "- Focus: guitar development", f"- Level: {s}", "- Goal: build steady musical progress", "- Current stage: lesson 1", f"- Next review date: {date.today().isoformat()}", ""]
    for i, lesson in enumerate(lessons, start=1):
        status = "current" if i == 1 else "queued"
        lines.extend([
            f"## Lesson {i}",
            f"- Title: {lesson}",
            f"- Status: {status}",
            "- Goal:",
            "- Exit criteria:",
            "  -",
            "  -",
            "- Practice menu:",
            "  -",
            "  -",
            "- Application:",
            "  -",
            "- Notes:",
            "",
        ])
    p.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    return p


def ensure(folder: Path):
    folder.mkdir(parents=True, exist_ok=True)
    found = list(folder.glob("roadmap-*.md"))
    created = []
    if not found:
        for name in DEFAULTS:
            created.append(create_default(folder, name))
        write_active(folder, "beginner")
    elif not (folder / "active-roadmap.md").exists():
        write_active(folder, found[0].stem.replace("roadmap-", ""))
    return created


def switch(folder: Path, name: str):
    p = roadmap_path(folder, name)
    if not p.exists():
        if slug(name) not in DEFAULTS:
            raise SystemExit(f"Unknown roadmap '{name}'. Available built-in roadmaps: {', '.join(DEFAULTS)}")
        create_default(folder, name)
    write_active(folder, name)
    return p


def list_maps(folder: Path):
    return sorted(x.name for x in folder.glob("roadmap-*.md"))


def main():
    parser = argparse.ArgumentParser(description="Manage external guitar lesson roadmap markdown files.")
    parser.add_argument("--folder", required=True, help="Folder containing roadmap and practice markdown files")
    parser.add_argument("--ensure-defaults", action="store_true", help="Create default roadmaps if none exist")
    parser.add_argument("--switch", help="Switch active roadmap by name, e.g. beginner or fingerstyle")
    parser.add_argument("--list", action="store_true", help="List roadmap files")
    args = parser.parse_args()

    folder = Path(args.folder)
    if args.ensure_defaults:
        created = ensure(folder)
        if created:
            print("Created default roadmap files:")
            for p in created:
                print(f"- {p.name}")
        else:
            print("Roadmap files already exist; nothing created.")

    if args.switch:
        p = switch(folder, args.switch)
        print(f"Active roadmap set to: {p.name}")

    if args.list:
        items = list_maps(folder)
        if not items:
            print("No roadmap files found.")
        else:
            print("Available roadmap files:")
            for item in items:
                print(f"- {item}")

    if not (args.ensure_defaults or args.switch or args.list):
        parser.print_help()


if __name__ == "__main__":
    main()
