"""Unit tests for the pure evaluation engine (app.core)."""
from __future__ import annotations

import unittest

from app.core import RpnError, evaluate, format_stack


class EvaluateTests(unittest.TestCase):
    def test_addition(self) -> None:
        self.assertEqual(evaluate(["3", "4", "+"]), [7.0])

    def test_subtraction_order(self) -> None:
        self.assertEqual(evaluate(["10", "4", "-"]), [6.0])

    def test_multiplication_and_division(self) -> None:
        self.assertEqual(evaluate(["3", "4", "*", "2", "/"]), [6.0])

    def test_stack_accumulates(self) -> None:
        self.assertEqual(evaluate(["1", "2", "3"]), [1.0, 2.0, 3.0])

    def test_division_by_zero_raises(self) -> None:
        with self.assertRaises(RpnError):
            evaluate(["1", "0", "/"])

    def test_insufficient_operands_raise(self) -> None:
        with self.assertRaises(RpnError):
            evaluate(["1", "+"])

    def test_invalid_token_raises(self) -> None:
        with self.assertRaises(RpnError):
            evaluate(["1", "2", "x"])


class FormatTests(unittest.TestCase):
    def test_integers_print_without_decimal_noise(self) -> None:
        self.assertEqual(format_stack([7.0]), "7")

    def test_floats_keep_precision(self) -> None:
        self.assertEqual(format_stack([0.5]), "0.5")

    def test_empty_stack(self) -> None:
        self.assertEqual(format_stack([]), "<empty stack>")


if __name__ == "__main__":
    unittest.main()
