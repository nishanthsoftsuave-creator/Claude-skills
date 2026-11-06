---
id: C08-001
title: Dataset Engineering (Chapter Introduction)
source_pages: "694-696"
chapter: 8
concepts: [dataset-engineering, data-centric-ai, model-centric-ai, data-curation, post-training-data, data-competitions]
related: [C08-002, C08-003, C08-004]
time_sensitive: false
---
# Dataset Engineering (Chapter Introduction)
(Source: PDF pp. 694-696; the sidebar on data-centric AI continues onto PDF p. 697, whose lines above the "Data Curation" heading are covered here and the rest belongs to C08-002)

## What the section covers
The framing of Chapter 8: why data is the lever that decides model quality, how data work has become a professional function, what the chapter will walk through, and a sidebar contrasting model-centric and data-centric views of AI.

## Meaning
- Dataset engineering is the work of building a dataset that lets you train the best possible model, ideally inside your budget (PDF p. 694).
- Model-centric AI tries to raise performance by improving the model: new architectures, bigger models, new training techniques. Data-centric AI tries to raise performance by improving the data: new data processing methods and high-quality datasets that let better models be trained with fewer resources (PDF p. 696).

## Why it matters
- Model quality depends on training data quality. Even the best ML team with unlimited compute cannot finetune a good model without data (PDF p. 694).
- Fewer companies can afford to build models from scratch, so more of them differentiate their AI through data (PDF p. 694).
- As models need more data, handling it gets harder and demands more talent and infrastructure. Data operations have moved from side tasks done when time allows to dedicated roles: data labelers, dataset creators and data quality engineers, either inside or next to the core engineering teams (PDF p. 694).
- The data landscape is described as even more bewildering than the model landscape, with a growing array of datasets and techniques (PDF p. 694).

## How the chapter is organised
- It starts with data curation: what data you need, how much, and what "high quality" means. It then moves to data synthesis and data processing (PDF p. 695).
- Curation, generation and processing are not a straight line; expect to go back and forth between the steps (PDF p. 695).
- Different training phases teach different capabilities and so need datasets with different attributes. Pre-training data volume is usually counted in tokens, supervised finetuning volume in examples. At a high level, though, the curation principles are the same (PDF p. 695).
- The chapter concentrates on post-training data because that is what application developers mostly deal with, and it brings in pre-training lessons when they illuminate post-training (PDF p. 695).
- The author warns that although best practices and automation tools exist, data work is mostly "toil, tears, and sweat" (PDF p. 695).

## A data-centric view of AI (sidebar)
- Early deep learning benchmarks were mostly model-centric: given a fixed dataset such as ImageNet, people trained the best model they could. Recent benchmarks are more often data-centric: given a fixed model, people build the dataset that gives it the best performance (PDF p. 696).
- In 2021 Andrew Ng launched a data-centric AI competition. Participants improved a common base dataset with techniques such as fixing wrong labels, adding edge-case examples and augmenting data (PDF p. 696).
- In 2023, DataComp hosted a competition to build the best dataset for training a CLIP model. A standard script trains a CLIP model on each submission, and dataset quality is judged by the resulting model's results on 38 downstream tasks. A 2024 edition did the same for language models at scales from 412M to 7B parameters. Similar data-centric benchmarks named are DataPerf and dcbench (PDF p. 697).
- The model-centric versus data-centric split is a guide for research, not a real dichotomy: meaningful progress often needs investment in both models and data (PDF p. 697).

## Relations
The first section after this introduction is data curation (lead-in in C08-002), whose three criteria are data quality (C08-003), data coverage (C08-004) and data quantity (later rows of the chapter).
