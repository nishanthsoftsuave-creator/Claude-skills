---
id: C08-015
title: Clean and Filter Data
source_pages: "763"
chapter: 8
concepts: [data-cleaning, html-removal, pii-removal, low-quality-filtering, active-learning, importance-sampling, data-pruning, annotator-fatigue]
related: [C08-014, C08-016, C08-013, C08-003]
time_sensitive: false
---
# Clean and Filter Data
(Source: PDF p. 763; the closing paragraph on further filtering is printed above the "Format Data" heading at the top of PDF p. 764 and belongs here)

## What the section covers
Cleaning data so the model is performant and safe, and filtering when there is more data than can be used (PDF p. 763).

## How it works
- Strip extraneous formatting tokens. Scraped public datasets often carry stray HTML tags; unless you want the model trained on them, remove them. Databricks found that removing extraneous Markdown and HTML tokens improved its model's accuracy by 20% and cut input token length by 60% (PDF p. 763).
- Remove anything that violates your policies: PII, sensitive data, copyrighted data, toxic data. Chapter 4 techniques can help. Drop fields you may not use, such as zip code, name and gender (PDF p. 763).
- Remove low-quality data using the techniques from "Data verification" (PDF p. 763).
- Manual inspection matters especially here. Looking at data can reveal patterns usable as heuristics for spotting low-quality examples, and these can be non-obvious. Kern et al. (2024) found that annotations made in the second half of an annotation session are lower quality, likely because of boredom or fatigue (PDF p. 763).

### Filtering to fit the budget
When there is more data than you need or can afford (for example under a compute budget), filter further. Options are active learning, to pick examples most useful for the model to learn from, and importance sampling, to find the examples most important to the task. Their efficiency depends on having a good way to score each example's importance. Meta researchers on data pruning (Sorscher et al., 2022) concluded that finding good pruning metrics could greatly lower the resource cost of modern deep learning (PDF p. 764 continuation, printed above the Format Data heading).

## When and how to apply
INTERPRETATION: Run policy compliance checks even when quality looks fine, and use inspection findings from C08-013 as filtering heuristics.

## Relations
Follows deduplication (C08-014) and precedes formatting (C08-016); relies on inspection (C08-013).
