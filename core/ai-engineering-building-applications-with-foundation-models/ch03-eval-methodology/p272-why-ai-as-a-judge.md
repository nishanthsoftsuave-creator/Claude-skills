---
id: C03-014
title: Why AI as a Judge?
source_pages: "272-273"
chapter: 3
concepts: [ai-as-judge, reference-free-evaluation, human-agreement, mt-bench, alpacaeval, explainable-judgment, evaluation-cost]
related: [C03-013, C03-011]
time_sensitive: true
---
# Why AI as a Judge?
(Source: PDF pp. 272-273)

## What the section covers
The case for using AI judges: speed, cost, independence from reference data, flexible criteria, agreement with humans, and the ability to explain verdicts.

## Why it matters
- AI judges are fast, easy to use and relatively cheap compared with human evaluators (PDF p. 272).
- They work without reference data, so they can be used in production where no references exist (PDF p. 272).
- They can judge any criterion: correctness, repetitiveness, toxicity, wholesomeness, hallucinations and more, much like asking a person for an opinion on anything (PDF p. 272).
- Trust caveat: people's opinions cannot always be trusted, and neither can an AI's judgments. But since each model aggregates the views of the masses, its judgments can be representative of them. With the right prompt on the right model, judgments on a wide range of topics can be reasonably good (PDF p. 272).

## Adoption and research context (end of the lead-in)
- The LangChain State of AI report (2023) sentence that begins at the bottom of the previous page ends here: 58% of evaluations on their platform were done by AI judges (PDF p. 272). AI as a judge is also an active area of research (PDF p. 272).

## Evidence of agreement with humans
- Zheng et al. (2023) found on their MT-Bench benchmark that GPT-4 agreed with humans 85% of the time, higher than human-to-human agreement (81%) (PDF p. 272).
- The AlpacaEval authors (Dubois et al., 2023) found their AI judges had a near-perfect 0.98 correlation with LMSYS's Chat Arena leaderboard, which is judged by humans (PDF pp. 272-273).

## Explainability and flexibility
- An AI judge can also explain its decision, which helps when auditing evaluation results. The text points to Figure 3-7 as an example of GPT-4 explaining its judgment (PDF p. 273). The figure itself is printed at the top of the following page (outside this row's range, so no page cite is given); viewed on the rendered page, it is a chat screenshot titled "Not only can AI judges score, they also can explain their decisions." The user prompt asks the model to evaluate the quality of a paragraph, give a score from 1 to 5, and explain its decision; the paragraph supplied is the book's own passage about HumanEval and BLEU (higher lexical similarity does not always mean better responses). The model answers "4.5 out of 5" and lists strengths (clarity: it explains the drawback of lexical-similarity scores with a specific example; evidence: it uses the HumanEval benchmark and OpenAI's findings; conciseness) and one area for improvement (flow: the transition between sentences is smooth, but the link between the general statement and the specific example could be slightly stronger). The point: a judge returns a score plus a reasoned justification that can be audited.
- Because it is so flexible, AI as a judge suits many applications, and for some it is the only automatic evaluation option. Even where it is weaker than human judgment, it may be good enough to steer development and give enough confidence to start a project (PDF p. 273).

## Relations
Builds on the introduction in C03-013 and is the alternative to hand-designed similarity metrics in C03-011.

## Time-sensitive statements
The agreement figures (85%, 81%, 0.98) refer to specific 2023 studies, models (GPT-4) and benchmarks (MT-Bench, AlpacaEval, Chat Arena).
