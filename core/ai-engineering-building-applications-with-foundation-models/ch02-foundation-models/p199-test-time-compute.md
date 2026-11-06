---
id: C02-013
title: Test Time Compute
source_pages: "199-205"
chapter: 2
concepts: [test-time-compute, best-of-n, beam-search, verifier, reward-model, sequence-probability, logprob, majority-vote, robustness]
related: [C02-009, C02-012, C02-014, C02-015]
time_sensitive: true
---
# Test Time Compute
(Source: PDF pp. 199-205)

## What the section covers
How a model can sample a whole output instead of one token: generate several candidate responses and select the best. It covers ways to generate candidates, ways to choose among them (probability, reward models and verifiers, heuristics, majority vote), evidence from OpenAI, DeepMind and Stanford, the cost, and uses such as cutting latency. The stopping-condition text at the top of PDF p. 199 belongs to C02-012. The text of the last page ends mid-example (PDF p. 205).

## Meaning
- Test time compute: rather than one response per query, generate multiple responses to raise the chance that a good one is among them (PDF pp. 199-200).
- The previous section covered sampling the next token; this one covers sampling the full output (PDF p. 199).
- Terminology warning: the author uses "test time compute" to match the literature, though early reviewers found it confusing. In research, test time normally means inference because researchers mostly do inference only to test a model. The technique applies to production models too; it is "test time compute" because the number of outputs you can sample depends on the compute you allocate to each inference call (PDF p. 200).

## How it works

### Generating candidates
- Best of N, discussed earlier in the chapter: randomly generate several outputs and pick the best one (PDF p. 200).
- Beam search: a more strategic option than independent generation (which includes many unpromising candidates). At each step of generating the sequence it keeps a fixed number of the most promising candidates, called the beam (PDF p. 200).
- A simple way to make test time compute more effective is to increase output diversity, since a diverse set is more likely to contain a better candidate. When one model generates all options, it is often good practice to vary its sampling variables (PDF p. 200).
- Cost: sampling multiple outputs usually improves performance but is expensive; on average two outputs cost about twice as much as one (PDF p. 200).

### Choosing the best output
- Let users see several outputs and choose, or devise a selection method (PDF p. 201).
- Highest sequence probability. A sequence's probability is the product of the probabilities of its tokens. Example: tokens ["I", "love", "food"] with p(I) = 0.2, p(love given I) = 0.1, p(food given I and love) = 0.3 gives 0.2 x 0.1 x 0.3 = 0.006. The displayed formula is printed as: p(I love food) = p(I) x p(I | love) x p(food | I, ... and is cut off at the right edge of a scrollable code box (PDF p. 201). Note that the printed second factor reads p(I | love), the reverse of the prose, which says the probability of "love" given "I". UNVERIFIED: everything after "p(food | I," is not visible in the PDF.
- INTERPRETATION: the intended formula is p(I) x p(love | I) x p(food | I, love), matching the prose; the printed second factor looks like a typo in the book.
- On the log scale a product becomes a sum, so the logprob of a sequence is the sum of its tokens' logprobs. The printed display reads logprob(I love food) = logprob(I) + logprob(I | l... and is cut off (PDF p. 201). UNVERIFIED: the remaining terms; by the same reasoning as above, INTERPRETATION: logprob(I) + logprob(love | I) + logprob(food | I, love).
- Because logprobs are usually negative (log of values between 0 and 1), longer sequences tend to have a lower total, which biases toward short ones. To avoid that, divide the sum by the sequence length and choose the output with the highest average logprob. At the time of writing this is what the OpenAI API does (PDF pp. 201-202).
- Reward model scoring: score each output and take the best, as discussed in the previous section. Stitch Fix and Grab both pick outputs given high scores by their reward models or verifiers, and Nextdoor found a reward model to be the key factor in improving its application's performance (2023) (PDF p. 202).
- OpenAI trained verifiers to select the best solutions to math problems (Cobbe et al., 2021). Verifiers significantly boosted performance, roughly equal to a 30x increase in model size: a 100-million-parameter model with a verifier could match a 3-billion-parameter model without one (PDF p. 202).
- Application-specific heuristics: pick the shortest candidate if shorter responses suit the application; for natural-language-to-SQL, keep generating until a valid SQL query appears (PDF pp. 204-205).
- Most common output (majority vote): good for tasks with exact answers. For a math problem, solve it several times and take the most frequent answer; for multiple choice, take the most frequent option. Google did this when evaluating Gemini on MMLU, sampling 32 outputs per question, which gave a higher score than a single output (PDF p. 205).

## Why it matters
- DeepMind (Snell et al., 2024) argues that scaling test time compute (more outputs at inference) can be more efficient than scaling model parameters. The paper asks how much an LLM can improve on a hard prompt when given a fixed but nontrivial amount of inference-time compute (PDF p. 202).
- Latency: for some queries, especially chain-of-thought ones, a model can take long to finish. Kittipat Kampa, head of AI at TIFIN, said his team has the model generate several responses in parallel and shows the user the first one that is complete and valid (PDF p. 205).
- Robustness: a model is robust if small input changes do not drastically change its outputs. The less robust the model, the more sampling multiple outputs helps. In a project extracting product information from an image, the model could read the information only half of the ... for the same image. The text of PDF p. 205 ends mid-sentence at "only half of the" and the example continues on the next page, so its conclusion is not recorded here.

## Limitations and failure modes
- Gains from more samples are not unbounded in OpenAI's experiment: performance rose with more outputs only up to 400 outputs, then declined (Figure 2-19). The hypothesis was that more samples raise the chance of finding adversarial outputs that fool the verifier (PDF p. 203). Figure 2-19 (PDF p. 204) is a scatter plot with a connecting line of test solve rate (%) against number of completions per test problem (25, 50, 100, 200, 400, 800, 1600, 3200, log-spaced). Estimated readings of the connecting line, read from the rendered page and not printed values: about 34.6% at 25, 37% at 50, 38.3% at 100, 39% at 200, 39.6% at 400 (the peak), 39.2% at 800, 38.3% at 1600 and 37.2% at 3200. Individual points scatter around the line (for example roughly 38% to 42% at 400, and a single point at 3200).
- A Stanford study ("Monkey Business", Brown et al., 2024) reached a different result: problems solved often grew log-linearly as samples went from 1 to 10,000 (PDF p. 203).
- Practical caveat from the author: nobody in production likely samples 400 or 10,000 outputs per input, because the cost would be astronomical (PDF p. 203).
- Cost: the book states only that two outputs cost about twice as much as one (PDF p. 200). INTERPRETATION: cost therefore grows roughly in proportion to the number of outputs.

## When and how to apply
INTERPRETATION: choose the selection method by task type: exact-answer tasks suit majority vote; tasks with a learned or programmatic quality signal suit a reward model or verifier; format-bound tasks suit validity checks such as valid SQL; interactive tasks with latency limits suit parallel generation returning the first valid result. The book supports each of these examples separately (PDF pp. 202, 204-205).

## Relations
Extends token-level sampling (C02-012) to whole outputs and reuses reward models from preference finetuning (C02-009). Structured-output validity checks connect to C02-014, and output variability to C02-015.

## Time-sensitive statements
- The OpenAI API's use of average logprob is stated as of the writing (PDF p. 202).
- Results cited from OpenAI (2021), DeepMind (2024), Stanford (2024), Nextdoor (2023) and Google's Gemini MMLU evaluation reflect those dates (PDF pp. 202-205).
