---
name: intake
mode: architect
rows: [C01-015, C01-016, C01-017]
---
# Intake: ask only for what is still missing and material

Run after discovery. The aim is the smallest set of questions whose answers change the work. A question is worth asking only if (a) discovery did not answer it, and (b) a different answer would lead to a different design or a different test plan.

## How to ask

- Use AskUserQuestion, at most four questions per round, each with 2-4 options and a recommended default marked first.
- Do not ask about something the project already shows. Confirm it in the context summary instead.
- If the session cannot ask questions, proceed on explicit assumptions, put them at the top of the output, and note which answer would change the result.
- Record every answer with `RunState.set_answer` and every assumption with `RunState.add_assumption`.

## Both modes

| Topic | Why it matters |
|---|---|
| Objective and definition of success | Everything is judged against this; evaluation criteria derive from it (Ch 4) |
| Users, scale and traffic shape | Drives latency, cost and infrastructure choices (Ch 9, 10) |
| Constraints: budget, latency target, privacy and compliance, data residency, preferred or banned providers | Eliminates options early (model selection, build vs buy; Ch 4) |
| What may be touched: dev, staging, production | Production is read-only |
| Who reads the output and in what format | Sets report length and depth |

## Architect mode adds

| Topic | Why it matters |
|---|---|
| The use case and the cost of a wrong answer | Sets the evaluation bar and guardrail strictness (Ch 1, 4) |
| Available data and its sensitivity | Decides RAG, finetuning and data-engineering needs (Ch 6-8) |
| Existing systems to integrate with | Shapes architecture and tool design (Ch 10) |
| Team skills and timeline | Affects build-vs-buy and how ambitious the pattern can be (Ch 1, 4) |
| Why build this: competitive threat, productivity gain, or hedge; and who the AI answers to (human reviews, AI answers simple cases, AI answers all) | Sets urgency, build-vs-buy lean and the human role `[C01-015]` |
| Is AI critical or complementary, reactive or proactive, static or continually updated from feedback | Each changes the accuracy bar, latency tolerance and feedback needs `[C01-015]` |
| Existing baseline: current process, current metrics, any prototype or demo | A demo says little about a product; the baseline sizes the gap `[C01-017]` |
| Hosting: cloud, self-hosted, local | Affects model choice and inference options (Ch 4, 9) |

## Review & Test mode adds

| Topic | Why it matters |
|---|---|
| Scope: whole system or one component | Bounds the test plan |
| How to run the project: commands, test suites, environment | Needed to execute checks at all |
| Access to a dev or staging endpoint, logs, sample inputs, any eval data | Without these, many checks become `NOT_RUN` |
| Permission for paid model calls and a spend cap | Eval runs and probes cost money |
| Known issues and recent incidents | Focuses the review |
| Report audience and format | Developers need repro steps; managers need impact |

## Modules to load

| Row | Module | Why it is needed here |
|---|---|---|
| C01-015 | [Use Case Evaluation](../../core/ai-engineering-building-applications-with-foundation-models/ch01-intro/p079-use-case-evaluation.md) | Why the use case exists, how critical AI is, reactive or proactive, dynamic or static, human role, defensibility: these decide the questions on use case, cost of a wrong answer and team ambition `[C01-015]` |
| C01-016 | [Setting Expectations](../../core/ai-engineering-building-applications-with-foundation-models/ch01-intro/p085-setting-expectations.md) | Success is business impact first, then a usefulness threshold across quality, latency and cost: this is why "objective and definition of success" and the latency and budget constraints are asked `[C01-016]` |
| C01-017 | [Milestone Planning](../../core/ai-engineering-building-applications-with-foundation-models/ch01-intro/p086-milestone-planning.md) | A demo says little about a product (the last mile), so team skills, timeline and the existing baseline are asked before design `[C01-017]` |

## Procedure

1. Read the discovery summary and mark every row of the tables above `known`, `ask` or `assume` (see [intake-questionnaire.md](../../templates/intake-questionnaire.md)). INTERPRETATION: this triage is the skill's, not the book's.
2. Ask the `ask` rows, at most four per round, most design-changing first. For a number the user cannot give (latency target, budget, usefulness threshold), offer a proposed default with its reasoning and mark it an assumption; the book says to define a usefulness threshold across quality, latency and cost, and to expect to refine metrics later `[C01-016]`.
3. Never request secrets, credentials or customer data; ask for their location or a redacted sample instead (SUPPLEMENTARY: standard data-handling practice).
4. Show the answers and assumptions back to the user for correction before the gate.

## Gate

Required inputs are present, or every gap is a recorded assumption. Then advance the run state to `intake`.

## Outputs

The recorded answers and assumptions in the run state, and the filled [intake-questionnaire.md](../../templates/intake-questionnaire.md) as the working list.

## Pitfalls

- Asking what discovery already answered, or asking questions whose answer would not change the design.
- Treating a working demo as evidence that the timeline is short `[C01-017]`.
- Defining success by volume alone and leaving out satisfaction and the usefulness threshold `[C01-016]`.
