# Reliability

rpn-calc reliability contract: correct answers, honest errors, no partial output.

## Failure modes and handling

| Failure | Behavior | Covered by |
|---|---|---|
| Division by zero | `error: division by zero` on stderr, exit `2`, stdout empty | unit, integration, e2e |
| Operand underflow (`1 +`) | `error: insufficient operands for '+'`, exit `2` | unit |
| Invalid token (`x`) | `error: invalid token 'x'`, exit `2` | unit |
| No arguments | argparse usage on stderr, exit `2` | integration, e2e |

## Invariants

1. **stdout is either one result line or empty** — never a partial stack followed by an error. Errors go to stderr only.
2. **Exit codes are stable:** `0` success, `2` any error. CI and scripts may rely on them (see `ARCHITECTURE.md`).
3. **Determinism:** same tokens, same output; no randomness, no time, no environment dependence.

## Recovery

There is no persistent state to corrupt; a failed run leaves nothing behind (checks are read-only, builds happen in temp directories). Failure recovery is always "re-run with corrected input".
