"""Pure evaluation engine for rpn-calc. No I/O, no CLI imports."""
from __future__ import annotations


class RpnError(ValueError):
    """Raised when an RPN expression cannot be evaluated."""


def evaluate(tokens: list[str]) -> list[float]:
    """Evaluate a reverse-polish token sequence and return the final stack."""
    stack: list[float] = []
    for token in tokens:
        if token in {"+", "-", "*", "/"}:
            if len(stack) < 2:
                raise RpnError(f"insufficient operands for {token!r}")
            right = stack.pop()
            left = stack.pop()
            if token == "+":
                stack.append(left + right)
            elif token == "-":
                stack.append(left - right)
            elif token == "*":
                stack.append(left * right)
            else:
                if right == 0:
                    raise RpnError("division by zero")
                stack.append(left / right)
        else:
            try:
                stack.append(float(token))
            except ValueError as exc:
                raise RpnError(f"invalid token {token!r}") from exc
    return stack


def format_stack(stack: list[float]) -> str:
    """Render the evaluated stack as the CLI output line."""
    if not stack:
        return "<empty stack>"
    return " ".join(_format_number(value) for value in stack)


def _format_number(value: float) -> str:
    if value == int(value) and abs(value) < 1e15:
        return str(int(value))
    return repr(value)
