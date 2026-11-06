---
id: C08-006
title: Data Acquisition and Annotation
source_pages: "721-725"
chapter: 8
concepts: [data-acquisition, data-flywheel, application-data, public-datasets, dataset-licensing, annotation-guidelines, data-curation-workflow, instruction-templates]
related: [C08-005, C08-007, C08-008, C04-012]
time_sensitive: true
---
# Data Acquisition and Annotation
(Source: PDF pp. 721-725; the section's last three lines run onto PDF p. 726, cited as the tail page, above the heading of the next section)

## What the section covers
Where finetuning data comes from and how it is labelled: using your own application's data, checking existing datasets, combining several acquisition channels into one dataset, a list of public dataset sources, and the difficulty of writing annotation guidelines.

## Meaning
- Data acquisition aims for a large enough dataset with the needed quality and diversity while respecting user privacy and regulation (PDF p. 721).
- Methods named: sourcing public data, buying proprietary data, annotating, and synthesizing. A niche but growing research area studies acquisition strategy, meaning how best to build a dataset to given requirements within a budget (PDF p. 721).

## Why it matters
- The most valuable source is usually your own application. A data flywheel, where user-generated data continually improves the product, is described as a significant advantage. Application data is perfectly relevant and aligned with the task, matching the distribution you care about, which other sources struggle to match (PDF p. 721).
- Application data can be user content, system-generated data from usage, or user feedback. Designing the feedback system is deferred to Chapter 10 (PDF p. 721).

## How it works

### Check existing data first
Data marketplaces offer open source and proprietary sets; some may fit exactly, but the usual outcome is mix-and-match, with one dataset built from several sources and channels (PDF pp. 721-722).

### Worked example: building an (instruction, response) dataset (PDF p. 722)
1. Find an available dataset with desirable traits: 10,000 examples.
2. Drop low-quality instructions: 9,000 remain.
3. Set aside examples with low-quality responses (3,000 of them), leaving 6,000 with good instructions and good responses.
4. Hand-write responses for the 3,000 good instructions that were set aside: total 9,000 high-quality examples.
5. Notice topic X is thin. Hand-write a set of instruction templates for X and have an AI model synthesize 2,000 instructions from them. (The text says 100 templates in one place and "these 10 templates" in the next sentence; the book is inconsistent, and I record both numbers as printed.)
6. Manually annotate the 2,000 synthetic instructions: total 11,000 examples.

The book calls this a heavy simplification. Real work includes rounds of discovering that annotations are unhelpful (so the guidelines are updated and data re-annotated), that some are factually wrong (so a second group of annotators fact-checks), or that 100 synthetic instructions per template hurts diversity (so you write more templates and generate fewer instructions from each) (PDF pp. 722-723).

### Public dataset sources (PDF pp. 724-725)
The book's advice: use available data but never fully trust it; inspect and validate it. Always check licenses and try to trace where data comes from, because even a commercially licensed dataset may contain part from a source that does not allow commercial use (PDF p. 724). Listed resources:
1. Hugging Face and Kaggle, hundreds of thousands of datasets each.
2. Google Dataset Search, called wonderful and underrated.
3. Government open data: Data.gov (hundreds of thousands of datasets) and data.gov.in (tens of thousands).
4. University of Michigan ICPSR, social-study data (tens of thousands).
5. UC Irvine Machine Learning Repository and OpenML, older, several thousand each.
6. Open Data Network, tens of thousands searchable.
7. Cloud providers' small open collections, notably AWS Open Data.
8. ML framework built-ins, such as TensorFlow datasets.
9. Evaluation harnesses, e.g. Eleuther AI's lm-evaluation-harness: 400+ benchmark datasets averaging 2,000+ examples each, large enough for PEFT finetuning (PDF p. 725).
10. Stanford Large Network Dataset Collection, for graph data.

### Annotation
- Often you must annotate your own data. The hard part is not only the labelling but writing clear guidelines: state what a good response is and why; whether a response can be correct yet unhelpful; what separates a 3 from a 4. Guidelines are needed for both human and AI-powered annotation (PDF p. 725).
- LinkedIn and other teams reported annotation guidelines among the hardest parts of the pipeline. The book finds it alarming how often people abandon careful annotation midway and hope the model figures out the answers; strong models sometimes succeed but this is too risky for many applications (PDF p. 725).
- Good news: these guidelines are the same as those for evaluation data (Chapter 4), another reason to invest in evaluation guidelines and data. Your evaluation examples can also be augmented or used as seeds to synthesize new data, taken up in the next section (PDF pp. 725-726).

## When and how to apply
INTERPRETATION: start with a flywheel design for your own application data, then fill gaps with checked public data, then manual annotation and synthesis, expecting several rounds of guideline revision.

## Limitations and failure modes
Unvetted or mis-licensed public data; low-quality or incorrect annotations needing fact-checking; reduced diversity from too many synthetic items per template; abandoning annotation half way (PDF pp. 722-725).

## Relations
The evaluation guideline step (C04-012) supplies the guideline content reused for annotation. Quantity decisions are in C08-005; the next section (C08-007 lead-in, C08-008 reasons) covers synthesis.

## Time-sensitive statements
The dataset counts for the repositories and the 400+ benchmark figure for lm-evaluation-harness reflect the book's writing date (PDF pp. 724-725).
