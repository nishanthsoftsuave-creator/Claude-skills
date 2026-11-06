---
name: review-checklist
mode: review-test
rows: [C01-015, C01-018, C02-015, C04-003, C04-004, C04-005, C04-006, C05-004, C06-011, C08-003, C10-004, C10-008]
---
# Master review checklist

## When to use
After `system-understanding.md` has produced the component inventory and before `test-plan.md`. It does two jobs: (1) routes each component class to the review workflow that owns it, and (2) carries the cross-cutting checks that no single component workflow owns (use-case fit, change management, non-determinism, the four evaluation criteria buckets, cost and latency, guardrails, monitoring). Its output is a list of candidate checks the test plan turns into cases.

## Inputs needed
- The component inventory and gap list from `system-understanding.md`.
- Anything the user said about known incidents, success criteria and constraints (`../architect/intake.md`).
- Which checks can run: commands, test suites, endpoints, sample inputs, eval data, spend cap. Unknown access is recorded as an assumption; it decides which candidate checks later become `NOT_RUN`.

## Modules to load
| Row | Module | Why it is needed here |
|---|---|---|
| C01-015 | [Use Case Evaluation](../../core/ai-engineering-building-applications-with-foundation-models/ch01-intro/p079-use-case-evaluation.md) | Role of AI and humans in the product |
| C01-018 | [Maintenance](../../core/ai-engineering-building-applications-with-foundation-models/ch01-intro/p088-maintenance.md) | Change management: model swaps, versioning, regulation, IP |
| C02-015 | [The Probabilistic Nature of AI](../../core/ai-engineering-building-applications-with-foundation-models/ch02-foundation-models/p214-the-probabilistic-nature-of-ai.md) | Inconsistency and hallucination mitigations |
| C04-003 | [Domain-Specific Capability](../../core/ai-engineering-building-applications-with-foundation-models/ch04-eval-systems/p319-domain-specific-capability.md) | Four criteria buckets; benchmarks and baselines |
| C04-004 | [Generation Capability](../../core/ai-engineering-building-applications-with-foundation-models/ch04-eval-systems/p324-generation-capability.md) | Factual consistency and safety |
| C04-005 | [Instruction-Following Capability](../../core/ai-engineering-building-applications-with-foundation-models/ch04-eval-systems/p339-instruction-following-capability.md) | Format and constraint adherence |
| C04-006 | [Cost and Latency](../../core/ai-engineering-building-applications-with-foundation-models/ch04-eval-systems/p351-cost-and-latency.md) | Hard requirements vs nice-to-have |
| C05-004 | [System Prompt and User Prompt](../../core/ai-engineering-building-applications-with-foundation-models/ch05-prompting/p423-system-prompt-and-user-prompt.md) | Chat template and silent failures |
| C06-011 | [Agent Failure Modes and Evaluation](../../core/ai-engineering-building-applications-with-foundation-models/ch06-rag-agents-memory/p576-agent-failure-modes-and-evaluation.md) | Planning, tool and efficiency failures |
| C08-003 | [Data Quality](../../core/ai-engineering-building-applications-with-foundation-models/ch08-datasets/p704-data-quality.md) | Six data-quality characteristics |
| C10-004 | [Step 2. Put in Guardrails](../../core/ai-engineering-building-applications-with-foundation-models/ch10-architecture-feedback/p856-step-2-put-in-guardrails.md) | Input and output guardrails |
| C10-008 | [Monitoring and Observability](../../core/ai-engineering-building-applications-with-foundation-models/ch10-architecture-feedback/p877-monitoring-and-observability.md) | Logs, traces, metrics, drift |

## Procedure
1. **Route by component class.** For each class present in the inventory, add the owning workflow to the plan. Classes absent from the system are skipped and recorded as "not applicable".

