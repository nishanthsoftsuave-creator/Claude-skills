---
name: agent-review
mode: review-test
rows: [C06-008, C06-009, C06-010, C06-011, C06-012, C10-007, C03-016]
---
# Agent review

## When to use
The project has a system in which a model decides actions: calls tools, plans multi-step work, loops, keeps memory, or can change external systems. The book counts even simple RAG-with-SQL systems as agents, so use this for any model that selects tools. Route here from `routing.md` for "Review an agent or its tools and memory". Use `security-and-prompt-attacks.md` for attack testing; this workflow only covers write-action exposure as a design review.

## Inputs needed
- The agent's environment, tool inventory (names, parameters, documentation), planner model, control flow (loops, branches, parallel steps), memory stores, and human approval points. Discovery (`../discovery.md`) usually finds these; ask only for gaps (`../architect/intake.md`).
- Which tools are read-only and which can write (send, update, delete, transfer).
- For run checks: a sandbox or non-production environment, permission to execute the agent, a spend cap, a step cap, and a kill switch. Never run write-capable tools against production; in the sandbox, stub or allow-list tools that reach the internet, email or payments. If no safe environment exists, run checks are `BLOCKED` and static review proceeds.
- Task fixtures: tasks with known right answers or known right tool sequences (from the user, or drafted by the reviewer and confirmed by the user).

## Modules to load
| Row | Module | Why it is needed here |
|---|---|---|
| C06-008 | [Agent overview](../../core/ai-engineering-building-applications-with-foundation-models/ch06-rag-agents-memory/p536-agent-overview.md) | Environment, actions, compounding step errors |
| C06-009 | [Agent tools](../../core/ai-engineering-building-applications-with-foundation-models/ch06-rag-agents-memory/p540-tools.md) | Tool categories, inventory, write-action risk |
| C06-010 | [Agent planning](../../core/ai-engineering-building-applications-with-foundation-models/ch06-rag-agents-memory/p546-planning.md) | Plan validation, function calling, control flow, reflection, tool selection |
| C06-011 | [Failure modes and evaluation](../../core/ai-engineering-building-applications-with-foundation-models/ch06-rag-agents-memory/p576-agent-failure-modes-and-evaluation.md) | Failure taxonomy and the metrics to compute |
| C06-012 | [Memory](../../core/ai-engineering-building-applications-with-foundation-models/ch06-rag-agents-memory/p581-memory.md) | Short-term, long-term, eviction strategies |
| C10-007 | [Add agent patterns](../../core/ai-engineering-building-applications-with-foundation-models/ch10-architecture-feedback/p875-step-5-add-agent-patterns.md) | Loops and write actions in the platform; observability need |
| C03-016 | [Limitations of AI as a Judge](../../core/ai-engineering-building-applications-with-foundation-models/ch03-eval-methodology/p281-limitations-of-ai-as-a-judge.md) | The book's limits of AI judges (inconsistent scores, unstandardized criteria, cost and latency, biases), relevant to judge-validated plans and judged trajectories. The skill's `probable` cap for judge-only findings is INTERPRETATION built on them |

