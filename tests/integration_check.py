"""Integration: exercise greet() together with CLI arg parsing."""
import subprocess
import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root))

from greeter import greet, main
assert greet("Grace") == "Hello, Grace!"
rc = main(["--name", "Grace"])
assert rc == 0, rc
proc = subprocess.run([sys.executable, str(root / "greeter.py"), "--name", "E2E-User"],
                      capture_output=True, text=True, cwd=root)
assert proc.returncode == 0, proc.stderr
assert proc.stdout.strip() == "Hello, E2E-User!", proc.stdout
print("integration: OK")
