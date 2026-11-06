---
id: WAS-C07-005
title: Identifying Weak Points in Application Architecture - Summary
source_pages: "139-140"
chapter: 7
concepts: [architecture-analysis, recon-prioritization, security-distribution, design-perspective, pattern-spotting]
related: [WAS-C07-001, WAS-C08-001]
time_sensitive: false
---
# Identifying Weak Points in Application Architecture - Summary
(Source: PDF p. 139; PDF p. 140 is blank)

## What the section covers
The chapter's conclusion on why architecture is a recon target.

## Meaning
- Vulnerabilities are usually discussed as code-level problems from badly written code. The book argues that code-level issues can be spotted earlier in the architecture (PDF p. 139).
- An application's design often decides whether it ends up with many security bugs or few, depending on how its defences are designed and spread across the codebase (PDF p. 139).

## Why it matters
- Finding weak points in the architecture is a useful recon technique. Poorly designed features should be examined first when hunting for vulnerabilities, because features with sound security design stay more consistent from endpoint to endpoint and when trying to get past filters (PDF p. 139).
- Architecture is usually discussed at a high level, while most security work happens at a low level, so the topic can be confusing if you are not used to viewing applications from a design angle (PDF p. 139).

## When and how to apply
- While investigating an application, keep its overall security architecture in mind as you build your map of it (PDF p. 139).
- Mastering this analysis focuses your search and may let you spot weak architecture in future features by recognising patterns that produced bugs in earlier ones (PDF p. 139).

## Relations
The notes to be organised are in WAS-C07-001; the whole of Part I is summarised in WAS-C08-001.
