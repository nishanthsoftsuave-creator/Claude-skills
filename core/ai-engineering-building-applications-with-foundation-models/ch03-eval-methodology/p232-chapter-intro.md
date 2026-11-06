---
id: C03-001
title: Evaluation Methodology Chapter Introduction
source_pages: "232-233"
chapter: 3
concepts: [evaluation, catastrophic-failure, systematic-evaluation, automatic-evaluation, exact-evaluation, subjective-evaluation, ai-as-a-judge, human-evaluation]
related: [C03-002, C03-003, C03-009, C03-013, C04-001]
time_sensitive: false
---
# Evaluation Methodology Chapter Introduction
(Source: PDF pp. 232-233)

## What the section covers
The framing of Chapter 3: why evaluation is the main obstacle to shipping AI applications, how the book splits evaluation across two chapters, and a roadmap of the topics the chapter will treat (language modeling metrics, exact evaluation, subjective evaluation with AI as a judge).

## Why it matters
- The wider AI is deployed, the more chances there are for a catastrophic failure. The author lists failures already seen in the short life of foundation models: a man who died by suicide after a chatbot encouraged him, lawyers who filed fake evidence invented by AI, and Air Canada being ordered to pay damages after its chatbot gave a passenger false information (PDF p. 232).
- Without a means of quality-controlling AI outputs, the risk may outweigh the benefit for many applications (PDF p. 232).
- As teams hurry to adopt AI, many discover that evaluation is the biggest hurdle to getting an application into reality. For some applications, working out evaluation can consume most of the development effort (PDF p. 232).

## How the book organizes the topic
- Because evaluation is both important and complex, the book gives it two chapters. This chapter covers the methods used to evaluate open-ended models, how they work and where they fall short. The next chapter covers using these methods to select models for an application and to build an evaluation pipeline for the application (PDF p. 232).
- Even though evaluation gets its own chapters, it must be judged within the context of the entire system rather than in isolation (PDF p. 232).

## When and how to apply: evaluation in a system context
- Evaluation has two aims: to reduce risk and to uncover opportunity (PDF p. 232).
- To reduce risk, first find where the system is likely to fail, then design the evaluation around those places. This can require redesigning the system so its failures become more visible (PDF pp. 232-233).
- Without a clear picture of where the system fails, no number of metrics or tools can make it robust (PDF p. 233).

## Alternatives and trade-offs
- Because evaluation is hard, many people fall back on word of mouth (someone says model X is good) or on eyeballing outputs. The book says this adds risk and slows application iteration, and argues for investing in systematic evaluation for more reliable results (PDF p. 233).
- Human evaluators remain a necessary option for many applications, but human annotation is slow and expensive, so the stated goal is to automate evaluation. The book concentrates on automatic evaluation, which includes both exact and subjective evaluation (PDF p. 233).

## Chapter roadmap (as previewed on these pages)
1. Challenges of evaluating foundation models, before any method is introduced (PDF p. 233).
2. A quick overview of metrics for language models, including cross entropy and perplexity. Many foundation models contain a language model component; these metrics guide training and finetuning of language models and appear inside many other evaluation methods (PDF p. 233).
3. Best practices for tackling the difficulty that foundation models are open-ended (PDF p. 233).
4. Automatic evaluation split into exact evaluation and subjective evaluation (PDF p. 233).
5. AI as a judge, using AI to evaluate AI responses, called the rising star of subjective evaluation. It is subjective because the score depends on which model and prompt the judge uses. It is spreading quickly in industry but meets strong opposition from people who think AI is not trustworthy enough for such an important job. The author says he is especially keen to explore this debate. (This item is the last paragraph of the chapter intro and sits at the top of the next page, which the matrix assigns to C03-002, so no page is cited here.)

## Relations
Opens the chapter; challenges are detailed in C03-002, language modeling metrics begin at C03-003, exact evaluation at C03-009, AI as a judge at C03-013. The follow-on chapter on model selection and evaluation pipelines starts at C04-001.
