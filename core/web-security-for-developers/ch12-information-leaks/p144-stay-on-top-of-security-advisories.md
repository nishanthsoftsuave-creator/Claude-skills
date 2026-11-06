---
id: WS-C12-004
title: Stay on Top of Security Advisories
source_pages: "144"
chapter: 12
concepts: [security-advisories, patching, server-fingerprinting, edge-case-behaviour, http-verbs, defense-in-depth]
related: [WS-C12-003, WS-C12-005, WS-C14-002]
time_sensitive: false
---
# Stay on Top of Security Advisories
(Source: PDF p. 144; the text above the "Stay on Top of Security Advisories" heading is mitigation 6, covered in WS-C12-003, and the "Summary" heading below belongs to WS-C12-005.)

## What the section covers
Why hiding information is never enough on its own, and why you must keep up with advisories for the software you run (PDF p. 144).

## Meaning
- A server fingerprint is a distinctive behaviour that identifies the stack behind a server. Web servers respond in characteristic ways to edge cases, for example deliberately corrupted HTTP requests or requests that use unusual HTTP verbs (PDF p. 144).
- A sophisticated attacker can use those unique behaviours to identify the server-side technology stack even when every other leak is closed (PDF p. 144).

## Why it matters
Because a determined attacker can still make a good guess about the technology, the earlier mitigations reduce exposure but do not eliminate it. Even when you follow best practice on information leakage, you must watch security advisories for the technology you use and deploy patches promptly (PDF p. 144).

## When and how to apply
INTERPRETATION: treat the hiding measures of WS-C12-002 and WS-C12-003 as a first layer and patch management as the backstop. Practical ways to follow advisories and tooling for dependency auditing appear in WS-C14-002.

## Relations
Follows WS-C12-003; recapped in WS-C12-005.
