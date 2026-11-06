---
id: P-005
title: Preface - Navigating This Book
source_pages: "19-22"
chapter: preface
concepts: [book-structure, chapter-roadmap, development-process, evaluation, prompt-engineering, rag-agents, finetuning, dataset-engineering, inference-optimization, user-feedback]
related: [P-004, C01-001, C02-001, C03-001, C04-001, C05-001, C06-001, C07-001, C08-001, C09-001, C10-001]
time_sensitive: false
---
# Preface - Navigating This Book
(Source: PDF pp. 19-22. The top of PDF p. 19 holds the end of the audience section, covered in P-004; the heading begins part-way down the page.)

## What the section covers
How the book is organized: chapters follow the typical process of developing an AI application, and the preface walks through what each chapter does. The book is modular, so readers may skip sections already familiar or less relevant (PDF p. 19).

## Chapter roadmap

### Chapter 1: should you build it (PDF p. 19)
Before deciding to build, you need to know what the process involves and answer: Is the application necessary? Is AI needed? Must I build it myself? Chapter 1 helps with these and also surveys a range of successful use cases to show what foundation models can do.

### Chapter 2: how foundation models work (PDF p. 20)
An ML background is not required to build applications, but understanding how a foundation model works helps get the most from it. Chapter 2 analyzes how a foundation model is made and the design decisions with big downstream effects: the training data recipe, model architecture and scale, and how the model is trained to align with human preference. It then explains how a model generates responses, which helps explain odd behaviors such as inconsistency and hallucination. Changing generation settings is often a cheap, easy way to substantially improve performance.

### Chapters 3 and 4: evaluation (PDF p. 20)
Once committed to building, evaluation is integral to every step and is called one of the hardest, if not the hardest, challenges of AI engineering. Two chapters cover evaluation methods and how to use them to build a reliable, systematic evaluation pipeline.

### Three levers on response quality (PDF pp. 20-21)
Aside from generation settings, the quality of a response to a query depends on three things: the instructions for how the model should behave, the context available to the model, and the model itself. The next three chapters each optimize one of them.

### Chapter 5: prompt engineering (PDF p. 21)
What a prompt is, why prompt engineering works, and best practices; then how bad actors can exploit an application through prompt attacks and how to defend against them.

### Chapter 6: context (RAG and agents) (PDF p. 21)
Why context matters for accurate responses. It focuses on two application patterns for context construction: RAG and agentic. RAG is better understood and has proven itself in production. The agentic pattern promises to be much more powerful but is more complex and still being explored.

### Chapter 7: finetuning (PDF p. 21)
Adapting by changing the model itself. At foundation-model scale, native finetuning is memory-intensive, so many techniques let you finetune better models with less memory. The chapter covers various finetuning approaches plus a more experimental one, model merging, and includes a more technical section on calculating a model's memory footprint.

### Chapter 8: data (PDF pp. 21-22)
Finetuning itself is often straightforward thanks to many frameworks, but obtaining finetuning data is hard. Chapter 8 covers data acquisition, annotation, synthesis, and processing. Many of its topics matter beyond finetuning, including what data quality means and how to evaluate it (PDF p. 22).

### Chapter 9: inference optimization (PDF p. 22)
If Chapters 5 to 8 improve model quality, Chapter 9 makes inference cheaper and faster, at both model level and inference-service level. If you use a model API, the provider likely handles optimization; if you host a model yourself (open source or built in-house), you need to implement many of these techniques.

### Chapter 10: end-to-end architecture and feedback (PDF p. 22)
Brings together the concepts to build an application end to end. Its second part is more product-focused, covering how to design a user feedback system that collects useful feedback while keeping a good user experience.

## Note on wording
The author often uses "we" to mean the reader and the author together, a habit from teaching, seeing writing as a shared learning experience (PDF p. 22).

## When and how to apply
INTERPRETATION: when looking for guidance on a specific problem, use this roadmap to pick the chapter: build/no-build decision in 1; model behavior and sampling in 2; evaluation in 3-4; instructions in 5; context in 6; model changes in 7-8; cost and latency in 9; system assembly and feedback in 10.

## Relations
Follows P-004. Each chapter's first section id (C01-001 through C10-001) is where the corresponding material begins.
