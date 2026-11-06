---
id: C03-021
title: Chapter 3 Summary and Notes
source_pages: "309-314"
chapter: 3
concepts: [summary, evaluation-challenges, language-modeling-metrics, exact-evaluation, ai-as-judge, comparative-evaluation, preference-models, human-evaluation]
related: [C03-016, C03-018, C03-019, C03-020, C04-001]
time_sensitive: false
---
# Chapter 3 Summary and Notes
(Source: PDF pp. 309-314)

## What the section covers
The chapter summary recapping evaluation methodology, followed by the chapter's endnotes (PDF pp. 311-314). A bridge to Chapter 4 follows on the tail page, which belongs to the next chapter and is not summarized here.

## Summary of the chapter
- Stronger models raise the potential for catastrophic failures, so evaluation matters more, yet evaluating open-ended powerful models is hard. That leads many teams to human evaluation. Humans in the loop for sanity checks always help, and often are essential, but this chapter concentrated on automatic approaches (PDF p. 309).
- The chapter began by explaining why foundation models are harder to evaluate than traditional ML models. New evaluation techniques are emerging, but investment in evaluation still trails investment in models and applications (PDF pp. 309-310).
- Many foundation models contain a language model, so the chapter examined language modeling metrics, perplexity and cross entropy. Because many find them confusing, it explained how to interpret them and use them in evaluation and data processing (PDF p. 310).
- It then covered approaches for open-ended responses: functional correctness, similarity scores and AI as a judge. The first two are exact; AI as a judge is subjective (PDF p. 310).
- Subjective metrics depend heavily on the judge, so scores must be read in context of which judge was used; scores for the same quality from different AI judges may not be comparable. AI judges, like all AI applications, are iterated upon, so their judgments change, which makes them unreliable as benchmarks for tracking an application's changes over time. Promising as they are, AI judges should be supplemented with exact evaluation, human evaluation, or both (PDF p. 310).
- Models can be scored independently and ranked by score, or ranked with comparative signals (which of two is better). Comparative evaluation is common in sports, especially chess, and gaining ground in AI (PDF pp. 310-311).
- Both comparative evaluation and post-training alignment need preference signals, which are expensive to collect. This drove the development of preference models, specialized AI judges predicting which response users prefer (PDF p. 311).
- Language modeling metrics and hand-designed similarity measures are old; AI as a judge and comparative evaluation took off only with foundation models. Many teams are still working out how to include them in pipelines. Building a reliable pipeline for open-ended applications is the topic of the next chapter (PDF p. 311).

## Endnotes of the chapter (substantive points)
- Greg Brockman (OpenAI cofounder) tweeted in December 2023 that "evals are surprisingly often all you need" (PDF p. 311).
- An a16z study in 2023 found 6 of 70 decision makers evaluated models by word of mouth (PDF p. 311). Informal evaluation of this kind is also called a vibe check (PDF p. 311).
- When GPT-o1 appeared in September 2024, the Fields medalist Terrence Tao (spelled this way in the book) likened it to "a mediocre, but not completely incompetent, graduate student", predicting one or two iterations to a competent one. People joked that if the brightest minds are needed to evaluate AI, nobody will be qualified to evaluate future models (PDF p. 311).
- The author searched for repositories with at least 500 stars using keywords "LLM", "GPT", "generative" and "transformer", plus crowdsourced additions (PDF p. 312).
- Language modeling performance correlates strongly with downstream performance but does not fully explain it; this is an active research area (PDF p. 312).
- A token may be a character, word or word part. When Claude Shannon introduced entropy in 1951 his tokens were characters; he described entropy as measuring how much information is produced on average per letter, and as the average binary digits per letter under the most efficient encoding (PDF p. 312).
- Natural log is often preferred over log base 2 because its math is easier, e.g. the derivative of ln(x) is 1/x (PDF p. 312).
- SFT and RLHF are explained in Chapter 2; quantization in Chapter 7 (PDF p. 312).
- Complex tasks often have measurable objectives, but AI cannot yet do them end to end, so it may do part of a solution, and evaluating a part can be harder than the end outcome. Chess analogy: the game result (win/lose/draw) is easier to evaluate than one move (PDF p. 312).
- Tokenization processing choices decide whether "cats"/"cat" or "will not"/"won't" count as separate tokens (PDF p. 312).
- A 10,000-element vector seems high-dimensional but is far lower than raw data, so an embedding is a representation in lower dimensions. Models also exist for word embeddings (word2vec, GloVe) rather than document embeddings (PDF p. 313).
- "AI judge" has nothing to do with AI as a judge in court (PDF p. 313).
- In 2017 the author presented MEWR (Machine translation Evaluation metric Without Reference text) at a NeurIPS workshop, using stronger language models to evaluate machine translation, but did not pursue it (PDF p. 313).
- Evaluation can sometimes take most of the budget, more than generating responses (PDF p. 313).
- Spot-checking is the same as sampling (PDF p. 313).
- Saito et al. (2023) found humans also favor longer responses, but far less than AI judges do (PDF p. 313).
- Asking a model to critique its own output is sometimes called self-critique or self-ask (PDF p. 313).
- The BLEURT score range is roughly -2.5 to 1.0, illustrating how score ranges can be arbitrary and criteria ambiguous with AI judges (PDF p. 313).
- One endnote consists only of the example "Such as using a Likert scale"; its anchor sentence (likely about scoring scales for AI judges) is not identifiable from the extracted text, so treat the context as UNVERIFIED (PDF p. 313).
- Chatbot Arena stopped using Elo but for a while still called ratings "Elo scores", scaling Bradley-Terry scores: each score multiplied by 400 and added to 1,000, then rescaled so that Llama-13b has 800 (PDF pp. 313-314).
- As Chatbot Arena grows popular, gaming attempts rise; no one admitted it to the author, but several developers are convinced competitors try (PDF p. 314).

## Relations
Recaps C03-016 (AI judge), C03-018 to C03-020 (comparative evaluation). Leads into Chapter 4 (C04-001).
