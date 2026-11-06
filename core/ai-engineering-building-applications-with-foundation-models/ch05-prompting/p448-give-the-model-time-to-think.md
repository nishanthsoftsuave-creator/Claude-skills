---
id: C05-010
title: Give the Model Time to Think
source_pages: "448-451"
chapter: 5
concepts: [chain-of-thought, cot-prompting, zero-shot-cot, one-shot-cot, self-critique, self-eval, latency-cost-tradeoff, hallucination-reduction]
related: [C05-009, C05-011, C03-010, C05-007]
time_sensitive: false
---
# Give the Model Time to Think
(Source: PDF pp. 448-451; tail PDF p. 452 holds the end of Table 5-4, the self-critique paragraph and the latency caveat, all cited below. The top of PDF p. 448 finishes the GoDaddy example of C05-009 and is not covered here)

## What the section covers
Two techniques that push a model to spend more effort, loosely "thinking", before answering: chain-of-thought (CoT) prompting and self-critique prompting. It presents evidence for CoT (Figure 5-6), variations of CoT prompts (Table 5-4), self-critique, and the shared latency and cost downside.

## Meaning
- CoT: explicitly ask the model to think step by step, which nudges it toward a more systematic way of solving the problem. It is among the first prompting techniques that worked well across models, introduced in "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models" (Wei et al., 2022), almost a year before ChatGPT appeared (PDF p. 448).
- Self-critique: asking the model to check its own outputs, also called self-eval (discussed in Chapter 3). Like CoT it nudges the model to think critically about the problem (PDF p. 452).

## Why it matters: evidence
- Figure 5-6 (from Wei et al., 2022, spanning PDF pp. 449-450) shows CoT improving LaMDA, GPT-3 and PaLM on three math benchmarks: GSM8K, SVAMP and MAWPS. It is a 3-by-3 grid of line charts, one row per benchmark and one column per model family; the x axis is model scale in billions of parameters (LaMDA 0.4, 8 and 137; GPT 0.4, 7 and 175; PaLM 8, 62 and 540) and the y axis is solve rate in percent. Each panel has a black line for standard prompting, a blue line for CoT prompting and a dashed orange horizontal line for the best prior supervised result (PDF p. 449).
- Reading the chart (all values are my approximate visual estimates; the book prints no per-point numbers, and the chart has more plotted points than labelled ticks, so only the largest-model points are read here): CoT gives little or no gain at the smallest scales and the gains appear at the largest sizes. GSM8K: the prior supervised best is about 55%; GPT-3 at 175B rises from roughly 15% (standard) to roughly 47% (CoT); PaLM at 540B rises from roughly 18% to roughly 57%, slightly above the prior best line; LaMDA at 137B stays low (about 7% to about 14%). SVAMP: the prior best is about 47%; LaMDA 137B goes from roughly 30% to 37%; GPT-3 175B is about 66% vs 69% and PaLM 540B about 69% vs 74%, so the large models pass the prior best with standard prompting already, and CoT adds only a few points. MAWPS: the prior best is about 88%; LaMDA 137B goes from roughly 43% to 58%; GPT-3 175B from about 73% to 87%; PaLM 540B from about 79% to 93%, the one panel where CoT exceeds the prior best (PDF p. 449). The caption (PDF p. 450) expands the benchmark names as MAWPS (Math Word Problem Solving), SVAMP (given there as "sequence variation analysis, maps, and phylogeny", which looks like a mis-expansion in the book) and GSM-8K, and credits the image to Wei et al., 2022 (CC BY 4.0).
- The book also notes that LinkedIn found CoT reduces hallucinations (PDF p. 448).

## How it works
- Simplest CoT: add "think step by step" or "explain your decision" to the prompt and let the model decide its steps. Alternatively spell out the steps to follow, or include examples of what the steps look like. Which variation works best depends on the application (PDF p. 450).
- Table 5-4 uses the question "Which animal is faster: cats or dogs?" and shows four variants (PDF pp. 451-452):
  1. Zero-shot CoT: append "Think step by step before arriving at an answer."
  2. Zero-shot CoT: append "Explain your rationale before giving an answer."
  3. Zero-shot CoT: give explicit steps: find the speed of the fastest dog breed, find the speed of the fastest cat breed, decide which is faster.
  4. One-shot CoT: include one worked example for a different question, "Which animal is faster: sharks or dolphins?", whose steps give the shortfin mako shark at about 74 km/h, the common dolphin at about 60 km/h, and the conclusion that sharks are faster; then the real question is asked (PDF pp. 451-452).

## Limitations and failure modes
- Like decomposition, CoT and self-critique can raise the latency users perceive: the model may run several intermediate steps before the first visible output token. This is hardest when the model devises the steps itself, since the sequence can be long, causing higher latency and possibly prohibitive cost (PDF p. 452).

## When and how to apply
Try a one-line zero-shot CoT first, then explicit steps or an example if needed; add a self-critique pass where checking quality matters; weigh the added tokens and wait time against accuracy gains. INTERPRETATION: when latency is tight, prefer prescribed short steps over letting the model invent a long plan.

## Relations
Shares the latency trade-off with task decomposition (C05-009); self-eval is treated in Chapter 3 (C03-010 is the AI-as-judge material). Next: iterating on prompts (C05-011).
