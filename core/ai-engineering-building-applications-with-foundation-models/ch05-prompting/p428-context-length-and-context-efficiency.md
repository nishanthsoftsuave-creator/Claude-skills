---
id: C05-005
title: Context Length and Context Efficiency
source_pages: "428-430"
chapter: 5
concepts: [context-length, context-efficiency, needle-in-a-haystack, lost-in-the-middle, ruler, long-context-evaluation, prompt-position]
related: [C05-004, C05-006, C05-003]
time_sensitive: true
---
# Context Length and Context Efficiency
(Source: PDF pp. 428-430, with the closing paragraphs on PDF p. 431 above the heading "Prompt Engineering Best Practices"; PDF p. 428 begins with the end of the system-prompt discussion, which is owned by C05-004, and the heading starts part-way down.)

## What the section covers
How much a prompt can hold, how fast context limits have grown, how well models use different positions in the prompt, and how to test that with needle-in-a-haystack style tests.

## Meaning
How much information fits in a prompt is bounded by the model's context length limit (PDF p. 428).

## How it works
### Growth of context length
- The first three GPT generations had 1K, 2K and 4K context, barely enough for a college essay and too short for most legal documents or research papers (PDF p. 428).
- Context length became a race. In five years it grew 2,000-fold, from GPT-2's 1K to Gemini-1.5 Pro's 2M (PDF p. 428).
- Scale references: 100K fits a moderate-sized book; this book is about 120,000 words or 160,000 tokens; 2M fits roughly 2,000 Wikipedia pages and a reasonably complex codebase like PyTorch (PDF p. 428).
- Figure 5-2 (PDF p. 429, read from the render) plots context length on a log scale from 02/2019 to 05/2024: GPT-2 (1K, 02/2019), GPT-3 (2K, 06/2020), GPT-3.5 (4K, 11/2022), Claude-1 (9K, 03/2023), GPT-4 (32K, 03/2023), Claude-1 (100K, 05/2023), GPT-4 (128K, 11/2023), Claude-3 (200K, 03/2024), Gemini-1.5 Pro (1M, 02/2024), Gemini-1.5 Pro (2M, 05/2024). The trend is steeply upward on the log axis (the x-axis places the ten points at even spacing in the order listed, so it is not a true time scale).

### Not all positions are equal
- A model understands instructions at the beginning and end of a prompt much better than in the middle (Liu et al., 2023) (PDF p. 429).
- The needle in a haystack (NIAH) test inserts a random piece of information (the needle) at different places in a prompt (the haystack) and asks the model to retrieve it (PDF p. 429).
- Figure 5-3 (PDF p. 430) shows the Liu et al. setup: a JSON object of random key-value string pairs, an instruction to extract the value for a specified key, and the desired output being that key's value.
- Figure 5-4 (PDF p. 430) shows accuracy against the position of the document holding the answer, in three panels: 10 documents (about 2K tokens), 20 (about 4K) and 30 (about 6K). Models shown: claude-1.3, claude-1.3-100k, gpt-3.5-turbo-0613, gpt-3.5-turbo-16k-0613, mpt-30b-instruct, longchat-13b-16k. All models do better when the answer is near the start or end of the context than in the middle; most curves are U-shaped or fall steeply from the first position, with a smaller rise at the last position. ESTIMATES read from a 300-dpi render (axis 50-75, points only approximate; several series overlap so claude-1.3 vs gpt-3.5-turbo-0613 and claude-1.3-100k vs gpt-3.5-turbo-16k cannot always be told apart): 10 documents, positions 1st/5th/10th: top pair of overlapping lines about 77, 61, 62.5; longchat-13b-16k about 72, 59, 58.5; the Claude-coloured pair about 63, 58.5, 60; mpt-30b-instruct about 60, 56, 60. 20 documents, positions 1st/5th/10th/15th/20th: top lines about 76, 57, 54, 55.5, 63; others about 60, 56, 57, 57, 60; longchat about 68.5, 57.5, 55.5, 52.5, 55; mpt about 54, 52, 52, 52.5, 56. 30 documents, positions 1st/5th/10th/15th/20th/25th/30th: gpt-3.5-turbo-16k about 73.5, 55, 50.5, 51, 52, 55, 63.5; longchat about 67, 55, 52.5, 53, 52, 51.5, 55; the Claude pair about 59, 55, 55, 56, 56.5, 56, 60; mpt about 51.5, 51.5, 51, 49, 49.5, 51.5, 54. Overall accuracy spans about 49 to 77 percent; the best first-position results are highest for the strongest models, and accuracy in the middle positions is often near the low 50s.

## When and how to apply
- The paper used random strings, but you can test with real questions and answers, for instance asking for the drug or blood type mentioned somewhere in a long doctor-visit transcript (PDF pp. 430-431).
- Use test information that is private, so it cannot have been in training data; otherwise the model could answer from internal knowledge instead of the context (PDF p. 431).
- Similar tests such as RULER (Hsieh et al., 2024) also gauge long-prompt handling (PDF p. 431).

## Evaluation and success criteria
If performance worsens steadily as context grows, the book suggests finding ways to shorten prompts (PDF p. 431).

## Relations
Follows system/user prompts (C05-004). The key prompt components are system prompt, user prompt, examples and context; best practices follow in C05-006. Few-shot examples consume context (C05-003).

## Time-sensitive statements
The context-length numbers and model names (GPT, Claude, Gemini versions) date to May 2024 in the book.
