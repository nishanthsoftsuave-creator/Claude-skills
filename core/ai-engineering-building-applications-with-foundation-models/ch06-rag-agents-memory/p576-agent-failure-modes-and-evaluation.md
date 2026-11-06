---
id: C06-011
title: Agent Failure Modes and Evaluation
source_pages: "576-580"
chapter: 6
concepts: [agent-evaluation, failure-modes, planning-failures, tool-failures, goal-failure, reflection-errors, agent-efficiency, tool-use-validity]
related: [C06-010, C06-012, C06-013]
time_sensitive: false
---
# Agent Failure Modes and Evaluation
(Source: PDF pp. 576-580; the section's last paragraph on comparing efficiency against a baseline sits at the top of PDF p. 581, cited below as the tail page. The lines at the top of p. 576 about the Voyager skill manager close the previous section and are not covered here.)

## What the section covers
How to evaluate an agent by cataloguing the ways it can fail and measuring how frequently each failure happens. The failures are grouped into planning failures, tool failures and efficiency problems, on top of the failures that every AI application shares (covered in Chapters 3 and 4).

## Meaning
- Evaluation is fundamentally about detecting failures. The more complicated the task an agent performs, the more places it can go wrong, and some failures are simpler to catch than others (PDF p. 576).
- Besides the failure modes common to all AI applications, agents have their own failures arising from planning, tool execution and efficiency (PDF p. 576).
- The book's recipe for evaluating an agent: identify its failure modes, then measure how often each occurs (PDF p. 576).
- The author built a small benchmark illustrating these failure modes, available in the book's GitHub repository. Existing agent benchmarks and leaderboards named in the text are the Berkeley Function Calling Leaderboard, the AgentOps evaluation harness and the TravelPlanner benchmark (PDF p. 577).
- This section follows the earlier observation that an agent's success in an environment depends on its tool inventory and its planning ability, so a weakness in either can make it fail (PDF p. 576).

## How it works

### Planning failures
Planning is difficult and can break in many ways. The most common kind is tool use failure, where the generated plan contains one or more of these errors (PDF p. 577):
- Invalid tool: the plan names a tool that is not in the inventory, for example `bing_search` when no such tool exists.
- Valid tool, invalid parameters: for example calling `lbs_to_kg` with two parameters when the tool takes only one, `lbs`.
- Valid tool, incorrect parameter values: for example calling `lbs_to_kg` with the right single parameter but passing 100 when it should be 120.

Other planning failure modes (PDF p. 578):
- Goal failure: the agent does not reach the goal, either because the plan does not solve the task at all or because it solves it while ignoring the stated constraints. Illustration: asked for a two-week trip from San Francisco to Hanoi on a $5,000 budget, an agent might plan a trip to Ho Chi Minh City, or plan the right trip but far over budget.
- Time as an overlooked constraint: often the time an agent takes does not matter much, since you hand it a task and check back when it is done. In many cases though an agent loses usefulness as time passes; a grant proposal finished after the deadline is of little help.
- Reflection errors: the agent believes it has completed a task when it has not. Example: told to assign 50 people to 30 hotel rooms, it assigns only 40 people yet insists the job is done. The book calls this an interesting planning failure.

### Evaluating planning
Build a planning dataset in which each example is a tuple (task, tool inventory). For each task, have the agent generate K plans. Then compute (PDF pp. 578-579):
1. Of all generated plans, how many are valid?
2. For a given task, how many plans must the agent generate on average to get a valid one?
3. Of all tool calls, how many are valid?
4. How often are invalid tools called?
5. How often are valid tools called with invalid parameters?
6. How often are valid tools called with incorrect parameter values?

Then look for patterns in the outputs (PDF p. 579): which task types the agent fails more on, and whether you have a hypothesis why; which tools it keeps getting wrong. Some tools are simply harder for an agent to use. A hard tool can be made easier through better prompting, more examples or finetuning; if all of these fail, consider replacing the tool with something easier to use.

### Tool failures
A tool failure means the correct tool was chosen but its output is wrong (PDF p. 579).
- The tool itself may give wrong results, for instance an image captioner producing an incorrect description or an SQL generator producing a wrong query (PDF p. 579).
- If the agent emits only high-level plans and a translation module converts each planned action into executable commands, the failure can be a translation error (PDF p. 579).
- The agent may lack the right tools altogether. The book's example is a task needing current stock prices from the internet when the agent has no internet access (PDF p. 580).

Practices for tool failures (PDF p. 580):
- Tool failures depend on the tool, so test every tool on its own.
- Always print each tool call and its output so they can be inspected and evaluated.
- If there is a translator, build benchmarks to evaluate it.
- Detecting missing tools requires knowing which tools should be used. If the agent keeps failing in a particular domain, it may lack tools for that domain; work with human domain experts and watch which tools they use.

### Efficiency
An agent may produce a valid plan with the right tools and still be inefficient. Track (PDF p. 580):
- the average number of steps needed to finish a task;
- the average cost to finish a task;
- how long each action usually takes, and whether some actions are especially slow or costly.

Compare these numbers to a baseline, which can be another agent or a human operator. The caution: humans and AI work very differently, so what is efficient for one may not be for the other. Visiting 100 web pages is inefficient for a person who can open one at a time but trivial for an AI agent that can fetch them all at once (PDF p. 581).

## Why it matters
Because failures grow with task complexity, knowing the specific failure categories and their rates tells you where to improve prompts, examples, finetuning, tools or the tool inventory.

## Relations
Builds on the planning and tool-inventory material of the preceding agent sections (C06-010). Followed by the memory section (C06-012), which the book introduces by noting that RAG and agents both handle information beyond the context limit. The chapter wrap-up is C06-013.
