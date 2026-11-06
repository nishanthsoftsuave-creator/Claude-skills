---
title: "Introduction"
book: pci-dss-integrated-data-security-standard-guide
chapter: 10
source_pages: "308-317"
format: source-text
---
# Introduction
(Source: PDF pp. 308-317)

<!-- PDF p. 308 (book p. 286) -->

Despite the fact that the PCI DSS has been continually evolving over the past 15 years, the volume of payment card theft/fraud/data breaches continues to grow and the number of businesses that manage to maintain PCI DSS compliance continues to decrease.

<!-- PDF p. 309 (book p. 287) -->

Payment Card Breach Trends[^2] PCI DSS Compliance Trends[^3]

*[Figure omitted]*

*[Figure omitted]*

With a ratio of just 1:5 businesses in the Americas managing to maintain their annual compliance obligations, the attraction for criminals becomes abundantly clear.

Unfortunately, despite all the efforts of the Card Brands and the PCI SSC to provide a bespoke controls framework for the Payment Card Industry, the complexities of different payment channels make maintaining a secure environment even more difficult. However, it is important to remember that the PCI DSS controls are only applicable to your business information systems, networks, infrastructure, and personnel. How the consumer safeguards their environment and systems is not applicable until you are entrusted with their payment card information.

Therefore, when seeking to fortify your payment card business operations through the use of the PCI DSS controls framework, it is important to start by looking at each point of interaction as a separate entity and to identify the potential risks that are associated with these methods of interface (a.k.a. Payment Channels). Helpfully, the PCI SSC have already done some of this for you through the creation of separate payment channel-aligned Self-Assessment Questionnaires.

This concept is similar to that applied by the National Institute of Standards and Technology (NIST),[^4] who have created a master catalogue of security controls (NIST SP800-53, R4[^5]). This master catalogue is then used as their reference for the creation of specific risk mitigation guidance.

[^2]: https://digitalguardian.com/blog/history-data-breaches
[^3]: https://enterprise.verizon.com/resources/reports/2019-payment-security-fullreport-bl-global.pdf
[^4]: www.nist.gov
[^5]: https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r4.pdf

<!-- PDF p. 310 (book p. 288) -->

All of the following NIST guidance are aligned with controls within the PCI DSS framework:

- **NIST SP800-18, Rev 1:** *Guide for Developing Security Plans for Federal Information Systems*[^6]
- **NIST SP800-37, Rev 2:** *Risk Management Framework for Information Systems and Organizations: A System Life Cycle Approach for Security and Privacy*[^7]
- **NIST SP800-39:** *Managing Information Security Risk: Organization, Mission, and Information System View*[^8]
- **NIST SP800-40, Rev 3:** *Guide to Enterprise Patch Management Technologies*[^9]
- **NIST SP800-41, Rev 1:** *Guidelines on Firewalls and Firewall Policy*[^10]
- **NIST SP800-70, Rev 4:** *National Checklist Program for IT Products: Guidelines for Checklist Users and Developers*[^11]
- **NIST SP800-77:** *Guide to IPsec VPNs*[^12]
- **NIST SP800-83, Rev 1:** *Guide to Malware Incident Prevention and Handling for Desktops and Laptops*[^13]
- **NIST SP800-92:** *Guide to Computer Security Log Management*[^14]
- **NIST SP800-153:** *Guidelines for Securing Wireless Local Area Networks (WLANs)*[^15]

[^6]: https://csrc.nist.gov/publications/detail/sp/800-18/rev-1/final
[^7]: https://csrc.nist.gov/publications/detail/sp/800-37/rev-2/final
[^8]: https://csrc.nist.gov/publications/detail/sp/800-39/final
[^9]: https://csrc.nist.gov/publications/detail/sp/800-40/rev-3/final
[^10]: https://csrc.nist.gov/publications/detail/sp/800-41/rev-1/final
[^11]: https://csrc.nist.gov/publications/detail/sp/800-70/rev-4/final
[^12]: https://csrc.nist.gov/publications/detail/sp/800-77/final
[^13]: https://csrc.nist.gov/publications/detail/sp/800-83/rev-1/final
[^14]: https://csrc.nist.gov/publications/detail/sp/800-92/final
[^15]: https://csrc.nist.gov/publications/detail/sp/800-153/final

<!-- PDF p. 311 (book p. 289) -->

For example, *you are an organization that is looking to mitigate the risks to your Manufacturing IT systems.*

SP800-53, R4: Security and Privacy Controls for Federal Information Systems and Organizations[^16]

