---
name: inference-plan
mode: architect
rows: [C09-002, C09-003, C09-004, C09-006, C09-007, C10-006, C04-006]
---
# Inference plan: performance, cost and latency

## When to use
After the model and pattern are chosen (`model-selection.md`, `solution-pattern.md`) and before `architecture-design.md`. Use it whenever the design has a latency target, a cost ceiling, or a self-hosted model. If the model is reached only through a managed API, most of the model-level and service-level levers are the provider's job; the plan then shrinks to metrics, caching, batch-vs-online and cost per request `[C09-002]`.

## Inputs needed
Take from discovery and `intake.md`; ask only what is missing.
- Which latency numbers the user feels (first token, per-token, whole answer), and which are hard requirements versus nice to have `[C04-006]`.
- Expected volume and traffic shape, typical input and output length, and whether requests are interactive or can wait.
- Hosting: managed API, self-hosted, local. Hardware if self-hosted.
- Cost ceiling per request or per month. Treat any price, chip name or discount quoted from the modules as time-sensitive `[C09-004]`.

## Modules to load
| Row | Module | Why it is needed here |
|---|---|---|
| C09-002 | [Inference Overview](../../core/ai-engineering-building-applications-with-foundation-models/ch09-inference/p775-inference-overview.md) | Server vs service, compute-bound vs memory-bandwidth-bound, prefill vs decode, online vs batch APIs |
| C09-003 | [Inference Performance Metrics](../../core/ai-engineering-building-applications-with-foundation-models/ch09-inference/p784-inference-performance-metrics.md) | TTFT, TPOT, percentiles, throughput, goodput, MFU and MBU |
| C09-004 | [AI Accelerators](../../core/ai-engineering-building-applications-with-foundation-models/ch09-inference/p796-ai-accelerators.md) | Chip choice by FLOP/s, memory size and bandwidth, power |
| C09-006 | [Model Optimization](../../core/ai-engineering-building-applications-with-foundation-models/ch09-inference/p809-model-optimization.md) | Quantization, distillation, speculative decoding, KV cache, kernels |
| C09-007 | [Inference Service Optimization](../../core/ai-engineering-building-applications-with-foundation-models/ch09-inference/p833-inference-service-optimization.md) | Batching, prefill/decode split, prompt caching, parallelism |
| C10-006 | [Step 4. Reduce Latency with Caches](../../core/ai-engineering-building-applications-with-foundation-models/ch10-architecture-feedback/p871-step-4-reduce-latency-with-caches.md) | System-level exact and semantic caches |
| C04-006 | [Cost and Latency](../../core/ai-engineering-building-applications-with-foundation-models/ch04-eval-systems/p351-cost-and-latency.md) | Hard requirements, Pareto view, API vs self-hosting economics |

## Procedure
1. **Write the objective set before any lever.** List the metrics that matter and mark each hard requirement or nice to have. The book's method: if latency is non-negotiable, collect each candidate's latency, drop those that miss it, then choose among the rest (Pareto thinking) `[C04-006]`. Do not accept "lower latency" as a goal; nobody says no to it, and high latency is usually an annoyance rather than a deal breaker `[C04-006]`.
2. **Pick the metric that matters and state it exactly.** Use `latency = TTFT + TPOT x output tokens` `[C09-003]`. Rules:
   - Chat or streaming: set a TTFT target and a TPOT target; TPOT need only beat reading speed (about 120 ms per token, 6-8 tokens/s) `[C09-003]`.
   - Long-document summarisation: looser TTFT is tolerated `[C09-003]`.
   - Agent or chain-of-thought flows: measure time to publish (the first token the user actually sees), not model-side TTFT `[C09-003]`.
   - Report p50, p90, p95, p99, never the mean alone; plot TTFT against input length `[C09-003]`.
   - Where throughput gains cost latency, track goodput (requests meeting the SLO per second) `[C09-003]`.
   - Compare servers and hardware by cost per request, not raw tokens/s, because token counts depend on the tokenizer `[C09-003]`.
3. **Decide who owns inference.** Managed API: provider runs the serving stack, so API users do not implement most of Chapter 9's techniques `[C09-002]`. INTERPRETATION: what stays with you is input and output length (prompt for concision, stopping conditions `[C04-006]`; an output token costs roughly 2-4x an input token across providers and drives latency `[C09-006]`), system caching, and the online-vs-batch API choice. Self-hosted: you own the server, so continue with steps 4-8 `[C09-002]`. With an API, cost per token barely falls with scale; with a cluster it can fall sharply, so revisit API vs self-hosting at each scale step `[C04-006]`.
4. **Choose online or batch.** Online APIs optimise latency; batch APIs optimise cost and suit work with no strict latency need (synthetic data, periodic reports, reindexing, reprocessing after a model change) `[C09-002]`. Customer-facing chat and code generation need online `[C09-002]`. Streaming cuts the wait for the first token but the response cannot be scored before the user sees it, so pair it with the output-guardrail decision in `architecture-design.md` `[C09-002]`.
5. **Find the bottleneck.** Prefill is compute-bound; decode is memory-bandwidth-bound; autoregressive LLM serving is usually memory-bandwidth-bound; image generators are usually compute-bound `[C09-002]`. Long context tends to push toward memory-bandwidth-bound `[C09-002]`. If you can measure, use MFU (observed over peak-FLOP/s throughput) and MBU (see Pitfalls for the formula), not the GPU utilisation figure, which can read 100% at very low efficiency `[C09-003]`. Compute-bound workloads show higher MFU and lower MBU; bandwidth-bound the reverse `[C09-003]`. If you cannot measure yet, record the bottleneck as an assumption and make the first milestone a measurement.
6. **Pick levers by bottleneck.** INTERPRETATION: the row order is a reading aid, not a ranking the book gives; the book says production usually combines levels `[C09-006]`. Commonly used and low effort: weight-only quantization ("by far the most popular") and distillation; pruning is uncommon (harder, smaller gains, sparse hardware support needed) `[C09-006]`.

