---
id: C04-011
title: Step 1. Evaluate All Components in a System
source_pages: "393-395"
chapter: 4
concepts: [evaluation-pipeline, component-evaluation, per-turn-evaluation, per-task-evaluation, intermediate-output, twenty-questions, open-ended-tasks]
related: [C04-010, C04-012]
time_sensitive: false
---
# Step 1. Evaluate All Components in a System
(Source: PDF pp. 393-395)

## What the section covers
The opening of the "Design Your Evaluation Pipeline" section and its first step: evaluate every component of a system, and evaluate at several levels (per task, per turn, per intermediate output), with a resume-parsing example and the twenty_questions benchmark as a task-based example. The page continues past this row with the example conversation (cut off at the end of PDF p. 395).

## Why an evaluation pipeline matters
An AI application's success often depends on telling good outcomes from bad ones, which requires an evaluation pipeline you can trust (PDF p. 393). With so many evaluation methods, choosing a combination is confusing (PDF p. 393). The section focuses on open-ended tasks; close-ended tasks are easier and their pipeline can be inferred from this process (PDF p. 393).

## Meaning: levels of evaluation
Real applications are complex: many components, and a task may finish only after many turns. Evaluation can therefore occur per task, per turn, and per intermediate output (PDF p. 393). The book's advice is to evaluate the end-to-end output and also each component's intermediate output, independently (PDF p. 393).

## How it works: component example
An application extracts a person's current employer from a resume PDF in two steps: (1) extract all text from the PDF; (2) extract the current employer from that text (PDF p. 393). A wrong final answer can come from either step; without separate evaluation you cannot tell where the system fails (PDF p. 394).
- Step 1 (PDF to text) can be scored by similarity between the extracted text and the ground-truth text (PDF p. 394).
- Step 2 can be scored by accuracy: given correctly extracted text, how often does the application pull out the right current employer? (PDF p. 394).

## Turn-based versus task-based evaluation
- A turn can contain several steps and messages. A system that takes multiple steps to produce an output still counts as one turn (PDF p. 394).
- Chatbot-like applications allow back-and-forth to finish a task. Example: you ask a model to debug failing Python code, and it first asks for hardware details or the Python version before it can help (PDF p. 394).
- Turn-based evaluation judges the quality of each output. Task-based evaluation asks whether the system completed the task: did it fix the bug, and how many turns did it take? Solving it in two turns versus twenty is a big difference (PDF p. 394).
- Evaluate both per turn and per task where applicable (PDF p. 394).

## Which matters more, and the difficulty
Users care about whether the model helps them finish tasks, so task-based evaluation is more important (PDF p. 395). The challenge is that task boundaries are hard to determine. In a ChatGPT conversation you might ask several questions at once, and when a new query arrives it is unclear whether it is a follow-up or a new task (PDF p. 395).

## Example of task-based evaluation: twenty_questions
From the BIG-bench suite, inspired by the game Twenty Questions. One model instance (Alice) picks a concept such as apple, car, or computer. Another instance (Bob) asks questions to identify it, and Alice may answer only yes or no. The score reflects whether Bob guesses correctly and how many questions he needs (PDF p. 395). The book then gives a plausible conversation from BIG-bench's GitHub repository, which falls beyond this row's text (PDF p. 395).

## When and how to apply
INTERPRETATION: for any multi-step system, write a separate check for each stage (as with the PDF-to-text and employer-extraction stages) in addition to the final-answer check, and track both turn quality and task completion with number of turns.

## Relations
Follows public benchmark navigation (C04-010), which ends by saying a custom evaluation pipeline is needed. Next step is creating an evaluation guideline (C04-012).
