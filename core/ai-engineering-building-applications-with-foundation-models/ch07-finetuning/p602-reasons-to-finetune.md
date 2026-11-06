---
id: C07-004
title: Reasons to Finetune
source_pages: "602-603"
chapter: 7
concepts: [reasons-to-finetune, structured-outputs, domain-adaptation, bias-mitigation, small-model-finetuning, distillation, grammarly-flan-t5, open-source-models]
related: [C07-003, C07-005, C07-006, C02-014, C08-011]
time_sensitive: false
---
# Reasons to Finetune
(Source: PDF pp. 602-603; the first lines of PDF p. 602 finish the lead-in sentence of C07-003, and the section's last paragraph, about open source models, runs onto the next page)

## What the section covers
The positive case for finetuning: improving model quality (general and task-specific), producing structured outputs, covering specialized or customer-specific data, mitigating bias, and using smaller finetuned (often distilled) models that are cheaper and faster.

## Meaning and why it matters
- The lead-in (C07-003) concluded that finetuning is usually attempted after extensive prompt experiments, and that finetuning and prompting are not mutually exclusive since real-world problems often need both (PDF p. 602).
- The main reason to finetune is better quality, both general capability and task-specific capability. It is commonly used to improve generation of outputs with specific structure, such as JSON or YAML (PDF p. 602).

### Task coverage gaps
- A general-purpose model that scores well on many benchmarks may still do poorly on your task. If the model was not trained enough on your task, finetuning on your data is especially helpful (PDF p. 602).
- SQL example: a model may handle standard SQL well but fail on a less common SQL dialect; finetuning on that dialect helps. Or it may handle common queries in standard SQL yet often fail on customer-specific queries; finetuning on customer-specific queries may help (PDF p. 602).

### Bias mitigation
- If a base model carries biases from its training data, exposing it to carefully curated data during finetuning can counteract them (Wang and Russakovsky, 2023). Example: if a model consistently gives CEOs male-sounding names, finetuning on a dataset with many female CEOs can reduce that (PDF pp. 602-603).
- Garimella et al. (2022): finetuning BERT-like models on text written by women can reduce gender bias, and finetuning on texts by African authors can reduce racial bias (PDF p. 603).

### Small models
- A big model can be finetuned to be better, but finetuning smaller models is much more common. Smaller models need less memory so they are easier to finetune, and they are cheaper and faster in production (PDF p. 603).
- A common approach is finetuning a small model to mimic a larger one using data the large model generated. Since this distills the large model's knowledge into the small one, it is called distillation; Chapter 8 covers it with other data synthesis techniques (PDF p. 603).
- A small model finetuned for a specific task can beat a much larger out-of-the-box model. Example: Grammarly found its finetuned Flan-T5 models (Chung et al., 2022) beat a GPT-3 variant specialized for text editing across many writing-assistant tasks while being 60 times smaller. Finetuning used only 82,000 (instruction, output) pairs, fewer than typically needed to train a text-editing model from scratch (PDF p. 603).

### Open source ecosystem
- Early in the foundation-model era the strongest models were commercial with limited finetuning access, so few competitive models could be finetuned. As the open source community has produced high-quality models of many sizes and domains, finetuning has become much more viable and attractive. This closing paragraph of the section is printed in full on the next page.

## When and how to apply
INTERPRETATION: finetuning is most justified when a specific gap (a rare dialect, customer-specific queries, strict output format, a bias, or the need for a small cheap model) is shown by evaluation, and prompting has not closed it.

## Relations
The counterweight is C07-005 (reasons not to finetune). Structured outputs techniques without finetuning are in Chapter 2 (C02-014); distillation is expanded in C08-011.
