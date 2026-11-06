---
id: C10-002
title: AI Engineering Architecture. Section Lead-in and the Simplest Architecture
source_pages: "853"
chapter: 10
concepts: [ai-architecture, simplest-architecture, model-api, query-response-flow, incremental-components, self-hosted-models]
related: [C10-001, C10-003, C10-004, C10-005, C09-001]
time_sensitive: false
---
# AI Engineering Architecture. Section Lead-in and the Simplest Architecture
(Source: PDF p. 853)

## What the section covers
The lead-in to the architecture section. It explains how the section is organised (follow a plausible production path, simplest design first, components added progressively), states how general the proposed architecture is, and defines the baseline design shown in Figure 10-1: a query goes to a model and a response comes back.

## Meaning
- A full-fledged AI architecture can be complex, so the section follows the sequence a team might actually take in production, adding components step by step (PDF p. 853).
- Applications differ a great deal, yet they share many common components. The architecture presented has been validated at multiple companies as general enough for a wide range of applications, with the caveat that some applications may deviate from it (PDF p. 853).

## How it works: the simplest form
- The application receives a query and passes it to the model. The model produces a response, which goes back to the user (PDF p. 853).
- Nothing else is present: no context augmentation, no guardrails, and no optimization (PDF p. 853).
- Figure 10-1 shows this. A user icon on the left sends an arrow labelled "Query" to a single box on the right titled "Model API", inside which there is one inner box labelled "Generation". A second arrow labelled "Response" runs from the Model API box back to the user. That is the entire diagram: one box, two arrows.
- The "Model API" box stands for two things at once: third-party APIs (the book names OpenAI, Google and Anthropic as examples) and self-hosted models. For self-hosted models someone must build an inference server, which the book defers to Chapter 9 (PDF p. 853).

## Why it matters
This baseline is the reference point for everything else in the chapter. Each later component (context construction, guardrails, router and gateway, caches, agent patterns, monitoring, orchestration) is introduced as an addition to this one-box design, so knowing exactly what the baseline lacks (context, protection, optimization) explains why each addition exists.

## Limitations of the baseline
By the book's own description, the baseline has no way to give the model outside information, no protection for the system or its users, and no latency or cost optimization (PDF p. 853). The next step list that fixes these begins on the following page (C10-003).

## Relations
Follows the chapter framing in C10-001. The first extension (adding context) is C10-003; guardrails are C10-004; router and gateway are C10-005. Building an inference server for the self-hosted case is covered by the inference optimization chapter (C09-001).
