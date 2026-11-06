---
id: C08-012
title: Data Processing (Section Lead-in)
source_pages: "755"
chapter: 8
concepts: [data-processing, processing-order, trial-runs, keep-original-data, data-papers]
related: [C08-011, C08-013, C08-014, C08-015, C08-016]
time_sensitive: false
---
# Data Processing (Section Lead-in)
(Source: PDF p. 755, below the "Data Processing" heading; the closing TIP box printed at the top of PDF p. 756 above the "Inspect Data" heading also belongs here. The text above the heading on p. 755 is the end of C08-011.)

## What the section covers
The introduction to the Data Processing section: data must be processed to suit each use case, the section lists some steps for reference, and a tip box gives efficiency advice for running those steps on large datasets (PDF p. 755). The steps themselves (inspect, deduplicate, clean and filter, format) follow in C08-013 to C08-016.

## Meaning and framing
- Processing requirements depend on the use case. The steps described are examples to consult, not a fixed pipeline (PDF p. 755).
- The author recommends reading model papers that disclose details about their datasets, because they often hold good tips about how the researchers curated, generated and processed data (PDF p. 755).

## How it works: the efficiency tips
With a lot of data, each processing step can take hours or even days. The tip box offers three suggestions (PDF p. 756):
1. Order is flexible. Run the steps in whatever order saves time and compute. If cleaning an example costs more than deduplicating, remove duplicates first and clean afterward. If deduplication costs more than filtering out low-quality data, filter first (PDF p. 756).
2. Do trial runs. Check that processing scripts behave as expected on a small run before applying them to the full data (PDF p. 756).
3. Do not modify data in place. Keep a copy of the original for two reasons: you or another team may need to process the data differently for other applications, and script bugs can corrupt data (PDF p. 756).

## When and how to apply
INTERPRETATION: Estimate the per-example cost of each step on a sample, order the cheap and most-reducing steps first, test on a subset, and write outputs to new files.

## Relations
Follows model distillation (C08-011) and is followed by inspecting data (C08-013), deduplication (C08-014), cleaning and filtering (C08-015) and formatting (C08-016).
