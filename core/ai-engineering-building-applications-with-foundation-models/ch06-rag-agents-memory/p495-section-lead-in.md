---
id: C06-002
title: RAG (Section Lead-in)
source_pages: "495-497"
chapter: 6
concepts: [rag, retrieve-then-generate, context-construction, long-context, feature-engineering, hallucination, external-memory]
related: [C06-001, C06-003, C06-004]
time_sensitive: true
---
# RAG (Section Lead-in)
(Source: PDF pp. 495-497; the lead-in's final paragraphs run onto PDF p. 498, above the "RAG Architecture" heading, which starts C06-003)

## What the section covers
The definition and origin of RAG, the intuition that RAG builds per-query context, its analogy to feature engineering, and the author's argument that longer context windows will not make RAG obsolete. The top of PDF p. 495 is the end of the chapter intro (C06-001).

## Meaning
- RAG enhances a model's generation by retrieving relevant information from external memory sources. Such a source may be an internal database, a user's earlier chat sessions, or the internet (PDF p. 495).
- The retrieve-then-generate pattern first appeared in "Reading Wikipedia to Answer Open-Domain Questions" (Chen et al., 2017). The system fetched the five Wikipedia pages most relevant to a question, and a model (called the document reader there) then read them to produce the answer (PDF p. 495). Figure 6-1 on PDF p. 496 illustrates this with the question "How many of Warsaw's inhabitants spoke Polish in 1933?": a document retriever pulls the Warsaw page from Wikipedia, and the document reader, a neural model that encodes question and passage, outputs the answer 833,500 (PDF p. 496).
- The name "retrieval-augmented generation" was coined by Lewis et al. (2020) in "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks". They proposed it for knowledge-intensive tasks in which all available knowledge cannot be placed into the model directly. Only the information the retriever judges most relevant to the query is fetched and given to the model. They found that relevant information lets the model write more detailed answers and hallucinate less (PDF p. 496).
- Example of the idea: for the query "Can Acme's fancy-printer-A300 print 100pps?", the model answers better when handed the fancy-printer-A300 specifications (PDF p. 496).

## Why it matters
- RAG can be seen as building context specific to each query instead of one context for all queries. This also helps with user data: data belonging to a user can be included only in queries about that user (PDF p. 497).
- The book equates context construction for foundation models with feature engineering for classical ML models: both give the model the information needed to process an input (PDF p. 497).

## Alternatives and trade-offs: does long context kill RAG?
In the early days of foundation models, RAG was among the most common patterns, chiefly to get around limited context length. The author disagrees with the view that a long enough context ends RAG, for two reasons (PDF p. 497):
1. Whatever the context length, some applications will need more. Data volume keeps growing because people add data and rarely delete it, and context windows are expanding fast but not fast enough for arbitrary applications' data needs (PDF p. 497).
2. Handling long context is not the same as using it well (the book refers back to its earlier discussion of context length and context efficiency). The longer the context, the more likely the model attends to the wrong part. Each extra context token adds cost and may add latency. RAG lets the model see only the most relevant information per query, which cuts input tokens and may raise performance (PDF p. 497, continued on PDF p. 498).
- The author also expects work to extend context length to proceed alongside work to make models use context better, and would not be surprised if a model provider added a retrieval-like or attention-like mechanism that helps the model pick the most salient parts of a context (PDF p. 498).

## When and how to apply
- A note cites Anthropic (2024): for Claude models, if a knowledge base is under 200,000 tokens (about 500 pages), you can put the whole thing in the prompt without RAG or similar methods. The author wishes other developers gave equivalent RAG-versus-long-context guidance for their own models (PDF p. 498).
- Time-sensitive: the 200,000-token figure is specific to Claude models as of the book's writing.

## Relations
Follows the chapter framing (C06-001). The two-component system (retriever and generator) is described in the next row (C06-003), and retrieval methods in C06-004.

## Time-sensitive statements
The Anthropic 200,000-token guidance for Claude, and the remark that context length is expanding quickly, reflect the state of models when the book was written (PDF pp. 497-498).
