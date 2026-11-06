---
id: C03-009
title: Exact Evaluation (Lead-in) and Computing Perplexity
source_pages: "252"
chapter: 3
concepts: [exact-evaluation, subjective-evaluation, perplexity-computation, logprobs, functional-correctness, similarity-measurement, open-ended-evaluation, close-ended-evaluation]
related: [C03-007, C03-008, C03-010, C03-011, C03-013]
time_sensitive: false
---
# Exact Evaluation (Lead-in) and Computing Perplexity
(Source: PDF p. 252, continuing onto PDF p. 253)

## What the section covers
The close of the language-modeling-metrics discussion, a sidebar on computing a text's perplexity from a model, and the opening of "Exact Evaluation", which separates exact from subjective evaluation and says which approaches the section covers.

## Perplexity as a proxy
Perplexity and the related metrics describe the performance of the underlying language model, which stands in as a proxy for performance on downstream tasks. The rest of the chapter turns to measuring downstream performance directly (PDF p. 252).

## How it works: sidebar on computing a text's perplexity
- A model's perplexity for a text measures how hard it is for the model to predict that text (PDF p. 252).
- For language model X and token sequence [x1, x2, ..., xn], the perplexity (formula read from the rendered page) is:
  PPL = P(x1, x2, ..., xn)^(-1/n) = (1 / P(x1, x2, ..., xn))^(1/n) = ( product over i = 1..n of 1 / P(xi | x1, ..., x(i-1)) )^(1/n)
  where P(xi | x1, ..., x(i-1)) is the probability X assigns to token xi given the preceding tokens (PDF p. 252). In words: the inverse of the sequence probability, taken to the n-th root.
- Computing it requires the probabilities (or logprobs) the model gives each next token. Not every commercial model exposes its logprobs, as discussed in Chapter 2 (PDF p. 252).

## Meaning: exact versus subjective evaluation
- When evaluating performance, distinguish exact from subjective evaluation (PDF p. 252). Exact evaluation yields a judgment with no ambiguity: if a multiple-choice answer is A and you choose B, you are wrong (PDF pp. 252-253).
- Essay grading is subjective: the score depends on the grader, and the same person asked twice at different times may give different scores. Clear grading guidelines can make it more exact (PDF p. 253).
- AI as a judge, covered later, is subjective: results can change with the judge model and the prompt (PDF p. 253).

## Scope of the Exact Evaluation section
- Two approaches that give exact scores are covered: functional correctness and similarity measurements against reference data (PDF p. 253).
- The focus is open-ended responses (arbitrary text generation), not close-ended ones such as classification. This is not because foundation models are not used for close-ended tasks; many systems include a classification component, typically for intent classification or scoring. It is because close-ended evaluation is already well understood (PDF p. 253).

## Relations
The perplexity definition is C03-007, with interpretation in C03-008. Functional correctness is C03-010; similarity measurements are C03-011; AI as a judge begins at C03-013.
