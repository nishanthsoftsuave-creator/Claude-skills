---
id: C10-005
title: Step 3. Add Model Router and Gateway
source_pages: "863-870"
chapter: 10
concepts: [model-router, intent-classifier, next-action-predictor, model-gateway, access-control, fallback-policy, cost-management, unified-interface, load-balancing]
related: [C10-004, C10-006, C10-007, C10-008, C09-001]
time_sensitive: true
---
# Step 3. Add Model Router and Gateway
(Source: PDF pp. 863-870)

## What the section covers
The third architecture step. As an application comes to use more than one model, two components help manage the complexity and cost: a router that decides which solution handles each query, and a gateway that gives the organization one unified, secure interface to all models. The top of PDF p. 863 holds Figure 10-4 (guardrails architecture), which belongs to the previous step.

## Figure 10-4 (PDF p. 863)
Application architecture with guardrails added. Left to right: the user's query enters "Context construction" (RAG, agent, query rewriting), which draws on "Read-only actions" (vector search, SQL queries, web search) and "Databases" (documents, tables, chat history, vector DB). Its output passes through "Input guardrails" (example: PII redaction) into "Model API", which has inner boxes "Generation" and "Scoring". The model output goes through "Output guardrails" (safety/verification, structured outputs) and back to the user as the response. The newly added boxes (input guardrails, scoring, output guardrails) are outlined in orange.

## Router

### Purpose
- Rather than one model for every query, use different solutions for different query types (PDF p. 863).
- Benefit 1: specialized models can outperform a general model on specific queries. Example: one model specialized for technical troubleshooting, another for billing (PDF p. 863).
- Benefit 2: cost savings. Send simpler queries to cheaper models instead of using one expensive model for everything (PDF p. 863).

### Intent classifier
- A router typically includes an intent classifier that predicts what the user is trying to do; the query is then sent to the matching solution (PDF p. 864).
- Customer support chatbot example (PDF p. 864): a password-reset request goes to the FAQ page on password recovery; a request to correct a billing mistake goes to a human operator; a technical troubleshooting request goes to a chatbot specialized in troubleshooting.
- Out-of-scope conversations: if the classifier judges a query inappropriate, the chatbot can politely decline with a stock response, without spending an API call. Example given: asked who you would vote for in the upcoming election, the bot answers that as a chatbot it cannot vote, and offers help with products (PDF p. 864).
- Ambiguity: the classifier can detect an ambiguous query and ask for clarification. For the one-word query "Freezing", the system might ask whether the user wants to freeze an account or is talking about the weather, or just ask the user to elaborate (PDF p. 864).

### Other routers
- Next-action predictor: for an agent with several possible actions, a router can predict what to do next, such as using a code interpreter or a search API (PDF pp. 864-865).
- Memory routing: for a model with a memory system, a router can predict which part of the memory hierarchy to read from. Example: a user attaches a document mentioning Melbourne, then asks "What's the cutest animal in Melbourne?". The model must decide whether to rely on the attached document or search the internet (PDF p. 865).

### Implementation
- Intent classifiers and next-action predictors can be built on foundation models. Many teams adapt smaller language models such as GPT-2, BERT and Llama 7B as classifiers, and many train even smaller classifiers from scratch (PDF p. 865).
- Routers must be fast and cheap, so that several can be used without adding much latency or cost (PDF p. 865).
- Context limits: when routing among models with different context limits, the query's context may need adjusting. Example: a 1,000-token query is meant for a model with a 4K context limit, then an action such as web search returns 8,000 tokens of context. Either truncate the context to fit the original model, or route the query to a model with a larger context limit (PDF p. 865).

### Placement in the architecture (Figure 10-5)
- Since routing is usually done by models, the book puts routing inside the Model API box, like scorers; routers are typically smaller than generation models (PDF p. 865).
- Grouping routers with other models eases management, but routing often happens before retrieval. Before retrieval, a router can decide whether a query is in scope and whether it needs retrieval. Routing can also follow retrieval, for instance to decide whether to send the query to a human. Still, the pattern "routing, retrieval, generation, scoring" is much more common (PDF p. 866).
- Figure 10-5 repeats the Figure 10-4 layout with the Model API box expanded to three inner boxes: Routing, Generation and Scoring, with the whole Model API box outlined in orange and the Routing box outlined in orange as the new element. Caption: routing helps the system use the optimal solution for each query (PDF p. 866).

