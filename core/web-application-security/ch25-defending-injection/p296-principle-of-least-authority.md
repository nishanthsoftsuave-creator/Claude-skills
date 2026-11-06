---
id: WAS-C25-006
title: Principle of Least Authority
source_pages: "296"
chapter: 25
concepts: [least-authority, least-privilege, privilege-separation, blast-radius, injection-containment, module-permissions]
related: [WAS-C25-005, WAS-C25-007, WAS-C19-007]
time_sensitive: false
---
# Principle of Least Authority
(Source: PDF pp. 296-297)

## What the section covers
The principle of least authority and how it limits the damage of an injection that slips through.

## Meaning
The principle, often called least privilege (the author finds that name less succinct), says every member of a system should have access only to the information and resources needed for its job. Applied to software: each module should only get the data and functionality it needs to operate correctly (PDF p. 296).

## How it works
Figure 25-1 starts with a user HTTP request containing unexpected commands, on the assumption that the endpoint does not sanitize input and so injection occurs. The server interprets the commands and runs them through a local CLI. If least authority was used, only the CLI process is compromised. If not, the entire system is compromised (PDF p. 296).

## Why it matters
The next page says the idea is simple but seldom applied in large applications, and gets more important as complexity grows because module interactions bring unexpected side effects. In its example a CLI backs up user profile photos, called from a terminal or through an adapter. Built with least authority, a compromise leaves the rest of the application safe; a CLI run as admin could expose the whole application server (PDF p. 297).

## Alternatives and trade-offs
It can feel like a roadblock, since it means managing extra accounts and keys, but proper use limits the risk of a breach (PDF p. 297).

## Relations
Containment complement to the detection and prevention rows; WAS-C19-007 describes the opposite trust-by-default anti-pattern.