| Component class | Owning workflow | Top checks (details in that workflow) |
|---|---|---|
| prompt | `prompt-review.md` | final prompt matches the model's chat template, prompts versioned `[C05-004]` |
| prompt, interface (attack surface) | `security-and-prompt-attacks.md` | own-system probes only; guardrail coverage `[C10-004]` |
| context-construction, retrieval | `retrieval-review.md`, `data-review.md` | retriever quality, chunking, factual consistency with context `[C04-004]` |
| agent-tool, memory | `agent-review.md` | tool validity, planning and efficiency failures `[C06-011]` |
| data | `data-review.md` | six quality characteristics `[C08-003]` |
| model, infrastructure | `perf-cost-latency.md` | cost and latency against stated requirements `[C04-006]` |
| pipeline-orchestration, cache-or-router | `observability-review.md`, `perf-cost-latency.md` | chain and orchestrator visibility, caches, routing cost and latency (rows in those workflows) |
| evaluation | `eval-execution.md` | eval set, criteria and method fit `[C04-003]` `[C04-004]` `[C04-005]` |
| monitoring | `observability-review.md` | logs, traces, drift, alerting `[C10-008]` |
| guardrail | `security-and-prompt-attacks.md` | input and output guardrail coverage, false refusals `[C10-004]` |
| feedback signals or UI (any class that collects user feedback) | `feedback-review.md` | signals, collection design, bias and loops (rows in that workflow) |
| a reported failure | `failure-diagnosis.md` | reproduce first, then isolate the component |

2. **Apply the cross-cutting checks below** to the whole system. Each becomes a candidate case.
3. **Rank by exposure.** Order checks by the cost of a wrong answer, using the role of AI in the product: the more critical AI is, the more accurate and reliable it must be; a proactive feature faces a higher quality bar than a reactive one. `[C01-015]`
   Also weigh change exposure: the field moves fast, a model swap needs adjusted prompts and data and is painful without versioning and evaluation infrastructure, regulation and IP rules can shift, and build-versus-buy conclusions go stale. `[C01-018]`
4. **Mark what cannot be run** (no access, no data, no spend approval) so the test plan lists it under "Cannot be run".
5. **Hand over** the candidate-check list to `test-plan.md`.

