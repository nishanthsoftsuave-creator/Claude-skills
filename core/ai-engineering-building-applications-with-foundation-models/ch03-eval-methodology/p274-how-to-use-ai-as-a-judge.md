---
id: C03-015
title: How to Use AI as a Judge
source_pages: "274-280"
chapter: 3
concepts: [ai-as-judge, judge-prompt, scoring-system, built-in-criteria, pairwise-comparison, reference-comparison, judge-as-system]
related: [C03-013, C03-014, C03-016, C03-017, C03-011]
time_sensitive: true
---
# How to Use AI as a Judge
(Source: PDF pp. 274-280, plus the end of the section on PDF p. 281)

## What the section covers
The three basic ways to prompt a model to make judgments, the kinds of criteria a judge can apply (including the built-in criteria shipped by evaluation tools), what a judge prompt must contain, which scoring systems work best, a real prompt excerpt from Azure AI Studio, and the closing point that a judge is a system (model plus prompt), not just a model.

## Opening illustration (Figure 3-7)
The page preceding the section heading ends with a screenshot in which a chat model is asked to rate a paragraph from 1 to 5 and explain its decision. The paragraph is about the drawback that higher lexical similarity does not always mean a better response (the HumanEval/BLEU example). The model returns 4.5 out of 5, lists strengths (clarity, evidence, conciseness) and one area for improvement (flow between the general statement and the example). The caption's point: AI judges can both score and explain their decisions (PDF p. 274).

## Meaning: three ways to use a judge
The book offers deliberately naive example prompts for three modes (PDF pp. 274-276):
1. **Single-response quality, given the original question.** The prompt supplies the question and the answer and asks for a score from 1 to 5, with 1 meaning very bad and 5 very good (PDF pp. 274-275).
2. **Generated response versus a reference response.** The judge is asked whether the generated answer is the same as the reference and must output True or False. The book frames this as an alternative to human-designed similarity measurements (PDF p. 275).
3. **Two generated responses compared.** The judge decides which is better, or predicts which one users will prefer, and outputs A or B. This is useful for producing preference data for post-training alignment, for test-time compute (both from Chapter 2), and for ranking models by comparative evaluation (the next section of the chapter) (PDF pp. 275-276).

## Flexible criteria
A general-purpose AI judge can be asked to assess a response against any criterion. Examples from the book: for a roleplaying chatbot, "Does this response sound like something Gandalf would say?"; for an app producing promotional product photos, rating from 1 to 5 how trustworthy the product looks in the image (PDF p. 276).

## Built-in criteria in tools (Table 3-3, time-sensitive)
As of September 2024 (the table's own date stamp), tools offered these built-in criteria (PDF p. 277):
- Azure AI Studio: groundedness, relevance, coherence, fluency, similarity.
- MLflow.metrics: faithfulness, relevance.
- LangChain Criteria Evaluation: conciseness, relevance, correctness, coherence, harmfulness, maliciousness, helpfulness, controversiality, misogyny, insensitivity, criminality.
- Ragas: faithfulness, answer relevance.
The book warns that these lists will change as the tools evolve (PDF p. 277).

Key caveat: AI-as-judge criteria are not standardized. Azure AI Studio's relevance score may be very different from MLflow's, because each score depends on the judge's underlying model and its prompt (PDF p. 277).

## How it works: what a judge prompt must state
Prompting a judge is like prompting any AI application. The prompt should clearly explain (PDF pp. 277-278):
1. **The task**, for example evaluating the relevance between a generated answer and the question.
2. **The criteria** to follow, for example focusing on whether the generated answer holds enough information to address the question according to the ground-truth answer. The more detailed the instruction, the better.
3. **The scoring system**, one of:
   - Classification, such as good/bad or relevant/irrelevant/neutral.
   - Discrete numerical values, such as 1 to 5; these are a special case of classification where each class has a numeric rather than semantic meaning.
   - Continuous numerical values, such as 0 to 1, for example when measuring a degree of similarity.

### Tip on scoring systems (PDF p. 278)
- Language models are generally better with text than numbers, and AI judges are reported to work better with classification than numerical scoring.
- Among numerical systems, discrete scoring seems to work better than continuous.
- Empirically, the wider the discrete range, the worse the model gets; typical discrete scales run from 1 to 5.
- Prompts containing examples perform better. With a 1-5 scale, include examples of what a 1, 2, 3, 4 and 5 look like and, if possible, why each gets its score. Prompting best practices are deferred to Chapter 5.

## Worked example: Azure AI Studio relevance prompt
The book shows part of Azure's relevance prompt (partly omitted for brevity). It contains the task (score relevance between a generated answer and the question, based on the ground-truth answer, on a 1-5 range, and give the reason), the criterion (does the generated answer contain sufficient information to address the question according to the ground truth), the scoring system, a low-score example, and the justification for that low score (PDF pp. 279-280). The example: for the question "Is the sky blue?", ground truth "Yes, the sky is blue.", a generated answer "No, the sky is not blue." contradicts the ground truth, so it gets a score of 1-2, and the reason given should name that contradiction (PDF pp. 280-281). This illustrates all four ingredients: task, criteria, scoring system, and a scored example with rationale.

## Figure 3-8: the judge as a pipeline
The figure shows an "AI judge" box. The object to be evaluated, a (question, answer) pair, is inserted into a prompt template for the criterion (the 1-5 quality prompt with placeholders for question and answer, ending in "Score:"). The resulting final prompt goes to a model (GPT-4 in the figure), which outputs a score (PDF p. 281).

## Key conclusion
An AI judge is not just a model; it is a system comprising a model and a prompt. Changing the model, the prompt or the sampling parameters produces a different judge (PDF p. 281). This sets up the reproducibility and comparability problems discussed in C03-016.

## When and how to apply
INTERPRETATION: when building a judge, write the prompt with all four elements (task, criteria, scoring system, scored examples), prefer a classification or a small discrete scale, and record the exact model, prompt and sampling settings, since these define the judge.

## Relations
Follows the motivation in C03-014 and the section lead-in C03-013; the alternative similarity metrics it can replace are in C03-011. Weaknesses are in C03-016; choice of judge model is in C03-017.

## Time-sensitive statements
Table 3-3 of built-in criteria is dated September 2024 and will change as the tools change (PDF p. 277). Tool and model names (Azure AI Studio, MLflow, LangChain, Ragas, GPT-4) reflect the time of writing.
