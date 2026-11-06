---
id: C05-017
title: Information Extraction
source_pages: "477-482"
chapter: 5
concepts: [information-extraction, training-data-extraction, factual-probing, lama, divergence-attack, memorization, pii-leakage, copyright-regurgitation, privacy]
related: [C05-016, C05-018, C05-015]
time_sensitive: true
---
# Information Extraction
(Source: PDF pp. 477-482, plus tail PDF p. 483 for the closing lines above the "Defenses Against Prompt Attacks" heading; the two lines at the top of PDF p. 477 belong to the previous row, C05-016.)

## What the section covers
How the very usefulness of a language model, that it stores a large body of knowledge reachable through conversation, can be exploited to pull out what it knows: training data, private context, copyrighted material. It covers the motives, factual probing, published extraction results for text and image models, PII, and copyright regurgitation with and without adversaries.

## Meaning: what attackers want (PDF p. 477)
- **Data theft**: extracting training data to build a competing model. Imagine spending millions of dollars and months or years collecting data, only for rivals to pull it out.
- **Privacy violation**: extracting private or sensitive information, whether in the training data or in the context given to the model. Many models are trained on private data; the book's example is Gmail's auto-complete model, trained on users' emails (Chen et al., 2019), so extracting its training data could expose private emails.
- **Copyright infringement**: if the model was trained on copyrighted data, attackers can get it to regurgitate that material (PDF pp. 477-478).

## How it works

### Factual probing (PDF p. 478)
- Factual probing is a niche research area aimed at finding out what a model knows. Meta's AI lab introduced the LAMA (Language Model Analysis) benchmark in 2019 (Petroni et al.) to probe relational knowledge in training data, of the form "X [relation] Y" such as "X was born in Y" or "X is a Y". It is elicited by fill-in-the-blank statements, e.g. "Winston Churchill is a _ citizen", where a model with the knowledge should answer "British".
- The same techniques can pull sensitive data from training sets. The assumption is that the model memorizes training data and the right prompt triggers recall. To get someone's email address, an attacker might prompt "X's email address is _".

### Early results: possible but low risk (PDF pp. 478-479)
Carlini et al. (2020) and Huang et al. (2022) extracted memorized training data from GPT-2 and GPT-3. Both concluded that although feasible, the risk is low because attackers must know the specific context in which the target data appears. Example: if an email address occurs in training as "X frequently changes her email address, and the latest one is [EMAIL ADDRESS]", then that exact context is more likely to yield the address than a general prompt such as "X's email is ...".

### The divergence attack (PDF p. 479)
- Later work by Nasr et al. (2023) showed a strategy that makes a model reveal sensitive information without knowing the context. Asked to repeat the word "poem" forever, ChatGPT (gpt-3.5-turbo) repeated it several hundred times and then diverged. After divergence the output is mostly nonsense, but a small fraction is copied directly from the training data. Figure 5-13 shows the user prompt asking the model to repeat the word "poem" forever, followed by a reply that, after the repeated word, shows a block of contact details (name, phone, email, address) (PDF p. 479).
- The implication is that prompt strategies may exist that extract training data while knowing nothing about it (PDF p. 479).
- Nasr et al. estimated memorization rates on their test corpus at close to 1% for some models. The rate is higher when the model's training distribution is closer to the test corpus. Across all model families studied, larger models memorize more, so larger models are more exposed to extraction attacks (PDF pp. 479-480).

### Other modalities (PDF p. 480)
"Extracting Training Data from Diffusion Models" (Carlini et al., 2023) pulled over a thousand near-duplicates of existing images out of the open-source Stable Diffusion, many with trademarked company logos. Figure 5-14 (viewed in the render) is two aligned strips of about a dozen small thumbnails, an "Original" row (including faces, a sports scene and a Netflix logo) above a "Generated" row that looks near-identical image by image; the caption says the generated images are near duplicates of real-world images, probably because the originals were in the training data. The authors concluded diffusion models are much less private than earlier generative models such as GANs, and that fixing this may need new advances in privacy-preserving training.

## Limitations, caveats and mitigations
- Extracting training data does not always mean extracting PII; often the extracted text is common material such as MIT license text or the lyrics of "Happy Birthday" (PDF pp. 480-481).
- PII risk can be reduced with filters that block requests asking for PII and responses containing PII (PDF p. 481).
- Some models block suspicious fill-in-the-blank requests. Figure 5-15 shows Claude refusing a fill-in-the-blank of a novel passage as copyrighted, then agreeing after the user said it was their own original work. The book's caption calls the block a mistake that was withdrawn once the user pointed it out; it illustrates a false refusal (PDF pp. 481-482).

## Copyright regurgitation without an adversary
- A model trained on copyrighted data can regurgitate it for ordinary users, which can harm model developers, application developers and copyright owners. Using regurgitated material unknowingly can get you sued (PDF p. 481).
- The 2022 Stanford paper "Holistic Evaluation of Language Models" measured this by giving the model the first paragraph of a book and asking for the second; an exact match implies the book was in training and is being regurgitated. Across many foundation models, it concluded direct regurgitation of long copyrighted sequences is "somewhat uncommon" but noticeable for popular books (PDF pp. 481-482).
- That does not mean the risk is small. Regurgitation can lead to costly lawsuits. The study also leaves out modified regurgitation: a story about a gray-bearded wizard "Randalf" who tries to destroy a dark lord's bracelet by throwing it into "Vordor" would not be flagged as copying The Lord of the Rings. Such non-verbatim regurgitation is still a notable risk for companies using AI in core business (PDF pp. 482-483).
- Why not measure it? It is hard: deciding whether something infringes can take IP lawyers and subject experts months or years, so a foolproof automatic detector is unlikely. The best fix is not to train on copyrighted material, but if you did not train the model yourself you have no control over that (PDF p. 483).

## When and how to apply
INTERPRETATION: when reviewing an application, check what private data sits in the training set or the prompt context, add input and output PII filters, and avoid over-blocking fill-in-the-blank style requests that are legitimate. Defense measures overall are in C05-018.

## Relations
Follows jailbreaking and prompt injection (C05-016); defenses are in C05-018. Reverse prompt engineering of proprietary prompts (C05-015) is a related extraction topic.

## Time-sensitive statements
Model-specific results (GPT-2, GPT-3, gpt-3.5-turbo, Stable Diffusion, Claude's blocking behavior) and the roughly 1% memorization estimate reflect the studies cited and the date of writing.
