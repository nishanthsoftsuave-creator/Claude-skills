---
id: C09-008
title: Chapter 9 Summary and Endnotes
source_pages: "845-851"
chapter: 9
concepts: [inference-optimization-summary, ttft-tpot, latency-throughput-tradeoff, model-level-vs-service-level, optimization-selection, quantization, tensor-parallelism, endnotes]
related: [C09-001, C09-002, C09-003, C09-004, C09-005, C09-006, C09-007, C10-001]
time_sensitive: false
---
# Chapter 9 Summary and Endnotes
(Source: PDF pp. 845-851. The top of PDF p. 845, above the Summary heading, is the end of the parallelism section and belongs to C09-007. The tail page opens Chapter 10 and is not covered here. Endnote markers are rendered as tiny, unreadable superscripts in the PDF image, so notes are described by content and not by number.)

## What the section covers
The chapter's closing summary (PDF pp. 845-848) and the chapter's endnotes (PDF pp. 848-851), which hold side facts on training versus inference cost, terminology, hardware, and some technique details.

## Why it matters (summary's framing)
- A model's usability depends strongly on inference cost and latency: cheaper inference makes AI-driven decisions more affordable, faster inference lets AI be built into more applications. That potential has drawn many talented people who keep inventing new methods (PDF p. 845).

## Chapter recap

### Metrics
- Efficiency must be measurable before it is improved, so the chapter began with latency, throughput and utilization metrics. For language-model inference, latency splits into time to first token (TTFT), shaped by the prefill phase, and time per output token (TPOT), shaped by the decode phase (PDF pp. 845-846).
- Throughput metrics tie directly to cost. Latency and throughput trade off: accept higher latency to cut cost, while cutting latency often raises cost (PDF p. 846).

### Hardware
- How efficiently a model runs depends on its hardware, so the chapter also surveyed AI hardware and what optimizing for different accelerators involves (PDF p. 846).

### Who needs the techniques
- Because model APIs exist, most application developers will use their built-in optimization and not implement these techniques. The author still thinks knowing what is possible helps in judging a model API's efficiency (PDF p. 846).

### Two levels
- Model-level optimization frequently changes the model itself and so can change behavior. Inference-service-level optimization usually leaves the model intact and changes only how it is served (PDF p. 846).
- Model-level techniques include model-agnostic ones, quantization and distillation. Architecture-specific ones follow the bottleneck: for transformers it is attention, so many methods make attention more efficient (KV cache management, attention kernels). For autoregressive language models the bottleneck is autoregressive decoding, which has produced its own techniques (PDF p. 847).
- Service-level techniques are batching and parallelism strategies, plus ones specific to autoregressive LMs: decoupling prefill and decode, and prompt caching (PDF p. 847).

### Choosing techniques
- Choice depends on workload. KV caching matters much more for long contexts than short. Prompt caching is crucial for workloads with long overlapping prompt segments or multi-turn conversations (PDF p. 847).
- Choice also depends on performance requirements. If low latency outranks cost, scale up replica parallelism: more replicas need more machines, but each machine handles fewer requests and can give each request more resources, improving response time (PDF p. 847).
- Across use cases, the most impactful techniques are usually (PDF p. 848): quantization (works well across models); tensor parallelism (cuts latency and allows larger models); replica parallelism (relatively easy to implement); attention-mechanism optimization (large speedups for transformers).
- Inference optimization is the last of the model adaptation techniques in the book; the next chapter looks at combining them into a cohesive system (PDF p. 848).

## Endnotes (content)
All notes are the author's asides, recorded here by topic.

