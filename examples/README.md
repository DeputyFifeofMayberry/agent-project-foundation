# Stack example configurations

`project.node-react.example.json` uses verifier schema v2 (`argv` plus `timeout_seconds`) and illustrates how to configure real package scripts for a React/Electron project. **None of these npm script names is guaranteed to exist in your application.** Add actual test/lint/build commands and scripts to its `package.json` before copying this example to `.foundation/project.json`.

Do not blindly remove gates to get a green CI run. If a mandatory capability does not exist yet, implement a meaningful test/command, record the gap, and keep the PR blocked until the agreed baseline has been established.

For iOS Swift/Xcode, replace commands with actual Xcode scheme/workspace commands and add a macOS GitHub Actions runner with simulator availability. For Windows/Electron desktop integration tests add a Windows runner; the default Ubuntu job is not sufficient. For Python applications use actual Ruff/Pyright/Pytest commands and project build tooling.