## Procedure
1. **Describe the agent.** State environment, tool inventory and planner. Per task, steps needed: accuracy compounds, so at 95% per step the book computes about 60% over 10 steps and about 0.6% over 100. INTERPRETATION: use that to flag long unvalidated chains as risky; report it as arithmetic from the book's example, not a measurement of this agent. `[C06-008]`
2. **Inventory review.** Classify every tool as knowledge augmentation, capability extension, or write action. For each: a name, parameters and documentation the model can use; a reason it is there. Rule: more tools raise capability but make correct use harder, so require evidence that each tool earns its place (ablation, RA-06). Internet-reaching tools: check that sources are chosen with care. Code interpreters: check isolation, since code injection is a named risk. `[C06-009]`
3. **Write actions.** For every write-capable tool, list the blast radius (data deleted, money moved, messages sent), who can trigger it, and the human approval point. The book's stance: write actions make automation possible but need trust in capability and security, and the intern analogy applies: no authority to delete production data. INTERPRETATION: a write action with no approval step, scope limit or audit trail is a `risk` at least (the book asks for trust in capability and security and the utmost care with write actions, not for these specific controls); reproduce only in a sandbox. `[C06-009]` `[C10-007]`
4. **Planning design.** Check whether planning is decoupled from execution: plans validated before execution (heuristic checks for invalid tools and maximum length; optionally a judge) so an unsupervised agent cannot burn time and spend on a long bad plan. Check step and cost caps (INTERPRETATION; the book names a maximum plan length as a heuristic). Check where humans can join (plan, validation, execution) and that the allowed automation level is defined per action. Check whether intent classification exists and can label out-of-scope requests as irrelevant so the agent declines instead of spending effort. `[C06-010]`
5. **Function calling.** Check each tool is declared with entry point, parameters and documentation, the per-query tool list and the tool-choice control (required, none, auto) are set deliberately, and that parameter values actually used are logged and inspectable. APIs may ensure a valid function name but not correct parameter values. `[C06-010]`
6. **Plan format and control flow.** Exact tool names in plans are brittle when inventories change; natural-language plans need a translator that must itself be tested. Identify supported control flows (sequential, parallel, branch, loop); non-sequential plans are harder to generate and translate. `[C06-010]`
7. **Reflection.** Check where the agent reflects (feasibility, plan, each step, completion) and what happens on failure (replan). Costs to report: extra tokens, latency, example-heavy prompts consuming context. `[C06-010]`
8. **Tool selection evidence.** Look for tool-set comparisons, an ablation (a tool whose removal changes nothing is a drop candidate), tool-call distribution, and tools the agent keeps getting wrong (candidates for better prompting, examples, finetuning, or replacement). Other planning levers the book lists: simpler or split functions, better tool descriptions, a stronger planner. Framework tool sets are examples; check how easily tools can be added. `[C06-010]`
9. **Failure taxonomy.** Evaluation means identifying failure modes and measuring how often each occurs. Planning failures: invalid tool, valid tool with invalid parameters, valid tool with wrong values, goal failure (wrong goal or constraints ignored), time ignored as a constraint, reflection error (claims done when not). Tool failures: wrong tool output, translation errors, missing tool. Efficiency: steps, cost, time per action against a baseline (humans and AI work differently, so a human baseline can mislead). Use these labels in findings. `[C06-011]`
10. **Memory.** Place each kind of information by frequency of use: essential for every task in the model (training or finetuning), rarely needed in retrieval-backed long-term memory, immediate details in context; structured data may need a store that keeps its structure rather than pasted text. Check what happens at context overflow and which eviction strategy is used: FIFO can discard the messages that state the goal; summarization, redundancy removal and reflection-based updates are the book's alternatives; check handling of contradictory entries (keep newer, or model decides, depending on use case). Retrieval from long-term memory is reviewed as in `retrieval-review.md`. `[C06-012]`
11. **Platform fit.** If the agent loops back into context construction or can act, check that monitoring and tracing exist: complex systems have more failure points and are harder to debug. Observability depth is reviewed in `observability-review.md`. `[C10-007]`

## Checks
Run commands as `python scripts/run_check.py --case <ID> --evidence-dir <run>/evidence -- <command>`. Executing an agent costs money and may act; run only in the sandbox with caps agreed in the plan.

