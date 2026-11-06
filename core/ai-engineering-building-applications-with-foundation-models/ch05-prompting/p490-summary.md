---
id: C05-019
title: Chapter 5 Summary
source_pages: "490-493"
chapter: 5
concepts: [chapter-summary, prompt-engineering, prompt-attacks, human-ai-communication, in-context-learning, security-cat-and-mouse, chapter-footnotes]
related: [C05-016, C05-017, C05-018, C06-001]
time_sensitive: true
---
# Chapter 5 Summary
(Source: PDF pp. 490-493: the summary itself, then the chapter's endnotes. PDF p. 494 opens Chapter 6, which belongs to C06-001; its only relevance here is the hand-off described below.)

## What the section covers
The book's wrap-up of the Prompt Engineering chapter, followed by the chapter's 22 footnotes (small asides on controversy, templates, context length, testing, prompt writing, security incidents and extraction attacks).

## Summary content

### Prompt engineering in one view (PDF p. 490)
- Foundation models can do a great deal but must be told exactly what you want. Crafting an instruction that makes a model do it is **prompt engineering**.
- How much crafting is needed depends on prompt sensitivity: if a small change in the prompt shifts the response a lot, more care is required.
- It can be viewed as human-AI communication. Everyone can communicate, few communicate well. Getting started is easy, which misleads many people into assuming doing it well is easy.

### What the first part of the chapter covered (PDF p. 490)
The anatomy of a prompt, why in-context learning works, and best practices. The shared lesson with human communication: clear instructions, examples and relevant information are essential. Simple tricks, such as telling the model to slow down and think step by step, can bring surprising gains. AI models, like people, have quirks and biases that a productive working relationship must take into account.

### Prompt attacks (PDF pp. 490-491)
- Models are useful because they follow instructions, but that same ability exposes them to prompt attacks in which bad actors get them to follow malicious instructions. The chapter covered attack approaches and defenses.
- Security is an ever-evolving cat-and-mouse game, so no safeguard is foolproof, and the book concludes that security risk will remain a significant barrier to AI adoption in high-stakes settings (PDF p. 491).

### Hand-off (PDF p. 491)
Instructions alone are not enough; to do a task a model also needs relevant context. How to supply it is the topic of the next chapter (RAG and agents, C06-001).

## Chapter endnotes (PDF pp. 491-493)
- Prompt engineering has attracted a surprising amount of hostility: complaints that it is not a real discipline gather thousands of supporting comments, and people rolled their eyes when the author mentioned a chapter on it (PDF p. 491).
- In late 2023 Stanford dropped robustness from its HELM Lite benchmark (PDF p. 491).
- Departing from the expected chat template usually degrades performance, though on rare occasions it makes the model do better, as one Reddit discussion shows (PDF p. 491).
- Chat-template mismatch bugs are widely reported on GitHub and Reddit; the author once lost a day debugging a finetuning problem caused by a library that had not updated the chat template for a newer model version (PDF p. 491). To spare users such mistakes, many model APIs hide special template tokens (PDF p. 491).
- Google announced experiments with a 10M-token context in February 2024, but the figure was left out of the chapter's chart because it was not yet public (PDF p. 491).
- Shreya Shankar wrote up a practical needle-in-a-haystack test on doctor visits (2024) (PDF p. 492).
- A language model by itself does not separate user-provided input from its own generation, as covered in Chapter 2 (PDF p. 492).
- The parallel-processing example comes from Anthropic's prompt engineering guide (PDF p. 492).
- A model's skill at writing prompts is probably helped by having trained on prompts shared on the internet (PDF p. 492).
- Hamel Husain's blog post "Show Me the Prompt" (February 14, 2024) is credited with codifying this philosophy (the one the main text argues for; PDF p. 492).
- Brand-risk and misinformation outputs were touched on in Chapter 4 (PDF p. 492).
- A remote-code-execution risk was found in LangChain in 2023, tracked in two GitHub issues (PDF p. 492).
- Popular prompt lists exist (English and Chinese awesome-chatgpt-prompts repositories); the author does not know how long prompts for new models stay relevant (PDF p. 492).
- Whether proprietary prompts could be patented like a book is untested; without precedent it is hard to say (PDF p. 492).
- The author tested typo understanding and was surprised that both ChatGPT and Claude understood "el qeada" (PDF p. 492). An aside also declines to explain what UwU is, and another points to the xkcd comic "Exploits of a Mom" for SQL sanitizing (PDF p. 492).
- Asking a model to repeat text is one variant of repeated-token attacks; another is a prompt that repeats a text many times. Dropbox's blog post "Bye Bye Bye...: Evolution of repeated token attacks on ChatGPT models" (Breitenbach and Wood, 2024) covers it (PDF p. 493).
- In Nasr et al. (2023), instead of hand-writing trigger prompts, they started from a corpus (100 MB of Wikipedia) and randomly sampled prompts from it. Extraction counted as successful "if the model outputs text that contains a substring of length at least 50 tokens that is contained verbatim in the training set" (PDF p. 493).
- That larger models memorize more is likely because they are better at learning from data (PDF p. 493).
- Since many high-stakes use cases have not yet adopted the internet, it will be a long time before they adopt AI (PDF p. 493).

## Relations
Closes the chapter after the attack and defense sections (C05-016, C05-017, C05-018) and leads into context construction in C06-001.

## Time-sensitive statements
Endnote facts tied to dates: HELM Lite dropping robustness (late 2023), Google's 10M-token context experiments (February 2024), the LangChain remote-code-execution finding (2023), and the Dropbox and Nasr et al. references (2023-2024) (PDF pp. 491-493).
