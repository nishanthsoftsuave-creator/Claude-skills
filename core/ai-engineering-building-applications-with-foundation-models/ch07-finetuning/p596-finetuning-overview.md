---
id: C07-002
title: Finetuning Overview
source_pages: "596-600"
chapter: 7
concepts: [finetuning, transfer-learning, sample-efficiency, feature-based-transfer, continued-pre-training, supervised-finetuning, preference-finetuning, infilling-finetuning, long-context-finetuning, code-llama]
related: [C07-001, C07-003, C07-004, C02-008, C02-009, C08-011]
time_sensitive: false
---
# Finetuning Overview
(Source: PDF pp. 596-600; the section ends on the top part of PDF p. 601, above the "When to Finetune" heading, which is cited as the tail page. Figure 7-1 is printed there.)

## What the section covers
What finetuning is conceptually (a form of transfer learning), why it is sample efficient, how it relates to pre-training, the main finetuning variants (self-supervised, supervised, infilling, preference, long-context), the Code Llama example, and who does finetuning.

## Meaning
- You begin with a base model that has some but not all capabilities you need; finetuning aims to make it perform well enough for your task (PDF p. 596).
- Finetuning is one way of doing transfer learning, introduced by Bozinovski and Fulgosi in 1976: knowledge gained on one task accelerates learning on a related new task. The book compares it to a pianist finding another instrument easier to learn (PDF p. 596).
- Early large-scale success: Google's multilingual translation system (Johnson et al., 2016). Having learned Portuguese-English and English-Spanish, it could translate Portuguese to Spanish directly although no Portuguese-Spanish examples were in the training data (PDF p. 596).
- Transfer learning offers a route for tasks where training data is scarce or costly: train a base model on a data-rich task, then transfer to the target task (PDF p. 596).
- For LLMs, what is learned during pre-training on text completion (abundant data) transfers to specialized tasks such as legal question answering or text-to-SQL, which usually have less data. This is what makes foundation models valuable (PDF p. 597).
- Sample efficiency: a sample-efficient model learns well from fewer examples. Training a legal question-answering model from scratch might need millions of examples, whereas finetuning a good base model may need only a few hundred (PDF p. 597).
- Ideally most of what the model needs is already in the base model and finetuning only refines behavior. The InstructGPT paper (2022) suggested seeing finetuning as unlocking capabilities the model already has but that are hard to reach through prompting alone (PDF p. 597).
- Feature-based transfer is a different kind of transfer learning: a model is trained to extract features, usually embedding vectors, that another model then uses. The book mentions this in Chapter 2 (adding a classifier head to part of a foundation model). It is very common in computer vision, where in the second half of the 2010s many people used ImageNet-trained models to extract image features for tasks like object detection or segmentation (PDF p. 598).

## How it works

### Finetuning in the training pipeline
- Finetuning is part of training and extends pre-training. Any training after pre-training counts as finetuning, so it takes many forms. Chapter 2 covered supervised and preference finetuning, recapped here from an application developer's viewpoint (PDF p. 598).
- Pre-training is usually self-supervised, learning from large unlabeled data; for language models this means plain text sequences needing no annotation (PDF p. 598).

### Self-supervised finetuning (continued pre-training)
- Before using expensive task-specific data, you can finetune with self-supervision on cheap task-related data. Examples: raw legal documents before annotated (question, answer) pairs for legal question answering; a large Vietnamese text collection before finetuning for Vietnamese book summarization (PDF pp. 598-599).
- This self-supervised finetuning is also called continued pre-training (PDF p. 599).

### Autoregressive versus infilling
- An autoregressive model predicts the next token from earlier tokens; a masked model fills a blank using tokens before and after it (Chapter 1 terms). Supervised finetuning can likewise train next-token prediction or fill-in-the-blank (PDF p. 599).
- The fill-in-the-blank variant is infilling finetuning, especially useful for text editing and code debugging. A model pre-trained autoregressively can still be finetuned for infilling (PDF p. 599).

### Supervised finetuning
- Self-supervised pre-training gives a rich understanding of the world, but users may find it hard to extract that knowledge, and the model's behavior may not match human preference. Supervised finetuning uses high-quality annotated data to align the model with human usage and preference (PDF p. 599).
- It trains on (input, output) pairs, where the input can be an instruction and the output a response. Responses may be open-ended (book summarization) or close-ended (classification) (PDF pp. 599-600).
- High-quality instruction data is hard and costly to create, particularly where factual consistency, domain expertise or political correctness matters. Chapter 8 covers acquiring instruction data (PDF p. 600).

### Preference finetuning
- A model can be finetuned with reinforcement learning to produce responses that maximize human preference. It needs comparative data, typically in the form (instruction, winning response, losing response) (PDF p. 600).

### Long-context finetuning
- It extends a model's context length and usually needs architecture changes such as adjusting positional embeddings, since longer sequences mean more token positions to handle (PDF p. 600).
- It is harder than other finetuning techniques, and the resulting model may get worse on shorter sequences (PDF p. 600).

### Example: Code Llama (Figure 7-1)
- Figure 7-1 (Rozière et al., 2024) shows how the Code Llama models are made from base Llama 2 (7B, 13B, 34B) through different finetuning steps (PDF p. 600, printed on PDF p. 601).
- From the rendered figure: Llama 2 foundation models go through code training including infilling code training (500B tokens; the infilling step applies to the 7B and 13B models as marked in the figure). A branch continues with long-context finetuning (20B) to yield Code Llama (7B, 13B, 34B). Another branch adds Python code training (100B) then long-context finetuning (20B) to yield Code Llama - Python. Instruction finetuning (5B) applied after long-context finetuning yields Code Llama - Instruct. The token units are as printed in the figure (B for billions).
- Long-context finetuning raised the maximum context length from 4,096 to 16,384 tokens so longer code files fit. In the figure, "instruction finetuning" means supervised finetuning (PDF p. 600).

### Who finetunes
- Both model developers and application developers can finetune. Model developers typically post-train with several techniques before release, and may publish several versions finetuned to different degrees so application developers pick the best fit (PDF p. 601).
- An application developer might finetune a pre-trained model but most likely finetunes an already post-trained one. The more refined the model and the more relevant its knowledge to your task, the less adaptation work is needed (PDF p. 601).

## Relations
Builds on supervised and preference finetuning from Chapter 2 (C02-008, C02-009); instruction data acquisition and distillation appear in Chapter 8 (C08-011). The next section, C07-003, begins the discussion of when to finetune.
