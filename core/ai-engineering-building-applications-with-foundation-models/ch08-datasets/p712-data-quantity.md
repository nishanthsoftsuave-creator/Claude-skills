---
id: C08-005
title: Data Quantity
source_pages: "712-720"
chapter: 8
concepts: [data-quantity, finetuning-data-size, ossification, peft-vs-full-finetuning, diminishing-returns, performance-gain-curve, task-diversity, annotation-budget]
related: [C08-003, C08-004, C08-006, C07-013, C07-015]
time_sensitive: false
---
# Data Quantity
(Source: PDF pp. 712-720. The Figure 8-1 caption at the very top of PDF p. 712 closes the preceding data-coverage discussion and is not part of this section.)

## What the section covers
How many examples a finetuning dataset needs. The book's answer is that there is no single number: it depends on the finetuning technique, the task's difficulty, and how good the base model already is, in addition to quality and diversity. The section also gives a cheap experimental procedure for estimating how much more data will help, tips for needing less high-quality data, the role of task diversity, and the budget constraint.

## Meaning
- The book compares "how much data do I need" to "how much money do I need": the answer swings enormously between situations (PDF p. 712).
- At one extreme, Jeremy Howard and Jonathan Whitaker ran an experiment showing an LLM can learn from a single example. At the other, some teams finetune with millions of examples (PDF p. 712).
- Even millions is small against what foundation-model training consumes. Llama 2 was trained on 2 trillion tokens and Llama 3 on 16 trillion; at 2,000 tokens per example that equals about 1 billion and 15 billion examples (PDF pp. 712-713).

## Why it matters
Data collection and annotation cost real money and compete with compute for budget, so knowing whether you need 50 examples, 5,000 or millions determines the plan. The section's practical message is to test small first and let measured scaling guide further spending (PDF pp. 715-720).

## How it works

### Should you train from scratch if you have millions of examples?
A note (PDF p. 713) says you can and should evaluate it. Finetuning a pre-trained model is normally more efficient, but with a lot of training data it can do worse, because of ossification: pre-training can effectively freeze the weights so that they adapt poorly to the finetuning data (Hernandez et al., 2021). Smaller models are more prone to ossification than larger ones (PDF p. 713).

### Three factors beyond quality and diversity (PDF pp. 713-714)
1. Finetuning technique. Full finetuning promises the best performance but needs orders of magnitude more data than PEFT methods such as LoRA. With tens of thousands to millions of (instruction, response) pairs, try full finetuning; with only a few hundred or a few thousand, PEFT likely works best.
2. Task complexity. A simple task such as classifying a product review as positive or negative needs far less data than a complex one such as question answering over financial filings.
3. Base model performance. The closer the base model already is to the target quality, the fewer examples are needed. If bigger models are better, big base models need fewer finetuning examples, which is the reverse of pre-training, where bigger models need more data.

### The OpenAI finetuning-guide experiment (Figure 8-2, PDF pp. 714-715)
Five OpenAI models were finetuned on the Stanford Natural Language Inference (SNLI) task. The figure has two bar charts of validation accuracy, one for 100 examples (16 epochs) and one for 550,000 examples (1 epoch), with models ada, babbage, curie, davinci and text-davinci-002.
- With 100 examples, accuracy rises with model sophistication. From my reading of the bars (estimates only): ada roughly 57%, babbage roughly 69%, curie roughly 71%, davinci roughly 80%, text-davinci-002 roughly 88%.
- With 550,000 examples, all five are bunched near 89-93% (estimates), so model choice barely matters.
- The book's explanation for the small-data gap is that the more advanced models already perform better out of the box (PDF p. 714).
- Takeaway stated by the book: with little data, use PEFT on more advanced models; with a lot of data, use full finetuning on smaller models (PDF p. 715).

