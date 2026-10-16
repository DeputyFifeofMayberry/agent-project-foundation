#!/usr/bin/env python3
"""Lint check for rpn-calc: AST rules that catch real defects in this codebase.

Rules: no eval/exec calls, no bare except, no unused imports, no wildcard
imports. Read-only: never writes to the checkout.
"""
from __future__ import annotations

import ast
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGETS = [ROOT / "app", ROOT / "tests", *(ROOT / "tools").glob("*.py")]


def check_file(path: Path) -> list[str]:
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    problems: list[str] = []

    imported: dict[str, int] = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id in {"eval", "exec"}:
            problems.append(f"{path}: forbidden {node.func.id}() call at line {node.lineno}")
        if isinstance(node, ast.ExceptHandler) and node.type is None:
            problems.append(f"{path}: bare except at line {node.lineno}")
        if isinstance(node, ast.Import):
            for alias in node.names:
                bound = alias.asname or alias.name.split(".")[0]
                imported[bound] = node.lineno
        elif isinstance(node, ast.ImportFrom):
            for alias in node.names:
                if alias.name == "*":
                    problems.append(f"{path}: wildcard import at line {node.lineno}")
                else:
                    bound = alias.asname or alias.name
                    imported[bound] = node.lineno

    used: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Name):
            used.add(node.id)
        elif isinstance(node, ast.Attribute):
            target = node
            while isinstance(target, ast.Attribute):
                target = target.value
            if isinstance(target, ast.Name):
                used.add(target.id)

    for name, lineno in sorted(imported.items(), key=lambda kv: kv[1]):
        if name not in used and name != "annotations":
            problems.append(f"{path}: unused import {name!r} at line {lineno}")
    return problems


def main() -> int:
    problems: list[str] = []
    for target in TARGETS:
        files = sorted(target.rglob("*.py")) if target.is_dir() else [target]
        for file in files:
            problems.extend(check_file(file))
    for problem in problems:
        print(f"LINT: {problem}", file=sys.stderr)
    if problems:
        print(f"lint: {len(problems)} problem(s)", file=sys.stderr)
        return 1
    print(f"lint: clean ({sum(1 for t in TARGETS if t.is_file() or t.is_dir())} targets)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
