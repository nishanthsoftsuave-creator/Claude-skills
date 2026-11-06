---
title: "PCI DSS Controls Framework Architecture"
book: pci-dss-integrated-data-security-standard-guide
chapter: 2
source_pages: "60-64"
format: source-text
---
# PCI DSS Controls Framework Architecture
(Source: PDF pp. 60-64)

<!-- PDF p. 60 (book p. 36) -->

The PCI DSS controls architecture employs a layered defensive structure, whereby each layer provides an isolated barrier in order to slow or deter an attacker’s ingress or egress. As a result, an attacker would need to peel back each layer of defense to move toward (or away from) the payment card data. Think of the architecture as being similar to the structure of an onion.

<!-- PDF p. 61 (book p. 37) -->

*[Figure omitted]*

## Primary (Core) Ring

At the core of the PCI DSS controls framework is the need to safeguard the payment card data (Storage, Transmission, and Processing) by ensuring that the aggregated risk associated with data retention is strictly limited based upon strict legal, regulatory, and/ or business requirements and with the most sensitive data (Sensitive Authentication Data (SAD) being prevented from being retained post authorization. Where the Primary Account Number (PAN) needs to be viewed, the risk is reduced to only the first six and last four digits. Having strictly controlled the retained payment card data, any unavoidable data stores need to be securely stored and, if encrypted, supported by robust key management processes to ensure that if the data vault becomes compromised, then the data appears to be worthless to the criminal. Additionally, all data in transit is also to be protected through the use of strong encryption.

**Figure 2-9.** *PCI DSS Layered Defenses*

<!-- PDF p. 62 (book p. 38) -->

## Secondary Ring

The next ring requires the supporting network and systems to be robustly configured to ensure that the network traffic is filtered to only allow authorized traffic into the trusted zone and to ensure that the supporting IT systems are locked down, so as to prevent misuse.

## Tertiary Ring

Having limited your data retention to a minimum and implemented robustly configured the supporting IT systems, you then need to strictly limit the access to only those with a legitimate need to know/need to access. The more personnel with authorized access, the greater the number of potential targets to be exploited by criminals and, thus, the greater the risk.

## Quaternary Ring

IT systems and software applications are dynamic by their very nature and, as such, need to be well maintained to ensure that they are protected from malware and any higher risk emerging vulnerabilities, and all software development activities have security considerations embedded within them to ensure no known high-risk vulnerabilities are introduced into your secure environment.

## Quinary Ring

This is the “checks and balance” ring, whereby the inner rings are monitored for ABNORMAL activities and are periodically tested to provide reassurance to confirm that no vulnerabilities exist. In the event that vulnerabilities are detected, they are remediated against in a timely manner *(based upon the perceived risks)*.

## Senary (Outer) Ring

The final outer ring is the “People Management” to ensure that all personnel supporting the payment card business operations understand the rules, their responsibilities, and the standard operating procedures (SOPs) that relate to their roles.

Each of these rings has subsequent sub-rings and micro-rings that need to be applied to provide robust rings of defense.

<!-- PDF p. 63 (book p. 39) -->

For example, see the following data taken from v3.2.1.

Requirement 3: Protect Stored Cardholder Data

3.1 Data retention

3.2 Sensitive authentication Data (SaD)

- 3.2.1. prohibit storage of full track data
- 3.2.2. prohibit storage of card verification code or value
- 3.2.3. prohibit storage of personal identification number (pin) or the encrypted pin block

3.3 Mask primary account number (pan)

3.4 render stored pan unreadable

- 3.4.1. Disk encryption

3.5 formal key management practices

- 3.5.1. Service providers – Documented description of the cryptographic architecture
- 3.5.2. restrict access to cryptographic Keys
- 3.5.3. Secret and private keys secure storage
- 3.5.4. Cryptographic keys storage

3.6 formal key management processes and procedures

- 3.6.1. Strong cryptographic key generation
- 3.6.2. Secure cryptographic key distribution
- 3.6.3. Cryptographic key secure storage
- 3.6.4. Cryptographic key change management
- 3.6.5. Cryptographic key retirement/replacement
- 3.6.6. Manual clear text cryptographic practices
- 3.6.7. prevention of unauthorized substitution of cryptographic keys
- 3.6.8. Cryptographic key custodians’ acknowledgment of their responsibilities

3.7 policies and procedures for securing ChD

Based upon the structure of an onion, the outer skin layer is paper thin, while the inner layers get progressively thicker, and the closer you get to the center of the onion, you will be feeling increasing layers of discomfort *(eyes watering)*.

The same principles apply within PCI DSS, to provide five Ds of defensive methodology:

- **D**eter
- **D**etect

<!-- PDF p. 64 (book p. 40) -->

- **D**elay
- **D**eny
- **D**efend

The concept of layered defenses (a.k.a. Defense in Depth) were believed to have been applied to protect the City of Troy,[^16] between 1174 BC and 1184 BC, to successfully repel a 10-year period of Greek army invasion attempts and finally succumbing to the attacker’s Trojan horse delivery. The Roman Empire were,[^17] in fourth century AD, to provide flexibility with efficient defenses for their rapidly expanding frontiers.

In 2001, the SANS Institute created a comprehensive paper[^18] on the very same topic, which still remains a fundamental defensive concept to this day and which remains a resource provision in their Reading Room.

[^16]: www.nationalgeographic.org/thisday/apr24/fall-troy/
[^17]: www.romanarmy.net/Latearmy.shtml
[^18]: www.sans.org/reading-room/whitepapers/basics/defense-in-depth-525
