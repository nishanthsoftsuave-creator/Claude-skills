---
id: A11-002
title: What's Next for DevSecOps
source_pages: "29"
chapter: back
concepts: [devsecops, continuous-security-testing, threat-model, security-automation, testing-strategy, coverage, communicating-findings, sdlc]
related: [A00-007, A11-001, A11-003]
time_sensitive: false
---
# What's Next for DevSecOps
(Source: PDF p. 29)

## What the section covers
Guidance for DevSecOps practitioners: why security cannot be left to a yearly exercise, and five practices for testing APIs continuously without slowing development.

## Meaning
- Because APIs matter so much in modern architectures, building them securely is crucial. Security must be part of the entire development life cycle, and scanning or penetration testing once a year is no longer enough (PDF p. 29).
- DevSecOps should join the development effort and enable continuous security testing across the whole software development life cycle. The goal is to strengthen the delivery pipeline with security automation without reducing development speed (PDF p. 29). Readers are told to revisit the DevSecOps Manifesto often (PDF p. 29).

## How it works: the five practices
1. **Understand the threat model.** Testing priorities come from a threat model. Without one, use the OWASP ASVS and the OWASP Testing Guide as inputs; involving the development team can raise its security awareness (PDF p. 29).
2. **Understand the SDLC.** Join the development team to learn its life cycle. Continuous security testing should fit its people, processes and tools, and everyone should agree on the process so there is no needless friction or resistance (PDF p. 29).
3. **Testing strategies.** Because the work must not slow development, choose the simplest, fastest, most accurate technique that verifies each security requirement. The OWASP Security Knowledge Framework and ASVS are good sources of functional and non-functional requirements, and the DevSecOps community offers further projects and tools (PDF p. 29).
4. **Achieving coverage and accuracy.** DevSecOps bridges developers and operations, so coverage must include the orchestration as well as the functionality. Work closely with both teams from the start, and aim for a state where the essential security is verified continuously (PDF p. 29).
5. **Clearly communicate findings.** Add value with little or no friction. Deliver findings promptly in the tools the development teams already use, not in PDF files. Join the team in fixing them, and use the chance to teach: describe the weakness, how it can be abused and an attack scenario that makes it real (PDF p. 29).

## When and how to apply
INTERPRETATION: the findings guidance matches how a review report should read, with each issue tied to a concrete attack scenario drawn from the relevant chapter (A01-001 to A10-001), and with evidence of what was actually tested.

## Relations
A11-001 gives the developer-side resources; A00-007 is the risk list the tests should cover; A11-003 explains the data behind the list.
