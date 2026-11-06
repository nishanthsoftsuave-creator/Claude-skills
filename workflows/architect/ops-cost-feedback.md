---
name: ops-cost-feedback
mode: architect
rows: [C01-018, C10-008, C10-011, C10-012, C10-013, C04-006, C09-003]
---
# Operations: monitoring, observability, feedback and maintenance

## When to use
After `architecture-design.md`, `eval-plan.md` and `inference-plan.md`. It fills section 5 (Operations) of the architecture template. Also use it alone when the user asks how to monitor, collect feedback or keep an AI product healthy.

## Inputs needed
Components in the design (more components mean more failure points `[C10-008]`). Metrics and thresholds from the eval plan. Cost and latency targets from `inference-plan.md`. Product type (conversational, integrated into a workflow, standalone), user base size, privacy constraints, who is on call. Ask only what discovery did not answer (`intake.md`).

## Modules to load
| Row | Module | Why it is needed here |
|---|---|---|
| C01-018 | [Maintenance](../../core/ai-engineering-building-applications-with-foundation-models/ch01-intro/p088-maintenance.md) | Planning for change after launch |
| C10-008 | [Monitoring and Observability](../../core/ai-engineering-building-applications-with-foundation-models/ch10-architecture-feedback/p877-monitoring-and-observability.md) | Metrics, logs, traces, drift |
| C10-011 | [Extracting Conversational Feedback](../../core/ai-engineering-building-applications-with-foundation-models/ch10-architecture-feedback/p895-extracting-conversational-feedback.md) | Explicit and implicit feedback signals |
| C10-012 | [Feedback Design](../../core/ai-engineering-building-applications-with-foundation-models/ch10-architecture-feedback/p907-feedback-design.md) | When and how to collect |
| C10-013 | [Feedback Limitations](../../core/ai-engineering-building-applications-with-foundation-models/ch10-architecture-feedback/p921-feedback-limitations.md) | Biases and degenerate loops |
| C04-006 | [Cost and Latency](../../core/ai-engineering-building-applications-with-foundation-models/ch04-eval-systems/p351-cost-and-latency.md) | Which cost and latency numbers to track |
| C09-003 | [Inference Performance Metrics](../../core/ai-engineering-building-applications-with-foundation-models/ch09-inference/p784-inference-performance-metrics.md) | Exact definitions for latency, throughput, utilisation |

