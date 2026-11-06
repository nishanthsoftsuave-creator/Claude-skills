---
id: C02-012
title: Sampling Strategies
source_pages: "191-198"
chapter: 2
concepts: [sampling-strategies, temperature, logprobs, top-k, top-p, nucleus-sampling, min-p, stopping-condition, softmax]
related: [C02-010, C02-011, C02-013, C02-014, C02-015]
time_sensitive: true
---
# Sampling Strategies
(Source: PDF pp. 191-198, plus the stopping-condition passage on PDF p. 199)

## What the section covers
The common techniques for choosing the next token from the model's probability distribution, and how each one steers a response toward being creative or predictable: temperature, logprobs (as a debugging and application aid), top-k, top-p (nucleus sampling), min-p, and stopping conditions. The page opens with the tail of the softmax definition from the previous section (C02-011).

## Meaning
- Softmax turns logits into probabilities. For a vocabulary of size N and logit vector [x1, x2, ..., xN], the probability of the i-th token is p_i = softmax(x_i) = e^(x_i) / SUM_j e^(x_j), where the sum runs over all N logits (PDF p. 191, formula read from the rendered page; the same expression recurs in the top-k discussion on PDF p. 196).
- The choice of sampling strategy can make a model's answers better suited to an application: one strategy yields more creative answers, another more predictable ones. Many strategies exist, and you can design your own, though that typically needs access to the model's logits (PDF p. 191).
- Logprobs are probabilities expressed on a log scale (PDF p. 195).

## Why it matters
Plain sampling in proportion to the distribution tends to produce bland output. In the book's running color example, common colors have the highest probabilities, so the model sounds like a five-year-old ("My favorite color is green"), while a creative phrasing such as one about "the color of a still lake on a spring morning" starts with a low-probability token ("the") and is rarely produced (PDF pp. 191-192). Strategies below redistribute or restrict the probability mass to fix this, or to cut cost.

## How it works

### Temperature
- Temperature T is a constant that divides the logits before softmax: the adjusted logit is x_i / T, and softmax is applied to the adjusted values (PDF p. 192).
- Intuition: higher temperature lowers the probability of common tokens and raises that of rarer ones, giving more creative responses (PDF p. 192).
- Worked example: a model with two outputs, A and B, with logits [1, 2]. With no temperature (equivalent to T = 1) the probabilities are [0.27, 0.73], so B is chosen 73% of the time. With T = 0.5 they become [0.12, 0.88], so B is chosen 88% of the time (PDF p. 192).
- Higher temperature makes the obvious (highest-logit) value less likely: more creative but potentially less coherent. Lower temperature makes it more likely: more consistent but potentially more boring (PDF p. 193).
- Figure 2-16 plots the A and B probabilities against temperature for logits [1, 2]. As T approaches 0, the probability of B approaches 1, and below about 0.1 the model almost always outputs B. As T rises, A's probability grows and B's shrinks (PDF pp. 193-194). The x-axis runs from 0 to 5; reading the curves, the two lines are about 0.27/0.73 at T = 1 and are still apart at T = 5 (roughly 0.45 for A, 0.55 for B). These curve readings are estimates, not printed values.
- Figure 2-17 (PDF p. 195) is a pipeline diagram: input goes through the neural network to give logits; a softmax step (with temperature marked optional) gives probabilities; a log step gives logprobs.
- Providers typically restrict temperature to the range 0 to 2; if you host the model, any non-negative value works. A value of 0.7 is often recommended for creative use, balancing creativity and predictability, but the book says to experiment to find what suits you (PDF p. 193).
- Setting temperature to 0 is common practice for more consistent outputs. Strictly, temperature cannot be 0 since you cannot divide by 0; in practice, at 0 the model simply picks the largest-logit token, skipping the logit adjustment and softmax (PDF p. 194).

