---
id: C02-011
title: Sampling Fundamentals
source_pages: "188-190"
chapter: 2
concepts: [sampling, greedy-sampling, probability-distribution, logits, vocabulary, classification, next-token]
related: [C02-010, C02-009]
time_sensitive: false
---
# Sampling Fundamentals
(Source: PDF pp. 188-190)

## What the section covers
How a neural network turns an input into probabilities over outcomes, why always picking the most likely token (greedy sampling) is poor for language models, and what logits are. The page range ends mid-sentence, just as the conversion of logits to probabilities begins.

## Meaning
- A neural network produces its output by first computing probabilities of possible outcomes. For a classifier these are the classes (PDF p. 188). Example: a spam model has two outcomes, spam and not spam, with probabilities like 90% and 10%. You then decide using the probabilities, for instance flagging anything above 50% spam probability (PDF p. 188).
- A language model computes, for the next token, a probability distribution over all tokens in the vocabulary (Figure 2-14) (PDF p. 188).
- Greedy sampling means always picking the highest-probability outcome. It often suits classification: if an email is more likely spam than not, marking it spam makes sense (PDF p. 189).
- A logit is the raw value a neural network outputs for each possible outcome. For a language model, each logit corresponds to one vocabulary token, so the logit vector has the size of the vocabulary (PDF p. 190).

## How it works
- Figure 2-14 shows the prompt "What's your favorite color?" with a distribution over tokens: "green" 50%, "red" 30%, "a" 0.1%, "the" 0.2%, and so on (PDF p. 189).
- For language models greedy sampling produces boring output: imagine a model that answers every question with the most common words (PDF p. 189).
- Instead, the model samples the next token according to the distribution. With "My favorite color is ...", if "red" has 30% and "green" 50%, red is chosen 30% of the time and green 50% (PDF p. 189).
- Figure 2-15 shows an input going into a neural network that emits a logit vector with one number per token, for example -0.5 for "a", 0.7 for "green", -0.2 for "house", 0.5 for "red", -1.2 for "the" (PDF p. 190).
- Larger logits correspond to higher probabilities, but logits are not probabilities: they do not sum to one and can be negative, whereas probabilities must be non-negative. Converting logits to probabilities is the next step, which continues on the following page (PDF p. 190).
- The text layer of PDF p. 189 shows a stray "=" in "most likely outcome = is called greedy sampling"; the rendered page shows the same, so it looks like a typo in the book.

## When and how to apply
INTERPRETATION: greedy choice suits classification-style outputs, while sampling from the distribution is what gives language model output variety.

## Relations
INTERPRETATION (cross-links, not content of these pages): this row opens the mechanics behind the sampling variables announced in C02-010, and best of N from C02-009 relies on how a model samples.
