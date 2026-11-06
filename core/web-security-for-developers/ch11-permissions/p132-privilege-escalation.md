---
id: WS-C11-002
title: Privilege Escalation
source_pages: "132"
chapter: 11
concepts: [privilege-escalation, vertical-escalation, horizontal-escalation, web-shell, root-access, access-tokens]
related: [WS-C11-001, WS-C11-003, WS-C06-004]
time_sensitive: true
---
# Privilege Escalation
(Source: PDF p. 132; the text above the "Privilege Escalation" heading is the end of WS-C11-001. This row ends where the "Access Control" heading begins.)

## What the section covers
The two categories of privilege escalation attack, vertical and horizontal.

## Meaning
- Security specialists divide escalation into vertical and horizontal (PDF p. 132).
- Vertical escalation: the attacker obtains an account with wider permissions than their own. For example, an attacker who manages to put a web shell on your server (an executable script that takes parts of an HTTP request and runs them on the command line) will want to climb to root privilege so they can do anything on the machine. Commands sent through the shell normally run as the operating-system account of the web server, which usually has limited network and disk access. Attackers have found many ways to escalate on operating systems to reach root, which lets them take over the entire server from the shell (PDF p. 132).
- Horizontal escalation: the attacker reaches another account with privileges similar to their own. The earlier chapters showed common routes: guessing passwords, hijacking sessions, or crafting malicious HTTP request data (PDF p. 132).
- The September 2018 Facebook attack (WS-C11-001) was horizontal escalation, caused by an API that issued access tokens without properly checking the requester's permissions (PDF p. 132).

## When and how to apply
- Defence is to implement access control securely for every sensitive resource, which the next section explains (WS-C11-003) (PDF p. 132).

## Time-sensitive statements
Facebook September 2018 incident as the worked example (PDF p. 132).

## Relations
Web shells arise from the remote-code-execution material in WS-C06-004.
