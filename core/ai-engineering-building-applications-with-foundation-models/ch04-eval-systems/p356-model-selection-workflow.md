---
id: C04-008
title: Model Selection Workflow
source_pages: "356-358"
chapter: 4
concepts: [model-selection-workflow, hard-attributes, soft-attributes, public-benchmarks, private-evaluation, monitoring, cost-performance, build-versus-buy]
related: [C04-007, C04-009, C04-010, C04-011]
time_sensitive: false
---
# Model Selection Workflow
(Source: PDF pp. 356-358)

## What the section covers
The two-step selection pattern for each adaptation technique, the distinction between hard and soft attributes, and the four-step iterative evaluation workflow (Figure 4-5), plus a roadmap of what the rest of the chapter covers.

## Meaning
- For each technique, selection generally has two steps: (1) find the best achievable performance; (2) map models on cost versus performance axes and pick the one giving the best performance for the money. The real process is more nuanced (PDF p. 356).
- Hard attributes are things impossible or impractical for you to change. They typically come from provider decisions (licenses, training data, model size) or your own policies (privacy, control). For some use cases they shrink the candidate pool a lot (PDF p. 356).
- Soft attributes can be improved, e.g. accuracy, toxicity, factual consistency. Estimating how much you can improve one is tricky, balancing optimism and realism. The author saw accuracy stuck near 20% on first prompts jump to 70% after splitting the task into two steps, and also saw a model stay unusable after weeks of tweaking, forcing him to give it up (PDF pp. 356-357).
- The hard/soft split depends on both model and use case. Latency is soft if you can access the model and optimize it, but hard if someone else hosts the model (PDF p. 357).

## How it works: the four-step workflow (Figure 4-5)
1. Filter out models whose hard attributes do not fit. The list depends heavily on your internal policies and on whether you will use commercial APIs or host models yourself (PDF p. 357).
2. Use public information such as benchmark results and leaderboard rankings to narrow to the most promising models to try, balancing quality, latency and cost (PDF p. 357).
3. Run experiments with your own evaluation pipeline to find the best model, again balancing all objectives (PDF p. 357).
4. Monitor continually in production to catch failures and gather feedback for improving the application (PDF p. 357).

Figure 4-5, as rendered, shows a left-to-right flow: the build-versus-buy decision (filter by hard attributes), then public benchmarks and leaderboards (public model evaluation), then private prompts and metrics (task-specific evaluation), then monitoring (online evaluation). A bracket over the middle stages is labelled "Balancing" with model quality, cost and latency, and ease of use (PDF p. 358).

## Why it matters and how to apply
- The steps are iterative: later information can overturn earlier decisions. Example: you may begin wanting to host open source models, but after public and private evaluation find they cannot reach the needed performance and switch to commercial APIs (PDF p. 358).

## Relations
Roadmap given by the book: monitoring and user feedback are in Chapter 10; this chapter covers the first three steps. It first addresses API versus self-hosting (C04-009), then how to navigate public benchmarks and why they cannot be fully trusted (C04-010), setting up the final section on designing your evaluation pipeline (C04-011) (PDF p. 358). Preceded by the lead-in C04-007.
