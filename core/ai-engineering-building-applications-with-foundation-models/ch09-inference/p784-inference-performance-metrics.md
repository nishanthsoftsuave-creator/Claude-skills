---
id: C09-003
title: Inference Performance Metrics
source_pages: "784-795"
chapter: 9
concepts: [latency, ttft, tpot, inter-token-latency, time-to-publish, percentiles, throughput, goodput, slo, mfu, mbu, gpu-utilization, cost-per-request]
related: [C09-001, C09-002, C09-004, C09-005]
time_sensitive: true
---
# Inference Performance Metrics
(Source: PDF pp. 784-795. The top of PDF p. 784 is a warning box that closes the preceding section; this row starts at the "Inference Performance Metrics" heading on that page. Figure 9-5, mentioned at the very end of PDF p. 795, is printed on the next page and belongs to the following row.)

## What the section covers
The measurements you should know before optimizing inference: latency and its parts (TTFT, TPOT, TBT/ITL, time to publish), why latency should be read as percentiles, throughput and its cost implications, goodput against an SLO, and the utilization family (GPU utilization as reported by nvidia-smi, MFU, MBU). From the user's side the central axis is latency (response quality is a property of the model, not the inference service); developers also care about throughput and utilization because these set application cost (PDF p. 784).

## Relation to the warning box on PDF p. 784
The warning box at the top of PDF p. 784, on batch APIs versus traditional-ML batch inference, belongs to C09-002 and is recorded there.

## Meaning

### Latency, TTFT, TPOT
- Latency is the time from the user sending a query to receiving the complete response. For autoregressive generation, particularly streaming, it is split into several metrics (PDF p. 784).
- TTFT (time to first token): how quickly the first token appears after the query is sent. It equals the duration of the prefill step and depends on input length. Expectations differ by application: a conversational chatbot should feel instantaneous, while users may tolerate waiting longer for a long-document summary (PDF p. 785).
- TPOT (time per output token): how fast each token after the first is produced. Example: at 100 ms per token, a 1,000-token response takes 100 s (PDF p. 785).
- In streaming mode TPOT must beat human reading speed but need not exceed it by much. A very fast reader consumes about 120 ms per token, so a TPOT near 120 ms, i.e. roughly 6-8 tokens per second, is enough for most uses (PDF p. 785).
- Time between tokens (TBT) and inter-token latency (ITL) are variations that both measure the gap between output tokens (PDF p. 785).

### Total latency formula
latency = TTFT + TPOT x (number of output tokens), where TTFT is time to first token, TPOT is time per output token after the first, and the last factor is the count of generated tokens (PDF p. 786).

### Same total, different experience
Two services with equal total latency can feel different because of different TTFT/TPOT splits. Do users prefer an instant first token with slower tokens afterwards, or a slightly later start followed by faster generation? The book says user studies are needed to decide. TTFT can be lowered at the cost of higher TPOT (and vice versa) by shifting compute instances between decoding and prefilling (PDF p. 786).

### User-observed versus model-observed latency, and time to publish
With chain-of-thought or agentic queries the model produces intermediate steps that the user never sees, so the TTFT and TPOT users experience can differ from those the model-side sees. Some teams use "time to publish" to make explicit that the clock stops at the first token the user actually sees (PDF p. 786).
Worked scenario (PDF pp. 786-787): after a query the model (1) generates a plan of actions, hidden from the user; (2) takes actions and logs outputs, also hidden; (3) writes a final response from those outputs. The model's first token occurs in step 1, but the user's first visible token occurs in step 3, so from the user's perspective TTFT is much longer.

### Latency is a distribution: use percentiles
- Averages mislead. Book example: ten TTFT values of 100, 102, 100, 100, 99, 104, 110, 90, 3,000 and 95 ms average 390 ms (the sum is 3,900 ms), which makes the service look slower than it is. The outlier might be a network error or an unusually long prompt that needed a long prefill; either way it deserves investigation. With large request volumes, outliers that skew the average are nearly inevitable (PDF p. 787).
- Percentiles describe a given share of requests. The median is p50: if it is 100 ms, half the requests take longer than 100 ms to produce the first token and half take less. Percentiles also expose outliers that may signal problems. The ones typically examined are p90, p95 and p99. It also helps to plot TTFT against input length (PDF p. 787).

