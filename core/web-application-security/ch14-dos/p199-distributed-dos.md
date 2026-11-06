---
id: WAS-C14-004
title: Distributed DoS
source_pages: "199-200"
chapter: 14
concepts: [ddos, botnet, network-level-attack, udp-flooding, bandwidth-exhaustion, malware-controlled-devices]
related: [WAS-C14-003, WAS-C14-005, WAS-C26-004]
time_sensitive: false
---
# Distributed DoS
(Source: PDF pp. 199-200)

## What the section covers
The conceptual picture of distributed denial of service: many illegitimate users drain resources together, how botnets supply them, why most real DDoS works at the network level rather than through application logic, and how it relates to the other DoS forms.

## Meaning
- In DDoS, server resources are drained by a large number of illegitimate users. Because they request en masse, they may even be able to send ordinary requests, and at scale this drowns out server resources for legitimate users (PDF p. 199).
- The book says a comprehensive treatment is outside its scope, but readers should understand conceptually how DDoS works. Unlike DoS, where a single hacker targets another client or a server, distributed attacks involve many attackers: other hackers, or networked bots called botnets (PDF p. 199).
- Figure 14-2 (PDF p. 200) shows three users each spamming requests to a server that now has too many requests to complete, while a legitimate user trying to make a request suffers severe performance degradation.

## How it works
- In theory bots could exploit any kind of DoS at larger scale. For example, if a server uses a regex in an API endpoint, many clients could send problematic payloads to that endpoint at once (PDF p. 200).
- In practice most DDoS attacks do not use logic or regex flaws. They work at a lower level, the network rather than the application. Most botnet-based attacks send requests directly at a server's IP address, not at a particular API endpoint, and the traffic is usually UDP, aimed at using up the server's available bandwidth for legitimate requests (PDF p. 200).
- A botnet is rarely a set of devices owned by one hacker. It is made of devices that a hacker or group has taken over through malware spread over the internet: real computers owned by real people, running software that lets them be controlled remotely. That makes illegitimate clients hard to identify, since they look like real users (PDF p. 200).

## When and how to apply
- If you have access to a botnet, or can simulate one for security testing, the book advises trying both network-level and application-level attacks (PDF p. 200).
- Any of the earlier DoS weaknesses that exist on a server is also vulnerable to DDoS. DDoS is generally not effective against a single client, although seeding large amounts of regex-vulnerable payloads that are later delivered to client devices could fall within scope (PDF p. 200).
INTERPRETATION: because the tests described here affect real availability, run them only in an environment you own or have explicit written permission to test, in line with the chapter's earlier warning.

## Relations
Extends logical DoS (WAS-C14-003). Chapter recap in WAS-C14-005; mitigations in WAS-C26-004.
