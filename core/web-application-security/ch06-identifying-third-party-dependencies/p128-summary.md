---
id: WAS-C06-008
title: Identifying Third-Party Dependencies - Summary
source_pages: "128-130"
chapter: 6
concepts: [third-party-dependencies, attack-surface-shift, integration-risk, dependency-evaluation, security-skill]
related: [WAS-C06-001, WAS-C15-010, WAS-C27-008]
time_sensitive: false
---
# Identifying Third-Party Dependencies - Summary
(Source: PDF pp. 128-129; PDF p. 130 is blank)

## What the section covers
The chapter's closing argument: third-party code has become a leading attack vector and finding and judging it is a core skill.

## Meaning
- For many years the source code most often attacked was the organisation's own first-party code. That is changing because modern applications depend heavily on third-party and open source integrations (PDF p. 128).
- Understanding a target's third-party integrations may expose security holes that are ripe for exploitation. These flaws are often hard for the application's owner to detect (PDF p. 129).

## Why it matters
- Knowing how third-party dependencies are used in your own codebase lets you reduce risk that comes from sloppy integration or from weaker libraries when safer options exist (PDF p. 129).
- Underneath most applications sits so much code that integrating third-party software is nearly mandatory; building a whole full stack web application from nothing would be a heroic effort. The book concludes that knowing how to find and evaluate dependencies is becoming a must-have skill for anyone in the security industry (PDF p. 129).

## What the chapter covered
INTERPRETATION: as a recap, the chapter showed how to detect SPA frameworks through globals and attributes (WAS-C06-002), helper libraries and stylesheets by listing script and link elements (WAS-C06-003, WAS-C06-004), server packages by headers and default pages (WAS-C06-005, WAS-C06-006) and databases by primary key shapes (WAS-C06-007).

## Relations
Exploitation is developed in WAS-C15-010, and defence in WAS-C27-008.
