---
id: C06-003
title: RAG Architecture
source_pages: "498-499"
chapter: 6
concepts: [rag-architecture, retriever, generator, indexing, querying, chunking, end-to-end-finetuning]
related: [C06-002, C06-004]
time_sensitive: false
---
# RAG Architecture
(Source: PDF pp. 498-499; the section ends on PDF p. 500 above the "Retrieval Algorithms" heading, which starts C06-004)

## What the section covers
The basic structure of a RAG system, the two components and how they are trained, the two retriever functions (indexing and querying), and a worked walk-through using a document database that introduces chunking.

## Meaning
- A RAG system has two components: a retriever, which gets information from external memory sources, and a generator, which writes the response from the retrieved information (PDF p. 498).
- Figure 6-2 (PDF p. 499) shows the basic architecture: external memory (documents, tables, chat history and so on) feeds the retriever. The user's prompt goes both to the retriever and directly to the generative model. The retriever passes "context relevant to query" to the generative model, which outputs the response back to the user (PDF p. 499).
- Terminology note: the chapter uses "document" for both documents and chunks, since a chunk is technically a document too. This keeps the book consistent with classical NLP and information retrieval vocabulary (PDF p. 500, the note above the next heading).

## How it works
- Training: in the original RAG paper Lewis et al. trained retriever and generator jointly. In current RAG systems the two are often trained separately, and many teams assemble systems from off-the-shelf retrievers and models. Even so, finetuning the whole system end to end can improve it significantly (PDF p. 499).
- A RAG system's success hinges on its retriever's quality. The retriever has two functions: indexing, which processes data so it can be retrieved quickly later, and querying, which sends a query to fetch the relevant data. How you index depends on how you want to retrieve later (PDF pp. 499-500).
- Worked example (PDF p. 500): assume the external memory is a database of documents such as company memos, contracts and meeting notes. A document may be 10 tokens or 1 million tokens, and retrieving whole documents naively could make the context arbitrarily long. So each document is split into more manageable chunks (chunking strategies are deferred to a later part of the chapter). For each query the goal is to retrieve the chunks most relevant to it. Minor post-processing then joins the retrieved chunks with the user prompt to form the final prompt, which goes to the generative model.

## Why it matters
Because retrieval quality dominates RAG success, the following retrieval-algorithm section (C06-004) is where most of the engineering choices lie.

## Relations
Builds on the RAG definition and long-context argument (C06-002) and leads into retrieval algorithms (C06-004).
