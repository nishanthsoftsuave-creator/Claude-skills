---
id: C10-003
title: Step 1. Enhance Context
source_pages: "854-855"
chapter: 10
concepts: [context-construction, enhance-context, rag, tool-use, feature-engineering, architecture-roadmap, provider-differences]
related: [C10-002, C10-004, C10-005, C10-006, C10-007, C10-008, C10-009, C06-003]
time_sensitive: false
---
# Step 1. Enhance Context
(Source: PDF pp. 854-855; the page 855 text ends by pointing to Figure 10-2, which is printed on the next page and is described in C10-004)

## What the section covers
First, the five-step roadmap the chapter follows for growing the simple architecture of C10-002, plus a note on what comes after the five steps. Second, the first step itself: building the context the model needs for each query, by retrieval and by tools, and how providers and frameworks differ in supporting it.

## The roadmap (PDF p. 854)
Starting from the simple architecture, components are added as needs arise. The order the book presents:
1. Enhance the context fed to the model, by giving it access to external data sources and tools for gathering information.
2. Put in guardrails to protect the system and its users.
3. Add a model router and gateway, to support complex pipelines and add more security.
4. Optimize latency and cost with caching.
5. Add complex logic and write actions, to maximize what the system can do.

Caveats and additions from the same page:
- This order is the progression the author commonly sees in production, but everyone's needs differ, so teams should use whatever order suits their application (PDF p. 854).
- Monitoring and observability, which every application needs for quality control and performance improvement, are discussed at the end of the process. Orchestration, which chains all the components together, comes after that (PDF p. 854).

## Meaning: Step 1, enhance context
- The first expansion of a platform usually adds mechanisms that let the system build the relevant context the model needs to answer each query (PDF pp. 854-855).
- Per Chapter 6, context can be constructed through several retrieval mechanisms: text retrieval, image retrieval and tabular data retrieval (PDF pp. 854-855).
- Context can also be augmented with tools that let the model gather information automatically through APIs. The examples given are web search, news, weather and events (PDF p. 855).
- The book likens context construction to feature engineering for foundation models: it supplies the information the model needs to produce an output (PDF p. 855).

## Why it matters
Because context construction has such a central effect on output quality, it is almost universally supported by model API providers. As examples, OpenAI, Claude and Gemini let users upload files and let their models use tools (PDF p. 855).

## Alternatives and trade-offs: providers differ
Providers differ in context construction support just as models differ in capability (PDF p. 855):
- Document handling: there may be limits on the types of documents and on how many can be uploaded. A specialized RAG solution may accept as many documents as the vector database can hold, while a generic model API may allow only a small number (PDF p. 855).
- Frameworks differ in retrieval algorithms and other retrieval settings such as chunk size (PDF p. 855).
- Tool use differs in which tools are supported and in execution modes, for example whether parallel function execution or long-running jobs are supported (PDF p. 855).

INTERPRETATION: Since these limits vary, check a provider's or framework's context support against your data volume and tool needs before relying on it.

## Resulting architecture
With context construction added, the architecture is drawn in Figure 10-2 (printed on the next row's first page; see C10-004 for its description).

## Relations
Extends the baseline in C10-002. The retrieval material it builds on is in the RAG architecture section (C06-003). The next component is guardrails (C10-004), then router and gateway (C10-005), caching (C10-006) and agent patterns (C10-007); monitoring is C10-008 and orchestration C10-009.
