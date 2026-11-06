---
id: WAS-C23-004
title: Anti-CSRF Coding Best Practices
source_pages: "282"
chapter: 23
concepts: [csrf-mitigation, secure-design, stateless-get, application-wide-defense, request-checking-middleware, design-phase-security]
related: [WAS-C23-005, WAS-C23-006, WAS-C23-003]
time_sensitive: false
---
# Anti-CSRF Coding Best Practices (lead-in)
(The book prints this heading as "Anti-CRSF Coding Best Practices"; the spelling slip is the book's.)
(Source: PDF p. 282)

## What the section covers
The short introduction to the third part of the chapter: a set of CSRF defenses that start at the code or design phase rather than in tokens or headers.

## Meaning
The book says many methods exist for eliminating or reducing CSRF risk in a web application from the code or design stage onward (PDF p. 282).

## Why it matters
Implementing these simple measures, the text claims, dramatically lowers the chance of falling victim to attackers who target CSRF (PDF p. 282).

## How it works
Three of the most effective methods are named, each treated in the following rows (PDF p. 282):
1. Refactor to stateless GET requests (WAS-C23-005).
2. Implement application-wide CSRF defenses (WAS-C23-006).
3. Introduce request-checking middleware (WAS-C23-006).
The later rows explain each: stateless GETs close the link-and-image vector, and the application-wide measure and middleware apply the checks to every route.

## When and how to apply
INTERPRETATION: because these are design-level choices, they are cheapest to adopt before endpoints multiply, and they work alongside the header checks and token scheme in WAS-C23-001 and WAS-C23-003.

## Relations
Leads into WAS-C23-005 (stateless GET requests) and WAS-C23-006 (application-wide mitigation).
