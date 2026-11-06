---
id: C02-014
title: Structured Outputs
source_pages: "206-213"
chapter: 2
concepts: [structured-outputs, semantic-parsing, json-mode, constrained-sampling, grammar, post-processing, finetuning-for-format, classifier-head]
related: [C02-011, C02-012, C02-013, C02-008, C02-015, C03-015, C04-005, C05-007, C06-008, C07-002]
time_sensitive: false
---
# Structured Outputs
(Source: PDF pp. 206-213, plus the pre-heading text of the tail page, PDF p. 214)

## What the section covers
How to get a foundation model to emit output in a required format: the two situations that call for structure, the tools that support it, and five layers at which to intervene (prompting, post-processing, test time compute, constrained sampling, finetuning), with their costs and limits.

## Meaning
- In production, models often must produce outputs that follow a particular format (PDF p. 206).
- Semantic parsing: converting natural language into a structured, machine-readable form. Text-to-SQL is the example; the output must be a valid query. It lets people use an API in plain English, e.g. asking a Postgres database for "the average monthly revenue over the last 6 months" without writing PostgreSQL (PDF p. 206).
- JSON mode: a feature of a provider's text generation API (OpenAI introduced it first) that usually guarantees only that the output is valid JSON, not that the contents are right (PDF p. 208).

## Why it matters: two scenarios
1. Tasks that inherently need structured output (PDF pp. 206-207). Semantic parsing is the main category. The book shows a text-to-regex prompt for GPT-4o: a system prompt asks for a regex covering all ways an item can be written and to return only the regex, gives one example (US phone number), and then the user supplies items such as "Email address" and "Dates"; the model returns a regex for each. Classification is another such task, since outputs must be valid classes (PDF p. 207).
2. Tasks whose outputs feed downstream applications (PDF p. 208). The task itself need not be structured, but another program must parse the result. Example: an AI-written email is free text, yet the consuming application may need a JSON document with specific keys such as title and body. This matters especially for agentic workflows, where model outputs become inputs to tools (Chapter 6 in the book) (PDF p. 208).

## Tools and provider support
- Frameworks that support structured outputs: guidance, outlines, instructor and llama.cpp. Individual providers also use their own techniques (PDF p. 208).
- Figure 2-20 (rendered and checked) shows guidance in two uses: generation constrained to a set of options (a color chosen from red, blue, green after "I like the color") and generation constrained to a regex (a digits-only answer to a small arithmetic word problem, answering 7) (PDF p. 209).

## JSON mode caveats
- Valid JSON does not mean correct content (PDF p. 208).
- Valid JSON can still be truncated and unparsable if generation stops early, for example on hitting the maximum output token length. Setting that limit too high makes responses slow and expensive (PDF p. 208).

## How it works: five layers
The book says structure can be encouraged at five layers of the AI stack: prompting, post-processing, test time compute, constrained sampling and finetuning. The first three are described as bandages that work when the model is already fairly good at the format and needs a nudge; constrained sampling and finetuning are the "intensive treatment" (PDF p. 209). Test time compute was covered in the previous section (generate until an output fits the expected format), so this section covers the other four (PDF pp. 209-210).

### Prompting
- First line of action: instruct the model to use the format. Success depends on the model's instruction-following ability (Chapter 4) and instruction clarity (Chapter 5) (PDF p. 210).
- No guarantee: even a few percent of invalid outputs can be unacceptable (PDF p. 210).
- To raise validity, some people use AI to validate or fix the first output, which is AI as a judge (Chapter 3). That means at least two model calls per output. It can help a lot, but the added cost and latency may be too much (PDF p. 210).

### Post-processing
- Simple, cheap and surprisingly effective. The author's teaching experience: students repeat similar mistakes, and models likewise repeat the same mistakes across queries. If you find the common ones, a script can fix them, such as adding a missing closing bracket to JSON (PDF pp. 210-211).
- Evidence: LinkedIn's defensive YAML parser raised the share of correct YAML outputs from 90% to 99.99% (PDF p. 211).
- Tip from the book: JSON and YAML are both common. LinkedIn found GPT-4 handled both but chose YAML because it is less verbose and so needs fewer output tokens (PDF p. 211).
- Works only if mistakes are easy to fix, which usually means output is mostly well formatted with occasional small slips (PDF p. 211).

### Constrained sampling
- A technique to steer generation toward constraints, typically delivered by structured-output tools (PDF p. 211).
- Mechanism: the model emits a logit vector with one logit per vocabulary token. Constrained sampling filters this vector to keep only tokens meeting the constraint, then samples from those valid tokens (PDF pp. 211-212). Figure 2-21 (rendered) shows: input to model, logits for the entire vocabulary, a filter fed by a constraint (example: output may only be one of red, green, blue), logits for valid tokens only, then softmax to probabilities (PDF p. 212).
- Real formats need a grammar stating what is allowed at each step. JSON example: after an opening brace you may not open another one unless it is inside a string (PDF p. 212).
- Costs: building a grammar and wiring it into sampling is nontrivial. Each format (JSON, YAML, regex, CSV and so on) needs its own grammar, so the technique generalizes poorly and is limited to formats supported by external tools or your own team. Grammar verification can add generation latency (PDF pp. 212-213).
- Some people oppose it, arguing the same resources are better spent training models to follow instructions (PDF p. 213).

### Finetuning
- Finetuning on examples in the desired format is described as the most effective and general approach, working with any format. Plain finetuning does not guarantee the format but is far more reliable than prompting (PDF p. 213).
- For some tasks the format can be guaranteed by changing the architecture before finetuning. For classification, attach a classifier head to the foundation model so it can output only one of the predefined classes. This is also called feature-based transfer, covered with transfer learning in Chapter 7 (PDF p. 213).
- Figure 2-22 (tail page, rendered and checked) is a left-to-right pipeline: input, pretrained model, an embedding vector, a classifier layer, logits for Class 0, 1 and 2, a softmax, and then probabilities for the same three classes (PDF p. 214).
- During finetuning you can retrain everything end to end or only part, such as the classifier head. End to end needs more resources but promises better performance (PDF p. 214).

## Assumptions and outlook
- These techniques exist on the assumption that the model alone cannot generate structured outputs. The author expects models to improve at following instructions, so that minimal prompting will eventually yield exactly the needed output and these techniques will matter less (PDF p. 214).

## When and how to apply
INTERPRETATION: from the book's ordering, start with prompting, add cheap post-processing for recurring slips, and move to constrained sampling or finetuning when invalid outputs are costly. The book states the first three suit a model already near the target format, and the last two are for harder cases (PDF p. 209).

## Alternatives and trade-offs (summary)
- Prompting: easiest, no guarantee; optional AI validator adds a second call.
- Post-processing: cheapest, only for easily fixable errors.
- Constrained sampling: guarantees conformance to a grammar but needs per-format grammars and may add latency.
- Finetuning: general and more reliable; classifier head can guarantee class outputs.

## Relations
Builds on sampling and logits (C02-011, C02-012) and on test time compute (C02-013). Instruction following is in Chapter 4 (C04-005) and AI as a judge in Chapter 3 (C03-015). Prompt clarity is in C05-007 and tool use by agents in C06-008. Finetuning is in Chapter 7 (C07-002).
