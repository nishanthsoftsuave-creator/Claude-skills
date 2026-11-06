---
name: system-understanding
mode: review-test
rows: [C01-020, C01-021, C01-022, C10-003, C10-009, C06-003, C06-008]
---
# System understanding: build the component inventory

## When to use
First Review & Test workflow, right after discovery (`../discovery.md`) and routing. Its output, the component inventory, is the input to `review-checklist.md`, `test-plan.md` and every component-specific review workflow. Skip it only for a plain question about the book.

## Inputs needed
- The discovery context summary (facts with source files, assumptions, unknowns, AI components found). Do not re-scan the whole project; read only the files needed to fill an inventory row. Ask the user only for what discovery could not answer (`../architect/intake.md`).
- If discovery found no AI components, stop: report that little of the book applies and why (the rule in `../discovery.md`).
- Never open secret files or copy credential values into the inventory.

## Modules to load
| Row | Module | Why it is needed here |
|---|---|---|
| C01-020 | [Three Layers of the AI Stack](../../core/ai-engineering-building-applications-with-foundation-models/ch01-intro/p093-three-layers-of-the-ai-stack.md) | Layer model used to place each component |
| C01-021 | [AI Engineering Versus ML Engineering](../../core/ai-engineering-building-applications-with-foundation-models/ch01-intro/p097-ai-engineering-versus-ml-engineering.md) | Adaptation method (prompt-based or finetuned) and model-development vs application-development parts |
| C01-022 | [AI Engineering Versus Full-Stack Engineering](../../core/ai-engineering-building-applications-with-foundation-models/ch01-intro/p112-ai-engineering-versus-full-stack-engineering.md) | Interface and product code is part of the system under review |
| C10-003 | [Step 1. Enhance Context](../../core/ai-engineering-building-applications-with-foundation-models/ch10-architecture-feedback/p854-step-1-enhance-context.md) | Context construction by retrieval and tools; provider and framework limits |
| C10-009 | [AI Pipeline Orchestration](../../core/ai-engineering-building-applications-with-foundation-models/ch10-architecture-feedback/p890-ai-pipeline-orchestration.md) | Components definition and chaining; finds the orchestrator and the chain |
| C06-003 | [RAG Architecture](../../core/ai-engineering-building-applications-with-foundation-models/ch06-rag-agents-memory/p498-rag-architecture.md) | Retriever, generator, indexing, querying, chunking |
| C06-008 | [Agent Overview](../../core/ai-engineering-building-applications-with-foundation-models/ch06-rag-agents-memory/p536-agent-overview.md) | Agent = environment + actions + tools |

