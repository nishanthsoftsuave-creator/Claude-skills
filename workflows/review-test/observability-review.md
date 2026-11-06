---
name: observability-review
mode: review-test
rows: [C10-008, C10-009, C10-006]
---
# Observability review (monitoring, logs, traces, drift, alerting, orchestration, caches)

## When to use
Use when the task is to review whether an existing AI application can detect and diagnose its own failures in production: metrics, logs, traces, drift detection, alerting, the pipeline orchestrator and the system caches. Also use it after a failure diagnosis that ended with "we could not tell what happened". Production stays read-only: review configuration, dashboards, exported logs and staging runs; do not change anything.

## Inputs needed
Take from discovery (`../discovery.md`, Operations row) before asking the user anything: logging, tracing or metrics libraries; dashboards and alert rules (exports or config files); the orchestrator or chain code; cache code or config; the list of components (retrieval, guardrails, router, tools). Ask only for what is missing, per `../architect/intake.md`: where logs and traces can be read, whether a staging environment exists, and whether the user can supply an anonymised log sample. If none of these exist, the finding is that the system has no observability (see the CFR rule in Procedure).

## Modules to load
| Row | Module | Why it is needed here |
|---|---|---|
| C10-008 | [Monitoring and Observability](../../core/ai-engineering-building-applications-with-foundation-models/ch10-architecture-feedback/p877-monitoring-and-observability.md) | MTTD/MTTR/CFR, metric design from failure modes, logs, traces, drift sources |
| C10-009 | [AI Pipeline Orchestration](../../core/ai-engineering-building-applications-with-foundation-models/ch10-architecture-feedback/p890-ai-pipeline-orchestration.md) | what an orchestrator must do, how to judge one, parallelism, alerting on broken data flow |
| C10-006 | [Step 4. Reduce Latency with Caches](../../core/ai-engineering-building-applications-with-foundation-models/ch10-architecture-feedback/p871-step-4-reduce-latency-with-caches.md) | caches as a monitored component: hit rate, cost, leak and wrong-hit failure modes |

## Procedure
1. **Establish the three outcome metrics.** Ask for or find the team's MTTD (time to notice something bad), MTTR (time from detection to resolution) and CFR (percent of changes or deployments that cause a failure needing a fix or rollback). Decision rule: if the team does not know its CFR, the book says to redesign the platform to be more observable; record that as a finding, not as a question to defer. A high CFR does not by itself mean poor monitoring but says the evaluation pipeline should catch bad changes before deployment. The book gives no target values for MTTD, MTTR or CFR: judge them against the team's own requirement or its past baseline, never against a number from this workflow. `[C10-008]`
2. **Check that evaluation and monitoring share metrics.** Metrics used in evaluation should carry over into monitoring, and issues found in monitoring should flow back into the evaluation set. Absence of either direction is a `risk`. `[C10-008]`
3. **Derive the metric list from failure modes, not from a menu.** For each failure mode the application can have, name the metric that would catch it (hallucination: is the output inferable from the context; credit burn: input and output tokens per request plus cache cost and hit rate). A metric that serves no failure mode or opportunity is noise. `[C10-008]`
4. **Walk the book's metric families against what is tracked.** Mark each tracked, missing or not applicable. `[C10-008]`

   | Family | What to look for |
   |---|---|
   | Format failures | invalid-output rate (for JSON: how many are repairable) |
   | Open-ended quality | factual consistency and attributes such as conciseness, often via AI judges |
   | Safety | toxicity, private data in inputs and outputs, guardrail trigger rate, refusal rate, abnormal queries |
   | Conversational signals | stopped generations, turns per conversation, tokens per input and output, output-length distribution over time |
   | Per component | retrieval relevance and precision, vector store index size and query time |
   | Latency | time to first token, time per output token, total latency, tracked per user |
   | Cost | queries, token volume, requests per second against rate limits |
   | Business | correlation with north star metrics (DAU, session duration, subscriptions) |