### Logprobs
- A debugging tip: inspect the probabilities the model computes for given inputs. If they look random, the model has not learned much (PDF p. 194).
- Many providers return the model's probabilities as logprobs. The log scale is preferred for neural-network probabilities because it reduces underflow: with a vocabulary of, say, 100,000, many token probabilities are so small that a machine may round them down to 0 (PDF p. 195).
- Figure 2-17 shows the pipeline: logits are computed first, then converted to probabilities (softmax, temperature optional), then to logprobs by taking the log (PDF p. 195).
- Logprobs are useful for building applications (especially classification), for evaluating applications and for understanding how models work internally (PDF p. 195).

### Top-k
- Purpose: cut computation without losing much diversity (PDF p. 196).
- Reason: softmax needs two passes over every candidate, one for the exponential sum and one for each token's e^(x_i) / sum value, which is costly for a large vocabulary (PDF p. 196).
- Method: after the logits are computed, keep only the top-k logits, run softmax over those, and sample from them. Depending on desired diversity, k can range from 50 to 500, far below the vocabulary size. A smaller k gives more predictable but less interesting text, since the model is confined to fewer likely words (PDF p. 196).

### Top-p (nucleus sampling)
- Top-k fixes the number of candidates, but the right number varies with the situation. For "Do you like music? Answer with only yes or no." two candidates (yes, no) are appropriate; for "What's the meaning of life?" many more are (PDF p. 197).
- Top-p adds up probabilities of the most likely next values in descending order and stops once the sum reaches p; only values inside that cumulative mass are considered. Typical p values are 0.9 to 0.95. For example p = 0.9 means the smallest set of values whose cumulative probability exceeds 90% (PDF p. 197).
- Figure 2-18 example probabilities: yes 60%, maybe 31%, no 8%, then tiny values such as "the". With p = 90%, only "yes" and "maybe" are considered (together 91%); with p = 99%, "yes", "maybe" and "no" are (PDF pp. 197-198, figure values read from the rendered page).
- Unlike top-k, top-p does not necessarily lower the softmax workload. Its benefit is that it focuses on the most relevant values per context, so outputs are more contextually appropriate. The book notes that in theory the benefits look small, but in practice it works well and has become more popular (PDF p. 198).
- Min-p is a related strategy: you set the minimum probability a token must have to be considered (PDF p. 198).

### Stopping condition
- An autoregressive model produces tokens one after another. Long outputs take more time, cost more compute (money) and can annoy users, so you may want a rule for stopping (PDF p. 199).
- Simple method: stop after a fixed number of tokens. Downside: output may be cut mid-sentence (PDF p. 199).
- Another method: stop tokens or stop words, for instance stopping on the end-of-sequence token (PDF p. 199).
- These conditions help keep latency and cost down. The downside of early stopping is malformed structured output: when asking for JSON, stopping early can drop closing brackets and make the JSON hard to parse (PDF p. 199).

## When and how to apply
- Use higher temperature (the book cites 0.7 for creative uses) when you want variety; use temperature 0 for consistency (PDF pp. 193-194).
- Pick k (50-500) when computation matters; pick p (0.9-0.95) when the number of sensible candidates varies by prompt (PDF pp. 196-197).
- Use stopping conditions to control latency and cost, but be careful with formatted outputs (PDF p. 199).
- Use logprobs for classification, evaluation and sanity checks of what the model has learned (PDF pp. 194-195).

## Limitations and failure modes
- High temperature risks incoherence; low temperature risks dull, repetitive answers (PDF p. 193).
- A small k limits variety (PDF p. 196).
- Fixed-length stopping truncates sentences; early stopping can break JSON (PDF p. 199).
- Logprob access is restricted: many providers do not expose them, or offer a limited logprobs API, likely for security reasons, since exposed logprobs make a model easier to replicate (PDF pp. 195-196).

## Relations
Builds on sampling fundamentals and the softmax definition (C02-011) and the sampling lead-in (C02-010). Sampling a whole output rather than a token is covered in C02-013, structured outputs (where truncated JSON matters) in C02-014, and the probabilistic nature of generation in C02-015.

## Time-sensitive statements
- That many providers do not expose logprobs or limit the API is stated "as of this writing" (PDF pp. 195-196).
- The provider temperature range of 0 to 2 and the typical value ranges (k of 50-500, p of 0.9-0.95) reflect practice at the time of writing (PDF pp. 193, 196-197).
