---
id: C02-010
title: Sampling Section Lead-in
source_pages: "187"
chapter: 2
concepts: [sampling, probabilistic-outputs, temperature, top-k, top-p, constrained-sampling]
related: [C02-009, C02-011]
time_sensitive: false
---
# Sampling Section Lead-in
(Source: PDF p. 187)

## What the section covers
The opening of the Sampling section: what it will discuss and why the probabilistic nature of outputs matters.

## Meaning
- A model constructs its outputs through a process called sampling (PDF p. 187).

## Scope of the section
- It will discuss different sampling strategies and sampling variables, including temperature, top-k and top-p (PDF p. 187).
- It then looks at sampling multiple outputs to improve performance, which, as the book puts it for best of N in the previous section, relies on how a model samples its outputs (PDF p. 187).
- It also covers modifying the sampling process so models generate responses that follow certain formats and constraints (PDF p. 187).

## Why it matters
Sampling makes AI outputs probabilistic. The book says understanding this probabilistic nature is important for handling behaviors such as inconsistency (PDF p. 187) and hallucination. This sentence is split across a page boundary: it ends at the top of the next page, where the book adds that the section closes with a deep dive into what the probabilistic nature means and how to work with it.

## Relations
Follows the closing remarks of preference finetuning (C02-009). The basics of sampling begin in C02-011.
