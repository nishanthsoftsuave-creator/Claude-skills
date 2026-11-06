---
id: C03-020
title: The Future of Comparative Evaluation
source_pages: "308"
chapter: 3
concepts: [comparative-evaluation, human-preference, benchmark-saturation, gaming, leaderboards, ab-testing, offline-evaluation, online-evaluation]
related: [C03-018, C03-019, C03-021]
time_sensitive: false
---
# The Future of Comparative Evaluation
(Source: PDF p. 308, continuing on PDF p. 309)

## What the section covers
After listing many limitations, the author argues comparative evaluation still has a future, and gives its benefits.

## Reasons it will endure
1. Comparing is easier than scoring. As covered under post-training, people find it easier to compare two outputs than to assign each a concrete score. As models surpass human performance, humans may be unable to score responses at all, but may still tell which of two is better, so comparison may be the only option left. The Llama 2 paper (Touvron et al., 2023) reported that when the model writes beyond the best human annotators' ability, humans can still give valuable feedback by comparing two answers (PDF p. 308).
2. It targets what we care about, human preference. This eases the pressure to keep building new benchmarks to match growing capabilities. A benchmark becomes useless once models reach perfect scores, but comparative evaluation never saturates as long as newer, stronger models keep arriving (PDF pp. 308-309).
3. It is hard to game: there is no easy way to cheat such as training on reference data. Therefore many trust public comparative leaderboards more than other public leaderboards (PDF p. 309).
4. It gives discriminating signals about models that cannot be obtained otherwise. Offline, it is a good addition to benchmarks; online, it complements A/B testing (PDF p. 309).

## Relations
Weighs against the challenges in C03-019; the setup is in C03-018; the chapter summary (C03-021) restates comparative evaluation's role.
