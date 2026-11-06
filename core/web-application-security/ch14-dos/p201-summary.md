---
id: WAS-C14-005
title: Denial of Service Summary
source_pages: "201-202"
chapter: 14
concepts: [denial-of-service, resource-consumption, ddos, attack-layers, data-leakage, summary]
related: [WAS-C14-002, WAS-C14-003, WAS-C14-004, WAS-C26-006]
time_sensitive: false
---
# Denial of Service: Summary
(Source: PDF pp. 201-202)

## What the section covers
The chapter recap. The second page of the range is blank.

## Key points
- Classic DDoS is by far the most common form of distributed attack, but it is only one of many attacks that aim to consume server resources so that legitimate users cannot (PDF p. 201).
- DoS can happen at many layers of the application stack: the client, the server, and sometimes the network layer. It can affect one user at a time or many, and the damage ranges from reduced application performance to complete lockout (PDF p. 201).
- When looking for DoS, the book advises first working out which server resources are most valuable and then finding the APIs that use those resources. The value of resources differs from application to application. It may be something standard such as RAM or CPU, or something more specific such as functionality performed in a queue, where user a is handled before user b and then user c (PDF p. 201).
- DoS typically causes only annoyance or interruption, but some DoS attacks can leak data. Testers should watch for logs and errors that appear as a result of DoS attempts (PDF p. 201).

## Relations
Recaps ReDoS (WAS-C14-002), logical DoS (WAS-C14-003) and distributed DoS (WAS-C14-004). The defensive recap is WAS-C26-006.
