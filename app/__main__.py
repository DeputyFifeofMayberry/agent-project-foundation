"""Entry point so the app runs as `python3 -m app`."""
import sys

from app.cli import main

if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
