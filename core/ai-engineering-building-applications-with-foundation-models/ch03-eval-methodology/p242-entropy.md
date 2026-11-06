---
id: C03-004
title: Entropy
source_pages: "242-243"
chapter: 3
concepts: [entropy, information, bits, tokens, predictability, language-modeling-metrics]
related: [C03-003, C03-005, C03-007]
time_sensitive: false
---
# Entropy
(Source: PDF pp. 242-243)

## What the section covers
The first of the language-modeling metrics, entropy, explained through a toy language that describes positions in a square. (The warning that this part of the chapter is mathematical sits above the Entropy heading and belongs to C03-003.)

## Why it matters
The author says this part is heavier on math than the rest of the book, and that a reader who finds it confusing may skip the derivations and concentrate on how the metrics are interpreted (PDF p. 242). Even people who never train or finetune a language model benefit, because these metrics help them judge which model to adopt for an application, and they sometimes serve in evaluation and data-deduplication techniques mentioned elsewhere in the book (PDF p. 242). The page also repeats a general rule: the closer your data is to a model's training data, the better the model tends to do on it (PDF p. 242).

## Meaning
- Entropy is the average amount of information carried by one token. A higher entropy means each token tells you more, and also that more bits are needed to encode a token (PDF p. 242).
- Intuitively it is a measure of how hard it is to predict what comes next in a language. Lower entropy means each token carries less information and the language is more predictable (PDF p. 243).
- Analogy given: if you could predict exactly what someone is going to say, their words would add no new information (PDF p. 243).

## How it works: the square example (Figure 3-4)
Figure 3-4 shows two small languages for locating a position inside a square. Panel (a) splits the square into two halves (tokens 1 and 2), panel (b) into four quadrants numbered 1 to 4 (PDF p. 243).
- Language (a), two tokens: each token says whether the position is upper or lower. Two tokens need only one bit, so the entropy is 1 (PDF pp. 242-243).
- Language (b), four tokens: each token names a quadrant (upper-left, upper-right, lower-left, lower-right). Four tokens need two bits, so the entropy is 2 (PDF p. 243).
- The point of the caption: language (b)'s tokens are more informative but cost more bits. Language (a) is easier to predict, since you choose between two tokens rather than four (PDF p. 243).

INTERPRETATION: in this example entropy equals the number of bits needed per token when all tokens are equally likely (log base 2 of the token count); the book states the two values (1 and 2) without a general formula on these pages.

## Relations
Entropy is the building block for cross entropy (C03-005) and perplexity (C03-007), which are defined from it. The lead-in to this subsection is C03-003.
