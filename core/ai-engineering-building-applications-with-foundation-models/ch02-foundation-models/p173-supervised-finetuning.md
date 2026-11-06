---
id: C02-008
title: Supervised Finetuning
source_pages: "173-178"
chapter: 2
concepts: [supervised-finetuning, sft, demonstration-data, behavior-cloning, labelers, instructgpt, data-cost, post-training]
related: [C02-007, C02-009, C02-010]
time_sensitive: true
---
# Supervised Finetuning
(Source: PDF pp. 173-178)

## What the section covers
The first post-training step: why a pre-trained model needs supervised finetuning (SFT), what demonstration data is, who produces it, what it costs, and cheaper alternatives to expert human labeling.

## Meaning
- A pre-trained model is usually optimized for completion, not for conversation (PDF p. 173). Given "How to make pizza", it may extend the sentence with more context ("for a family of six?"), add follow-up questions, or give instructions. All three are valid completions, but only the third, the instructions, answers the user appropriately (PDF p. 173).
- Since a model mimics its training data, you steer it by showing examples of appropriate responses. These examples are (prompt, response) pairs called demonstration data. The process is also called behavior cloning: you show how the model should behave and it copies that behavior (PDF p. 173).

## How it works
- Different request types need different responses, so demonstration data must cover the range of tasks the model should handle, for example question answering, summarization and translation (PDF pp. 173-174).
- Figure 2-12 (a ring chart built from numbers in the OpenAI paper) shows the prompt mix used to finetune InstructGPT: generation about 45.6%, open QA 12.4%, brainstorming 11.2%, chat 8.4%, rewrite 6.6%, summarization 4.2%, classification 3.5%, other 3.5%, closed QA 2.6%, extract 1.9% (PDF p. 174). The book notes there are no multimodal tasks because InstructGPT is text-only (PDF p. 174).
- Good labelers matter for an AI learning to converse just as good teachers matter for people. Unlike ordinary data labeling, which needs little domain expertise, demonstration data can involve complex prompts whose answers need critical thinking, information gathering and judgment about whether the user's request is appropriate (PDF pp. 174-175).
- Table 2-6 gives InstructGPT examples: using "serendipity" in a sentence; reading an article (about Justice Ruth Bader Ginsburg's death) and answering three questions, including a reasoning answer about the court's controlling vote; and an "ELI5" explanation of the anxiety lump in the chest, attributed to muscular tension keeping the glottis dilated and to the vagus nerve (PDF pp. 176-177). They show how varied and demanding the labelers' responses are.

## Cost and labeler quality
- Because the work is hard, companies often hire highly educated labelers: about 90% of InstructGPT's demonstration labelers had at least a college degree and over a third had a master's (PDF p. 177).
- Labeling an image object may take seconds, but one (prompt, response) pair can take up to 30 minutes, especially for long-context tasks such as summarization. At a hypothetical $10 per pair, the 13,000 pairs OpenAI used would cost $130,000, before counting task and prompt design, labeler recruitment and quality control (PDF pp. 177-178).

## Alternatives and trade-offs
- LAION, a non-profit, recruited 13,500 volunteers to produce 10,000 conversations: 161,443 messages in 35 languages, annotated with 461,292 quality ratings (PDF p. 178). Volunteer data gave little control over bias. Labelers who teach human preference should in theory represent the human population, but LAION's were skewed; a self-reported survey found 90% identified as male (Köpf et al., 2023) (PDF p. 178).
- DeepMind used simple heuristics to filter conversations from internet data for Gopher, claiming they reliably produce high-quality dialogue. They looked for text shaped as alternating speaker turns, [A]: short paragraph, [B]: short paragraph, repeated (PDF pp. 178-179).
- To lessen reliance on human-written data, many teams use AI-generated (synthetic) data, covered in Chapter 8 (PDF p. 179).
- In principle you could train on demonstration data from scratch and skip self-supervised pre-training, but pre-training followed by finetuning has often given better results (PDF p. 179).

## Limitations and failure modes
- High-quality human annotation is expensive and out of reach for many teams (PDF p. 178).
- Volunteer or cheap labeling can introduce demographic bias (PDF p. 178).

## Relations
Follows pre-training (C02-007). Preference finetuning, the second post-training step, is C02-009. The sampling section that follows is C02-010 and C02-011. Synthetic data is expanded in Chapter 8.

## Time-sensitive statements
- InstructGPT task mix, 13,000 pairs, and LAION figures are as reported at the book's writing (PDF pp. 174, 178). The $10 per pair is the book's illustrative assumption.
