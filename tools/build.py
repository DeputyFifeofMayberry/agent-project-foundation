#!/usr/bin/env python3
"""Build check for rpn-calc: produces a runnable zipapp artifact OUTSIDE the
checkout (read-only-safe per docs/STACKS.md), smoke-runs it, then cleans up.

The archive is staged from a copy of the `app` package so the package layout
(and its absolute imports) is preserved inside the zipapp.
"""
from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
import zipapp
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    source = ROOT / "app"
    if not (source / "__main__.py").is_file():
        print("BUILD: app/__main__.py missing; nothing to build", file=sys.stderr)
        return 1
    with tempfile.TemporaryDirectory(prefix="rpn-calc-build-") as tmp:
        staging = Path(tmp) / "staging"
        staging.mkdir()
        shutil.copytree(source, staging / "app")
        artifact = Path(tmp) / "rpn-calc.pyz"
        zipapp.create_archive(staging, target=str(artifact), interpreter="/usr/bin/env python3", main="app.__main__:main")
        if not artifact.is_file() or artifact.stat().st_size == 0:
            print("BUILD: artifact missing or empty", file=sys.stderr)
            return 1
        proc = subprocess.run(
            [sys.executable, str(artifact), "3", "4", "+"],
            capture_output=True, text=True, timeout=60, cwd=tmp,
        )
        if proc.returncode != 0 or proc.stdout.strip() != "7":
            print(f"BUILD: artifact smoke run failed: rc={proc.returncode} out={proc.stdout!r} err={proc.stderr!r}", file=sys.stderr)
            return 1
        print(f"BUILD: ok ({artifact.stat().st_size} bytes, smoke run: {proc.stdout.strip()}; artifact in temp dir, not the checkout)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
