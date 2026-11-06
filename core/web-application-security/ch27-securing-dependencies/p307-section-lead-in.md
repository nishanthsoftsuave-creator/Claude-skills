---
id: WAS-C27-001
title: Securing Third-Party Dependencies - Evaluating Dependency Trees (Lead-in)
source_pages: "307"
chapter: 27
concepts: [third-party-dependencies, fourth-party-dependencies, dependency-tree, npm-ls, manual-review-limits, defensive-integration]
related: [WAS-C27-002, WAS-C15-006, WAS-C15-009]
time_sensitive: false
---
# Securing Third-Party Dependencies: Evaluating Dependency Trees (lead-in)
(Source: PDF p. 307, with the continuation on PDF p. 308)

## What the section covers
The opening of Chapter 27: how it connects to the earlier parts of the book, and why a third-party dependency cannot be judged in isolation, because dependencies bring dependencies of their own.

## Where the chapter fits
- Part I (recon) taught how to spot third-party dependencies inside a first-party web application; Part II (offense) looked at the ways such dependencies get integrated and how those integrations can be attacked (PDF p. 307).
- Part III is about defense, so this chapter turns to protecting an application from the vulnerabilities that integration with third-party code can introduce (PDF p. 307).

## Meaning
- A dependency of a dependency is called a fourth-party dependency (PDF p. 307).
- The dependencies of the application, their dependencies, and so on down the chain form a dependency tree (PDF p. 307).

## Why it matters
- Reviewing the source of one third-party dependency that has no fourth-party dependencies is feasible, and a manual code-level review is the ideal choice in many cases (PDF p. 307).
- Manual reviews do not scale. Comprehensively reviewing a dependency that relies on fourth-party dependencies is often impossible, and more so when those carry further dependencies of their own (PDF p. 307).

## How it works: listing the tree
- In a project managed with npm, the command `npm ls` prints the whole dependency tree. The book calls it powerful for seeing how many dependencies the application really has, since the sub-dependencies are not something developers think about regularly (PDF pp. 307-308).
- Figure 27-1 (printed at the top of the next page, so it is described here with its page cite) is a terminal screenshot of such a tree: nested package names with version numbers, some entries tagged "deduped". The visible entries include a font-icon package for the Ember framework with its own sub-packages, and several broccoli build packages (PDF p. 308).
- The book then notes why trees matter beyond security: they let the overall application's code be evaluated, which can bring a large reduction in file and memory size (PDF p. 308).

## Relations
Modeling and versions of the tree follow in WAS-C27-002 and WAS-C27-003; the package manager background is in WAS-C15-006 and the public vulnerability database in WAS-C15-009.