SP800-82: Guide to Industrial Control Systems (ICS) Security[^17]

PCI DSS v3.2.1

Control Families aC – access Control; aU – audit and accountability; at – awareness and training; Cm – Configuration management; Cp – Contingency planning; Ia – Identification and authentication; Ir – Incident response; ma – maintenance; mp – media protection; ps – personnel security; pe – physical and environmental protection; pl – planning; pm – program management; ra – risk assessment; Ca – security assessment and authorization; sC – system and Communications protection; sI – system and Information Integrity; sa – system and services acquisition

- access Control (aC)
- awareness and training (at)
- audit and accountability (aU)
- security assessment and authorization (Ca)
- Contingency planning (Cp)
- Configuration management (Cm)
- Identification and authentication (Ia)
- Incident response (Ir)
- maintenance (ma)
- media protection (mp)
- physical and environmental protection (pe)
- planning (pl)
- personnel security (ps)
- risk assessment (ra)
- system and services acquisition (sa)
- system and Communications (sC)
- system and Information Integrity (sI)
- program management (pm)
  - requirement 7
  - requirement 8
  - requirement 10 requirement 12.10
  - requirement 12.6
  - requirement 2
  - requirement 8.7
  - requirement 12.10
  - requirement 9.5/9.6
  - requirement 9
  - requirement 12.2
  - requirement 11
  - requirement 1
  - requirement 4
  - requirement 5
  - requirement 6

[^16]: https://nvd.nist.gov/800-53/Rev4
[^17]: https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-82r2.pdf

<!-- PDF p. 312 (book p. 290) -->

The NIST suite of controls are compartmentalized into family groups and are prioritized based upon their perceived importance:

**Total of 170 High-Impact Controls**[^18]

**Table 10-1.** *Access Control (AC) High-Impact Controls*

| No. | Control | Priority | High |
|---|---|---|---|
| aC-1 | aCCess Control polICy anD proCeDUres | p1 | aC-1 |
| aC-2 | aCCoUnt manaGement | p1 | aC-2 (1) (2) (3) (4) (5) (11)<br>(12) (13) |
| aC-3 | aCCess enForCement | p1 | aC-3 |
| aC-4 | InFormatIon FloW enForCement | p1 | aC-4 |
| aC-5 | separatIon oF DUtIes | p1 | aC-5 |
| aC-6 | least prIVIleGe | p1 | aC-6 (1) (2) (3) (5) (9) (10) |
| aC-7 | UnsUCCessFUl loGon attempts | p2 | aC-7 |
| aC-8 | system Use notIFICatIon | p1 | aC-8 |
| aC- 10 | ConCUrrent sessIon Control | p3 | aC-10 |
| aC- 11 | sessIon loCk | p3 | aC-11 (1) |
| aC- 12 | sessIon termInatIon | p2 | aC-12 |
| aC- 14 | permItteD aCtIons WIthoUt<br>IDentIFICatIon or aUthentICatIon | p3 | aC-14 |
| aC- 17 | remote aCCess | p1 | aC-17 (1) (2) (3) (4) |
| aC- 18 | WIreless aCCess | p1 | aC-18 (1) (4) (5) |
| aC- 19 | aCCess Control For moBIle DeVICes | p1 | aC-19 (5) |
| aC- 20 | Use oF eXternal InFormatIon systems | p1 | aC-20 (1) (2) |
| aC- 21 | InFormatIon sharInG | p2 | aC-21 |
| aC- 22 | pUBlICly aCCessIBle Content | p3 | aC-22 |

[^18]: https://nvd.nist.gov/800-53/Rev4/impact/HIGH

<!-- PDF p. 313 (book p. 291) -->

Additionally, NIST provide an extremely useful supporting guidance document to help explain how the controls from the catalogue should be assessed:

- **NIST SP800-53A, Rev 4:** Assessing Security and Privacy Controls in Federal Information Systems and Organizations: Building Effective Assessment Plans[^19]

This is a very helpful aid to help you understand what is expected when assessing the effectiveness of your controls *(either by yourself or with a Qualified Security Assessor (QSA))*.

Under PCI DSS version 3.2.1, the PCI SSC have identified and grouped the applicable controls into shortened SAQs, based upon the perceived risks associated with these business operations, for example:

[^19]: https://csrc.nist.gov/publications/detail/sp/800-53a/rev-4/final

## Card Not Present

### E-commerce

- **SAQ A: Fully Outsourced** – No business systems or personal interaction with Cardholder Data
  - *Circa 22 controls*
