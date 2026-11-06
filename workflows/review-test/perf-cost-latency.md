---
name: perf-cost-latency
mode: review-test
rows: [C09-002, C09-003, C09-004, C09-006, C09-007, C04-006, C10-006]
---
# Performance, cost and latency review

## When to use
The user asks whether an AI system is fast enough or cheap enough, why latency or spend is high, or what to optimize. Run after `system-understanding.md` so the components, models and hosting mode are known. If every model is a managed API, most of Chapter 9 is provider-side; the review then focuses on token counts, caching, batch versus online use, and model choice `[C09-002]`.

## Inputs needed
- Hosting mode per model: managed API, third-party inference service, or self-hosted (and on which accelerator). Discovery usually answers this; ask only if it does not.
- Latency and cost targets per application, split into hard requirements and nice-to-haves `[C04-006]`. If none exist, record that as a finding and propose targets, never invent them.
- Real traffic data (logs, traces, billing export) or permission to run a probe. A paid probe needs the user's approval and a stated spend cap (see Safety below).

## Modules to load
| Row | Module | Why it is needed here |
|---|---|---|
| C09-002 | [Inference Overview](../../core/ai-engineering-building-applications-with-foundation-models/ch09-inference/p775-inference-overview.md) | compute-bound vs memory-bound, prefill vs decode, online vs batch APIs |
| C09-003 | [Inference Performance Metrics](../../core/ai-engineering-building-applications-with-foundation-models/ch09-inference/p784-inference-performance-metrics.md) | TTFT, TPOT, percentiles, throughput, goodput, MFU/MBU, cost per request |
| C09-004 | [AI Accelerators](../../core/ai-engineering-building-applications-with-foundation-models/ch09-inference/p796-ai-accelerators.md) | FLOP/s, memory size and bandwidth, accelerator selection |
| C09-006 | [Model Optimization](../../core/ai-engineering-building-applications-with-foundation-models/ch09-inference/p809-model-optimization.md) | quantization, distillation, speculative decoding, KV cache levers |
| C09-007 | [Inference Service Optimization](../../core/ai-engineering-building-applications-with-foundation-models/ch09-inference/p833-inference-service-optimization.md) | batching, prefill/decode decoupling, prompt caching, parallelism |
| C04-006 | [Cost and Latency](../../core/ai-engineering-building-applications-with-foundation-models/ch04-eval-systems/p351-cost-and-latency.md) | criteria, hard vs nice-to-have, API vs self-hosting economics |
| C10-006 | [Step 4. Reduce Latency with Caches](../../core/ai-engineering-building-applications-with-foundation-models/ch10-architecture-feedback/p871-step-4-reduce-latency-with-caches.md) | exact and semantic system caches and their leak risk |

