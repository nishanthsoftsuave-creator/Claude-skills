---
id: C03-016
title: Limitations of AI as a Judge
source_pages: "281-289"
chapter: 3
concepts: [ai-as-judge, judge-inconsistency, criteria-ambiguity, judge-cost-latency, self-bias, position-bias, verbosity-bias, spot-checking]
related: [C03-014, C03-015, C03-017, C04-013]
time_sensitive: true
---
# Limitations of AI as a Judge
(Source: PDF pp. 281-289, plus the section's closing paragraphs on PDF p. 290)

## What the section covers
Why many teams hesitate to adopt AI judges, then four families of limitation: inconsistency, ambiguity of criteria, added cost and latency, and biases (self-bias, position bias, verbosity bias), plus privacy/IP concerns and the book's overall verdict.

## Why teams hesitate
Using AI to evaluate AI can seem tautological. The probabilistic nature of AI makes it look too unreliable as an evaluator. Judges can add nontrivial cost and latency. For these reasons some teams treat AI as a judge as a fallback, used when no other way to evaluate exists, especially in production (PDF pp. 281-282).

## Inconsistency
- A trustworthy evaluation method must give consistent results, but judges are probabilistic like every AI application. The same judge on the same input can give different scores if the prompt is worded differently, and even with an identical instruction it can give different scores across two runs. This makes results hard to reproduce or trust (PDF p. 282).
- Consistency can be improved, for example through sampling variables (Chapter 2). Zheng et al. (2023) showed that putting evaluation examples in the prompt raised GPT-4's consistency from 65% to 77.5% (PDF p. 282).
- Caveats: high consistency does not imply high accuracy, since a judge may consistently repeat the same mistakes. More examples also mean longer prompts and higher inference cost; in Zheng et al.'s experiment, adding examples quadrupled the GPT-4 spend (PDF p. 282).

## Criteria ambiguity
- AI-as-judge metrics are not standardized, so they are easy to misread and misuse. At the time of writing, MLflow, Ragas and LlamaIndex each have a built-in "faithfulness" criterion (how faithful an output is to the given context), but with different instructions and scoring systems: MLflow scores 1 to 5, Ragas uses 0 and 1, and LlamaIndex asks for YES or NO (PDF p. 283).
- Table 3-4 contrasts their default prompts (PDF pp. 284-286):
  - MLflow: evaluate faithfulness using only the output and context, ignoring the input; faithfulness is how much of the output is factually consistent with the context; score 1 means none of the claims can be inferred from the context (the other levels are omitted in the table).
  - Ragas: judge the faithfulness of a series of statements against a context; return verdict 1 if a statement can be verified from the context, 0 if not.
  - LlamaIndex: say whether a piece of information is supported by the context, answering YES or NO; answer YES if any of the context supports it even when most of the context is unrelated; includes an example (apple pie is generally double-crusted, supported by the context, answer YES).
- Consequence: the scores from the three tools are not comparable. If a (context, answer) pair gets 3 from MLflow, 1 from Ragas and NO from LlamaIndex, there is no principled way to pick one (PDF p. 286).
- Evolution over time: an application changes, but ideally its evaluation stays fixed so metrics can monitor the change. Judges are AI applications too and can change (PDF p. 286). Example: coherence rose from 90% to 92% month over month, but you cannot say the application improved unless the judges are identical. A better prompt, or a coworker fixing a typo that makes the judge more lenient, could explain the shift (PDF p. 287).
- This is worse when the application and the judge are owned by different teams: the judge team may change the judges without telling the application team, who then attribute the shifts to their own application (PDF p. 287).
- Tip: do not trust any AI judge whose model and prompt you cannot see (PDF p. 287). The author hopes judges become more standardized and reliable as the field matures (PDF p. 287).

## Increased cost and latency
- Judges are used in experimentation and in production; many teams use them as production guardrails, showing users only responses the judge deems good (PDF p. 288).
- Cost: if GPT-4 both generates and judges, you make about twice as many GPT-4 calls, roughly doubling API cost. With three evaluation prompts (for example overall quality, factual consistency, toxicity), calls multiply by four (PDF p. 288).
- Mitigations: use weaker judge models (see C03-017), or spot-check by judging only a subset. Spot-checking can miss failures; evaluating a larger share gives more confidence at higher cost, and finding the balance may take trial and error (revisited in Chapter 4). Overall, AI judges are much cheaper than human evaluators (PDF p. 288).
- Latency: judging before returning a response to the user gives lower risk but higher latency, which may rule the approach out for apps with strict latency requirements (PDF p. 289).

## Biases of AI as a judge
Humans and AI judges are both biased, and different judges have different biases. Knowing them helps you interpret scores and may let you mitigate them (PDF p. 289).
- **Self-bias.** A model favors its own responses over other models'. The mechanism that makes a model produce its most likely response also gives that response a high score. In Zheng et al. (2023), GPT-4 favored itself with a 10% higher win rate and Claude-v1 with a 25% higher win rate (PDF p. 289).
- **First-position bias.** Many models favor the first answer in a pairwise comparison or the first item in a list. Mitigate by repeating the test with different orderings or by carefully designed prompts. This is the opposite of human position bias: humans tend to favor the last answer they see (recency bias) (PDF p. 289).
- **Verbosity bias.** Some judges favor longer answers regardless of quality. Wu and Aji (2023) found GPT-4 and Claude-1 preferred longer (~100 words) responses with factual errors over shorter (~50 words) correct ones. Saito et al. (2023), studying creative tasks, found that when the length difference is large (for instance one response twice as long), the judge almost always picks the longer one. Both studies found GPT-4 less prone than GPT-3.5, suggesting the bias may fade as models strengthen (PDF p. 290).

## Other limitations: privacy and IP
Judges share the limitations of all AI applications. Using a proprietary model as a judge means sending your data to it, and if the provider does not disclose training data you cannot be sure the judge is commercially safe to use (PDF p. 290).

## Overall verdict
Despite the limitations, the author expects adoption to keep growing because of the advantages, but judges should be supplemented with exact evaluation methods and/or human evaluation (PDF p. 290).

## When and how to apply
INTERPRETATION: pin and version the judge model, prompt and sampling settings; randomize answer order in pairwise tests; keep a human or exact-metric check alongside; and budget judge calls per criterion when estimating cost.

## Relations
Builds on the mechanics in C03-015 and the advantages in C03-014. The cheaper-judge option is explored in C03-017. Evaluation pipeline design with judges appears in C04-013.

## Time-sensitive statements
Model names and bias figures (GPT-4, GPT-3.5, Claude-v1, Claude-1; 10% and 25% self-win-rate gaps; 65% to 77.5% consistency) come from 2023 studies. The statement about MLflow, Ragas and LlamaIndex built-in faithfulness prompts is as of the book's writing (PDF p. 283).