## Procedure
1. **Place every component in a layer.** Assign each item found by discovery to one of three layers: application development (prompts, context construction, evaluation, AI interface), model development (modeling and training, finetuning, dataset engineering, inference optimization, evaluation), infrastructure (compute management, data management, serving, monitoring). `[C01-020]` A component that fits no layer, or a layer with nothing in it (for example no monitoring), is recorded as a gap, not skipped. INTERPRETATION: use the layers to locate where a later problem lives (interface and prompts, model or data, serving and monitoring), as the module suggests. `[C01-020]`
2. **Record the model and how it is adapted.** For each model: provider or self-hosted, the exact model identifier string, and the adaptation used. Prompt-based adaptation leaves weights untouched; finetuning changes them. `[C01-021]` Do not call prompt changes "training" or "finetuning" in the inventory; record what the code actually does. `[C01-021]` If weights were finetuned, list the training data source so `data-review.md` can pick it up. INTERPRETATION: a model identifier with no pinned version is recorded as a fact worth checking later (the review checklist covers silent model changes).
3. **Inventory prompts.** For each prompt: where it lives, whether it is split into system prompt and user prompt, who can edit it, and whether it is versioned (INTERPRETATION: inventory fields, not book content; prompt engineering is the prompt-based, weights-untouched way of adapting a model `[C01-021]`). Record how the final model input is built (chat template or application prompt template) if the code builds it itself; `prompt-review.md` checks it.
4. **Inventory context construction.** List each mechanism that builds the model's context: text, image or tabular retrieval, and tools that call APIs (web search, news, weather and the like). `[C10-003]` For each note the provider or framework limits that bear on this system: document types and counts, retrieval algorithm and chunk-size settings, supported tool-execution modes (parallel, long-running). `[C10-003]`
5. **If there is retrieval, map the RAG parts.** Name the retriever and the generator, the external memory (documents, tables, chat history), how indexing is done, how querying is done, and the chunking. `[C06-003]` Note whether retriever and generator were finetuned together or separately; many systems use off-the-shelf parts. `[C06-003]` Route retrieval-quality questions to `retrieval-review.md`; the book says RAG success hinges on retriever quality. `[C06-003]`
6. **If there is an agent, map environment, actions and tools.** An agent is characterized by the environment it works in and the actions it can perform; tools extend those actions. `[C06-008]` Record the environment (repo, internet, database) and each tool `[C06-008]`; INTERPRETATION: also record each tool's parameters, the planner or loop, the stopping condition, memory and any write actions. A RAG system that executes SQL or uses retrievers as tools is an agent in the book's sense; record it under both headings and let the checklist decide depth. `[C06-008]` Count the steps a typical task takes, since accuracy compounds down with step count (95% per step is about 60% after 10 steps). `[C06-008]`
7. **Map the pipeline and orchestrator.** Find how components are wired: components definition (models, data sources, tools, evaluation and monitoring tools) and chaining (the steps from user query to completion). `[C10-009]` Write the chain as ordered steps, marking where the response is evaluated and where a human fallback exists. `[C10-009]` Record the orchestration tool if any (the book names LangChain, LlamaIndex, Flowise, Langflow and Haystack as examples; time-sensitive) and whether it hides API calls or adds latency. `[C10-009]` Note steps that run in parallel. `[C10-009]` A general workflow orchestrator such as Airflow or Metaflow is a different thing from an AI pipeline orchestrator; do not conflate them. `[C10-009]`
8. **Include the interface and product code.** The AI interface (web, desktop or mobile app, extension, chat integration, API) and the surrounding application are part of the system; list them with language and framework. `[C01-022]` `[C01-021]` Do not assume one language: JavaScript support in AI tooling is growing alongside Python. `[C01-022]`
9. **Record data and evaluation assets.** Datasets, ingestion code, anything holding user data or PII, existing eval sets, test folders, judge-model calls. Discovery supplies them; add location and owner only. They feed `data-review.md` and `eval-execution.md`.
10. **Mark safeguards and operations found.** Input or output guardrails, caching, routing or gateway, logging, tracing, cost tracking, CI. Note presence or absence and where; judging them is `review-checklist.md`'s job.
11. **Show the inventory to the user** as one table and let them correct it. Record corrections as facts; keep unconfirmed rows as assumptions.

## Inventory format
| ID | Component | Class | Layer | Where (file or endpoint) | Model or tool | Notes and unknowns | Source |
|---|---|---|---|---|---|---|---|
| K1 | support answer prompt | prompt | application | path | model id | versioned? | file seen |

Class values (used by `review-checklist.md`): model, prompt, context-construction, retrieval, agent-tool, memory, data, pipeline-orchestration, guardrail, cache-or-router, evaluation, monitoring, interface, infrastructure. Every row needs a Source (a file or command output); a row without one is an assumption and is labelled so.

## Evidence and exit gate
- Every inventory row cites a file or command output seen in this run. Anything inferred is marked assumption.
- Every discovered AI component has a class and a layer; absent layers or safeguards are listed separately as gaps.
- The user has seen the inventory and corrections are recorded (in a non-interactive session, the inventory is listed as assumptions).

## Outputs
The component inventory, the gap list and the updated unknowns. These feed the scope and assumptions of the test plan (`../../templates/test-plan.md`, filled via `test-plan.md`). Nothing here is a finding.

## Pitfalls
- INTERPRETATION: treating a framework name as proof of a capability; record what the code calls, not what the library can do (the book warns orchestrators can hide behaviour `[C10-009]`).
- Missing the hidden agent: RAG with tools or SQL execution behaves as an agent. `[C06-008]`
- Forgetting the interface and glue code because "the AI part" is elsewhere. `[C01-022]`
- Mixing up finetuning with prompt engineering when recording the adaptation. `[C01-021]`
- Assuming a provider or framework supports the data volume, file types or tool-execution mode in use without checking. `[C10-003]`
- Reading the layers too literally: evaluation appears in two layers, so one component may serve both. `[C01-020]`
