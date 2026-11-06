---
id: C01-020
title: Three Layers of the AI Stack
source_pages: "93-96"
chapter: 1
concepts: [ai-stack, application-development, model-development, infrastructure, github-repositories, enduring-principles, experimentation, feedback-loop]
related: [C01-019, C01-021, C01-018]
time_sensitive: true
---
# Three Layers of the AI Stack
(Source: PDF pp. 93-96; concluding paragraph on PDF p. 97)

## What the section covers
The three layers of an AI application stack (application development, model development, infrastructure), a GitHub-based analysis of how the ecosystem grew after foundation models, and the argument that many classic ML engineering principles still hold.

## Figure 1-13: separate AI engineering job descriptions
Printed at the top of PDF p. 93 (rendered and read); the text introducing it is on the previous page. Caption: some companies have separate job descriptions for AI engineering, shown as LinkedIn job headlines from December 17, 2023. It shows ten headlines whose titles use AI engineering terms rather than ML: Principal AI Engineer (Figure); Senior Generative-AI Software Engineer (NVIDIA); AI Engineer (Notion); Generative AI Engineer (Storm6); Generative AI Engineer, Senior (Booz Allen Hamilton); Senior AI Research Engineer, Recommendation (Duolingo); AI Engineer (WilmerHale); AI Engineer (Motion Recruitment); Lead Artificial Intelligence (AI) Engineer (St. Jude Children's Research Hospital); and Generative AI Engineer (Western Asset Management). (PDF p. 93)

## Meaning: the three layers
Any AI application stack has three layers. When building an application you likely start at the top and move down as needed (PDF p. 93).
- **Application development.** With models readily available, anyone can build applications on them. This layer has seen the most action in the last two years and is still evolving quickly. It means giving a model good prompts and necessary context, needs rigorous evaluation, and good applications also demand good interfaces (PDF pp. 93-94).
- **Model development.** Tooling for developing models: frameworks for modeling, training, finetuning and inference optimization. Since data is central, dataset engineering sits here too. It also requires rigorous evaluation (PDF p. 94).
- **Infrastructure.** The bottom layer: tooling for model serving, managing data and compute, and monitoring (PDF p. 94).

Figure 1-14 (PDF p. 95, rendered) draws the layers as three stacked blocks (application development on top, model development in the middle, infrastructure at the bottom), each with example responsibilities listed beside it (evaluation appears in both of the top two): Application development has AI interface, prompt engineering, context construction, evaluation; Model development has inference optimization, dataset engineering, modeling and training, evaluation; Infrastructure has compute management, data management, serving, monitoring.

## GitHub analysis of ecosystem growth
- In March 2024 the author searched GitHub for AI-related repositories with at least 500 stars, treating this as a proxy for the ecosystem. Repositories for applications and models (products of the top two layers) were included. The total was 920 repositories (PDF p. 95).
- Figure 1-15 (PDF p. 96, rendered) plots cumulative repository counts by category (applications, AI engineering, model repo, model development, infrastructure) over time, with milestones annotated: tensorflow (2015-11), Transformers paper (2017-06), hf/transformers (2018-10), GPT-3 (2020-06), Stable Diffusion (2022-08), ChatGPT (2022-11). It is a stacked area chart. Growth is slow and steady from 2015 to 2022 (roughly 250-300 cumulative repositories by the ChatGPT marker) and then rises steeply through 2023. ESTIMATE from the chart: the stacked total reaches roughly 840-850 at the right edge, whereas the text says 920 repositories; the two differ, the book does not explain the gap, and the five legend categories are all stacked in the chart so they do not account for it. Approximate band sizes at the end: infrastructure about 65 (the thinnest), model development about 215, model repo about 180, AI engineering about 195, applications about 190 (estimates only; no per-category values are printed). The legend names the category "AI engineering", not "application development"; the text says application development grew most, and the chart legend's correspondence is not stated.
- Findings: a big jump in AI tooling in 2023 after Stable Diffusion and ChatGPT. Applications and application development grew most. Infrastructure grew, but far less. This is expected because core infrastructure needs (resource management, serving, monitoring) stay the same even as models and applications change (PDF p. 96).

## Many principles remain the same
- Despite unprecedented excitement, many principles of building AI applications are unchanged (PDF p. 96).
- Enterprise applications must still solve business problems, so mapping business metrics to ML metrics and back is still essential (PDF p. 96).
- Systematic experimentation is still needed. In classical ML you vary hyperparameters; with foundation models you vary models, prompts, retrieval algorithms, sampling variables and more (sampling variables are covered in Chapter 2) (PDF pp. 96-97).
- Making models faster and cheaper still matters, and a feedback loop from production data for iterative improvement is still important (PDF p. 97).
- So much of what ML engineers learned over the last decade still applies, easing entry, while on top of these enduring principles sit innovations unique to AI engineering (PDF p. 97).

## When and how to apply
INTERPRETATION: treat the layers as a way to locate a problem (interface and prompts, model or data, or serving and monitoring) and to see which existing ML platform parts can be reused.

## Time-sensitive statements
The repository counts (920 as of March 2024) and the growth trend in Figure 1-15 are data from the date of writing.

## Relations
Follows the lead-in (C01-019); the next section compares AI and ML engineering (C01-021). Evaluation, mentioned in two layers, and the unchanged need for metrics echo planning in C01-018.
