---
id: P-002
title: Preface - What This Book Is About
source_pages: "11-14"
chapter: preface
concepts: [book-scope, foundation-models, llm, lmm, fundamentals-over-tools, designing-ml-systems, lindys-law, start-simple]
related: [P-001, P-003, P-004, P-005, C01-001]
time_sensitive: false
---
# Preface - What This Book Is About
(Source: PDF pp. 11-14, tail PDF p. 15. The top of PDF p. 11 is the end of the preceding opening section, covered in P-001. The heading starts on PDF p. 12.)

## What the section covers
The book's scope: a framework for adapting foundation models to applications, the questions it helps answer, its fundamentals-first stance, its relationship to the author's earlier book Designing Machine Learning Systems, and the criteria used to decide what content would last.

## Meaning
- The book provides a framework for adapting foundation models, a term covering both large language models (LLMs) and large multimodal models (LMMs), to specific applications (PDF p. 12).
- There are many ways to build an application. The book lays out several solutions and also supplies questions you can use to judge which fits your needs (PDF p. 12).

## Questions the book helps answer (PDF p. 12)
- Should I build this AI application?
- How do I evaluate it, and can AI evaluate AI outputs?
- What causes hallucinations, and how do I detect and mitigate them?
- What are the best practices in prompt engineering?
- Why does RAG work, and what strategies exist for it?
- What is an agent, and how do I build and evaluate one?
- When should a model be finetuned and when not?
- How much data is needed, and how is data quality validated?
- How do I make a model faster, cheaper, and secure?
- How do I build a feedback loop that keeps improving the application?

The book also aims to help readers navigate an overwhelming landscape: types of models, evaluation benchmarks, and a seemingly endless set of use cases and application patterns (PDF pp. 12-13).

## Method and stance
- Content is illustrated with case studies, many of which the author worked on, supported by extensive references and reviewed by experts from varied backgrounds. Writing took two years but draws on roughly a decade of experience with language models and ML systems (PDF p. 13).
- Like the author's earlier O'Reilly book, Designing Machine Learning Systems (DMLS), this book concentrates on fundamentals rather than any particular tool or API: tools go out of date fast, fundamentals last longer (PDF p. 13).

## Reading AIE with DMLS (PDF p. 14)
- AIE (this book) can accompany DMLS. DMLS is about applications on traditional ML models: more tabular-data annotation, feature engineering, and model training. AIE is about applications on foundation models: more prompt engineering, context construction, and parameter-efficient finetuning.
- Both books are self-contained and modular; either can be read alone.
- Because foundation models are ML models, some concepts apply to both. Topics relevant to AIE that DMLS covers at length are still covered here, more briefly, with pointers to resources. Many topics appear in only one of the two books.
- Chapter 1 of this book covers differences between traditional ML engineering and AI engineering. Real systems often mix traditional ML models and foundation models, so knowing both is often needed.

## Deciding what will last (PDF pp. 14-15)
The author admits that judging longevity is hard and used three criteria:
1. Whether a problem stems from fundamental limitations of how AI works or would disappear with better models. For fundamental problems the book analyzes the challenges and solutions. The author favors a start-simple approach, so for many problems the book begins with the simplest solution and moves to more complex ones as challenges grow (PDF pp. 14-15).
2. Consulting an extensive network of researchers and engineers about which problems and solutions matter most (PDF p. 15).
3. Occasionally, Lindy's Law: a technology's future life expectancy is proportional to its current age, so something that has existed a while is assumed to persist a while longer (PDF p. 15).
The author notes an exception: some concepts believed to be temporary are included because they are immediately useful to some developers or illustrate an interesting way of solving problems (PDF p. 15).

## Relations
Preceded by P-001; followed by P-003 (what the book is not), P-004 (audience), P-005 (chapter roadmap). Chapter 1 (C01-001) covers AI engineering versus ML engineering.
