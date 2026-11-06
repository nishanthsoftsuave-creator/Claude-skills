---
id: C03-002
title: Challenges of Evaluating Foundation Models
source_pages: "234-239"
chapter: 3
concepts: [evaluation-challenges, open-ended-outputs, ground-truth, black-box-models, benchmark-saturation, general-purpose-models, evaluation-investment, eyeballing]
related: [C03-001, C03-003, C03-009, C03-013]
time_sensitive: true
---
# Challenges of Evaluating Foundation Models
(Source: PDF pp. 234-239)

## What the section covers
Why evaluating foundation models is harder than evaluating traditional ML models, evidence that evaluation research and tooling still lag behind the rest of AI engineering, and the consequence that many teams only eyeball results. The section ends by committing the book to a systematic approach.

## Lead-in text at the top of p. 234 (closes the chapter intro)
AI as a judge, using AI to evaluate AI responses, is called the rising star of subjective evaluation. It is subjective because the score depends on the judge model and prompt. It is gaining rapid traction in industry but meets intense opposition from those who think AI is not trustworthy enough for the task (PDF p. 234).

## Meaning
- Evaluating ML models was always hard; foundation models make it harder, for several separate reasons (PDF p. 234).
- A benchmark becomes saturated for a model once the model reaches the perfect score (PDF p. 235).

## Why it is harder: five reasons
1. Smarter models are harder to evaluate. Most people can see that a first grader's math is wrong; few can check PhD-level math. A gibberish book summary is easy to condemn, but a coherent one may require having read the book (PDF p. 234). A corollary: evaluation of sophisticated tasks costs much more time, since you can no longer judge by how a response sounds and must fact-check, reason, and bring in domain expertise (PDF pp. 234-235).
2. Open-endedness breaks the ground-truth approach. Traditional ML tasks are mostly close-ended: a classifier can only emit the expected categories, so predicted category Y when X was expected is plainly wrong. For an open-ended task one input has many correct responses, so a complete list of correct outputs cannot be curated for comparison (PDF p. 235).
3. Foundation models are mostly black boxes, either because providers withhold details or because application developers lack the expertise to interpret them. Architecture, training data and training process reveal much about strengths and weaknesses; without them you can only evaluate by watching outputs (PDF p. 235).
4. Public benchmarks have proven inadequate. Ideally a benchmark covers the full range of capabilities and evolves as AI advances, yet benchmarks saturate fast (PDF pp. 235-236). Examples: GLUE appeared in 2018 and saturated within a year, prompting SuperGLUE in 2019; NaturalInstructions (2021) was replaced by Super-NaturalInstructions (2022); MMLU (2020), a strong benchmark relied on by many early foundation models, was largely replaced by MMLU-Pro (2024) (PDF p. 236).
5. The scope of evaluation has widened. For a task-specific model you measure performance on its trained task. For a general-purpose model you must also discover new tasks it can do, possibly beyond human ability, so evaluation takes on the added job of exploring the potential and limits of AI (PDF p. 236).

## Signs of progress (the good news)
- New challenges have produced many new methods and benchmarks. Figure 3-1 (from Chang et al., 2023) shows the number of LLM-evaluation papers growing exponentially month by month in the first half of 2023, from about 2 papers a month to almost 35 (PDF pp. 236-237).
- The author's own analysis of the 1,000 most-starred AI repositories on GitHub found over 50 devoted to evaluation as of May 2024; plotted by creation date, the count grows in an exponential-looking curve (Figure 3-2) (PDF p. 237). Figure 3-2 is a cumulative area chart of evaluation repositories by month, starting near zero in 2016, about 5 by 2020, about 20 by early 2023, and levelling at about 40 by 2024; the plotted maximum (about 40) is lower than the text's 'over 50', which the book does not reconcile (PDF p. 238). Figure 3-1 is a line chart: roughly 0 papers in 2020, about 3 in 2021 and 2022, 2 in January 2023, then rising each month to about 33 for June 2023 and later (PDF p. 237).

## Limitations and failure modes: underinvestment (the bad news)
- Interest in evaluation still trails interest in the rest of the AI engineering pipeline (PDF p. 237).
- Balduzzi et al. of DeepMind wrote that developing evaluations "has received little systematic attention compared to developing algorithms"; experiment results are almost solely used to improve algorithms and rarely to improve evaluation (PDF p. 238).
- Anthropic called on policymakers to increase government funding and grants, both for new evaluation methods and for analyzing how robust existing evaluations are (PDF p. 238).
- Figure 3-3, built from the same top-1,000 GitHub list, shows evaluation tools being few compared with tools for modeling and training and for AI orchestration (PDF pp. 238-240). It is a horizontal bar chart of repository counts by category: modeling and training about 120, AI orchestration about 78, inference optimization about 49, prompt engineering about 47, AI interface about 45, agent about 44, and evals the smallest at about 40 (PDF p. 240).
- Inadequate investment yields inadequate infrastructure, making systematic evaluation hard. Asked how they evaluate their applications, many people said they just eyeball results, or they keep a small set of go-to prompts whose selection is ad hoc and rests on the curator's personal experience instead of the application's needs (PDF p. 239).

## When and how to apply
The ad hoc approach may be tolerable while getting a project started but is not enough for iterating on an application, and the book therefore takes a systematic approach to evaluation (PDF p. 239).

## Relations
Follows the chapter framing in C03-001. Language modeling metrics come next (C03-003); exact evaluation (C03-009) and AI as a judge (C03-013) are the book's methods for the open-ended problem described here.

## Time-sensitive statements
Benchmark replacement dates (GLUE/SuperGLUE, NaturalInstructions, MMLU/MMLU-Pro), the 2023 paper-count trend, and the May 2024 count of over 50 evaluation repositories reflect the time of writing (PDF pp. 236-237).
