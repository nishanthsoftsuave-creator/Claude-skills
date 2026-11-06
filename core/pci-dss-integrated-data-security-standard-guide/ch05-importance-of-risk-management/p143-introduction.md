---
title: "Introduction"
book: pci-dss-integrated-data-security-standard-guide
chapter: 5
source_pages: "143-146"
format: source-text
---
# Introduction
(Source: PDF pp. 143-146)

<!-- PDF p. 143 (book p. 120) -->

The ENISA EU Agency for Cyber security publishes PCI DSS in their risk management section of their web site,[^9] confirming that they are in agreement that PCI DSS is a catalogue of baseline security control developed to mitigate the risks to payment card processes. Consequently, it is important to develop an understanding of effective risk management practices.

[^9]: www.enisa.europa.eu/topics/threat-risk-management/risk-management/current-risk/laws-regulation/corporate-governance/pci-dss

## What Is a Risk Assessment?

In PCI DSS, v3.2.1, there are six main control areas that integrate with one another to form the risk assessment process:

- 6.1. Vulnerability Risk Identification
- 11.2 Quarterly Vulnerability Scanning

**Figure 5-3.** *Payment Card Number Verification*

<!-- PDF p. 144 (book p. 121) -->

- 11.3. Penetration Testing
- 12.2. Risk Assessment
- 12.6. Formal Security Awareness
- 12.10. Incident Response

Each of these controls is complementary to each other and supports the risk assessment process. However, every PCI DSS control is a risk mitigation control and should be incorporated into the development of suitable risk assessment scenarios.

Synopsys[^10] defines a security risk assessment as

the identification, assessment, and implementation of key security controls in applications and systems. It also focuses on preventing application and systems security defects and vulnerabilities.

SANS[^11] provides further clarification of the core areas of the risk assessment process that you should be including in the development of your risk assessment practices:

- Scope
- Data Collection
- Analysis of Policies and Procedures
- Threat Analysis
- Vulnerability Analysis
- Correlation and assessment of Risk Acceptability

[^10]: www.synopsys.com/glossary/what-is-security-risk-assessment.html
[^11]: www.sans.org/reading-room/whitepapers/auditing/overview-threat-risk-assessment-76

## Background

I was first introduced to formal Security Risk Management practices during my attendance of the RAF Police’s 10-week residential Counter Intelligence course, in 2002, through the application of the Royal Air Force’s Air Publication 3085 (Risk Management in the RAF) and the supporting Air Publication 3085A (tactics, techniques, and protocols (TTPs) for <!-- PDF p. 145 (book p. 122) --> Risk Management in the RAF). These publications outlined the expectations for effective risk management, including the four Ts model[^12] of risk treatment:

- Terminate risk Altering processes or practices to eliminate risk completely.
- Treat risk Controlling risk through actions that reduce the likelihood of the risk occurring or minimize its impact prior to its occurrence.
- Tolerate risk No action is taken to mitigate or reduce a risk (it still needs to be monitored).
- Transfer risk Assigning an individual, group, or third party to be responsible for the risk.

During my further studies in Risk Management (a module Loughborough University’s Security Management MSc[^13] and ISACA’s Certified Information Security Manager (CISM[^14]) and certified in risk and information systems control (CRISC[^15])), the same treatment options are presented but using different synonyms, which are not as easy to readily recall:

- Avoid
- Mitigate
- Accept
- Transfer

Consequently, I still tend to favor the use of the four Ts model of Risk Treatment. Before you can carry out an effective risk assessment, you need to ensure that you have developed sufficient risk scenarios[^16] for your various processes that support your payment card processes to ensure that an appropriate level of risk has been assessed for the effective protection of your payment card processing, based upon the balance of the risk elements for your business:

Business Risk = Vulnerability × threat × Impact

[^12]: www.skillcast.com/blog/10-things-you-should-do-to-improve-risk-management-at-work
[^13]: www.lboro.ac.uk/students/programme-specifications/2013/business-and-economics/postgraduate/name-56595-en.html
[^14]: www.isaca.org/Certification/Documents/CISM-Certification-Overview_bro_eng_0519.pdf
[^15]: www.isaca.org/Certification/Documents/CRISC-Certification-Overview_bro_eng_0519.pdf
[^16]: www.isaca.org/Knowledge-Center/Research/ResearchDeliverables/Pages/Risk-Scenarios-Using-COBIT-5-for-Risk.aspx

<!-- PDF p. 146 (book p. 123) -->

Appropriate risk assessments should be based upon realistic, business aligned scenarios. Such scenarios should be based upon input on your specific business processes that may impact your payment card operations.

Within the current version of PCI DSS (v3.2.1), the guidance column provides extensive context on the threats and risks that these controls have been designed to mitigate against.

*[Figure omitted]*

*Note: The PCI SSC have intimated that risk will have a greater importance with the release of the next version of the PCI DSS integrated controls framework:*

Goals for PCI DSS v4.0 the 12 core pCI Dss requirements are not expected to fundamentally change with pCI Dss v4.0, as these are still the critical foundation for securing payment card data. however, based on feedback received, pCI ssC is evaluating how to evolve the standard to accommodate changes in technology, risk mitigation techniques, and the threat landscape. pCI ssC is also looking at ways to introduce greater flexibility to support organizations using a broad range of controls and methods to meet security objectives.

key high-level goals for pCI Dss v4.0 are ensure the standard continues to meet the security needs of the payments industry.

add flexibility and support of additional methodologies to achieve security.

promote security as a continuous process.

enhance validation methods and procedures.

**Figure 5-4.** *PCI DSS Threat and Risk Guidance*
