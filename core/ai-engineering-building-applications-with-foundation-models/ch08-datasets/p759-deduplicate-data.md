---
id: C08-014
title: Deduplicate Data
source_pages: "759-762"
chapter: 8
concepts: [deduplication, test-set-contamination, duplicate-types, pairwise-comparison, hashing, minhash, bloom-filter, dimensionality-reduction, identity-resolution]
related: [C08-013, C08-015, C03-011, C08-003]
time_sensitive: false
---
# Deduplicate Data
(Source: PDF pp. 759-762; the page 759 text above the "Deduplicate Data" heading is the end of C08-013)

## What the section covers
Why duplicates hurt a training dataset, the kinds of duplication and the need to define what counts as a duplicate, and three families of methods for removing them (PDF pp. 759-762).

## Why it matters
- Duplicates skew the data distribution and can introduce bias. In the toy product-price dataset of Table 8-3, repeated entries could lead a model to conclude that all red items are expensive (PDF p. 759).
- Duplicates can cause test set contamination: when duplicated data is split into train and test sets, one copy may land in train and its twin in test (PDF p. 759).
- Several studies show that duplication in training data harms performance (Lee et al., 2021; Tirumala et al., 2023). An Anthropic study (Hernandez et al., 2022) found that repeating 0.1% of the data 100 times can drag an 800M-parameter model down to the performance of a 400M-parameter model, even though the other 90% of training tokens stayed unique (PDF p. 760).
- Even where duplicates do not hurt quality, they waste time and compute (PDF pp. 760-761).

## Table 8-3 (PDF p. 760)
A five-row table with an input column of product descriptions and an output column of prices. Rows 1, 3 and 4 are the same input, {item: pencil, color: red}, each priced $20; row 2 is {item: compass, color: green} at $2; row 5 is {item: pencil, color: green} at $1. Rows 1, 3 and 4 are the duplicates (the caption says duplicates are in grey cells). The printed text wraps mid-word ("re d") but the rendered page was checked and the values above are read from it.

## Meaning: forms of duplication (PDF p. 761)
For a dataset of documents, the book lists:
- whole-document duplication: the same document appears more than once;
- intra-document duplication: for instance, one paragraph appears twice within a document;
- cross-document duplication: for instance, a well-known quote appears in many documents.

What counts as a duplicate depends on your definition. Decide whether you work at document, paragraph, sentence or token level; whether texts must match exactly or an 80% overlap suffices; and whether two lists with the same items in a different order are duplicates (PDF p. 761).

## How it works: deduplication methods
Deduplication can use the same techniques as similarity measurement (Chapter 3), and it is also used for identity resolution, deciding whether two identities such as social media profiles are the same (PDF pp. 761-762). Concrete approaches (PDF p. 762):
- Pairwise comparison: score every example against every other using exact match, n-gram match, fuzzy match or semantic similarity (Chapter 3). Can be expensive for large datasets.
- Hashing: hash examples into buckets and compare only within a bucket. Hash-based methods include MinHash and Bloom filter.
- Dimensionality reduction: reduce dimensions first, then compare pairwise. Many vector-search techniques from Chapter 6 apply.
- Libraries: a quick search finds many; the book names dupeGuru, Dedupe, datasketch, TextDistance, TheFuzz and deduplicate-text-datasets (PDF p. 762). An endnote says the author's open source library lazyNLP also supports overlap estimation and deduplication with a Bloom filter.

## When and how to apply
INTERPRETATION: Fix the duplicate definition and granularity first, deduplicate before splitting into train and test, and choose hashing or dimensionality reduction when pairwise comparison is too costly. Step order against cleaning follows the tip in C08-012.

## Relations
Follows inspection (C08-013), precedes cleaning (C08-015); the similarity measures reuse C03-011. Data quality background in C08-003.
