---
id: C04-003
title: Domain-Specific Capability
source_pages: "319-323"
chapter: 4
concepts: [evaluation-bottleneck, evaluation-criteria, domain-specific-capability, benchmarks, functional-correctness, multiple-choice, mmlu, classification-metrics, random-baseline, prompt-sensitivity]
related: [C04-002, C04-004, C04-001]
time_sensitive: true
---
# Domain-Specific Capability
(Source: PDF pp. 319-323)

## What the section covers
The four buckets of evaluation criteria, then a detailed look at the first one, domain-specific capability: how it is evaluated with benchmarks, exact evaluation for code (functional correctness, efficiency, readability), and close-ended multiple-choice evaluation for non-coding domains, including its metrics, strengths and weaknesses.

## Meaning
- The author's belief: evaluation is the biggest bottleneck to AI adoption, and being able to build reliable evaluation pipelines will unlock many new applications (PDF p. 319). This is why an application should start with a list of evaluation criteria.
- An application should start from a list of evaluation criteria specific to it. In general the criteria fall into four buckets: domain-specific capability, generation capability, instruction-following capability, and cost and latency (PDF p. 319).
- Worked illustration with a legal contract summary (PDF p. 319):
  - Domain-specific capability: how well the model understands legal contracts.
  - Generation capability: how coherent or faithful the summary is.
  - Instruction-following capability: whether the summary is in the requested format, e.g. meets a length constraint.
  - Cost and latency: what the summary costs and how long one waits.
- Different angle from Chapter 3: that chapter began with an evaluation approach and asked what criteria it can evaluate; this one starts from a criterion and asks which approaches can evaluate it (PDF p. 319).
- Domain-specific capability is the ability a task needs from the model: a coding agent needs a model that can write code; an app translating Latin to English needs a model that understands both languages (PDF pp. 319-320).

## Why it matters
- A model's domain-specific capabilities are constrained by its configuration (architecture and size) and by its training data. A model that never saw Latin in training cannot understand Latin, and models lacking the capabilities an application needs will not work for it (PDF p. 320).

## How it works: evaluating domain capability
- Use domain-specific benchmarks, public or private. Thousands of public benchmarks exist covering code generation, code debugging, grade school math, science knowledge, common sense, reasoning, legal knowledge, tool use, game playing and more (PDF p. 320).
- Domain-specific capabilities are commonly evaluated with exact evaluation (PDF p. 320).

### Coding
- Coding capabilities are typically evaluated by functional correctness, as in Chapter 3 (PDF p. 320).
- Correctness may not be the only concern; efficiency and cost can matter too. The book's analogy: you would not want a car that runs but burns excessive fuel. A text-to-SQL model's query may be correct yet take too long or use too much memory to be usable (PDF p. 320).
- Efficiency can be evaluated exactly by measuring runtime or memory use. BIRD-SQL (Li et al., 2023) considers not only a generated query's execution accuracy but also its efficiency, measured by comparing the generated query's runtime with the ground truth SQL query's runtime (PDF pp. 320-321).
- Code readability matters for maintenance and integration into a system. There is no obvious exact evaluation for it, so subjective evaluation such as AI judges may be needed (PDF p. 321).

### Non-coding domains: close-ended tasks
- Non-coding capabilities are often evaluated with close-ended tasks such as multiple-choice questions, because close-ended outputs are easier to verify and reproduce (PDF p. 321).
- Math example: an open-ended approach asks the model to generate the solution; a close-ended approach offers several options and has the model pick. If the expected answer is C and the model says A, it is wrong (PDF p. 321).
- Most public benchmarks follow this approach. In April 2024, 75% of the tasks in Eleuther's lm-evaluation-harness were multiple choice, including UC Berkeley's MMLU (2020), Microsoft's AGIEval (2023) and the AI2 Reasoning Challenge, ARC-C (2018). The AGIEval authors said they excluded open-ended tasks on purpose to avoid inconsistent assessment (PDF p. 321).
- Example MMLU item (PDF p. 322): the question asks why governments discourage and regulate monopolies; four options (A) to (D); label is (D), that consumer surplus is lost with higher prices and lower levels of output. The distractors are: (A) producer surplus is lost and consumer surplus gained; (B) monopoly prices ensure productive efficiency but cost society allocative efficiency; (C) monopoly firms do not engage in significant research and development.

### Multiple-choice metrics
- An MCQ may have one or more correct answers. The common metric is accuracy, the count of questions answered correctly (PDF p. 322).
- Some tasks use a point system in which harder questions are worth more. A point system also fits multi-answer questions: one point per correctly chosen option (PDF p. 322).
- Classification is a special case of multiple choice in which the choices are the same for every question. Example: tweet sentiment with NEGATIVE, POSITIVE and NEUTRAL on every item. Besides accuracy, classification uses F1 scores, precision and recall (PDF p. 322).

## Why MCQs are popular
They are easy to create, easy to verify, and easy to evaluate against the random baseline. With four options and one correct answer, random accuracy is 25%, and scores above 25% typically (though not always) mean the model beats random (PDF p. 323).

## Limitations and failure modes
- Sensitivity to presentation: performance on MCQs can vary with small changes in how the question and options are shown. Alzahrani et al. (2024) found that an extra space between question and answer, or an added instruction phrase such as "Choices:", can make a model change its answers (PDF p. 323). Prompt sensitivity and prompt engineering best practices are deferred to Chapter 5.
- Validity doubts: despite the prevalence of close-ended benchmarks, it is unclear whether they are a good way to evaluate foundation models. MCQs test the ability to tell good responses from bad ones (classification), which differs from the ability to generate good responses (PDF p. 323).
- Where MCQs fit: best for knowledge (does the model know Paris is the capital of France?) and reasoning (can it infer from a table of business expenses which department spends most?). They are not ideal for generation capabilities like summarization, translation and essay writing, which the next section addresses (PDF p. 323).

## When and how to apply
- Decide which of the four criteria buckets matter, then pick domain benchmarks (public or private) matching the capability the application needs.
- For code, add efficiency (runtime, memory) to functional correctness when it affects usability, and use subjective methods for readability.
- For knowledge and reasoning, MCQ benchmarks with accuracy (or F1, precision, recall for classification) are appropriate; compare against the random baseline; and do not use them as the main check of generation quality (PDF pp. 320-323).

## Time-sensitive statements
- The "April 2024" share of multiple-choice tasks (75%) in lm-evaluation-harness, and the named benchmarks and years, reflect the time of writing (PDF p. 321).

## Relations
Continues the criteria introduction in C04-002 and the chapter plan in C04-001. Generation capability, the next criterion, is covered in the following section (C04-004 onward). Functional correctness and exact versus subjective evaluation, including AI judges, are Chapter 3 material.
