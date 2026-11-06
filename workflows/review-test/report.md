---
name: report
mode: review-test
rows: [C01-018, C03-016]
---
# Final Review & Test report

## When to use
At the end of a Review & Test run, after checks have been executed or marked, findings re-run once, and `results.json` written. This workflow turns `results.json` into the report using [the findings report template](../../templates/findings-report.md). It adds no new testing. In a non-interactive harness, or when the user asks for a short answer, the report may be summarised in the final message instead of the full template, but `validate_report.py` must still print 0 problems on `results.json`, and what was not tested must still be stated.

## Inputs needed
- `<run_dir>/results.json` and the `evidence/` folder it references (shape: see [results.example.json](../../templates/results.example.json)).
- The list of modules and rows used, the spend cap if model calls were made, and the assumptions recorded at plan approval.

## Modules to load
| Row | Module | Why it is needed here |
|---|---|---|
| C03-016 | [Limitations of AI as a Judge](../../core/ai-engineering-building-applications-with-foundation-models/ch03-eval-methodology/p281-limitations-of-ai-as-a-judge.md) | why a judge-only finding is never confirmed; how to word judge-based evidence |
| C01-018 | [Maintenance](../../core/ai-engineering-building-applications-with-foundation-models/ch01-intro/p088-maintenance.md) | time-sensitivity of model, price and benchmark claims; versioning and re-evaluation as the maintenance practice |

## Procedure
1. **Validate first.** Run `python scripts/validate_report.py <run_dir>`. It must print `0 problem(s)` before any prose is written. Fix the data in `results.json` or the evidence, never the validator. Re-run after each fix.
2. **Classify every finding by its real evidence.**

   | Evidence behind the finding | Highest label allowed |
   |---|---|
   | A FAILED case with a `run_check.py` record, repro steps, and a same-result re-run | `confirmed` |
   | Reproduced once, or code or config reading that strongly implies the defect | `probable` |
   | Judge model only (`basis: judge`) | `probable` at most, state the judge's limits |
   | Pattern or exposure that could matter, not shown to fail | `risk` |
   | Suggested improvement without a defect | `recommendation` |
   | Could not be checked | `unverified` |

   A judge can be inconsistent across runs, sensitive to prompt wording, biased (self-bias, first-position bias, verbosity bias), unstandardized across tools, and its scores shift if the judge model or prompt changes `[C03-016]`. For a judge-based finding therefore state which judge model and prompt version scored it, whether the scores were repeated, and what exact or human check is missing. The book says judges should be supplemented with exact evaluation or human evaluation `[C03-016]`. Do not trust a judge whose model and prompt you cannot see `[C03-016]`. When two runs used different judges, do not report a score change as an application change `[C03-016]`.
3. **Order findings** within each section by severity (critical, major, minor, trivial), then by user impact, then by strength of evidence. Confirmed findings come first, then probable, then risks and recommendations (one line each).
4. **Cite the criterion behind every finding.** In the "Expected" field give the matrix row id and PDF pages taken from the cited module's `source_pages` and its in-text `(PDF p. N)` marks, in the form "criterion C0X-NNN, PDF p. N". Take the row ids from the case's `criteria_refs`. A case without a book basis is marked supplementary and the report says "not from the book". Never invent a page number: if the module does not state it, cite the module's page range.
5. **State what was not tested.** List every case that is BLOCKED, SKIPPED or NOT_RUN with its reason from `results.json` and the manual step that would cover it, even when the list is long. A case never run is never described as passed. Group the REVIEWED cases and say plainly that code or configuration was read, not executed.
6. **Flag time-sensitive claims.** The book dates from a point in time; model names, benchmark scores, prices and regulatory or cost estimates can be stale, and the pace of change is itself a maintenance risk `[C01-018]`. Where a finding or recommendation leans on such a figure, add "time-sensitive: as of the book's writing" and the module's own time-sensitive note. Recommend re-running affected checks after a model, provider or price change `[C01-018]`. INTERPRETATION: keep versioning and evaluation infrastructure so model swaps are testable (the module's own practice note).
7. **Keep it short.** Use the template's sections only when they have content. Target: a verdict of two sentences, counts, then findings. One finding is about six lines; do not paste logs, quote evidence paths instead. Merge findings that share a root cause. Give risks without evidence one line each. If the result is simple (all PASSED, nothing else), say so in the summary and omit empty sections.
8. **Write the summary honestly.** Counts must match `results.json` (the validator checks the case counts). The verdict says what is solid and what is not, and says plainly if the evidence is thin.
9. **Next steps.** Order by impact. Offer follow-ups (tickets, a redesign through `handoff-to-architect.md`) without performing them. Updating the project layer happens only with approval.

