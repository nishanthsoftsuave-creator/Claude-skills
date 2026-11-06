---
id: C02-001
title: Chapter 2 Introduction - Understanding Foundation Models
source_pages: "119-120"
chapter: 2
concepts: [foundation-models, design-decisions, training-data, architecture, model-size, post-training, sampling]
related: [C02-002, C02-003, C02-004]
time_sensitive: false
---
# Chapter 2 Introduction - Understanding Foundation Models
(Source: PDF pp. 119-120, with the closing lines of the intro on PDF p. 121)

## What the section covers
The framing of the whole chapter: why an application builder should understand how foundation models are made, which design decisions the chapter will examine, and how the chapter is organised. It is a roadmap, not a technical section.

## Meaning
- The chapter's premise is that you need a foundation model before you can build on one. You do not have to know how to develop a model to use it, but a high-level grasp helps you pick a model and decide how to adapt it (PDF p. 119).
- Training a foundation model is described as extremely complex and costly. The people who do it well are probably bound by confidentiality agreements, so the chapter cannot teach you to build a competitor to ChatGPT. It concentrates instead on design decisions that have a material effect on downstream applications (PDF p. 119).
- Transparency about training is shrinking, so not every design decision behind a model can be known. Still, the book says differences between foundation models generally trace back to three things: the training data, the model architecture and size, and how the model is post-trained to match human preferences (PDF p. 119).

## Why it matters
- Models learn from data, so a model's training data tells you much about what it can and cannot do (PDF p. 119).
- Understanding these decisions is what lets a practitioner choose a model and adapt it sensibly rather than treating it as a black box (PDF p. 119).

## How the chapter is laid out
1. Training data first: how developers curate it, with emphasis on its distribution. Detailed dataset engineering, including data-quality evaluation and data synthesis, is deferred to Chapter 8 (PDF pp. 119-120).
2. Model architecture. Because the transformer dominates, architecture can look like a non-choice. The chapter promises to explain what makes the transformer so durable, how long before another architecture might replace it, and what that successor might look like (PDF p. 120).
3. Model size. A new model's size is usually the first thing people ask about, so the chapter explores how a developer might decide the right size (PDF p. 120).
4. Post-training. As Chapter 1 noted, training is often split into pre-training and post-training. Pre-training makes a model capable but not necessarily safe or easy to use; post-training aims to align it with human preferences. The chapter asks what human preference even is and how it can be represented so a model can learn it, and notes that the alignment approach strongly affects usability (PDF p. 120).
5. Sampling: how a model picks one output from all possible options. The author calls it perhaps one of the most underrated concepts in AI, because the impact of sampling is often overlooked while the impact of training is widely understood (PDF p. 120).

## Why sampling gets special emphasis
Sampling explains many puzzling AI behaviours, including hallucinations and inconsistencies, and choosing a good sampling strategy can lift performance noticeably for relatively little effort. The author says this was the section he was most excited to write (PDF pp. 120-121).

## When and how to apply
- The concepts here are foundational for the rest of the book, but because they are foundational a reader may already know them. The author invites readers to skip anything they are confident about and to come back if a later concept is confusing (PDF p. 121).

## Relations
Training data is taken up in C02-002 (lead-in), C02-003 (multilingual models) and C02-004 (domain-specific models). Dataset engineering is developed later in Chapter 8; pre- and post-training were introduced in Chapter 1.