- **SAQ A-EP**: Partially Outsourced E-commerce Merchants Using a Third-Party Web site for Payment Processing
  - *Circa 148 controls*
- **SAQ C**: Merchants with Payment Application Systems Connected to the Internet – **No Electronic Cardholder Data Storage**
  - *Circa 108 controls*
- **SAQ D-Merchants**: All other SAQ-Eligible Merchants

For example, Application Programmable Interface (API) enabled e-Commerce

- *Circa 332 controls*

<!-- PDF p. 314 (book p. 292) -->

### Telephone-Based (a.k.a. Mail Order Telephone Order)

- **SAQ C-VT**: Merchants with Web-Based Virtual Payment Terminals – **No Electronic Cardholder Data Storage**
  - *Circa 66 controls*

## Card Present

### Face to Face

- **SAQ P2PE**: Merchants using Hardware Payment Terminals in a PCI SSC-Listed P2PE Solution Only – **No Electronic Cardholder Data Storage**
  - *Circa 24 controls*
- **SAQ B**: Merchants with Only Imprint Machines or Only Standalone, Dial-out Terminals – **No Electronic Cardholder Data Storage**
  - *Circa 38 controls*
- **SAQ B-IP**: Merchants with Standalone, IP-Connected PTS Point-of-Interaction (POI) Terminals – **No Electronic Cardholder Data Storage**
  - *Circa 64 controls*
- **SAQ D-Service Providers**: SAQ-Eligible Service Providers

For example, Provision and Management of Automated Teller Machines (ATMs)

- *Circa 362 controls*

Eligibility for completion of the shortened SAQs must meet the criteria outlined in the “**Before You Start”** section of the SAQ, and any electronic storage *(Localized spreadsheets, CCTV recording, Telephone recordings, System Logs, etc.)* of cardholder data makes you ineligible for the shortened SAQs and you will need to be assessed against the SAQ D controls (circa 332 controls.).

If you are a business that provides services to Merchants, you will need to use the SAQ D-Service Providers (SAQ D-SP), which includes additional specific Service <!-- PDF p. 315 (book p. 293) --> Provider controls. However, it might be that your offered service aligns to one of the shortened SAQs. In this case it might be that you validate your company against the shortened SAQ plus the Service Provider controls on the SAQ D-SP.

Important Reminder higher risk merchants and service providers are ineligible for completion of the saQ and must have their compliance independently validated through an onsite assessment, conducted by a pCI ssC-verified Qualified security assessor (Qsa), and compiled into the report on Compliance (roC) and the supporting attestation of Compliance (aoC).

Note Completed roCs should be securely retained for 3 years (as supporting evidence, in the case of suffering a data breach), and these should not be provided as proof of evidence (owing to sensitive contents).

the aoCs should be the only documentation needed to prove your pCI Dss compliance status.

However, just like any effective defensive strategy, before simply applying the suite of controls, first it is important to assess the potential impact on your business operations (e.g., critical systems that are difficult to update, external facing and sensitive data processing systems, etc.). Having identified the importance and potential impact on each system, it is then important to understand the applicable and potential attack vectors that could be leveraged against your payment card business operations.

Understanding your attack vectors is essential in helping you understand the importance of the mitigation controls (a.k.a. Threat Intelligence[^20]).

*Threat intelligence is evidence-based knowledge, including context, mecha- nisms, indicators, implications, and action-oriented advice about an exist- ing or emerging menace or hazard to assets. This intelligence can be used to inform decisions regarding the subject’s response to that menace or hazard.*

—Gartner

[^20]: www.gartner.com/en/documents/2487216/definition-threat-intelligence

<!-- PDF p. 316 (book p. 294) -->

Think of it as playing a competitive sport and researching the set plays of your competitor. In order to be able to effectively defend against them, you need to have knowledge of their “Set Plays.” The same applies when trying to proactively defend your business from compromise or data loss.

There are multiple sources of information that are available to you. However, you need to ensure that these various sources of information are refined and made relevant to your business, rather than just being a dump of raw information.

Turning information into actionable intelligence

*[Figure omitted]*

**Figure 10-1.** *CM-Alliance TI Pyramid*

- How well do you know your enemy?
- How aligned are your security tools to your identified and known threats?
- Does your defensive strategy adapt to the changing TTPs of your attackers?

<!-- PDF p. 317 (book p. 295) -->

*[Figure omitted]*

**Figure 10-2.** *E-commerce*