## Procedure
1. **Fix the targets.** List each application's objectives (quality, latency, cost, scale) and mark which are hard requirements. Quality, latency and cost are traded off (Pareto); with a non-negotiable latency, drop models that miss it, then choose among the rest `[C04-006]`. Use user-visible latency: with chain-of-thought or agent steps the user's first visible token comes later than the model's first token, so measure "time to publish" where hidden steps exist `[C09-003]`.
2. **Pick the metrics and report them as distributions.** Report TTFT and TPOT separately; latency = TTFT + TPOT x output tokens `[C09-003]`. Use p50, p90, p95, p99, never the mean alone (one 3,000 ms outlier among ten values distorts the average), and plot TTFT against input length to spot prefill-driven outliers `[C09-003]`. Streaming TPOT needs only to beat reading speed (about 120 ms per token, roughly 6-8 tokens/s) `[C09-003]`.
3. **Model cost per request.** Cost = prefill cost + decode cost. API: tokens in and out times price; model APIs charge per token `[C04-006]`; across providers an output token costs roughly two to four times an input token, and one output token can affect latency as much as about 100 input tokens (a time-sensitive book figure) `[C09-006]`. Self-hosted: hardware price per hour divided by throughput, counted separately for input and output tokens; the book's worked example gives about 1.44 dollars per 1K requests under stated assumptions, treat it as a method not a benchmark `[C09-003]`. Compare servers on cost per request, not raw tokens/s, since tokenizers differ `[C09-003]`. Re-check API versus self-hosting at the current volume: API cost per token barely falls with scale, a fixed cluster's does `[C04-006]`.
4. **Identify the bottleneck.** Prefill is compute-bound; decode of autoregressive models is typically memory-bandwidth-bound; context length, output length and batching change the mix `[C09-002]`. Evidence order: roofline or profiler output if the user has it; otherwise MFU and MBU derived from measured tokens/s (MBU = parameters x bytes per parameter x tokens/s divided by peak bandwidth; the book's printed denominator is clipped, so state the peak-bandwidth reading as INTERPRETATION) `[C09-003]`. Do not use nvidia-smi utilization as the efficiency measure; it can read 100% at very low efficiency `[C09-003]`. MFU is observed tokens/s over the chip's theoretical peak-FLOP/s tokens/s. The book's example is a 7B model in FP16 at 100 tokens/s: 7B x 2 x 100 = 700 GB/s against 2 TB/s peak = 70% MBU `[C09-003]`. Estimate KV cache memory with 2 x B x S x L x H x M (B batch, S sequence length, L layers, H model dimension, M bytes per cached value; the book's Llama 2 13B example is about 54 GB) before judging batch size and context length `[C09-006]`. Treat the book's wording that attention computation grows "exponentially" with sequence length as UNVERIFIED; the KV cache itself grows linearly `[C09-006]`.
5. **Check hardware fit (self-hosted only).** Match chip to bottleneck: more FLOP/s for compute-bound, more bandwidth and memory for memory-bound; answer "can it run, how long, how much" from FLOP/s, memory size, bandwidth and price `[C09-004]`. Peak FLOP/s is theoretical and lower numeric precision gives higher FLOP/s; spec numbers are reference only `[C09-004]`. For owned hardware, cost is purchase price plus ongoing power draw `[C09-004]`.
6. **Check goodput, not just throughput.** Batching raises throughput and hurts latency; goodput counts requests that meet the SLO (the book's example: TTFT at most 200 ms and TPOT at most 100 ms; 100 requests per minute with 30 meeting it gives goodput of 30 per minute) `[C09-003]`. Compute goodput from raw per-request TTFT and TPOT, never from a figure's caption: the book's Figure 9-4 caption says 3 of 10 meet the SLO but its plotted bars give 2 (requests 1 and 5) `[C09-003]`. If throughput rose but goodput fell, report the trade-off, not a win.
7. **Review service-level levers** (no model change, quality should be unaffected) `[C09-007]`:
   - Batching: static waits for a full batch; dynamic caps the wait; continuous returns each response when done and refills the slot. Flag static batching on variable-length LLM traffic.
   - Prefill/decode on one machine interfere; decoupling helps when TTFT and TPOT SLOs are both missed, at the cost of state transfer.
   - Prompt caching: shared system prompts, long documents, long conversations. Check whether the provider offers it before building one; it costs memory and engineering `[C09-007]`.
   - Parallelism: replicas are simplest and serve more simultaneous requests; tensor parallelism serves models too big for one machine and can cut latency, though communication overhead erodes the gain; pipeline parallelism adds per-request latency, so avoid it under strict latency `[C09-007]`.
   - Decoupling ratios depend on workload and goals (book examples: long inputs with TTFT priority 2:1 to 4:1 prefill:decode instances; short inputs with TPOT priority 1:2 to 1:1) `[C09-007]`. Provider prompt-cache discounts the book quotes are dated; check current terms `[C09-007]`.
8. **Review system caches** `[C10-006]`. Exact caching suits multi-step or slow queries (retrieval, SQL, web search); exclude user-specific and time-sensitive queries. Check the eviction policy (LRU, LFU or FIFO in the book), retention time, and whether a classifier or rule decides what is cacheable. The book's warning is that a cached answer containing one user's private data can be served to another. INTERPRETATION: decide cacheability by whether the answer used user-specific retrieved data, not by how the question reads. Semantic caching needs good embeddings, a tuned similarity threshold and a measured hit rate; if the hit rate is unknown, recommend measuring before adding it.
9. **Review model-level levers** only where the project controls the model `[C09-006]`: weight-only quantization and distillation are the commonly used options; speculative decoding keeps quality and suits structured output; inference with reference suits outputs that copy inputs (RAG, code editing). KV cache management (for example paged cache blocks, cache quantization) matters for long context or large batches; attention redesigns (windowed, grouped-query, cross-layer) need training or finetuning time `[C09-006]`. Speculative decoding does not change quality, but model-level changes in general can alter behavior, so require a quality re-evaluation before recommending them `[C09-006]`.
10. **Choose online or batch.** Customer-facing flows need online APIs; reporting, synthetic data, reindexing and migrations tolerate batch APIs, which the book cites, as of its writing, as about 50% cheaper with turnaround in hours (time-sensitive) `[C09-002]`. Flag batchable work running on the online path.
11. **Rank recommendations** by expected gain against quality risk and effort, citing the lever's row. Label each `recommendation` or `risk`, never `confirmed`, unless a run measured the defect.

## Checks
| check | what is checked | how | evidence produced | type | criterion | how a failure is judged |
|---|---|---|---|---|---|---|
| PF-01 | Targets exist per application, hard vs nice-to-have | review of requirements docs and config | notes with the targets found | review | C04-006 | no stated target: `risk`, ask the user |
| PF-02 | TTFT and TPOT reported separately with p50/p90/p95/p99 | review of existing logs or dashboards | notes with the distribution | review | C09-003 | only averages or one combined figure: `recommendation` |
| PF-03 | Measured TTFT/TPOT against target (needs approval and spend cap) | run a user-approved probe script through `run_check.py`; at least dozens of requests with realistic input lengths | `PF-03.exec.json` plus the timing output | run | C09-003 | a percentile above the stated hard target on a re-run: FAILED, finding `confirmed`; one noisy run: `probable` |
| PF-04 | Cost per request from token counts and price | review of billing export or token logs; arithmetic written in the notes | cost notes | review | C04-006 | cost per request above the hard requirement: `probable` unless the data is measured |
| PF-05 | Goodput vs throughput under the SLO | compute from logs, or from the PF-03 output | script output via `run_check.py` | run | C09-003 | high throughput with low goodput: finding `probable` or `confirmed` with the record |
| PF-06 | Bottleneck classified (prefill, decode, memory capacity) | review of metrics, profiler output, KV cache estimate | notes and arithmetic | review | C09-002 | cannot classify: `unverified`, name the missing profile |
| PF-07 | Efficiency (MFU/MBU), self-hosted only | derive from measured tokens/s and hardware specs (MBU denominator is INTERPRETATION, see step 4) | notes; run record if tokens/s was measured | review | C09-003 | utilization quoted only from nvidia-smi: `recommendation` |
| PF-08 | Batching mode matches traffic | review of server config | config excerpt in notes | review | C09-007 | static batching on variable-length traffic: `recommendation` |
| PF-09 | Prompt caching used for shared prefixes | review of prompts and provider settings | notes | review | C09-007 | large repeated prefix, no caching: `recommendation` |
| PF-10 | System cache safety | review of cache keys and what is cached | notes | review | C10-006 | user-specific data cached under a shared key: `risk`; reproduced with a two-user test on the user's own system via `run_check.py`: `confirmed` |
| PF-11 | Batchable work on the online path | review of call sites | notes | review | C09-002 | batchable job on the online API: `recommendation` |
| PF-12 | Hardware fits the bottleneck | review of hardware spec against PF-06 | notes | review | C09-004 | mismatch: `recommendation` |

## Evidence and exit gate
- `PASSED` needs a `run_check.py` record; reading logs or config is `REVIEWED`. A missing endpoint, key or approval is `BLOCKED` with a reason.
- Measured numbers go in evidence files; estimates are labelled INTERPRETATION. Latency from a single run is not a finding; re-run once and say if it differs.
- Gate: every check has a status, the targets are stated, and each recommendation names its lever's row.

## Outputs
Cases and findings for `results.json`; the findings feed `report.md` and, for redesign, `handoff-to-architect.md` (inference and cost decisions).

## Pitfalls
- Average latency hides outliers `[C09-003]`. nvidia-smi utilization is not efficiency `[C09-003]`.
- Token throughput across models is not comparable `[C09-003]`.
- Semantic caches can return wrong or leaked answers `[C10-006]`.
- INTERPRETATION: capping or stopping output to save tokens can truncate structured output; check output limits. The book lists concise prompting and stopping conditions as latency levers `[C04-006]`.
- Model names, prices, discounts, chip specs and the MFU "above 50% is good for training" figure are time-sensitive; flag them rather than treating them as current `[C09-004]` `[C09-003]`.
- The book prints "exponentially" for attention cost growth (UNVERIFIED; likely quadratic) and a clipped MBU formula; do not quote either as settled `[C09-006]` `[C09-003]`.
- Safety: probes spend money. Ask for approval and a cap, stop at the cap, and never put keys in evidence.
