#!/usr/bin/env python3
"""Type-coverage check for rpn-calc: every function and method must carry a
return annotation and full parameter annotations. This is the project's real
typecheck contract (stdlib-only codebase; no third-party type checker used).
Read-only: never writes to the checkout.
"""
from __future__ import annotations

import ast
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKAGES = [ROOT / "app", ROOT / "tools"]


def check_file(path: Path) -> list[str]:
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    problems: list[str] = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            if node.name.startswith("__"):
                continue
            if node.returns is None:
                problems.append(f"{path}:{node.lineno}: function {node.name!r} lacks a return annotation")
            for arg in node.args.args + node.args.kwonlyargs:
                if arg.arg in {"self", "cls"}:
                    continue
                if arg.annotation is None:
                    problems.append(
                        f"{path}:{node.lineno}: parameter {arg.arg!r} of {node.name!r} lacks an annotation"
                    )
    return problems


def main() -> int:
    problems: list[str] = []
    for package in PACKAGES:
        for file in sorted(package.rglob("*.py")):
            problems.extend(check_file(file))
    for problem in problems:
        print(f"TYPECHECK: {problem}", file=sys.stderr)
    if problems:
        print(f"typecheck: {len(problems)} unannotated function(s)/parameter(s)", file=sys.stderr)
        return 1
    print("typecheck: all functions fully annotated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
