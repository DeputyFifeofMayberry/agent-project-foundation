"""End-to-end: run the real CLI exactly as a user would."""
import subprocess
import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
cases = [("Ada", "Hello, Ada!"), ("Linus", "Hello, Linus!")]
for name, expected in cases:
    proc = subprocess.run([sys.executable, "greeter.py", "--name", name],
                          capture_output=True, text=True, cwd=root)
    assert proc.returncode == 0, (name, proc.stderr)
    assert proc.stdout.strip() == expected, (proc.stdout, expected)
bad = subprocess.run([sys.executable, "greeter.py"], capture_output=True, text=True, cwd=root)
assert bad.returncode != 0, "missing --name must fail"
print("e2e: OK (2 happy paths + 1 negative)")
