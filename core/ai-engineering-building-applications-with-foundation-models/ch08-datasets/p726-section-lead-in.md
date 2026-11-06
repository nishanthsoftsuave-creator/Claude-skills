---
id: C08-007
title: Data Augmentation and Synthesis (Section Lead-in)
source_pages: "726"
chapter: 8
concepts: [data-augmentation, data-synthesis, synthetic-data, programmatic-data-generation, faker, fake-data-generators, human-plus-ai-data]
related: [C08-006, C08-008, C08-009]
time_sensitive: false
---
# Data Augmentation and Synthesis (Section Lead-in)
(Source: PDF p. 726, from the heading "Data Augmentation and Synthesis" onward, plus the lead-in text on PDF p. 727 above the heading "Why Data Synthesis". The first lines of PDF p. 726 close the preceding annotation section, C08-006.)

## What the section covers
The introduction to the section: it defines data augmentation and data synthesis, notes how the book uses the terms, gives the history of artificially generated data in software testing, and states that synthetic data complements rather than replaces human data.

## Meaning
- Along with compute and talent, data is called the hardest challenge in AI, and generating data programmatically has long been an industry goal (PDF p. 726).
- Data augmentation creates new data from existing real data. Example: flip a real photo of a cat to get a new image of the same cat (PDF p. 726).
- Data synthesis generates data that mimics the properties of real data. Example: simulate a mouse moving across a web page to produce what bot movements look like (PDF p. 726).
- So augmented data is derived from real data while synthetic data is not real. Because both aim to automate data creation, the terms are sometimes used interchangeably, and the book often says "data synthesis" for both (PDF p. 726).

## How it works: history and scope
- Artificial data has a long history in software engineering, first as fake data for tests. Libraries such as Faker and Chance generate names, addresses, phone numbers and emails in simple formats. Example: to test a shipping-address parser, generate addresses from various countries and states in many formats to check that all parse (PDF p. 727).
- With AI that can produce text and media indistinguishable from human output, much richer data can be synthesized: doctor's notes, contracts, financial statements, product descriptions, images, video commercials, and so on. That lowers the cost of generation and opens more use cases (PDF p. 727).

## Limitations and caveats
Synthetic data should reduce pressure on human-generated data but does not replace it. In many use cases a mix of human and AI data gives the best value, as discussed in the book's later "Limitations to AI-generated data" discussion (PDF p. 727).

## Relations
The preceding section on acquisition (C08-006) ends by suggesting evaluation examples can seed synthesis. The reasons for synthesizing are in C08-008; traditional techniques follow in C08-009.
