---
id: C05-006
title: Prompt Engineering Best Practices (Section Lead-in)
source_pages: "431"
chapter: 5
concepts: [prompt-engineering-best-practices, prompt-tricks, outdated-tips, model-specific-quirks, prompt-libraries]
related: [C05-005, C05-001]
time_sensitive: true
---
# Prompt Engineering Best Practices (Section Lead-in)
(Source: PDF p. 431 from the heading "Prompt Engineering Best Practices" onward, plus the lead-in paragraphs at the top of PDF p. 432 that precede the heading "Write Clear and Explicit Instructions", which belongs to the next row. The paragraphs above the heading on p. 431 belong to C05-005.)

## What the section covers
The framing for the best-practices section: why early prompt hacks age badly, and what kind of guidance this section will offer.

## Meaning and why it matters
- Prompt engineering can be very hacky, especially with weaker models. Early guides recommended tricks such as writing "Q:" instead of "Questions:" or promising the model a "$300 tip for the right answer" (PDF p. 431).
- Such tips can help some models, but they tend to become outdated as models follow instructions better and become more robust to prompt perturbation (PDF p. 431).

## What the section offers
- It focuses on general techniques that have worked across a wide range of models and will likely stay relevant for the near future (PDF p. 432).
- They were distilled from prompt engineering tutorials by model providers (OpenAI, Anthropic, Meta, Google) and from practices shared by teams that deployed generative AI applications successfully (PDF p. 432).
- These providers also publish libraries of pre-crafted prompts for reference (Anthropic, Google, OpenAI) (PDF p. 432).

## Limitations
Beyond the general practices, each model probably has quirks that respond to particular tricks, so when working with a model you should seek out prompt guides specific to it (PDF p. 432).

## When and how to apply
INTERPRETATION: prefer the general practices over folklore tricks, and re-test any model-specific trick when the model version changes.

## Relations
Follows the prompt-components discussion ending in C05-005 (system prompt, user prompt, examples, context are the key prompt components). The first concrete practice, clear and explicit instructions, begins the next row. Connects back to the chapter's rigor stance (C05-001).

## Time-sensitive statements
The examples of tricks and the provider guide libraries reflect the state at the time of writing.
