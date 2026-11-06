---
id: WAS-C27-008
title: Summary - Securing Third-Party Dependencies
source_pages: "311-312"
chapter: 27
concepts: [chapter-summary, third-party-risk, least-privilege, version-locking, shrinkwrap, risk-mitigation]
related: [WAS-C27-006, WAS-C27-007, WAS-C27-004]
time_sensitive: false
---
# Summary: Securing Third-Party Dependencies
(Source: PDF p. 311; PDF p. 312 is blank)

## What the section covers
The chapter's closing summary, which is printed on the same page as the end of the package management section and starts below it.

## Key points
- A modern web application often has thousands of dependencies, or more, that it needs to work normally. Checking every script in every dependency is a very large job, so any third-party integration is assumed to carry some risk, accepted in exchange for shorter development time (PDF p. 311).
- That risk cannot be removed but can be mitigated in several ways (PDF p. 311).
- Apply the principle of least privilege: let specific dependencies run on their own server, or at least in their own environment with isolated server resources. This limits the damage to the rest of the application if a severe bug is found or a malicious script goes unnoticed. For some dependencies isolation is hard or impossible (PDF p. 311).
- Dependencies tightly integrated with the core application should be evaluated independently at a particular version. If they arrive through a package manager such as npm, they should be version-locked and shrinkwrapped; for extra security, reference Git SHAs or run your own npm mirror. The same techniques apply to similar package managers in other languages (PDF p. 311).
- Closing view: third-party dependencies always carry risk, but careful, thoughtful integration can cut much of the risk the application would otherwise start with (PDF p. 311).

## Wording note
This summary says "least privilege", while the section on separation of concerns used "least authority".
INTERPRETATION: the book appears to use the two terms for the same principle here; it does not say so.

## Relations
Summarizes WAS-C27-004 (automated evaluation), WAS-C27-006 (separation of concerns) and WAS-C27-007 (package management).
