---
id: C04-002
title: Evaluation Criteria - Evaluation-Driven Development
source_pages: "316-318"
chapter: 4
concepts: [evaluation-driven-development, evaluation-criteria, return-on-investment, lamppost-bias, functional-correctness, close-ended-tasks]
related: [C04-001, C04-003, C04-004]
time_sensitive: false
---
# Evaluation Criteria - Evaluation-Driven Development
(Source: PDF pp. 316-318)

## What the section covers
The lead-in to the Evaluation Criteria section: why an application that cannot be evaluated is a liability, the book's principle of evaluation-driven development, which kinds of applications are most common in production because they are easy to evaluate, and the caution that this bias hides valuable applications.

## Meaning
- **Evaluation-driven development**: before investing time, money and resources in an application, understand how it will be evaluated. The author coins this name by analogy with test-driven development, where tests are written before code. In AI engineering it means defining the evaluation criteria before building (PDF p. 317).

## Why it matters
- The author's conference question: which is worse, an application never deployed, or one deployed with nobody knowing whether it works? Most people answered the latter, and the book agrees. An application that can't be evaluated costs money to maintain, and taking it down may cost even more (PDF p. 316).
- AI applications with questionable return on investment are common. Two reasons: the applications are hard to evaluate, and developers lack visibility into how the applications are used (PDF p. 316).
- Examples of that blindness (PDF p. 316):
  - An ML engineer at a used car dealership said his team built a model to predict a car's value from specs the owner supplied. A year after deployment users seemed to like it, but he had no idea whether the predictions were accurate.
  - At the start of the ChatGPT fever, companies rushed to deploy customer support chatbots, and many are still unsure whether the chatbots help or hurt the user experience.
- Sensible business decisions rest on return on investment, not hype, and applications must demonstrate value to be deployed (PDF p. 318).

## How it works: applications with clear criteria dominate production
The most common enterprise applications are those with clear evaluation criteria (PDF p. 318):
- Recommender systems: success is measurable as increased engagement or purchase-through rates.
- Fraud detection: success is measurable as money saved by prevented fraud.
- Coding: unlike other generation tasks, generated code can be evaluated by functional correctness.
- Close-ended uses of foundation models, such as intent classification, sentiment analysis and next-action prediction. Although foundation models are open-ended, many of their use cases are close-ended, and classification is much easier to evaluate than open-ended tasks.

## Limitations and failure modes
- Restricting oneself to applications whose outcomes can be measured is likened to looking for a lost key under the lamppost at night: easier, but that doesn't mean the key is there. Potentially game-changing applications may be skipped because they have no easy evaluation (PDF p. 318).

## When and how to apply
- Begin an AI application with a list of evaluation criteria specific to it, decided before building (PDF p. 317).
- The lamppost caution implies that better evaluation methods widen the set of applications worth building; the author's explicit statement of this idea falls on the next page and belongs to the following row.

## Relations
Follows the chapter preview (C04-001). The criteria buckets that this lead-in leads to (domain-specific capability, generation capability, instruction following, cost and latency) begin in C04-003, and later criteria sections continue from there (C04-004 onward). Functional correctness and exact evaluation come from Chapter 3.
