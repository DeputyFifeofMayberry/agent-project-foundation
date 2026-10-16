#!/usr/bin/env python3
"""E2E check for rpn-calc: drives the packaged CLI in real subprocesses.
Read-only: never writes to the checkout.
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run(tokens: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "-m", "app", *tokens],
        cwd=ROOT, capture_output=True, text=True, timeout=60,
    )


def main() -> int:
    failures: list[str] = []
    happy = run(["3", "4", "+"])
    if happy.returncode != 0 or happy.stdout.strip() != "7":
        failures.append(f"happy path: rc={happy.returncode} out={happy.stdout!r}")
    compound = run(["5", "1", "2", "+", "4", "*", "+", "3", "-"])
    if compound.returncode != 0 or compound.stdout.strip() != "14":
        failures.append(f"compound expression: rc={compound.returncode} out={compound.stdout!r}")
    error = run(["2", "0", "/"])
    if error.returncode != 2 or "division by zero" not in error.stderr:
        failures.append(f"error path: rc={error.returncode} err={error.stderr!r}")
    usage = run([])
    if usage.returncode != 2:
        failures.append(f"missing-args usage error: rc={usage.returncode}")
    for failure in failures:
        print(f"E2E: {failure}", file=sys.stderr)
    if failures:
        print(f"e2e: {len(failures)} failure(s)", file=sys.stderr)
        return 1
    print("e2e: CLI happy path, compound expression, and error paths behave")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
