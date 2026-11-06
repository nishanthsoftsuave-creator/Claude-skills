---
id: C03-019
title: Challenges of Comparative Evaluation
source_pages: "302-307"
chapter: 3
concepts: [comparative-evaluation, scalability, transitivity, matching-algorithm, crowdsourcing, quality-control, leaderboard, win-rate, absolute-performance, cost-benefit]
related: [C03-018, C03-020, C03-016]
time_sensitive: false
---
# Challenges of Comparative Evaluation
(Source: PDF pp. 302-307)

## What the section covers
Three challenges of comparative evaluation: scalability bottlenecks, lack of standardization and quality control, and the gap between comparative and absolute performance.

## Why it matters
With pointwise evaluation the hard part is designing the benchmark and metrics; computing scores to rank is easy. With comparative evaluation, both gathering signals and ranking models are hard (PDF p. 302).

## 1. Scalability bottlenecks
- Comparative evaluation is data-intensive; the number of model pairs grows quadratically with the number of models. In January 2024, LMSYS evaluated 57 models with 244,000 comparisons. 57 models make 1,596 pairs, so that is only about 153 comparisons per pair, few given the breadth of tasks (PDF p. 302).
- Mitigation by transitivity: ranking algorithms usually assume that if A beats B and B beats C, then A beats C, so A versus C need not be compared directly (PDF p. 302).
- Caveat: it is unclear that transitivity holds for AI models. Papers analyzing Elo for AI (Boubdir et al.; Balduzzi et al.; Munos et al.) list it as a limitation, arguing human preference is not necessarily transitive. Non-transitivity can also arise because different pairs are judged by different evaluators on different prompts (PDF p. 303).
- New models: independent (pointwise) evaluation needs only the new model scored. Comparative evaluation must match the new model against existing ones, which can change the existing ranking (PDF p. 303).
- Private models: if you build a model from internal data and want to compare it with public ones, you probably need to collect your own comparative signals and build your own leaderboard, or pay a public leaderboard to run a private evaluation (PDF p. 303).
- Better matching algorithms help. So far models were assumed to be paired randomly so every pair gets about equal matches, but not all pairs need equal comparison. Once the outcome for a pair is confident, stop matching them. An efficient matcher samples the matches that reduce overall ranking uncertainty the most (PDF pp. 303-304).

## 2. Lack of standardization and quality control
- LMSYS Chatbot Arena crowdsources: anyone enters a prompt, gets two anonymous responses, votes, and only then are model names revealed. Benefits: a wide range of signals and relative resistance to gaming. Downside: standardization and quality control are hard to enforce (PDF p. 304).
- Problems, first group:
  - Anyone can use any prompt and there is no standard for a better response. Volunteers may not fact-check, so they may prefer responses that sound better but are wrong (PDF p. 304).
  - Preferences differ (polite and moderate vs unfiltered). That captures real human preference but it may not suit every use case; e.g. a user may downvote a model that refuses an inappropriate joke while an application developer would prefer the refusal. Some users may even maliciously choose toxic responses and pollute the ranking (PDF pp. 304-305).
- Problems, second group: crowdsourced comparison happens outside users' working environments, without real-world grounding. People use the first prompts that come to mind, rarely sophisticated prompting techniques (PDF p. 305).
  - Among 33,000 prompts LMSYS published in 2023, 180 were "hello" or "hi", 0.55% of the data, not counting variants such as "hello!", "hola", "hey". There are many brainteasers; one ("X has 3 sisters, each has a brother. How many brothers does X have?") appeared 44 times (PDF p. 305).
  - Simple prompts are easy to answer and do not separate models; too many of them can pollute the ranking (PDF p. 305).
  - A public leaderboard without sophisticated context construction (e.g. adding documents retrieved from your internal databases) will not reflect how a model works in your RAG system, since generating good responses differs from retrieving the most relevant documents (PDF p. 305).
- Ways to impose standardization:
  - Restrict users to predetermined prompts, at the cost of diversity of use cases. LMSYS instead allows any prompt, then uses its internal model to filter out hard prompts and ranks models on only those (PDF p. 306).
  - Use only trusted evaluators trained on the comparison criteria and on realistic prompts and advanced prompting. Scale does this for its private comparative leaderboard; the downside is expense and far fewer comparisons (PDF p. 306).
  - Embed comparison in your own product so users judge models inside their workflow, e.g. two code snippets offered in a code editor. Many chat apps already do this. Caveats: users may not know which is better, may not read both options and click randomly, adding noise; yet signals from the small share who vote correctly can still suffice to tell which model is better (PDF p. 306).
  - Some teams prefer AI evaluators: not as good as trained human experts but possibly more reliable than random internet users (PDF p. 307).

## 3. From comparative to absolute performance
- Often a model just has to be good enough, not the best. Comparative evaluation says which is better, not how good it is or whether it suffices (PDF p. 307).
- If B beats A, any of three scenarios may hold: B good and A bad; both bad; both good. Other forms of evaluation are needed to tell which (PDF p. 307).
- Example: model A resolves 70% of customer support tickets; model B wins against A 51% of the time. It is unclear how a 51% win rate converts to the number of requests B can resolve. Several practitioners told the author a 1% change in win rate can give a huge gain in some applications and a minimal one in others (PDF p. 307).
- Swapping A for B involves more than human preference, such as cost. Not knowing the expected performance boost blocks cost-benefit analysis; if B costs twice as much, comparison alone cannot decide whether the gain is worth it (this closing point continues onto the next page, which belongs to the following row).

## Evaluation and success criteria
INTERPRETATION: combine comparative results with pointwise or exact metrics on your own task, since the book says other evaluation forms are needed to establish absolute quality (PDF p. 307).

## Relations
Builds on the setup in C03-018 (matches, win rates, rating algorithms); the benefits that offset these limits are in C03-020. The AI-evaluator alternative links to AI as a judge (C03-016).
