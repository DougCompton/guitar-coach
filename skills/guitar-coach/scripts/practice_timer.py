#!/usr/bin/env python3
import argparse
import time
from math import floor


def fmt_minutes(m):
    if abs(m - int(m)) < 1e-9:
        return f"{int(m)} minute" + ("s" if int(m) != 1 else "")
    return f"{m:g} minutes"


def fmt_time(seconds: int) -> str:
    m, s = divmod(seconds, 60)
    return f"{m}:{s:02d}"


def build_checkpoints(minutes: float):
    checkpoints = []
    if minutes <= 2:
        return checkpoints
    if minutes <= 5:
        checkpoints.append((max(1, floor(minutes / 2)), "stay relaxed and keep it clean"))
        return checkpoints
    halfway = round(minutes / 2)
    checkpoints.append((halfway, "reset posture, relax your hands, and keep the tempo steady"))
    if minutes >= 8:
        checkpoints.append((max(1, int(minutes - 1)), "finish with your cleanest reps, not your fastest ones"))
    return checkpoints


def run_countdown(section, minutes, task, success):
    total = int(round(minutes * 60))
    checkpoints = {m * 60: note for m, note in build_checkpoints(minutes)}

    print(f"\n{'='*50}")
    print(f"  {section}")
    print(f"  Task: {task}")
    print(f"  Goal: {success}")
    print(f"{'='*50}\n")

    start = time.monotonic()
    last_elapsed = -1
    try:
        while True:
            elapsed = int(time.monotonic() - start)
            remaining = max(0, total - elapsed)
            filled = int((elapsed / total) * 30)
            bar = "#" * filled + "-" * (30 - filled)
            print(f"\r  [{bar}]  {fmt_time(remaining)}", end="", flush=True)

            if elapsed != last_elapsed:
                last_elapsed = elapsed
                if elapsed in checkpoints:
                    print(f"\n\n  >> CHECKPOINT: {checkpoints[elapsed]}\n")

            if remaining == 0:
                break
            time.sleep(0.25)
    except KeyboardInterrupt:
        print("\n\n  Timer stopped early.")
        return

    print(f"\n\n  TIME! Stop and reflect on {section.lower()}.")
    print(f"{'='*50}\n")


def main():
    parser = argparse.ArgumentParser(description="Practice timer for a guitar section.")
    parser.add_argument("--section", required=True, help="Section name")
    parser.add_argument("--minutes", required=True, type=float, help="Duration in minutes")
    parser.add_argument("--task", required=True, help="What to practice")
    parser.add_argument("--success", required=True, help="Simple success target")
    args = parser.parse_args()
    run_countdown(args.section, args.minutes, args.task, args.success)


if __name__ == "__main__":
    main()
