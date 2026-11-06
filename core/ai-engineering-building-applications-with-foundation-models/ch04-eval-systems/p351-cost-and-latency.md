---
id: C04-006
title: Cost and Latency
source_pages: "351-354"
chapter: 4
concepts: [cost, latency, pareto-optimization, time-to-first-token, tokens-per-minute, self-hosting, api-pricing, hard-requirements, model-selection-criteria]
related: [C04-005, C04-007, C04-008, C04-009]
time_sensitive: true
---
# Cost and Latency
(Source: PDF pp. 351-354, with the end of Table 4-3 on the tail page 355)

## What the section covers
Why quality must be balanced against speed and price, the latency metrics to distinguish, what drives latency and cost for API use versus self-hosting, how scale changes the economics, and Table 4-3, an example set of selection criteria for a fictional application. Detailed optimization is deferred to Chapter 9 (PDF p. 351).

## Meaning and why it matters
- A model that writes excellent outputs but is too slow or expensive is not useful, so evaluation balances quality, latency and cost. Many companies pick a lower-quality model for better cost and latency (PDF p. 351).
- Optimizing several objectives at once is a field called Pareto optimization. Be explicit about which objectives you can and cannot compromise on. If latency is non-negotiable, collect each model's latency expectations, drop those that miss the requirement, then choose the best among the remainder (PDF p. 351).

## Latency
- Foundation-model latency has several metrics: time to first token, time per token, time between tokens, time per query, and others. Know which matter to you (PDF p. 351).
- Latency depends on the model, the individual prompt and the sampling variables. Autoregressive models generate token by token, so more output tokens means more total latency. You can influence it by prompting for concision, setting a generation stopping condition (Chapter 2) or other techniques (Chapter 9) (PDF p. 352).
- Tip: separate must-have from nice-to-have. Nobody answers no to "do you want lower latency?", but high latency is usually an annoyance rather than a deal breaker (PDF p. 352).

## Cost
- Model APIs normally charge per token, so more input and output tokens cost more; many applications therefore try to cut token counts (PDF p. 352).
- When you host your own models, apart from engineering cost, the cost is compute. To use machines well, people often choose the largest model that fits. GPUs commonly have 16, 24, 48 or 80 GB of memory, so popular models tend to max out those sizes; the book says it is no coincidence that many models have 7 billion or 65 billion parameters (PDF p. 352).
- Scaling: with an API, cost per token generally does not shrink much as you grow. With self-hosting it can fall sharply. If you have invested in a cluster that serves up to 1 billion tokens a day, compute cost is the same at 1 million or 1 billion tokens a day. So at different scales companies should reconsider API versus self-hosting (PDF p. 353).
- Scale (row in the table) matters particularly when evaluating APIs, because the service must support your volume (PDF p. 353).

## Example criteria (Table 4-3, a fictional application)
Columns: criteria, metric, benchmark, hard requirement, ideal (PDF pp. 354-355).
- Cost: cost per output token; benchmark column marked X (none); hard requirement under $30.00 per 1M tokens; ideal legible only as "< $15" followed by a cut-off "1M t..." (PDF p. 354).
- Scale: tokens per minute (TPM); benchmark marked X; hard requirement over 1M TPM; ideal legible only as "> 1M" (PDF p. 354).
- Latency: time to first token at P90 on an internal user-prompt dataset, under 200 ms; time per total query at P90, under 1 minute (PDF p. 354).
- Overall model quality: Elo score from Chatbot Arena ranking, over 1200 (PDF p. 354).
- Code generation: pass@1 on HumanEval, over 90% (PDF p. 354).
- Factual consistency: an internal GPT-based metric on an internal hallucination dataset, over 0.8 hard, over 0.9 ideal (PDF p. 355).
- Legible parts of the Ideal column on p. 354 (verified on the rendered page): time to first token "< 100" (unit cut off, presumably ms), total query time "< 30s", Elo "> 125" (last digit(s) cut off), pass@1 "> 95" with the percent sign partly cut. Only the factual-consistency row (p. 355) shows its ideal in full.
- UNVERIFIED: the Ideal column is cut off at the page edge in the PDF itself, so the full values for the cost, scale, time-to-first-token, Elo and pass@1 rows are not recoverable from this copy.
- The book then says that with criteria defined, the next step is to use them to select the best model (PDF p. 355).

## Time-sensitive statements
The GPU memory sizes, the 7B/65B parameter remark and the example thresholds reflect the book's time of writing; Table 4-3 is only an illustration, not a recommendation.

## Relations
Follows instruction-following (C04-005). Leads into Model Selection (C04-007, C04-008) and the API-versus-host question (C04-009); the per-token versus compute cost shift is revisited there.
