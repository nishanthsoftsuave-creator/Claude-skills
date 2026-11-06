---
id: C10-004
title: Step 2. Put in Guardrails
source_pages: "856-862"
chapter: 10
concepts: [guardrails, input-guardrails, output-guardrails, pii-masking, sensitive-data-detection, retry-logic, human-fallback, streaming-guardrails, false-refusal-rate]
related: [C10-003, C10-005, C10-006, C10-008, C05-018]
time_sensitive: true
---
# Step 2. Put in Guardrails
(Source: PDF pp. 856-862. Figure 10-4, which the text on the last page refers to, is printed at the top of the next row's first page and is described in C10-005; a summary is given below without a page cite.)

## What the section covers
The second architecture step: protective checks placed around the model. Input guardrails (private data leaving the system, harmful prompts), output guardrails (catching bad outputs and deciding what to do about them), the trade-offs of implementing guardrails (latency, streaming, self-hosting versus third-party APIs), who provides them, and the resulting architecture. The top of PDF p. 856 holds Figure 10-2, the context-construction architecture left over from Step 1.

## Figure 10-2 (PDF p. 856)
The platform architecture with context construction. The user's query goes first to a box "Context construction" (examples listed in it: RAG, agent, query rewriting) instead of straight to the model. That box draws on two supporting elements: "Read-only actions" (examples: vector search, run SQL queries, web search) and "Databases" (examples: documents, tables, chat history, vector DB). The output of context construction goes to the "Model API" box (still containing only "Generation"), and the response returns to the user. The orange outlining highlights the newly added boxes.

## Meaning
- Guardrails reduce risk and protect you and your users. They should be placed wherever the system is exposed to risk, and fall broadly into guardrails around inputs and guardrails around outputs (PDF p. 856).

## Input guardrails
Input guardrails typically address two risks: private information leaking to external APIs, and bad prompts that compromise the system being executed. Chapter 5 covers how attackers exploit prompt hacks and how to defend against them. Risks can be reduced but never fully removed, because of how models generate responses and because of unavoidable human failures (PDF p. 856).

### Leaking private information to external APIs
- This risk is specific to using external model APIs, where data has to leave the organization (PDF p. 857).
- Ways it happens (PDF p. 857): an employee pastes a company secret or a user's private information into a prompt sent to a third party; a developer puts internal policies or data into the application's system prompt; a tool pulls private information from an internal database and adds it to the context.
- There is no airtight way to eliminate such leaks with third-party APIs, but guardrails mitigate them. Many tools automatically detect sensitive data, and you specify which classes to look for (PDF p. 857).
- Common sensitive classes (PDF p. 857): personal information such as ID numbers, phone numbers and bank accounts; human faces; and keywords or phrases tied to the company's intellectual property or privileged information.
- Many detectors are themselves AI-based, for example judging whether a string looks like a valid home address (PDF p. 857).
- When a query is found to contain sensitive data there are two options: block the whole query, or strip the sensitive part out of it (PDF pp. 857-858).

### Masking and unmasking (Figure 10-3)
- Example masking: replace a user's phone number with a placeholder such as [PHONE NUMBER]. If the generated response contains the placeholder, a PII reverse dictionary that maps placeholders back to the original values lets you unmask it before showing the user (PDF p. 858).
- Figure 10-3 shows four stacked text boxes (user query, masked query, model response, unmasked response) plus a "Reversible PII map" table. The user query is a coding question: "I got 403 error on this code. What did I do wrong?" followed by code that contains a personal access token string, in red. In the masked query the token is replaced by [ACCESS_TOKEN]. The reversible map has one entry: [ACCESS_TOKEN] corresponds to the original secret string. The model response tells the user that the URL has a syntax error (a query parameter introduced with & rather than ?) and gives corrected code that still contains [ACCESS_TOKEN]. The unmasked response puts the real token back via the map. The point: the external API never sees the secret, yet the user gets a complete answer (PDF p. 858).

## Output guardrails
Output guardrails have two main functions: catch output failures, and specify the policy for handling each failure mode (PDF pp. 858-859).

### Catching failures
- To catch failing outputs you must know what failure looks like for your application. The easiest failure to detect is an empty response when there should not be one (PDF p. 859).
- Quality failures (covered in Chapter 4) (PDF p. 859): malformatted responses that break the expected format (for instance invalid JSON when JSON is expected); factually inconsistent, hallucinated responses; generally bad responses (an essay that is simply poor).
- Security failures (covered in Chapter 5) (PDF p. 859): toxic responses (racist, sexual or illegal content); responses containing private or sensitive information; responses that trigger remote tool or code execution; and brand-risk responses that misrepresent your company or competitors.
- For security measurement, track not only security failures but also the false refusal rate. A system can be too secure, blocking legitimate requests, interrupting users' work and frustrating them (PDF p. 860).

### Handling failures: retries
- Models are probabilistic, so many failures go away if you simply try again: for an empty response, retry up to X times or until the response is non-empty; for a malformatted response, retry until it is correctly formatted (PDF p. 860).
- Cost of retrying: each retry is another round of API calls, and if the retry waits for a failure, the user-perceived latency doubles. To contain latency, send the same query to the model twice in parallel, get two responses and pick the better one. This adds redundant API calls (cost) but keeps latency manageable (PDF p. 860).

### Handling failures: human fallback
- Teams commonly hand tricky requests to humans. Some transfer queries containing specific phrases to human operators. Some use a specialized model to decide when to hand off (PDF p. 860).
- Two reported examples: one team transfers when its sentiment analysis model detects anger in the user's messages; another transfers after a set number of turns so users do not get stuck in a loop (PDF pp. 860-861).

## Guardrail implementation: trade-offs
- Reliability versus latency: some teams told the author that latency matters more and chose not to implement guardrails at all, since guardrails can increase latency significantly (PDF p. 861).
- Streaming: by default the whole response is generated before display, which can be slow. In stream completion mode, tokens are shown as they are generated, cutting the wait. The downside is that partial responses are hard to evaluate, so unsafe content may reach the user before the guardrail decides to block it (PDF p. 861).
- Self-hosting versus third-party APIs: guardrails can be built over either. Third-party providers typically supply many guardrails out of the box, reducing what you must build. Self-hosting avoids sending requests outside, which removes the need for many input guardrails (PDF p. 861).

## Who provides guardrails
- Model providers build guardrails into their models to make them better and more secure, but they must balance safety against flexibility: restrictions can make a model safer and less usable for particular use cases (PDF p. 862).
- Application developers can add their own; many techniques are in the "Defenses Against Prompt Attacks" section (C05-018) (PDF p. 862).
- Out-of-the-box solutions named (PDF p. 862): Meta's Purple Llama, NVIDIA's NeMo Guardrails, Azure's PyRIT, Azure's AI content filters, the Perspective API, and OpenAI's content moderation API. Because input and output risks overlap, a guardrail product usually protects both directions. Some model gateways also offer guardrails (see C10-005).

## Resulting architecture (Figure 10-4)
Figure 10-4 adds, to the Figure 10-2 layout, an "Input guardrails" box (example: PII redaction) placed between context construction and the Model API, and an "Output guardrails" box (listing safety/verification and structured outputs) on the return path between the Model API and the user. The Model API box now contains two inner boxes, Generation and Scoring. The author put scorers under model APIs because scorers are often AI-powered, even though they are typically smaller and faster than generative models; scorers could equally be placed inside the output guardrails box (PDF p. 862).

## When and how to apply
INTERPRETATION: Place a check wherever data crosses a trust boundary: before the prompt leaves for an external API (masking or blocking sensitive data) and after the response comes back (format, factuality, safety checks with retries or human handoff). Decide per application whether guardrail latency is acceptable, and whether streaming is worth the loss of full-response checks.

## Limitations and failure modes
Guardrails never eliminate risk entirely (PDF p. 856); retries add cost and latency (PDF p. 860); over-strict systems produce false refusals (PDF p. 860); streaming undermines output checks (PDF p. 861); provider guardrails trade safety against flexibility (PDF p. 862).

## Time-sensitive statements
The list of named guardrail products and providers (PDF p. 862) reflects the date of writing.

## Relations
Builds on the context-construction step (C10-003). Next component: model router and gateway (C10-005), which can also host guardrails. Prompt-attack defenses are in C05-018. Caching, which interacts with guardrails, is C10-006, and monitoring is C10-008.
