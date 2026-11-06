---
id: C04-013
title: Step 3. Define Evaluation Methods and Data
source_pages: "400-408"
chapter: 4
concepts: [evaluation-methods, logprobs, human-evaluation, data-slicing, simpsons-paradox, bootstrap, evaluation-set-size, evaluation-pipeline-reliability, experiment-tracking]
related: [C04-012, C04-014]
time_sensitive: false
---
# Step 3. Define Evaluation Methods and Data
(Source: PDF pp. 400-408)

## What the section covers
Step 3 of the evaluation pipeline: choosing evaluation methods per criterion, annotating and slicing evaluation data, deciding how large evaluation sets should be, evaluating the evaluation pipeline itself, and iterating on it. Step 3 begins at the foot of PDF p. 400, noting that criteria and rubrics now exist, so methods and data must be defined (PDF p. 400). The lines above that heading on p. 400 (usefulness threshold, stickiness and engagement metrics) belong to Step 2 (C04-012). The closing lines of the Iterate discussion sit at the top of the next page and are recorded in C04-014.

## Select evaluation methods
- Different criteria may need different methods. Examples: a small specialized toxicity classifier for toxicity; semantic similarity for relevance between response and the user's question; an AI judge for factual consistency between response and the whole context. Unambiguous rubrics and examples are critical for specialized scorers and AI judges (PDF p. 401).
- Methods can be mixed for one criterion: a cheap classifier giving low-quality signals on 100% of data plus an expensive AI judge giving high-quality signals on 1%. This gives some confidence at manageable cost (PDF p. 401).
- Use logprobs when available. They show how confident a model is in a generated token, which is especially helpful for classification. If three class logprobs all sit between 30% and 40%, the model is not confident; if one class has 95%, it is highly confident. Logprobs can also yield a perplexity for generated text, usable for measures such as fluency and factual consistency (PDF p. 401).
- Use automatic metrics as much as possible but do not hesitate to use human evaluation, even in production. Manual expert evaluation of model quality is a long-standing practice in AI. Because open-ended outputs are hard to evaluate, many teams treat human evaluation as the "North Star" metric. Each day experts can evaluate a subset of that day's outputs to spot performance changes or unusual usage; LinkedIn built a process to manually evaluate up to 500 daily conversations (PDF p. 402).
- Plan methods for production as well as experimentation. In experimentation you may have reference data to compare against; in production reference data may not exist, but you have real users. Decide what feedback to want from users, how it correlates with other metrics, and how to use it to improve the application. Collecting feedback is covered in Chapter 10 (PDF p. 402).

## Annotate evaluation data
- Curate annotated examples to evaluate every system component and every criterion, for both turn-based and task-based evaluation. Prefer real production data. Use natural labels if the application has them; otherwise label with humans or AI (AI-generated data is in Chapter 8). Success also depends on rubric clarity, and the evaluation annotation guideline can later become instruction data for finetuning (PDF pp. 402-403).

### Slice your data
- Slicing means splitting data into subsets and examining performance on each separately. The author covered slice-based evaluation at length in her earlier book Designing Machine Learning Systems (PDF p. 403).
- Purposes: avoid biases such as against minority user groups; debug (is poor performance on a subset tied to its length, topic or format?); find improvements (if bad on long inputs, try another processing technique or a model better at long inputs); and avoid Simpson's paradox (PDF p. 403).
- Simpson's paradox: model A beats model B on every subset but loses on the aggregate. Table 4-6 (numbers from Charig et al., 1986, a medical study) shows: Group 1, A 93% (81/87) vs B 87% (234/270); Group 2, A 73% (192/263) vs B 69% (55/80); overall, A 78% (273/350) vs B 83% (289/350). A wins both groups yet is worse overall (PDF pp. 403-404). The book's prose definition of the paradox words the direction the opposite way round (A better on the aggregate, worse on every subset), while its table shows A better on every subset and worse overall; the table is what is recorded here.
  INTERPRETATION: the reversal arises because the two groups are very unevenly represented across the two models (B has 270 cases in Group 1 versus A's 87, and A has 263 in Group 2 versus B's 80), as the table's counts show.
- Keep multiple evaluation sets for different slices: one matching the production distribution for the overall estimate; slices by tier (paying vs free), traffic source (mobile vs web), usage and more; a set of examples where the system often errs; a set where users often err (if typos are common, include typos); and an out-of-scope set of inputs the application should not engage with, to check it handles them properly (PDF p. 404).
- "If you care about something, put a test set on it" (PDF p. 405). Curated evaluation data can later seed synthetic training data (Chapter 8) (PDF p. 405).

## How much data
- An evaluation set should be large enough for reliable results but small enough to be affordable to run (PDF p. 405).
- Bootstrap check for a set of 100: draw 100 samples with replacement from the 100 examples, evaluate the model on them, and repeat many times. If results swing widely (for example 90% on one bootstrap, 70% on another), the pipeline is untrustworthy and needs a bigger set (PDF p. 405).
- Evaluation results are also used to compare systems and decide which model, prompt or other component is better. If a new prompt scores 10% higher, how big must the set be to be sure it is better? In theory a statistical significance test gives the sample size for a confidence level such as 95% if the score distribution is known, but in practice it rarely is (PDF p. 406).
- OpenAI's rough guide (Table 4-7), samples needed for 95% confidence that one system is better: difference of 30% needs about 10; 10% about 100; 3% about 1,000; 1% about 10,000. Rule of thumb: each 3x drop in difference means 10x more samples (PDF p. 406). A chapter footnote (see C04-014) explains the 3.3 factor as the square root of 10.
- References: among benchmarks in Eleuther's lm-evaluation-harness the median size is 1,000 and the mean 2,159. Inverse Scaling prize organizers called 300 examples the absolute minimum, preferring at least 1,000, especially for synthesized examples (PDF p. 407).

## Evaluate your evaluation pipeline
It improves reliability and efficiency, and reliability matters most for subjective methods such as AI as a judge. Questions (PDF pp. 407-408):
- Does it give the right signals? Do better responses get higher scores, and do better metrics lead to better business outcomes?
- How reliable is it? Does running it twice give different results? What variance appears across different evaluation datasets? Aim for reproducibility and low variance, with consistent configuration; for an AI judge, set temperature to 0.
- How correlated are the metrics? Perfectly correlated metrics make one redundant (see benchmark selection and aggregation); uncorrelated metrics mean either an interesting insight or untrustworthy metrics.
- How much cost and latency does it add? Careless evaluation adds significant both; skipping evaluation to cut latency is a risky bet.

## Iterate
- As needs and user behavior change, evaluation criteria will evolve, so the pipeline must be iterated: update the criteria, change the scoring rubric, add or remove examples. Iteration is necessary, but you should still be able to expect a certain level of consistency from the pipeline (PDF p. 408). The rest of this discussion (consequence of constant change, and experiment tracking) is at the top of the following page and is recorded in C04-014.

## Relations
Builds on the criteria and rubrics of C04-012; the chapter wrap-up is C04-014. Related topics elsewhere: user feedback (Chapter 10), data synthesis and annotation (Chapter 8).
