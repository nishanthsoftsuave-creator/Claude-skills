---
id: C08-016
title: Format Data
source_pages: "764-767"
chapter: 8
concepts: [data-formatting, chat-template, tokenizer, instruction-response, finetuning-format, few-shot-to-finetuning, prompt-format-matching]
related: [C08-015, C08-017, C05-003, C05-004, C07-001]
time_sensitive: false
---
# Format Data
(Source: PDF pp. 764-767; the section's last sentence begins on PDF p. 767 and finishes at the top of the next page, so its final examples are described below without a page cite)

## What the section covers
The last processing step: putting deduplicated, cleaned data into the format the target model expects, with a worked example of converting a few-shot prompt into finetuning data (PDF pp. 764-767).

## How it works
- Each model has its own tokenizer and expects a specific chat template (Chapter 5). Feeding the wrong template can create strange bugs in the model (PDF p. 764).
- For supervised finetuning, data is most likely (instruction, response) pairs. An instruction can be split further into (system prompt, user prompt) (PDF p. 764).
- If you moved to finetuning from prompt engineering, the finetuning instructions may differ from the prompting ones. During finetuning, instructions usually need no task description or examples, because with enough training examples the model learns the expected behavior directly (PDF pp. 764-765).

### Worked example: food classification (PDF pp. 765-767)
- With a base model you might have used a three-shot prompt: "Label the following item as either edible or inedible." followed by the examples burger: edible, car: inedible, mushroom: edible, then "Item: {INPUT}" and "Label:" (PDF p. 766).
- For finetuning, each example in the three-shot prompt becomes a training example. Table 8-4 (PDF p. 767) lists example IDs 1 to 3 with inputs "burger -->", "car -->", "mushroom -->" and outputs edible, inedible, edible, followed by an ellipsis row for more examples.
- After finetuning, the prompt can be just "{INPUT} -->", far shorter than the base-model prompt. So if input tokens from instructions worry you, finetuning is one way to manage cost (PDF p. 767).

## Why it matters
- Different finetuning data formats can change the finetuned model's performance, so it may pay to run experiments to find the best format for you (PDF p. 767).
- At inference, prompts must match the training-data format (PDF p. 767). The book's example: if training used "burger -->", then these variants can cause problems: "burger" (missing the end arrow), "Item: burger -->" (extra prefix) and "burger --> " (extra space appended). The sentence beginning on p. 767 ("if the training data...") finishes with this list on the following page.

## When and how to apply
INTERPRETATION: Generate training and serving prompts from one shared template function so they cannot drift apart, and strip few-shot examples and task descriptions from finetuning instructions once enough examples exist.

## Relations
Follows cleaning and filtering (C08-015); the template background is in Chapter 5 (C05-003, C05-004); the chapter closes in C08-017.
