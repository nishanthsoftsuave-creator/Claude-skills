---
id: C06-010
title: Agent Planning
source_pages: "546-575"
chapter: 6
concepts: [planning, plan-generation, decoupled-planning-execution, function-calling, planning-granularity, control-flow, reflection, react, reflexion, tool-selection, tool-transition, fm-vs-rl-planners]
related: [C06-008, C06-009, C06-011]
time_sensitive: false
---
# Agent Planning
(Source: PDF pp. 546-575, plus the opening of the tail page, PDF p. 576, before the "Agent Failure Modes and Evaluation" heading. The section starts part-way down PDF p. 546 at the "Planning" heading; the lines above it belong to the Tools row.)

## What the section covers
How a foundation model agent plans and corrects itself. Topics, in the book's order: what a task and a plan are; an overview of planning, including decoupling planning from execution, multi-agent framing, intent classification and human involvement; whether foundation models can plan at all; a contrast with reinforcement learning planners; plan generation by prompting; function calling; planning granularity; complex plans and control flows; reflection and error correction (ReAct and Reflexion); and tool selection, tool transition and skill libraries.

## Meaning
- A foundation model agent has, at its heart, the model that solves a task. A task is defined by a goal and constraints. The book's example is to schedule a two-week trip from San Francisco to India with a budget of $5,000: the goal is the trip, the constraint is the budget (PDF pp. 546-547).
- Complex tasks need planning. Its output is a plan, "a roadmap outlining the steps needed to accomplish a task". Effective planning generally means understanding the task, weighing options, and choosing the most promising one (PDF p. 547). The author notes planning is a well-studied computational problem and the book only covers the surface.
- Task decomposition is another name for plan generation, because a plan is a sequence of manageable actions (PDF p. 551).

## How it works

### Planning overview
- Many decompositions of a task exist, but not all succeed, and among the correct ones some are more efficient. Example query: "How many companies without revenue have raised at least $1 billion?" Option 1 finds all companies without revenue and then filters by amount raised; option 2 finds companies that raised at least $1 billion and then filters by revenue. Option 2 is more efficient because far more companies lack revenue than have raised $1 billion, so an intelligent agent should choose it (PDF pp. 547-548).
- Planning and execution can be coupled in one prompt: ask the model to think step by step (as in chain-of-thought) and then carry out the steps. The danger is a model producing, say, a 1,000-step plan that does not reach the goal; unsupervised, the agent could burn hours and API spend before anyone notices (PDF p. 548).
- The remedy is to decouple planning from execution: generate a plan first and execute it only after it is validated (PDF p. 548).
  - Heuristic validation: drop plans that contain invalid actions (for example a plan needing Google Search when the agent has no access to it), or plans longer than some number X of steps.
  - AI-judge validation: ask a model whether the plan seems reasonable or how to improve it.
  - If the plan is judged bad, ask the planner for another one. If good, execute it; when the plan uses external tools, function calling is invoked (PDF pp. 548-549).
  - The outputs of execution are evaluated again. A generated plan need not cover the entire task; it can be a small plan for one subtask (PDF p. 549).
- Figure 6-9 (PDF p. 549) shows this loop. What is visible at high resolution: Query -> Planner -> Generated plan -> Evaluator -> Finish (a left-to-right chain). Executor sends an arrow to Tools (up and left into Tools' right side) and an arrow to Tool outputs; Tools also sends an arrow down to Tool outputs; Tool outputs send an arrow down to the Evaluator. A line leaves the left side of Tools and runs left and down into the top of the Planner (arrowhead at the Planner). A separate return line runs along the bottom of the diagram with arrowheads at both ends: one into the bottom of the Planner and one into the bottom of the Executor. That bottom line crosses the Evaluator -> Finish line with no visible junction marker, and no arrow visibly connects the Evaluator to it, so the figure does not unambiguously show the source of the return path to Planner and Executor (it is presumably the Evaluator's feedback, but the drawing does not make this explicit; treat as UNVERIFIED beyond what is drawn). The point of the figure is that only validated plans are executed.
- The resulting system has three components: one generating plans, one validating them, one executing them. Treating each component as an agent makes this a multi-agent system (PDF p. 549).
- Latency/cost trade-off: to speed things up, generate several plans in parallel and let the evaluator choose the best, at extra cost (PDF p. 549).
- Intent: planning requires understanding what the user is trying to do. An intent classifier often helps, built either with another prompt or with a trained classification model (see the earlier discussion of breaking complex tasks into simpler subtasks). It can be regarded as another agent in the multi-agent system (PDF pp. 549-550).
- Knowing the intent helps pick tools. In customer support, a billing query may need a tool for recent payments, whereas a password reset question may need documentation retrieval (PDF p. 550).
- Tip from the book: some queries are out of scope, so the intent classifier should be able to label requests IRRELEVANT. The agent can then politely decline instead of spending FLOPs on impossible solutions (PDF p. 550).
- Humans can join any of the three stages (plan, validate, execute). An expert can supply a high-level plan for the agent to expand when the agent struggles with the whole plan, approve risky operations such as updating a database or merging a code change, or carry out those operations themselves. This requires defining clearly the level of automation allowed for each action (PDF pp. 550-551).

