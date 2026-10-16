# Spec: greet(name, punctuation="!")

- Input `name`: any string; trimmed; empty-after-trim raises `ValueError`.
- Output: `f"Hello, {name}{punctuation}"` with trimmed name.
- Default punctuation: `!`.
- Observable acceptance: unit tests in `tests/test_greeter.py` assert exact strings; e2e asserts CLI stdout equality.
