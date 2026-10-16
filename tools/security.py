#!/usr/bin/env python3
"""Security scan for rpn-calc: secret patterns and dangerous calls in app code.
Read-only: never writes to the checkout.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGETS = [ROOT / "app"]
SECRET_PATTERNS = {
    "hardcoded assignment to a secret-like name": re.compile(
        r"(?i)\b(password|passwd|secret|api[_-]?key|access[_-]?token|auth[_-]?token|private[_-]?key)\s*=\s*[\"'][^\"']+[\"']"
    ),
    "hardcoded bearer token literal": re.compile(r"(?i)[\"']bearer\s+[a-z0-9._-]{10,}[\"']"),
    "hardcoded aws-style key literal": re.compile(r"AKIA[0-9A-Z]{16}"),
}
DANGEROUS_CALLS = {"eval", "exec", "compile", "__import__", "pickle.load", "pickle.loads", "os.system"}
DANGEROUS_IMPORTS = {"pickle", "ctypes", "subprocess"}


def main() -> int:
    findings: list[str] = []
    for package in TARGETS:
        for file in sorted(package.rglob("*.py")):
            text = file.read_text(encoding="utf-8")
            for description, pattern in SECRET_PATTERNS.items():
                for match in pattern.finditer(text):
                    line = text.count("\n", 0, match.start()) + 1
                    findings.append(f"{file}:{line}: {description}")
            for call in DANGEROUS_CALLS:
                if re.search(r"(?<![\w.])" + re.escape(call) + r"\s*\(", text):
                    line_match = re.search(r"(?<![\w.])" + re.escape(call) + r"\s*\(", text)
                    line = text.count("\n", 0, line_match.start()) + 1 if line_match else 0
                    findings.append(f"{file}:{line}: forbidden call {call}()")
            for module in DANGEROUS_IMPORTS:
                if re.search(r"(?m)^\s*(import|from)\s+" + re.escape(module) + r"\b", text):
                    findings.append(f"{file}: forbidden import {module!r} in application code")
    for finding in findings:
        print(f"SECURITY: {finding}", file=sys.stderr)
    if findings:
        print(f"security: {len(findings)} finding(s)", file=sys.stderr)
        return 1
    print("security: no secret patterns or dangerous calls in app code")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
