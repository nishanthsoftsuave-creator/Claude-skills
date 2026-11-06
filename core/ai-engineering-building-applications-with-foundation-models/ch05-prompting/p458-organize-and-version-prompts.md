---
id: C05-013
title: Organize and Version Prompts
source_pages: "458-461"
chapter: 5
concepts: [prompt-organization, prompt-versioning, prompt-catalog, prompt-metadata, dotprompt, separating-prompts-from-code]
related: [C05-012, C05-014, C05-011]
time_sensitive: false
---
# Organize and Version Prompts
(Source: PDF pp. 458-461; the section's closing sentences run onto PDF p. 462, above the "Defensive Prompt Engineering" heading. The first lines of PDF p. 458 belong to the preceding row on tool evaluation.)

## What the section covers
Good practice for storing, structuring, and versioning prompts: keep them apart from application code, attach metadata, consider dedicated prompt file formats, and choose between git versioning and a separate prompt catalog.

## Separate prompts from code
- The book recommends keeping prompts out of code, with reasons promised "in a moment" (PDF p. 458).
- Its example: define a constant such as GPT4o_ENTITY_EXTRACTION_PROMPT in a prompts.py file, then import it in application.py. A function (query_openai) calls the chat completions endpoint with a messages list whose system message is that imported prompt and whose user message is the incoming user prompt (PDF pp. 458-459). The code listings are clipped at the right edge in the PDF itself (the import line on PDF p. 458 ends at "...ENTITY_EXTRACTION_PROMP", and the system message's content on PDF p. 459 ends at "GPT4o_ENTIT"), so only their structure is recorded here; the remaining characters are UNVERIFIED but evidently the prompt constant's name.

### Advantages (PDF p. 459)
- Reusability: several applications can share one prompt.
- Testing: code and prompts can be tested independently. For example, the same code can be exercised with different prompts.
- Readability: both prompts and code are easier to read when split.
- Collaboration: subject matter experts can help write prompts without being distracted by code.

## Prompt metadata and organization
- When you hold many prompts across several applications, give each prompt metadata saying which prompt it is and which use case it serves, and arrange them so they can be searched by model, application, and so on (PDF p. 460).
- One way: wrap each prompt in a Python object, shown as a pydantic BaseModel with fields model_name, date_created, prompt_text, application, and creator (PDF p. 460).
- A prompt template may also record how the prompt is meant to be used (PDF p. 460):
  - the model endpoint URL
  - the ideal sampling parameters, such as temperature or top-p
  - the input schema
  - the expected output schema, for structured outputs

## Dedicated prompt file formats
- Several tools propose special .prompt formats: Google Firebase's Dotprompt, Humanloop, Continue Dev, and Promptfile (PDF p. 460).
- The Dotprompt example (PDF p. 461) has a header block between dashed lines that names the model (vertexai/gemini-1.5-flash), declares an input schema (a string field theme), and declares a JSON output schema (name as string, price as integer, ingredients as an array of strings). The body below the header is the prompt text, which begins "Generate a menu item that could be found at a {{t..." and is cut off in the book at the page edge (the visible text ends at "{{t"). UNVERIFIED: the rest of the line; INTERPRETATION: the variable is probably the declared theme input. The point is that model, input and output contracts, and prompt text live in one file.

## Versioning options and trade-offs
- Git: if prompt files sit in your git repository they can be versioned with git. The drawback is coupling. When several applications share a prompt and it is updated, all dependent applications are forced onto the new version, so a team can hardly choose to stay on an older one (PDF p. 461).
- Prompt catalog: many teams instead keep a separate catalog that explicitly versions each prompt so that different applications can use different versions. It should also hold relevant metadata for each prompt and support searching (PDF pp. 461-462).
- A well-built catalog may even track which applications depend on a prompt and notify their owners when a newer version appears (PDF p. 462).

## When and how to apply
INTERPRETATION: if only one application uses a prompt, git versioning alongside the code is enough; once prompts are shared across applications and teams need to upgrade independently, the book's described catalog with explicit versions and dependency tracking addresses the coupling problem.

## Relations
Builds on the advice to version prompts and track experiments (C05-011 and C05-012). The next section, defensive prompt engineering (C05-014), covers attacks on prompts.
