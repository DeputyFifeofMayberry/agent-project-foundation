# Stack-specific minimum verification sets

These are practical **minimums** for configuring `.foundation/project.json` checks; riskier changes require more (`docs/TESTING.md`). Infrastructure checks (verifier self-tests, config validation) never substitute for the application checks below — a green gate is infrastructure health, not app acceptance (`docs/CHECKLISTS.md`). Adapt commands to the project's real toolchain and record them in the project configuration.

## Web apps (generic)

- Lint + typecheck (if typed); unit tests; production build; served smoke check that the built artifact answers on its port; one E2E happy-path of the top user journey.

## React / Next.js

- `eslint`; typecheck (`tsc --noEmit` or framework equivalent); unit/component tests; production build (`next build`); one E2E run (Playwright/Cypress) **against the production build**, not the dev server, covering the top journey; a route-level failure-state check (404/error boundary).

## Node backends

- Lint + typecheck; unit tests; integration tests against a real (e.g. containerized) datastore; boot check that the server starts and its health endpoint answers in production mode with env validation failing closed on missing configuration; contract tests for the public API schema.

## Electron

- Renderer web checks (lint, unit, build); packaged-build smoke test (artifact produced by `electron-builder`/`forge` actually launches); at least one scripted main-process test. Packaging/launch verification must happen on the target OS — a renderer web build alone is not app verification.

## Native iOS / macOS

**Linux-runnable checks alone NEVER verify the app.** Build, test, and lint must run on macOS with the project's Xcode toolchain (`xcodebuild`, `swift test`, `xcodebuild test` on simulator/device); UI verification requires a simulator or device run. Linux runners may validate infrastructure only (verifier self-tests, config checks). Record which checks ran on which OS; missing macOS execution is **BLOCKED**, never a pass.

## Python

- Lint (`ruff` or `flake8`); typecheck (`mypy`/`pyright`) if typed; `pytest` unit + integration; package build (`python -m build`); install into a clean venv and run the CLI entry point as a smoke test. Pin and record the interpreter version.

## API / database-backed

- All Node/Python backend checks above, plus: schema migrations applied **and reversed** against a disposable database; seed/rollback proven reproducible; contract tests for every public endpoint including authorization cases. Never run destructive migrations against shared data without explicit human approval.
