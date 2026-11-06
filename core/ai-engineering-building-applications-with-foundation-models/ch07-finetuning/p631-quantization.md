---
id: C07-011
title: Quantization
source_pages: "631-637"
chapter: 7
concepts: [quantization, post-training-quantization, quantization-aware-training, low-precision, mixed-precision, weight-quantization, bitnet, memory-footprint]
related: [C07-010, C07-012, C07-013]
time_sensitive: true
---
# Quantization
(Source: PDF pp. 631-637; the section's closing paragraphs on mixed-precision training run onto PDF p. 638 above the "Finetuning Techniques" heading, which belongs to C07-012)

## What the section covers
The last part of the "Memory Bottlenecks" discussion in Chapter 7: how reducing the number of bits per value shrinks a model's memory footprint, what and when to quantize, the split between inference (post-training) quantization and training quantization, and the pitfalls of low precision. The text above the "Quantization" heading on PDF p. 631 (the BF16 versus FP16 comparison and the warning about loading a model in its intended format) belongs to the preceding numerical-representations row (C07-010).

## Meaning
- Quantization (reduced precision) means representing a model's values with fewer bits. A 10B-parameter model needs 40 GB for weights in a 32-bit format but 20 GB in a 16-bit format (PDF p. 631).
- The book calls it a cheap and extremely effective way to cut memory: easy to do and it generalizes across tasks and architectures (PDF p. 631). "Low precision" in ML generally means any format with fewer bits than the standard FP32 (PDF p. 632).
- Terminology note: strictly, it is quantization only when the target format is integer; in practice the word is used for every technique that converts values to a lower-precision format, and the book follows that usage to match the literature (PDF p. 632).

## How it works

### What to quantize
- Ideally quantize whatever eats most memory, limited by what can be quantized without hurting performance too much. At inference the main memory consumers are weights and activations (see "Memory Math") (PDF p. 632).
- Weight quantization is more common than activation quantization, because the effect of quantizing weights on performance is steadier and the accuracy loss smaller (the text says "weight activation" in that sentence, which appears to mean activation) (PDF p. 632).

### When to quantize
Quantization can occur during training or after it. Post-training quantization (PTQ) means quantizing a fully trained model; it is by far the most common and the most relevant to application developers who do not usually train models (PDF p. 633).

### Inference quantization
- Early deep learning trained and served in FP32. Since the late 2010s serving in 16 bits and lower has become increasingly common (PDF p. 633).
- Examples: Dettmers et al. (2022) quantized LLMs to 8 bits with LLM.int8() and to 4 bits with QLoRA (2023) (PDF p. 633).
- Mixed-precision serving keeps values low-precision where possible and higher-precision where needed. Apple (2024) used a mix of 2-bit and 4-bit formats averaging 3.5 bits per weight to serve models on-device. In 2024 NVIDIA announced Blackwell, a GPU architecture supporting 4-bit float inference, anticipating 4-bit networks (PDF p. 633).
- At 8 bits and below it gets trickier. Values can stay floating-point in minifloat formats such as FP8 and FP4, but more commonly they are converted to integers such as INT8 or INT4 (PDF pp. 633-634).
- There is a floor: nothing can go below 1 bit per value. Attempts at 1-bit include BinaryConnect (2015), Xnor-Net (2016) and BitNet (2023) (PDF p. 634).
- In 2024 Microsoft researchers (Ma et al.) announced BitNet b1.58, a transformer language model needing only 1.58 bits per parameter, with performance comparable to 16-bit Llama 2 up to 3.9B parameters (PDF p. 634).

### Table 7-4 (BitNet b1.58 versus 16-bit Llama on benchmarks)
The table is clipped at the right edge in the PDF: only the columns Model, Size, ARCe, ARCc and HS are legible, and the caption is cut ("on different benchmarks an..."). Legible values (model, size, ARCe / ARCc / HS) (PDF p. 635):
- Llama LLM 700M: 54.7 / 23.0 / 37.0; BitNet b1.58 700M: 51.8 / 21.4 / 35.1
- Llama LLM 1.3B: 56.9 / 23.5 / 38.5; BitNet b1.58 1.3B: 54.9 / 24.2 / 37.7
- Llama LLM 3B: 62.1 / 25.6 / 43.3; BitNet b1.58 3B: 61.4 / 28.3 / 42.9
- BitNet b1.58 3.9B: 64.2 / 28.7 / 44.2 (no Llama row at that size)
UNVERIFIED: any columns to the right of HS, and the end of the caption, are not visible in the PDF.
The pattern in the legible columns: BitNet is lower than Llama on all three at 700M; at 1.3B and 3B it is lower on ARCe and HS but higher on ARCc (24.2 vs 23.5, 28.3 vs 25.6), with the gaps narrowing as size grows. The HS column's right edge is flush against the clip, but its values read fully.

### Why reduced precision speeds things up
- It allows a larger batch size, so more inputs are processed in parallel; and it makes the arithmetic itself faster, cutting inference latency and training time (PDF p. 635).
- Illustration: adding two numbers bit by bit at t nanoseconds per bit takes 32t ns at 32 bits but 16t ns at 16 bits. Latency does not always fall, however, because format conversion adds computation (PDF p. 635).

## Limitations and failure modes
- Every conversion usually changes a value slightly, and many small changes can add up to a large performance change. A value outside the range of the lower-precision format may become infinity or an arbitrary value, further degrading quality (PDF p. 636).
- Reducing precision with minimal damage is an active research area for model developers, hardware makers and application developers (PDF p. 636).

## When and how to apply
- Inference in lower precision is now standard: train in higher precision for maximum quality, then reduce precision for serving. PyTorch, TensorFlow and Hugging Face transformers offer PTQ for free in a few lines of code (PDF p. 636).
- Some edge devices only support quantized inference, so on-device frameworks (TensorFlow Lite, PyTorch Mobile) also offer PTQ (PDF p. 636).

### Training quantization
Less common than PTQ but growing. It has two distinct goals, and a technique may serve one or both (PDF pp. 636-637):
1. Produce a model that performs well in low precision at inference, countering the quality loss that PTQ can cause.
2. Cut training time and cost: lower memory lets you train on cheaper hardware or train a bigger model on the same hardware, and faster arithmetic lowers cost further.

- Quantization-aware training (QAT) simulates low-precision (for example 8-bit) behavior during training so the model learns to produce good outputs in low precision. It serves goal 1 only: computation is still done in high precision, so QAT does not shorten training and can lengthen it because of the simulation work (PDF p. 637).
- Training directly in lower precision can serve both goals. Attempts date to 2016 (Hubara et al.; Jacob et al., 2017). Character.AI (2024) reported training fully in INT8, which removed the training/serving precision mismatch and greatly improved training efficiency. It is harder, because backpropagation is more sensitive to low precision (PDF p. 637).
- Low-precision training is often mixed precision: a higher-precision copy of the weights is kept while gradients and activations are lower-precision. Less sensitive weights can be computed in low precision and more sensitive ones in high precision. Example: LLM-QAT (Liu et al., 2023) quantizes weights and activations to 4 bits but keeps embeddings at 16 bits (PDF p. 638).
- Automatic mixed precision (AMP), offered by many frameworks, can pick automatically which parts run in lower precision (PDF p. 638).
- Phases can differ in precision. A model may be trained in higher precision and finetuned in lower precision. This is common for foundation models: the originating organization has compute for high-precision training, and developers with less compute finetune the published model in lower precision (PDF p. 638).

## Relations
Follows the numerical-representations row (C07-010) and the memory math it builds on; the next heading (C07-012) turns the memory discussion into finetuning techniques. QLoRA, mentioned here as a 4-bit example, is treated in C07-013.

## Time-sensitive statements
Apple's 3.5-bit scheme, NVIDIA Blackwell 4-bit support, BitNet b1.58 results, Character.AI's INT8 training, and the statement that PTQ and low-precision serving are standard reflect 2024 writing (PDF pp. 633-637).
