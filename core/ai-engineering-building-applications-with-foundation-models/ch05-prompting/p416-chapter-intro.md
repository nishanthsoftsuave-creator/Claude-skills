---
id: C05-001
title: Chapter 5 Introduction. Prompt Engineering
source_pages: "416"
chapter: 5
concepts: [prompt-engineering, model-adaptation, finetuning-vs-prompting, prompt-experiments, human-to-ai-communication, chapter-scope]
related: [C05-002, C05-006]
time_sensitive: false
---
# Chapter 5 Introduction. Prompt Engineering
(Source: PDF p. 416, plus the opening lines of PDF p. 417 that precede the heading "Introduction to Prompting")

## What the section covers
The opening of Chapter 5. It defines prompt engineering, positions it against finetuning, argues that it deserves rigor, and previews what the chapter covers: how to write effective prompts and how to defend applications against prompt attacks.

## Meaning
- Prompt engineering is the process of crafting an instruction that gets a model to generate the desired outcome (PDF p. 416).
- It is described as the easiest and most common model adaptation technique. Unlike finetuning, it steers a model's behavior without changing its weights (PDF p. 416).

## Why it matters
- Because foundation models have strong base capabilities, many people have adapted them for real applications using prompting alone. The book's advice is to get the most out of prompting before moving to more resource-intensive techniques such as finetuning (PDF p. 416).
- Ease of use is deceptive. It can look like fiddling with words until something works, yet the book says it also contains interesting challenges and ingenious solutions (PDF p. 416).
- The book frames it as human-to-AI communication: anyone can communicate, but not everyone communicates effectively, and likewise writing a prompt is easy while constructing an effective one is not (PDF p. 416).

## Rigor and its limits
- Some argue that prompt engineering is not rigorous enough to count as engineering. The book disagrees that this must be so: prompt experiments should be run with the same rigor as any ML experiment, meaning systematic experimentation and evaluation (PDF pp. 416-417).
- The book quotes an OpenAI research manager it interviewed: prompt engineering is a real and useful skill, and the problem arises "when prompt engineering is the only thing people know" (PDF p. 417).
- Building production-ready applications requires more than prompting: statistics, engineering and classic ML knowledge for experiment tracking, evaluation and dataset curation (PDF p. 417).

## What the chapter will do
It covers both writing effective prompts and defending applications from prompt attacks. Before the applications, it starts with fundamentals: what a prompt is, and best practices (PDF p. 417).

## When and how to apply
INTERPRETATION: treat prompt changes as tracked experiments with an evaluation set, and exhaust prompting before committing to finetuning.

## Relations
The fundamentals begin in C05-002 (what a prompt is) and the best practices start at C05-006. The finetuning alternative is the later chapters' topic.
