# Maintenance guide

The skill has one rule that all maintenance protects: **every section of the book is covered, and nothing counts as covered until it has been written and independently verified.** The coverage matrix is the record; scripts enforce its structure; verification by a second reader enforces its substance.

## The pieces and how they relate

- `coverage/<book>/coverage-matrix.csv`: one row per leaf section for each book. The original AI Engineering book has its own folder; legacy root-level matrices remain supported. Columns: `id, chapter, section_path, start_page, end_page, tail_page, role, role_reason, destination_file, status, verification, gaps`. Roles: `ACTIONABLE` (must be named by at least one workflow), `KNOWLEDGE_ONLY` (must be linked from the index), `NON_SUBSTANTIVE` (no module; a reason is recorded). Statuses: `NOT_STARTED`, `IN_PROGRESS`, `IMPLEMENTED` (written, not yet verified), `VERIFIED` (re-read against the source by someone other than the writer), `GAP` (material missing or unreliable; say exactly what in `gaps`). Change the matrix only through `scripts/matrix_update.py` (a single writer, so parallel agents cannot clash).
- `core/<book>/<chapter>/pNNN-<slug>.md`: one module per row, in the format of `coverage/module-spec.md`.
- `workflows/`: procedures in the format of `coverage/workflow-spec.md`. Each names the rows it relies on in `rows:` and cites them in the body as `[ID]`.
- Generated, never hand-edited: `core/ai-engineering-building-applications-with-foundation-models/index.md`, `core/ai-engineering-building-applications-with-foundation-models/concepts.md`, `core/ai-engineering-building-applications-with-foundation-models/xref.md` (`scripts/build_index.py`), `core/ai-engineering-building-applications-with-foundation-models/front-back-matter/p932-index.md` (`scripts/build_term_index.py`), the content-gaps section of `coverage/known-gaps.md` (`scripts/gaps_report.py`).

## Checks (run them after every change)

```
python scripts/run_all_checks.py --source-dir <extracted-source-dir> --tests
python scripts/run_all_checks.py --final --source-dir <extracted-source-dir>   # release gate
```

`run_all_checks.py` runs: `coverage_check.py` (matrix structure, page tiling, modules exist, frontmatter and citations, size floor, verbatim-copy ceiling; with `--final`, every row VERIFIED or an explained GAP, every ACTIONABLE row named by a workflow, every KNOWLEDGE_ONLY row linked), `link_check.py`, `core_purity_check.py` (no personal paths, emails or secret shapes in the core), `workflow_check.py`, and a freshness check that the generated index files match the modules. These checks prove structure, not correctness: they cannot tell that a claim is right or that a verifier really re-read the source. That is why verification is a separate step.

## Extracting the source text

`scripts/extract_rows.py <book.pdf> coverage/<book>/coverage-matrix.csv <out-dir>` writes one text file per row (page markers, plus the tail page) and an `index.json` flagging pages that need a visual check. `--render` makes PNGs of pages. The text layer flattens superscripts and subscripts and clips some tables: formulas and tables must be read from rendered pages.

## Revising or adding a section (the pipeline)

1. Update the row (or add rows with `build_matrix.py` if the book's outline changed; keep the page tiling exact). Set the status `IN_PROGRESS`.
2. **Write** the module from the extracted text and rendered pages, following `coverage/module-spec.md` (original wording, `(PDF p. N)` citations inside the row's range or its tail page, labels, equations from the rendered page). Write nothing the book does not say as book content.
3. Set `IMPLEMENTED` and run `coverage_check.py --source-dir` (catches wrong citations, too-short modules, copied text, unknown `related` ids).
4. **Verify with a different reader**: re-read the source and the rendered pages, check accuracy, completeness, citations, framing, original wording; fix defects; record `VERIFIED` with a note of what was checked and any residual gap in `gaps`.
5. Regenerate the indexes (`build_index.py`, `gaps_report.py`, and `build_term_index.py` if rows changed) and run all checks.
6. If the section is ACTIONABLE, make sure a workflow names it; update the workflow and have it re-verified against the changed module.

Do not mark a row VERIFIED because the checks pass. Do not shrink a module to fit a context limit: split the work across rows and resume from the matrix.

## Keeping it useful across projects

- The core stays project-independent: no project names, paths or stack assumptions (the purity check enforces the obvious cases). Project details live only in each project's `.ai-architecture-and-reviewer/`.
- Refresh time-sensitive material deliberately. Modules flag dated statements (`time_sensitive: true` and a list in the body). To refresh, add a clearly labelled `SUPPLEMENTARY:` line with a named current source; never overwrite what the book says.
- If a new edition of the book appears, treat it as a new source: rebuild the matrix, and carry over verified modules only after re-verifying them against the new text.

## Evaluating the skill itself

`evals/` holds one folder per scenario (Architect and Review & Test, including negative cases: no AI components, thin evidence, an unavailable tool); see `evals/README.md` for the layout and how to run them. `evals/fixtures/` holds small unrelated sample projects. Run the scenarios in fresh agent sessions with the skill, grade the results against each scenario's expected behaviour, and record them in `evals/reports/`. Re-run them after any change to `SKILL.md`, routing or a workflow, and compare with the previous report before accepting the change. The trigger description in `SKILL.md` is tuned with the should-trigger and should-not-trigger queries in `evals/trigger-queries.json`.

## Known limits of the tooling

- `run_check.py` redacts common secret shapes, not personal data; scripts that read user data must print aggregates only.
- `validate_report.py` checks structure and evidence presence (including a re-run note, a known basis for confirmed findings, evidence for reviewed cases). It cannot judge whether a finding is correct.
- Generated index terms come from a heuristic parse of the book's own Index; entries it cannot resolve are listed as `unmapped` in the known-gaps register.
