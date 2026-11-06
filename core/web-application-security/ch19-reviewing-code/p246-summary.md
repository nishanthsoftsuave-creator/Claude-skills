---
id: WAS-C19-009
title: Reviewing Code for Security - Summary
source_pages: "246"
chapter: 19
concepts: [separation-of-concerns, security-review-summary, anti-patterns, risk-ordered-review, review-pipeline, security-engineers]
related: [WAS-C19-008, WAS-C19-003, WAS-C19-004]
time_sensitive: false
---
# Reviewing Code for Security: Summary
(Source: PDF p. 246)

## What the section covers
The end of the client and server separation discussion, followed by the chapter summary.

## Conclusion of the separation anti-pattern
- In a totally separated client and server application, the server is not responsible for the structure or content of HTML. It rejects any HTML sent and accepts authentication payloads only in a predefined data transit format (PDF p. 246).
- In a distributed application each module has fewer unique security mechanisms to carry. A monolithic application that couples client and server code has to defend against many languages, and must allow for received data being formatted in many ways rather than one predefined way.
- Separation of concerns matters for engineering and for security alike. Cleanly separated modules give security controls that are easier to manage, with no need to overlap them or to account for rare edge cases caused by complex interactions between several data and script types.

## Chapter summary
- Security review involves more than hunting for common vulnerabilities, which later chapters treat. It also means watching for anti-patterns that look like solutions but turn into problems, and reviews should be comprehensive, covering every area where vulnerabilities might hide (PDF p. 246).
- Reviewers should consider the specific usage requirements of the application, so they can recognize logical vulnerabilities that do not fit a standard archetype.
- A review should follow a logical path that builds understanding of the use cases before it assesses and evaluates risk. In established applications where the high-risk areas are known, most effort should go there, with the rest reviewed in descending order of risk.
- Putting security reviews into the code review pipeline, if done well, lowers the odds of introducing vulnerabilities. It should be part of any modern development pipeline and be carried out by engineers who know security, alongside the product or feature developer where possible.

## When and how to apply
INTERPRETATION: keep one written list of the application's risk areas and update it after each review, so that the next review starts in the right place.

## Relations
Completes the separation anti-pattern (WAS-C19-008). Repeats the points about logic bugs (WAS-C19-003) and review order (WAS-C19-004).
