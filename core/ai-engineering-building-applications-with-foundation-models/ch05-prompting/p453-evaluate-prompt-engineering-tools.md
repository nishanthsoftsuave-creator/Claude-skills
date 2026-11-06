---
id: C05-012
title: Evaluate Prompt Engineering Tools
source_pages: "453-457"
chapter: 5
concepts: [prompt-engineering-tools, prompt-optimization, dspy, openprompt, promptbreeder, textgrad, hidden-api-calls, tool-risks]
related: [C05-011, C05-013, C05-014]
time_sensitive: true
---
# Evaluate Prompt Engineering Tools
(Source: PDF pp. 453-457, with the section's closing paragraphs on PDF p. 458 above the "Organize and Version Prompts" heading. The lines at the top of PDF p. 453 about experimenting with a model belong to the preceding row and are only touched on in one sentence below.)

## What the section covers
How automated and semi-automated tools for prompt engineering work, what they are good for, and the costs and risks of relying on them: hidden API calls, tool-author mistakes, and silent changes to the tool. It ends with the advice to start without tools and to inspect whatever a tool produces.

## Context from the preceding section
The preceding practice advice (PDF p. 453) tells you to learn the quirks of your model, to version prompts, to track experiments, to standardize metrics and evaluation data, and to judge each prompt in the context of the whole system, since a prompt that helps one subtask can hurt the whole system. The tool discussion starts from there.

## Why tools exist
- For any task the space of possible prompts is unbounded, manual prompt engineering takes a lot of time, and the best prompt is hard to pin down, so many tools have been built to help or automate the work (PDF p. 453).

## Meaning and how it works

### Tools that automate the whole workflow
- OpenPrompt (Ding et al., 2021) and DSPy (Khattab et al., 2023) aim to automate the complete workflow. You supply the input and output formats, the evaluation metrics, and the evaluation data for the task. The optimizer then searches for a prompt, or a chain of prompts, that maximizes the metrics on that data (PDF p. 454).
- The book compares these to autoML tools, which search for the best hyperparameters of classical ML models (PDF p. 454).

### Using AI models to write prompts
- A common way to automate prompt generation is to use an AI model. In the simplest case you ask a model to write a prompt for your application, for example "Help me write a concise prompt for an application that grades college essays between 1 and 5". You can also ask a model to critique or improve your prompts, or to produce in-context examples (PDF p. 454).
- Figure 5-7 (PDF p. 455) is a screenshot of this exact request sent to Claude 3.5 Sonnet. The reply is a short grader prompt: it casts the model as an AI essay grader for college admissions, asks for a 1 to 5 scale where 1 is poor and 5 excellent, lists five criteria (clarity of argument, structure and organization, use of evidence, writing quality and style, creativity and originality), and asks for a numeric grade plus a brief explanation. The model then offers to expand the prompt. The figure's point is simply that a model can draft a usable prompt for you.

### AI-powered optimizers
- DeepMind's Promptbreeder (Fernando et al., 2023) and Stanford's TextGrad (Yuksekgonul et al., 2024) are the two examples given (PDF p. 454).
- Promptbreeder uses an evolutionary strategy to "breed" prompts. It starts from an initial prompt and asks an AI model to generate mutations of it, guided by a set of mutator prompts. It then generates mutations of the most promising mutation, and repeats until a prompt meets your criteria (PDF pp. 454-455).
- Figure 5-8 (PDF p. 456) shows one cycle. A mutator prompt ("modify the following instruction creatively, giving some advice on how to solve it") wraps the original instruction ("Solve the math word problem, giving your answer as an Arabic numeral"). The model responds with a mutated prompt (a reworded instruction asking for the answer in regular numbers), which becomes the next original prompt, forming a loop. The caption stresses that promising mutants are selected and mutated again.

### Tools that assist only part of the work
- Guidance, Outlines, and Instructor steer models toward structured outputs (PDF p. 456).
- Other tools perturb a prompt, for instance swapping a word for a synonym or rewriting it, to find which variant performs best (PDF p. 456).

## Why it matters
Used correctly these tools can substantially improve system performance, but you need to understand how they work internally to avoid unnecessary cost and trouble (PDF p. 456).

## Limitations and failure modes (what to watch for)

### 1. Hidden API calls and cost
- Tools often make model API calls you do not see, which can exhaust your API budget if unmonitored (PDF p. 456).
- Worked arithmetic: with one call per prompt variation, 30 evaluation examples and ten variations give 300 calls (PDF pp. 456-457).
- Often more than one call is needed per variation: one to generate a response, one to validate it (such as checking for valid JSON), and one to score it. Giving the tool freedom to design prompt chains can make the count grow further and lead to chains that are very long and expensive (PDF p. 457).

### 2. Tool developers make mistakes
- A developer might use the wrong template for a given model, build the prompt by concatenating tokens rather than raw text, or leave typos in the templates (PDF p. 457).
- Figure 5-9 (PDF p. 457) shows a LangChain default critique prompt. The figure stacks two code snippets of the same HumanMessagePromptTemplate, with the differing words highlighted: the upper snippet (red highlight) has "options" and "Let'w work this out in a step", the lower snippet (green highlight) has "option" and "Let's work this out in a step". The book gives only the caption "Typos in a LangChain default prompt are highlighted"; that the upper is the typo version and the lower the fixed one is read from the colours and the wording. The point is that a widely used library shipped typos in a default prompt, so tool prompts need checking.

### 3. Tools change without notice
- Any tool can switch prompt templates or rewrite default prompts without warning (PDF p. 458).
- The more tools you stack, the more complex and error-prone the system becomes (PDF p. 458).

## When and how to apply
- Following the keep-it-simple principle, begin by writing your own prompts without tools. That teaches you about the underlying model and your own requirements (PDF p. 458).
- If you do adopt a tool, always read the prompts it generates to check they make sense, and track how many API calls it makes (PDF p. 458).
- The book's closing reminder: however skilled the developers, they can err like anyone (PDF p. 458).

## Relations
Follows the model-experimentation and systematic-testing advice in C05-011 and is followed by prompt organization and versioning (C05-013). Evaluating prompt variants requires the evaluation data and metrics discussed in the evaluation chapters.

## Time-sensitive statements
The named tools (OpenPrompt, DSPy, Promptbreeder, TextGrad, Guidance, Outlines, Instructor, LangChain) and the use of Claude 3.5 Sonnet in Figure 5-7 reflect the state of the field when the book was written.
