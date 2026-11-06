---
id: C03-005
title: Cross Entropy
source_pages: "244"
chapter: 3
concepts: [cross-entropy, kl-divergence, entropy, training-objective, true-distribution, learned-distribution]
related: [C03-004, C03-006, C03-007]
time_sensitive: false
---
# Cross Entropy
(Source: PDF p. 244; continues on PDF p. 245)

## What the section covers
What cross entropy measures for a language model, what it is made of, the formula relating it to entropy and KL divergence, and what it means when training succeeds.

## Meaning
- Training a language model means getting it to learn the distribution of its training data, that is, to predict what comes next in that data. The model's cross entropy on a dataset measures how hard the model finds that prediction task (PDF p. 244).
- Cross entropy depends on two things (PDF p. 244): (1) how predictable the training data is, which is the data's entropy; and (2) how far the distribution the model has learned departs from the true distribution of the data.
- Notation: entropy and cross entropy both use the letter H. P is the true distribution of the training data, Q is the distribution the model learned. The data's entropy is H(P). The divergence of Q from P is the Kullback-Leibler (KL) divergence, written D_KL(P||Q) (PDF p. 244).

## How it works
Formula: H(P, Q) = H(P) + D_KL(P||Q), where H(P, Q) is the model's cross entropy with respect to the training data, H(P) is the entropy of the data and D_KL(P||Q) is the KL divergence of Q with respect to P (PDF p. 244).

Further points (PDF p. 245):
- Cross entropy is not symmetric: H(P, Q) differs from H(Q, P).
- A language model is trained to minimize its cross entropy on the training data.
- If learning were perfect, Q would equal P, the KL divergence would be 0, and the cross entropy would equal the entropy of the training data exactly.
- So a model's cross entropy can be read as its approximation of the entropy of its training data.

## Relations
Builds on entropy (C03-004). Its unit and per-character variants are in C03-006; perplexity (C03-007) is the exponential of it.
