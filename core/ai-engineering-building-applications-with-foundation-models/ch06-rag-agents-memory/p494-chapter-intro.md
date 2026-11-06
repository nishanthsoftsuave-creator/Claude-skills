---
id: C06-001
title: Chapter 6 Introduction. RAG and Agents
source_pages: "494"
chapter: 6
concepts: [context-construction, rag, agents, tool-use, instructions-vs-context, hallucination]
related: [C06-002, C06-003]
time_sensitive: false
---
# Chapter 6 Introduction. RAG and Agents
(Source: PDF p. 494; the intro's last two sentences continue onto PDF p. 495, whose text below the "RAG" heading belongs to C06-002)

## What the section covers
The opening framing of the chapter. It explains why a model needs per-query context in addition to instructions, names the two dominant patterns for building that context (retrieval-augmented generation and agents), and previews what the rest of the chapter will examine.

## Meaning
- To complete a task, a model needs two ingredients: instructions describing how to do it, and the information necessary to do it (PDF p. 494).
- A model that lacks context behaves like a person lacking information: it is more likely to answer wrongly and to hallucinate (PDF p. 494).
- Instructions are shared by all queries of an application, whereas context differs for every query. The previous chapter (prompt engineering) dealt with writing instructions; this chapter deals with constructing the relevant context for each query (PDF p. 494).

## How it works: the two patterns
- RAG (retrieval-augmented generation): the model retrieves relevant information from external data sources (PDF p. 494).
- The agentic pattern: the model uses tools, for example web search and news APIs, to gather information (PDF p. 494).
- RAG is mainly a context-construction technique. Agents go further: external tools can compensate for a model's weaknesses and extend what it can do, and above all they let a model act directly on the world, which is what makes it possible to automate many parts of daily life (PDF p. 494).

## Why it matters
Both patterns add capability to already strong models. The book notes they quickly captured the collective imagination (the sentence ends on PDF p. 495), producing demos and products that persuade many people they are the future; the chapter promises to explain how each pattern works and why it is promising.

## Relations
Leads into the RAG section (C06-002 lead-in, then the architecture in C06-003). The agent portion of the chapter appears later in the chapter, beyond the RAG rows.
