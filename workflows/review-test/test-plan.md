---
name: test-plan
mode: review-test
rows: [C03-002, C04-011, C04-012, C04-013]
---
# Test plan

## When to use
After `system-understanding.md` and `review-checklist.md`. Produces the plan the user approves before anything is run, edited or paid for. Fills `../../templates/test-plan.md`. Approval words are recorded with `RunState.advance("plan_approval", True, note=<their words>)` (see SKILL.md step 5).

## Inputs needed
- Component inventory and gap list (`system-understanding.md`); candidate checks, routes and cannot-run list (`review-checklist.md`).
- Scope: whole system or one component; the environment (dev, staging; production is read-only); how to run the project and its tests; what data, endpoints and logs are available; permission for paid model calls and a spend cap. Ask only for what is missing, at most four questions per round (`../architect/intake.md`).
- Known issues and the report audience.

## Modules to load
| Row | Module | Why it is needed here |
|---|---|---|
| C03-002 | [Challenges of Evaluating Foundation Models](../../core/ai-engineering-building-applications-with-foundation-models/ch03-eval-methodology/p234-challenges-of-evaluating-foundation-models.md) | Why eyeballing is not a test; evaluation has to be systematic |
| C04-011 | [Step 1. Evaluate All Components in a System](../../core/ai-engineering-building-applications-with-foundation-models/ch04-eval-systems/p393-step-1-evaluate-all-components-in-a-system.md) | Per-component, per-turn and per-task evaluation |
| C04-012 | [Step 2. Create an Evaluation Guideline](../../core/ai-engineering-building-applications-with-foundation-models/ch04-eval-systems/p396-step-2-create-an-evaluation-guideline.md) | Criteria, rubric, usefulness threshold, business mapping |
| C04-013 | [Step 3. Define Evaluation Methods and Data](../../core/ai-engineering-building-applications-with-foundation-models/ch04-eval-systems/p400-step-3-define-evaluation-methods-and-data.md) | Methods, slices, set size, evaluating the pipeline |

## Procedure
1. **Do not accept eyeballing as the project's test.** Many teams judge outputs by eye or keep a small ad hoc prompt set chosen from the curator's experience rather than the application's needs. That can be tolerable at project start but is not enough for iterating. `[C03-002]` If the project's only quality evidence is of this kind, say so in the plan as a finding candidate (`risk`) and plan to build a small evaluation set (see `run-checks.md`).
2. **Step 1: one test group per component and per level.** For every inventory row that processes data in stages, plan a check of the final output and a separate check of each stage's intermediate output, so a wrong answer can be traced to a stage. `[C04-011]` Example shape from the book: text extraction from a PDF scored by similarity to ground-truth text, then field extraction scored by accuracy on correctly extracted text. `[C04-011]` For multi-turn systems plan both per-turn (quality of each output) and per-task (was the task completed, and in how many turns) checks; per-task matters more to users but task boundaries are hard to determine, so record how the project defines one. `[C04-011]`
3. **Step 2: state the guideline the checks will be judged against.** Use the project's own written guideline if it exists. If not, draft one and mark it as an assumption for the user to confirm: what the application should and should not do (including out-of-scope inputs and the expected response), criteria for a good response (for a support app the book's example is relevance, factual consistency, safety), a scoring system per criterion with rubric examples, and the minimum score that makes the application usable. `[C04-012]` A correct answer is not always a good one, so criteria must say what "good" means. `[C04-012]` To arrive at criteria, the book experiments with test queries, ideally real user queries, producing several responses per query and deciding which are good or bad. `[C04-012]` Validate the rubric with a person where possible; an unclear rubric yields unclear scores. `[C04-012]` Where a business metric is known, map metric levels to outcomes; do not invent the mapping. `[C04-012]` INTERPRETATION: checks judged against an assumed guideline are weakened accordingly; failures against it are `probable` at most.
4. **Step 3: choose a method per criterion and plan the data.**
   - Method per criterion, and mixing is allowed (a cheap classifier on all data plus an expensive judge on a small sample). `[C04-013]` Exact methods are covered in `run-checks.md`; an AI judge result obeys the cap in `evidence-and-confidence.md`. Use logprobs where available for confidence. `[C04-013]` Human evaluation is acceptable, even in production. `[C04-013]`
   - Data: prefer real production data; natural labels if available, else human or AI labels. Cover every component and criterion. `[C04-013]`
   - Slices: plan separate sets or slices by tier, traffic source, input length or topic, a set where the system often errs, a set where users often err (typos), and an out-of-scope set. `[C04-013]` Slicing guards against Simpson's paradox, where an aggregate hides a reversal across subsets. `[C04-013]`
   - Size: large enough to be reliable and small enough to afford. Bootstrap a set of about 100: resample with replacement and repeat; wide swings mean the set is too small. `[C04-013]` To tell whether a change is better with 95% confidence the book's rough guide is a difference of 30% needing about 10 samples, 10% about 100, 3% about 1,000, 1% about 10,000. `[C04-013]` If the project's eval set is smaller than the guide implies, say what difference it can and cannot detect. For scale, the book cites a benchmark-organizer view that 300 examples is the absolute minimum and at least 1,000 is preferred. `[C04-013]`
