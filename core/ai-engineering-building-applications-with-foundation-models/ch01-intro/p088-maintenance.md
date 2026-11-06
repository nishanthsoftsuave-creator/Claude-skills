---
id: C01-018
title: Maintenance
source_pages: "88-90"
chapter: 1
concepts: [maintenance, rapid-change, inference-cost, mmlu, cost-benefit-analysis, model-api-convergence, regulation, intellectual-property]
related: [C01-016, C01-017, C01-019]
time_sensitive: true
---
# Maintenance
(Source: PDF pp. 88-90; transition at the start of PDF p. 91)

## What the section covers
Why planning continues after goals are met: an AI product must be maintained against a very fast-moving field, where even favorable changes cause friction, some are easy to absorb, some are hard (regulation), and some can be fatal (intellectual property).

## Meaning
- Product planning does not end when goals are achieved; one must think about how the product will change over time and how it will be maintained (PDF p. 88).
- AI adds a challenge: the field has moved extremely fast for a decade and will probably keep doing so. Building on foundation models means "committing to riding this bullet train" (PDF p. 88).

## Good changes
- Model limitations are being addressed: context lengths grow, outputs improve, and inference (computing an output from an input) gets faster and cheaper (PDF p. 88).
- The text introduces Figure 1-11 as the evolution of inference cost and model performance between 2022 and 2024 on MMLU (Massive Multitask Language Understanding, Hendrycks et al., 2020), a popular foundation model benchmark (PDF p. 88).
- Figure 1-11 (PDF p. 89, rendered and read), titled "MMLU Performance vs. Cost Over Time (2022-2024)", is a scatter plot with MMLU accuracy on the x axis (about 25 to 90%) and cost per million tokens on a log y axis (about $0.1 to $100, the average of input and output price). Points are colored by year (2022, 2023, 2024) and labeled by model, and a few dashed vertical lines mark models (for example Gemma 7B, Grok-1, Grok-1.5, Gemini Ultra) and one dashed horizontal line marks GPT-4.5-turbo. It is credited to Katrina Nguyen (2024); the caption says "The cost of AI reasoning rapidly drops over time."
- Reading it (approximate, estimates from the chart): the 2022 models (GPT-3 Curie and Davinci, GPT-3.5 text-davinci) sit between roughly 26% and 65% accuracy at about $2-$60 per million tokens. Several 2023-2024 models reach similar or higher accuracy at far lower prices (for example Llama 2 7B near 45% at about $0.2, Mistral 7B near 62% at about $0.25, Claude 3 Haiku near 75% at about $0.8), while the top-accuracy models of 2023-2024 (GPT-4 and Claude 3 Opus, about 86-87%) are still among the most expensive. Per-point values are not printed in the book and are not transcribed here.

## Even good changes cause friction
- You must keep guard and run a cost-benefit analysis of each technology investment; the best option today may become the worst tomorrow (PDF p. 89).
- Example 1: building a model in-house because it seems cheaper than a provider, then discovering after three months that providers halved their prices (PDF p. 89).
- Example 2: investing in a third-party solution and tailoring infrastructure around it, then the provider goes out of business after failing to get funding (PDF p. 89).

## Changes that are easier to adapt to
- Providers are converging on the same API, so swapping one model API for another is easier (PDF pp. 89-90).
- Each model still has quirks, strengths and weaknesses, so developers must adjust workflows, prompts and data to the new model. Without infrastructure for versioning and evaluation, this causes many headaches (PDF p. 90).

## Changes that are harder to adapt to
- Regulation. AI technologies are treated as national security issues in many countries, so compute, talent and data are heavily regulated (PDF p. 90).
- GDPR was estimated to have cost businesses $9 billion to become compliant (PDF p. 90).
- Compute availability can shift overnight with new laws on who may buy and sell compute (the book cites the US October 2023 Executive Order). If a GPU vendor were suddenly banned from selling to your country, you would be in trouble (PDF p. 90).

## Changes that can be fatal
Intellectual property rules around AI are still evolving. If a product is built on a model trained on other people's data, one cannot be certain the product's IP will always be one's own. The author reports that many IP-heavy companies, such as game studios, hesitate to use AI for fear of losing their IP later (PDF p. 90).

## When and how to apply
INTERPRETATION: keep versioning and evaluation infrastructure in place so model swaps are testable, and re-run build-versus-buy cost comparisons periodically.

## Transition
The book ends the planning discussion by noting that once committed to building an AI product, the next step is to look at the engineering stack required (PDF p. 91).

## Relations
Extends Milestone Planning (C01-017) and goal setting (C01-016). The stack discussion begins at C01-019.

## Time-sensitive statements
The GDPR cost estimate, the October 2023 executive order, and the 2022-2024 MMLU cost trend in Figure 1-11 reflect the date of writing.