### Cost and terminology (PDF pp. 848-849)
- Inference is the forward pass, training is forward plus backward (as in Chapter 7) (PDF p. 848).
- Training versus inference cost, from a friend (Mark Saroufim): let T be total training cost, p the price charged per inference, N the number of inference calls sold. Building the model makes sense only if T <= p x N (the book prints "T <= p × N"). The more a model is used in production, the more the provider can lower inference cost; this does not hold for third-party API providers selling inference on top of open source models (PDF p. 848).
- "Memory-bound" is used inconsistently: anecdotally, systems people (optimization and GPU engineers) mean bandwidth-bound, while AI people (ML and AI engineers) mean memory-capacity-bound. The Roofline paper uses it for memory-bandwidth-bound (PDF p. 848).
- Prefilling effectively fills the initial KV cache of a transformer (PDF p. 849).
- Serving practice: splitting an inference API into online and batch lets you favor latency where it matters. Example: if the server can handle at most X requests per second without latency degradation but must serve Y > X, less urgent users can send requests to the batch API so the service handles online requests first (PDF p. 849).
- An application's system prompt is often known in advance; only exact user queries are unpredictable (see "Prompt caching" in C09-007) (PDF p. 849).
- Early chatbots were sometimes criticized for answering too fast, which seemed unnatural; the book cites a 2017 iTnews piece on Lufthansa delaying its chatbot's replies. As people grew used to chatbots this complaint faded (PDF p. 849).
- Time between tokens (TBT) is LinkedIn's term and inter-token latency (ITL) is NVIDIA's for the per-token latency idea (PDF p. 849).
- An Anyscale experiment found 100 input tokens affect overall latency about as much as one output token (PDF p. 849).
- MFU was introduced in the PaLM paper (Chowdhery et al., 2022), though people long cared about FLOP/s utilization. Chip makers may also do what the author calls "peak FLOP/s hacking": running experiments in special conditions, such as sparse matrices of particular shapes, to raise peak FLOP/s, which makes chips look better but makes high MFU harder for users to reach (PDF p. 849).

### Hardware and history (PDF pp. 849-850)
- In the 1960s computers could run only one-layer neural networks. Minsky and Papert's 1969 book Perceptrons argued networks with hidden layers could do little more than a low-order perceptron; their quoted view was that little is known about such machines and that they "can do little more than" a low-order perceptron; there was not enough compute to rebut it, and it was widely cited as a reason AI funding dried up in the 1970s (PDF pp. 849-850).
- GPU naming: there were discussions of renaming the GPU since it does far more than graphics. NVIDIA's Jensen Huang said they considered a more general name such as GPGPU or XGU but decided against it, assuming buyers know what a GPU is good for (PDF p. 850).
- Matrix multiplication ("matmul") is estimated at more than 90% of all floating point operations in a neural network, per Ivanov et al. (2021) and Zhu et al. (2024) (PDF p. 850).
- Chip and architecture co-design runs both ways: for instance the transformer was originally designed by Google to run fast on TPUs and only later optimized on GPUs (PDF p. 850).
- Lower-end to mid-range GPUs may use GDDR (Graphics Double Data Rate) memory (PDF p. 850).
- Data-center siting: a major challenge for data centers with tens of thousands of GPUs is a location with guaranteed electricity, along with supply, speed and geopolitical limits. Remote regions may have cheaper power but higher network latency, which hurts latency-sensitive uses such as inference (PDF p. 850).

### Technique details (PDF p. 851)
- Each token-generation step moves the whole model's parameters from the accelerator's high-bandwidth memory to its compute units, making it bandwidth-heavy; because only one token is produced at a time, few FLOP/s are used, which is computationally inefficient (PDF p. 851).
- Consequently, if MFU is already maxed out, speculative decoding makes less sense (PDF p. 851).
- The Jacobi method is an iterative algorithm whose parts of the solution can be updated simultaneously and independently (PDF p. 851).
- Attention computations in an autoregressive model number O(n^2) (the text layer drops the superscript; the rendered page shows O(n^2)) (PDF p. 851).
- Convolution operations are often used in image generation models such as Stable Diffusion (PDF p. 851).
- Many companies treat their kernels as trade secrets, since faster and cheaper model runs are a competitive advantage (PDF p. 851).
- Talks that mention the prefill-to-decode instance ratio include "Llama Inference at Meta" (Meta, 2024) (PDF p. 851).
- llama.cpp also has prompt caching, but as of writing it appears to cache only whole prompts within one chat session; the author's reading of the code is that in a long conversation it caches earlier messages and processes only the newest (PDF p. 851).
- During training, replica parallelism's equivalent is called data parallelism (PDF p. 851).

## Relations
Wraps up C09-001 to C09-007 (metrics, hardware, model-level and service-level techniques). The chapter's next step, C10-001, begins integrating adaptation techniques into a full system (the endnotes end the chapter; the following page starts Chapter 10).
