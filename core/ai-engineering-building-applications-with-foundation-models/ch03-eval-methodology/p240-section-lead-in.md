---
id: C03-003
title: Understanding Language Modeling Metrics (Lead-in)
source_pages: "240-241"
chapter: 3
concepts: [language-modeling-metrics, cross-entropy, perplexity, bits-per-character, bits-per-byte, autoregressive-models, training-data-distribution]
related: [C03-004, C03-005, C03-007, C03-008, C03-002]
time_sensitive: false
---
# Understanding Language Modeling Metrics (Lead-in)
(Source: PDF pp. 240-241, with the end of the lead-in on PDF p. 242)

## What the section covers
Why a rough grasp of language modeling metrics is useful, which metrics exist (cross entropy, perplexity, BPC, BPB), how they relate, and a reminder of what a language model learns.

## Why it matters
- Foundation models grew out of language models, and many still have a language model as a main component. For such models, performance of that component tends to correlate well with the foundation model's downstream performance (Liu et al., 2023), so understanding the metrics helps in understanding downstream performance (PDF p. 240).
- Even if you never train or finetune a language model, knowing these metrics helps when choosing which models to use. They can also occasionally serve in certain evaluation and data deduplication techniques mentioned elsewhere in the book (PDF p. 242).

## Meaning
- Language modeling goes back decades, popularized by Claude Shannon's 1951 paper "Prediction and Entropy of Printed English". The metrics guiding it have changed little since (PDF p. 241).
- Most autoregressive language models are trained with cross entropy or its relative, perplexity. Papers and model reports may also report bits-per-character (BPC) and bits-per-byte (BPB), both variations of cross entropy (PDF p. 241).
- The four metrics are closely linked: given one value and the needed extra information, the other three can be computed. Although called language modeling metrics, they apply to any model generating token sequences, including non-text tokens (PDF p. 241).

## How it works: what is being measured
- A language model encodes statistical information about a language, meaning how likely a token is in a given context. Given "I like drinking __", "tea" is statistically more likely than "charcoal". The more of this statistical information a model captures, the better it predicts the next token (PDF p. 241).
- In ML terms the model learns the distribution of its training data. The better it learns, the better it predicts what follows in that data and the lower its training cross entropy (PDF p. 241).
- As with any ML model, what matters is also performance on production data rather than training data alone. In general, the closer your data resembles the training data, the better the model performs on it (PDF pp. 241-242).

## Assumptions and prerequisites
The author warns that this section is math-heavy compared with the rest of the book. A reader who finds it confusing may skip the math and focus on how to interpret the metrics (PDF p. 242).

## Relations
Builds on Chapter 1's treatment of language modeling. The detailed treatment follows: entropy (C03-004), cross entropy (C03-005), perplexity (C03-007) and its interpretation and computation (C03-008). The challenge motivating a proxy such as this is in C03-002.
