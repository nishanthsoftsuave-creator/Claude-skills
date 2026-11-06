---
id: C09-002
title: Inference Overview
source_pages: "775-783"
chapter: 9
concepts: [inference-server, inference-service, compute-bound, memory-bandwidth-bound, arithmetic-intensity, roofline-chart, prefill, decode, online-api, batch-api, streaming]
related: [C09-001, C09-003, C09-004, C09-006, C09-007]
time_sensitive: true
---
# Inference Overview
(Source: PDF pp. 775-783, tail PDF p. 784)

## What the section covers
It fixes a shared vocabulary: inference server versus inference service, the two computational bottlenecks (compute-bound and memory bandwidth-bound), how prefill and decode differ in bottleneck, and the difference between online and batch inference APIs, including streaming. The metrics section that follows is a separate row (C09-003).

## Meaning
- The training-versus-inference distinction that opens the page is recorded in C09-001, which owns the text above this section's heading.
- Inference server: the production component that runs model inference. It hosts the available models, has access to the hardware, allocates resources to run the right model for each application request (for example a user prompt) and returns the response (PDF p. 775).
- Inference service: the larger system containing the server. It also receives and routes requests and may preprocess them before they reach the server (PDF p. 775).
- Figure 9-1 shows a simple service: apps send requests to and get responses from an inference server that holds several models (three are drawn, of different sizes), and the server sits on a block of hardware drawn as several accelerator chips (PDF p. 776).
- Model APIs from providers such as OpenAI and Google are inference services, so API users do not implement most of this chapter's techniques. Anyone hosting a model themselves is responsible for building, optimizing and maintaining the service (PDF p. 776).

## Computational bottlenecks
Optimization means finding bottlenecks and dealing with them, like city planners locating congestion points; an inference server should be built around the bottlenecks of the workloads it serves (PDF pp. 776-777). There are two main ones (PDF p. 777):
- Compute-bound: completion time is set by the amount of computation needed. The example is password decryption, which needs heavy mathematical calculation.
- Memory bandwidth-bound: completion time is limited by data transfer speed inside the system, such as moving data between memory and processors. The example is keeping data in CPU memory while training on GPUs, so data must be shipped from CPU to GPU, which can take long. The literature often abbreviates this to memory-bound (PDF p. 777).

### Terminology ambiguity
(PDF p. 778) Some people use memory-bound to mean limited by memory capacity rather than bandwidth. That happens when hardware lacks enough memory for the task and shows up as an out-of-memory (OOM) error. It can often be relieved by splitting the task into pieces, for instance splitting a model across GPU memory and CPU memory. This slows computation because of CPU-GPU transfers, but if transfer is fast enough the penalty shrinks. The book therefore argues that the capacity limit is really more about bandwidth.

### Arithmetic intensity and the roofline chart
- The compute-bound versus bandwidth-bound idea comes from the "Roofline" paper (Williams et al., 2009) (PDF p. 778).
- An operation is classified by its arithmetic intensity: the number of arithmetic operations per byte of memory access (PDF p. 778). In the figure the axis unit is FLOP/byte.
- Profiling tools such as NVIDIA Nsight can show a roofline chart telling you which kind of bound a workload is; it is named for its roof-like shape, and such charts are common in hardware performance analysis (PDF pp. 778-779).
- Figure 9-2 (log-scale axes, titled "Floating Point Operations Roofline") plots performance in FLOP/s (vertical, from about 1e-05 to 100,000, labelled in billions) against arithmetic intensity in FLOP/byte (horizontal, about 0.001 to 10,000). A sloped line rises on the left and flattens into a horizontal ceiling. The left, shaded area is the memory bound region and the right, shaded area is the compute bound region. Two ceilings are drawn (one near 100-300 and one near 10,000 on the vertical axis, with square markers where each meets the slope), and a dotted vertical line with a dot well below the slope in the memory bound region. The caption states that the chart shows whether an operation is compute-bound or memory bandwidth-bound (PDF p. 779). The book text does not explain the two ceilings or the dotted line, so their meaning is not stated here. Values read from the figure are only approximate.