5. **Plan checks on the evaluation pipeline itself** when the project has one: does it give the right signals, is it reproducible (run twice, compare; judge temperature at 0), are metrics redundant or uncorrelated, what cost and latency does it add. `[C04-013]`
6. **Convert candidate checks into cases.** One row per case with ID `T<n>`, what is checked, how, criterion (module id and PDF page from the module), evidence, type. Type `run` means executed through `scripts/run_check.py`; type `review` means code or config read and ends as `REVIEWED`. No book basis: mark `supplementary` in the plan and set `"supplementary": true` on that case in `results.json` (the validator then accepts empty `criteria_refs`; otherwise empty `criteria_refs` is a problem). `[C04-011]`
7. **List what cannot be run** with the reason and the manual step that would cover it (no endpoint, no data, no spend approval, missing tool). Each becomes `NOT_RUN` or `BLOCKED` later (skill rule, not from the book).
8. **State spend and safety.** Spend cap for model calls (or "none; no model calls"); production read-only; no secrets copied; attack probes only against the user's own system.
9. **Present for approval.** Show the filled plan. Wait for explicit approval before step 6 of SKILL.md. Changes to the plan after approval are re-shown.

## Checks
| check | what is checked | how | evidence produced | type | criterion | how a failure is judged |
|---|---|---|---|---|---|---|
| TP-01 | Plan covers each inventory component class present, or marks it not applicable | compare plan rows with the inventory | notes | review | C04-011 | uncovered component: add a case or list under "Cannot be run" |
| TP-02 | Every case has criterion, evidence and type; `run` cases name the exact command | read the plan | notes | review | C04-011 | missing fields: fix before approval |
| TP-03 | Guideline (criteria, rubric, usefulness threshold) exists and is stated as project fact or assumption | read project docs; draft if absent | guideline text | review | C04-012 | absent: label dependent failures `probable` at most |
| TP-04 | Eval data covers slices and out-of-scope inputs; size is justified | count examples in the project eval data with a command through `run_check.py`; read the slice definitions | exec record | run | C04-013 | set below the guide for the claimed difference: `risk` |
| TP-05 | Existing evaluation is more than eyeballing | read eval folders, golden sets, metrics code | notes | review | C03-002 | only ad hoc prompts: `risk` |

## Evidence and exit gate
Template sections are all filled: Scope, Assumptions, Cases, Cannot be run, Evidence and confidence rules, Exit criteria. The user has approved, and their words are recorded. No check was run before approval. Approval does not extend to paid calls beyond the stated cap.

## Outputs
`../../templates/test-plan.md` filled; the approved case list is the seed of `results.json` (each case starts `NOT_RUN`, which needs a `reason` such as "not yet run" until it is executed) used in `run-checks.md`.

## Pitfalls
- Planning only an end-to-end check, so a failure cannot be localised to a stage. `[C04-011]`
- Scoring only per turn when the user's real question is task completion. `[C04-011]`
- Vague guidelines producing vague scores. `[C04-012]`
- Reading a high aggregate score as proof while a slice is failing. `[C04-013]`
- A tiny eval set presented as proof of a small improvement. `[C04-013]`
- Letting an assumed guideline harden into a confirmed defect. `[C04-012]`
- Treating an ad hoc prompt list as an evaluation set. `[C03-002]`
