---
id: WAS-C26-003
title: Protecting Against Logical DoS
source_pages: "302"
chapter: 26
concepts: [logical-dos, dos-risk-scale, resource-intensive-logic, risk-rating, critical-resources, error-on-caution]
related: [WAS-C14-003, WAS-C26-002, WAS-C26-001]
time_sensitive: false
---
# Protecting Against Logical DoS
(Source: PDF pp. 302-303)

## What the section covers
How to think about, and begin defending against, logical DoS. It starts partway down the page, below the regex discussion, and finishes on the next page above the DDoS heading.

## Why it matters
Logical DoS is much harder to detect and prevent than regex DoS. As with regex DoS, it is usually not exploitable unless developers accidentally introduce logic that can be abused to consume system resources (PDF p. 302).

## Meaning
Systems without exploitable logic generally do not fall to logical DoS. Yet a well-written application could still be hit, assuming the attacker has enough resources to overwhelm normally performant code. DoS is measured on a scale rather than as a yes-or-no property, so the book suggests rating exposed functionality as high, medium or low DoS risk, not as vulnerable or secure. Resource consumption is harder to categorize than, say, XSS, which is binary: you either have the exploit or you do not (PDF pp. 302-303).

## How it works
The next page continues: code may be very hard to exploit, easy to exploit, or somewhere between. A user on a powerful desktop may not notice an exploitable client-side function while someone on an older mobile device does. The book labels the very hard category "safe" and the other two "vulnerable", and says to err on the side of caution when evaluating security (PDF p. 303).

## When and how to apply
To protect against logical DoS, identify the parts of the codebase where critical system resources are used (PDF p. 303).

## Relations
Defends against WAS-C14-003; the logging advice in WAS-C26-001 helps spot abuse.