5. **Check how metrics are computed.** Is it spot-check, exhaustive or a mix, and is that choice justified by cost and requirement? Can metrics be sliced by user, release, prompt or chain version, prompt type and time? A metric that cannot be sliced cannot locate a regression. `[C10-008]`
6. **Review logs.** The book's rule is to log everything because you cannot know what you will need. Expected content: configuration (model endpoint and name, temperature, top-p, top-k, stopping condition, prompt template); user query, final prompt, output and intermediate outputs; tool calls and outputs; component start and end times and crashes; tags and IDs on every entry. Also check log latency against the team's detection need: logs delayed longer than the issue window defeat response (the book's example is logs 15 minutes late against a 5-minute-old issue; it sets no required delay). The book also says to inspect production data manually every day, with AI-assisted log analysis for volume; check that someone does so on a regular cadence. `[C10-008]`
7. **Review traces.** A trace must link a request across components: actions taken, documents retrieved, final prompt, time per step, cost if measurable. Test: take one failed request and see whether the trace pinpoints the step (bad query processing, irrelevant context, wrong generation). If it cannot, say which step is invisible. `[C10-008]`
8. **Review drift detection for the three sources the book names.** System prompt changes (is there logic that detects a changed prompt, including via an upstream template), user behaviour changes (does anything watch for shifts such as falling response length, with root-cause investigation), and underlying model changes behind an unchanged API (does anything detect the change; the book names the risk, and INTERPRETATION: pinning the version or rerunning a regression set on a schedule are ways to detect it). The book's examples of model drift are dated 2023 studies; treat the principle, not the numbers, as current. `[C10-008]`
9. **Review alerting.** For each failure-mode metric, is there a threshold or anomaly alert, who receives it, and does the orchestrator alert when data flow breaks (component failure, data mismatch)? The book states only that the orchestrator ideally does the latter; whether a given orchestrator does is a fact to check, not assume. INTERPRETATION: threshold or anomaly alerts per failure-mode metric, with a named owner and tied to the team's detection target, are an operational adaptation, not a book rule. `[C10-009]`
10. **Review orchestration.** Components defined (models, data sources, tools, plus evaluation and monitoring tools registered), chaining described from query to task completion, step output format checked before the next step, parallelism where latency matters (for example routing and PII removal in parallel). Judge a chosen orchestrator on integration and extensibility, support for complex pipelines (branching, parallel work, error handling) and ease of use, performance and scalability, including hidden API calls or added latency. If the project adopted one early, note the book's advice to start without one and the cost in transparency; that is a `recommendation`, not a defect. The tool list in the book is dated. `[C10-009]`
11. **Review each cache as a monitored component.** For every exact or semantic cache found: are hit rate, cost and eviction behaviour monitored; are user-specific and time-sensitive queries excluded (or a classifier decides); is the cacheability decision based on whether the answer used user-specific retrieved data (INTERPRETATION, from the data-leak example); for a semantic cache, is the similarity threshold tuned against measured wrong hits (the book says tuning takes trial and error), is its value justified by hit rate, and are lookup latency and cost tracked as the cached set grows. INTERPRETATION: a cache that can serve one user's answer to another is the highest-severity item in this workflow (the book gives the leak scenario, not a severity). `[C10-006]`
12. **Report the gaps as findings with honest labels.** Static reading yields `REVIEWED` cases and `risk`, `recommendation` or `probable` findings. A `confirmed` finding needs a failing run record (for example a staging probe that shows a cache serving another user's answer). Anything needing production access you do not have is `BLOCKED` with the reason.

## Checks
| check | what is checked | how | evidence produced | type | criterion | how a failure is judged |
|---|---|---|---|---|---|---|
| OB-01 | MTTD, MTTR and CFR are known and recorded | ask user; read incident or deploy records supplied | notes with the values and their source | review | C10-008 | CFR unknown or unmeasured is a finding (platform should be redesigned to be observable) |
| OB-02 | Each known failure mode has a metric | read metric definitions and dashboards; map failure modes to metrics | table failure mode to metric | review | C10-008 | failure mode with no metric, or metric with no failure mode |
| OB-03 | Metric families covered (format, quality, safety, conversational, component, latency, cost) | code and config review, then search for the metric names | coverage table | review | C10-008 | a family relevant to the app is absent |
| OB-04 | Metrics sliceable by user, release, prompt version, time | read the metrics schema or labels | notes | review | C10-008 | key dimension missing |
| OB-05 | Log content and accessibility | read the logging code and a log sample; compare log delay with MTTD | log field checklist, delay figure | review | C10-008 | required fields missing (prompt, output, tool calls, config) or delay exceeds detection window |
| OB-06 | Log hygiene: no secrets or raw personal data in sample | SUPPLEMENTARY (hygiene; the book only says to log everything): run a pattern scan over the supplied sample via `python scripts/run_check.py --case OB-06 --evidence-dir <run>/evidence -- <scan command>`; the scan must print counts and line numbers only, never the matched text, because run_check redacts only common key shapes | exec record with counts | run | C10-008 | secrets or personal data found in logs (also report to user, do not copy values) |
| OB-07 | One failed request can be traced end to end | pick a failed request from staging or the sample; follow it through traces | notes naming the invisible step, if any | review | C10-008 | trace cannot show the failing step |
| OB-08 | Drift: system prompt change detection | read code for prompt hashing, diffing or version checks | notes | review | C10-008 | prompt can change with no detection |
| OB-09 | Drift: model version pinned or regression set scheduled | read provider config and scheduler or CI config | notes | review | C10-008 | unpinned model and no scheduled rerun |
| OB-10 | Drift: user behaviour metrics trended | read dashboards for length and turn trends | notes | review | C10-008 | no trend metrics |
| OB-11 | Alert rules exist, have owners and thresholds | read alert config (SUPPLEMENTARY: the book does not describe metric alerting; judged against the team's own detection need) | rule list | review | C10-008 | failure-mode metric without an alert or owner |
| OB-12 | Orchestrator alerts on broken data flow and validates step formats | read orchestrator code; optionally run the project's own pipeline tests through run_check.py | notes, or exec record | review (run only if the project has such tests) | C10-009 | silent failure when a component errors or a format mismatches |
| OB-13 | Orchestrator fit: extensibility, complex-pipeline support, hidden calls | read dependencies and trace a request for calls not in the chain | notes | review | C10-009 | hidden API calls or latency the team did not know about |
| OB-14 | Cacheability rules exclude user-specific and time-sensitive answers | read cache code and key construction | notes with cache key anatomy | review | C10-006 | key does not include user or permission scope for personalised answers |
| OB-15 | Cross-user cache leak probe (staging only, with approval) | with the user's recorded approval, two synthetic test users (fake data only) ask the same question after the first triggers a personalised answer; run through the project's own staging client via run_check.py, never production | exec records, both responses | run | C10-006 | second user receives first user's data: `confirmed`, severity critical |
| OB-16 | Cache hit rate, cost and eviction monitored; semantic cache threshold justified | read metrics and cache config | notes | review | C10-006 | cache invisible in monitoring, or semantic cache with no measured hit rate or wrong-hit rate |

## Evidence and exit gate
- A check typed `review (run only if ...)` is `REVIEWED` unless an exec record exists for its run part.
- Every case in the table has a status. Run cases need an exec record from `scripts/run_check.py`; review cases cite the files or exports read.
- Exit when each family and each drift source has a verdict (covered, partial, absent, not applicable) with evidence, and every `BLOCKED` item names what was missing.
- Never write `PASSED` for a review check. A finding that depends on an AI judge's output is capped at `probable` (`../../coverage/workflow-spec.md`, rule 4).
- Run `python scripts/validate_report.py <run_dir>` before reporting.

## Outputs
Cases and findings go into `results.json`; the report uses [../../templates/findings-report.md](../../templates/findings-report.md). Include a one-table observability coverage summary and the MTTD, MTTR and CFR values or the statement that they are unknown. Redesign suggestions are offered as a handoff, not performed.

## Pitfalls
- Treating dashboards as observability: metrics say something went wrong but not what; logs and traces are needed to find out `[C10-008]`.
- Metrics chosen because a tool provides them rather than from failure modes `[C10-008]`.
- Logs that arrive after the incident window, or that omit the final prompt and tool outputs `[C10-008]`.
- Assuming the model behind an API is unchanged `[C10-008]`.
- Adopting an orchestrator early so the pipeline becomes opaque `[C10-009]`.
- Caching a personalised answer as if it were generic, and trusting a semantic cache without measuring wrong hits `[C10-006]`.
- Figure 10-11's Bengals score is unverified in the module; do not quote it.
