---
id: WAS-C18-008
title: Secure Application Architecture - Summary
source_pages: "235-236"
chapter: 18
concepts: [architecture-review, cost-of-late-fixes, re-architecture, migration-plan, security-flaws, security-engineer, bad-publicity]
related: [WAS-C18-001, WAS-C18-007, WAS-C17-002]
time_sensitive: false
---
# Secure Application Architecture: Summary
(Source: PDF pp. 235-236; the second page carries no text)

## What the section covers
The chapter's closing argument for treating architecture as the best moment to catch security problems, and the reasons late fixes cost so much more.

## Main points
- Many concerns must be weighed when building an application. When a product organization develops a new application, a skilled security engineer or architect should analyze its design and architecture (PDF p. 235).
- Deep flaws, such as a weak authentication scheme or a half-baked integration with a search engine, can leave the application exposed to risk that is not easy to resolve. Once paying customers depend on the application in their workflows, and especially once contracts are signed, fixing architecture-level bugs becomes a daunting task.
- The author repeats the NIST estimate from the start of the chapter: a flaw found in the architecture phase can cost 30 to 60 times less to fix than one found in production.

## Why late fixes cost more
The book lists four contributing factors (PDF p. 235):
- Customers may rely on insecure functionality, so the team has to build a secure equivalent and give them a migration plan to avoid downtime.
- Deep architectural flaws may force rewriting many modules besides the insecure one. The example is a complex 3D video game with a flawed multiplayer module: fixing it can mean rewriting not just the networking module but the game modules built on top of it, especially if an underlying technology must be swapped to improve security, such as moving between UDP and TCP networking.
- The flaw may already have been exploited, costing real money on top of engineering time.
- The flaw may be published, causing bad publicity that costs engagements and customers who leave.

## Conclusion
The ideal phase for finding and resolving security concerns is always the architecture phase. Removing issues there saves money in the long run and avoids the trouble of outside discovery or publication later (PDF p. 235).

## When and how to apply
INTERPRETATION: when a flaw is found in a live product, estimate the migration cost to existing customers as well as the engineering cost, since the book counts both.

## Relations
Closes the chapter that began with feature analysis (WAS-C18-001). It repeats the point made about early architecture review in WAS-C17-002.
