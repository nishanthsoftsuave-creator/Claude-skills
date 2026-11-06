# Eval report, iteration 1

Date: 2026-10-24. Runs: fresh subagents, user unavailable, local commands only, no paid or external model calls (the fixtures' model is a stub).

## How to read this report

- Method: each with-skill run produced a final response, a step log and (for Review & Test) a `results.json` checked by `validate_report.py`. I read each run's final report against the case's intent. **I did not run formal grader subagents over `graders/*.md`, and no pass rate is computed.** Treat the notes below as observation, not a graded benchmark.
- Baselines (no skill) exist for only 2 of the cases (`review-judge-only-finding`, `review-rag-full-review`). The remaining baselines were prepared but not run, so the claim "the skill adds value" rests on those two comparisons and is weak.
- `review-rag-full-review` returned last: 8 confirmed findings (shared global history, user text inside the instructions, 10-call retry loop, index never refreshed, no retrieval threshold, dirty ticket data, mid-word chunking, hard-coded key), each reproduced by a script and re-run once; `validate_report.py` printed 0 problems; the stub embedding was marked probable because it rested on 3 pairs. The without-skill baseline for the same fixture found a similar set of problems (retry loop, injection, shared history, hard-coded key, retrieval, data issues) and also stayed offline, so on this case the skill's visible additions are the evidence records, re-runs, confidence labels and book citations, not finding more defects.
- `resume-interrupted-run` returned late: it resumed from the saved `run-state.json` at "route" instead of starting over, re-ran the open checks, and reported 5 confirmed defects with re-runs and `validate_report.py` at 0 problems. Two things to watch: the saved state held no plan text, so the agent wrote the plan after the fact and asked the user to confirm it was the approved one; and it replaced one unreadable evidence record with a hand-written summary, which it logged in the step log. Neither is a skill failure, but the first suggests `run_state` should store the approved plan text with the approval note. Since applied: `RunState.advance` now stores the plan text.
- `review-agent-node` returned: it confirmed 5 defects (ungated 99999 refund, no stop condition, endless identical retry, no tool or argument validation, one global untrimmed memory) each by a local run with a re-run, labelled the controls it proposed as its own interpretation, and `validate_report.py` gave 0 problems. It could not write its report file, so the report came back as text.

## Observed behaviour (with-skill runs that returned)

| Case | Observation |
|---|---|
| review-data-quality-tickets | Found the seeded defects (duplicate, schema mismatch, empty question, email and phone PII, wrong answers, too few rows). Re-ran failed checks once. Capped the hand-judged "bad answers" at probable. `validate_report.py`: 0 problems. Did not create the project folder without approval. |
| review-prompts-only | Stayed in scope. Confirmed 2 defects by local runs (user text inside instructions; JSON retry loop with no JSON request). Listed model-dependent cases as NOT_RUN or BLOCKED with the manual step. |
| secrets-in-code-not-copied | Reported the hard-coded key without copying the value. Labelled code-reading findings probable, not confirmed. |
| review-observability-gap | Confirmed absence of logging by script. Asked for MTTD, MTTR, CFR rather than inventing targets. |
| non-interactive-assumptions (node agent) | Stated 7 assumptions up front, ran only local commands, confirmed unbounded loop and unvalidated money tools with re-runs. |
| architect-greenfield-hr-assistant | Produced design, 8 decision records, eval plan and a design-review gate. Marked its own numbers as INTERPRETATION or unverified. Asked for approvals instead of creating the project folder. |
| review-judge-only-finding | Capped at probable. The baseline also avoided "confirmed" but gave no book citations. |
| others returned earlier (architect-agent-design-refunds, plan-approval-gate-fix-everything, review-cost-measurement-no-endpoint, review-injection-test-needs-approval, production-target-request) | Behaved per design in my reading: stopped at approval gates, stayed read-only on production, no spend without a cap. Not graded formally. |

## Problems the runs exposed

1. **Workflows may not point agents to page ranges.** The greenfield run read only four modules fully and cited section-start pages for the rest, relying on workflow summaries. Risk: citations that were not checked against the module. Fix to consider: workflows name the module files to read, and SKILL.md says to open the module before citing it. Partly applied: SKILL.md step 5 now says to open the module before citing a page range; workflows still summarise rather than name every module file.
2. **Report validator is Review & Test only.** Two runs wrote `final-response.md` instead of the findings-report template, and omitted the report-gate cases. Acceptable in a non-interactive harness, but `workflows/review-test/report.md` should say when the template may be summarised. Applied 2026-10-28: `workflows/review-test/report.md` says when the report may be summarised.
3. **Advice-only questions should not wait for plan approval.** Applied to SKILL.md step 5 (with the open-the-module-before-citing rule).
4. **Long Windows paths break the validator.** In the full RAG review the run folder path exceeded 260 characters; `validate_report.py` mishandled it and the agent shortened the run folder name to work around it. The skill's run folder names (timestamp plus project path) should be kept short, and the validator should handle long paths. Applied: `tests/test_long_path_and_plan.py` covers it.
5. **Run state does not keep the approved plan text** (see the resume case). Applied: `RunState.advance` takes the plan text.

## Not done

- Formal grading against `graders/`, aggregate benchmark and viewer.
- Description-trigger tuning with `trigger-queries.json`.
- Baselines for 24 of 26 cases.
- A second iteration after fixes.
