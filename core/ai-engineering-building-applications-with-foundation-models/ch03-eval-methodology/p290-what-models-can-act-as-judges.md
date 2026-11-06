---
id: C03-017
title: What Models Can Act as Judges?
source_pages: "290-294"
chapter: 3
concepts: [ai-as-judge, stronger-judge, self-evaluation, weaker-judge, specialized-judge, reward-model, reference-based-judge, preference-model]
related: [C03-014, C03-015, C03-016, C03-018]
time_sensitive: true
---
# What Models Can Act as Judges?
(Source: PDF pp. 290-294, plus the end of the section on PDF p. 295)

## What the section covers
Whether the judge should be stronger than, weaker than, or the same as the model being judged, and the idea of small specialized judges: reward models, reference-based judges and preference models.

## Framing
The judge can be stronger, weaker or equal to the judged model, and each case has pros and cons (PDF p. 290).

## Stronger judge
- Intuition: the exam grader should know more than the exam taker. Stronger models judge better and can also help improve weaker models by guiding them toward better responses (PDF p. 291).
- Why generate with a weaker model at all? Cost and latency. You may lack the budget to generate everything with the strong model, so you use it to judge a subset, for example a cheap in-house model generating and GPT-4 judging 1% of responses (PDF p. 291).
- Latency pattern: a fast model generates while the stronger, slower model judges in the background; if it finds the response bad, remedial action such as replacing the response with the strong model's can follow. The opposite pattern is also common: a strong model generates and a weak model judges in the background (PDF p. 291).
- Two challenges: the strongest model has no eligible judge, and an alternative evaluation method is needed to decide which model is the strongest (PDF p. 291).

## Same model: self-evaluation (self-critique)
- A model judging itself sounds like cheating, especially given self-bias, but it is useful for sanity checks: if a model thinks its own answer is wrong, it may not be very reliable. It can also nudge the model to revise and improve its response (Press et al., 2022; Gou et al., 2023; Valmeekam et al., 2023) (PDF p. 292).
- Example: user asks "What's 10+3?"; first response "30"; self-critique prompt "Is this answer correct?"; final response "No it's not. The correct answer is 13." (PDF p. 292).

## Weaker judge: an open question
- Argument in favor: judging is easier than generating. Anyone can say whether a song is good, but not everyone can write one, so weaker models should be able to judge stronger models' outputs (PDF p. 292).
- Counter-evidence: Zheng et al. (2023) found stronger models correlate better with human preference, which leads people to choose the strongest judge they can afford. But that experiment covered only general-purpose judges (PDF pp. 292-293).

## Small specialized judges
The author is excited about small judges trained for specific judgments, with specific criteria and scoring systems; such a judge can be more reliable than a larger general-purpose one for those judgments. Many uses imply many possible specialized judges; the book gives three (PDF p. 293).
- **Reward model.** Takes a (prompt, response) pair and scores how good the response is for the prompt. Reward models have been used successfully in RLHF for years. Example: Google's Cappy (2023) outputs a 0-1 score of how correct the response is; it is a lightweight scorer with 360 million parameters, far smaller than general-purpose foundation models (PDF p. 293).
- **Reference-based judge.** Evaluates a generated response against one or more references, outputting a similarity or quality score. Examples: BLEURT (Sellam et al., 2020) takes (candidate, reference) and outputs a similarity score; Prometheus (Kim et al., 2023) takes (prompt, generated response, reference response, scoring rubric) and outputs a 1-5 quality score, assuming the reference would get 5 (PDF pp. 293-294).
- **Preference model.** Takes (prompt, response 1, response 2) and says which response users would prefer. The author calls this one of the more exciting directions: predicting human preference opens many possibilities, and preference data, essential for aligning models (Chapter 2), is hard and costly to collect. A good preference predictor can make evaluation easier and models safer. Initiatives include PandaLM (Wang et al., 2023) and JudgeLM (Zhu et al., 2023) (PDF p. 294).

### Figure 3-9 (PandaLM)
A human instruction asks to explain the phrase "With a little give in them" simply, with an example. Response 1 (from Bloom) says they can bend and adapt to different situations; Response 2 (from LLaMA) says it means having a bit of flexibility or room for compromise. PandaLM outputs an evaluation that Response 2 is better because it gives a clear, concise explanation, and also a reference response. The point: the preference model picks a winner and explains its rationale (PDF pp. 294-295).

## Closing remarks
Despite limits, the approach is versatile and powerful, and cheaper judge models make it more so. Many of the author's initially skeptical colleagues have come to rely on it more in production. The next section turns to comparative evaluation, inspired by game design (PDF p. 295).

## When and how to apply
INTERPRETATION: choose the judge by the cost, latency and reliability needs: a strong judge on a sampled subset, a weak judge as a background monitor, self-critique for sanity checks, or a small specialized judge where the judgment is narrow.

## Relations
Cost trade-offs motivating cheaper judges are in C03-016; judge prompting in C03-015; comparative evaluation follows in C03-018.

## Time-sensitive statements
Model names (GPT-4, Cappy, BLEURT, Prometheus, PandaLM, JudgeLM) and the 360-million-parameter size reflect the state of the field when written.
