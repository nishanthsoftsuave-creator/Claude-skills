---
name: architecture-design
mode: architect
rows: [C01-020, C10-003, C10-004, C10-005, C10-006, C10-007, C10-009, C05-004, C05-016, C05-017, C05-018]
---
# Architecture design: assemble the system

## When to use
After the decisions upstream are made (`use-case-and-requirements.md`, `model-selection.md`, `solution-pattern.md`, and `inference-plan.md` for cost and latency). This workflow assembles the components and fills the architecture-design template.

## Inputs needed
Objective, cost of a wrong answer, data sensitivity, existing systems, hosting and latency target, all from intake. The chosen pattern and model. Which components the book's roadmap would add is decided here, not assumed.

## Modules to load
| Row | Module | Why it is needed here |
|---|---|---|
| C01-020 | [Three Layers of the AI Stack](../../core/ai-engineering-building-applications-with-foundation-models/ch01-intro/p093-three-layers-of-the-ai-stack.md) | Place each component in a layer; reuse of ML platform parts |
| C10-003 | [Step 1. Enhance Context](../../core/ai-engineering-building-applications-with-foundation-models/ch10-architecture-feedback/p854-step-1-enhance-context.md) | Roadmap and context construction |
| C10-004 | [Step 2. Put in Guardrails](../../core/ai-engineering-building-applications-with-foundation-models/ch10-architecture-feedback/p856-step-2-put-in-guardrails.md) | Input and output guardrails and their trade-offs |
| C10-005 | [Step 3. Add Model Router and Gateway](../../core/ai-engineering-building-applications-with-foundation-models/ch10-architecture-feedback/p863-step-3-add-model-router-and-gateway.md) | Router, gateway, fallback, access control |
| C10-006 | [Step 4. Reduce Latency with Caches](../../core/ai-engineering-building-applications-with-foundation-models/ch10-architecture-feedback/p871-step-4-reduce-latency-with-caches.md) | Exact and semantic caches, leak risk |
| C10-007 | [Step 5. Add Agent Patterns](../../core/ai-engineering-building-applications-with-foundation-models/ch10-architecture-feedback/p875-step-5-add-agent-patterns.md) | Loops, parallel flows, write actions |
| C10-009 | [AI Pipeline Orchestration](../../core/ai-engineering-building-applications-with-foundation-models/ch10-architecture-feedback/p890-ai-pipeline-orchestration.md) | Components definition, chaining, orchestrator choice |
| C05-004 | [System Prompt and User Prompt](../../core/ai-engineering-building-applications-with-foundation-models/ch05-prompting/p423-system-prompt-and-user-prompt.md) | Prompt separation, where defenses start |
| C05-016 | [Jailbreaking and Prompt Injection](../../core/ai-engineering-building-applications-with-foundation-models/ch05-prompting/p467-jailbreaking-and-prompt-injection.md) | Attack families the guardrails must face |
| C05-017 | [Information Extraction](../../core/ai-engineering-building-applications-with-foundation-models/ch05-prompting/p477-information-extraction.md) | Leakage of training data, prompt and PII |
| C05-018 | [Defenses Against Prompt Attacks](../../core/ai-engineering-building-applications-with-foundation-models/ch05-prompting/p483-defenses-against-prompt-attacks.md) | Model, prompt and system-level defenses, metrics |

## Procedure
Start from the simplest architecture (query to model to response) and add a component only when a stated need justifies it. The book's order is common in production but not mandatory `[C10-003]`. Record each addition as a decision record.

1. **Place components in the stack.** Label each as application layer (interface, prompts, context, evaluation), model layer (inference optimisation, dataset engineering, modeling and training, evaluation) or infrastructure (compute and data management, serving, monitoring) `[C01-020]`. Evaluation sits in both upper layers; classic ML principles (business-to-ML metric mapping, systematic experimentation, a production feedback loop) still apply `[C01-020]`. INTERPRETATION: use the layers to locate where a failure will be debugged and which existing ML platform parts can be reused `[C01-020]`.
2. **Enhance context.** If the model needs data it does not have, add context construction: text, image or tabular retrieval and read-only tools such as search APIs `[C10-003]`. Check the chosen provider or framework against your document count, retrieval settings (chunk size) and tool modes (parallel calls, long jobs) before relying on it `[C10-003]`. Pull the retrieval and tool design from `data-and-retrieval.md` and `agents-and-tools.md`. Put developer instructions in the system prompt and user content in the user prompt, but note the two are concatenated into one prompt through the model's chat template, so the split helps (system prompt comes first; some models are post-trained to attend to it) without being a security boundary `[C05-004]`, `[C05-016]`. Build inputs with the model's exact chat template, check any third-party tool uses it, and print the final prompt before sending; template slips fail silently `[C05-004]`.
3. **Threat-model before designing guardrails.** List what the system can reach and what an attacker could plant. Walk the attack families as a checklist `[C05-016]`: direct manual hacking (obfuscation, output-format tricks, roleplay); automated and AI-generated attacks; indirect injection through every tool, retrieved document, email or database field the model reads; and extraction of training data, private context or copyrighted text `[C05-017]`. The book says many old tricks no longer work on most models, so treat them as test cases, not a current-threat ranking `[C05-016]`. Models that follow instructions better also follow malicious ones better, and tool or data access widens the surface `[C05-016]`. Plan to learn exposure by red teaming or probing with attack benchmarks and tools (examples, time-sensitive) `[C05-018]`.
4. **Design input guardrails** `[C10-004]`.
   - External API in use: detect sensitive data (IDs, phone numbers, bank accounts, faces, company keywords) and either block or mask; keep a reversible map to unmask the response `[C10-004]`. Self-hosting removes many input checks `[C10-004]`.
   - Add filters for unusual strings, out-of-scope topics, known attack patterns and abnormal usage (many near-identical requests in a short time) `[C05-018]`.
