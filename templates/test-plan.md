# Test plan: <project or component>

Date: <date> · Mode: Review & Test · Status: awaiting approval

Approval is needed before any check is run, any file is changed, or any paid model call is made.

## Scope

What is in, what is out, and the environment. Production is read-only. Spend cap for model calls: <amount or none>.

## Assumptions

Each assumption, and which answer would change the plan.

## Cases

| ID | What is checked | How | Criterion (module id, PDF p.) | Evidence produced | Type |
|---|---|---|---|---|---|
| T1 | | command via `run_check.py`, probe, eval run, or code review | | exec record, output file, notes | run / review |

- `run` cases are executed through `scripts/run_check.py` so they leave an execution record.
- `review` cases read code or configuration; they end as `REVIEWED`, never `PASSED`.
- Every case cites the book criterion behind it. A check that has no book basis is marked `supplementary` and labelled that way in the report.

## Cannot be run

Checks that need access, data, or permission that is missing. Each becomes `NOT_RUN` or `BLOCKED` with the reason and the manual step that would cover it.

## Evidence and confidence rules

- A failure is re-run once before it is called confirmed.
- A finding that rests only on an AI judge's verdict is capped at `probable`.
- Weak evidence is labelled `probable`, `risk` or `unverified`, never `confirmed`.

## Exit criteria

When the run is complete: every planned case has a status, `validate_report.py` reports 0 problems, and the report lists everything that was not tested.
