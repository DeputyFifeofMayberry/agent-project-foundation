"""End-to-end test: launches the real CLI in a subprocess (read-only)."""
from __future__ import annotations

import subprocess
import sys
import unittest

REPO_ROOT = __file__.rsplit("/tests/", 1)[0]


def run_cli(tokens: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "-m", "app", *tokens],
        cwd=REPO_ROOT, capture_output=True, text=True, timeout=60,
    )


class EndToEndTests(unittest.TestCase):
    def test_happy_path(self) -> None:
        proc = run_cli(["3", "4", "+"])
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertEqual(proc.stdout.strip(), "7")

    def test_error_path_exit_code(self) -> None:
        proc = run_cli(["2", "0", "/"])
        self.assertEqual(proc.returncode, 2)
        self.assertIn("division by zero", proc.stderr)
        self.assertEqual(proc.stdout, "")

    def test_compound_expression(self) -> None:
        proc = run_cli(["5", "1", "2", "+", "4", "*", "+", "3", "-"])
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertEqual(proc.stdout.strip(), "14")


if __name__ == "__main__":
    unittest.main()
