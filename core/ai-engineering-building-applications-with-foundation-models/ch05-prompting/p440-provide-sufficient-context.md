---
id: C05-008
title: Provide Sufficient Context
source_pages: "440-441"
chapter: 5
concepts: [context-construction, hallucination-mitigation, restricting-model-knowledge, rag, roleplay, grounding, finetuning-limits]
related: [C05-007, C05-009, C05-005, C06-002, C06-003]
time_sensitive: false
---
# Provide Sufficient Context
(Source: PDF pp. 440-441)

## What the section covers
The second best practice: give the model the information it needs to answer, either directly in the prompt or through tools that fetch it. A boxed sidebar, "How to restrict a model's knowledge to only its context", discusses the harder case where the model must use nothing but the supplied context (PDF p. 441).

## Meaning
- Context works like reference texts for a student sitting an exam: it helps the model do better. If you want questions answered about a paper, put the paper in the context (PDF p. 440).
- Context construction is the book's term for gathering the necessary context for a given query. Tools for it include data retrieval (as in a RAG pipeline) and web search; these are covered in Chapter 6 (PDF p. 440).

## Why it matters
- Sufficient context improves response quality and can mitigate hallucinations. When the needed information is missing, the model falls back on its internal knowledge, which may be unreliable, and that is what produces hallucination (PDF p. 440).
- You have two options: supply the context yourself, or give the model tools to collect it (PDF p. 440).

## How it works: restricting a model to its context (sidebar)
- Motivation: in many scenarios, such as roleplay and simulation, the model should know only what the provided context contains. Example: a model playing a character in Skyrim should know only that game universe and should not be able to answer "What's your favorite Starbucks item?" (PDF p. 441).
- This restriction is tricky. Helpful measures are a clear instruction such as "answer using only the provided context", plus examples of questions it must not be able to answer. You can also tell the model to quote the place in the provided corpus where its answer comes from, which nudges it toward answers the context supports (PDF p. 441).

## Limitations and failure modes
- No guarantee that the model follows every instruction, so prompting alone may not reliably deliver the restriction (PDF p. 441).
- Finetuning on your own corpus is another route, but pretraining data can still leak into responses (PDF p. 441).
- The safest approach is training a model only on the permitted corpus, but this is often infeasible, and the corpus may be too small to yield a high-quality model (PDF p. 441).

## When and how to apply
INTERPRETATION: Include the source material when the answer depends on it; use retrieval or search when the material is too large or unknown ahead of time; for closed-world uses combine a context-only instruction, negative examples and a request to quote sources, while accepting that this is not a guarantee.

## Relations
Follows clear instructions (C05-007); context construction via retrieval is developed in the RAG sections (C06-002, C06-003). Context length considerations are in C05-005. Next: decomposing tasks (C05-009).