### Throughput and goodput
- Throughput is the number of output tokens per second the service generates across all users and requests (PDF p. 788).
- Some teams count input plus output tokens. The book advises counting them separately, since prefill and decode have different computational bottlenecks and are often decoupled in modern inference servers. Unqualified, "throughput" normally means output tokens (PDF p. 788).
- Units: tokens per second (TPS); tokens/s/user is used to judge how the system scales with more users. Throughput can also be completed requests per unit time: requests per second (RPS), or, because foundation-model requests can take seconds, completed requests per minute (RPM). This is useful for understanding concurrency, and some providers throttle you if you send too many concurrent requests (PDF p. 788).

### Throughput and cost
Throughput is directly linked to compute cost; higher throughput usually means lower cost (PDF p. 789). Worked example (PDF p. 789):
- Decoding: hardware at $2 per hour with 100 tokens/s throughput costs about $5.556 per 1M output tokens (100 tokens/s x 3,600 s = 360,000 tokens per hour; $2 / 0.36M is about $5.556 per million). At 200 output tokens per request, decoding 1K requests (200K tokens) costs about $1.11.
- Prefill: the same $2/hour hardware prefilling 100 requests per minute (6,000 per hour) costs about $0.33 per 1K requests.
- Total per 1K requests: $1.11 + $0.33 = $1.44. Total cost per request is prefill plus decode cost.
- What counts as good throughput depends on model, hardware and workload: smaller models and higher-end chips yield higher throughput, and workloads with consistent input and output lengths are easier to optimize than variable ones (PDF p. 789).
- Cross-model throughput comparisons are only approximate, because token counts depend on each model's tokenizer. The book recommends comparing inference servers on something like cost per request instead (PDF p. 789).

### Latency/throughput trade-off and goodput
- Like most software, AI applications trade latency against throughput; batching improves throughput but hurts latency (PDF pp. 789-790). The LinkedIn AI team's reflection after a year of generative AI deployment says doubling or tripling throughput is not unusual if you accept worse TTFT and TPOT (PDF p. 790).
- Judging only by throughput and cost can give a poor user experience, so some teams use goodput, borrowed from networking: the number of requests per second that satisfy the SLO (the book expands the abbreviation as "software-level objective") (PDF p. 790).
- Example: SLO is TTFT at most 200 ms and TPOT at most 100 ms. The service completes 100 requests per minute but only 30 meet the SLO, so goodput is 30 requests per minute (PDF p. 790).
- Figure 9-4 (PDF p. 791): ten requests plotted with TTFT bars (upward, dashed 200 ms line) and TPOT bars (downward, dashed 100 ms line). Readings: TTFT 150, 180, 220, 250, 140, 260, 210, 170, 260, 220 ms; TPOT 70, 120, 110, 130, 60, 80, 140, 105, 130, 150 ms. Requests that meet a threshold are drawn in a darker colour. The caption says 10 RPS completed with 3 meeting the SLO gives goodput 3 RPS. Applying both thresholds to the printed bars, only requests 1 (150/70) and 5 (140/60) meet both, which is 2, not 3; the caption and the plotted values differ and both are recorded here without reconciling them. Observation only: the darker TPOT bars (those under 100 ms) number three (requests 1, 5 and 6), and the darker TTFT bars (under 200 ms) number four (requests 1, 2, 5, 8). The readings above were checked on a 150 dpi render.

