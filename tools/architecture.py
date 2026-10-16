#!/usr/bin/env python3
"""Architecture rules for rpn-calc (dependency direction, layering).

Rules:
  1. app.core (engine) must not import app.cli or app.__main__ (pure core).
  2. app.cli must not import app.__main__.
  3. Application code must never import the tests package.
  4. Tools must not import the application package (checks stay independent).
Read-only: never writes to the checkout.
"""
from __future__ import annotations

import ast
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FORBIDDEN = {
    "app/core.py": {"app.cli", "app.__main__"},
    "app/cli.py": {"app.__main__"},
}


def module_imports(path: Path) -> set[str]:
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    found: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            found.update(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            found.add(node.module)
    return found


def main() -> int:
    violations: list[str] = []
    app_root = ROOT / "app"
    for file in sorted(app_root.rglob("*.py")):
        rel = file.relative_to(ROOT).as_posix()
        imports = module_imports(file)
        if any(imp.startswith("tests") for imp in imports):
            violations.append(f"{rel}: application code imports the tests package")
        for forbidden in FORBIDDEN.get(rel, set()):
            if forbidden in imports:
                violations.append(f"{rel}: forbidden dependency on {forbidden}")
    for tool in sorted((ROOT / "tools").glob("*.py")):
        if any(imp == "app" or imp.startswith("app.") for imp in module_imports(tool)):
            violations.append(f"{tool.relative_to(ROOT).as_posix()}: tool imports application package")
    for violation in violations:
        print(f"ARCHITECTURE: {violation}", file=sys.stderr)
    if violations:
        print(f"architecture: {len(violations)} violation(s)", file=sys.stderr)
        return 1
    print("architecture: dependency rules hold")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
