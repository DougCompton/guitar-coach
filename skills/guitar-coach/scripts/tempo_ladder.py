#!/usr/bin/env python3
import argparse


def main():
    parser = argparse.ArgumentParser(description="Generate a conservative tempo ladder for guitar practice.")
    parser.add_argument("--start-bpm", type=int, required=True)
    parser.add_argument("--target-bpm", type=int, required=True)
    parser.add_argument("--step", type=int, default=4)
    parser.add_argument("--reps", type=int, default=3, help="Clean reps required before moving up")
    args = parser.parse_args()

    if args.start_bpm <= 0 or args.target_bpm <= 0 or args.step <= 0 or args.reps <= 0:
        raise SystemExit("All numeric inputs must be positive.")
    if args.start_bpm > args.target_bpm:
        raise SystemExit("start-bpm must be less than or equal to target-bpm.")

    print("Tempo ladder")
    print(f"Start BPM: {args.start_bpm}")
    print(f"Target BPM: {args.target_bpm}")
    print(f"Step size: {args.step}")
    print(f"Advance rule: only move up after {args.reps} clean reps")
    print("")
    bpm = args.start_bpm
    rung = 1
    while bpm <= args.target_bpm:
        print(f"{rung}. {bpm} BPM - stay here until {args.reps} clean reps")
        bpm += args.step
        rung += 1
    last = args.target_bpm
    if (bpm - args.step) != last:
        print(f"{rung}. {last} BPM - final target")
    print("")


if __name__ == "__main__":
    main()
