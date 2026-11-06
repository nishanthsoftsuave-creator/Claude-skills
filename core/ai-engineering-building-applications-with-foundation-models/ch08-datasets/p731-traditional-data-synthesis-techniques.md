---
id: C08-009
title: Traditional Data Synthesis Techniques
source_pages: "731-737"
chapter: 8
concepts: [data-synthesis, procedural-generation, rule-based-synthesis, templates, data-augmentation, perturbation, simulation, sim2real, rare-events]
related: [C08-007, C08-008, C08-010]
time_sensitive: false
---
# Traditional Data Synthesis Techniques
(Source: PDF pp. 731-737)

## What the section covers
The two pre-LLM families of generating or expanding training data: rule-based synthesis (templates plus simple transformations, including perturbation) and simulation. Data synthesis is not new to AI; it has a long history in software testing, gaming and robotics, where algorithmic generation is called procedural generation, as opposed to manual generation. Games use it to build levels, maps, items and characters on the fly, and most techniques from those fields carry over to AI (PDF p. 731). The section ends by pointing to AI-powered synthesis, the third and newer approach, which is the next row (C08-010) (PDF p. 737).

## Meaning
- **Procedural generation**: producing data by algorithm rather than by hand (PDF p. 731).
- **Rule-based synthesis**: using predefined rules and templates, with a random generator filling in the fields (PDF p. 731).
- **Augmentation by transformation**: creating new examples from existing ones through simple changes that keep the label or meaning intact (PDF pp. 732-733).
- **Perturbation**: adding noise to existing data to produce new data (PDF p. 734).
- **Simulation**: running experiments in a virtual environment instead of the real world (PDF p. 736).
- **Sim2Real**: the subfield about adapting algorithms trained in simulation so they work in the real world (PDF p. 736).

## How it works

### Templates and random generators
- The simplest recipe: start with a template and populate each field using a random generator such as Faker. The book's example is a credit card transaction template with fields for transaction ID, date, time, amount, merchant name, merchant category, location (city, state, country), payment method (card, cash, online and so on), transaction status (completed, pending, failed) and a description (PDF pp. 731-732).
- Why it is used: because transaction data is sensitive, many fraud detection models are first trained on synthetic transactions made from templates like this, to demonstrate feasibility before anyone grants access to real data (PDF p. 732).
- Templates are widely used to produce structured documents: invoices, resumes, tax forms, bank statements, event agendas, product catalogs, contracts, configuration files. They also work for data governed by a grammar or syntax, such as regular expressions and math equations (PDF p. 732).
- Scale example: DeepMind trained AlphaGeometry, an Olympiad-level geometry model, on 100 million synthetic examples (Trinh et al., 2024) (PDF p. 732).

### Simple transformations of existing data
- Images: randomly rotate, crop, scale or erase part of an image. A flipped cat is still a cat; a slightly cropped soccer match is still a soccer match (PDF p. 732). Krizhevsky et al. (2012) showed in the AlexNet paper how useful this is by augmenting ImageNet (PDF p. 733).
- Text: replace a word with a similar one, provided meaning and sentiment do not change. "She's a fantastic nurse" can yield "She's a great nurse" (PDF p. 733).
- Bias mitigation by swapping: if the data associates "nurse" with women and "doctor" with men, swap typically gendered words for their opposites (PDF p. 733). Table 8-2 shows four original-to-augmented pairs: "She's a fantastic nurse" becomes "He's a fantastic nurse" (and, in the same table cell, "She's a fantastic doctor"); "The CEO of the firm, Mr. Alex Wang" becomes "Ms. Alexa Wang"; "my mom made a casserole" becomes "my dad made a casserole"; "Emily has always loved the violin" becomes "Mohammed has always loved the violin" (PDF p. 734). The render of p. 734 confirms the first row's augmented cell holds two lines (the pronoun swap and the occupation swap nurse to doctor). Together the swaps cover pronouns, an occupation word, titles and names, family roles, and a first-name change (Emily to Mohammed).
- Finding similar words: use a dictionary of synonyms, or take words whose embeddings lie close together in word embedding space. Beyond word replacement, AI can be asked to rephrase or translate an example; the book defers that to the AI-powered section (PDF p. 734).

