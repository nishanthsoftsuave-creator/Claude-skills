# Routing: from the request to workflows and modules

After discovery and intake, find the request below, run the listed workflows in order, and load only the `core/` modules those workflows name (each workflow has a "Modules to load" table). If a request spans several rows, take the union and keep the order. Routing decides what to read now; nothing in the book is excluded. Workflows are under `architect/` and `review-test/` in this folder; names below are file names without `.md`.

## Always

- `discovery` first, then `architect/intake` (ask only what is still missing).
- Any Review & Test run that produces findings ends with `review-test/evidence-and-confidence` (labels and caps) and `review-test/report`.
- Anything the skill labels INTERPRETATION or SUPPLEMENTARY is its own adaptation, not the book's; say so in the output.

## Architect mode (design something new)

| The user wants | Workflows, in order |
|---|---|
| A full design for a new AI application or feature | `use-case-and-requirements`, `model-selection`, `solution-pattern`, then only the ones the chosen pattern needs: `structured-outputs-and-sampling`, `data-and-retrieval`, `agents-and-tools`, `finetune-decision` (then `finetune-plan`), `inference-plan`; then `architecture-design`, `eval-plan`, `ops-cost-feedback`, `design-review-gate` |
| Prompting vs RAG vs agent vs finetuning | `solution-pattern`, then `finetune-decision` (and `data-and-retrieval` if retrieval wins) |
| A model choice, or build vs buy | `model-selection`, then `eval-plan` for the comparison criteria |
| Feasibility or planning of finetuning | `finetune-decision`; if it goes ahead, `finetune-plan` |
| A RAG system | `data-and-retrieval`, with `structured-outputs-and-sampling` if outputs must be structured |
| An agent | `agents-and-tools`, then `architecture-design` (guardrails, orchestration) |
| An evaluation plan before building | `eval-plan` |
| Inference cost, latency or hardware planning before a system exists | `inference-plan`, then `ops-cost-feedback` |
| Monitoring, feedback and maintenance planning | `ops-cost-feedback` |
| A final check before handing over a design | `design-review-gate` |

## Review & Test mode (inspect and test something that exists)

| The user wants | Workflows, in order |
|---|---|
| A full review and test of an AI system, or "are we ready to launch" | `system-understanding`, `review-checklist`, `test-plan` (approval gate), `run-checks`, then the review workflows the checklist routes to, then `evidence-and-confidence`, `report` |
| Prompts reviewed | `prompt-review`, plus `security-and-prompt-attacks` for exposure |
| A RAG or retrieval system reviewed | `retrieval-review`, plus `data-review` for what feeds the index |
| An agent reviewed for failure modes | `agent-review` (with `failure-diagnosis` only if a specific failure is reported; `security-and-prompt-attacks` for abuse) |
| Datasets reviewed (finetuning, retrieval or evaluation data) | `data-review` |
| Output quality measured, or an existing evaluation audited | `eval-execution` |
| Prompt-attack and guardrail testing | `security-and-prompt-attacks` (needs approval and a non-production target) |
| Performance, cost or latency of a running system | `perf-cost-latency` |
| Monitoring and observability reviewed | `observability-review` |
| User-feedback collection and use reviewed | `feedback-review` |
| A reported failure (hallucination, inconsistency, wrong format, bad retrieval, agent loop, regression, cost spike) | `failure-diagnosis`, which hands off to `retrieval-review`, `data-review`, `agent-review`, `prompt-review`, `observability-review` or `eval-execution` as the evidence points; then `evidence-and-confidence` |
| Turning review findings into a redesign | `handoff-to-architect`, then the Architect workflows it names |

## A plain question about the book or a concept

No mode ceremony. Look the term up in `../core/ai-engineering-building-applications-with-foundation-models/front-back-matter/p932-index.md` (the book's own Index mapped to modules), `../core/ai-engineering-building-applications-with-foundation-models/concepts.md` (by concept) or `../core/ai-engineering-building-applications-with-foundation-models/index.md` (by chapter), read that module, answer, and cite its row id and PDF pages. Say when a statement is time-sensitive, and read the matrix `gaps` entry (`../coverage/known-gaps.md`) before relying on a section that has one.

## When nothing fits

- No AI components in the project: say little of the book applies and why; offer the one or two relevant checks (for example evaluation of whatever AI features are planned), do not force the rest.
- A request outside what the book covers: say so, label any answer SUPPLEMENTARY, and name the source.
- Not enough evidence to route: ask the single question that decides it.
