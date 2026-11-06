---
id: WAS-C26-004
title: Protecting Against DDoS
source_pages: "303"
chapter: 26
concepts: [ddos, botnet, malware-distribution, iot-devices, volumetric-attack, legitimate-looking-traffic]
related: [WAS-C14-004, WAS-C26-005, WAS-C26-003]
time_sensitive: false
---
# Protecting Against DDoS (lead-in)
(Source: PDF p. 303)

## What the section covers
What makes distributed denial of service attacks harder to defend against than single-attacker DoS, and how botnets are formed. It starts partway down the page.

## Meaning
A DDoS attack comes from many sources but is controlled from one. A single attacker or a group distributes malware through some channel. The malware runs in the background on legitimate PCs, may arrive bundled with a legitimate program, and gives the attacker a backdoor so the machines can be controlled remotely and used together (PDF p. 303).

Computers are not the only targets: mobile devices and IoT devices such as routers, hotspots and smart toasters can be used too, often more easily. The collection of compromised devices is a botnet, from "robot" and "network" (PDF p. 303).

## Why it matters
Single-target DoS often exploits a bug in application code, such as a badly written regex or a resource-hungry API call. DDoS is usually simpler: it rarely targets logic bugs and instead overwhelms the target with a sheer volume of requests that look legitimate. Real users are shut out, or their experience is badly slowed (PDF p. 303).

## Limitations
The book states that DDoS attacks cannot be prevented, only mitigated in various ways (PDF p. 303).

## Relations
Defends against WAS-C14-004; the mitigations are in WAS-C26-005.
