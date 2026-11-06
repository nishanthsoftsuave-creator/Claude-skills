---
id: C02-007
title: Post-Training Overview
source_pages: "169-172"
chapter: 2
concepts: [post-training, supervised-finetuning, preference-finetuning, rlhf, dpo, rlaif, pre-training-vs-post-training, shoggoth]
related: [C02-006, C03-007]
time_sensitive: false
---
# Post-Training Overview
(Source: PDF pp. 169-172)

## What the section covers
The lead-in of the Post-Training section: why a pre-trained model needs further work, the two standard post-training steps, how post-training differs from pre-training, a terminology warning, and the Figure 2-10 workflow with its Shoggoth analogy. The page-169 sentence about architecture and scale being covered closes the preceding section and only links to this one (PDF p. 169).

## Meaning
- Post-training starts from a pre-trained model, e.g. one pre-trained with self-supervision (PDF p. 169).
- **Two issues of a pre-trained model.** (1) Self-supervision optimizes for text completion, not conversation. (2) If the data was scraped indiscriminately from the internet, outputs can be racist, sexist, rude or simply wrong. Post-training aims to fix both (PDF p. 169).
- **Two general steps** (each model's post-training differs) (PDF p. 169):
  1. Supervised finetuning (SFT): finetune on high-quality instruction data so the model suits conversation rather than completion.
  2. Preference finetuning: further finetune so responses match human preference; typically done with reinforcement learning (RL).
- **Preference finetuning techniques** (PDF p. 170): reinforcement learning from human feedback (RLHF), used by GPT-3.5 and Llama 2; Direct Preference Optimization (DPO), used by Llama 3; reinforcement learning from AI feedback (RLAIF), potentially used by Claude.

## Why it matters
- Pre-training optimizes token-level quality (predict the next token accurately), but users care about the quality of the whole response. Post-training optimizes the model to produce responses users prefer (PDF p. 170).
- Analogy: pre-training is like reading to acquire knowledge; post-training is like learning how to use it (PDF p. 170).
- Post-training uses a small slice of resources compared with pre-training: InstructGPT used 2% of compute for post-training and 98% for pre-training. It can therefore be seen as unlocking capabilities the pre-trained model already has but that are hard to reach by prompting alone (PDF pp. 170-171).

## Terminology warning
Some people use "instruction finetuning" for SFT alone, others for SFT plus preference finetuning. To avoid ambiguity the book does not use the term (PDF p. 170).

## How it works: the workflow in Figure 2-10 (PDF p. 171)
The figure (rendered and checked) assumes RLHF as the last step. Left to right: low-quality data such as internet data feeds self-supervised pre-training (optimized for completion), giving a pre-trained model. That model is finetuned on high-quality demonstration data (fine-tuned for dialogue), giving the SFT model. The RLHF portion then has two parts: human-feedback comparison data trains a classification step that yields a reward model (trained to give a scalar score for a prompt and response), and prompts are used in reinforcement learning, starting from the SFT model, to optimize responses to maximize reward-model scores, producing the final model. The book notes you can approximate how well a model aligns with human preference by checking which of these steps its creators took (PDF p. 171).

## The Shoggoth analogy (PDF pp. 171-172)
Figure 2-10 resembles the Shoggoth-with-a-smiley-face meme (Figure 2-11):
1. Self-supervised pre-training yields a rogue, untamed monster because it uses indiscriminate internet data (PDF p. 171).
2. Supervised finetuning on higher-quality data, such as Stack Overflow, Quora or human annotations, makes it more socially acceptable (PDF p. 172).
3. Preference finetuning polishes it to be customer-appropriate, like adding the smiley face (PDF p. 172).

## Figure 2-11 (PDF p. 172)
The Shoggoth meme is a hand-drawn image of a large, many-tentacled, many-eyed monster with a toothy maw, labelled "Unsupervised Learning" (the monster itself). A small pink face on one tentacle is labelled "Supervised Fine-tuning", and a yellow smiley face attached to it is labelled "RLHF (cherry on top)". It maps onto the three steps above: the monster is the pre-trained model, and the face and smiley are the thin layers added by SFT and preference finetuning. Source credit in the book: adapted from an image shared by anthrupad.

## Alternatives and trade-offs
The book notes that the combination of pre-training, SFT and preference finetuning is the popular solution for building foundation models today, but not the only one (PDF p. 172). The sentence is split across the row boundary: it continues at the top of the next page, where the book adds that any of the steps can be skipped, as the following sections show; that continuation is outside this row's pages.

## Relations
Follows the model size and scaling discussion (C02-006). SFT and preference finetuning are developed in the sections that follow in Chapter 2; the compute split here connects to the pre-training compute figures in C02-006.
