"""Integration tests: CLI layer plus evaluation engine working together."""
from __future__ import annotations

import io
import unittest
from contextlib import redirect_stderr, redirect_stdout
from unittest import mock

from app import cli


class CliIntegrationTests(unittest.TestCase):
    def run_main(self, argv: list[str]) -> tuple[int, str, str]:
        stdout, stderr = io.StringIO(), io.StringIO()
        with redirect_stdout(stdout), redirect_stderr(stderr):
            code = cli.main(argv)
        return code, stdout.getvalue(), stderr.getvalue()

    def test_successful_expression(self) -> None:
        code, out, err = self.run_main(["3", "4", "+"])
        self.assertEqual((code, err), (0, ""))
        self.assertEqual(out.strip(), "7")

    def test_error_expression_exits_two(self) -> None:
        code, out, err = self.run_main(["1", "0", "/"])
        self.assertEqual(code, 2)
        self.assertIn("division by zero", err)
        self.assertEqual(out, "")

    def test_parse_args_requires_tokens(self) -> None:
        with self.assertRaises(SystemExit):
            cli.parse_args([])

    def test_cli_uses_real_engine(self) -> None:
        with mock.patch("app.cli.evaluate", wraps=__import__("app.core", fromlist=["evaluate"]).evaluate) as spy:
            code, out, _ = self.run_main(["6", "7", "*"])
        self.assertEqual(code, 0)
        spy.assert_called_once_with(["6", "7", "*"])
        self.assertEqual(out.strip(), "42")


if __name__ == "__main__":
    unittest.main()
