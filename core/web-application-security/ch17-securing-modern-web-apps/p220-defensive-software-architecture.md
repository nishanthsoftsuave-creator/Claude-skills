---
id: WAS-C17-002
title: Defensive Software Architecture
source_pages: "220"
chapter: 17
concepts: [defensive-architecture, data-flow, architecture-phase, threat-modeling, re-architecture-cost, data-in-transit]
related: [WAS-C17-001, WAS-C17-003, WAS-C18-001]
time_sensitive: false
---
# Defensive Software Architecture
(Source: PDF p. 220)

## What the section covers
The first step of building a well-fortified web application: the architecture phase, which comes before any software is written, and why architectural security problems are cheapest to fix at that point.

## Meaning
- The architecture phase is the stage of a new product or feature where attention goes to the data that flows through the application (PDF p. 220).
- The author reduces software engineering to the efficient movement of data from point A to point B. In the same spirit, security engineering is the efficient securing of that data in transit and wherever it rests before, after or during the transit.

## Why it matters
- It is much easier to find and fix deep architectural security flaws before the software is written and deployed (PDF p. 220).
- After an application has been adopted by users, the depth at which a re-architecture can be done to close a security gap is usually limited.
- The effect is strongest in applications that consumers build on. Web applications that let users open their own stores or run their own code are costly to re-architect, because a deep change may force customers to redo time-consuming manual work.

## How it will be taught
The following chapters teach techniques for judging the security of an application's architecture, ranging from analysis of data flow to threat modeling for new features (PDF p. 220).

## When and how to apply
INTERPRETATION: run a data-flow review of each new feature before coding starts, noting where data enters, travels, rests and leaves, and ask what protects it at each step.

## Relations
This is the first stage in the defensive sequence introduced in WAS-C17-001. The next stage is the review of each commit (WAS-C17-003). The chapter on secure architecture (WAS-C18-001) works the idea through a concrete example.
