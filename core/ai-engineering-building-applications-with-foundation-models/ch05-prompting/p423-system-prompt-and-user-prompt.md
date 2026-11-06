---
id: C05-004
title: System Prompt and User Prompt
source_pages: "423-427"
chapter: 5
concepts: [system-prompt, user-prompt, chat-template, prompt-template, llama-chat-template, silent-failure, instruction-hierarchy, roleplay]
related: [C05-003, C05-005, C05-002]
time_sensitive: true
---
# System Prompt and User Prompt
(Source: PDF pp. 423-427; coverage begins at the heading part-way down PDF p. 423. The explanation of why system prompts help is cut at the page boundary and finishes at the top of the next page, described here without a cite and owned by the next row's first page.)

## What the section covers
How many APIs split a prompt into a system prompt and a user prompt, a worked real-estate example, how the two are merged by a chat template (Llama 2 and Llama 3 examples), the dangers of template mismatch, and why system prompts may improve performance.

## Meaning
- Many model APIs let you split a prompt into a system prompt (think: task description) and a user prompt (think: the task) (PDF p. 423).
- Example: a chatbot helping buyers understand property disclosures. The user uploads a disclosure and asks things like "How old is the roof?" or "What is unusual about this property?". The roleplay instruction (act like a real estate agent) goes into the system prompt; the question and the uploaded disclosure go into the user prompt (PDF p. 423).

## How it works
- The example system prompt (PDF p. 424) tells the model it is an experienced real estate agent who reads each disclosure carefully, fairly assesses the property's condition, helps the buyer understand risks and opportunities, and answers each question succinctly and professionally. The user prompt has a "Context:" slot holding the disclosure file, a "Question:" such as summarizing any noise complaints, and an "Answer:" cue.
- Almost all generative AI applications, ChatGPT included, have system prompts. Usually developer instructions go in the system prompt and user instructions in the user prompt, but you can move instructions around, even put everything in one of them, and should experiment with which structure works best (PDF p. 424).
- The model combines system and user prompt into a single prompt, usually following a chat template. The Llama 2 chat template wraps the system prompt between <<SYS>> markers inside an [INST] block, then adds the user message. With system prompt "Translate the text below into French" and user prompt "How are you?", the final input is that template filled in (PDF p. 425).
- Llama 3 uses a different template: begin-of-text, then header markers for system, user and assistant roles, each message ended by an end-of-turn token. Each span between <| and |> is a single token (PDF p. 426).

## Chat template versus prompt template
A warning on PDF p. 426: a model's chat template is defined by its developers and usually documented with the model. A prompt template is something any application developer defines to populate (hydrate) prompts with data. They are different things.

## Limitations and failure modes
- Different models use different chat templates, and one provider may change it between versions, as Meta did from Llama 2 to Llama 3 (PDF p. 426).
- Using the wrong template can cause bewildering performance problems, and small slips like an extra newline can significantly change behavior (PDF p. 426).
- Template errors are very common and hard to spot, because they fail silently: the model still does something reasonable (PDF p. 427).

## When and how to apply (the book's tips, PDF p. 427)
1. Follow the model's chat template exactly when building inputs.
2. If a third-party tool builds your prompts, verify it uses the right template.
3. Print the final prompt before sending to confirm it matches the expected template.

## Why system prompts may help
Providers stress that crafted system prompts improve performance; the book quotes Anthropic's documentation saying a role assigned in the system prompt lets Claude keep the character more effectively through the conversation (PDF p. 427). Yet under the hood the two prompts are concatenated into one, so to the model they are processed alike. Any boost is likely due to one or both of two factors (PDF p. 427). They are given on the following page: the system prompt comes first and models may handle earlier instructions better, and the model may have been post-trained to attend more to the system prompt (the OpenAI instruction-hierarchy paper by Wallace et al., 2024), which also helps against prompt attacks covered later in the chapter.

## Time-sensitive statements
The Llama 2 and Llama 3 template formats and the Anthropic quotation reflect versions at the time of writing.

## Relations
Follows in-context learning (C05-003); context length is the next subsection (C05-005).