## Gateway

### Purpose and unified interface
- A model gateway is an intermediate layer through which an organization interfaces with different models in a unified and secure way (PDF pp. 866-867).
- Most basic function: a unified interface to different models, both self-hosted and behind commercial APIs. This simplifies code maintenance: if a model API changes, only the gateway needs updating, not every application that uses the API (PDF p. 867).
- Figure 10-6: on the left a stack of applications (customer support chatbot, product review summarization, text-to-SQL, and "..."), all feeding into a single box "Model gateway" labelled "Unified API"; on the right the gateway fans out to dashed-outline model providers (self-hosted models, OpenAI APIs, Google APIs, and "...") (PDF p. 867).

### The wrapper code example
- The book gives code showing a gateway in its simplest form, a unified wrapper, and says it is illustrative only: no error checking and no optimization (PDF p. 867).
- What the code does (PDF pp. 867-869): it imports the Google generative AI and OpenAI libraries; defines one function per provider (openai_model and gemini_model) that reads the API key from an environment variable and calls that provider with the input, model name and max tokens, returning a dictionary with the response; and defines a POST route '/model' (a Flask-style handler named model_gateway) that reads model_type, model_name, input_data and max_tokens from the JSON request and calls the OpenAI function if the type is "openai" or the Gemini function if "gemini", then returns the result as JSON.
- Legible in the render: the OpenAI function sets the key from the OPENAI_API_KEY environment variable and calls openai.Completion.create with engine, prompt and max_tokens arguments; the Gemini function configures genai with a Google API key, builds a GenerativeModel and calls generate_content; the handler ends with a return of jsonify(result) (PDF pp. 868-869).
- UNVERIFIED: several lines of the printed code are cut off at the right edge in the PDF (for example parameter lists and the Gemini return line), and the final lines of the handler continue onto p. 869; only the legible parts are described.

### Access control and cost management
- Instead of handing everyone the organization's OpenAI API tokens, which are easily leaked, give people access only to the gateway, creating a single controlled access point (PDF p. 869).
- The gateway can enforce fine-grained rules about which user or application may use which model, and can monitor and cap API usage to prevent abuse and control cost (PDF p. 869).

### Fallback policies
- The gateway can implement fallbacks to get around rate limits or API failures (which the book notes are unfortunately common). If the primary API is unavailable, it can route to alternative models, retry after a short wait, or handle the failure gracefully in other ways, so the application keeps running (PDF p. 869).

### Other functions
- Because every request and response passes through it, the gateway is a natural place for load balancing, logging and analytics. Some gateways also provide caching and guardrails (PDF p. 869).
- Gateways are fairly easy to build, so many off-the-shelf ones exist. Named examples: Portkey's AI Gateway, MLflow AI Gateway, Wealthsimple's LLM Gateway, TrueFoundry, Kong and Cloudflare (PDF p. 870).

### Resulting architecture (Figure 10-7)
The gateway replaces the plain Model API box. In Figure 10-7 the right-hand orange-outlined box is titled "Model gateway" with the subtitle "Model catalog, access token management, ...", containing three boxes: Routing, Generation and Scoring. The rest is as in Figure 10-4: context construction with read-only actions and databases, input guardrails, output guardrails, response to the user (PDF p. 870).

NOTE from the book: a similar abstraction, a tool gateway, could help reach many tools, but is not covered since it was not a common pattern at the time of writing (PDF p. 870).

## Trade-offs and limitations
INTERPRETATION: Routers add a classification step and its failure risk, so keep them small and fast, as the book advises; a gateway adds a single point through which all traffic flows, in exchange for central control, easier maintenance and fallback.

## Time-sensitive statements
The named models (GPT-2, BERT, Llama 7B), the vendor library calls in the code example, and the list of off-the-shelf gateways (PDF pp. 865, 867, 870) reflect the time of writing.

## Relations
Follows guardrails (C10-004), whose box layout it extends. Next steps are caching (C10-006) and agent patterns (C10-007); monitoring is C10-008. Self-hosted model serving is in the inference chapter (C09-001).
