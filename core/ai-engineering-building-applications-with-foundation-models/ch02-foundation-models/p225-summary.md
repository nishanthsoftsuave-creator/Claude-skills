---
id: C02-016
title: Chapter 2 Summary and Notes
source_pages: "225-231"
chapter: 2
concepts: [chapter-summary, training-data, transformer, scaling-law, post-training, sampling, probabilistic-models, evaluation-pipeline]
related: [C02-001, C02-006, C02-009, C02-011, C02-015, C03-001]
time_sensitive: true
---
# Chapter 2 Summary and Notes
(Source: PDF pp. 225-231)

## What the section covers
The chapter's closing summary, and the chapter's endnotes that follow it (PDF pp. 228-231). The notes are listed by content below because their numbering is garbled in the extracted text.

## The summary
- Scope: the chapter covered core design decisions in building a foundation model. Since most people use ready-made models rather than train from scratch, the author skipped detailed training mechanics in favor of modeling factors that guide which model to use and how (PDF pp. 225-226).
- Training data: a key driver of performance. Large models need large data, expensive and slow to get, so providers use whatever is available. Such models do well on tasks represented in the data, which may not include yours. Hence curating data to build models for specific languages (especially low-resource ones) and domains is often needed (PDF p. 226).
- Architecture and size: before training comes architecting. Transformer dominates language foundation models; the chapter covered the problems it was designed to solve and its limitations (PDF p. 226).
- Scale: measured by three numbers: parameters, training tokens, and training FLOPs. Model size and data size drive compute needs. The scaling law gives the best number of parameters and tokens for a compute budget. Scaling bottlenecks were examined; scaling up currently tends to improve a model, but how long that holds is an open question (PDF pp. 226-227).
- Post-training: low-quality data and self-supervised pre-training can yield outputs that miss what users want. Post-training addresses this with supervised finetuning and preference finetuning. Human preference is diverse and cannot be captured by one formula, so existing solutions are far from foolproof (PDF p. 227).
- Sampling: how models generate output tokens, one of the author's favorite topics. It makes models probabilistic, which suits creative tasks and fun conversation (ChatGPT, Gemini) but also causes inconsistency and hallucinations (PDF p. 227).
- Direction: work with models means building workflows around their probabilistic nature. The rest of the book aims to make AI engineering, if not deterministic, at least systematic. The first step is a solid evaluation pipeline to detect failures and unexpected changes; evaluation is so crucial that two chapters are devoted to it, starting next (PDF p. 227).

## The chapter notes (content only)
Tokenization and bias (PDF p. 228):
- A study titled "GPT-4 Can Solve Math Problems - but Not in All Languages" (Yennie Jun) can be checked with OpenAI's Tokenizer.
- Possible reason for weaker Chinese performance: bias in pre-training or alignment data; perhaps less Chinese or China-centric material was included.
- A Washington Post piece (2023) on websites that make AI sound smart.
- For text, domain keywords can serve as heuristics to analyze data domains; for images there are no obvious heuristics, and most vision-dataset analyses cover sizes, resolutions or video lengths.
- Training fundamentals are out of scope; self-supervision (a model generates its own labels) is in Chapter 1 and backpropagation (updating parameters from error) in Chapter 7.
- RNNs suffer vanishing and exploding gradients because of their recursion: small gradients shrink toward zero through repeated multiplication, large ones grow exponentially, destabilizing learning.
- Bahdanau et al. is cited for the attention-based translation work.
- Because tokens are processed in batches, the input vector has shape N x T x 4096 (N batch size, T sequence length), and each resulting K, V, Q vector is also N x T x 4096.

Architecture and compute notes (PDF pp. 228-229):
- Simple activation functions work for large models: researchers once raced to design sophisticated ones, but fancier ones did not work better. The model just needs a nonlinearity to break the linearity of the feedforward layers, and cheaper functions save compute and memory.
- Fun fact: Ilya Sutskever is first author of the seq2seq paper and second author of the AlexNet paper.
- Sutskever's argument on why beating existing architectures is hard: neural networks simulate many programs, and gradient descent searches over those programs for the best one for the task. So a new architecture could possibly be simulated by existing ones; to win, it must simulate programs the existing ones cannot (talk at Simons Institute, 2023).
- The transformer was originally designed by Google to run fast on TPUs and only later optimized for GPUs.
- Memory figures in the chapter are lower bounds; actual memory is higher, and Chapter 7 shows how to compute model memory usage.
- A book is assumed to be about 50,000 words or 67,000 tokens.
- Large models are typically pre-trained on one epoch of data, as of writing.
- FLOP/s are measured in FP32; floating point formats are in Chapter 7.
- As of writing, cloud H100s cost roughly $2 to $5 per hour, expected to fall as compute gets cheaper.
- Jascha Sohl-Dickstein visualized which hyperparameters work and which do not (on his X page).

Scaling, alignment and sampling notes (PDF p. 230):
- Dario Amodei said that if the scaling hypothesis is true, a $100 billion model would be as good as a Nobel prize winner.
- AI content is multiplied by easy machine translation: generate an article, then translate it into many languages (Thompson et al., 2024, "A Shocking Amount of the Web Is Machine Translated").
- A friend's analogy: a pre-trained model talks like a web page, not a human.
- RL basics are out of scope; the highlight is that RL optimizes against hard objectives such as human preference.
- Misaligned models can sometimes be useful, e.g. building one that is excellent at fake news to gauge how convincing AI misinformation could be.
- The author's informal picture of temperature: higher temperature makes the distribution more chaotic, letting lower-probability tokens surface.
- Greedy choice is an arg max.
- Underflow: a number too small for the format is rounded to zero.
- At writing, the OpenAI API shows logprobs only for up to the 20 most likely tokens; it stopped letting users get logprobs for arbitrary text in September 2023; Anthropic does not expose logprobs.
- Paid model APIs often charge per output token.

Test-time compute and structured-output notes (PDF p. 231):
- Costs of generating several outputs per input can be cut, e.g. process the input once and reuse it.
- At writing, OpenAI's API had a best_of parameter (say 10) returning the output with the highest average logprob among that many outputs.
- Wang et al. (2023) named the vote-over-samples approach self-consistency.
- For a brittle model, the optimal move is to swap it for another.
- Share of correctly generated JSON objects observed ranges from 0% to the high 90s depending on application and model.
- Training from scratch on data in the target format works too but is out of scope.
- Some finetuning services add a classifier head automatically; OpenAI's once allowed it but the feature was disabled at writing.
- Meme: chances are low but never zero.
- In December 2023 the author reviewed three months of customer support requests at an AI company he advised and found one fifth concerned handling model inconsistency. In a July 2023 panel with Drew Houston (Dropbox) and Harrison Chase (LangChain), all agreed hallucination is the biggest blocker for many enterprise use cases.

## Relations
Recaps all of Chapter 2: data and architecture (C02-001 to C02-006), post-training (C02-009), sampling (C02-011), and probabilistic problems (C02-015). Evaluation, the next step, begins in C03-001.

## Time-sensitive statements
H100 rental prices, API logprob limits and the best_of parameter, one-epoch pre-training, the disabled classifier-head feature, and the 0%-to-high-90s JSON success range all reflect the book's writing date.
