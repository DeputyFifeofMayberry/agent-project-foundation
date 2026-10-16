# Product

rpn-calc evaluates reverse-polish notation (RPN) expressions from the command line.

## Job to be done

A developer or operator wants to compute an expression in one shell command without leaving the terminal and without operator-precedence ambiguity. RPN removes parentheses entirely: operands first, operator after.

## Essential flows

1. **Happy path:** `python3 -m app 3 4 +` prints `7` and exits `0`.
2. **Compound expression:** `python3 -m app 5 1 2 + 4 * + 3 -` prints `14` (the classic Dijkstra example) and exits `0`.
3. **Evaluation error:** `python3 -m app 2 0 /` prints `error: division by zero` on stderr and exits `2`.
4. **Usage error:** `python3 -m app` with no tokens prints usage on stderr and exits `2`.

## Non-goals

- No interactive REPL, no floating-point formatting options, no operator extensions (`%`, `^`) in this baseline.
- No persistent history or config files: the tool is a pure function of its arguments.

## Quality bar

The `unit` category covers engine semantics including error cases; `integration` covers CLI-plus-engine behavior in-process; `e2e` launches the real CLI in subprocesses. See `docs/TESTING.md` and `docs/BASELINE.md` for the verification contract.
