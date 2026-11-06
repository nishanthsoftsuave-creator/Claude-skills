---
name: run-checks
mode: review-test
rows: [C03-010, C03-011, C03-012]
---
# Run the checks the environment permits

## When to use
After the user has approved the test plan (`test-plan.md`). This workflow executes the `run` cases and records every result so `scripts/validate_report.py` can pass. `review` cases are not executed here; they are read and recorded as `REVIEWED`.

## Inputs needed
- The approved plan with case IDs, the commands to run, the spend cap, and the run directory (`<run>/`, with `<run>/evidence/` and `<run>/results.json`).
- Run commands, test commands and environment details given by the user or found in discovery. If none exist, say so; do not guess install steps that change the project.
- Reference data for any similarity check, and approval for any call to a paid model or embedding API.

## Modules to load
| Row | Module | Why it is needed here |
|---|---|---|
| C03-010 | [Functional Correctness](../../core/ai-engineering-building-applications-with-foundation-models/ch03-eval-methodology/p253-functional-correctness.md) | Tests and execution as the strongest automatic check; pass@k |
| C03-011 | [Similarity Measurements Against Reference Data](../../core/ai-engineering-building-applications-with-foundation-models/ch03-eval-methodology/p257-similarity-measurements-against-reference-data.md) | Exact match, lexical and semantic similarity; reference-data limits |
| C03-012 | [Introduction to Embedding](../../core/ai-engineering-building-applications-with-foundation-models/ch03-eval-methodology/p267-introduction-to-embedding.md) | What an embedding is and how its quality is judged |

## Procedure
1. **Run existing test suites first.** Functional correctness, whether the application does its job, is the ultimate metric, and software tests that run code in varied scenarios and compare against expected outputs are the established way to automate it. `[C03-010]` Execute each suite as one case: `python scripts/run_check.py --case T1 --evidence-dir <run>/evidence -- <test command>` (add `--timeout` for slow suites). Read the exec record, not the console. A record with `status: EXECUTED` and `exit_code: 0` supports `PASSED`; a non-zero exit supports `FAILED`. `run_check.py` itself always exits 0 and prints only a one-line summary, so the record is the result. Mechanics of the real script: the command runs without a shell (no pipes, `&&` or redirects; wrap them in a small script under `<run>/scripts/`), in the current working directory (there is no `--cwd` option), so start from the project directory and give the absolute path to the skill's `scripts/run_check.py` when the tests must run inside the project. A timeout records `EXECUTED` with `exit_code: null`, which cannot be `PASSED`. INTERPRETATION: before running a project's test command, read what it touches; if it calls paid model APIs, production systems or writes outside the project's test fixtures, it needs the user's approval (and counts against the spend cap) or becomes `BLOCKED`/`SKIPPED`.
2. **Choose the exact method that fits the criterion**, using the plan's guideline.

| Situation | Method | Notes |
|---|---|---|
| Output can be verified by running it (code, SQL, a measurable objective) | functional correctness: run it against test cases with expected outputs `[C03-010]` | for several samples per problem report pass@k: a problem counts as solved if any of k samples passes all its tests `[C03-010]` |
| Short exact answers (arithmetic, trivia; labels by INTERPRETATION) | exact match against reference `[C03-011]` | the "output contains the reference" variant can accept wrong answers (a right year inside a wrong date); say which variant was used `[C03-011]` |
| Longer text with references | lexical similarity: token overlap, edit distance, n-gram `[C03-011]` | score is only as good as reference coverage; a correct output can score low if no reference resembles it `[C03-011]` |
| Same meaning, different wording | semantic similarity: embeddings plus cosine similarity (identical vectors 1, opposite -1) `[C03-011]` | needs an embedding model; its quality limits the result and it costs compute `[C03-011]` |
| No references and no automatic check | AI judge or human review | follow `evidence-and-confidence.md`; cap applies |

