---
id: C07-005
title: Reasons Not to Finetune
source_pages: "604-610"
chapter: 7
concepts: [reasons-not-to-finetune, catastrophic-forgetting, task-degradation, prompt-experiments-first, finetuning-costs, model-maintenance, bloomberggpt, token-optimization, prompt-caching]
related: [C07-003, C07-004, C07-006, C07-013, C07-014, C06-001, C09-007, C08-011]
time_sensitive: true
---
# Reasons Not to Finetune
(Source: PDF pp. 604-610; the first paragraph of PDF p. 604 finishes the preceding section on open source models and belongs to C07-004)

## What the section covers
The case against finetuning, or at least against finetuning early: it can hurt other tasks, demands data, training know-how, serving capability and ongoing maintenance, is usually unnecessary if prompting has been tested properly, and general models often overtake specialized ones (the BloombergGPT example). It ends with the one benefit finetuning has for token usage and how prompt caching changes that.

## Why it matters
Many gains attributed to finetuning can be had to some extent without it. Carefully crafted prompts and context raise performance too, and structured outputs can be obtained by several non-finetuning techniques discussed in Chapter 2 (PDF p. 604).

## How it works / the arguments

### 1. Finetuning for one task can degrade others
- Finetuning improves the target task but can lower performance on other tasks, which is frustrating when the application receives diverse prompts (PDF p. 604).
- Example: a model must handle product recommendations, order changes and general feedback. It starts good at recommendations and feedback but poor at order changes. Finetuning on (query, response) pairs about order changes may improve that task while making the other two worse (PDF pp. 604-605).
- Remedies: finetune on all the queries you care about, not just the weak one; if one model cannot do all tasks well, use separate models per task; if you want one model to ease serving, consider merging the separate models (merging is covered later in the chapter) (PDF p. 605).

### 2. High up-front investment and continual maintenance
When just starting a project, finetuning is rarely the first thing to try (PDF p. 605). The requirements:
- Data. Manually annotated data is slow and expensive, especially for tasks needing critical thinking or domain expertise. Open source or AI-generated data lowers the cost but with highly variable effectiveness (PDF p. 605).
- Training know-how. You must evaluate base models to choose one, and options may be limited by needs and resources. Finetuning frameworks and APIs automate many steps, but you still need to understand the training knobs, monitor learning and debug problems: how an optimizer works, which learning rate to use, how much training data is needed, how to handle overfitting and underfitting, and how to evaluate throughout (PDF pp. 605-606).
- Serving. Decide whether to host the model yourself or use an API service. Inference optimization for large models is nontrivial (see Chapter 9). Finetuning is a smaller technical leap if you already host models in-house and know how to operate them (PDF p. 606).
- Policy and budget for monitoring, maintaining and updating. New base models appear rapidly and may improve faster than your finetuned model. Questions to settle in advance: how large must a new base model's gain be on your task before you switch; and if a new base model does not beat your model now but could after finetuning, would you experiment with it? (PDF p. 606).
- Switching to a better model often yields only a small incremental gain, and the task may be deprioritized behind projects with larger returns such as new use cases (PDF p. 606).

### 3. Prompting should come first
- AI engineering experiments should begin with prompting using Chapter 6 best practices; move to more advanced solutions only if prompting proves inadequate. Test a variety of prompts thoroughly since performance can vary greatly with prompt wording (PDF p. 607).
- A recurring story from practitioners: someone says prompting does not work and insists on finetuning; investigation shows prompt experiments were minimal and unsystematic, with unclear instructions, examples unrepresentative of actual data and poorly defined metrics. After the prompt experiments were improved, prompt quality was enough for the application (PDF p. 607).

### 4. Domain-specific tasks: the BloombergGPT case
- Be wary of the argument that general-purpose models fail at domain tasks and so you must finetune or train your own. As general models become more capable they also improve on domain tasks and can outperform domain-specific models (PDF p. 608).
- BloombergGPT, introduced by Bloomberg in March 2023: at the time the strongest models were proprietary, and Bloomberg wanted a mid-size model good at financial tasks that could be hosted in-house for sensitive-data use cases. It has 50 billion parameters, needed 1.3 million A100 GPU hours to train, and the compute was estimated at between $1.3 million and $2.6 million, excluding data costs (Wu et al., 2023) (PDF p. 608).
- The same month OpenAI released GPT-4-0314. Li et al. (2023) showed it significantly outperformed BloombergGPT on many financial benchmarks (PDF p. 608).
- Table 7-1 (two benchmarks): FiQA sentiment analysis (weighted F1) GPT-4-0314 zero-shot 87.15 versus BloombergGPT 75.07; ConvFinQA (accuracy) GPT-4-0314 zero-shot 76.48 versus BloombergGPT 43.41 (PDF p. 609). The table was read from the rendered page and has no clipped cells.
- Afterward, several mid-size models comparable to GPT-4 appeared: Claude 3.5 Sonnet (70B parameters), Llama 3-70B-Instruct and Qwen2-72B-Instruct, the latter two open weight and self-hostable (PDF p. 609).
- Caveat in fairness to Bloomberg: benchmarks do not capture real-world performance, so BloombergGPT may work well for Bloomberg's own use cases, and the team gained experience that may help build and run future models (PDF p. 609).
- Both finetuning and prompting need systematic processes. Prompt experiments build the evaluation pipeline, data annotation guideline and experiment-tracking habits that are stepping stones to finetuning (PDF p. 609).

### 5. The token-usage benefit and prompt caching
- Before prompt caching existed, finetuning could optimize token usage: more in-prompt examples mean more input tokens, higher latency and cost. Finetuning on those examples allows shorter prompts with the finetuned model, as the text points out with Figure 7-2 (PDF p. 610). Figure 7-2 itself is printed at the top of the next page and is described in C07-006 (not here).
- With prompt caching, where repeated prompt segments are cached for reuse, this is no longer a strong benefit (Chapter 9 discusses caching) (PDF p. 610).
- A remaining advantage: the number of in-prompt examples is bounded by maximum context length, whereas with finetuning there is no limit on how many examples you can use (PDF p. 610).

## When and how to apply
- INTERPRETATION: before finetuning, ask whether (a) systematic prompt experiments with representative examples and defined metrics have been run, (b) you have data, training skill, serving capability and a maintenance/switching policy, (c) the target gain justifies the cost relative to simply adopting a newer general model, and (d) other tasks in the application will not regress, or can be protected by multi-task data, separate models or merging.

## Limitations and failure modes
Task degradation, unstable data quality, training and debugging errors, obsolescence of the finetuned model as base models improve, and low priority for refresh work (all described above).

## Relations
Counterpart to C07-004; the finetuning versus RAG framework is C07-006. Merging and multi-task finetuning appear in C07-014. Prompting best practices are in Chapter 6 (C06-001 is the chapter's opening), prompt caching in C09-007, and distillation or data synthesis in Chapter 8 (C08-011).

## Time-sensitive statements
The BloombergGPT figures (March 2023), the GPT-4-0314 comparison, the Table 7-1 scores, and the list of mid-size models comparable to GPT-4 (Claude 3.5 Sonnet, Llama 3-70B-Instruct, Qwen2-72B-Instruct) reflect the date of writing. The point that prompt caching erased much of finetuning's token benefit also depends on provider features available then.