## Checks
| check | what is checked | how | evidence produced | type | criterion | how a failure is judged |
|---|---|---|---|---|---|---|
| RP-01 | `results.json` passes the report gate | `python scripts/validate_report.py <run_dir>` through `run_check.py` (case `RP-01`; the validator exits 1 on problems, so record this case only for the run that prints 0 problems) | `RP-01.exec.json` | run | C03-016 | any printed problem: fix the data, re-run |
| RP-02 | No confirmed finding rests on a judge | review `basis` on every confirmed finding | notes | review | C03-016 | any: downgrade to `probable` |
| RP-03 | Every finding cites a row id and pages | review the draft against the modules | notes | review | C03-016 | missing citation: add it or mark as not from the book |
| RP-04 | Time-sensitive claims flagged | review the draft | notes | review | C01-018 | unflagged price, model or benchmark claim: flag it |

RP-01 can be PASSED with its record; RP-02 to RP-04 are REVIEWED. Order: run the validator directly until it prints 0 problems; run it once more through `run_check.py` as `RP-01` (its record and `results.json` are then complete); add the `RP-01` to `RP-04` cases to `results.json` (update `summary`, if present, to include them) and confirm with a final direct validator run.

## Evidence and exit gate
Handover checklist, all must hold:
- [ ] `validate_report.py` printed `0 problem(s)` on the final data.
- [ ] Counts in the summary equal the case counts; finding counts match the labels.
- [ ] No `confirmed` finding without a FAILED case, evidence, repro steps, impact and a re-run note.
- [ ] No judge-only finding above `probable`.
- [ ] "Not tested, and why" lists every BLOCKED, SKIPPED and NOT_RUN case.
- [ ] Every finding has a criterion (row id and PDF pages) or is marked not from the book.
- [ ] Time-sensitive figures flagged; assumptions stated with what would change them.
- [ ] No secrets, keys or personal data in the report or evidence; spend against the cap stated.
- [ ] Follow-up actions are offered, not performed.

## Outputs
The filled [findings report](../../templates/findings-report.md) saved in the run folder. Nothing is sent or filed outside the project without confirmation.

## Pitfalls
- Presenting a judge score as proof; high judge consistency does not mean accuracy `[C03-016]`.
- Reporting a metric trend across a silent judge change `[C03-016]`.
- Quoting prices, models or benchmark figures as current `[C01-018]`.
- Lengthening the report to look thorough; clarity about confidence matters more than volume.
- Turning REVIEWED into PASSED, or omitting BLOCKED cases, to improve how the result looks.


## Wording guide
| Situation | Say | Do not say |
|---|---|---|
| Judge scored 3.2 of 5 on faithfulness | "Probable: judge `<model>`/prompt `<version>` scored 3.2; not confirmed by an exact or human check" `[C03-016]` | "The system is unfaithful" |
| Case never run | "NOT_RUN: `<reason>`; manual step: `<step>`" | "No issues found" |
| Code read, behaviour not run | "REVIEWED: configuration reads as X; not executed" | "PASSED" |
| Price or model figure from the book | "time-sensitive, as of the book's writing" `[C01-018]` | "costs X today" |