3. **Decide whether a reference-based check is possible.** It needs (input, reference) pairs; limited by how much reference data exists. References can be human-written or AI-generated, and AI-generated ones still need human review. `[C03-011]` References can themselves be wrong (WMT 2023 organizers reported many bad reference translations); INTERPRETATION: spot-check a handful before relying on a score. `[C03-011]` Hand-designed measures stay in wide use because they are exact; semantic similarity is exact given two embeddings but can be called subjective because different embedding algorithms give different scores. `[C03-011]` If the project has no reference data, build a small evaluation set (step 4) or mark the check `NOT_RUN` with the reason.
4. **Build a small evaluation set when none exists** (only if the plan approved it). Take real inputs from logs or fixtures the user provided (never scrape production, never copy secrets or PII into the set), write or obtain references, label each example with its slice, and save it under `<run>/evalset/`, not in the project. Keep it a measurement tool, not a claim of coverage: state its size and what difference it can detect (`test-plan.md`, Step 3 sizing). Re-score a resampled copy of the set several times; if results swing widely, say the set is too small to support a verdict (the sizing rules are in `test-plan.md`).
5. **Run the evaluation through `run_check.py`.** Put the scoring script in `<run>/scripts/`, not the project, and call it as `python scripts/run_check.py --case T7 --evidence-dir <run>/evidence -- python <run>/scripts/score.py ...`. The script writes its per-example outputs and the metric to a file in `<run>/evidence/` and exits non-zero only if the metric is below the agreed usefulness threshold. INTERPRETATION: with no agreed threshold, the script prints the measurement and exits 0, and you record the case as `REVIEWED` with the metric file as evidence and report the number; do not call it `PASSED`.
6. **Embedding-based checks.** The embedding model is chosen by you or the project; INTERPRETATION: record its name and vector size (real embedding vectors typically have 100 to 10,000 elements; model names and sizes are time-sensitive). `[C03-012]` A good embedding puts more similar texts closer (a cat-on-a-mat sentence nearer a dog-on-grass sentence than a sentence about AI research); run that small sanity check on a few pairs before trusting scores, because embeddings cannot be judged by eye. `[C03-012]` If the embedding model is a paid API or sends data off the machine, it needs the user's approval and counts against the spend cap. Embeddings pulled from a general chat model's intermediate layers may be worse than a dedicated embedding model. `[C03-012]`
7. **Record each case in `results.json`** (shape in `../../templates/results.example.json`). Fields: `id`, `title`, `status`, `criteria_refs` (the row id from the plan; may be empty only if `supplementary` is `true`), `supplementary` (true for a check with no book basis), `exec_record` (the `evidence/<case>.exec.json` path, relative to the run directory), `evidence` (files inside the run directory that exist and are not empty), `rerun` (`same`, `differs` or `not_possible`, required for `FAILED`), and `reason` (required for `BLOCKED`, `SKIPPED` or `NOT_RUN`). Add top-level `run_id` and `mode: review-test` as in the example; `summary` is optional but, if present, must equal the case counts. Write evidence files you author yourself (notes, response captures) into `<run>/evidence/`.

| What happened | Status to record |
|---|---|
| executed, exit code 0, criterion met | `PASSED` (needs `exec_record`) |
| executed, exit code non-zero or metric below threshold | `FAILED` (needs evidence, a `rerun` note, and a finding) |
| code or config read, not run | `REVIEWED` (needs evidence notes) |
| command not found, record shows `BLOCKED`, missing credentials, no endpoint, timeout from an environment cause | `BLOCKED` with reason |
| approved but deliberately not done | `SKIPPED` with reason |
| planned but not attempted | `NOT_RUN` with reason |

8. **Re-run each failure once.** Re-run the same command as a new record (for example case `T2-rerun`) and set `rerun` to `same` or `differs` on the original case; `not_possible` if it cannot be repeated. A failure that does not reproduce stays out of `confirmed` (the validator requires only that a `rerun` note exists; the `same` requirement is this skill's rule). For generated output, differing results across runs are expected, so compare against the criterion, not for identical text. (Skill rule in SKILL.md step 7.)
9. **Missing tool or access.** Never install packages or alter the project to get a check to run unless the plan approved it. Record `BLOCKED` (a tool or environment problem is not a project failure), give the exact reason, and name the manual step that would cover it. Do not substitute a weaker check without saying so.
10. **Keep the summary in step.** `summary` counts must equal the case counts, or `validate_report.py` reports a mismatch. Run `python scripts/validate_report.py <run>`; fix the data, never the validator.

## Checks
| check | what is checked | how | evidence produced | type | criterion | how a failure is judged |
|---|---|---|---|---|---|---|
| RN-01 | Existing test suite passes | `run_check.py` with the project's test command | exec record | run | C03-010 | non-zero exit; confirm by one re-run |
| RN-02 | Code-generating or SQL-generating features pass their test cases | run the project's tests or a scoring script in the run directory | exec record, results file | run | C03-010 | any failed test case; report pass@k only if k samples were drawn |
| RN-03 | Short-answer or label outputs match references | exact-match script over the small eval set | exec record, per-example file | run | C03-011 | below usefulness threshold; no threshold means a measurement, not a verdict |
| RN-04 | Free-text outputs are close to references | lexical or embedding-similarity script | exec record, score file | run | C03-011 | same; also spot-check references |
| RN-05 | Embedding model sanity (similar pairs closer than unrelated) | script on a few pairs | exec record | run | C03-012 | ordering violated: scores from that embedding are not trusted |

## Evidence and exit gate
Every planned case has a status and the right artefacts: `PASSED` and `FAILED` have an exec record; `FAILED` has a rerun note and a finding; `BLOCKED`, `SKIPPED` and `NOT_RUN` have reasons; evidence files exist, are non-empty and sit inside the run directory. `validate_report.py` prints 0 problems (the final report is written only after that). No secret values are in any evidence file; `run_check.py` redacts common shapes but check anyway.

## Outputs
`<run>/results.json`, `<run>/evidence/*`, and the evaluation set and scripts under `<run>/`. Findings are classified in `evidence-and-confidence.md`; the report follows `../../templates/findings-report.md`.

## Pitfalls
- Calling a code read `PASSED`: it is `REVIEWED`. (skill rule)
- Trusting an exact-match score on open-ended text: many valid answers are missed. `[C03-011]`
- Optimizing or trusting lexical overlap as a proxy for correctness: in code, BLEU scores for incorrect and correct solutions can be similar. `[C03-011]`
- Reference data that is incomplete or wrong. `[C03-011]`
- Reporting a similarity score from an embedding model you did not sanity-check. `[C03-012]`
- Functional correctness is not always automatable; do not force it onto subjective tasks. `[C03-010]`
- Treating a timeout or missing binary as a project failure. (skill rule)