## Checks
| check | what is checked | how | evidence produced | type | criterion | how a failure is judged |
|---|---|---|---|---|---|---|
| RC-01 | Role of AI is stated: critical or complementary, reactive or proactive, and what humans do (review, fallback, none) | read README, product docs, UI code; ask the user if absent | notes with file refs | review | C01-015 | AI is critical or proactive and no human fallback or quality bar is stated: `risk` |
| RC-02 | Model identifiers are pinned and recorded, and a model swap can be tested (versioned prompts, eval set to re-run) | read config and CI; search for model-name strings and prompt versioning | notes | review | C01-018 | unpinned model plus no re-runnable eval: `risk` (a provider can change the model behind an unchanged API, which the book lists as a drift source `[C10-008]`) |
| RC-03 | Build-versus-buy and provider assumptions are dated and revisited; regulation and IP exposure are acknowledged | read docs and ADRs | notes | review | C01-018 | no record at all: `recommendation` only |
| RC-04 | Non-determinism handled: sampling settings fixed where repeatability matters; repeat answers cached where acceptable | read generation config; INTERPRETATION: if endpoint access and approval exist, send one input several times via `run_check.py` and compare; paid calls need approval and the spend cap | config notes; exec records | review, or run | C02-015 | differing outputs with settings already fixed is expected (hardware, provider control), so report as `risk`, not `confirmed` |
| RC-05 | Hallucination mitigation exists for fact-dependent features (grounding in context, honest "I don't know" instruction, concision, verification) | read prompts and pipeline; then `eval-execution.md` for measurement | notes | review | C02-015 | fact-dependent feature with none of these: `risk`; measured hallucination rate belongs to a run case |
| RC-06 | Evaluation criteria cover the buckets that matter: domain capability, generation capability, instruction following, cost and latency | compare the project's metrics and eval data with the four buckets | gap list | review | C04-003 | a bucket critical to the use case with no measure: `risk` |
| RC-07 | Domain capability evidenced by a domain benchmark or own eval set; multiple-choice results are compared with the random baseline and not used as the main check of generation quality | read eval code and reports | notes | review | C04-003 | only public MCQ scores cited for a generation task: `recommendation` |
| RC-08 | For fact-dependent output, factual consistency is measured (local against supplied context, global against open knowledge) | read eval code; later run via `eval-execution.md` | notes | review | C04-004 | no measure exists: `risk`; a measured failure needs a run case |
| RC-09 | Safety (toxicity, harmful or biased content) is checked on outputs | read guardrails and eval code | notes | review | C04-004 | no check on user-facing free text: `risk` |
| RC-10 | Instruction following is tested on the project's own instructions (required formats such as JSON or YAML, forbidden phrases, length) | read tests; run the project's format tests if present | exec record or notes | run if suite exists, else review | C04-005 | format break in a test run: `FAILED`; no tests: `recommendation` |
| RC-11 | Cost and latency requirements are written down, split into hard requirements and nice-to-have, with the latency metric named (for example time to first token, total query time) | read docs and monitoring config | notes | review | C04-006 | no stated requirement: `unverified`; a stated hard requirement is measured in `perf-cost-latency.md` |
| RC-12 | Where the project builds the model input itself (typically self-hosted or open-weight models), the final prompt matches the model's chat template; prompt-building code is not left to an unverified third-party tool | print the final prompt through the project's own code or a debug path; compare with the model's documented template | exec record or notes | run if printable, else review | C05-004 | mismatch: `probable`, confirmed only when behaviour change is reproduced; template errors fail silently |
| RC-13 | Agent failure modes have an owner: invalid tool, invalid parameters, wrong values, goal failure, reflection error; every tool call and its output is logged | read agent code and logs | notes | review | C06-011 | none logged: `risk`; rates are measured in `agent-review.md` |
| RC-14 | Data feeding the model (RAG corpus, finetuning set, eval set) is checked against relevance, task alignment, consistency, format, uniqueness, compliance | sample and inspect the data (read-only); do not copy PII or secrets into notes | sample notes | review | C08-003 | clear violations in the sample (duplicates, markup, PII where forbidden): `probable`; full-data claims need a run case |
| RC-15 | Guardrails: private data masked or blocked before leaving for an external API; outputs checked for format, factuality, safety; failure policy exists (retry or human fallback); false refusal rate tracked | read code and gateway config | notes | review | C10-004 | external API with user data and no input guardrail: `risk`; a probe that gets through is a run case in `security-and-prompt-attacks.md` |
| RC-16 | Observability: logs include configuration, final prompt, outputs, tool calls; traces link a request across steps; drift (prompt, user behaviour, underlying model) can be detected; MTTD, MTTR, CFR are known | read logging and tracing setup | notes | review | C10-008 | CFR unknown: `recommendation` to improve observability |
| RC-17 | A tested path exists to run all of the above on a schedule or per change | read CI | notes | review | SUPPLEMENTARY | SUPPLEMENTARY (no book basis; common engineering practice): `recommendation` only |

## Evidence and exit gate
- Every route and every RC check has a decision: owning workflow added, or "not applicable" with a reason.
- Every check carries its criterion row id, or is labelled SUPPLEMENTARY.
- Checks resting on reading code or configuration are typed `review` and will end as `REVIEWED`, never `PASSED`.
- Checks that need access the run lacks are listed as cannot-be-run candidates.

## Outputs
The candidate-check list (workflow routes plus RC checks), the cannot-run list and the ranking. Pass them to `test-plan.md`; fill `../../templates/test-plan.md` from them.

## Pitfalls
- Declaring a prompt or config "fine" after reading it: that is `REVIEWED`, and the template-mismatch problem fails silently. `[C05-004]`
- Reporting inconsistent outputs as a defect when sampling and hardware make exact repeatability impossible. `[C02-015]`
- Using a public multiple-choice benchmark as proof of generation quality. `[C04-003]`
- Treating "no guardrails" as a defect where the team deliberately traded them for latency; record the trade-off and the exposure instead. `[C10-004]`
- Over-strict guardrails: track false refusals as well as leaks. `[C10-004]`
- Judging efficiency of an agent against a human baseline without noting that humans and AI work differently. `[C06-011]`
- INTERPRETATION: pushing agent or RAG checks onto a system with neither; record "not applicable" instead.