### The four processes of solving a task
Reflection is optional but boosts performance considerably (PDF p. 551).
1. Plan generation: produce a plan for the task (task decomposition).
2. Reflection and error correction: evaluate the plan; if bad, generate a new one.
3. Execution: take the planned actions, often by calling specific functions.
4. Reflection and error correction: evaluate the outcomes, decide whether the goal is met, find and fix mistakes, and generate a new plan if the goal is not reached.
Earlier techniques map onto these: asking a model to "think step by step" asks it to decompose; asking it to "verify if your answer is correct" asks it to reflect (PDF p. 551).

### Can foundation models plan?
- It is an open question. Many researchers think models built on autoregressive language models cannot. Yann LeCun (Meta's Chief AI Scientist) said unequivocally in 2023 that autoregressive LLMs cannot plan. Kambhampati (2023), in "Can LLMs Really Reason and Plan?", argues that LLMs are good at extracting knowledge but not at planning, and that claims of planning ability confuse general planning knowledge with executable plans. His quoted warning: LLM plans may look reasonable yet lead to execution-time interactions and errors (PDF p. 552).
- The book's counterpoint: much of the evidence is anecdotal, and it is unclear whether poor results come from not knowing how to use LLMs properly or from a fundamental inability (PDF p. 552).
- Planning is at its core a search problem: explore paths toward the goal, predict the outcome (reward) of each, choose the most promising, and sometimes conclude that no path exists. Search often needs backtracking; if action A leads to an unpromising state, return and try action B (PDF pp. 552-553).
- Objection: an autoregressive model only generates forward and cannot backtrack. The book says this is not necessarily true: after following action A, a model that decides the path makes no sense can revise it using action B, which is effectively backtracking, or start over on another path (PDF p. 553).
- Another possible cause of poor planning is missing tooling. Planning requires knowing each action's available options and its outcome state. Mountain-walking example: moves are turn right, turn left, turn around, go straight; if turning right means falling off a cliff you would not consider it. Technically, an action moves you between states, and you need the outcome state to decide whether to take it (PDF p. 553).
- So prompting a model to output only a sequence of actions, as chain-of-thought does, is not enough. "Reasoning with Language Model is Planning with World Model" (Hao et al., 2023) argues that an LLM holds so much world information that it can predict each action's outcome and use this to build coherent plans (PDF pp. 553-554).
- Even if AI cannot plan alone, it can be part of a planner, for instance an LLM augmented with a search tool and a state-tracking system (PDF p. 554).

### Foundation model (FM) versus reinforcement learning (RL) planners (sidebar)
- The agent is a core RL concept. The book cites a Wikipedia definition: RL is concerned with how an intelligent agent should act in a dynamic environment to maximize cumulative reward (PDF p. 554).
- FM agents and RL agents are alike in being characterized by their environment and possible actions. They differ in the planner: an RL agent's planner is trained by an RL algorithm, which can take large amounts of time and resources; in an FM agent the model is the planner, which can be prompted or finetuned, generally with less time and fewer resources (PDF p. 554).
- Nothing stops an FM agent from also using RL algorithms. The author suspects that eventually FM agents and RL agents will merge (PDF p. 554).

### Plan generation by prompting
- The simplest way to turn a model into a plan generator is prompt engineering. The running example is an agent helping customers learn about products at Kitty Vogue, with three tools: retrieve products by price, retrieve top products, retrieve product information. The prompt is for illustration only; production prompts would be more complex (PDF p. 555).
- Prompt content (PDF pp. 556-557): a system prompt saying "Propose a plan to solve the task" with five available actions: get_today_date(), fetch_top_products(start_date, end_date, num_products), fetch_product_info(product_name), generate_query(task_history, tool_output), generate_response(query). The plan must be a sequence of valid actions. Two few-shot examples: the task "Tell me about Fruity Fedora" gets the plan [fetch_product_info, generate_query, generate_response]; "What was the best selling product last week?" gets [fetch_top_products, generate_query, generate_response]. Then Task: {USER INPUT} and Plan: is left for the model to complete.
- Two notes on the example (PDF p. 557): the plan format, a list of functions whose parameters the agent infers, is only one of many ways to structure agent control flow; and generate_query takes the task history and the latest tool outputs to build a query for the response generator, with each step's tool output appended to the task history.
- For the input "What's the price of the best-selling product last week", a plan might be get_time(), fetch_top_products(), fetch_product_info(), generate_query(), generate_response() (PDF pp. 557-558).
- Parameters are hard to know beforehand because they often come from earlier tool outputs. If get_time() returns "2030-09-13", the agent can deduce the next call: start_date 2030-09-07, end_date 2030-09-13, num_products 1 (PDF p. 558).
- Often there is not enough information. For "What's the average price of best-selling products?", it is unclear how many products to consider and whether the user means last week, last month or all time. The model then has to guess, and guesses can be wrong (PDF pp. 558-559).
- Since both the action sequence and its parameters are model-generated, they can be hallucinated: an invalid function can be called, or a valid function called with wrong parameters (PDF p. 559).

### Ways to improve an agent's planning (PDF p. 559)
General techniques for improving model performance apply. Specifically:
- Write a better system prompt with more examples.
- Describe the tools and their parameters better.
- Rewrite the functions to be simpler, such as splitting a complex function into two simpler ones.
- Use a stronger model; stronger models are generally better planners.
- Finetune a model for plan generation.

### Function calling
- Many providers offer tool use, effectively turning their models into agents. A tool is a function, so invoking one is called function calling. APIs differ, but generally (PDF pp. 559-560):
  1. Create a tool inventory: declare every tool the model might use. Each tool is described by its execution entry point (such as the function name), its parameters, and its documentation (what it does and which parameters it needs).
  2. Specify which tools the agent may use for a query, since queries need different tools. Many APIs let you pass a list of declared tools per query, and some add a control setting: required (model must use at least one tool), none (model must not use any tool), auto (model decides).
- Figure 6-10 (PDF p. 561), pseudocode meant to be representative across APIs, shows two simple tools. Tool definition: lbs_to_kg(lbs) returns lbs * 0.45359237, and ft_to_meters(ft) returns ft * 0.3048. Tool description (1): lbs_to_kg_tool is a FunctionDeclaration with name "lbs_to_kg", description "Convert from pounds to kilograms", a required integer parameter "lbs" (the value to convert); ft_to_m_tool is declared similarly. Then the user query goes into messages, and a chat completions call (2) passes tools=[lbs_to_kg_tool, ft_to_m_tool] with tool_choice="auto", meaning this query can use two tools.
- Given a query, an agent defined this way decides which tools to use and with what parameters. Some function calling APIs ensure only valid functions are generated but cannot guarantee correct parameter values (PDF p. 561).
- Example: for "How many kilograms are 40 pounds?" the agent decides to use lbs_to_kg_tool with parameter 40. The returned response has finish_reason 'tool_calls', content None, role 'assistant', and one tool call of type 'function' whose name is 'lbs_to_kg' and arguments are '{"lbs":40}'. You then invoke lbs_to_kg(lbs=40) and use its output to answer the user (PDF pp. 561-562).
- Tip: always have the system report the parameter values used in each function call, and inspect them for correctness (PDF p. 562).

### Planning granularity
- Plans can be coarse or fine, like a year planned by quarter, then month, then week. There is a planning/execution trade-off: a detailed plan is harder to generate but easier to execute; a high-level plan is easier to generate but harder to execute. One workaround is hierarchical planning: generate a high-level (quarter-by-quarter) plan, then for each quarter make a month-by-month plan with the same or a different planner (PDF pp. 562-563).
- The examples so far use exact function names, which is very granular. The problem: tool inventories change. get_time() may be renamed get_current_time(), forcing updates to the prompt and every example, and exact names make it harder to reuse a planner across use cases with different tool APIs. A model finetuned on the old inventory must be finetuned again (PDF p. 563).
- Alternative: plans in more natural language, such as: get current date; retrieve the best-selling product last week; retrieve product information; generate query; generate response (PDF pp. 563-564).
- Benefits: the planner is robust to tool API changes, and a model trained mostly on natural language is likely better at understanding and producing natural-language plans and less likely to hallucinate. Drawback: you need a translator that converts each natural-language action into an executable command. Translation is much simpler than planning, so a weaker model can do it with lower hallucination risk (PDF p. 564).

### Complex plans and control flows
- The plans so far were sequential. The order in which actions run is the control flow, and sequential is only one kind; others are parallel, if statement and for loop (PDF pp. 564-565).
  - Sequential: task B after task A completes, probably because B depends on A, e.g. a SQL query runs only after it has been translated from natural language.
  - Parallel: tasks A and B at once. Example: for "Find me best-selling products under $100", retrieve the top 100 best sellers and, for each, retrieve its price.
  - If statement: run B or C depending on the previous step's output. Example: check NVIDIA's earnings report, then decide to buy or sell NVIDIA stock.
  - For loop: repeat task A until a condition is met, e.g. keep generating random numbers until one is prime (PDF p. 565).
- Figure 6-11 (PDF p. 566) draws the four patterns, each with a "control flow decision" node after Task A, and gives these examples: sequential, "talk-to-your-data" (translate text into a SQL query, then execute it); parallel, data analysis (find last week's best sellers, then retrieve each item's price); if, customer support (analyze a company's earnings report, buy shares if positive, sell if negative); for loop, lineage (track a viral post's origin by following reposts back to the original poster).
- In traditional software the conditions for control flows are exact; with AI agents, models decide the control flow. Non-sequential plans are harder to generate and to translate into executable commands (PDF p. 566).
- When evaluating an agent framework, check which control flows it supports. If the system must browse ten websites, can it do so at the same time? Parallel execution can cut user-perceived latency significantly (PDF p. 566).

### Reflection and error correction
- Reflection is not strictly required for an agent to operate but is needed for it to succeed. It can be used (PDF p. 567):
  - after receiving a query, to judge whether the request is feasible;
  - after initial plan generation, to judge whether the plan makes sense;
  - after each execution step, to see whether it is on track;
  - after the whole plan has run, to decide whether the task is done.
- Reflection and error correction are separate mechanisms that go together: reflection produces insights that expose errors to correct. Reflection can be done by the same agent via self-critique prompts, or by a separate component such as a specialized scorer, a model that outputs a concrete score for each outcome (PDF p. 567).
- ReAct (Yao et al., 2022) proposed interleaving reasoning and action, now a common agent pattern. "Reasoning" there covers both planning and reflection. At each step the agent explains its thinking (planning), acts, then analyzes observations (reflection), until it judges the task finished. The agent is typically prompted with examples to use the format Thought 1, Act 1, Observation 1, and so on, ending with Thought N and Act N: Finish [response] (PDF pp. 567-568).
- Figure 6-12 (PDF p. 570) shows a ReAct agent on a HotpotQA multi-hop question: "Aside from the Apple Remote, what other device can control the program Apple Remote was originally designed to interact with?" Thought 1 plans to search Apple Remote; Observation 1 says it was designed to control the Front Row media center program. Thought 2 plans to search Front Row; Act 2 Search[Front Row] finds nothing exact, only similar entries including "Front Row (software)". Thought 3 decides to search that; Observation 3 says it is a discontinued media center software. Thought 4 concludes it is controlled by an Apple Remote or the keyboard function keys, so Act 4 is Finish[keyboard function keys], marked correct. HotpotQA is a multi-hop question answering benchmark (Yang et al., 2018) (PDF p. 568).
- Reflection can be set up multi-agent: one agent plans and acts while another evaluates the outcome after each step or several steps (PDF p. 568).
- If the response failed, prompt the agent to reflect on why and how to improve, then produce a new plan from that suggestion, letting it learn from mistakes. Example: an evaluator finds generated code fails one third of test cases; the agent reflects that it ignored arrays of all negative numbers and produces new code that handles them (PDF pp. 568-569).
- This is the approach of Reflexion (Shinn et al., 2023), which splits reflection into two modules: an evaluator that scores the outcome and a self-reflection module that analyzes what went wrong. The authors call a plan a "trajectory", and after each evaluation and self-reflection the agent proposes a new trajectory (PDF pp. 570-571).
- Figure 6-13 (PDF p. 571) gives two Reflexion examples, each flowing task, trajectory, evaluation, reflection, next trajectory. Decision making: the task is to clean a pan and put it on the countertop; the trajectory takes the pan from stoveburner 1 and observes "Nothing happens" (and a following attempt to clean the pan at the sink basin also yields "Nothing happens"); a rule/LM heuristic evaluates it as hallucination; the reflection notes the pan was not in stoveburner 1; the next trajectory takes the pan from stoveburner 2 and succeeds. Programming: the task is a function match_parens over two strings of parentheses; the trajectory returns 'No' on a count check; self-generated unit tests fail; reflection says the code only checks that the total count of open and close parentheses is equal, not their order; the next trajectory returns 'Yes' if check(S1) or check(S2) else 'No'.
- Reflection is relatively easy to implement compared with plan generation and can give surprisingly good gains (PDF p. 571).

## Limitations and failure modes
- Reflection costs latency and money: thoughts, observations and sometimes actions consume many tokens, raising cost and user-perceived latency, especially on tasks with many intermediate steps. ReAct and Reflexion authors both used many prompt examples to enforce the format, which raises input-token cost and leaves less context for other information (PDF p. 571).
- Hallucination of function names and parameters, and guessing of missing parameters, are noted under plan generation (PDF pp. 558-559).
- Unvalidated plans can waste time and API spend (PDF p. 548).
- Non-sequential control flows are harder for models to generate and translate (PDF p. 566).
- Exact function names in plans are brittle when tool APIs change (PDF p. 563).

## Tool selection
- Tools often decide a task's success, so selection needs care; it depends on the environment, the task and also the model powering the agent. There is no foolproof guide, and the literature spans wide inventories: Toolformer (Schick et al., 2023) finetuned GPT-J to learn five tools, Chameleon (Lu et al., 2023) uses 13, and Gorilla (Patil et al., 2023) tried to prompt agents to choose the right API call among 1,645 APIs (PDF p. 572).
- More tools mean more capability but harder efficient use, like humans mastering many tools, and longer tool descriptions that may not fit the model's context (PDF p. 572).
- Decide by experiment and analysis (PDF pp. 572-573):
  - Compare agent performance with different tool sets.
  - Run an ablation study: if removing a tool causes no performance drop, drop the tool.
  - Look for tools the agent often gets wrong; if one is too hard (even extensive prompting and finetuning do not teach it), change the tool.
  - Plot the distribution of tool calls to see which are used most and least.
- Figure 6-14 (PDF p. 573) shows, for Chameleon with ChatGPT and with GPT-4, how often each tool was called in generated programs (light segment called, dark segment not called; the two numbers per bar sum to 100, but the page does not state the unit). On ScienceQA, called/not called: knowledge retrieval 72/28 (ChatGPT) and 81/19 (GPT-4); text detector 17/83 and 30/70; image captioner 10/90 and 6/94; query generator 2/98 and 11/89; Bing search 3/97 and 11/89. On TabMWP: row lookup 47/53 and 26/74; column lookup 4/96 and 6/94; table verbalizer 3/97 and 7/93; knowledge retrieval 16/84 and 25/75; program generator 71/29 and 72/28.
- Lu et al. conclude two things (PDF pp. 573-574): different tasks need different tools (ScienceQA relies much more on knowledge retrieval than TabMWP); and different models prefer different tools (GPT-4 selects a wider set than ChatGPT; ChatGPT leans toward image captioning, GPT-4 toward knowledge retrieval).
- Tip on frameworks: evaluate which planners and tools a framework supports, since frameworks focus on different categories. AutoGPT focuses on social media APIs (Reddit, X, Wikipedia) while Composio focuses on enterprise APIs (Google Apps, GitHub, Slack). Needs change, so also check how easily the agent can be extended with new tools (PDF p. 574).

### Tools built from tools
- Humans gain productivity by making ever more powerful tools from simpler ones; the book asks whether AI can do likewise. Chameleon proposes studying tool transition: after tool X, how likely is the agent to call tool Y? Frequently co-used tools can be merged into a bigger tool, and an agent aware of this could combine initial tools itself to build more complex ones (PDF p. 574).
- Figure 6-15 (PDF p. 575) is a tool transition graph from START to END with edge probabilities. From START: text_detector 0.3, knowledge_retrieval 0.53, query_generator 0.11, image_captioner 0.06. query_generator goes to bing_search 1.0. bing_search goes to solution_generator 0.97, knowledge_retrieval 0.02, image_captioner 0.01. image_captioner goes to knowledge_retrieval 0.79, solution_generator 0.21, query_generator 0.01. text_detector goes to knowledge_retrieval 0.78 and solution_generator 0.22. knowledge_retrieval goes to solution_generator 1.0, which goes to answer_generator 1.0, then END 1.0. (Edge labels were verified against the rendered image. The figure caption runs onto the tail page, PDF p. 576, as "CC BY 4.0.")
- Voyager (Wang et al., 2023) adds a skill manager that tracks newly acquired skills (tools) for reuse. Each skill is a coding program; when the manager judges a new skill useful, for example because it helped complete a task, it adds it to the skill library, conceptually like the tool inventory, to be retrieved for later tasks (PDF p. 576).
- The section closes by restating that an agent's success depends on its tool inventory and planning ability and that failure in either can sink it; the next section covers failure modes and evaluation (PDF p. 576).

## Relations
Builds on the tool categories and function-calling remark in C06-009, and on the agent overview in C06-008. Leads into agent failure modes and their evaluation (C06-011).