5. **Design output guardrails** `[C10-004]`. Name the failure modes for this application: empty or malformed output, hallucination, toxicity, PII, tool or code execution, brand risk. For each pick a policy: retry (adds cost; parallel duplicate calls keep latency down), fallback to a human, or block `[C10-004]`. Guardrails reduce risk but never remove it `[C10-004]`. Track the false refusal rate alongside the violation rate (successful attacks over attempts); a system that refuses everything has zero violations and is useless `[C10-004]`, `[C05-018]`. Human-fallback triggers the book reports: detected anger, a turn-count limit, specific phrases `[C10-004]`.
6. **Add system-level defenses** from `[C05-018]`:
   - Run generated code isolated from the user's machine.
   - Require human approval for impactful actions (any query that changes a database: DELETE, DROP, UPDATE).
   - Prompt-level: say explicitly what not to return, repeat the system prompt after the user input (costs tokens and latency), warn about known attack styles, and inspect default templates of prompt tools, which can be too permissive.
   - Model-level: prefer models with an instruction hierarchy (system over user over model output over tool output), so tool output cannot override instructions.
   - Residual risk remains while the system can take impactful actions; state it in the risk section.
7. **Decide streaming against guardrails.** Streaming shows tokens before a guardrail can judge them; decide whether the loss of full-response checks is acceptable, and whether guardrail latency is acceptable at all `[C10-004]`.
8. **Router and gateway.** Add a router only when more than one solution or model is in play: an intent classifier sends simple queries to cheaper models, specialised queries to specialised ones, out-of-scope queries to a stock reply, ambiguous ones to a clarifying question `[C10-005]`. Routers must be small, fast and cheap, and context limits between routed models must be handled `[C10-005]`. Add a gateway for a unified interface, one controlled access point instead of shared API keys, per-user model rules and usage caps, and fallback on rate limits or outages `[C10-005]`. Building one is easy; off-the-shelf ones exist (examples, time-sensitive) `[C10-005]`. Routing usually sits before retrieval (scope and need-for-retrieval checks), though the common pattern is routing, retrieval, generation, scoring `[C10-005]`.
9. **Caches.** Take the decisions from `inference-plan.md`; place an input cache and a retrieval cache, and exclude user-specific data `[C10-006]`.
10. **Agent patterns.** Add loops, parallel branches or conditional flow only if the task needs them `[C10-007]`. Grant write actions (send email, place order, transfer money) only with the strictest controls, as they raise risk sharply `[C10-007]`, `[C05-018]`. A complex system has more failure modes and is harder to debug; that obliges the observability plan in `ops-cost-feedback.md` `[C10-007]`.
11. **Orchestration.** Define components (models, data sources, tools, evaluation and monitoring tools) and chain them; run independent steps in parallel for latency (a router and PII removal can run together) `[C10-009]`. An AI pipeline orchestrator is not a general workflow scheduler `[C10-009]`. Build the first version without an orchestrator, since tools add complexity and can hide behaviour; adopt one later after checking integration and extensibility, support for complex pipelines, and ease of use, performance and scalability (avoid hidden API calls and added latency) `[C10-009]`.
12. **Draw the diagram and fill the template** (section 3 components, one line each on purpose, I/O, decision record, failure modes; section 4 links the evaluation plan; section 6 holds residual risks and open questions).

## Evidence and exit gate
Each component has a stated need, an owner layer, a decision record and a failure mode. Every guardrail ties to an attack family or failure mode from step 3 or 5. Residual risks and unverified provider claims are listed. Then run `design-review-gate.md`.

## Outputs
Fill `../../templates/architecture-design.md` and write `../../templates/decision-record.md` per added component.

## Pitfalls
- Adding components "because the book lists them"; the order is a common path, not a rule `[C10-003]`.
- Guardrails so strict they refuse legitimate requests (false refusals) `[C10-004]`, `[C05-018]`.
- Treating a prompt as a security boundary `[C05-018]`, `[C05-004]`; trusting tool output as instructions `[C05-016]`.
- Caching an answer that contains one user's data `[C10-006]`.
- Write actions without approval or isolation `[C10-007]`.
- Adopting an orchestrator first and losing visibility `[C10-009]`.
- Leaking private data to an external API through prompts, system prompts or tool results `[C10-004]`, `[C05-017]`.