| check | what is checked | how | evidence produced | type | criterion | how a failure is judged |
|---|---|---|---|---|---|---|
| AR-01 | Environment, tools, planner, control flow documented from code | Read agent code and config | `AR-01-notes.md` | review | C06-008 | Undetermined element: `unverified` with the question that would settle it |
| AR-02 | Tool inventory classified; each tool documented and justified | Read tool declarations | `AR-02-notes.md` table | review | C06-009 | Tool with missing or vague parameter docs: `probable` source of invalid calls; unjustified tool: `recommendation` |
| AR-03 | Write-action exposure and approval points | Read write-capable tools and the code paths that reach them | `AR-03-notes.md` | review | C06-009, C10-007 | No approval, scope limit or audit on a destructive or financial action: `risk`, major; becomes `confirmed` only if reproduced in a sandbox |
| AR-04 | Plan validation and step/cost caps before execution | Read planner and executor; in sandbox, give a task that induces an invalid plan (run through `run_check.py`) | `AR-04-notes.md`, optionally `AR-04.exec.json` | review (run if induced) | C06-010 | Invalid or over-long plan executed anyway: `confirmed` if reproduced |
| AR-05 | Parameter values logged for every tool call | Read logging; run one fixture and inspect the trace | `AR-05-notes.md`, optionally `AR-05.exec.json` | review (run if fixture run) | C06-010 | Calls not inspectable: `probable` defect (book tip: always report parameter values) |
| AR-06 | Tool usefulness: ablation and call distribution | Run fixture suite with and without a tool; count calls per tool from traces | `AR-06.exec.json`, comparison table | run | C06-010 | Tool whose removal does not change results: `recommendation` to drop; reported with suite size |
| AR-07 | Planning metrics on (task, tool inventory) fixtures: valid-plan rate, plans needed per valid one, valid-call rate, invalid-tool rate, bad-parameter rate, wrong-value rate | Generate K plans per fixture task (needs approval and spend cap); script counts each category | `AR-07.exec.json`, `AR-07-plans.*`, metric table | run | C06-011 | Rates are reported as measured; no book threshold exists, so judge against the user's requirement. Invalid-tool and bad-parameter counts can be scripted against the declarations; wrong-value rates need known correct values in the fixtures, else `unverified`; a judge-only plan-validity verdict is capped at `probable`. Patterns by task type or tool are findings |
| AR-08 | Failure injection: invalid tool name, bad parameter, tool error, tool timeout, empty result | Sandbox harness (user-approved) wraps a tool to return each fault; run through `run_check.py` | `AR-08.exec.json`, traces | run | C06-011 | INTERPRETATION: these fault types are the reviewer's adaptation of the book's tool-failure ideas. Agent loops, hides the error, or claims success after a fault: `confirmed` if it occurs in the first run and the one re-run |
| AR-09 | Goal and constraint failures: tasks with a hard constraint (budget, deadline, count) | Run constraint fixtures; compare final state to the constraint | `AR-09.exec.json`, results | run | C06-011 | Constraint violated or task declared done while incomplete (reflection error): `confirmed` if reproduced |
| AR-10 | Each tool tested on its own | Existing unit tests or a small harness per tool | `AR-10.exec.json` per tool | run | C06-011 | A tool giving wrong output on a known case: `confirmed` tool failure |
| AR-11 | Trajectory inspection: steps, cost, time per action against a baseline | Collect traces from AR-07 to AR-09 runs; compute averages; baseline from a human or another agent if available | `AR-11-notes.md`, `AR-11.exec.json` | run | C06-011 | No baseline: report numbers as `unverified` efficiency; step counts far beyond the baseline: `probable` inefficiency (a human baseline may not transfer to an AI agent) |
| AR-12 | Memory placement and overflow strategy | Read memory code; run a long fixture conversation past the context limit and ask about its early content | `AR-12-notes.md`, optionally `AR-12.exec.json` | review (run if fixture run) | C06-012 | Early goal lost after eviction: `confirmed` if reproduced; strategy never tested at overflow: `risk` |
| AR-13 | Contradictory or outdated memory entries | Insert a fact and later its contradiction in a sandbox; query | `AR-13.exec.json` | run | C06-012 | Stale value returned where a newer one exists and the use case wants the newer: `confirmed` |
| AR-14 | Pattern fit and observability for loops | Read orchestration; check traces cover each step | `AR-14-notes.md` | review | C10-007 | Loops with no trace of intermediate steps: `risk` |
| AR-15 | Human involvement defined per action | Review automation levels | `AR-15-notes.md` | review | C06-010 | Risky action automated with no stated level of autonomy: `risk` |
| AR-16 | Reflection points and replanning on failure | Read control flow for reflection after query, plan, step, completion; in sandbox, run a fixture with a failing step and read the trace | `AR-16-notes.md`, optionally `AR-16.exec.json` | review (run if fixture run) | C06-010 | No check of outcomes before declaring done: `risk`; reflection present but its token and latency cost never reported: `recommendation` |
| AR-17 | Plan translator and intent handling (if present) | Read translator and intent classifier; in sandbox, feed natural-language plan and out-of-scope fixtures | `AR-17-notes.md`, optionally `AR-17.exec.json` | review (run if fixtures run) | C06-010, C06-011 | Untested translator, or out-of-scope request that triggers tool use: `probable`; reproduced wrong translation: `confirmed` |

## Evidence and exit gate
- Run checks have exec records plus saved traces with tool calls and parameters; secrets in traces are redacted before storing.
- Any failure is re-run once (agents are non-deterministic); differing outcomes are reported as unstable with counts.
- A finding based only on a judge's reading of a trajectory is capped at `probable` (`[C03-016]`).
- Exit gate: every check has a status with reason; if no sandbox existed, the run parts of AR-04 to AR-13, AR-16 and AR-17 are `BLOCKED` and the report says what remains unverified; `python scripts/validate_report.py <run_dir>` prints 0 problems.

## Outputs
Results data and the findings report (`../../templates/findings-report.md`) with failure-mode labels from step 9.

## Pitfalls
- Running a write-capable agent against real systems to "see what happens". `[C06-009]`
- Evaluating only final answers and missing wrong tool calls inside them. `[C06-011]`
- Letting a plan execute unvalidated. `[C06-010]`
- Assuming a long chain is reliable because each step usually works. `[C06-008]`
- Treating a framework's name-brand tools as needed. `[C06-010]`
- FIFO memory that drops the goal statement. `[C06-012]`
- Reading the book's named benchmarks and frameworks as current. `[C06-011]`
