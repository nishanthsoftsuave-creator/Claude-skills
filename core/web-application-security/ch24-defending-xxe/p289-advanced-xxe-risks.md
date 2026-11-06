---
id: WAS-C24-003
title: Advanced XXE Risks
source_pages: "289"
chapter: 24
concepts: [xxe-impact, gateway-attack, remote-code-execution, server-takeover, reconnaissance-platform, severity]
related: [WAS-C24-001, WAS-C12-001, WAS-C12-002]
time_sensitive: false
---
# Advanced XXE Risks
(Source: PDF p. 289)

## What the section covers
Why an XXE flaw should be treated as more than a file-reading bug.

## Meaning
XXE attacks often begin as read-only attacks but can grow into more advanced forms. The book calls XXE a gateway attack: it gives an attacker a reconnaissance platform from which to reach data that is otherwise inaccessible from outside the web server (PDF p. 289).

## Why it matters
The data obtained can make other parts of the application easier to compromise. The final impact therefore ranges from read-only data access all the way to remote code execution and a full server takeover, which is why the text calls XXE so dangerous (PDF p. 289).

## When and how to apply
INTERPRETATION: when ranking an XXE finding, rate it by the worst chain it enables, not by the file it first exposes.

## Relations
The direct and indirect forms of the attack are WAS-C12-001 and WAS-C12-002; the fix is WAS-C24-001.
