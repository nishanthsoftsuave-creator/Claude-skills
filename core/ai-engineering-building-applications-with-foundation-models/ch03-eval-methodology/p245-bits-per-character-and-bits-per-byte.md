---
id: C03-006
title: Bits-per-Character and Bits-per-Byte
source_pages: "245"
chapter: 3
concepts: [bits-per-character, bits-per-byte, bpc, bpb, tokenization, compression, character-encoding]
related: [C03-005, C03-007]
time_sensitive: false
---
# Bits-per-Character and Bits-per-Byte
(Source: PDF p. 245; continues on PDF p. 246)

## What the section covers
Why bits per token cannot be compared across models, how bits-per-character (BPC) and bits-per-byte (BPB) fix this, and what BPB says about compression.

## Meaning
- Entropy and cross entropy are measured in bits. A cross entropy of 6 bits means the model needs 6 bits to represent each token (PDF p. 245).
- Models tokenize differently (one may use words, another characters), so bits per token is not comparable between models (PDF p. 245).
- BPC is a workaround: divide bits per token by the average characters per token. Example: 6 bits per token and 2 characters per token gives BPC = 6/2 = 3 (PDF p. 245).
- BPC has its own problem: character encodings differ. ASCII uses 7 bits per character, while UTF-8 uses between 8 and 32 bits per character (PDF pp. 245-246).
- A more standard metric is bits-per-byte (BPB): the bits a model needs to represent one byte of the original training data (PDF p. 246).

## How it works
Worked example from the book: BPC = 3 and each character is 7 bits, which is 7/8 of a byte. Then BPB = BPC / (7/8) = 3 / (7/8) = 3.43 (PDF p. 246).

## Evaluation and success criteria
Cross entropy indicates how efficiently a model could compress text. With BPB 3.43, each original byte (8 bits) is represented in 3.43 bits, so the model could compress the training text to less than half its original size (PDF p. 246).

## Relations
Follows cross entropy (C03-005); perplexity (C03-007) follows on the same page 246.
