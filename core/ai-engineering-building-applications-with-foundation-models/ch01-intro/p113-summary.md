---
id: C01-023
title: Chapter 1 Summary and Notes
source_pages: "113-118"
chapter: 1
concepts: [chapter-summary, ai-engineering, self-supervision, foundation-models, build-or-not, ai-engineering-stack, footnotes]
related: [C01-020, C01-021, C01-022, C02-001]
time_sensitive: true
---
# Chapter 1 Summary and Notes
(Source: PDF pp. 113-118)

## What the section covers
The chapter's closing summary and the chapter's footnotes. The footnotes are collected on pages 115-118 and are covered below.

## The summary's purposes
- Two goals: explain the emergence of AI engineering as a discipline thanks to foundation models, and give an overview of the process of building applications on them. It is an overview chapter that touches many concepts lightly, to be developed later in the book (PDF pp. 113-114).

## What the chapter covered
- The rapid evolution of AI: from language models to large language models via self-supervision, then language models taking in other modalities to become foundation models, which gave rise to AI engineering (PDF p. 114).
- Growth driven by applications enabled by emerging foundation model capabilities, with successful patterns for consumers and enterprises. Despite many applications in production, it is still early, with many more innovations to come (PDF p. 114).
- An often overlooked question: should you build the application at all? The chapter discussed it with the major considerations for building (PDF p. 114).
- AI engineering evolved from ML engineering, the overarching discipline for building applications with any ML model. Many ML engineering principles still apply, but AI engineering brings new challenges and solutions; the last section covered the AI engineering stack and how it changed (PDF pp. 114-115).

## Framework and next steps
- The community's energy and output is hard to capture and impossible to keep up with. AI can help aggregate updates, but only to a degree; the more overwhelming a space, the more a framework is needed, and the book aims to supply one (PDF p. 115).
- The framework is explored step by step, beginning with the fundamental building block: the foundation models (PDF p. 115). That is the subject of the next chapter (C02-001).

## Footnotes of the chapter (pages 115-118)
Definitions and clarifications:
- "Traditional ML" means all ML before foundation models (PDF p. 115).
- For non-English languages a single Unicode character can be several tokens (PDF p. 115).
- Autoregressive language models are sometimes called causal language models; a masked model such as BERT can technically generate text with effort (PDF p. 116).
- Model parameters were once taught as weights plus biases, but today "weights" generally means all parameters (PDF p. 116).
- It seems odd that larger models need more training data, but the goal is to maximize performance, not match a small model on the same data (PDF p. 116).
- Pre-training and post-training are admittedly unimaginative names; the author also dislikes "large" as unscientific and "X is all you need" titles (PDF p. 118).

Figures and numbers (time-sensitive):
- Labeling cost varies with task complexity, scale and provider; as of September 2024 Amazon SageMaker Ground Truth charged 8 cents per image under 50,000 images and 2 cents per image above 1 million (PDF p. 116).
- US public school spending is about $900 billion, only nine times US AI investment (PDF p. 116).
- As of 16 September 2024, theresanaiforthat.com listed 16,814 AIs for 14,688 tasks and 4,803 jobs; the author tracks an open source AI application list updated every 12 hours (PDF p. 116).
- On average 11% of a company's budget goes to marketing (WSJ, 2017), so automating it can save a lot (PDF p. 117).

Observations and asides:
- Knowing when to stop generating matters, as it does for people talking (PDF p. 116).
- AI helped the author write (e.g., brainstorming fiction); what writing can be automated remains under evaluation. The author hypothesizes people will trust only content from people or brands they trust (PDF p. 117).
- Apple and Amazon have been slow to bring generative AI to Siri and Alexa; a friend suggests higher quality and compliance bars and harder voice interfaces (PDF p. 117).
- The author finds AI very helpful for searching 40,000+ photos in Google Photos (otherwise near impossible) and for explaining confusing graphs; small startups may not afford someone to "look around"; an early joke called AI startups OpenAI or Claude wrappers; "data flywheel" was heard constantly (PDF p. 117).
- A Fortune 500 AI head said his team can work with 10 GPUs but not 1,000, and such engineers get incredible compensation (PDF p. 118).
- Streamlit, Gradio and Plotly Dash are common tools for AI web apps (PDF p. 118).
- Anton Bacaj: "AI engineering is just software engineering with AI models thrown in the stack" (PDF p. 118).
- Disclosures: the author advises Convai and invests in Photoroom (PDF pp. 117-118).

## Relations
Wraps up C01-019 to C01-022; leads into chapter 2 (C02-001).

## Time-sensitive statements
Prices, counts and dates in the footnotes (2017, September 2024) are as of writing (PDF pp. 116-117).
