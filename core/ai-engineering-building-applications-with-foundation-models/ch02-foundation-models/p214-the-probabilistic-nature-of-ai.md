---
id: C02-015
title: The Probabilistic Nature of AI
source_pages: "214-224"
chapter: 2
concepts: [probabilistic, deterministic, inconsistency, hallucination, self-delusion, snowballing-hallucination, mismatched-knowledge, rlhf, temperature-seed]
related: [C02-011, C02-012, C02-008, C02-009, C02-016, C04-004, C05-007, C06-012]
time_sensitive: true
---
# The Probabilistic Nature of AI
(Source: PDF pp. 214-224, plus the closing text on the tail page, PDF p. 225)

## What the section covers
Why models that sample their answers are probabilistic, and the two resulting problems: inconsistency and hallucination. It gives mitigations for inconsistency and two competing hypotheses, with proposed remedies, for why hallucination happens.

## Meaning
- Because models sample responses, they are probabilistic. Asked the same question twice, a friend answers the same way, but a model may not (PDF pp. 214-215).
- Example: if a model rates Vietnamese cuisine 70% and Italian 30% as the world's best, it answers Vietnamese about 70% of the time and Italian about 30% (PDF p. 215).
- Deterministic is the opposite: the outcome follows with no random variation (PDF p. 215).
- Inconsistency: very different responses to the same or slightly different prompts. Hallucination: a response not grounded in facts (PDF p. 215).
- Illustration: if an essay claiming US presidents are aliens were in the training data, the model could probabilistically say the current president is an alien; to a skeptic, that is making things up (PDF p. 215).
- Foundation models aggregate the opinions of the masses; anything with non-zero probability, however wrong, can be generated (PDF p. 215).

## Why it matters
- This trait makes AI applications both exciting and challenging; much AI engineering aims to harness and mitigate it (PDF p. 215).
- It suits creative tasks, since creativity means exploring beyond common paths. AI is a good sidekick for brainstorming and new designs, but the same trait is a pain elsewhere (PDF p. 216).

## Inconsistency
Two forms (PDF p. 216):
1. Same input, different outputs.
2. Slightly different input (for example an accidentally capitalized letter), drastically different output.

Example: the author used ChatGPT to score essays; the same prompt run twice gave 3/5 and 5/5 (PDF pp. 216-217). Figure 2-23 (rendered) shows the prompt (a critical, unbiased writing professor asked to score an essay from 0 to 5 in the format "Essay score: {score} / 5", followed by an essay about a student named Lana) branching into a first response of 3/5 and a second of 5/5 (PDF p. 217).

Impact: inconsistency produces a jarring experience; users expect consistency as they do from people, like someone giving a different name each time you meet (PDF p. 217).

Mitigations for same-input-different-output (PDF p. 217):
- Cache the answer and return it for repeat questions.
- Fix sampling variables: temperature, top-p, top-k.
- Fix the seed, the starting point of the random number generator used for sampling.

Limits: even with all fixed there is no guarantee of 100% consistency, because hardware affects the result (different machines execute instructions differently and handle different numeric ranges). Hosting yourself gives some control; with an API provider such as OpenAI or Google, control is theirs (PDF pp. 217-218). Fixing settings is good practice but does not inspire trust, like a teacher who grades consistently only in one room (PDF p. 218).

The second scenario is harder. Fixing generation settings will not make different inputs give the same output. Carefully crafted prompts (Chapter 5) and a memory system (Chapter 6) can move responses closer to what you want (PDF p. 218).

## Hallucination
- Fatal for tasks that rely on facts, e.g. explaining a vaccine's pros and cons (PDF p. 218). In June 2023 a law firm was fined for submitting fictitious legal research prepared with ChatGPT (PDF p. 218).
- Not new: hallucination in text generation was mentioned as early as 2016 (Goyal et al.), and detecting and measuring it has been a staple of natural language generation since. This section explains causes; detection and measurement come in Chapter 4 (PDF p. 219).
- Inconsistency comes from sampling randomness, but hallucination is subtler. Sampling picks among probable options, so how does something never seen become probable? Models may output things believed absent from training data, which cannot be verified since the data cannot be combed through; building something too complex to understand is "both a blessing and a curse" (PDF p. 219).
- Eliminating hallucination requires understanding it; there are two hypotheses (PDF p. 219).

