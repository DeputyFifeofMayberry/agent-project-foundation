# Reliability guarantees

- Deterministic output for identical inputs; no randomness, no clock dependence.
- Failure modes are explicit: exit 2 + stderr for invalid names; argparse exit for missing args (`docs/PRODUCT.md` UJ table).
- No persistent state, so there is no recovery path to test; reliability evidence is the repeated green gate (`verify.py --ci`).
- The build check is idempotent: it rebuilds `dist/greeter.pyz` from scratch each run.
