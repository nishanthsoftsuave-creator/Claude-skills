---
id: C04-007
title: Model Selection (Section Lead-in)
source_pages: "355"
chapter: 4
concepts: [model-selection, application-specific-evaluation, adaptation-techniques, prompt-engineering, finetuning, iterative-selection]
related: [C04-006, C04-008, C04-009]
time_sensitive: false
---
# Model Selection (Section Lead-in)
(Source: PDF p. 355)

## What the section covers
The opening of the Model Selection section: the point that the best model is the best one for your application, and that selection recurs throughout development. (The top of the page finishes Table 4-3 on cost and latency criteria, covered in C04-006.)

## Meaning
- Ultimately you do not care which model is best in general; you care which is best for your application. Once the application's criteria are defined, models should be evaluated against them (PDF p. 355).

## How it works
- Model selection is repeated, not done once. As you move through different adaptation techniques you must select again and again (PDF p. 355).
- Prompt engineering example: you might start with the strongest model overall to see whether the task is feasible, then work backward to check whether smaller models would do (PDF p. 355).
- Finetuning example: you might start with a small model to test your code, then move toward the biggest model that fits your hardware limits, such as a single GPU (PDF p. 355).

## Relations
Criteria come from the preceding Evaluation Criteria sections (C04-006). The concrete workflow follows in C04-008, and the two-step selection pattern (best achievable performance, then cost-performance mapping) begins at the top of the next page (C04-008).