### Utilization, MFU and MBU
- Utilization metrics describe how efficiently a resource is used, typically the proportion actively used out of total available capacity (PDF p. 791).
- GPU utilization, as shown by NVIDIA's nvidia-smi (System Management Interface), is the percentage of time the GPU is actively processing. Running 10 hours with the GPUs busy 5 of them gives 50% (PDF pp. 791-792). The book says NVIDIA is partly to blame for the common misunderstanding of this metric.
- Busy does not mean efficient. Take a tiny GPU capable of 100 operations per second: under nvidia-smi's definition it can show 100% utilization while doing one operation per second. Paying for a machine capable of 100 operations and using it for one wastes money, so this metric is not very useful for optimization (PDF p. 792).
- MFU (Model FLOP/s Utilization) is the metric of interest: of all operations the machine can do, how many it does in a given time. It is the ratio of observed throughput (tokens/s) to the theoretical maximum throughput of the system at peak FLOP/s. If the chip could produce 100 tokens/s at its advertised peak but your service gets 20 tokens/s, MFU is 20% (PDF p. 792).
- MBU (Model Bandwidth Utilization) is the percentage of achievable memory bandwidth in use; useful because memory bandwidth is expensive. Peak 1 TB/s with 500 GB/s used gives 50% (PDF p. 793).
- Formulas (PDF p. 793): bandwidth used = parameter count x bytes/param x tokens/s. MBU is printed as (parameter count x bytes/param x tokens/s) / (the ... and the code box is cut off there by a horizontal scroll bar, so the denominator is not legible. UNVERIFIED: the full denominator wording. INTERPRETATION: the surrounding prose (percentage of achievable memory bandwidth used; the 1 TB/s example and the 70% example dividing by the GPU's theoretical bandwidth) indicates the denominator is the chip's peak bandwidth.
- Worked example (PDF pp. 793-794): a 7B-parameter model in FP16 (2 bytes per parameter) at 100 tokens/s uses 7B x 2 x 100 = 700 GB/s. On an A100-80GB with theoretical 2 TB/s bandwidth, MBU = 700 GB/s / 2 TB/s = 70% (PDF p. 794). The book draws the lesson that quantization matters: fewer bytes per parameter means less bandwidth consumed (PDF p. 793).
- Throughput (tokens/s) relates linearly to both MBU and MFU, so some people use "throughput" to refer to them (PDF p. 794).

## Interpreting MFU and MBU
- A good value depends on model, hardware and workload. Compute-bound workloads usually show higher MFU and lower MBU; bandwidth-bound workloads usually show lower MFU and higher MBU (PDF p. 794).
- Training generally reaches higher MFU than inference because its workload is more predictable and allows better batching. Within inference, prefill is compute-bound and decode is memory-bandwidth-bound, so MFU is typically higher in prefill than in decode (PDF p. 794).
- As of the book's writing, an MFU above 50% is generally considered good for training, though hard to reach on particular hardware (PDF p. 794).
- Table 9-1 (PDF p. 795), MFU examples from the PaLM paper (Chowdhery et al., 2022): GPT-3, 175B parameters, V100 chips, 21.3%; Gopher, 280B, 4096 TPU v3, 32.5%; Megatron-Turing NLG, 530B, 2240 A100, 30.2%; PaLM, 540B, 6144 TPU v4, 46.2%.
- The section ends by introducing Figure 9-5, MBU for Llama 2-70B in FP16 on different hardware, whose decline with more users the book says is likely due to the higher computational load per second shifting the workload from bandwidth-bound to compute-bound (PDF p. 795). The figure itself is on the next page.

## When and how to apply
- INTERPRETATION: report TTFT and TPOT separately per workload, track p50/p90/p95/p99 rather than the mean, and plot TTFT against input length to spot prefill-driven outliers.
- Choose targets per application (instant TTFT for chat, looser for long summaries; TPOT around reading speed for streaming), and use user studies to settle the TTFT/TPOT balance (PDF pp. 785-786).
- Compare servers or hardware by cost per request, not raw tokens/s across different tokenizers; use goodput when throughput gains come at the expense of latency SLOs (PDF pp. 789-790).
- Use MFU and MBU rather than nvidia-smi utilization to judge hardware efficiency (PDF p. 792).

## Limitations and caveats
- Averages hide outliers; model-side TTFT can understate user-side TTFT in CoT/agent flows; token-based throughput is tokenizer dependent; nvidia-smi utilization can read 100% at very low real efficiency (PDF pp. 786-792).

## Relations
Builds on the prefill/decode distinction introduced earlier in the chapter (C09-002 and C09-001 for context); the optimization techniques that move these metrics are in the following sections (C09-004, C09-005).

## Time-sensitive statements
The MFU "above 50% is good for training" benchmark is stated "as of this writing"; Table 9-1 values and the A100 2 TB/s bandwidth figure reflect the hardware generations of the time (PDF pp. 794-795).
