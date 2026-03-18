#!/usr/bin/env python3
import argparse
import math
import os
import struct
import sys
import wave
from pathlib import Path
from statistics import mean


def record_with_sounddevice(seconds: int, out_path: Path, samplerate: int = 44100):
    try:
        import sounddevice as sd  # type: ignore
    except Exception as exc:
        raise RuntimeError(
            "Microphone recording needs the optional 'sounddevice' package and a local environment with microphone access. "
            "Install sounddevice and run this script on your own machine, or pass --input with a WAV file."
        ) from exc

    channels = 1
    print(f"Recording {seconds} seconds from microphone...", file=sys.stderr)
    audio = sd.rec(int(seconds * samplerate), samplerate=samplerate, channels=channels, dtype='int16')
    sd.wait()
    with wave.open(str(out_path), 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(2)
        wf.setframerate(samplerate)
        wf.writeframes(audio.tobytes())
    return out_path


def read_wav_mono(path: Path):
    with wave.open(str(path), 'rb') as wf:
        channels = wf.getnchannels()
        sampwidth = wf.getsampwidth()
        framerate = wf.getframerate()
        nframes = wf.getnframes()
        raw = wf.readframes(nframes)
    if sampwidth != 2:
        raise ValueError('Only 16-bit PCM WAV files are supported.')
    total_samples = len(raw) // 2
    samples = list(struct.unpack('<' + 'h' * total_samples, raw))
    if channels > 1:
        mono = []
        for i in range(0, len(samples), channels):
            mono.append(int(sum(samples[i:i + channels]) / channels))
        samples = mono
    return framerate, samples


def rms(chunk):
    if not chunk:
        return 0.0
    return math.sqrt(sum(s * s for s in chunk) / len(chunk))


def zero_cross_rate(chunk):
    if len(chunk) < 2:
        return 0.0
    count = 0
    prev = chunk[0]
    for cur in chunk[1:]:
        if (prev < 0 <= cur) or (prev > 0 >= cur):
            count += 1
        prev = cur
    return count / (len(chunk) - 1)


def frame_metrics(samples, sr, frame_ms=50):
    frame_len = max(1, int(sr * frame_ms / 1000))
    frames = [samples[i:i + frame_len] for i in range(0, len(samples), frame_len)]
    frames = [f for f in frames if len(f) >= frame_len // 2]
    energies = [rms(f) for f in frames]
    zcrs = [zero_cross_rate(f) for f in frames]
    return frames, energies, zcrs


def coefficient_of_variation(values):
    vals = [v for v in values if v > 0]
    if len(vals) < 2:
        return 0.0
    avg = mean(vals)
    if avg == 0:
        return 0.0
    variance = sum((v - avg) ** 2 for v in vals) / len(vals)
    return math.sqrt(variance) / avg


def top_peaks(values, threshold):
    peaks = []
    for i, v in enumerate(values):
        left = values[i - 1] if i > 0 else v
        right = values[i + 1] if i + 1 < len(values) else v
        if v >= threshold and v >= left and v >= right:
            peaks.append(i)
    return peaks


def intervals_seconds(peaks, frame_seconds):
    if len(peaks) < 2:
        return []
    return [(peaks[i] - peaks[i - 1]) * frame_seconds for i in range(1, len(peaks))]


def score_band(value, good_max, okay_max):
    if value <= good_max:
        return 1
    if value <= okay_max:
        return 2
    if value <= okay_max * 1.5:
        return 3
    return 4


def invert_score_band(value, good_min, okay_min):
    if value >= good_min:
        return 1
    if value >= okay_min:
        return 2
    if value >= okay_min * 0.75:
        return 3
    return 4


def label_for(question, score):
    banks = {
        'timing stability': {
            1: 'very steady', 2: 'mostly steady', 3: 'noticeably uneven', 4: 'unstable'
        },
        'note clarity': {
            1: 'clear', 2: 'mostly clear', 3: 'muddy or noisy', 4: 'very unclear'
        },
        'string noise': {
            1: 'minimal', 2: 'some', 3: 'frequent', 4: 'dominant'
        },
        'dynamic control': {
            1: 'well controlled', 2: 'usable', 3: 'inconsistent', 4: 'wildly uneven'
        },
    }
    return banks[question][score]


def analyze(path: Path):
    sr, samples = read_wav_mono(path)
    if len(samples) < sr:
        raise ValueError('Recording is too short. Capture at least 1 second.')
    duration = len(samples) / sr
    _, energies, zcrs = frame_metrics(samples, sr)
    frame_seconds = 0.05

    max_energy = max(energies) if energies else 0.0
    active_threshold = max_energy * 0.35
    peaks = top_peaks(energies, active_threshold)
    intervals = intervals_seconds(peaks, frame_seconds)
    interval_cv = coefficient_of_variation(intervals) if intervals else 1.0

    non_silent = [e for e in energies if e > max_energy * 0.12]
    dynamic_cv = coefficient_of_variation(non_silent) if non_silent else 1.0

    active_zcr = [z for z, e in zip(zcrs, energies) if e > active_threshold]
    noise_metric = mean(active_zcr) if active_zcr else 0.0

    crest_ratios = []
    frame_len = max(1, int(sr * frame_seconds))
    for i in range(0, len(samples), frame_len):
        chunk = samples[i:i + frame_len]
        if not chunk:
            continue
        local_rms = rms(chunk)
        peak = max(abs(s) for s in chunk)
        if local_rms > 0:
            crest_ratios.append(peak / local_rms)
    clarity_metric = mean(crest_ratios) if crest_ratios else 0.0

    timing_score = score_band(interval_cv, 0.18, 0.32)
    clarity_score = invert_score_band(clarity_metric, 3.8, 2.8)
    noise_score = score_band(noise_metric, 0.08, 0.14)
    dynamic_score = score_band(dynamic_cv, 0.22, 0.42)

    return {
        'duration_seconds': round(duration, 2),
        'timing stability': timing_score,
        'note clarity': clarity_score,
        'string noise': noise_score,
        'dynamic control': dynamic_score,
        'timing_metric_cv': round(interval_cv, 3),
        'clarity_metric_crest': round(clarity_metric, 3),
        'noise_metric_zcr': round(noise_metric, 3),
        'dynamic_metric_cv': round(dynamic_cv, 3),
        'estimated_attacks': len(peaks),
    }


def print_report(result, source_name):
    print(f'## Audio Analysis')
    print(f'- Source: {source_name}')
    print(f'- Duration: {result["duration_seconds"]} seconds')
    print(f'- Estimated attacks: {result["estimated_attacks"]}')
    print('')
    print('## Scores (1=best, 4=worst)')
    for key in ['timing stability', 'note clarity', 'string noise', 'dynamic control']:
        score = result[key]
        print(f'- {key.title()}: {score}/4 ({label_for(key, score)})')
    print('')
    print('## Raw Metrics')
    print(f'- Timing interval variability (CV): {result["timing_metric_cv"]}')
    print(f'- Clarity crest factor: {result["clarity_metric_crest"]}')
    print(f'- Noise zero-crossing rate: {result["noise_metric_zcr"]}')
    print(f'- Dynamic variability (CV): {result["dynamic_metric_cv"]}')


def main():
    parser = argparse.ArgumentParser(description='Record from microphone or analyze a WAV file to generate numeric reflection prompts.')
    parser.add_argument('--input', help='Path to an existing 16-bit PCM WAV file')
    parser.add_argument('--record-seconds', type=int, help='Record from microphone for this many seconds and analyze it')
    parser.add_argument('--output', default='mic-capture.wav', help='Where to save a microphone recording when --record-seconds is used')
    args = parser.parse_args()

    if not args.input and not args.record_seconds:
        raise SystemExit('Provide --input <wav> or --record-seconds <seconds>.')

    if args.record_seconds:
        path = Path(args.output)
        record_with_sounddevice(args.record_seconds, path)
        result = analyze(path)
        print_report(result, path.name)
        return

    path = Path(args.input)
    if not path.exists():
        raise SystemExit(f'Missing input file: {path}')
    result = analyze(path)
    print_report(result, path.name)


if __name__ == '__main__':
    main()
