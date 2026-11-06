---
id: A00-006
title: API Security Risk (risk-rating scales)
source_pages: "6"
chapter: front
concepts: [risk-rating, owasp-risk-rating-methodology, exploitability, weakness-prevalence, weakness-detectability, technical-impact, business-impact, threat-agents, risk-acceptance]
related: [A00-007, A00-003, A11-003]
time_sensitive: false
---
# API Security Risk (risk-rating scales)
(Source: PDF p. 6)

## What the section covers
The scoring scheme behind the number strip printed at the top of every risk chapter (for example "Exploitability: 3, Prevalence: 3, Detectability: 2, Technical: 3"), the limits of that scheme, and the standards the authors point to for a fuller risk analysis.

## How it works
The risk analysis follows the OWASP Risk Rating Methodology. A single table defines the vocabulary of a risk score (PDF p. 6):

| Factor | Values as printed |
|---|---|
| Threat agents | "API Specific" (printed with no numeric scale) |
| Exploitability | Easy 3, Average 2, Difficult 1 |
| Weakness prevalence | Widespread 3, Common 2, Difficult 1 |
| Weakness detectability | Easy 3, Average 2, Difficult 1 |
| Technical impact | Severe 3, Moderate 2, Minor 1 |
| Business impacts | "Business Specific" (no numeric scale; left to the organisation) |

- INTERPRETATION: higher numbers mean a worse position for the defender: easier to exploit, more widespread, easier for an attacker to detect, or more severe in technical terms.
- The prevalence row prints "Difficult 1" for its lowest value, which reads like a slip for a word such as "uncommon"; it is recorded here as printed (PDF p. 6). INTERPRETATION: treat prevalence 1 as "rare".

## Limitations and failure modes
The authors are explicit about what the scheme leaves out (PDF p. 6):
- It does not take the likelihood of a particular threat agent into account.
- It ignores the technical details of your own application, which could significantly change how likely an attacker is to find and exploit a given vulnerability.
- It does not measure the real impact on your business. Each organisation must decide how much application and API security risk it will accept, given its culture, industry and regulatory environment.
- The stated purpose of the Top 10 is not to perform that risk analysis for you.

## When and how to apply
INTERPRETATION: when a review reports a finding that maps to one of the ten risks, quote the document's four scores for that risk as the document's generic rating, then record the project's own exploitability, detectability and business impact separately; never present the generic strip as a project-specific severity. The per-risk scores are recorded in each chapter module (A01-001 through A10-001) and summarised in this book's index.

## References the section lists
OWASP: the Risk Rating Methodology and an article on threat and risk modelling. External: ISO 31000 (risk management), ISO 27001 (information security management systems), the NIST Cyber Framework (US), the ASD Strategic Mitigations (Australia), NIST CVSS 3.0 and the Microsoft Threat Modeling Tool (PDF p. 6).

## Relations
A00-007 lists the risks the scales are applied to; A11-003 says the scores were discussed and reviewed among the contributing practitioners; A00-003 directs new readers here before the list.
