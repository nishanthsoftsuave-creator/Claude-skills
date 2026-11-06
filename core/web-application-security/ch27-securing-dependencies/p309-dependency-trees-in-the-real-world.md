---
id: WAS-C27-003
title: Dependency Trees in the Real World
source_pages: "309"
chapter: 27
concepts: [dependency-tree, version-mismatch, vulnerable-version, per-version-evaluation, subdependencies, scale-of-dependencies]
related: [WAS-C27-002, WAS-C27-004, WAS-C15-009]
time_sensitive: false
---
# Dependency Trees in the Real World
(Source: PDF p. 309)

## What the section covers
The same jQuery example as in the previous subsection, now with version numbers, to show that each unique dependency and each unique version has to be evaluated.

## How it works: the example with versions
As printed, the three paths are run together on one line (PDF p. 309):
- Primary Application v1.6 depends on jQuery 3.4.0.
- Primary Application v1.6 depends on SPA Framework v1.3.2, which depends on jQuery v2.2.1.
- Primary Application v1.6 depends on UI Component Library v4.5.0, which depends on jQuery v2.2.1.

## Why it matters
- Version 2.2.1 of a dependency can have critical vulnerabilities while version 3.4.0 has none, so the book says each unique dependency, and each unique version of each one, must be evaluated (PDF p. 309).
- Scale: an application with a hundred third-party dependencies can have a tree spanning thousands, or even tens of thousands, of unique sub-dependencies and versions (PDF p. 309).

## Relations
This follows the modeling example in WAS-C27-002; the automated approach to evaluating such a large tree is WAS-C27-004. Public vulnerability records that can be checked against these versions are covered in WAS-C15-009.
