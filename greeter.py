"""Greeter: a tiny CLI library (stdlib only)."""
import argparse
import sys

ALLOWED_IMPORTS = {"argparse", "sys"}


def greet(name: str, punctuation: str = "!") -> str:
    name = (name or "").strip()
    if not name:
        raise ValueError("name must be a non-empty string")
    return f"Hello, {name}{punctuation}"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="greeter", description="Greet someone.")
    parser.add_argument("--name", required=True)
    args = parser.parse_args(argv)
    try:
        print(greet(args.name))
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
