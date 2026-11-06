# Coverage audit

Date: 2026-10-24. Scope: all 175 leaf rows of `ai-engineering-building-applications-with-foundation-models/coverage-matrix.csv`, tiling PDF pages 1-991 of the source book.

Re-checked 2026-10-28: after wording edits (author name removed, docs refreshed), `run_all_checks.py --final` passes and the test suite passes (133 passed, 1 skipped). Row verification itself was not repeated.

## What was checked, and by whom

1. **Structure (scripts).** `scripts/run_all_checks.py --final --tests` passes: every row is `VERIFIED`, every ACTIONABLE row is named by a workflow, every KNOWLEDGE_ONLY row is indexed, links resolve, the core holds no project-specific strings, and generated indexes are current. 132 pytest tests pass. Scripts prove structure and presence only. They do not prove that a claim matches the book.
2. **Independent verification of every row.** Each module was re-read against the extracted source text and rendered pages (equations, figures, tables) by a verifier agent that was not the writer. Verifiers fixed defects in place and recorded corrections in the row's `verification` field.
3. **Independent audit sample.** A separate agent audited 30 rows, with every chapter represented and the equation/table-heavy sections included. Result: **22 PASS, 8 MINOR, 0 FAIL**. The minor findings were wording or labelling issues: some sentences that were the skill's own interpretation were not marked `INTERPRETATION`, a few cross-links were presented as page content, one figure description over-specified marker positions, and some page cites sat beside the wrong clause. All were corrected (rows C02-010, C02-011, C03-004, C04-004, C07-009, C07-013, C08-003, C10-001, C10-012) and the correction is noted in each row.

## What this does and does not support

- Supported: every section of the book from the Preface to the Epilogue and the Index has a module with page citations, an independent verification record, and a place in the workflows or index.
- Not supported: a claim that the modules are error-free. The audit sampled 30 of 175 rows (about 17%); the other rows rely on the single verifier pass. The audit found no failures, but a sample cannot rule out defects elsewhere.
- Modules are original-wording notes with short quotes, not reproductions. Verbatim reuse is capped by `coverage_check.py`.

## Residual gaps

See `known-gaps.md`. In short: some tables and figures are clipped in the source PDF, some figure values were read from charts and are estimates, a few book slips are noted, and 48 Index entries could not be mapped to a module (the Index points at headings, not page numbers). None is hidden. Each is recorded against its row.

## Re-running the audit

Pick a fresh sample (for example with a different seed), give a new agent only the extracted source text and the module, and have it rate fidelity, completeness and citation accuracy. Record the results here with the date.
