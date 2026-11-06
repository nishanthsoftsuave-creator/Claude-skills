---
id: A11-001
title: What's Next for Developers
source_pages: "28"
chapter: back
concepts: [secure-development, security-education, security-requirements, asvs, cheat-sheets, proactive-controls, samm, secure-sdlc, security-architecture]
related: [A00-007, A11-002, A11-003]
time_sensitive: true
---
# What's Next for Developers
(Source: PDF p. 28)

## What the section covers
The document's pointers for developers after reading the list: that secure software is hard to create and maintain, and which free OWASP resources help at each stage.

## Meaning
- Creating, maintaining or repairing secure software is difficult, and APIs are no different (PDF p. 28).
- OWASP has offered free, open security resources since the project began; the OWASP Projects page lists them comprehensively (PDF p. 28).
- The authors hold that education and awareness are the key factors in writing secure software, and that everything else depends on establishing and using repeatable security processes and standard security controls (PDF p. 28).

## How it works: the five areas the document names
1. **Education.** Start with the OWASP Education Project materials chosen by profession and interest. For hands-on practice the document mentions its planned "crAPI" (Completely Ridiculous API) on the roadmap and, meanwhile, the OWASP DevSlop Pixi module, a deliberately vulnerable web application and API service for learning to test and write safer APIs. Training at OWASP AppSec conferences and local chapters is also suggested (PDF p. 28).
2. **Security requirements.** Security belongs in every project from the start, and requirements work should define what "secure" means for the project. The document recommends the OWASP Application Security Verification Standard (ASVS) as a guide and, for outsourced work, the OWASP Secure Software Contract Annex, adapted to local law and regulation (PDF p. 28).
3. **Security architecture.** Security stays a concern in every project stage. The OWASP Prevention Cheat Sheets are the starting point for designing security in, among them the REST Security and REST Assessment cheat sheets (PDF p. 28).
4. **Standard security controls.** Adopting standard controls lowers the risk of introducing weaknesses while writing your own logic. Many frameworks now ship effective controls, and the OWASP Proactive Controls give an overview of what to include; OWASP also offers libraries and tools such as validation controls (PDF p. 28).
5. **Secure software development life cycle.** The OWASP Software Assurance Maturity Model (SAMM) helps improve the process of building APIs, and projects such as the OWASP Code Review Project help in the different development phases (PDF p. 28).

## When and how to apply
INTERPRETATION: when advising a team, use the five areas as a gap check: where is security education, requirements, design review, standard control use and process maturity missing, and map the ten chapter risks (A01-001 to A10-001) onto the requirements step.

## Time-sensitive statements
- The crAPI project is described as being on the roadmap in 2019 (PDF p. 28). INTERPRETATION: resource names, availability and links may have changed since 2019 and should be re-checked.

## Relations
A11-002 gives the DevSecOps counterpart; A00-007 is the list these resources help prevent; A11-003 describes how the list was built.
