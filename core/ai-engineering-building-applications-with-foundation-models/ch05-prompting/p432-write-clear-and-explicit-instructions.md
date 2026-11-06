---
id: C05-007
title: Write Clear and Explicit Instructions
source_pages: "432-439"
chapter: 5
concepts: [clear-instructions, persona-prompting, few-shot-examples, output-format, token-cost-of-examples, end-of-prompt-markers, structured-output, prompt-preambles]
related: [C05-003, C05-004, C05-006, C05-008, C05-009, C05-010, C05-011]
time_sensitive: false
---
# Write Clear and Explicit Instructions
(Source: PDF pp. 432-439; the opening lines of PDF p. 432 are the lead-in of the best-practices section, which belongs to C05-006, and the section's heading begins part-way down that page)

## What the section covers
The first of the book's general prompt engineering best practices: be unambiguous about what the model should do. It walks through four tips: state the task without ambiguity, ask the model to adopt a persona, provide examples, and specify the output format. The lead-in (owned by C05-006) says these practices are techniques that work across many models, distilled from provider tutorials (OpenAI, Anthropic, Meta, Google) and from teams that shipped generative AI applications, and that each model also has quirks, so a model-specific prompting guide should be consulted (PDF p. 432).

## Why it matters
Communicating with an AI is, in the book's view, like communicating with people: clarity helps (PDF p. 432). Vague instructions leave the model to guess at scoring scales, tone, format or boundaries, and the undesirable behaviors you observe while experimenting can usually be fixed by making the prompt more explicit. Output format also matters operationally: long outputs cost money and add latency, and downstream software may need strictly structured output (PDF p. 438).

## How it works

### Explain, without ambiguity, what you want
- Example: to have a model score an essay, say which scale to use (1 to 5 or 1 to 10) and say what to do when the model is unsure of a score, either give its best-effort score or answer "I don't know" (PDF p. 432).
- Prompt refinement is reactive: if the model returns fractional scores such as 4.5 and you do not want them, add an instruction to output integers only (PDF pp. 432-433).

### Ask the model to adopt a persona
- A persona tells the model whose perspective to use when answering (PDF p. 433).
- Worked example (Figure 5-5): the essay "I like chickens. Chickens are fluffy and they give tasty eggs." is scored with a prompt asking for a 1-to-5 score, concise, score only. With no persona the model returns 2. With the single added sentence "You're a first-grade teacher." at the front of the same prompt, the model returns 4. The figure highlights that sentence as the "persona request" (PDF p. 433).

### Provide examples
- Examples cut down ambiguity about how to respond (PDF p. 434).
- Scenario: a bot for young children asked "Will Santa bring me presents on Christmas?" may answer that Santa is fictional and cannot bring presents, which would put users off. Supplying an example of how to handle a fictional character, such as treating the tooth fairy as real, steers it (PDF p. 434).
- Table 5-1 (inspired by Claude's tutorial) shows both runs. Without an example, the model gives an informative reply that Santa is a fictional figure kids believe in, and that many parents encourage the belief. With an example prompt containing "Q: Is the tooth fairy real? A: Of course! Put your tooth under your pillow tonight. The tooth fairy might visit and leave you something." followed by the Santa question, the model replies enthusiastically that Santa loves to bring presents to kids who believe and have been kind, suggests being extra good and leaving out cookies, and mentions waking to gifts under the tree (PDF pp. 435-436).
- Token cost of examples: if input length is a concern, choose an example format that uses fewer tokens, provided performance is equal (PDF p. 436). Table 5-2 compares two prompts for labeling items edible or inedible. The verbose one uses "Input: chickpea / Output: edible" lines and counts 38 tokens (GPT-4). The compact one uses "chickpea --> edible" lines and counts 27 tokens. The compact format should be preferred if accuracy is the same (PDF p. 437).

### Specify the output format
- Ask for concision if you want it. Long outputs are costly because APIs charge per token, and they raise latency. If the model habitually opens with a preamble like "Based on the content of this essay, I'd give it a score of...", say explicitly that you do not want preambles (PDF p. 438).
- When downstream applications consume the output, the format must be correct. For JSON, name the keys you expect and give examples if needed (PDF p. 438).
- For structured tasks such as classification, put a marker at the end of the prompt that signals where the structured output should begin. Without one, the model may just keep extending the input. Choose markers unlikely to occur in your inputs, or the model may be confused (PDF p. 438).
- Table 5-3 shows this failure: with the edible/inedible examples ending at "chicken", the model continues the input line with extra text ("tacos --> edible") instead of labeling it, which the table marks as wrong. With the item written as "chicken -->" and the arrow acting as the marker, the model answers "edible", marked as right (PDF p. 439).

## When and how to apply
INTERPRETATION: practical reading of the tips above.
- Spell out scales, tie-breaking behavior, forbidden behaviors and output shape; after each test run, add the instruction that removes any unwanted behavior you saw.
- Add a persona when the right judging perspective matters (for example the level at which an essay is graded).
- Use examples for tone and edge cases, and pick the cheapest format that performs equally.
- Use end markers and named JSON keys when software parses the result.

## Limitations and trade-offs
- Examples add input tokens, so they trade cost and latency for clearer behavior (PDF pp. 436-437).
- Persona and example effects shown are single illustrations ("might give" a 2 or a 4), not guaranteed outcomes (PDF p. 433).
- Markers that appear in real inputs can confuse the model (PDF p. 438).

## Relations
Builds on in-context learning and system/user prompts (C05-003, C05-004). Next practices: provide context (C05-008), decompose tasks (C05-009), give the model time to think (C05-010), iterate (C05-011). The section lead-in is C05-006.
