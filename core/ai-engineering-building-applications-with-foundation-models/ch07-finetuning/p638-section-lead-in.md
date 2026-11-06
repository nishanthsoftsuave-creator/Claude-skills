---
id: C07-012
title: Finetuning Techniques (Section Lead-In)
source_pages: "638"
chapter: 7
concepts: [finetuning-techniques, memory-efficient-finetuning, finetuning-accessibility, parameter-efficient-finetuning, model-merging]
related: [C07-011, C07-013, C07-014]
time_sensitive: false
---
# Finetuning Techniques (Section Lead-In)
(Source: PDF p. 638, below the "Finetuning Techniques" heading; the lead-in paragraphs continue onto the next page, above the "Parameter-Efficient Finetuning" heading)

## What the section covers
The opening of the "Finetuning Techniques" section. The lines above the heading on PDF p. 638 finish the quantization discussion and belong to C07-011. Only the first sentences of the lead-in sit on this page, and the lead-in then continues on the next page.

## Why it matters
- The author asks the reader to take away from the preceding memory discussion why finetuning large models is so memory-intensive (PDF p. 638).
- The stated reasoning chain: the more memory finetuning demands, the fewer people can afford to do it (PDF p. 638). The sentence is cut at the page boundary; it continues on the next page.
- The book then states (on the next page, no cite) that techniques which shrink the memory footprint of finetuning make it available to more people, so more of them can adapt models to their own applications.

## Relations
- The section is organised around memory-efficient finetuning, centred on parameter-efficient finetuning (C07-013). The lead-in also announces model merging, which is described as complementary to finetuning rather than a form of it: finetuning tailors one model, merging combines several, often finetuned, models (C07-014). These two announcements are stated on the next page, where the author also calls merging exciting but more experimental, and says that new model types and finetuning techniques have inspired many creative merging approaches.
- It builds on the quantization row (C07-011) and the memory math before it, which explain where finetuning memory goes.
