---
id: C08-004
title: Data Coverage
source_pages: "707-711"
chapter: 8
concepts: [data-coverage, data-diversity, data-mix, llama-3, annealing, scaling-law-experiments, quality-vs-diversity]
related: [C08-002, C08-003]
time_sensitive: true
---
# Data Coverage
(Source: PDF pp. 707-711; the paragraph introducing Figure 8-1 ends PDF p. 711, and the figure itself is printed on the next page, so it is described only briefly here)

## What the section covers
The second data-curation criterion: training data should span the range of problems and phrasings users bring. It covers diversity dimensions per application, examples from NVIDIA Nemotron and Llama 3, Llama 3's per-phase domain mix (Table 8-1), how to choose a data mix, and the Zhou et al. quality-versus-diversity experiment.

## Meaning
- Training data should cover the problems you expect the model to solve. Real users have varied problems and express them in very different ways, so data capturing the application's diverse usage patterns is key. Because coverage needs enough diversity, many call this attribute data diversity (PDF p. 707).
- Examples: if some users write detailed instructions with many references and others write short ones, finetuning data should contain both; if user queries contain typos, include typos; if the application handles several programming languages, include those users care about (PDF p. 707).

## How it works: diversity depends on the application
- A French-to-English translation tool needs no language diversity but may benefit from diversity in topic, length and speaking style. A product-recommendation chatbot for global customers may not need domain diversity but needs linguistic and cultural diversity (PDF p. 708).
- General-purpose chatbots need finetuning data covering wide topics and speaking patterns. Ding et al. (2023) argue the most direct way to improve chat models is to raise data quality and diversity (PDF p. 708).
- NVIDIA's Nemotron dataset aimed at task diversity, topic diversity and instruction diversity, including instructions for different output formats and lengths, and open-ended as well as yes-or-no answers (PDF p. 708).
- "The Data Addition Dilemma" (Shen et al.) showed that in some cases adding more heterogeneous data makes performance worse (PDF p. 708).
- Meta says Llama 3 barely departs from earlier Llama architectures, and its gains are "primarily driven by improvements in data quality and diversity as well as by increased training scale" (PDF p. 708).

## Llama 3 data mix across phases
- The Llama 3 paper details coverage in all three phases: pre-training, supervised finetuning and preference finetuning. Although this chapter is about post-training, comparing the phases highlights the considerations of each (PDF pp. 708-709).
- Domain diversity is a consistent axis across phases, though what "diverse" means differs. Table 8-1 shows only high-level domains, not finer topics such as geometry within math. Post-training data has further axes not in the table: token counts for context and response, number of turns, and, since Llama 3 uses synthetic post-training data, the ratio of human to AI-generated data (PDF p. 709).
- Table 8-1 (percent of each phase's data; X means the domain is not used in that phase) (PDF p. 710):
  - General knowledge (English): pre-training 50%, supervised finetuning 52.66%, preference finetuning 81.99%.
  - Math and reasoning: 25%, 21.19%, 5.89%.
  - Coding: 17%, 14.89%, 6.93%.
  - Multilingual: 8%, 3.01%, 5.19%.
  - Exam-like: X, 8.14%, X.
  - Long context: X, 0.11%, X.
- Observation: in pre-training and SFT, math, reasoning and code together make up nearly half of the data. The author believes the internet contains far less than 50% math and code. Llama 3's authors reported that annealing on small amounts of high-quality code and math data (training with an increasingly smaller learning rate while using more code and math) boosts key benchmark performance, supporting the belief that high-quality code and math data lifts reasoning more than natural-language text does (PDF pp. 710-711).
- In preference finetuning code and math drop to 12.82% combined, probably because the aim there is to mirror the real distribution of user preferences (PDF p. 711).

## When and how to apply: choosing a data mix
- Simple approach: choose a mix that accurately reflects real-world application usage (PDF p. 711).
- Experimental approach: Meta ran scaling-law experiments like those discussed in the earlier "Scaling extrapolation" section. For each candidate mix they trained several small models and used them to predict a large model's performance on that mix. The final mix is the best guess from those results (PDF p. 711).

## Evaluation: quality versus diversity experiment
Zhou et al. (2023) trained a 7B-parameter language model on three datasets of equal size (2,000 examples): one high-quality but not diverse, one diverse but low-quality, one both diverse and high-quality. The generation quality of the three models is compared in Figure 8-1, printed on the next page (PDF p. 711).

## Time-sensitive statements
The Llama 3 mix percentages and the claims about Llama 3's architecture reflect the model as published at the time of writing.

## Relations
Companion to data quality (C08-003); the lead-in's three criteria are in C08-002. Data quantity, the third criterion, follows in later rows.
