# Evaluation plan: <project or feature>

The plan is written before the system is built (Architect mode) or before it is judged (Review & Test), because without agreed criteria nothing can be called good or bad.

## 1. What is evaluated

Every component and the system as a whole, since a failure can hide in any one of them. For each: its job and how it can fail.

## 2. Criteria

| Criterion | Why it matters here | Metric or rubric | Threshold | Source of the threshold |
|---|---|---|---|---|
| Domain capability | | | | |
| Generation quality (factual consistency, safety, fluency as relevant) | | | | |
| Instruction following and format compliance | | | | |
| Cost | | | | |
| Latency (time to first token, total, throughput as relevant) | | | | |

Add criteria the use case needs. A threshold without a reason is a guess; say where it came from.

## 3. Methods

For each criterion, how it is measured: exact checks (functional correctness, matching against reference data), similarity measures, AI judge with a written rubric (state the judge model, the prompt, and how the judge itself is checked), comparative evaluation, or human review. Give the reason for each choice and its known limits.

## 4. Data

- The evaluation set: size, how it was built, how it covers real usage and edge cases, how it is kept separate from tuning data, how it is refreshed.
- Slices that must be reported separately (user segments, languages, difficulty, failure-prone inputs).

## 5. Evaluation guideline

Written rules that let two reviewers score the same output the same way: definitions, examples of pass and fail, how ties and ambiguous cases are handled.

## 6. Execution

When each evaluation runs (before release, on every change, in production sampling), who owns it, the budget it needs, and what happens when a threshold is missed.

## 7. Reliability of the evaluation itself

Noise and variance (repeat runs), judge bias and drift, contamination of the evaluation set, and how each is monitored.
