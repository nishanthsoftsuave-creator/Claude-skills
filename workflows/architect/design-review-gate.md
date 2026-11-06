---
name: design-review-gate
mode: architect
rows: [C01-016, C01-017, C04-011, C04-012, C05-018, C10-004]
---
# Design review gate

## When to use
The last step of Architect mode, before the architecture design, decision records and eval plan are handed to the user. It checks the design; it does not design. Items G1-G11 each tie to a module; G12-G15 are gate-level checks with no book basis of their own (labelled so in the Source column). A failed item goes back to the workflow that owns it, and the gate is re-run on the changed parts.

## Inputs needed
The filled `../../templates/architecture-design.md`, the decision records, `../../templates/eval-plan.md`, and the intake answers and assumptions (run state). Nothing new is asked of the user unless an item fails for lack of a fact.

## Modules to load
| Row | Module | Why it is needed here |
|---|---|---|
| C01-016 | [Setting Expectations](../../core/ai-engineering-building-applications-with-foundation-models/ch01-intro/p085-setting-expectations.md) | Business metrics and usefulness threshold |
| C01-017 | [Milestone Planning](../../core/ai-engineering-building-applications-with-foundation-models/ch01-intro/p086-milestone-planning.md) | Baseline first, last-mile effort |
| C04-011 | [Step 1. Evaluate All Components in a System](../../core/ai-engineering-building-applications-with-foundation-models/ch04-eval-systems/p393-step-1-evaluate-all-components-in-a-system.md) | Every component and level is evaluated |
| C04-012 | [Step 2. Create an Evaluation Guideline](../../core/ai-engineering-building-applications-with-foundation-models/ch04-eval-systems/p396-step-2-create-an-evaluation-guideline.md) | Guideline, rubric, business mapping |
| C05-018 | [Defenses Against Prompt Attacks](../../core/ai-engineering-building-applications-with-foundation-models/ch05-prompting/p483-defenses-against-prompt-attacks.md) | Defense levels and robustness metrics |
| C10-004 | [Step 2. Put in Guardrails](../../core/ai-engineering-building-applications-with-foundation-models/ch10-architecture-feedback/p856-step-2-put-in-guardrails.md) | Input and output guardrail coverage |

## Procedure
Run each item. Record `pass`, `fail` or `waived with reason` (the user may waive; the skill may not). Do not mark pass on a claim the design only asserts; the design must show where it is written.

| # | Check | Pass when | On fail | Source |
|---|---|---|---|---|
| G1 | Business metrics | Goal states business impact (for a support bot, share automated, volume handled, speed, labour saved) and customer satisfaction or feedback is tracked too | Return to `use-case-and-requirements.md`; add the missing metric | `[C01-016]` |
| G2 | Usefulness threshold | A minimum quality, latency (TTFT, TPOT, total) and cost per request exists below which the product is not shipped, each with its origin (other metrics such as interpretability and fairness can be added; acceptable latency depends on the use case, for example the human median it replaces) | Return to `eval-plan.md` and `inference-plan.md`; write the threshold or mark the gap as an open risk | `[C01-016]`, `[C04-012]` |
| G3 | Baseline first | Plan starts from an evaluation of existing or off-the-shelf models and states the gap to the threshold; if the gap costs more than the return, the design says "do not build" | Add a baseline milestone; if gap unknown, make baseline the first milestone | `[C01-017]` |
| G4 | Last mile | Milestones budget the long tail separately from demo speed (the book: 80% in a month, beyond 95% four more months) | Re-plan milestones; add buffer and a check per milestone | `[C01-017]` |
| G5 | Component coverage | Eval plan names every component (retrieval, router, guardrail, generation, each tool) and system level, per turn and per task | Return to `eval-plan.md` step 1 | `[C04-011]` |
| G6 | Guideline | Criteria come from real test queries; rubrics have scored examples validated by humans; out-of-scope behaviour is defined; metric levels map to business outcomes | Return to `eval-plan.md` step 2; do not hand over a plan with a "TBD" rubric | `[C04-012]` |
| G7 | Guardrail coverage | Input side (sensitive data to external APIs, bad prompts) and output side (format, factuality, safety, PII, execution, brand) each have a detection and a handling policy (mask or block sensitive input; retry, human or block on output). With a self-hosted model many input guardrails fall away | Return to `architecture-design.md` steps 4-5 | `[C10-004]` |
| G8 | Guardrail trade-offs | Latency cost of guardrails and streaming vs full-response checks is decided and written; false refusal rate is tracked beside violations | Return to `architecture-design.md` step 7; add the metric to `ops-cost-feedback.md` | `[C10-004]`, `[C05-018]` |
| G9 | Attack exposure | Design lists which attack families apply (direct, automated, indirect injection through each tool or data source, extraction; the families are in the attack modules cited by `architecture-design.md` step 3, which cites the attack modules) and a defense at model, prompt or system level for each | Return to `architecture-design.md` step 3 and 6 | `[C05-018]` |
| G10 | Robustness metrics | Violation rate and false refusal rate are in the eval plan, with a way to generate attacks (benchmarks, probing tools, red team) | Add to `eval-plan.md`; if no attack source, list as an open item | `[C05-018]` |
| G11 | Impactful actions | Every write or code-executing action has human approval or isolation; residual risk is stated | Return to `architecture-design.md` step 10 | `[C05-018]` |
| G12 | Cost and latency levers | Targets have named levers tied to a bottleneck (see `inference-plan.md`) and caches exclude user-specific data | Return to `inference-plan.md` | Gate-level check, no book basis (INTERPRETATION) |
| G13 | Operations | Monitoring metrics, logs, traces, drift checks and feedback design exist (see `ops-cost-feedback.md`) | Return to `ops-cost-feedback.md` | Gate-level check, no book basis; content owned by that workflow |
| G14 | Traceability | Every design choice has a decision record citing a module; book claims are labelled BOOK / INTERPRETATION / SUPPLEMENTARY; time-sensitive figures are flagged | Add records and labels | Gate-level check, no book basis (SKILL.md labelling rule) |
| G15 | Honest gaps | Assumptions, unknowns and `UNVERIFIED` items are listed at the top of the output with what would resolve each | Add them; never delete a gap to look complete | Gate-level check, no book basis (SKILL.md evidence rule) |

Order of work: G1-G4 (is it worth building), G5-G6 (can we tell if it works), G7-G11 (is it safe), G12-G15 (is it operable and honest).

When an item fails twice after rework, stop looping: present the item as an open risk with the question that would settle it, and let the user decide. Conflicts between items (for example guardrails versus latency target) go to the user with both costs, not resolved silently `[C10-004]`.

## Evidence and exit gate
Exit when no item is `fail`. Each `pass` points to a section or record in the design; each `waived` item carries the user's words. Write the gate result (table, one line per item) at the end of the architecture design, in section 6 (risks and open questions). Then update run state and move to the report step.

## Outputs
A completed gate table appended to `../../templates/architecture-design.md`; reworked sections in the same template; updated `../../templates/decision-record.md` files; the final `../../templates/eval-plan.md`.

## Pitfalls
- Passing G1-G2 because the goal sounds measurable; no number means fail `[C01-016]`.
- Skipping the baseline because a demo already works `[C01-017]`.
- A guideline with undefined "good", so scores differ between reviewers `[C04-012]`.
- Evaluating only the final answer and missing which component failed `[C04-011]`.
- Declaring guardrails complete on the input side only; harmless input can still yield harmful output `[C05-018]`.
- Treating residual prompt-attack risk as zero while the system can act `[C05-018]`.
- Over-strict guardrails measured only by violation rate `[C10-004]`.
