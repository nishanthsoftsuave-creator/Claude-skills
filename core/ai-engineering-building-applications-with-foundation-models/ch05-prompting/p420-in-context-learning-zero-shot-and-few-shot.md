---
id: C05-003
title: In-Context Learning. Zero-Shot and Few-Shot
source_pages: "420-422"
chapter: 5
concepts: [in-context-learning, zero-shot, few-shot, shot, continual-learning, prompt-vs-context, context-length, inference-cost]
related: [C05-002, C05-004, C05-005]
time_sensitive: true
---
# In-Context Learning. Zero-Shot and Few-Shot
(Source: PDF pp. 420-422; the section's final paragraph, on Chollet's "library of programs" view, is on PDF p. 423 above the heading "System Prompt and User Prompt", which belongs to C05-004)

## What the section covers
What in-context learning is, why it matters, the vocabulary of shots, how many examples are needed, a terminology note on "prompt" versus "context", and a closing view of why in-context learning works.

## Meaning
- Teaching a model what to do through the prompt is called in-context learning, a term introduced by Brown et al. (2020) in the GPT-3 paper (PDF p. 420).
- Traditionally a model learns desired behavior during training (pre-training, post-training, finetuning), which updates weights. The GPT-3 paper showed that a model can learn behavior from examples in the prompt, even behavior different from what it was trained for, with no weight update (PDF p. 420).
- Concrete case: GPT-3 was trained for next-token prediction, yet learned from context to do translation, reading comprehension, simple math and even SAT questions (PDF p. 420).
- Each example in the prompt is a "shot". Learning from prompt examples is few-shot learning (five examples = 5-shot); with no examples it is zero-shot learning (PDF p. 421).

## Why it matters
In-context learning lets a model take in new information continually and avoid going stale. Example: a model trained on old JavaScript documentation would need retraining to answer about a new version; with in-context learning you place the changes in the context and the model can answer beyond its cut-off date. The book therefore calls it a form of continual learning (PDF p. 420).

## How many examples
- The right number depends on the model and the application, so experiment (PDF p. 421).
- In general more examples help the model learn, but the count is capped by the model's maximum context length, and more examples make the prompt longer and raise inference cost (PDF p. 421).
- For GPT-3, few-shot was a significant improvement over zero-shot. In Microsoft's 2023 analysis, for the use cases studied, few-shot gave only limited gains over zero-shot on GPT-4 and a few other models. The book reads this as stronger models following instructions better and needing fewer examples (PDF p. 421).
- Caveat: that study may underestimate few-shot value for domain-specific use cases. If a model saw little of the Ibis dataframe API in training, putting Ibis examples in the prompt can still matter a lot (PDF p. 421).

## Terminology ambiguity: prompt versus context
- In the GPT-3 paper, "context" meant the entire model input, i.e. the same as prompt. Some people argue context is part of the prompt: the information the model needs to do what the prompt asks. Google's PaLM 2 documentation defines context as the description shaping how the model responds throughout a conversation (words allowed or banned, topics, format, style), which equates it with the task description (PDF p. 422).
- The book's own convention: prompt is the whole input to the model; context is the information supplied so the model can perform the task (PDF p. 422).

## Why it works (framing)
Today in-context learning is taken for granted, but before GPT-3 models did only what they were trained to do, so it seemed like magic and many researchers pondered why it works (PDF p. 422). The explanation attributed to Keras creator Francois Chollet, on the next page, treats a foundation model as a library of programs, with prompt engineering being the search for the prompt that activates the right one.

## When and how to apply
INTERPRETATION: start zero-shot, add shots while measuring the gain against prompt length and cost, and expect examples to matter most for domain-specific or rarely seen APIs.

## Time-sensitive statements
The Microsoft 2023 finding on GPT-4 and the GPT-3 comparison reflect models at the time of writing.

## Relations
Builds on the prompt parts in C05-002; length limits are developed in C05-005; the next topic is C05-004.
