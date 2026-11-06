---
id: C10-008
title: Monitoring and Observability
source_pages: "877-889"
chapter: 10
concepts: [observability, monitoring, mttd, mttr, change-failure-rate, metrics-design, logging, tracing, drift-detection, north-star-metrics, latency-metrics]
related: [C10-007, C10-009, C09-003, C06-011]
time_sensitive: true
---
# Monitoring and Observability
(Source: PDF pp. 877-889; the section's last drift item, underlying model changes, and the heading that starts the next section appear on tail PDF p. 890)

## What the section covers
Why observability must be designed into an AI product, how to judge it (MTTD, MTTR, CFR), the difference between monitoring and observability, what metrics to track for foundation-model applications, logging, tracing (with the LangSmith trace figure), and drift detection. The book skips general observability practice (a large established industry) and concentrates on what is distinctive for foundation-model applications; the book's GitHub repository holds further observability resources (PDF p. 878). The metrics part is a recap of quality metrics covered earlier (Chapters 4-6 and 3, 5 for computation) (PDF p. 881).

## Figure 10-10 (printed at the top of PDF p. 877)
The figure shows the full architecture with write actions: the Figure 10-9 platform (input cache, context construction, read-only actions plus cache plus databases, input guardrails, model gateway with routing/generation/scoring, output guardrails) plus a highlighted "Write actions" box (examples: update orders, send emails) fed from the output side. The final response goes back to the user, and a line also loops back to context construction (PDF p. 877). The accompanying text says a system built through all the steps has become complex: more capability, but more failure modes and harder debugging, hence the need for observability (PDF p. 877).

## Why it matters
- Observability should be integral to product design, not an afterthought; the more complex the product, the more crucial it is (PDF p. 877).
- Monitoring has the same goal as evaluation: reduce risk and find opportunities. Risks include application failures, security attacks and drifts; opportunities include improvement and cost savings. It also supports accountability by giving visibility into system performance (PDF p. 878).

## Evaluating observability: three DevOps metrics
- **MTTD (mean time to detection)**: how long it takes to notice that something bad has happened.
- **MTTR (mean time to response)**: how long, after detection, resolution takes.
- **CFR (change failure rate)**: the percentage of changes or deployments that cause failures needing fixes or rollbacks. If you do not know your CFR, the book says to redesign the platform to be more observable (PDF p. 878).
- A high CFR does not by itself mean poor monitoring, but it signals that the evaluation pipeline should be rethought so bad changes are caught before deployment (PDF p. 879).
- Evaluation and monitoring must work closely: evaluation metrics should carry over to monitoring metrics (a model that does well in evaluation should do well in monitoring), and issues found in monitoring should be fed back into the evaluation pipeline (PDF p. 879).

## Monitoring versus observability (sidebar, PDF p. 880)
- Since the mid-2010s the industry prefers "observability". Monitoring assumes nothing about the link between a system's internal state and its outputs: you watch external outputs to learn that something is wrong inside, with no guarantee they will show what.
- Observability assumes more: internal states can be inferred from external outputs. When an observable system misbehaves, logs and metrics should reveal what went wrong without shipping new code. It means instrumenting the system so enough runtime information is collected and analysed.
- The book's usage: "monitoring" is the act of tracking system information; "observability" is the whole process of instrumenting, tracking and debugging.

## Metrics

### Principles
- Metrics are not the goal; most companies do not care about an output relevancy score unless it serves a purpose, which is to flag problems and show opportunities (PDF p. 881).
- Start from the failure modes you want to catch and design metrics around them. Examples: to detect hallucination, check whether outputs can be inferred from the context; to avoid burning API credit, track input and output tokens per request, and the cache's cost and hit rate (PDF p. 881).
- Open-ended generation means many ways to fail. Metric design takes analytical thinking, statistical knowledge and often creativity, and is highly application-specific (PDF p. 881).

### What to track (PDF pp. 882-883)
- **Format failures** are the easiest to track. For JSON output, count how often it is invalid and, of those, how many are easily repairable (a missing closing bracket is easy, missing expected keys is harder) (PDF p. 882).
- **Open-ended generation**: factual consistency and quality attributes such as conciseness, creativity or positivity, many computable with AI judges (PDF p. 882).
- **Safety**: toxicity metrics; private or sensitive information in inputs and outputs; how often guardrails trigger and how often the system refuses; abnormal queries, which can expose edge cases or prompt attacks (PDF p. 882).
- **User feedback and conversational signals** as proxies for quality (PDF pp. 882-883): how often users stop a generation midway; average turns per conversation; average tokens per input (are users doing more complex tasks, or learning to write tighter prompts?); average tokens per output (are some models more verbose, do certain query types draw long answers?); the output-token distribution and how it shifts over time (is the model becoming more or less diverse?).
- Length metrics also matter for latency and cost, since longer contexts and responses usually raise both (PDF p. 883).
- **Per-component metrics**: in RAG, retrieval quality via context relevance and context precision; a vector database via the storage needed to index data and the query time (PDF p. 883).
- **Correlate with north star metrics** such as DAU, session duration (time actively engaged) or subscriptions. Strongly correlated metrics may suggest ways to move the north star; uncorrelated ones suggest what not to optimise (PDF p. 883).
- **Latency** (details in Chapter 9): time to first token (TTFT), time per output token (TPOT) and total latency, tracked per user to see scaling with more users (PDF p. 884).
- **Cost**: number of queries and input/output token volume, such as tokens per second (TPS). With rate-limited APIs, track requests per second to stay within allocated limits and avoid service interruption (PDF p. 884).

### How to compute them
- Choose between **spot checks** (sample a subset to find problems quickly) and **exhaustive checks** (evaluate every request for a full view). The choice depends on requirements and resources; a mix gives balance (PDF p. 884).
- Make metrics sliceable by users, releases, prompt/chain versions, prompt/chain types and time, to understand variation and locate specific problems (PDF p. 885).

## Logs and traces

### Logs
- Metrics are aggregated summaries; they cannot answer questions like "has this happened before?" after a spike. Logs are an append-only record of events and can (PDF p. 885).
- Debugging flow in production (PDF p. 885): (1) metrics say something went wrong five minutes ago but not what; (2) read the logs around that time to find out what happened; (3) correlate log errors with the metrics to confirm the right issue was found.
- Speed requirements: metrics must be computed quickly for fast detection; logs must be readily accessible for fast response. With logs delayed 15 minutes, a 5-minute-old issue cannot be investigated until they arrive (PDF p. 886).
- General rule: log everything, since you cannot know what you will need. Log configuration (model API endpoint, model name, sampling settings such as temperature, top-p, top-k, stopping condition, and the prompt template); the user query, the final prompt sent to the model, the output and intermediate outputs; any tool calls and their outputs; component start and end times and crashes. Tag each entry and give it IDs so its origin in the system is known (PDF p. 886).
- Log volume grows fast; many log-analysis and anomaly-detection tools are AI-powered. Even so, inspect production data manually every day to see how users really use the application. Shankar et al. (2024) found that developers' ideas of good and bad outputs change as they see more data, letting them rewrite prompts and update the evaluation pipeline to catch bad responses (PDF pp. 886-887).

### Traces
- Logs are disjointed events; a trace links related events into a complete timeline of a transaction, a detailed record of a request's path through components and services (PDF p. 887).
- In an AI application a trace should show the whole process from user query to final response: actions taken, documents retrieved, the final prompt sent to the model, time per step and cost if measurable (PDF p. 887).
- Ideal: follow each query's transformation step by step, and when it fails, pinpoint the step: wrongly processed query, irrelevant retrieved context, or wrong model generation (PDF p. 887).
- **Figure 10-11** (PDF p. 888), a LangSmith request trace. The right panel is a "run tree" with a top-level Chain AgentExecutor (about 13.57 s, 5,271 tokens). Beneath it, in order: a LLMChain (1.46 s, 144 tokens) containing a ChatOpenAI call (0.88 s, 144 tokens); a Search tool call (2.87 s); a second LLMChain (1.97 s, 2,037 tokens) containing ChatOpenAI (0.88 s, 2,037 tokens); a second Search tool call (3.50 s); a third LLMChain (2.07 s, 3,090 tokens) containing ChatOpenAI (2.48 s, 3,090 tokens). Behind it a panel shows the human input (asking how many more points were scored in the 2023 Super Bowl than the 2022 one) and the AI output (a final answer giving the two scores and a 15-point difference), with total tokens 5,271. Point: a trace gives timing and token counts per step, so slow or costly steps can be found. The panels overlap, so the answer text is clipped at its right edge. Legible in the rendered page: the 2023 game's final score read as Kansas City Chiefs 38, Philadelphia Eagles 35; the 2022 game's as Los Angeles Rams 23, Cincinnati Bengals (their score is clipped; UNVERIFIED: its value, though the text states 15 more points in 2023); a left sidebar shows counters 23 and 8.

## Drift detection
More parts mean more things that can change. Three drift sources are named (PDF p. 889, continuing onto the tail page):
- **System prompt changes**: the prompt can change without your knowing, for example when a template it builds on is updated or a coworker fixes a typo. Simple logic is enough to detect that the system prompt changed (PDF p. 889).
- **User behaviour changes**: users adapt to technology. People learned how to phrase Google queries or optimise pages for search ranking, and residents near self-driving cars learned to bully them into yielding (Liu et al., 2020). Users may, for example, learn to ask for concise answers, producing a gradual fall in response length. Metrics alone may not show the cause, so investigation is needed to find the root cause (PDF pp. 889-890).
- **Underlying model changes**: through an API the interface can stay the same while the model behind it is updated, often undisclosed (see Chapter 4), leaving you to detect it. Chen et al. (2023) saw notable benchmark differences between March and June 2023 versions of GPT-4 and GPT-3.5; Voiceflow reported a 10% performance drop moving from GPT-3.5-turbo-0301 to GPT-3.5-turbo-1106 (PDF p. 890).

## Alternatives and trade-offs
Spot versus exhaustive checks (cost against coverage); log everything versus log volume that cannot be read by hand (AI-assisted analysis plus daily manual sampling); aggregated metrics (quick, coarse) versus logs and traces (detailed, need to be available quickly).

## Time-sensitive statements
The model version names and the 2023 comparisons (GPT-4/GPT-3.5 March vs June 2023; Voiceflow's 10% drop) are dated examples; the principles are not.

## Relations
Follows the agent-patterns step whose added complexity motivates it (C10-007); the next section, pipeline orchestration, is C10-009. Latency metrics are defined in C09-003; agent failure modes and evaluation in C06-011.
