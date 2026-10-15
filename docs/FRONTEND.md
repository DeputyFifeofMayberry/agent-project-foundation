# Frontend and mobile verification

Supported runtimes and screen sizes: protection-test project (disposable)

## Minimum flow verification

1. Start the actual app in an isolated environment.
2. Exercise the relevant journey end to end, including restart/persistence as applicable.
3. Check loading, empty, network failure, retry, permission denial, and error feedback.
4. Check keyboard, touch/focus, small screen, and accessibility for affected UI.
5. Inspect console/runtime errors, network calls and traces where available.
6. Capture proof (test report, screenshot or video) for major UI changes and tie it to the tested commit/environment.

**Tool selection:** Playwright for browser/Electron renderer paths when appropriate; platform-specific automated tooling for iOS and OS integrations. Browser E2E is not a substitute for native iOS integration tests. Add stack-specific commands to `TESTING.md` and `.foundation/project.json`.
