# Architecture

rpn-calc is a three-layer command-line application with a strict dependency direction:

```
app/__main__.py  ->  app/cli.py  ->  app/core.py
```

- `app/core.py` — pure evaluation engine (`evaluate`, `format_stack`, `RpnError`). No I/O, no CLI imports. This is the only module containing arithmetic or parsing rules.
- `app/cli.py` — argument parsing and process exit-code policy. Calls the engine, prints one output line or one `error:` line on stderr.
- `app/__main__.py` — entry point so the tool runs as `python3 -m app ...`.

Dependency rules (enforced by the `architecture` check in `tools/architecture.py`):

1. `app/core.py` never imports `app.cli` or `app.__main__`.
2. `app.cli.py` never imports `app.__main__`.
3. Application code never imports the `tests` package.
4. Tools under `tools/` never import the application package, so verification stays independent of the code it verifies.

Exit-code contract: `0` success, `2` evaluation/usage error. The build artifact is a zipapp produced by `tools/build.py` into a temporary directory outside the checkout (read-only-safe checkout rule, `docs/STACKS.md`).
