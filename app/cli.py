"""Command-line interface for rpn-calc."""
from __future__ import annotations

import argparse
import sys

from app.core import RpnError, evaluate, format_stack


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="rpn-calc",
        description="Evaluate a reverse-polish notation expression.",
    )
    parser.add_argument("tokens", nargs="+", help="RPN tokens, e.g. 3 4 +")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        stack = evaluate(args.tokens)
    except RpnError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    print(format_stack(stack))
    return 0
