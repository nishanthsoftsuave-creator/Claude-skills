---
id: C10-007
title: Step 5. Add Agent Patterns
source_pages: "875-876"
chapter: 10
concepts: [architecture-with-caches, agent-patterns, feedback-loop, write-actions, orchestration-complexity, failure-modes]
related: [C10-006, C10-008, C06-010, C10-005]
time_sensitive: false
---
# Step 5. Add Agent Patterns
(Source: PDF pp. 875-876; the section's closing paragraph and Figure 10-10 continue at the top of the next page, above the Monitoring and Observability heading, and are summarised without page cites here)

## What the section covers
The fifth step of the architecture: moving from a simple sequential application flow to one with loops, parallel branches and conditional logic by adding agentic patterns (Chapter 6), and allowing the model to take write actions. It also holds the tail end of Step 4: Figure 10-8, the platform diagram with caches added.

## Figure 10-8: architecture with the added caches (PDF p. 875)
The book says the platform now looks like this figure. The diagram, as rendered: a user icon sends a query into a cache; on a hit a dashed "cached response" arrow goes straight back to the user, on a miss the query goes on to a context-construction box (examples: RAG, agent, query rewriting). A second cache sits between context construction and the read-only actions box (examples: vector search, SQL queries, web search) and the databases (documents, tables, chat history, vector DB). Context then flows to input guardrails (example: PII redaction), then into a model gateway (model catalog, access token management) containing routing, generation and scoring, then to output guardrails (safety/verification, structured outputs), and the response returns to the user (a branch of the response line also runs up into the first cache). The text notes that KV cache and prompt cache are usually implemented by model API providers, so they are not drawn; if you wanted to show them, they would go inside the Model API box. The new element is an arrow that writes generated responses into the cache (PDF p. 875).

## Meaning and how it works

### Agentic patterns
- Everything so far gives each query a sequential flow. Real flows can contain loops, parallel execution and conditional branching, and the agent patterns of Chapter 6 are what enable such complex applications (PDF p. 875).
- Example loop: after producing an output the system may judge that the task is unfinished and perform another retrieval for more information. The first response plus the new context goes into the same model or a different one. This creates a loop (PDF pp. 875-876).
- Figure 10-9 shows this: the same architecture as Figure 10-8 plus a highlighted (yellow) arrow taking the response from the output-guardrails side back into the context-construction stage, so a generated response can re-enter the system (PDF p. 876).

### Write actions
- Model outputs can also trigger write actions: composing an email, placing an order, starting a bank transfer. These let the system change its environment directly (PDF p. 876).
- Trade-off: write actions make a system far more capable but expose it to much greater risk, so granting a model access to them must be done with the utmost care (PDF p. 876).
- The architecture with write actions is Figure 10-10 (printed on the next page, described in C10-008): a new write-actions box (examples: update orders, send emails) fed from the output stage, with the final response going to the user.

## Limitations and failure modes
The book's remark after the last step: a system that has followed all steps is probably complex; complex systems solve more tasks but have more failure modes and are harder to debug because there are many points of failure. This motivates the observability section that follows.

## Relations
Builds on caches (C10-006) and the gateway (C10-005); agent planning and tools are developed in C06-010; observability, which the book presents as the answer to the added complexity, is C10-008.
