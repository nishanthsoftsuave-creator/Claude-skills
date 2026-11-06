---
id: C05-011
title: Iterate on Your Prompts
source_pages: "452"
chapter: 5
concepts: [prompt-iteration, model-quirks, prompt-versioning, experiment-tracking, systematic-evaluation, playground, system-level-evaluation]
related: [C05-010, C05-012, C05-013, C04-001]
time_sensitive: false
---
# Iterate on Your Prompts
(Source: PDF p. 452; the section continues onto PDF p. 453, cited below as its tail page, and ends where the heading "Evaluate Prompt Engineering Tools" begins, which is C05-012)

## What the section covers
The last general best practice: prompt engineering is back-and-forth. As you learn a model, you get better ideas for writing prompts. The section gives an example of reacting to a response, advice on getting to know a model's quirks, and rules for testing prompt changes systematically.

## How it works
- Example: asked to pick the best video game, a model may answer that opinions differ and no game is absolutely the best (PDF p. 452). Seeing that, you revise the prompt to ask it to pick a game even though opinions differ (PDF p. 453).
- Know your model's quirks. One model may be stronger with numbers, another at roleplay. One may prefer system instructions at the start of the prompt, another at the end (PDF p. 453). Ways to learn them (PDF p. 453):
  - play with the model and try different prompts;
  - read the developer's prompting guide if one exists;
  - look for other people's experiences online;
  - use the model's playground if available;
  - run the same prompt on several models and compare, which also sharpens your understanding of each.

## Evaluation and success criteria: test systematically
Per PDF p. 453:
- Version your prompts.
- Use an experiment tracking tool.
- Standardize evaluation metrics and evaluation data so different prompts can be compared fairly.
- Evaluate each prompt within the whole system: a prompt change may help one subtask yet worsen the overall system.

## When and how to apply
INTERPRETATION: Treat every prompt as an experiment: observe an undesired response, adjust the instruction, rerun on the same fixed evaluation set, record the result, and judge it at the system level rather than only on the step you edited.

## Relations
Follows CoT and self-critique (C05-010), whose last page shares PDF p. 452 with this section's start. The next sections, evaluating prompt engineering tools and organizing/versioning prompts, are C05-012 and C05-013. Evaluation fundamentals are in Chapter 4.
