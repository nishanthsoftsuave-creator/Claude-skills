---
id: C08-003
title: Data Quality
source_pages: "704-706"
chapter: 8
concepts: [data-quality, noisy-data, annotation-guideline, consistency, deduplication, data-contamination, compliance, lima]
related: [C08-002, C08-004]
time_sensitive: false
---
# Data Quality
(Source: PDF pp. 704-706; the last characteristic, "Compliant", sits at the top of the next page and is summarised here without a page cite)

## What the section covers
Evidence that a small amount of high-quality data can beat a large amount of noisy data, a working definition of high-quality data, and the six characteristics the book lists: relevant, aligned with task requirements, consistent, correctly formatted, sufficiently unique, and compliant.

## Why it matters: evidence that quality beats quantity
- A small amount of high-quality data can outperform a large amount of noisy data (irrelevant or inconsistent). The Yi model family's creators found 10K carefully crafted instructions better than hundreds of thousands of noisy ones (PDF p. 704).
- LIMA ("Less Is More for Alignment"): a 65B-parameter Llama finetuned on only 1,000 carefully curated prompts and responses produced answers that human annotators judged equivalent or strictly preferred to GPT-4 in 43% of cases. The downside of so few examples is that LIMA is not as robust as product-grade models (PDF p. 704).
- The Llama 3 team reached the same conclusion. They found human-generated data more prone to errors and inconsistencies, especially for nuanced safety policies, and so built AI-assisted annotation tools to keep quality high (PDF p. 704).

## Meaning
High-quality data is data that helps you do your job efficiently and reliably. Detailed answers vary by person, but in general six characteristics apply, and particular use cases may add others (PDF pp. 704-705).

## The six characteristics
1. Relevant. Examples must relate to the task the model is being trained for. A 19th-century legal dataset is probably irrelevant for answering legal questions today, but highly relevant if the task is the 19th-century legal system (PDF p. 705).
2. Aligned with task requirements. Annotations must fit what the task demands: factually correct for a factual-consistency task, creative for a creativity task, scores plus justifications if the task wants justified scores, concise if the task wants concise answers. The author deliberately says "aligned" rather than "accurate" or "correct", because an accurate response may not be what the user wants (PDF p. 705).
3. Consistent. Annotations should agree across examples and across annotators: two annotators labelling the same example should not differ much. For essay scoring from 1 to 5, do two essays with the same score have the same quality? Inconsistent annotations confuse the model and make learning harder. A good annotation guideline is essential both for alignment with task requirements and for consistency (PDF p. 706).
4. Correctly formatted. Every example should follow the format the model expects. Redundant formatting tokens interfere with learning and should be removed; for instance strip HTML tags from scraped product reviews. Watch for trailing whitespace, newlines, inconsistent casing and numeric formats (PDF p. 706).
5. Sufficiently unique. Duplicated examples can introduce bias and cause data contamination. "Sufficiently" is used because some use cases tolerate more duplication than others (PDF p. 706).
6. Compliant. Data must meet all relevant internal and external policies, including laws and regulations. For example, if PII may not be used for training, the data must contain none (continues onto the next page).

## When and how to apply
INTERPRETATION: before creating data, work out what each characteristic means for your application. The book says at the start of the next page that the techniques later in the chapter aim to produce data with these properties.

## Relations
Follows the lead-in (C08-002) and is followed by data coverage (C08-004).