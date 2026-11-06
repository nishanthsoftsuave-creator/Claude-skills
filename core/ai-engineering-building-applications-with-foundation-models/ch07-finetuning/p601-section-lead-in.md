---
id: C07-003
title: When to Finetune (Section Lead-in)
source_pages: "601"
chapter: 7
concepts: [when-to-finetune, finetuning-cost, prompting-first, resource-requirements, ml-talent]
related: [C07-002, C07-004, C07-005, C07-006]
time_sensitive: false
---
# When to Finetune (Section Lead-in)
(Source: PDF p. 601, from the "When to Finetune" heading onward. The text above that heading on the same page belongs to C07-002.)

## What the section covers
The short opening of the "When to Finetune" section, before its first subsection. It frames the decision whether finetuning is appropriate at all, before the book goes into specific finetuning techniques. The last sentence begins at the bottom of this page and finishes at the top of the next page (covered in C07-004); the lead-in is thus split across the page break.

## Why it matters
- Before diving into techniques, one must decide whether finetuning is the right option (PDF p. 601).
- Relative to prompt-based methods, finetuning needs considerably more resources, and not only data and hardware but also ML talent (PDF p. 601).
- Because of this, finetuning is generally attempted only after extensive experiments with prompt-based methods; this conclusion is stated on the next page. Prompting and finetuning are not mutually exclusive, and real-world problems often need both.

## When and how to apply
INTERPRETATION: treat finetuning as a later step in the adaptation ladder. Exhaust prompting first, then weigh finetuning's data, hardware and ML-talent costs against the expected gain, using the reasons for and against given in C07-004 and C07-005.

## Relations
Followed by the reasons to finetune (C07-004), reasons not to finetune (C07-005) and the finetuning versus RAG comparison (C07-006).
