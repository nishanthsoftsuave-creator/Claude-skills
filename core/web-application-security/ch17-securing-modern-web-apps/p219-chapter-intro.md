---
id: WAS-C17-001
title: Securing Modern Web Applications - Chapter Introduction
source_pages: "219"
chapter: 17
concepts: [defense, attack-surface, recon-offense-defense, castle-analogy, prioritization, security-engineer-role, distributed-applications]
related: [WAS-T-003, WAS-C17-002, WAS-C09-002]
time_sensitive: false
---
# Securing Modern Web Applications: Chapter Introduction
(Source: PDF p. 219; the opening paragraphs continue on the next page above the first section heading)

## What the section covers
Why the book turns to defense after recon and offense, and the castle analogy the author uses to explain how a web application is defended and why defenses must be prioritized.

## Why the book is ordered recon, offense, defense
- The earlier techniques for researching, analyzing and breaking into web applications are valuable in their own right and also give insight for the defense part (PDF p. 219).
- Today's applications are more complex and more distributed than older monolithic ones, especially those that rendered pages on the server and allowed little user interaction. That enlarges the surface area available to attack.
- The author argues that understanding the surface area of an application, and how a hacker would map and analyze it, matters for defenders. Knowing the methods hackers use to break in lets a defender prioritize defenses and camouflage the application's architecture and logic from malicious eyes.
- The skills across recon, offense and defense are synergistic: improving mastery of any one makes the use of time more efficient (PDF p. 219).

## The castle analogy
- Defending a web application is compared to defending a medieval castle. The castle's buildings and walls stand for the core application code (PDF p. 219).
- Outside the castle sit buildings that integrate with and support the lord. They stand for the application's dependencies and integrations.
- Because the castle and its surrounding kingdom have a large surface area, the analogy continues on the next page: in wartime it would be infeasible to maximize fortifications at every possible entrance, so defenses have to be prioritized.

## Who does the work (continues on the next page)
The text above the first section heading adds that such prioritization and vulnerability management is usually the job of security engineers in large corporations, or of more generalist software engineers in smaller companies. These professionals act as master defenders: they combine software engineering skill with recon and hacking skill to lower the probability of a successful attack, limit potential damage, and then manage damage that is active or already past. This paragraph is printed on the next page, so it carries no page cite here.

## When and how to apply
INTERPRETATION: when planning defenses, rank entry points by the value of what they expose and by how easy they are to reach, since the book says maximum fortification everywhere is not realistic.

## Relations
Recon techniques from the earlier part supply the map of the surface area (WAS-C09-002). The sections that follow in this chapter walk through the defensive process in order, starting with architecture (WAS-C17-002).
