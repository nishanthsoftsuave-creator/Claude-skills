---
id: C08-013
title: Inspect Data
source_pages: "756-758"
chapter: 8
concepts: [data-inspection, data-statistics, token-distribution, inter-annotator-disagreement, annotator-bias, manual-inspection, outliers]
related: [C08-012, C08-014, C08-015, C08-006, C08-003]
time_sensitive: false
---
# Inspect Data
(Source: PDF pp. 756-758; the section's closing paragraph runs onto the top of the next page, above the "Deduplicate Data" heading)

## What the section covers
The first data-processing step: looking at a freshly gathered raw dataset to judge its quality through statistics, distributions broken down by source or annotator, and hands-on manual checking (PDF p. 756). The tip box above the heading on p. 756 belongs to C08-012.

## How it works
### Basic questions and statistics (PDF p. 756)
- Once public and internal data have been collected, inspect the data to get a feel for quality. Gather information about it: where it came from, how it was processed, what else it has been used for.
- Plot distributions of tokens (which are common), input lengths, response lengths and similar. Ask whether it contains special tokens, and whether you can get a distribution of topics and languages and how relevant they are to your task.

### Creative statistics (PDF pp. 757-758)
- Be inventive with statistics. A Microsoft research group (2023) compared GPT-3 and GPT-4 generations for the same instructions using the distribution of (verb, direct object noun) pairs and the distribution of response length. The analysis helps evaluate data and also models (PDF p. 757).
- Figure 8-6 (PDF p. 757, from Peng et al., 2023, "Instruction Tuning with GPT-4") is a horizontal bar chart of the top 25 verb-noun pair frequencies, one side for GPT-4 and one for GPT-3. Frequent pairs include (have, impact), (follow, step), (involve, step) and (play, role). An inset reports unique verb-noun pairs: GPT-4 5229, GPT-3 6133 (read from the rendered image). Note that the printed unique-pair count is higher for GPT-3 than GPT-4, while the book's remark below describes GPT-4 as broader; the two are not reconciled here. Frequencies on the axis run to roughly 175.
- Figure 8-7 (PDF p. 757) is a histogram of output sequence length (0 to about 500) on a log frequency axis. GPT-3 responses concentrate at short lengths, while GPT-4's extend further, with substantial mass between roughly 100 and 400.
- The book's takeaway: GPT-4 appears to have a broader and more varied range of verb-noun pairings and tends to write longer responses (PDF p. 758).

### Breaking down and checking annotations (PDF p. 758)
- Plot distributions by data source, time, annotator and so on. Look for question patterns that draw longer or shorter responses or higher or lower scores, look for outliers, ask what causes them and what to do about them.
- If scores should be normally distributed, check whether each annotator's scores are. Some annotators give much shorter responses or lean toward high scores, and you decide what to do with their annotations.
- For examples with more than one annotation, compute inter-annotator disagreement, examine the conflicting examples and resolve the conflicts.

### Manual inspection (PDF p. 758, continuing onto the next page)
- Exploration tools are useful but do not replace manual inspection. The author reports that about 15 minutes of staring at data in any project usually yields insight that saves hours of trouble. Greg Brockman (OpenAI co-founder) is quoted tweeting that manual data inspection has "probably the highest value-to-prestige ratio" of any ML activity (PDF p. 758).
- Check that examples make sense. For annotated data, choose a few queries, annotate them yourself and compare with the given annotations to gauge trustworthiness. The sentence about annotating queries yourself starts on this page and finishes on the next. Also fact-check responses. Ask how unique the examples are, whether any share a query but have different responses, and whether any share a response but have different queries (these questions appear on the next page).

## When and how to apply
INTERPRETATION: Run this before deduplication and cleaning, since what you find (outlier annotators, language mix, odd tokens) informs the heuristics used in C08-014 and C08-015.

## Relations
Follows the lead-in C08-012; feeds deduplication (C08-014) and cleaning (C08-015). Annotation quality themes tie to C08-006 and data quality to C08-003.
