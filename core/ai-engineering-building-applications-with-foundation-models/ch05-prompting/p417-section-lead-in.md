---
id: C05-002
title: Introduction to Prompting (Section Lead-in)
source_pages: "417-419"
chapter: 5
concepts: [prompt, prompt-structure, task-description, few-shot-examples, instruction-following, prompt-robustness, prompt-perturbation, ner]
related: [C05-001, C05-003, C05-004, C04-001]
time_sensitive: true
---
# Introduction to Prompting (Section Lead-in)
(Source: PDF pp. 417-419; coverage starts at the heading "Introduction to Prompting" part-way down PDF p. 417. The lines above it belong to C05-001.)

## What the section covers
The definition of a prompt, its three typical parts, a simple NER example, and two prerequisites for prompting to work: instruction-following ability and robustness to prompt perturbation. The subsections on in-context learning, system/user prompts and context length follow.

## Meaning
- A prompt is an instruction given to a model to perform a task. Tasks range from a simple question such as "Who invented the number zero?" to complex jobs like researching competitors for a product idea, building a website from scratch, or analyzing data (PDF p. 417).
- A prompt generally has one or more of three parts (PDF p. 418):
  1. Task description: what the model should do, including the role it should play and the output format.
  2. Example(s) of how to do the task. For toxicity detection you might show a few toxic and non-toxic texts.
  3. The task itself: the concrete question to answer or book to summarize.

## How it works: the NER example (Figure 5-1)
Figure 5-1 (PDF p. 418, read from the rendered page) shows a minimal named-entity-recognition prompt with its three labelled parts. The task description tells the model to extract all entities and output only the comma-separated list and nothing else. The example is a text, "Brave New World is a dystopian novel written by Aldous Huxley, first published in 1932", with the entities "Brave New World, Aldous Huxley". The task slot holds a placeholder for the text to extract from, followed by "Entities:" for the model to complete. The point is how description, example and task map onto one prompt.

## Assumptions and prerequisites
- The model must be able to follow instructions. If it is poor at that, a perfect prompt will still fail. Evaluating instruction-following is covered in Chapter 4 (PDF p. 419).
- How much prompt engineering you need depends on the model's robustness to prompt perturbation: would a small change such as "5" instead of "five", an added newline or different capitalization change the answer drastically? The less robust the model, the more fiddling is required (PDF p. 419).

## Evaluation and success criteria
Robustness can be measured by randomly perturbing prompts and watching how outputs change (PDF p. 419). Like instruction-following, robustness correlates strongly with overall capability: stronger models understand that "5" and "five" mean the same, so using a stronger model can save headaches and reduce wasted fiddling (PDF p. 419).

## When and how to apply
The book's tip: experiment with prompt structures to see which works best. Most models, GPT-4 among them, empirically do better with the task description at the start of the prompt, but some, including Llama 3, seem to do better with it at the end (PDF p. 419).

## Time-sensitive statements
The GPT-4 versus Llama 3 placement of the task description (PDF p. 419) reflects models at the time of writing.

## Limitations
Tips like this are model-specific and empirical, so they need to be tested per model.

## Relations
Follows the chapter intro (C05-001). Instruction-following evaluation is in Chapter 4. The examples part leads into C05-003, and the task description versus task split leads into C05-004.
