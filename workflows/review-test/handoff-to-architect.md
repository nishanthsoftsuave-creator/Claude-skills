---
name: handoff-to-architect
mode: review-test
rows: [C01-017, C04-008, C04-009]
---
# Handoff to Architect mode

## When to use
After the report is written (or while drafting it) and the user wants to act on the findings with a redesign, a model change or a rebuild. This workflow converts confirmed and probable findings into inputs for Architect mode. It does not redesign anything itself, and it offers the handoff rather than starting it without the user's approval.

## Inputs needed
- `results.json` with findings and labels; the findings report.
- The discovery context summary (components, hosting, models) and the user's goals and constraints. Ask only what these do not answer, using `../architect/intake.md`.

## Modules to load
| Row | Module | Why it is needed here |
|---|---|---|
| C01-017 | [Milestone Planning](../../core/ai-engineering-building-applications-with-foundation-models/ch01-intro/p086-milestone-planning.md) | baseline from existing models, goals shifting after evaluation, the last-mile effort |
| C04-008 | [Model Selection Workflow](../../core/ai-engineering-building-applications-with-foundation-models/ch04-eval-systems/p356-model-selection-workflow.md) | hard vs soft attributes and the four-step selection loop |
| C04-009 | [Model Build Versus Buy](../../core/ai-engineering-building-applications-with-foundation-models/ch04-eval-systems/p359-model-build-versus-buy.md) | the seven axes for API versus self-hosting |

## Procedure
1. **Select what is eligible.** Take `confirmed` and `probable` findings. Carry `risk` items only as constraints for the design. Leave `unverified` items out, except as open questions the design must resolve; never promote a finding's label for the handoff.
2. **Group findings by the decision they imply.** One finding may imply several. Use the table; every mapping to an Architect workflow is INTERPRETATION (the book does not map review findings to workflows); a row id marks the book idea behind the decision, not the mapping.

   | Finding type | Architect decision it feeds | Architect workflow to run |
   |---|---|---|
   | Model too weak, slow or costly for the target; model quirks after a swap | model selection: re-run the hard/soft filter and the cost-quality map `[C04-008]` | `architect/model-selection.md` |
   | API cost, privacy, control or lock-in concerns; scale changed | build vs buy, per the seven axes `[C04-009]` | `architect/model-selection.md` |
   | Prompt-only approach cannot reach quality; knowledge missing | solution pattern: prompt, RAG, agent or finetune | `architect/solution-pattern.md`, `architect/finetune-decision.md` |
   | Format failures, inconsistency | sampling and structured-output design | `architect/structured-outputs-and-sampling.md` |
   | Poor retrieval, stale or low-quality data | data and retrieval design | `architect/data-and-retrieval.md` |
   | Agent failures, tool misuse | agent and tool design | `architect/agents-and-tools.md` |
   | Prompt quality, context length or position problems | prompt and context design within the solution pattern | `architect/solution-pattern.md` |
   | Prompt-attack, guardrail or data-exposure findings | guardrails and defenses in the architecture | `architect/architecture-design.md` |
   | Poor finetuning or evaluation data | dataset and finetune planning | `architect/finetune-plan.md`, `architect/data-and-retrieval.md` |
   | Latency, throughput or cost over target | inference and cost plan | `architect/inference-plan.md`, `architect/ops-cost-feedback.md` |
   | No eval set, weak or judge-only measurement | evaluation plan | `architect/eval-plan.md` |
   | Missing monitoring or feedback | operations and feedback design | `architect/ops-cost-feedback.md` |
   | Overall structure unclear, many issues across layers | full design run, in the order routing.md lists | `architect/use-case-and-requirements.md` first, ending at `architect/design-review-gate.md` |

3. **Decide whether the model decision is open.** Use the hard/soft split: a hard attribute (license, privacy policy, provider-hosted latency) cannot be changed and filters candidates; a soft attribute (accuracy, factual consistency, self-hosted latency) can be improved, so estimate the achievable improvement realistically before dropping a model `[C04-008]`. If a finding blames the model, first check whether a soft attribute was fixable by prompt, data or inference work; the book reports both a jump from 20% to 70% accuracy after splitting a task and a model that stayed unusable after weeks of tweaking `[C04-008]`. The selection loop is: filter by hard attributes, narrow with public benchmarks, test with your own evaluation, then monitor in production; later steps can overturn earlier ones `[C04-008]`.
4. **Frame build vs buy as a checklist, not a verdict.** For each finding that questions the current provider or hosting, list the seven axes with the project's facts: data privacy, data lineage and copyright, performance, functionality (scalability, function calling, structured outputs, guardrails, logprobs), API cost versus engineering cost, control, access and transparency, on-device needs `[C04-009]`. Strict privacy or cross-border data rules and on-device needs rule out external APIs; need for logprobs, finetuning or fine control favors open models; need for the strongest model and ready-made functionality favors commercial APIs `[C04-009]`. Also pass the license questions for any open model: commercial use, restrictions, whether outputs may train other models `[C04-009]`. Revisit the answer when scale or prices change `[C04-009]`.
5. **Turn findings into milestones.** The first planning step is to evaluate existing models to see what they already do; the remaining gap sets the work `[C01-017]`. Pass the review's measured baseline (pass rates, latency, cost) as the starting point and the target as the goal. If the gap to the usefulness threshold costs more than the expected return, tell the user the project may not be worth pursuing `[C01-017]`. Plan the long tail separately: the book reports that going from a good demo to a product is slow (LinkedIn: 80% in a month, then four more months to pass 95%) `[C01-017]`; do not extrapolate review progress to a delivery date.
6. **Write the handoff note** (a section appended to the report, or a separate file in the run folder), per decision:
   - Source findings (ids, labels, evidence paths) and the criterion rows behind them.
   - The question for Architect: current state, target, constraints, hard attributes known.
   - Baseline numbers and what is unmeasured.
   - Assumptions and unknowns the design must resolve.
   - Time-sensitive items (model names, prices, benchmarks) flagged as dated.
7. **Offer the next step.** Name the first Architect workflow to run, and wait for the user's approval. Starting the Architect run is a new plan with its own approval; no code, config or provider changes are made during the handoff.

## Evidence and exit gate
- Every handoff item traces to a finding id with its label and evidence; no item rests on an `unverified` finding.
- The workflow to run next is named, and the open decisions and unknowns are listed.
- The user has been offered, not committed to, the redesign.

## Outputs
A handoff section (or file) in the run folder; no template beyond the report. The Architect run then uses `../../templates/decision-record.md` for each choice.

## Pitfalls
- Promoting a `probable` or judge-only finding to a requirement as if confirmed.
- Concluding "switch model" or "self-host" from one failure without the seven-axis check `[C04-009]`.
- Dropping a model on a soft attribute without estimating how much it can improve `[C04-008]`.
- Forgetting that earlier steps can be overturned by later evidence, for example open models failing the private evaluation and pushing the choice to APIs `[C04-008]`.
- Treating demo-level results as a delivery estimate `[C01-017]`.
- Presenting dated licensing terms, prices or chip figures from the modules as current `[C04-009]`.
