# Architecture design: <project or feature>

Date: <date> · Mode: Architect · Audience: <who reads this>

Keep each section as short as the project allows. Delete sections that do not apply and say why in one line.

## 1. Goal and success criteria

The use case, who it serves, the cost of a wrong answer, and the measurable definition of success. Constraints carried from intake (budget, latency, privacy, residency, providers).

## 2. Approach in one page

The chosen pattern (prompting, RAG, agent, finetuning, or a combination) and the reason, in a paragraph, with a simple component diagram (text or a Mermaid block).

## 3. Components

For each component that exists in the design: purpose, inputs and outputs, the decision record behind it, and its failure modes.

- Model(s) and how they are accessed (build vs buy, hosting)
- Context construction (prompts, retrieval, memory, tools)
- Guardrails (input and output)
- Routing and gateway, caching, agent patterns, if used
- Data pipelines and datasets
- Orchestration

## 4. Evaluation plan

Link to `eval-plan.md`: criteria, methods, datasets, thresholds, and when each runs.

## 5. Operations

Monitoring and observability, cost and latency targets with the levers to hold them, feedback collection, maintenance and update cadence.

## 6. Risks and open questions

Each risk with its mitigation or the decision still needed. Assumptions the design rests on.

## 7. Milestones

Ordered steps with the check that ends each one.

## 8. Decision records and book modules used

List of decision records and the `core/` modules consulted, so each choice is traceable to its criterion.
