---
id: C02-002
title: Training Data - Section Lead-in
source_pages: "121-123"
chapter: 2
concepts: [training-data, common-crawl, c4, data-quality, data-curation, heuristic-filtering, domain-specific-data]
related: [C02-001, C02-003, C02-004]
time_sensitive: true
---
# Training Data - Section Lead-in
(Source: PDF pp. 121-123)

## What the section covers
The opening of the Training Data section, before its first subsection (Multilingual Models). It argues that a model is bounded by its data, uses Common Crawl as the typical example of data that is available rather than ideal, and explains why curating language- and domain-specific data matters, including why more data is not automatically better.

## Meaning
- Core claim: "An AI model is only as good as the data it was trained on" (PDF p. 121).
- Illustrations: with no Vietnamese in the training data, a model cannot translate English into Vietnamese; an image classifier trained only on animals will do badly on photos of plants (PDF p. 121).
- To improve a model on a task, you might add more data for that task. But gathering enough data for a large model is hard and expensive, so developers often depend on whatever data exists even if it does not fit their needs well (PDF p. 121).

## How it works: the Common Crawl example
- Common Crawl is created by a nonprofit that crawls internet websites sporadically. In 2022 and 2023 it crawled roughly 2-3 billion web pages every month (PDF p. 122).
- Google offers a cleaned subset called the Colossal Clean Crawled Corpus (C4) (PDF p. 122).
- Quality is questionable, for Common Crawl and to a degree C4: clickbait, misinformation, propaganda, conspiracy theories, racism, misogyny and other dubious sites. A Washington Post study found that among the 1,000 most common websites in the dataset were several media outlets rated low for trustworthiness on NewsGuard's scale; in plain terms, it contains plenty of fake news (PDF p. 122).
- Despite this, availability drives adoption: variants of Common Crawl are used in most foundation models that disclose their data sources, such as OpenAI's GPT-3 and Google's Gemini. The author suspects models that do not disclose their data also use it. To dodge scrutiny from the public and competitors, many companies have stopped disclosing training data (PDF p. 122).
- Heuristic filtering example: for GPT-2, OpenAI used only Reddit links that received at least three upvotes. This screens out links nobody cares about, but Reddit is hardly a model of propriety and good taste (PDF p. 122).

## Limitations and failure modes
- The "use what we have, not what we want" approach can yield models that do well on tasks represented in their training data but not on the tasks you care about (PDF p. 123).
- Training on everything (general plus specialised data) is what many people do, but more data usually costs more compute and does not always give better results (PDF p. 123).

## When and how to apply
- To counter the availability problem, curate datasets that match your needs. The following subsections focus on curating data for specific languages and domains, which gives a broad but specialised foundation for applications in those areas; data strategies for highly specific tasks are left to Chapter 8 (PDF p. 123).
- Language- and domain-specific foundation models can be trained from scratch, but it is also common to finetune them on top of general-purpose models (PDF p. 123).

## Alternatives and trade-offs: quality versus quantity
- A smaller amount of high-quality data can beat a large amount of low-quality data. Example: Gunasekar et al. (2023) used 7B tokens of high-quality coding data to train a 1.3B-parameter model that beat much larger models on several important coding benchmarks (PDF p. 123).
- The book defers the deeper treatment of data quality to Chapter 8 (PDF p. 123).

## Relations
Introduced by the chapter roadmap (C02-001). The language-specific case is C02-003 (Multilingual Models) and the domain-specific case is C02-004 (Domain-Specific Models).

## Time-sensitive statements
The Common Crawl crawl volume (2022-2023), the models said to use it (GPT-3, Gemini), the GPT-2 Reddit filter and the 2023 coding-model result reflect the state of things at the time of writing.
