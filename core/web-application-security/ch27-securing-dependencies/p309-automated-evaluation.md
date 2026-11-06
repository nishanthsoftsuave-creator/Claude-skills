---
id: WAS-C27-004
title: Automated Evaluation of Dependency Trees
source_pages: "309"
chapter: 27
concepts: [automated-evaluation, cve-database, snyk, npm-list, tree-data-structure, nist-database, dependency-scanning]
related: [WAS-C27-003, WAS-C15-009, WAS-C27-005]
time_sensitive: true
---
# Automated Evaluation of Dependency Trees
(Source: PDF p. 309)

## What the section covers
Why a large dependency tree has to be evaluated by automation, and the simplest automated check the book gives: comparing the tree against a well-known vulnerability database.

## Meaning and why it matters
- An application whose dependency chain holds ten thousand items cannot properly be evaluated by hand, so the tree must be evaluated by automated means, with other techniques added on top to protect the integrity of what is relied upon (PDF p. 309).

## How it works
- If the dependency tree can be loaded into memory and modeled as a tree-like data structure, walking through it is simple and surprisingly efficient (PDF p. 309).
- When a dependency is added to the first-party application, it and all of its sub-dependency trees should be evaluated, and the evaluation should be automated (PDF p. 309).
- The easiest way to start finding vulnerabilities is to compare the application's tree with a well-known CVE database. Such databases hold lists, and reproductions, of vulnerabilities in well-known open source and third-party packages that are often integrated into first-party applications (PDF p. 309).
- Two routes are named: download a third-party scanner (the book gives Snyk as the example), or write a small script that turns the dependency tree into a list and compares it with a remote CVE database. In the npm world a starting point is `npm list --depth=[depth]` (PDF p. 309).
- Several databases can be used; the book suggests starting with NIST's, since it is funded by the US government and likely to remain for a long time (PDF p. 309).

## Limitations
The book says other techniques should be used in addition, but does not name them on this page (PDF p. 309).
INTERPRETATION: a comparison against a database can only find vulnerabilities that have already been reported.

## Time-sensitive statements
The Snyk reference, the `npm list` command form and the statement about the NIST database being government funded reflect the time of writing.

## Relations
Follows WAS-C27-003; the public vulnerability database is described in WAS-C15-009; the integration techniques that come next are in WAS-C27-005.
