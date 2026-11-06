---
id: C09-007
title: Inference Service Optimization
source_pages: "833-844"
chapter: 9
concepts: [inference-service-optimization, batching, static-batching, dynamic-batching, continuous-batching, prefill-decode-disaggregation, prompt-caching, replica-parallelism, tensor-parallelism, pipeline-parallelism, context-parallelism, sequence-parallelism]
related: [C09-001, C09-002, C09-005, C09-006, C09-008, C10-001]
time_sensitive: true
---
# Inference Service Optimization
(Source: PDF pp. 833-844; the section's last paragraphs on context and sequence parallelism run onto PDF p. 845, above the Summary heading, which belongs to C09-008. The first lines of PDF p. 833 above the "Inference Service Optimization" heading finish the compiler discussion of C09-006.)

## What the section covers
Service-level techniques that make serving cheaper and faster without touching the model: batching (static, dynamic, continuous), separating the prefill and decode phases onto different machines, prompt caching, and several parallelism strategies (replica, tensor, pipeline, context, sequence). Time-sensitive: the API discounts and prices quoted under prompt caching (PDF pp. 839-840).

## Meaning
- Most service-level optimization is resource management. There is a fixed pool of compute and memory and a dynamic stream of inference requests (possibly for different models); the aim is to allocate resources so that latency and cost are optimized (PDF p. 833).
- Unlike many model-level techniques, these do not modify the model and should not change output quality (PDF p. 833). That is the main contrast with C09-006.

## How it works

### Batching
- Batching is described as one of the easiest ways to cut cost. A service that receives several requests at once can group those arriving around the same time rather than process each alone, which the book says can "significantly reduce the service's throughput" as printed (PDF p. 833). INTERPRETATION: this is evidently a slip for increase, since the surrounding argument is that batching lowers cost by raising throughput; the printed wording is kept here and not silently corrected. Analogy: separate processing is everyone driving their own car; batching is putting people on a bus. A bus carries more people but can lengthen each journey, though done smartly the latency impact can be small (PDF pp. 833-834).
- Three main techniques (PDF p. 834):
  1. Static batching: a fixed number of inputs is grouped. The bus waits until every seat is full. Drawback: every request waits for the batch to fill, so the first request is held until the last arrives, however late that is.
  2. Dynamic batching: a maximum time window per batch. With batch size 4 and a 100 ms window, the server runs the batch when it has four requests or when 100 ms elapse, whichever is first. Like a bus that leaves on schedule or when full. Latency stays under control because early requests are not held by later ones. Downside: batches may be partly empty when run, wasting compute.
  3. Continuous batching (below).
- Figure 9-15 (PDF p. 835) shows a timeline of incoming requests, with static batching as three long boxes that cover whole groups of requests including long gaps, and dynamic batching as four shorter boxes that cut batches at time boundaries. Its caption makes the point that dynamic batching keeps latency manageable but may be less compute-efficient.
- Problem with naive batching for LLMs: all requests in a batch must finish before any response is returned, and LLM requests vary in length. If one request produces 10 tokens and another 1,000, the short one waits for the long one, adding avoidable latency (PDF p. 835).
- Continuous batching, also called in-flight batching, returns each response as soon as it is done. It selectively batches only those operations that do not cause one response's generation to hold up another, as introduced in the Orca paper (Yu et al., 2022). When a request finishes and is returned, another request can take its slot, so the batch is refilled continuously. Analogy: a bus that drops off a passenger and immediately picks up another to keep occupancy high (PDF p. 835).
- Figure 9-16 (PDF p. 836) contrasts normal batching (Batch 1 = R1-R4, Batch 2 = R5-R8, each batch lasting until its longest request ends) with continuous batching, where four lanes run in parallel and, when a short request ends, the next request starts in that lane: R7 follows R1, R8 follows R2, R5 follows R3, R6 follows R4. Bars have different lengths, which shows requests differ in duration.

### Decoupling prefill and decode
- LLM inference has two steps, prefill and decode. Prefill is compute-bound and decode is memory-bandwidth-bound, so running both on one machine makes them compete inefficiently and can substantially slow both TTFT and TPOT (PDF p. 836).
- Illustration: a GPU already near peak compute with prefill and decode jobs might still absorb another light job such as decoding. But a new query brings a prefill job as well as a decode job, and that one prefill can drain compute from the decode jobs already running, slowing TPOT for those requests (PDF pp. 836-837).
- A common remedy is to disaggregate: put prefill and decode on different instances (for example different GPUs). The cited papers "DistServe" (Zhong et al., 2024) and "Inference Without Interference" (Hu et al., 2024) show that for various popular LLMs and applications this significantly increases the volume of requests served while still meeting latency targets (PDF p. 837).
- Cost of decoupling: intermediate states must be moved from prefill instances to decode instances. The papers find this communication overhead not substantial in modern GPU clusters with high-bandwidth links such as NVLink inside a node (PDF p. 837).
- The prefill-to-decode instance ratio depends on workload (longer inputs need more prefill compute) and latency goals (prioritizing TTFT versus TPOT). Book examples: long inputs plus TTFT priority gives a ratio between 2:1 and 4:1; short inputs plus TPOT priority gives 1:2 to 1:1 (PDF p. 837).

### Prompt caching
- Many prompts share text segments. A prompt cache stores these segments so they are processed once. Typical shared segment: the system prompt, which without a cache is reprocessed for every query and with a cache only for the first (PDF p. 838).
- Also useful for queries about one long document (a book, a codebase) that can be cached across queries, and for long conversations where earlier messages are cached and reused to predict later ones. Alternate names: context cache, prefix cache (PDF p. 838). Figure 9-17 (PDF p. 839) shows several prompts with overlapping segments, where the overlapping parts are cached and reused.
- Saving example: a 1,000-token system prompt and one million API calls per day means roughly one billion repeated input tokens avoided daily (PDF p. 839).
- Costs and caveats: it is not free. Like the KV cache, a prompt cache can be large and occupy memory; unless a model API already provides it, building prompt caching can take significant engineering effort (PDF p. 839).
- History and offerings (as of the book's writing): introduced by Gim et al. in November 2023 and quickly adopted by APIs. Google Gemini gives a 75% discount on cached input tokens but charges extra for cache storage ($1.00 per million tokens per hour). Anthropic promises up to 90% cost savings (more for longer cached context) and up to 75% latency reduction (PDF p. 839).
- Table 9-3 (PDF p. 840, data from Anthropic, 2024) lists time to first token and cost impact:

| Use case | TTFT without caching | TTFT with caching | Cost reduction |
|---|---|---|---|
| Chat with a book (100,000-token cached prompt) | 11.5 s | 2.4 s (-79%) | -90% |
| Many-shot prompting (10,000-token prompt) | 1.6 s | 1.1 s (-31%) | -86% |
| Multi-turn conversation (10 turns, long system prompt) | about 10 s | about 2.5 s (-75%) | -53% |

### Parallelism
- Accelerators are built for parallel work, so parallelization is central to high-performance computing, and new strategies keep appearing; the book covers only a few. Two families work for any model: data parallelism and model parallelism. A family specific to LLMs is context and sequence parallelism. One optimization may combine several strategies (PDF p. 841).
- Replica parallelism: the simplest; create multiple copies of the model. More replicas serve more simultaneous requests, possibly using more chips. Placing models of different sizes on different chips is a bin-packing problem that grows harder with more models, replicas and chips (PDF p. 841). The book's setting: models of 8B, 13B, 34B and 70B parameters, GPUs of 24, 40, 48 and 80 GB, all in 8-bit precision (PDF p. 841).
  - With a fixed chip count you decide how many replicas of each model and which GPU for each, to maximize your metrics; for instance, three 13B models on a 40 GB GPU, or keep it for one 34B model (PDF pp. 841-842).
  - With a fixed replica count you decide what chips to buy to minimize cost, which the book says rarely happens (PDF p. 842).
  - The book's footnote on training notes that the same technique is called data parallelism there (see C09-008).
- Model parallelism: when a model is too big for one machine, split the same model across machines. Fitting models to chips gets still more complicated (PDF p. 842).
- Tensor parallelism (intra-operator parallelism) is the most common inference split. Operators such as matrix multiplication act on multidimensional tensors; the tensors of an operator are partitioned over devices, so the operator breaks into smaller pieces that run in parallel. Figure 9-18 (PDF p. 843) shows a matrix multiplied by a two-column matrix nondistributed, versus split so device 1 multiplies with the first column and device 2 with the second, then a gather step combines the partial results into the full output. Benefits: it lets models too large for one machine be served, and it cuts latency, although communication overhead can erode the latency gain (PDF p. 842).
- Pipeline parallelism: divide the model's computation into stages, one device per stage; while one stage works on one part, others work on subsequent parts, overlapping computation (PDF p. 843). Figure 9-19 (PDF p. 844) shows four devices holding layers 1 to 4 and four micro-batches MB1-MB4 flowing diagonally through them in a staircase pattern, with outputs emerging in order. A batch is split into micro-batches; each one's output passes to the next machine after it is processed (PDF p. 844).
  - Trade-off: enables serving large models across machines but raises per-request total latency because of communication between stages. So strict-latency applications generally avoid it in favor of replica parallelism. It is, however, widely used in training because it can raise throughput (PDF p. 844).
- Context parallelism and sequence parallelism: less common, mentioned to show diversity; both aim to make processing long inputs more efficient (PDF pp. 844-845).
  - Context parallelism splits the input sequence across devices, for example first half on machine 1 and second half on machine 2 (PDF p. 845).
  - Sequence parallelism splits the operators needed for the whole input across machines, for example attention on machine 1 and feedforward on machine 2 (PDF p. 845).

## When and how to apply
- The book does not give a single recipe in this section; the chapter summary (C09-008) says choices depend on workload and performance goals.
- INTERPRETATION: if you use a managed model API, these are mostly provider-side; check whether it offers prompt caching and what discount applies before building your own, given the engineering effort the book mentions.

## Alternatives and trade-offs
- Static vs dynamic vs continuous batching: waiting for a full batch, versus bounded waiting with possibly wasted compute, versus returning responses early and refilling slots.
- Co-located vs decoupled prefill and decode: interference versus state-transfer overhead.
- Replica vs tensor vs pipeline parallelism: replicas are simplest and good for latency but cost chips; tensor parallelism helps latency and capacity but adds communication; pipeline parallelism adds latency and so is avoided for strict-latency serving.

## Limitations and failure modes
- Bus analogy cost: batching can lengthen individual journeys (PDF p. 834).
- Prompt cache consumes memory and may need heavy engineering; Gemini charges for storage (PDF p. 839).
- Communication overhead reduces tensor parallel latency gains (PDF p. 842).

## Relations
Follows model-level optimization (C09-006); builds on the prefill/decode and TTFT/TPOT metrics (C09-001, C09-002); chapter wrap-up in C09-008; the chapter lead-in is C09-005; the next chapter (C10-001) assembles techniques into systems.

## Time-sensitive statements
Gemini 75% cached-token discount and $1.00 per million tokens per hour storage; Anthropic up to 90% cost and 75% latency savings; Table 9-3 figures from Anthropic (2024) (PDF pp. 839-840).
