---
name: agents-and-tools
mode: architect
rows: [C06-008, C06-009, C06-010, C06-011, C06-012, C10-007]
---
# Agents, tools, planning, memory and agent evaluation

## When to use
Run when `solution-pattern.md` selected an agentic pattern: the system must take several steps, call tools, or change its environment. If a single prompt or plain RAG meets the use case, do not add an agent; each step adds compounding error and cost. Reconcile with `data-and-retrieval.md` (retrievers and SQL executors are tools) and `structured-outputs-and-sampling.md` (tool calls are structured outputs).

## Inputs needed
From discovery and `intake.md`; ask only what is missing:
- The environment the agent works in and the actions it may perform (read-only vs write).
- Task shape: typical number of steps, which tasks are in and out of scope, time limits.
- Cost of a wrong action, who can approve risky actions, and existing systems the tools would touch.
- Candidate model(s) (agents usually need stronger models) and context-window size.
- What must persist across sessions (preferences, history).

## Modules to load
| Row | Module | Why it is needed here |
|---|---|---|
| C06-008 | [Agent Overview](../../core/ai-engineering-building-applications-with-foundation-models/ch06-rag-agents-memory/p536-agent-overview.md) | Definition, environment and actions, compound mistakes |
| C06-009 | [Agent Tools](../../core/ai-engineering-building-applications-with-foundation-models/ch06-rag-agents-memory/p540-tools.md) | Tool categories, inventory, write-action risk |
| C06-010 | [Agent Planning](../../core/ai-engineering-building-applications-with-foundation-models/ch06-rag-agents-memory/p546-planning.md) | Plan generation, function calling, control flow, reflection, tool selection |
| C06-011 | [Agent Failure Modes and Evaluation](../../core/ai-engineering-building-applications-with-foundation-models/ch06-rag-agents-memory/p576-agent-failure-modes-and-evaluation.md) | Failure taxonomy and metrics |
| C06-012 | [Memory](../../core/ai-engineering-building-applications-with-foundation-models/ch06-rag-agents-memory/p581-memory.md) | Short-term, long-term, internal knowledge; management strategies |
| C10-007 | [Step 5. Add Agent Patterns](../../core/ai-engineering-building-applications-with-foundation-models/ch10-architecture-feedback/p875-step-5-add-agent-patterns.md) | Where loops and write actions sit in the platform |

