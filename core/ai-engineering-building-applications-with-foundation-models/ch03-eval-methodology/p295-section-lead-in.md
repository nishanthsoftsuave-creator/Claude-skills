---
id: C03-018
title: Ranking Models with Comparative Evaluation (Lead-in)
source_pages: "295-301"
chapter: 3
concepts: [comparative-evaluation, pointwise-evaluation, pairwise-comparison, win-rate, rating-algorithm, elo, bradley-terry, trueskill, chatbot-arena, preference-voting]
related: [C03-016, C03-017, C03-019, C03-020]
time_sensitive: false
---
# Ranking Models with Comparative Evaluation (Lead-in)
(Source: PDF pp. 295-301)

## What the section covers
The introduction to comparative evaluation: how it differs from pointwise evaluation, how matches and win rates work, when preference voting is and is not appropriate, and how rating algorithms turn match outcomes into a ranking that is judged by its predictive power.

## Relation to the preceding AI-as-a-judge material
- The top of PDF p. 295 (the PandaLM example, Figure 3-9, and the author's closing remark that AI as a judge is versatile and powerful) belongs to the earlier AI-as-a-judge row (C03-017); here it matters only as the hand-off: the author says the next approach, comparative evaluation, is "inspired by game design" (PDF p. 295).

## Meaning: pointwise vs comparative evaluation
- Often you evaluate models not for their scores but to find which is best for you, i.e. you want a ranking (PDF p. 296).
- Pointwise evaluation: evaluate each model independently, then rank by score. Analogy: score each dancer individually and pick the highest (PDF p. 296).
- Comparative evaluation: evaluate models against each other and compute a ranking from the comparison results. Analogy: dancers perform side by side and judges pick the one most prefer (PDF p. 296).
- For responses whose quality is subjective, comparative evaluation is usually easier than pointwise: it is easier to say which of two songs is better than to give each a concrete score (PDF p. 296).
- History: in AI, comparative evaluation was first used in 2021 by Anthropic to rank models. It also powers the LMSYS Chatbot Arena leaderboard, which ranks models from scores computed on pairwise community comparisons (PDF pp. 296-297).

## How it works
- Many model providers use it on production traffic. Figure 3-10 (PDF p. 297) shows ChatGPT occasionally asking a user "Which response do you prefer?" with two answers side by side (a code request in the example). The two outputs may come from different models, or from the same model with different sampling variables (PDF p. 297).
- For each request, two or more models are chosen to respond; an evaluator, human or AI, picks the winner. Many developers allow ties so that a winner is not picked at random when two drafts are equally good or equally bad (PDF p. 297).
- Each comparison is called a match (PDF p. 298). The process yields a history of matches; Table 3-5 (PDF p. 299) lists examples with columns for match number, Model A, Model B and winner (e.g. match 1: Model 1 vs Model 2, Model 1 wins; match 2: Model 3 vs Model 10, Model 10 wins; match 3: Model 7 vs Model 4, Model 4 wins).
- Win rate: the probability that model A is preferred over model B, computed as the percentage of matches between A and B that A wins (PDF p. 299).
- With only two models, ranking is easy: the one that wins more often ranks higher. With more models it gets harder. Table 3-6 (PDF p. 300; its last column header, A >> B, is cut off in the PDF, but the caption defines it as the share of matches where A is preferred) gives empirical win rates for five models over 10 pairs, each pair with 1,000 matches. Examples of the figures: Model 1 beats Model 2 in 90% of matches, but beats Model 3 in 40%, Model 4 in 15% and Model 5 in 10%; Model 2 beats Model 3 60%, Model 4 80%, Model 5 80%; Model 3 beats Model 4 70% and Model 5 10%; Model 4 beats Model 5 20%. The text states it is not obvious from this table how the five should be ranked (PDF pp. 299-300).
- A rating algorithm then computes a ranking: typically it first derives a score per model from the comparative signals, then ranks by score (PDF p. 300).

## When and how to apply: preference vs correctness
- Not all questions should be answered by preference; many should be answered by correctness. Example: asking whether cell phone radiation is linked to brain tumors and offering "Yes"/"No" options for voting. Preference-based voting can send wrong signals, and if those are used to train a model, misaligned behavior can result (PDF pp. 297-298).
- Asking users to pick also frustrates them: someone asking a math question because they do not know the answer should not be asked to choose between two different answers (PDF p. 298).
- A key challenge when collecting comparative feedback is deciding which questions can be settled by preference voting. Voting works only if voters are knowledgeable in the subject, so it fits applications where AI is an intern or assistant speeding up tasks users already know how to do, not tasks users cannot do themselves (PDF p. 298).
- Comparative evaluation is not A/B testing: in A/B testing a user sees one candidate model's output at a time, while in comparative evaluation a user sees outputs from several models at once (PDF p. 298).

## Rating algorithms and what a correct ranking means
- Comparative evaluation is new in AI but almost a century old in other industries, notably sports and video games. Rating algorithms from those fields, such as Elo, Bradley-Terry and TrueSkill, can be adapted (PDF p. 301).
- LMSYS Chatbot Arena first used Elo but switched to Bradley-Terry because Elo proved sensitive to the order of evaluators and prompts (PDF p. 301).
- A ranking is correct if, for any model pair, the higher-ranked model is more likely to win against the lower-ranked one: if A ranks above B, users should prefer A over B more than half the time (PDF p. 301).
- Model ranking is therefore a predictive problem: compute a ranking from historical match outcomes and use it to predict future outcomes. Different algorithms may give different rankings and there is no ground truth for the correct ranking; ranking quality is judged by how well it predicts future matches. The author's analysis (in the book's GitHub repo) found Chatbot Arena's ranking good, at least for pairs with enough matches (PDF p. 301).

## Relations
Continues from the AI-as-a-judge sections (C03-016, C03-017). The challenges of comparative evaluation follow in C03-019 and its outlook in C03-020.
