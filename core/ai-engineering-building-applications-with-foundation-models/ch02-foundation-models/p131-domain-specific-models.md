---
id: C02-004
title: Domain-Specific Models
source_pages: "131-134"
chapter: 2
concepts: [domain-specific-models, training-data-distribution, common-crawl-domains, alphafold, med-palm2, bionemo, clip, vision-benchmarks]
related: [C02-002, C02-003]
time_sensitive: true
---
# Domain-Specific Models
(Source: PDF pp. 131-134)

## What the section covers
Why general-purpose models handle everyday questions across many domains but struggle on specialised tasks, how to see which domains a model has been exposed to (for text and for images), and examples of purpose-built domain models.

## Meaning
- General-purpose models such as Gemini, GPTs and Llamas perform very well across many domains, including coding, law, science, business, sports and environmental science. The reason is largely that these domains are present in their training data (PDF p. 131).
- Figure 2-3 shows the domain distribution of the C4 dataset (Common Crawl subset) from a 2023 Washington Post analysis: Business and Industrial 16%, Technology 15%, News and Media 13%, Arts and Entertainment 11%, Science and Health 9%, Hobbies and Leisure 8%, Jobs and Education 7%, Home and Garden 6%, Travel 6%, Community 5%, Law and Government 4%. The caption warns that the analysis shows only the categories included, not those missing (PDF pp. 131-132).

## How it works: inferring a model's domains
- For vision data there have not been many domain-distribution analyses so far, perhaps because images are harder to categorise than text (PDF p. 132).
- Workaround: infer a model's domains from its benchmark performance. Table 2-3 compares CLIP (OpenAI ViT-B/32) and Open CLIP (ViT-B/32, Cade) accuracy: ImageNet 63.2 vs 62.9; ImageNet v2 not reported for CLIP vs 62.6; Birdsnap 37.8 vs 46.0; Country211 17.8 vs 14.8; Oxford 102 Category Flower 66.7 vs 66.0; German Traffic Sign Recognition Benchmark 32.2 vs 42.0; Stanford Cars 59.4 vs 79.3; UCF101 64.5 vs 63.1 (PDF p. 133).
- The caveat: these benchmarks cover birds, flowers, cars and a few other categories, while the world is far bigger and more complex (PDF p. 132).

## Limitations and failure modes
- General models can answer everyday questions in many domains but are unlikely to do well on domain-specific tasks, especially ones never seen in training (PDF p. 133).
- Drug discovery: involves protein, DNA and RNA data in specific formats that are expensive to obtain and unlikely to appear in public internet data. Cancer screening: usually uses X-ray and fMRI scans, which are hard to get because of privacy (PDF pp. 133-134).

## When and how to apply
- For such tasks you may need to curate very specific datasets (PDF p. 134).
- Notable domain models named: DeepMind's AlphaFold, trained on the sequences and 3D structures of around 100,000 known proteins; NVIDIA's BioNeMo, focused on biomolecular data for drug discovery; Google's Med-PaLM2, which combined an LLM with medical data to answer medical queries more accurately (PDF p. 134).
- Tip from the book: domain-specific models are especially common in biomedicine but other fields can benefit. A model trained on architectural sketches might help architects much more than Stable Diffusion, and one trained on factory plans might optimise manufacturing better than a generic model like ChatGPT (PDF p. 134).

## Relations
Continues the data-curation argument from C02-002 and parallels C02-003 (language-specific data). The section closes by moving on to how model design (architecture and size) affects performance, the next part of the chapter (PDF p. 134).

## Time-sensitive statements
Model names, the 2023 Washington Post domain shares and the CLIP/Open CLIP accuracies are tied to the time of writing.