## Procedure
1. **Design observability in, not on.** The more complex the product, the more crucial it is `[C10-008]`. Monitoring has the same goal as evaluation: reduce risk (failures, attacks, drift) and find opportunities (improvement, cost savings) `[C10-008]`. Metrics carry over from the eval plan, and issues found in production flow back into the evaluation set `[C10-008]`.
2. **Set three health measures for the process** and record the current value or "unknown": MTTD (time to detect), MTTR (time to respond), CFR (change failure rate). If CFR is unknown, redesign for observability; a high CFR means rethinking the evaluation pipeline so bad changes are caught before deployment `[C10-008]`.
3. **Design metrics from failure modes.** For each failure mode named in the eval plan and guardrail design, choose one metric that would catch it `[C10-008]`. Candidate set (the book's list; keep those that catch a failure mode of this product):
   - Format failures (invalid output rate, repairable share) `[C10-008]`.
   - Factual consistency and quality attributes, often judge-computed (limits in `eval-plan.md`) `[C10-008]`.
   - Safety: toxicity, sensitive data in inputs and outputs, guardrail trigger rate, refusal rate, abnormal queries `[C10-008]`.
   - Conversational signals as proxies: stopped generations, turns per conversation, tokens per input and output and their drift `[C10-008]`.
   - Per-component metrics: retrieval context relevance and precision, vector store size and query time `[C10-008]`.
   - Latency: TTFT, TPOT and total, tracked per user `[C10-008]`; report percentiles (p50, p90, p95, p99) rather than the mean, and measure what the user sees (with hidden plan or tool steps, the user's TTFT is later than the model's; "time to publish") using the definitions in `[C09-003]`; targets and the must-have versus nice-to-have split come from `[C04-006]` and `inference-plan.md`. Where throughput is traded for latency, goodput (requests per second that meet the latency targets) shows it `[C09-003]`. For self-hosted serving, judge hardware efficiency by MFU and MBU, not nvidia-smi utilisation `[C09-003]`.
   - Cost: query count, input and output token volume, cache cost and hit rate, requests per second against rate limits `[C10-008]`. Compare cost per request, not raw tokens per second across models, since token counts depend on the tokenizer `[C09-003]`. Per-token API cost barely falls with scale while self-hosted cost can, so revisit API versus self-hosting as volume changes `[C04-006]`.
   - Correlate metrics with north-star metrics (daily active users, session duration, subscriptions); drop metrics that correlate with nothing `[C10-008]`.
4. **Decide computation and slicing.** Spot checks (sample) versus exhaustive checks (every request), or a mix, by cost and risk `[C10-008]`. Make every metric sliceable by user, release, prompt or chain version, type and time `[C10-008]`.
5. **Specify logs and traces.** Log everything you may later need: configuration (endpoint, model, sampling settings, prompt template), query, final prompt, output, intermediate outputs, tool calls and outputs, component timings and crashes, each tagged with IDs `[C10-008]`. Logs must be quickly accessible (a 15-minute delay blocks response to a 5-minute-old issue) `[C10-008]`. Add traces that link events end to end (query to final response, retrieved documents, final prompt, time and cost per step) so a failure can be pinned to query processing, retrieval or generation `[C10-008]`. Plan a daily manual look at production data; ideas of good and bad outputs shift as people see data `[C10-008]`. Apply the secrets and PII rules from `architecture-design.md` to what is logged (INTERPRETATION).
6. **Detect drift.** Three sources: system prompt changes (detect with simple change logic), user behaviour change (investigate root cause), and underlying model change behind an unchanged API (the book cites measured benchmark differences between versions) `[C10-008]`. INTERPRETATION: pin model versions where the provider allows and re-run the evaluation set on a schedule to catch it. INTERPRETATION: version prompts and judges too, since an unnoticed judge change can look like a product change.
7. **Choose feedback signals.** Explicit (thumbs, ratings): easy to read, sparse, biased toward unhappy users. Implicit (inferred from actions): abundant, noisy `[C10-011]`. For conversational products consider: early termination, error correction and rephrasing, "Are you sure?" requests, user edits (each edit is a preference pair), complaints and sentiment, refusals, regeneration, conversation organisation, length and diversity `[C10-011]`. Most signals have both positive and negative readings by application (long conversations: good for companions, bad for support); treat them as hypotheses to validate by data analysis and user studies `[C10-011]`. State the use of each signal: evaluation metrics, development data, or personalisation `[C10-011]`.
8. **Design collection.** Choose moments: onboarding (optional, with a neutral default), when something goes wrong (let the user finish the task, hand off to a human), when the model is unsure (offer options if latency allows), and optionally when something good happens (the book gives two views: Apple's guideline advises against asking, practitioners want to flag amazing moments; if asked, limit exposure, for example to 1% of users, accepting more bias) `[C10-012]`. Give users an incentive to give good feedback `[C10-012]`. Make feedback part of the workflow, low effort, easy to ignore `[C10-012]`. Decide consent for capturing context (service agreement or data donation) and tell users how feedback is used `[C10-012]`. Test the feedback UI for ambiguity; decide public or private visibility deliberately; never ask users to judge what they cannot judge `[C10-012]`.
9. **Plan for feedback bias.** Check the rating distribution for leniency; vary option position or model position effect; treat random clicks and length preference as noise; guard against degenerate loops (the system only gets feedback on what it shows; amplified bias, "cat haven" drift); do not train directly on raw feedback without checking for sycophancy `[C10-013]`.
10. **Write the maintenance plan.** The product keeps changing after launch: the field moves fast, prices fall, providers converge on APIs, regulation and IP rules shift `[C01-018]`. Commit to: versioning and evaluation infrastructure so a model swap is testable; a periodic cost-benefit and build-versus-buy review (the book's examples: providers halved prices after an in-house build; a third-party provider failed); a watch on regulation, compute availability and IP exposure; update cadence and owner. INTERPRETATION: tie each review to a trigger (price change, drift alert, CFR rise) as well as a calendar date `[C01-018]`.

## Evidence and exit gate
Done when each failure mode has a metric, an alert owner and an action; MTTD, MTTR and CFR have a baseline or an explicit "not measured yet" with a milestone; the log and trace fields are listed; each feedback signal has an interpretation hypothesis and a bias check; maintenance has owners and triggers. Anything not decided becomes an open question in the template's risk section.

## Outputs
Fill section 5 of `../../templates/architecture-design.md` and add the monitoring metrics to `../../templates/eval-plan.md` section 6. One `../../templates/decision-record.md` for feedback collection design if it affects the UI.

## Pitfalls
- Metrics chosen because they are easy, not because they catch a failure `[C10-008]`.
- Averaging latency; ignoring user-observed versus model-observed time `[C09-003]`.
- Delayed logs; logging too little context to debug `[C10-008]`.
- Ignoring silent upstream model changes `[C10-008]`.
- Reading regenerate, share or long chats as always bad or always good `[C10-011]`.
- Intrusive or ambiguous feedback prompts (the book's reversed emoji scale) `[C10-012]`.
- Using feedback to retrain without handling leniency, position bias and loops `[C10-013]`.
- Treating launch as done, with no review of cost, vendor and regulation `[C01-018]`.
- INTERPRETATION: tracking cost only as a monthly bill instead of per request and per component (the book lists per-request token and cache metrics `[C10-008]`).
