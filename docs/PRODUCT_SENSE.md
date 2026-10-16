# Product sense

rpn-calc exists because the smallest useful calculator is also the easiest calculator to verify: a pure token stream, no precedence table, no hidden state.

Decisions this implies:

- **Errors are values, not crashes.** Any invalid expression exits `2` with one stderr line; stdout stays clean for pipelines.
- **The stack is the output.** Printing the whole final stack (not just the top) keeps multi-result expressions observable.
- **Integers print as integers.** `7.0` renders as `7` so shell arithmetic feels native; genuine fractions keep full precision.
- **Headless by design.** There is no UI surface, so `docs/DESIGN.md` and `docs/FRONTEND.md` are declared not applicable in `.foundation/project.json` with explicit reasons, per the whitelist mechanism in `docs/COMPONENTS.md`.

When in doubt, add capability to the engine and keep the CLI contract (one line out, exit code) frozen.