### Start small
Before investing in a large dataset, build a small, carefully crafted one (for example 50 examples) and see whether finetuning helps. If it does, more data will likely help more. If a small dataset shows no improvement, a bigger one rarely fixes that (PDF p. 715). The book adds a caution: other factors can mask gains, such as a learning rate that is too high or too low, poor data quality, or badly written prompts. In the vast majority of cases, 50-100 examples should already produce visible improvement (PDF p. 716).

### Tip: reduce the high-quality data you need (PDF p. 717)
Finetune first on lower-quality or less relevant data, then on the good data. Three examples:
- Self-supervised to supervised: for legal question answering with few (question, answer) pairs but many legal documents, first finetune self-supervised on the documents, then on the pairs.
- Less relevant to relevant: for product-review sentiment with little product data but much tweet sentiment data, finetune on tweets first, then on product reviews.
- Synthetic to real: for predicting medical conditions from reports, where real data is scarce because of sensitivity, generate lots of synthetic data to finetune first, then finetune on the real data. This is harder, since you run two distinct finetuning jobs and must coordinate the handoff; done badly you can burn more compute and end up with a worse model than simply finetuning on high-quality data.

### Estimate returns by scaling experiments (PDF pp. 717-718)
Finetune on subsets of your current data, such as 25%, 50% and 100%, and plot performance against dataset size. A steep slope means doubling the data should help a lot; a plateau means doubling it gives only a small gain. Figure 8-3 is a schematic curve of model performance against number of examples: a steep segment at the start, labelled "steep performance gain slope," flattening to a labelled plateau for larger sizes. It carries no numeric axis values.

### Diminishing returns (PDF p. 718)
The Figure 8-3 curve is described as typical: the same number of extra examples gives a smaller boost as the dataset grows. Illustration: the first 1,000 examples might add ten accuracy points, the next 1,000 only five.

### Diversity matters as well as count (PDF pp. 718-720)
- Chung et al. (2022), "Scaling Instruction-Finetuned Language Models": performance rose sharply as the number of finetuning tasks went from 9 to 282, began to plateau after 282, yet still improved incrementally up to 1,836 tasks. The conclusion is that exposure to a diverse set of tasks benefits the model greatly (PDF p. 719).
- Figure 8-4 plots normalized average performance on held-out tasks (%) against number of finetuning tasks (x-axis points at 0, 9, 89, 282, 682, 1,836) for 8B, 62B and 540B models. All three curves rise steeply at first and flatten; the larger the model, the higher the curve. Rough estimates from the plot: the 540B model goes from about 49% to about 58%, the 62B from about 28% to about 39%, the 8B from about 6% to about 22% (PDF p. 720).
- Diversity can show up in task types (summarization, question answering), topics (fashion, finance, technology), and expected output formats (JSON, yes/no answers) (PDF p. 719).

### Budget (PDF p. 720)
The amount you use depends on what you can afford, not just what you need. With a $10,000 annotation budget and $2 per example, you can have at most 5,000 examples. Money spent on data is not available for compute, and vice versa, so the two budgets must be balanced.

## When and how to apply
INTERPRETATION: a workflow that follows the book: (1) hand-craft about 50 examples and finetune; (2) if no gain, check hyperparameters, data quality and prompts before concluding finetuning fails; (3) finetune on 25%, 50% and 100% of what you have and read the curve; (4) choose PEFT with a stronger base model when data is small, full finetuning with a smaller model when data is large; (5) cap the target size with the annotation budget.

## Limitations and failure modes
- Full finetuning of a pre-trained model on abundant data may underperform because of ossification, especially for smaller models (PDF p. 713).
- A small experiment can mislead if hyperparameters, data quality or prompts are poor (PDF p. 716).
- Staged finetuning with synthetic or less relevant data can waste compute if mishandled (PDF p. 717).
- Gains from more data of the same kind flatten; adding task diversity continues to help for longer (PDF pp. 718-719).

## Relations
Quality (C08-003) and coverage (C08-004) are the other two parts of the dataset trio; where to get and label the examples is C08-006; synthetic data to raise quantity is C08-008. PEFT versus full finetuning is covered in C07-013 and finetuning workflow tactics in C07-015.
