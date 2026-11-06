---
id: C05-009
title: Break Complex Tasks into Simpler Subtasks
source_pages: "442-447"
chapter: 5
concepts: [prompt-decomposition, prompt-chaining, intent-classification, monitoring, debugging, parallelization, latency-cost-tradeoff, model-routing]
related: [C05-007, C05-008, C05-010, C05-011, C06-008]
time_sensitive: false
---
# Break Complex Tasks into Simpler Subtasks
(Source: PDF pp. 442-447; the last paragraph of PDF p. 447, about GoDaddy's prompt, continues onto the next page, whose first lines finish it)

## What the section covers
The third best practice: replace one giant prompt with several smaller prompts, one per subtask, chained together. It gives a customer-support example from OpenAI's guide, lists the benefits (monitoring, debugging, parallelization, effort), and discusses the drawbacks in latency and cost.

## Meaning and how it works
- Decomposition: each subtask gets its own prompt and the prompts are linked in sequence (PDF p. 442).
- Customer-support chatbot example, two steps (PDF p. 442):
  1. Intent classification: identify what the request is about.
  2. Response generation: given the intent, instruct the model how to answer. With ten possible intents, ten different response prompts are needed.
- Prompt 1 (classification), from OpenAI's guide, lightly shortened. The system prompt says the model will receive customer service queries and must classify each into a primary and a secondary category, outputting JSON with keys "primary" and "secondary". Primary categories are Billing, Technical Support, Account Management and General Inquiry, each with a list of secondary categories (for instance Billing has "Unsubscribe or upgrade", Technical Support has "Troubleshooting"; the others are elided with ellipses). The user message is "I need to get my internet working again." (PDF pp. 443-444).
- Prompt 2 (response for the troubleshooting intent): the system prompt tells the model to help the user by asking them to check that all router cables are connected (noting cables often come loose); if that does not fix it, asking which router model they use; and if the problem persists after restarting and waiting five minutes, connecting them to IT support by outputting {"IT support requested"}. If the user turns to unrelated topics, the model should confirm whether they want to end the troubleshooting chat and then classify the new request with the scheme from Prompt 1. The user message is the same internet complaint (PDF pp. 444-446).
- Granularity question: why not split classification further into one prompt for the primary category and one for the secondary? The book says how small a subtask should be depends on the use case and on the performance, cost and latency trade-off you accept, so you must experiment to find the best decomposition and chaining (PDF p. 446).

## Why it matters: benefits
Models are improving at complex instructions but still do better with simpler ones; decomposition improves performance and also gives (PDF p. 446):
- Monitoring: you can watch intermediate outputs, not just the final one.
- Debugging: you can isolate the failing step and fix it without changing behavior at other steps.
- Parallelization: independent steps can run at once. Example: generating three story versions for first grade, eighth grade and college freshman reading levels at the same time, which greatly reduces output latency (PDF pp. 446-447).
- Effort: simple prompts are easier to write than complex ones (PDF p. 447).

## Limitations and trade-offs
- Latency: perceived latency can rise, particularly when users do not see intermediate outputs, because the time to the first token of the final step grows with each added step (PDF p. 447).
- Cost: more model queries usually means higher cost, but two decomposed prompts may not cost double a single one, since APIs charge per input and output token and smaller prompts often use fewer tokens (PDF p. 447).
- Cost lever: cheaper models can handle simple steps. In customer support it is common to use a weaker model for intent classification and a stronger one to generate the response (PDF p. 447).
- Even when cost goes up, the book says better performance and reliability can make it worthwhile (PDF p. 447).

## When and how to apply
As an application evolves, its prompt tends to grow with more detailed instructions, examples and edge cases (PDF p. 447). The cited case is GoDaddy (2024), whose support-chatbot prompt swelled past 1,500 tokens after one iteration; the continuation on the next page reports that splitting it into smaller subtask prompts improved performance and lowered token costs. INTERPRETATION: decompose when a prompt becomes bloated or hard to debug, and tune step size by experiment.

## Relations
Follows providing context (C05-008); the next practice, giving the model time to think (C05-010), shares the latency concern. Chained steps anticipate agent workflows (C06-008). Iterating on prompts is C05-011.
