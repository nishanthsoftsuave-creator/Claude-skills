---
id: C03-007
title: Perplexity
source_pages: "246-247"
chapter: 3
concepts: [perplexity, ppl, exponential-of-entropy, bits, nats, cross-entropy, uncertainty]
related: [C03-004, C03-005, C03-006, C03-008]
time_sensitive: false
---
# Perplexity
(Source: PDF pp. 246-247)

## What the section covers
The definition of perplexity as the exponential of entropy and cross entropy, its intuitive meaning, a worked example, and the bit versus nat unit issue.

## Meaning
- Perplexity (PPL) is the exponential of entropy and of cross entropy (PDF p. 246).
- For a dataset with true distribution P: PPL(P) = 2^H(P), where H(P) is the entropy in bits. For a model with learned distribution Q on that dataset: PPL(P, Q) = 2^H(P, Q), where H(P, Q) is the cross entropy in bits (PDF p. 246, formulas checked on the rendered page).
- Where cross entropy captures how hard next-token prediction is, perplexity captures the uncertainty the model has when predicting it. Higher uncertainty means more candidate next tokens (PDF pp. 246-247).

## How it works: example
A model that has perfectly learned the four position tokens of Figure 3-4(b) has a cross entropy of 2 bits. Predicting a position, it must choose among 2^2 = 4 options, so its perplexity is 4 (PDF p. 247). The page as printed and rendered reads "2 = 4", with the superscript missing in the book itself; INTERPRETATION: the intended expression is 2 squared = 4, consistent with PPL = 2^H and the 2-bit cross entropy.

## Units: bits versus nats
- Bits underlie the base 2 in the formula, since each bit stands for 2 values (PDF p. 247).
- Popular frameworks such as TensorFlow and PyTorch use nats (natural log, base e). With nats, PPL(P, Q) = e^H(P, Q) (PDF p. 247).
- Because of this bit/nat confusion, many people report perplexity rather than cross entropy when stating a model's performance (PDF p. 247).

## Relations
Defined from entropy (C03-004) and cross entropy (C03-005); BPC/BPB in C03-006. Interpretation and use cases, plus the formula for computing perplexity from token probabilities, are in C03-008.
