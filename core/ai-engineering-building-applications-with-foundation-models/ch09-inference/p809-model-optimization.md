---
id: C09-006
title: Model Optimization
source_pages: "809-832"
chapter: 9
concepts: [model-optimization, model-compression, pruning, speculative-decoding, parallel-decoding, medusa, kv-cache, flashattention, kernels, compilers, grouped-query-attention]
related: [C09-002, C09-003, C09-004, C09-005, C09-007, C07-011, C08-011]
time_sensitive: true
---
# Model Optimization
(Source: PDF pp. 809-832. The first lines of PDF p. 809 are the end of the lead-in section C09-005, which says hardware design is out of scope and that production optimization usually mixes several levels. The section's last sentence, about compilers being standalone tools or integrated into frameworks, continues onto the next page, where the service-level section begins.)

## What the section covers
Model-level inference optimization: changes to the model itself that make serving cheaper or faster, even when that alters model behavior. The book organises it into four groups: model compression (quantization, distillation, pruning); overcoming the autoregressive decoding bottleneck (speculative decoding, inference with reference, parallel decoding); attention mechanism optimization (redesigning attention, managing the KV cache, writing attention kernels); and kernels and compilers, closed by a PyTorch case study.

## Meaning
- Many current foundation models are transformers with an autoregressive language-model part. Three traits make their inference resource-hungry: model size, autoregressive decoding, and the attention mechanism (PDF p. 809). The book then lists approaches to address these challenges.
- Model compression = techniques that shrink a model; a smaller model is often also faster. Two were covered earlier: quantization (lower numeric precision, smaller memory footprint, higher throughput; Chapter 7) and distillation (train a small model to mimic a large one; Chapter 8) (PDF p. 809).
- Pruning, in neural networks, has two meanings: (a) remove whole nodes, which changes the architecture and cuts parameter count; (b) find the parameters least useful for predictions and set them to zero. In the second case the total parameter count is unchanged, only the count of non-zero parameters drops, so the model becomes sparse, which reduces storage and speeds computation (PDF p. 810).
- Target model: the model you actually want to use. Draft (proposal) model: a faster, weaker model that proposes draft output in speculative decoding (PDF p. 812).
- KV cache: the cache holding key and value vectors of earlier tokens so they are reused rather than recomputed (PDF p. 821).
- Kernel: code optimized for a specific chip such as a GPU or TPU (PDF pp. 826-827). Lowering: converting a model script into a language the hardware understands; a compiler is the tool that lowers code for a given hardware (PDF p. 830).

## How it works

### Model compression
- Pruning idea: distillation shows a large model's behavior can be captured by fewer parameters, so perhaps a subset of the large model's own parameters already captures its whole behavior (PDF p. 810).
- A pruned model can be used as is, or finetuned to adjust the surviving parameters and repair any accuracy loss from pruning. Pruning can also help discover promising architectures (Liu et al., 2018); the smaller pruned architectures can then be trained from scratch (Zhu et al., 2017) (PDF p. 810).
- Reported result: Frankle and Carbin (2019) showed pruning could cut non-zero parameters of certain trained networks by over 90%, reducing memory and improving speed without hurting accuracy (PDF p. 810).
- Why pruning is nonetheless uncommon in practice (as of writing): it is harder, since it needs understanding of the original architecture; the speedup is often much smaller than other approaches give; and it yields sparse models that not all hardware can exploit (PDF pp. 810-811).
- What is common: weight-only quantization is "by far the most popular" approach, being easy, working out of the box for many models, and very effective. Going from 32 to 16 bits halves memory. The book notes we are near the floor, since a value cannot use fewer than 1 bit (PDF p. 811). Distillation is also common because it can yield a small model whose behavior suits your needs about as well as a much larger one (PDF p. 811).

### The autoregressive decoding bottleneck
- Models emit one token after another. At 100 ms per token, a 100-token answer takes 10 s. It is also costly: across API providers an output token costs roughly two to four times an input token, and Anyscale found one output token can affect latency as much as 100 input tokens (Kadous et al., 2023). So small percentage gains in generation speed noticeably help user experience (PDF p. 811).
- The book stresses this space is moving fast, that new techniques keep appearing, that a future architecture may remove the bottleneck, and that the techniques shown illustrate what a solution may look like (PDF p. 812).

### Speculative decoding (speculative sampling)
Procedure, given input tokens x1 ... xt (PDF p. 812). Notation: K is the number of draft tokens per round, j the number the target accepts.
1. The draft model generates K tokens x(t+1) ... x(t+K).
2. The target model verifies these K tokens in parallel.
3. The target accepts the longest left-to-right prefix of draft tokens it agrees with.
4. If it accepts j draft tokens x(t+1) ... x(t+j), it then generates one extra token x(t+j+1).
5. The loop restarts: the draft model generates K new tokens conditioned on x1 ... xt plus the j accepted tokens.

Output per round: if no draft token is accepted, only one token (from the target) is produced; if all are accepted, K + 1 tokens (K from the draft, one from the target) (PDF p. 813). Figure 9-9 (from Stern et al., 2018) shows the prefix "I saw a dog ride" with the draft proposing "in the bus"; three verification rows run in parallel, "in" and "in the" pass, and "in the car" fails, so the accepted output is "I saw a dog ride in the" (PDF p. 813).

Why it is not a latency risk even though a full rejection forces the target to generate everything plus verify it (PDF pp. 813-814):
1. Verification is parallel while generation is sequential, so verifying is faster than generating; speculative decoding turns the decoding workload into one resembling prefill.
2. Some tokens are easier to predict than others, so a weaker model can get those right, giving a high acceptance rate.
3. Decoding is memory-bandwidth-bound, so there are normally idle FLOPs available to do verification for free.

Practical details (PDF pp. 814-815):
- Acceptance rate depends on domain; it is typically higher for structured text such as code.
- Larger K means fewer verification calls to the target but a lower acceptance rate of draft tokens.
- The draft model may have any architecture, ideally sharing the target's vocabulary and tokenizer; train a custom one or reuse an existing weaker model.
- Example: for Chinchilla-70B, DeepMind trained a 4B-parameter draft model of the same architecture (Chen et al., 2023). The draft produced a token in 1.8 ms versus 14.1 ms for the target (about eight times faster), cutting overall latency by more than half without hurting response quality. A similar gain was seen on T5-XXL (Laviathan et al., 2022).
- Adoption: relatively easy to implement and does not change model quality; about 50 lines of PyTorch; built into vLLM, TensorRT-LLM and llama.cpp (PDF pp. 814-815).

### Inference with reference
- Many responses repeat input text: quoting a passage of an attached document, or editing code where most of the original is kept. Instead of generating those tokens, copy them from the input (PDF p. 815).
- It resembles speculative decoding but draws the draft tokens from the input rather than from a draft model. The key challenge is an algorithm that finds the most relevant input span at each decoding step; the simplest option is to find a span matching the current tokens (PDF p. 815).
- No extra model is needed, but it helps only when context and output overlap heavily, such as retrieval systems, coding, and multi-turn conversations. Yang et al. (2023) report about a two-times generation speedup in such settings (PDF pp. 815-816).
- Figure 9-10 (Yang et al., 2023) gives two examples: a retrieval answer to "where does real insulin come from", where spans copied from the retrieved documents are highlighted, and a two-turn LaTeX coding exchange where the second turn reuses most of the first turn's code with small edits. Copied spans are marked in colour (PDF pp. 817-818).

### Parallel decoding
- Aim: break the sequential dependency by generating several future tokens x(t+1), x(t+2), ..., x(t+k) at once, so a token is produced before the one preceding it is known. This can work because the existing sequence often suffices to predict a few next tokens. Example: given "the cat sits" you may guess that the word after the next one is "the" without knowing whether the next is "on", "under" or "behind" (PDF p. 818).
- Parallel tokens can come from one decoder, as in Lookahead decoding (Fu et al., 2024), or from several decoding heads, as in Medusa (Cai et al., 2024) (PDF p. 818).
- Medusa: the original model gets multiple extra decoding heads, each a small neural layer trained to predict a token at a given future position. If the base model predicts token x(t+1), then head k predicts x(t+k+1). The heads are trained together with the base model, which is frozen. NVIDIA claimed Medusa lifted Llama 3.1 token generation by up to 1.9 times on HGX H200 GPUs (Eassa et al., 2024) (PDF p. 818).
- Because tokens are not produced sequentially they must be verified and integrated (PDF p. 819):
  - Lookahead decoding uses the Jacobi method: (1) generate K future tokens in parallel; (2) check them for coherence and consistency with context; (3) regenerate or adjust only the tokens that fail, not all K; repeat until all pass and are merged into the output. This family is also called Jacobi decoding.
  - Medusa uses tree-based attention: each head offers several options per position, organised into a tree to pick the most promising combination.
- Figure 9-11 shows the Medusa structure: the input "What will happen if Medusa meets a llama?" goes through the original model (embedding, transformer layers, LM head) and three Medusa heads that read the last hidden state; each gives top-k options (the LM head: "It, I, As"; head 1: "is, ', the"; head 2: "difficult, is, '"; head 3: "not, difficult, a"). Candidate sequences are scored, with "It is difficult" accepted and variants like "It' difficult a" rejected, yielding one multi-token step (PDF p. 820).
- Caveat: attractive, but not intuitive, and some methods such as Medusa are hard to implement (PDF p. 820).

### Attention mechanism optimization
- Generating token x(t) needs key and value vectors for x1 ... x(t-1); generating x(t+1) needs those for x1 ... x(t). Instead of recomputing, reuse earlier vectors; only the newest token's key and value vectors are computed and appended to the KV cache (PDF pp. 820-821). Figure 9-12 depicts the cache holding earlier K and V vectors while only the newest token's K and V are added each step (translation example "How are you ?" producing "Como") (PDF p. 821).
- The KV cache is inference-only. In training all tokens are known in advance, so next-token computation can run all at once and no cache is needed (PDF p. 822).
- Scaling: attention computations per token grow with sequence length; the book says the number of attention computations "grows exponentially" with sequence length, while KV cache size grows linearly (PDF p. 822). UNVERIFIED: "exponentially" is the book's wording; the surrounding argument (each new token attends to all previous ones) reads as a quadratic total, but the book does not say so.
- The cache also grows with batch size. A Google paper (Pope et al., 2022) computed that a 500B+ model with multi-head attention, batch size 512 and context 2048 needs a 3 TB cache, three times the weights (PDF p. 822).
- Cache size is capped by available hardware storage, which bottlenecks long-context apps, and a large cache is slow to load, which hurts strict latency. Attention's compute and memory demands are one reason longer contexts are hard (PDF p. 822).
- Three families of fixes: redesign attention, optimize the KV cache, write attention kernels (PDF pp. 822-823).

#### KV cache size formula (PDF p. 823; rendered and checked)
Memory without optimization = 2 × B × S × L × H × M, where B = batch size, S = sequence length, L = number of transformer layers, H = model dimension, M = memory per cached number (for example FP16 or FP32); the 2 covers keys plus values. Worked example from the book: Llama 2 13B has 40 layers and model dimension 5,120; with B = 32, S = 2,048 and 2 bytes per value, 2 × 32 × 2,048 × 40 × 5,120 × 2 = 54 GB. Arithmetic check: the product is about 53.7 billion bytes, which rounds to the book's 54 GB.

#### Redesigning the attention mechanism (PDF pp. 824-825)
- These change the architecture, so they can be applied only in training or finetuning.
- Local windowed attention (Beltagy et al., 2020): attend only to a fixed window of nearby tokens, cutting both cache and attention compute. With an average sequence of 10,000 tokens and a 1,000-token window the cache shrinks 10 times. It can be interleaved with global attention: local covers nearby context, global captures task-specific information across the document.
- Cross-layer attention (Brandon et al., 2024) shares key and value vectors across adjacent layers; three layers sharing means a three-times smaller cache.
- Multi-query attention (Shazeer, 2019) shares key-value vectors across query heads. Both reduce the number of key-value pairs.
- Grouped-query attention (Ainslie et al., 2023) generalises multi-query: query heads are split into groups and key-value pairs are shared only within a group, giving a flexible balance between number of query heads and number of key-value pairs.
- Case: Character.AI reports an average dialogue history of 180 messages (2024); with such long sequences the KV cache is the main throughput bottleneck. Multi-query attention, interleaved local and global attention, and cross-layer attention together cut the cache by over 20 times, so memory stopped limiting large batch sizes (PDF p. 825).

#### Optimizing KV cache management (PDF pp. 825-826)
- Good cache management eases the memory bottleneck and allows larger batches, especially for long context.
- vLLM, one of the fastest-growing inference frameworks, became popular for PagedAttention (Kwon et al., 2023): it splits the cache into non-contiguous blocks, reducing fragmentation and allowing flexible memory sharing.
- Other techniques named: KV cache quantization (Hooper et al., 2024; Kang et al., 2024), adaptive KV cache compression (Ge et al., 2023), selective KV cache (Liu et al., 2024).

#### Kernels for attention (PDF pp. 826-827)
- This approach leaves the design and storage alone and speeds up how attention scores are computed, working best when it accounts for the hardware. Chip-specific code is a kernel.
- FlashAttention (Dao et al., 2022) fuses many operators common in transformers. Figure 9-13 (attention on GPT-2) shows a bar chart of time in ms: the PyTorch version is a stack of matmul, mask, softmax, dropout and matmul totalling roughly 16-17 ms (estimate from the chart), while the FlashAttention fused kernel is a single block of about 2 ms (estimate). Per-segment values are not printed.

### Kernels and compilers
- Kernels are specialised code for hardware accelerators such as GPUs and TPUs, written for compute-heavy routines run repeatedly and in parallel. Matrix multiplication, attention and convolution all have specialised kernels per hardware (PDF pp. 827-828).
- Writing them demands deep hardware knowledge, including the memory hierarchy (caches, global memory, shared memory, registers) and how data moves between levels. They are written in low-level languages: CUDA (NVIDIA GPUs), Triton (OpenAI's language for custom kernels), ROCm (AMD GPUs). These give fine control over threads and memory access but are harder than Python (PDF p. 828).
- Historically "a dark art" practised by few: NVIDIA and AMD employ optimization engineers; PyTorch and TensorFlow employ kernel engineers. Rising inference demand and ubiquitous accelerators are drawing more AI engineers in, and tutorials exist (PDF pp. 828-829).
- Four common speed-up techniques (PDF p. 829):
  - Vectorization: process multiple contiguous data elements at once instead of one per loop step, reducing data I/O and latency.
  - Parallelization: split the (n-dimensional) input into independent chunks processed on different cores or threads.
  - Loop tiling: reorder data access in a loop to suit the hardware's memory layout and cache. Hardware-dependent: a good CPU tiling pattern may not suit GPUs.
  - Operator fusion: merge several operators into one pass to avoid redundant memory access, for instance fusing two loops over the same array so data is read and written fewer times.
- Vectorization, parallelization and loop tiling apply broadly across models; operator fusion needs knowledge of a model's specific operators and architecture, so it takes more of optimization engineers' attention (PDF p. 830).
- Kernels are tied to a hardware architecture, so each new architecture needs new kernels. Example: FlashAttention was first built mainly for NVIDIA A100; FlashAttention-3 later targeted H100 (Shah et al., 2024) (PDF p. 830).
- Compilers bridge models and hardware: a model script lists operations; to run on a GPU it must be lowered, and during lowering operations are, where possible, mapped onto specialised kernels (PDF p. 830). Compilers can be standalone (Apache TVM, MLIR, Multi-Level Intermediate Representation) or built into ML and inference frameworks (PDF p. 832).

### PyTorch case study (PDF pp. 831-832)
Steps applied to Llama-7B (PyTorch, 2023): call torch.compile; quantize weights to INT8; further to INT4; add speculative decoding. Figure 9-14 (read from the rendered chart) gives throughput in tokens per second per user: eager 25.5; compile 107.0; int8 157.4; int4 202.1; int4 plus speculative 244.7 (labelled +21%, the gain over int4). A dashed line marks "SOTA 4-bit OSS inference" at roughly 170 (estimate). The run used one 80 GB A100. The book notes it is unclear how each step affected output quality (PDF p. 832). Arithmetic note: 244.7 / 202.1 is about 1.21, matching the +21% label; total gain from eager is about 9.6 times.

## Why it matters
Decoding is slow and expensive, and attention memory limits batch size and context length; these techniques raise throughput and lower latency and cost. The book says speculative decoding does not change output quality (PDF pp. 814-815), while model-level optimization in general can alter model behavior (PDF p. 809), and attention redesign changes the architecture (PDF p. 824). In the PyTorch case study the quality effect of the steps was unclear (PDF p. 832).

## When and how to apply
- Optimization in production usually combines techniques at more than one level (PDF p. 809).
- Start from the commonly used options: weight-only quantization and distillation (PDF p. 811). Speculative decoding is easy to add through frameworks that already support it, and most useful for structured output like code (PDF pp. 814-815).
- Use inference with reference when outputs copy inputs heavily (RAG, code editing, multi-turn chat) (PDF pp. 815-816).
- Attention redesigns must be chosen at training or finetuning time (PDF p. 824); for long-context or large-batch serving the KV cache is the lever to inspect (PDF p. 825).
- INTERPRETATION: use the KV cache formula to estimate cache memory before choosing batch size and context length.

## Alternatives and trade-offs
- Pruning: possible large parameter cuts but harder, smaller practical gains, hardware-dependent sparsity benefit (PDF pp. 810-811).
- Quantization: very easy but near its limit (1 bit floor) (PDF p. 811).
- Speculative decoding: no quality change, needs a draft model (ideally same tokenizer); larger K trades fewer verification calls for lower acceptance (PDF p. 814). Inference with reference: no extra model but only works with heavy overlap (PDF p. 815).
- Parallel decoding: removes sequential dependency but non-intuitive and, for Medusa, hard to implement (PDF p. 820).
- Kernels: strong gains but hardware-specific, requiring rewrites per new accelerator (PDF p. 830).

## Limitations and failure modes
- Full rejection of drafts costs extra verification latency (PDF p. 813).
- Pruned models may lose accuracy and need finetuning (PDF p. 810).
- Case-study numbers are for one model and one GPU, and quality impact was not reported (PDF p. 832).

## Relations
Follows the lead-in C09-005 and the hardware and metrics background (C09-002, C09-003, C09-004); precedes service-level optimization (C09-007). Quantization is detailed in C07-011 and distillation in C08-011.

## Time-sensitive statements
Claims tied to the book's writing date: that pruning is "less common" as of writing, the transformer-based architecture assumption, tool names and support (vLLM, TensorRT-LLM, llama.cpp, FlashAttention-3 for H100), NVIDIA's 1.9x Medusa claim on H200, and the Figure 9-14 throughput numbers on A100 (PDF pp. 809-811, 815, 818, 830-832).
