---
id: WAS-C26-006
title: Summary - Defending Against DoS
source_pages: "305-306"
chapter: 26
concepts: [dos-summary, ddos-archetypes, single-attacker-dos, static-analysis-regex, anti-dos-mitigation, legitimate-user-impact]
related: [WAS-C26-002, WAS-C26-003, WAS-C26-005]
time_sensitive: false
---
# Summary: Defending Against DoS
(Source: PDF pp. 305-306; p. 306 is blank, so all content is on p. 305)

## What the section covers
The chapter's closing summary. Text above the Summary heading on this page, the final sentence of the DDoS mitigation advice, belongs to WAS-C26-005.

## Key points
- DoS attacks come in two main archetypes: a single attacker (DoS) and many attackers (DDoS) (PDF p. 305).
- Most DDoS attacks, though not all, work by overwhelming server resources, not by exploiting bugs. Countermeasures can therefore also trouble legitimate users (PDF p. 305).
- Single-attacker DoS can be mitigated through application architecture that stops users from holding application resources for long periods (PDF p. 305).
- Regex-based DoS can be mitigated with a static analysis tool, such as a linter, that scans the codebase's regular expressions and warns when one looks "evil" in syntax (PDF p. 305).
- Because DoS attacks are generally easy to exploit and rampant on the web, anti-DoS mitigations should be implemented once affordable, even when no attack is expected (PDF p. 305).

## Relations
Summarizes WAS-C26-002 (regex), WAS-C26-003 (logical) and WAS-C26-005 (DDoS). The remaining page in the range is blank in the source.