## Procedure
1. **Define the agent.** Write its environment and its action set; each constrains the other. Plain RAG is already an agent with retrieval and SQL tools, so state what the agentic upgrade adds. `[C06-008]`
2. **Estimate compound error before committing.** At 95% accuracy per step the book gives about 60% over 10 steps and about 0.6% over 100. Take the per-step accuracy from evaluation of the chosen model, compute the product for the expected step count, and if it misses the success bar, cut steps, add validation, or use a stronger model. `[C06-008]` (the formula is the book's compounding example; applying it to your numbers is `INTERPRETATION`).
3. **Design the tool inventory.** Success depends on the inventory and the planner. Pick from three categories: `[C06-009]`

| Category | Examples in the book | Design note |
|---|---|---|
| Knowledge augmentation | retrievers, SQL executor, web browsing, internal search, email and chat readers | Fixes stale knowledge; choose internet APIs carefully |
| Capability extension | calculator, converters, translator, code interpreter, image captioning, OCR | Cheaper than training the weakness away; code interpreter carries code-injection risk |
| Write actions | send email, update database, start a transfer | Highest risk; see step 4 |

   The book's evidence that tools pay: a GPT-4 agent with 13 tools (Chameleon) beat GPT-4 alone on several benchmarks (time-sensitive example). Tools can also make a text-only model multimodal (captioning, OCR, transcription, image generation). More tools mean more capability but harder use and longer descriptions. Settle the set by experiment: compare tool sets, ablate (if removing a tool causes no drop, drop it), plot call distribution, and replace tools the agent keeps getting wrong. Different tasks and models prefer different tools. `[C06-010]` When choosing a framework, check which planners, tools and control flows (parallel, if, for loop) it supports and how easily tools are added; the book's framework names are time-sensitive examples. `[C06-010]`
4. **Gate write actions.** Default to read-only. For each write action define the automation level: human approval for risky operations (database updates, merging code, transfers), or human execution. Place write actions after the output stage with guardrails, per the architecture pattern. The book's rule is utmost care because capability and risk rise together. `[C10-007]` `[C06-009]` `[C06-010]`
5. **Design planning.**
   - Decouple planning from execution: generate a plan, validate it (heuristics such as no invalid tools and a maximum step count, or an AI judge), execute only validated plans. Unvalidated plans can burn time and API spend. `[C06-010]`
   - Add an intent classifier, including an IRRELEVANT label so out-of-scope requests are declined cheaply. `[C06-010]`
   - Use function calling: declare each tool with entry point, parameters and documentation; set tool choice (required, none, auto) per query. APIs may ensure valid function names but not correct parameter values, so log every call's parameters. `[C06-010]`
   - Granularity: detailed plans are harder to generate but easier to execute. Natural-language plans plus a translator survive tool API changes; exact function names are brittle. `[C06-010]`
   - Control flow: sequential, parallel, if, for loop. Non-sequential plans are harder for models; use parallelism to cut latency only where the framework supports it. `[C06-010]`
   - Improve weak planning with the book's list of levers: better prompt and examples, better tool descriptions, simpler functions (split a complex one), stronger model, finetune the planner (then see `finetune-decision.md`). INTERPRETATION: try them roughly in that order, cheapest first. `[C06-010]`
   - To cut latency, several plans can be generated in parallel and an evaluator picks one, at extra cost. `[C06-010]`
   - Whether foundation models can plan is an open question in the book (evidence is largely anecdotal; a model may be one part of a planner alongside search and state tracking). INTERPRETATION: treat plans as proposals to validate, not facts. `[C06-010]`
   - Humans can join plan, validate or execute stages (supply a high-level plan, approve, or execute); define the automation level per action. `[C06-010]`
6. **Add reflection where it pays.** Reflect after the query (feasible?), after the plan, after each step, and after the run. ReAct interleaves thought, action and observation; Reflexion adds an evaluator and a self-reflection module. Cost: more tokens and latency, and long few-shot formats eat context. INTERPRETATION: use it where reflection errors (claiming done when not) matter more than latency. `[C06-010]` `[C06-011]`
7. **Design memory.** Sort information by use frequency: needed for every task goes into the model (training or finetuning), rarely needed goes to retrieval-backed long-term memory, immediate details stay in context. Reserve a share of context for retrieved memory (the book's example is 30%) and spill the overflow. Pick the eviction policy: FIFO is simple but can drop the messages that state the goal; summarisation with entity tracking, redundancy removal, and reflection-based insert/merge/replace are the alternatives. Decide how contradictions resolve (newest wins, or a model decides). Memory also gives cross-session persistence, consistency and structure-preserving storage. `[C06-012]`
8. **Place it in the platform.** Agent patterns turn the sequential flow into loops, branches and parallel steps: for example a response re-entering context construction for another retrieval. The book notes complexity adds failure modes and makes debugging harder and points to observability; INTERPRETATION: require tracing before launch (see `ops-cost-feedback.md`). `[C10-007]`
9. **Plan agent evaluation now.** Evaluate by identifying failure modes and measuring how often each occurs. Build a planning dataset of (task, tool inventory) tuples, generate K plans per task, and measure: `[C06-011]`

| Metric | Failure it exposes |
|---|---|
| Share of valid plans; plans needed to get one valid | Planning quality |
| Share of valid tool calls | Tool use failure |
| Rate of invalid tool; invalid parameters; incorrect parameter values | Three distinct tool-use errors |
| Goal failure (wrong goal or ignored constraints), reflection errors, time overruns | Plan-level failures |
| Tool correctness tested per tool; translator benchmark if used | Tool failures |
| Steps, cost and latency per task against a baseline (human or other agent) | Efficiency |

   Test each tool on its own and log every tool call with its output for inspection. Look for patterns by task type and by tool; fix a hard tool with prompts, examples or finetuning, or replace it. Missing tools show up as repeated failures in one domain; consult domain experts. The book names function-calling and planning benchmarks as examples (time-sensitive). `[C06-011]`

## Evidence and exit gate
Exit when: environment and actions are written; compound-error arithmetic is shown with stated per-step accuracy (or marked `UNVERIFIED`); each tool has a category, owner and test; every write action has an approval level; plan validation, intent classification and reflection choices are recorded; memory placement and eviction are chosen; the failure-mode metrics above are in the eval plan with thresholds. Unknown model accuracy per step is an assumption to be measured.

## Outputs
Fill [../../templates/decision-record.md](../../templates/decision-record.md) for: agent vs non-agent, tool inventory, write-action policy, planning design, memory design. Send the metric table to [../../templates/eval-plan.md](../../templates/eval-plan.md) and the flow to [../../templates/architecture-design.md](../../templates/architecture-design.md).

## Pitfalls
- Underestimating compounding errors on long tasks. `[C06-008]`
- Giving a code interpreter or write tool without security controls. `[C06-009]`
- Adding tools without ablation; very long tool descriptions. `[C06-010]`
- Executing a plan that was never validated, or hallucinated tool names and guessed parameters. `[C06-010]`
- Hard-coding exact function names that change. `[C06-010]`
- Agent claims completion without finishing (reflection error); ignoring time as a constraint. `[C06-011]`
- Judging efficiency against a human baseline without noting AI and humans work differently. `[C06-011]`
- FIFO eviction dropping the conversation's purpose. `[C06-012]`
- Shipping a multi-step system with no tracing: more failure points, harder debugging. `[C10-007]`