### Perturbation
- Origin: researchers found that a slight perturbation can trick a model into misclassifying a sample, for instance white noise added to a ship picture making the model say "car" (PDF p. 734).
- The "One Pixel Attack for Fooling Deep Neural Networks" paper (Su et al., 2017) found that changing a single pixel could cause misclassification for 67.97% of natural images in the Kaggle CIFAR-10 test set and 16.04% of ImageNet test images (PDF pp. 734-735).
- Risk if exploited: an attacker could get an AI model to take them for an authorized employee, or make a self-driving car read a divider as a lane and cause accidents (PDF p. 735).
- Benefit: training on perturbed data can improve performance and make the model more robust to attacks (Goodfellow et al., 2013; Moosavi-Dezfooli et al., 2015). In 2019 Hendrycks and Dietterich built ImageNet-C and ImageNet-P by applying 15 common visual corruptions (brightness, snow, contrast, noise and others) to ImageNet images (PDF p. 735).
- Text perturbation: to train BERT, the authors replaced 1.5% of tokens with random words and saw a small performance gain (Devlin et al., 2018) (PDF p. 735).
- More sophisticated visual augmentation: Snap (2022) describes taking a character and synthesizing similar characters with different skin colors, body types, hairstyles, clothes and facial expressions, to create under-represented corner cases and reduce implicit bias; the augmented assets then train AI models (PDF p. 735).

### Simulation
- Idea: virtual experiments replace real-world data collection that is expensive or dangerous. Testing how a self-driving car reacts to a horse on the highway is done in a virtual environment, not with a real horse. Self-driving simulation engines named: CARLA (Dosovitskiy et al., 2017), Waymo's SimulationCity, and Tesla's simulation of San Francisco (PDF p. 736).
- Robotics: to teach a robot to pour coffee when the correct joint motions are unknown, simulate many scenarios with different joint movements and train only on the ones where coffee was poured successfully (PDF p. 736).
- Benefits: many experiments at minimal cost, without accidents or physical damage (PDF p. 736).
- Caveat: a robot that works in simulation might fail in reality, but one that fails in simulation will probably fail in reality too. However sophisticated, a simulation is a simplification of the real world, hence Sim2Real (PDF p. 736).
- Tool-use data: human-generated actions are not always the most efficient for AI agents, and simulation can reveal actions humans overlook. Given a query, simulate different action sequences, execute them, validate the outcomes, and use the most efficient sequence as the annotated response (PDF p. 737).
- Rare events: simulate a company going public or a major bankruptcy to study market effects (finance); simulate defects in materials or assemblies to train anomaly detection and quality control models (manufacturing); vary temperature, precipitation and extreme weather by simulating Earth systems, so models see a broader range of possible futures (climate science) (PDF p. 737).

## Alternatives and trade-offs
Rule-based and simulation methods were useful for many cases, but the book says data synthesis only truly took off once AI could generate realistic, high-quality data (PDF p. 737). INTERPRETATION: rule-based transformations are cheap and label-preserving but limited to what the rules express; simulations give access to dangerous or rare situations but only as faithful as the simplified model of the world.

## Limitations and failure modes
- Word replacement assumes the swap does not change the sentence's meaning or sentiment (PDF p. 733); INTERPRETATION: if it does, the original label no longer fits.
- Simulated data may not transfer to reality (PDF p. 736).
- The same perturbation sensitivity that makes models more robust when trained on also exposes security risks (PDF p. 735).

## Relations
Follows the reasons for synthesis (C08-008) and the section lead-in (C08-007); continues into AI-powered synthesis (C08-010). The rewriting and translation ideas deferred here are covered there.
