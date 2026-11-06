---
id: C07-007
title: Memory Bottlenecks (section lead-in)
source_pages: "618-619"
chapter: 7
concepts: [memory-bottleneck, finetuning-memory, peft, quantization, trainable-parameters, numerical-precision, mixed-precision]
related: [C07-006, C07-008, C07-009, C07-010, C07-011]
time_sensitive: false
---
# Memory Bottlenecks (section lead-in)
(Source: PDF pp. 618-619; the last two key takeaways continue at the top of the next page and are summarised below without a page cite)

## What the section covers
The introduction to the Memory Bottlenecks section: why finetuning is memory-hungry, what the section will explain, and a list of key takeaways for readers who want to skip the technical material.

## Why it matters
- Finetuning is memory-intensive, so many finetuning techniques are designed to shrink the memory footprint. Knowing where the bottleneck comes from is needed to understand why and how those techniques work, and helps you pick the method that suits you (PDF p. 618).
- The section also gives formulas for back-of-the-napkin estimates of a model's memory use, useful for working out what hardware you need to serve or finetune a model (PDF p. 618).
- The author warns that the section is technically dense because memory calculation requires unpacking low-level ML and computing concepts; readers already familiar with them may skip it (PDF p. 618).

## Key takeaways (the book's skip-ahead list)
1. Foundation models are so large that memory is a bottleneck for both inference and finetuning. Finetuning typically needs far more memory than inference because of how neural networks are trained (PDF p. 619).
2. Three things drive the memory footprint during finetuning: the number of parameters, the number of trainable parameters, and the numerical representations used (PDF p. 619).
3. More trainable parameters means more memory. Cutting trainable parameters lowers finetuning memory, and this is the motivation for PEFT (parameter-efficient finetuning) (PDF p. 619).
4. Quantization means converting a model from a format with more bits to one with fewer. It is a simple, effective way to cut memory. Worked example from the book: a 13-billion-parameter model in FP32 uses 4 bytes per weight, so 13B x 4 = 52 GB for the weights; at 2 bytes per value that falls to 26 GB (PDF p. 619).
5. Inference is typically run with as few bits as possible, such as 16, 8 or even 4 bits (stated at the top of the next page).
6. Training is more sensitive to numerical precision, so training in low precision is harder. It is usually done in mixed precision: some operations in higher precision (for example 32-bit) and some in lower (16-bit or 8-bit) (stated at the top of the next page).

The takeaways introduce concepts developed in the following rows: trainable parameters and backpropagation (C07-008), the memory formulas (C07-009), numerical formats (C07-010) and quantization (C07-011).

## Relations
Follows the finetuning-versus-RAG decision (C07-006), whose closing sentence names memory as the number one challenge of finetuning.
