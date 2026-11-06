---
id: C07-001
title: Finetuning Chapter Introduction
source_pages: "594-595"
chapter: 7
concepts: [finetuning, weight-adaptation, memory-footprint, peft, adapter-techniques, finetune-vs-rag, ml-knowledge-prerequisite]
related: [C07-002, C07-004, C07-005, C07-006, C07-007, C07-013]
time_sensitive: false
---
# Finetuning Chapter Introduction
(Source: PDF pp. 594-595)

## What the section covers
The opening of Chapter 7. It defines finetuning, contrasts it with the prompt-based methods of Chapters 5 and 6, and previews what the chapter will cover: an overview, the reasons for and against finetuning, a framework for choosing between finetuning and alternatives, memory bottlenecks, and parameter-efficient finetuning (PEFT).

## Meaning
- Finetuning is adapting a model to a specific task by training further, either the whole model or only part of it (PDF p. 594).
- Prompt-based methods (Chapters 5 and 6) adapt a model by supplying instructions, context and tools. Finetuning adapts it by changing its weights (PDF p. 594).
- PEFT (parameter-efficient finetuning) is described as the memory-efficient approach that has become dominant. The chapter will explain how it differs from traditional finetuning, survey its evolving techniques, and focus on one category the author finds compelling: adapter-based techniques (PDF p. 595).

## Why it matters
- Finetuning can improve many aspects of a model: domain-specific capability (coding, medical question answering) and safety. In practice it is used most often to improve instruction following, especially adherence to particular output styles and formats (PDF p. 594).
- It yields models more customized to your needs but demands more up-front investment than prompting (PDF p. 594).
- The author says readers ask very often when to finetune and when to use RAG, and the chapter takes this up through reasons for and against finetuning plus a simple decision framework (PDF p. 594).

## Limitations and cost
- Compared with prompt-based methods, finetuning has a much higher memory footprint. At the scale of current foundation models, naive finetuning often needs more memory than a single GPU provides, which makes it costly and hard (PDF p. 594).
- Reducing memory requirements is therefore the main motivation behind many finetuning techniques, which is why the chapter includes a dedicated section on what contributes to a model's memory footprint (PDF pp. 594-595).

## Assumptions and prerequisites
- Prompting benefits from, but does not strictly require, knowing how models work internally. Finetuning enters model training, where ML knowledge is required (PDF p. 595).
- ML basics are out of scope for the book; the book's GitHub repository points to refresher resources, and the chapter covers only the core concepts immediately relevant (PDF p. 595).
- The author calls this the most technically challenging chapter to write, owing to the breadth of material rather than concept difficulty, and says readers may skip details that are irrelevant to their work (PDF p. 595).

## Relations
Leads into the overview of finetuning (C07-002), the decision sections (C07-004, C07-005, and the finetuning versus RAG discussion C07-006), memory bottlenecks (C07-007) and PEFT (C07-013).