### Matching optimization to bottleneck
- A compute-bound workload may be accelerated by spreading it over more chips or using chips with more computing power (a higher FLOP/s figure) (PDF p. 779).
- A memory bandwidth-bound workload may be accelerated by chips with higher bandwidth (PDF p. 779).
- Architectures and workloads differ: inference for image generators like Stable Diffusion is typically compute-bound, whereas inference for autoregressive language models is typically memory bandwidth-bound (PDF pp. 779-780).

## How it works: prefill and decode in language models
Transformer language model inference, recalled from Chapter 2, has two steps (PDF p. 780):
- Prefill: the input tokens are processed in parallel. How many can be handled at once is limited by how many operations the hardware can perform in a given time, so prefill is compute-bound.
- Decode: one output token is generated at a time. This step typically requires loading large matrices (such as model weights) into the GPU, limited by how fast data can be loaded, so decode is memory bandwidth-bound.
- Figure 9-3 illustrates this with the prompt "Who wrote the book Chaos?" going through one prefill block labelled compute-bound, followed by a chain of decode blocks (labelled memory bandwidth-bound) that emit "James", "Gleick", "did", "." and an end-of-sequence token (PDF p. 781).
- Because their profiles differ, prefill and decode are often separated onto different machines in production; the book defers this to "Inference Service Optimization" (PDF p. 781).
- Factors that change the amount of prefill and decode work, and hence the bottlenecks: context length, output length and request batching strategy. Long context typically gives a memory bandwidth-bound workload, though clever techniques covered later can remove that bottleneck (PDF p. 781).

## Time-sensitive statements
- As of the book's writing, the transformer's prevalence and the limits of current accelerators make many AI and data workloads memory bandwidth-bound; the book expects future software and hardware advances to make them compute-bound (PDF p. 781).
- Batch API discounts and turnaround times below are stated "as of this writing" (PDF p. 782).

## Online and batch inference APIs
(PDF p. 782)
- Online APIs optimize for latency: requests are handled as soon as they arrive.
- Batch APIs optimize for cost. If the application has no strict latency need, higher latency permits more optimization techniques, such as batching requests together and using cheaper hardware. The book's example: Google Gemini and OpenAI offered batch APIs at a 50% cost reduction with much longer turnaround, in the order of hours rather than seconds or minutes.
- Online APIs may still batch requests when that does not noticeably hurt latency (see "Batching" in the service-optimization row). The real difference is that online APIs focus on lower latency and batch APIs on higher throughput.

### When to use which
- Customer-facing use cases such as chatbots and code generation usually need low latency, so they use online APIs (PDF p. 782).
- Good fits for batch APIs (PDF pp. 782-783): synthetic data generation; periodic reporting (summarizing Slack messages, sentiment analysis of brand mentions on social media, analyzing customer support tickets); onboarding new customers whose uploaded documents must all be processed; migrating to a new model that requires reprocessing all data; generating personalized recommendations or newsletters for a large customer base; and knowledge base updates by reindexing an organization's data.

### Streaming
- APIs normally return a complete response, but autoregressive decoding can take a long time and users are impatient. Many online APIs therefore offer a streaming mode that returns each token as generated, shortening the wait for the first token (PDF p. 783).
- Downside: the response cannot be scored before the user sees it, so the risk of showing a bad response rises. A response can still be updated or removed retroactively once the risk is detected (PDF p. 783).

## Limitations and cautions: batch API versus traditional ML batch inference
(PDF p. 784) A foundation-model batch API is not the same thing as batch inference in traditional ML. In traditional ML, online inference computes predictions after requests arrive, while batch inference precomputes predictions before requests arrive. Precomputation works when inputs are finite and predictable, such as recommendation systems where recommendations for all users can be generated ahead and fetched when a user visits. With foundation models the inputs are open-ended and all user prompts are hard to predict, so this does not carry over.

## Relations
Continues from C09-001 (chapter framing); C09-003 defines latency, TTFT, TPOT and throughput metrics; C09-004 covers accelerators and their memory and compute characteristics; C09-006 and C09-007 give the model-level and service-level techniques that target the bottlenecks defined here.