### Hypothesis 1: self-delusion
- Raised by Ortega et al. at DeepMind (2021): the model cannot differentiate between data it is given and data it generates (PDF p. 220).
- Example: prompt "Who's [a named person]?"; the model's first sentence is "[That person] is an architect." The next token is conditioned on the question plus that sentence, so the model treats its own output like a given fact and can build outrageous falsehoods on it. The authors call hallucination a form of self-delusion (PDF p. 220).
- Figure 2-24 (rendered): given a photo of a shampoo bottle and the prompt to read the exact ingredients from the label, LLaVA-v1.5-7B stated the product was a bottle of milk and listed nine milk-like ingredients (milk, vitamin D, vitamin A, calcium, phosphorus, potassium, sodium, chloride, protein) (PDF pp. 220-221).
- Zhang et al. (2023) call this snowballing hallucinations: after a wrong assumption the model keeps hallucinating to justify it. Such assumptions can make it fail questions it would otherwise answer correctly (PDF p. 221). Figure 2-25 (rendered): asked whether 9677 is prime, the model wrongly says no and claims 9677 = 13 x 745; in a separate session, asked whether 9677 is divisible by 13, GPT-4 correctly says no (PDF p. 222).
- DeepMind's two mitigations (PDF pp. 222-223): from reinforcement learning, make the model distinguish user prompts (observations about the world) from its own tokens (its actions); from supervised learning, include factual and counterfactual signals in training data.

### Hypothesis 2: mismatch between model and labeler knowledge
- First argued by OpenAI researcher Leo Gao. In SFT the model imitates labeler-written responses. If those use knowledge the model lacks, we effectively teach it to hallucinate. In theory labelers could include the knowledge behind each response so the model learns to use only what it knows, but this is impossible in practice (PDF p. 223).
- John Schulman (OpenAI co-founder, UC Berkeley talk, April 2023) shared the view and believes LLMs know whether they know something, "a big claim". If true, forcing answers from known information would fix hallucinations (PDF p. 223). His two proposals: verification (ask the model to retrieve the sources behind each response) and reinforcement learning, noting that reward models learn only from comparisons (A better than B) with no reason given, so a reward function penalizing fabrication more could help (PDF p. 223).
- Schulman said OpenAI found RLHF reduces hallucination, but the InstructGPT paper shows RLHF worsened it (PDF p. 224). Figure 2-26 (rendered; values for GPT, SFT, InstructGPT in that order): Hallucinations, measured on OpenAI's API prompt distribution (lower is better) 0.414, 0.078, 0.172; "Customer Assistant Appropriate", also API prompts (higher is better) 0.811, 0.880, 0.902; TruthfulQA (higher is better) 0.224, 0.206, 0.413; RealToxicity (lower is better) 0.233, 0.199, 0.196. Scores are combined across model sizes (PDF p. 224). Despite worse hallucination, RLHF improved other aspects and labelers overall preferred the RLHF model over SFT alone (PDF p. 224).

### Prompt-level mitigation and combining the hypotheses (tail page)
- Assuming a model knows what it knows, some add prompts like "Answer as truthfully as possible, and if you're unsure of the answer, say, 'Sorry, I don't know.'" (PDF p. 225).
- Asking for concise responses seems to help: fewer tokens means fewer chances to make things up (PDF p. 225).
- Prompting and context construction (Chapters 5 and 6) can also help (PDF p. 225).
- The hypotheses complement: self-delusion concerns how self-supervision causes hallucinations; mismatched knowledge concerns how supervision causes them (PDF p. 225).
- If it cannot be stopped, detection would help, but detecting is hard, like spotting a human lying. Chapter 4 covers detection and measurement (PDF p. 225).

## Limitations and failure modes
Fixed settings cannot guarantee consistency (hardware), cannot handle input-wording sensitivity, and hallucination has no complete fix; the evidence on RLHF is mixed (PDF pp. 217-224).

## Relations
Sampling mechanics (temperature, top-p, top-k, seeds) are in C02-011 and C02-012. SFT and RLHF are in C02-008 and C02-009. The chapter wrap-up is C02-016. Hallucination evaluation is in Chapter 4 (C04-004); prompting in C05-007; memory in C06-012.

## Time-sensitive statements
The June 2023 law-firm fine, the April 2023 Schulman talk, and the model-specific results (GPT-4, LLaVA-v1.5-7B, InstructGPT) reflect the state at the book's writing.
