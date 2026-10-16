"""Security: scan first-party sources for hardcoded credential patterns."""
import re
import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
patterns = [
    re.compile(r"(?i)(api[_-]?key|secret|password|passwd|token|credential)\s*[:=]\s*['\"][^'\"]{6,}"),
    re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
]
hits = []
for path in [root / "greeter.py", *sorted((root / "tests").glob("*.py")),
             *sorted((root / "scripts").glob("*.py"))]:
    for i, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        for pat in patterns:
            if pat.search(line):
                hits.append(f"{path.relative_to(root)}:{i}")
if hits:
    print("security: FAILED - potential credentials in source:")
    for hit in hits:
        print(" ", hit)
    sys.exit(1)
print("security: OK (no credential patterns in first-party sources)")
