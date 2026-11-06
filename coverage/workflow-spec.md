# Workflow specification (contract for workflow writers)

Workflows turn the book's knowledge (the modules under `core/`) into procedures the skill follows. A workflow is not a summary of modules. It says what to decide or check, in what order, using which criteria, and what evidence closes each step. Every substantive instruction must be traceable to a module (the book) or labelled as not from the book.

## Where workflows live and how they are named

`workflows/architect/<name>.md` (Architect mode) and `workflows/review-test/<name>.md` (Review & Test mode). Relative links from a workflow to a module use the path recorded in `destination_file` in the relevant coverage matrix (for example, `../../core/ai-engineering-building-applications-with-foundation-models/<chapter-folder>/<file>.md`); a link checker rejects broken links. Links to templates use `../../templates/<file>.md`.

## File format

```markdown
---
name: model-selection
mode: architect            # architect | review-test
rows: [C04-008, C04-009, C04-010]   # every matrix row id this workflow relies on
---
# Model selection

## When to use
...
## Inputs needed
(What must be known before starting; ask the user only for what discovery did not answer; refer to `intake.md` for how to ask.)
## Modules to load
| Row | Module | Why it is needed here |
|---|---|---|
| C04-008 | [Model Selection Workflow](../../core/ai-engineering-building-applications-with-foundation-models/ch04-eval-systems/p356-model-selection-workflow.md) | ... |
## Procedure
1. Step ... Criteria and decision rule ... `[C04-008]`
...
## Evidence and exit gate
...
## Outputs
(Which template to fill: `../../templates/decision-record.md`, etc.)
## Pitfalls
(Failure modes the book names, each with its row id.)
```

Review & Test workflows also contain a **Checks** table: `check` (short id such as `PR-03`), `what is checked`, `how` (a command run through `scripts/run_check.py`, a probe, an eval run, or a code/config review), `evidence produced`, `type` (`run` or `review`), `criterion` (row id), `how a failure is judged`. `review` checks end as `REVIEWED`, never `PASSED`. A check with no book basis is labelled `SUPPLEMENTARY` in that table.

## Rules

1. **Trace every instruction.** After each substantive instruction cite the row id in backticks and brackets, like `[C05-016]`. Anything not from the book is prefixed `INTERPRETATION:` (your operational adaptation of a book idea) or `SUPPLEMENTARY:` (outside knowledge, with the source named). Do not invent book content, numbers or page references. Read the modules you cite; do not work from memory of the book.
2. **Name every assigned row.** Each row id assigned to your workflow in the brief must appear in the body at least once as `[ID]`, and in the `rows:` list. A final checker fails any actionable row that no workflow names.
3. **Decide, don't summarise.** State the decision rules, thresholds the book gives (with the row id), what to do when evidence conflicts, and what the user must confirm. Prefer short decision tables to prose. Do not paste module text.
4. **Honest evidence.** In Review & Test workflows a result is `PASSED` only with an execution record from `run_check.py`; reading code or config is `REVIEWED`; an environment or access problem is `BLOCKED`; a finding resting only on an AI judge is capped at `probable` (the book's limits of AI as a judge are in `[C03-016]`). Never tell the skill to claim something it cannot evidence.
5. **Safety.** Production is read-only; paid model calls need approval and a spend cap; no secrets in outputs; attacks are probed only against the user's own system at the level of detail the book gives.
6. **Project independence.** No project names, paths, vendors-as-requirements or stack assumptions. Where the book names tools or models as examples, say they are examples and time-sensitive.
7. **Length.** Aim for 80-200 lines. Longer means module content was copied in; shorter usually means the decision rules are missing.
8. **Do not touch** the matrix, the modules, scripts, or any file other than your assigned workflow files. Return a compact report listing each file and the row ids it names, plus anything you could not ground in a module.

## Verification of a workflow

A different agent re-reads each workflow against the cited modules and checks: every cited row id is relevant and correctly used; no instruction is unsupported; the decision rules match the modules; the Checks table is executable by a tool-using agent without invented capabilities; links resolve; every assigned row is named.
