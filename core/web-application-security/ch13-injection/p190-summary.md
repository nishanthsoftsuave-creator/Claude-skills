---
id: WAS-C13-004
title: Injection Summary
source_pages: "190-192"
chapter: 13
concepts: [injection, trusting-user-input, bug-bounty, penetration-testing, parsers-and-clis, summary]
related: [WAS-C13-001, WAS-C13-002, WAS-C13-003]
time_sensitive: false
---
# Injection: Summary
(Source: PDF pp. 190-192)

## What the section covers
The chapter's closing remarks on why injection attacks matter beyond SQL and how a tester should regard them. The final page of the range is blank.

## Meaning and key points
- Injection-style attacks reach beyond classic SQL injection into many other technologies, as the chapter showed with CLIs and command execution (PDF p. 190).
- Unlike XXE, injection is not caused by one weak specification. It is a class of vulnerability that appears whenever user input is trusted too much (PDF p. 190).
- Why it is worth mastering for a bug bounty hunter or penetration tester: well-known databases probably already have defenses, but injection against parsers and CLIs is less documented, so the defensive mechanisms around them are likely less rigid (PDF pp. 190-191).
- These attacks require some understanding of what the application does. They typically arise when server code is executed that includes text parsed from the client's HTTP request (PDF p. 191).
- They are described as powerful, elegant and capable of many goals: data theft, account takeover, permission elevation, or simply causing chaos (PDF p. 191).

## When and how to apply
INTERPRETATION: during recon, rank endpoints that touch parsers, converters or shell calls above plain database lookups when looking for under-defended injection points, and use knowledge of the feature's purpose to guess which fields reach the interpreter.

## Relations
Recaps WAS-C13-001, WAS-C13-002 and WAS-C13-003. The defensive treatment of injection is in Chapter 25.
