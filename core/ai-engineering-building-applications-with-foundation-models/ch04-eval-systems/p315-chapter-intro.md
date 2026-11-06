---
id: C04-001
title: Chapter 4 Introduction - Evaluate AI Systems
source_pages: "315"
chapter: 4
concepts: [evaluation, evaluation-criteria, model-selection, benchmarks, leaderboards, hosting-vs-api, evaluation-pipeline]
related: [C04-002, C04-003, C04-004]
time_sensitive: false
---
# Chapter 4 Introduction - Evaluate AI Systems
(Source: PDF p. 315)

## What the section covers
The opening of Chapter 4. It states why evaluation has to be done in the context of one's own application, links the chapter to the evaluation methods of Chapter 3, and previews the three parts of the chapter. The last sentence of the preview spills onto the next page (PDF p. 316).

## Meaning
- The chapter's premise is that a model is only useful if it works for the purposes it is meant for, so models must be judged against the application they will serve (PDF p. 315).
- Chapter 3 covered the different approaches to automatic evaluation. Chapter 4 turns to how those approaches are used to evaluate models for real applications (PDF p. 315).

## How the chapter is organised
1. **Evaluation criteria.** The criteria one might use to evaluate an application, and how each is defined and calculated. The page's examples of questions this part answers: many people worry about AI inventing facts, so how is factual consistency detected? And how are domain-specific capabilities such as math, science, reasoning and summarization measured? (PDF p. 315)
2. **Model selection.** The number of foundation models keeps growing, which makes choosing one feel overwhelming. Thousands of benchmarks evaluate models along different criteria, so the questions are whether benchmarks can be trusted, how to pick which ones to use, and what to make of public leaderboards that aggregate several benchmarks (PDF p. 315). This part also covers a decision many teams revisit repeatedly: whether to host their own model or use a model API. The landscape mixes proprietary and open source models, and the question has become subtler now that API services exist that are built on top of open source models (PDF p. 315).
3. **Building an evaluation pipeline.** The last part is about designing an evaluation pipeline that can steer the application's development over time. It pulls together the techniques from across the book to evaluate concrete applications (PDF p. 316).

## Why it matters
The framing sets up the rest of the chapter: evaluation is application-specific, criteria come first, model choice depends on trustworthy benchmark evidence, and the end product is a reusable pipeline rather than a one-off test (PDF pp. 315-316).

## Relations
The criteria part begins in C04-002 (lead-in) and C04-003 (domain-specific capability). Model selection, benchmark trustworthiness and leaderboards, and the host-versus-API question appear in later Chapter 4 sections (see C04-004 onward); the pipeline discussion closes the chapter.
