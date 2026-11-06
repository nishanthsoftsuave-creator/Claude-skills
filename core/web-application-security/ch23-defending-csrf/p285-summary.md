---
id: WAS-C23-007
title: Summary - Defending Against CSRF Attacks
source_pages: "285-286"
chapter: 23
concepts: [csrf-summary, stateless-get, header-validation, csrf-tokens, user-trust, session-protection]
related: [WAS-C23-001, WAS-C23-002, WAS-C23-005, WAS-C23-006]
time_sensitive: false
---
# Summary: Defending Against CSRF Attacks
(Source: PDF pp. 285-286; p. 286 is blank, so all content is on p. 285)

## What the section covers
The chapter's closing summary. Text above the Summary heading on this page (the end of the middleware example and the advice on automating token passing on the client) belongs to WAS-C23-006.

## Key points
- Most CSRF risk can be reduced by making sure HTTP GET requests never change application state (see WAS-C23-005) (PDF p. 285).
- Beyond that, mitigations should consider validating headers (WAS-C23-001) and adding CSRF tokens to each request (WAS-C23-002) (PDF p. 285).
- The stated payoff: users can enter the web application from other origins with more confidence, and face lower risk that a hacker with malicious intent abuses their account permissions (PDF p. 285).

## When and how to apply
INTERPRETATION: treat the three measures as layers, not alternatives: stateless GETs remove the easiest attack vector, header checks filter by origin, and tokens block requests that did not come from a page the server itself issued.

## Relations
Summarizes WAS-C23-001 through WAS-C23-006. The attacks defended against are in the CSRF chapter of Part II, WAS-C11-004.
