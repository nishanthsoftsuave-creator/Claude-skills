---
id: WS-C12-001
title: "Chapter 12 Introduction: Information Leaks"
source_pages: "141"
chapter: 12
concepts: [information-leakage, zero-day-vulnerability, technology-stack, fingerprinting, attack-surface, vulnerability-scanning]
related: [WS-C12-002, WS-C12-003, WS-C12-004, WS-C12-005]
time_sensitive: false
---
# Chapter 12 Introduction: Information Leaks
(Source: PDF p. 141)

## What the section covers
The opening framing of Chapter 12: why a web server should not advertise which software it runs, and what the chapter will teach (PDF p. 141).

## Meaning
- A zero-day vulnerability is a security flaw that has been made public within the last 24 hours (PDF p. 141). Attackers pay close attention to such publicized flaws, and to publicized vulnerabilities in general (PDF p. 141).
- Information leakage here means a web server revealing the type of software stack it runs, through details such as technology names or versions that are visible from outside (PDF p. 141).

## Why it matters
- When a zero-day is published for some software component, attackers immediately scan the web for servers that run that component, so they can exploit the flaw (PDF p. 141).
- A server that broadcasts its technology choices makes itself a target for those scans. The book's advice is to make sure the server does not leak this information, since advertising the technology inadvertently invites attack (PDF p. 141).

## How the chapter proceeds
The chapter walks through common ways a web server leaks information about its technology choices and gives a mitigation for each risk (PDF p. 141). The mitigations are numbered 1 to 6 and followed by a note on security advisories; see WS-C12-002 (mitigations 1-3), WS-C12-003 (mitigations 4-6), WS-C12-004 (advisories) and WS-C12-005 (summary).

## Relations
Connects to the third-party code theme in Chapter 14, where unpatched components are the target of mass scans (see WS-C14-001).