| Bottleneck / goal | Levers | Source |
|---|---|---|
| Compute-bound | more chips, higher FLOP/s chips | `[C09-002]`, `[C09-004]` |
| Memory-bandwidth-bound | higher-bandwidth chips, fewer bytes per parameter (weight-only quantization), distillation | `[C09-004]`, `[C09-006]` |
| Slow decode (sequential tokens) | speculative decoding (no quality change, needs a draft model sharing the tokenizer; best on structured text such as code), inference with reference (when output copies input: RAG, code edit), parallel decoding (harder to implement) | `[C09-006]` |
| Long context or large batch | KV cache budget, PagedAttention-style cache management, attention redesign (only at training or finetuning time) | `[C09-006]` |
| Throughput and cost | continuous batching (returns each response as soon as done), dynamic batching with a time window | `[C09-007]` |
| Prefill and decode interfering | split them onto separate instances; ratio by workload (long input plus TTFT priority 2:1 to 4:1; short input plus TPOT priority 1:2 to 1:1) | `[C09-007]` |
| Repeated prompt prefix | prompt caching (system prompt, long document, long chat) | `[C09-007]` |
| Model too big for one device | tensor parallelism; avoid pipeline parallelism when latency is strict; replicas for concurrency | `[C09-007]` |
| Repeated or slow-to-compute queries | system caches (step 8) | `[C10-006]` |

7. **Size memory before choosing batch and context.** KV cache bytes = 2 x batch x sequence length x layers x model dimension x bytes per value `[C09-006]`. Worked check from the book: 13B model, 40 layers, dimension 5,120, batch 32, 2,048 tokens, 2 bytes gives about 54 GB `[C09-006]`. Compare with accelerator memory and its hierarchy (CPU DRAM, GPU HBM, on-chip SRAM) `[C09-004]`. Three questions for hardware: can it run the workload, how long does it take, what does it cost `[C09-004]`. For owned hardware, cost is purchase price plus power; cloud pricing is usage-based `[C09-004]`. Quantization and distillation can change behaviour, so any model-level lever needs a re-run of the eval plan (`eval-plan.md`) `[C09-006]`. Service-level levers should not change output quality `[C09-007]`.
8. **Decide system caching.** Exact cache: for repeated identical requests and slow steps (retrieval, SQL, web search); set an eviction policy and storage tier `[C10-006]`. Do not cache user-specific or time-sensitive answers; a classifier can decide `[C10-006]`. Semantic cache: only if hit rate is high enough to justify extra failure points (embeddings, vector search, similarity threshold) `[C10-006]`. INTERPRETATION: decide cacheability from whether the answer used user-specific retrieved data, not from how the question reads, because of the cross-user leak case `[C10-006]`. Inference-level KV and prompt caches are provider-side with an API; check the offered discount before building one `[C09-007]`.
9. **Write targets with their levers** into the architecture template section 5 and a decision record per lever chosen.

## Evidence and exit gate
Done when: every metric has a target, percentile and hard/nice flag; the bottleneck is stated as measured or assumed; each lever has an expected effect and a re-evaluation trigger; cost per request is estimated as prefill plus decode cost `[C09-003]`; caching choices name what is and is not cached. Mark book example numbers (prices, discounts, chip specs) as time-sensitive, never as current `[C09-007]`.

## Outputs
Fill `../../templates/architecture-design.md` section 5 (Operations) and one `../../templates/decision-record.md` per lever. Hand targets to `ops-cost-feedback.md` for monitoring.

## Pitfalls
- Judging by averages: one 3,000 ms outlier turned a ~100 ms service into a 390 ms mean `[C09-003]`.
- Trusting nvidia-smi utilisation `[C09-003]`; comparing tokens/s across tokenizers `[C09-003]`.
- Quantising or distilling without re-evaluating quality `[C09-006]`.
- Semantic caching adopted without hit-rate evidence, or caching personalised answers `[C10-006]`.
- Batching to cut cost while breaking the TTFT/TPOT target `[C09-003]`, `[C09-007]`. Note: C09-007 prints that batching "reduces" throughput; the module flags this as a slip (batching raises throughput and cost-efficiency, can lengthen each request's latency). Rely on the C09-003 trade-off (batching improves throughput, hurts latency), not the printed wording.
- Using MBU without the formula: bandwidth used = parameters x bytes per parameter x tokens/s; the book's printed MBU denominator is clipped, so INTERPRETATION: divide by the chip's peak bandwidth (book example: 7B FP16 at 100 tokens/s = 700 GB/s, 70% of a 2 TB/s chip) `[C09-003]`.
- Building prompt caching when the API already offers it `[C09-007]`.
- Citing a chip, price or discount from the book as current `[C09-004]`.
