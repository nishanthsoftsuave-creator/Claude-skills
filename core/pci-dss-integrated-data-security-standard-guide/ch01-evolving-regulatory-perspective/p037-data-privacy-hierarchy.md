---
title: "Data Privacy Hierarchy"
book: pci-dss-integrated-data-security-standard-guide
chapter: 1
source_pages: "37-39"
format: source-text
---
# Data Privacy Hierarchy
(Source: PDF pp. 37-39)

<!-- PDF p. 37 (book p. 13) -->

Whether you are a small Merchant or a large Global Bank, if you are a business that relies on payment card data, you have an obligation to align with the PCI DSS for both legal and regulatory obligations. Consequently, a natural hierarchy has developed where your compliance obligations are aligned to the potential risks associated with particular business types (see Figure 1-7).

*[Figure omitted]*

**Figure 1-7.** *PCI DSS Hierarchy*

<!-- PDF p. 38 (book p. 14) -->

The manner in which you validate your PCI DSS compliance varies based upon the perceived risks for a heavily regulated industry or the volume of payment card data involved within your business operations.

## PCI DSS Validation Requirements

As previously mentioned, it is extremely important to keep track of your PCI DSS compliance status, all year around, to ensure that you have the evidence to support any breach investigations and not for a “Once-A-Year” compliance obligation, as per Table 1- 1.

**Banking Industry**

- **Card Issuer/Acquirer**
  - Self-regulation
  - Incorporated into a formal Information Security program
  - Compliance status called upon as evidence, in the event of a data breach

**Table 1-1.** *Mastercard Compliance Criteria – Merchants*[^28]

Level Criteria Validation

1

- any merchant that has suffered a hack or an attack that resulted in an account Data Compromise (aDC) event
- any merchant having greater than 6 Million total combined Mastercard and Maestro transactions annually
- Any merchant meeting the Level 1 criteria of Visa
- any merchant that Mastercard, in its sole discretion, determines should meet the level 1 merchant requirements to minimize risk to the system.
  - Annual Onsite Assessment[^29]
  - Quarterly Network Scan conducted by an Approved Scanning Vendor (ASV)[^30]

(*continued*)

[^28]: www.mastercard.us/en-us/merchants/safety-security/security-recommendations/merchants-need-to-know.html
[^29]: Level 1 merchants that choose to conduct an annual onsite assessment using an internal auditor must ensure that primary internal auditor staff engaged in validating PCI DSS compliance attend PCI SSC ISA Training and pass the associated accreditation program annually in order to continue to use internal auditors.
[^30]: www.pcisecuritystandards.org/assessors_and_solutions/approved_scanning_vendors

<!-- PDF p. 39 (book p. 15) -->

**Table 1-1.** (*continued*)

Level Criteria Validation

2

- any merchant with more than 1 to 6 Million total combined Mastercard and Maestro transactions annually
- any merchant meeting the level 2 criteria of visa
  - Annual Self- Assessment (Self- Assessment Questionnaire (SAQ))[^31]
  - Onsite Assessment at Merchant Discretion[^32]

3

- any merchant with greater than 20,000 combined Mastercard and Maestro e-commerce transactions annually but less than or equal to 1 Million total combined Mastercard and Maestro e-commerce transactions annually
- any merchant meeting the level 3 criteria of visa
  - Annual Self- Assessment
  - Onsite Assessment at Merchant Discretion[^33]
  - Quarterly Network Scan conducted by an ASV

4

- all other merchants[^34]
  - Annual Self-Assessment
  - Onsite Assessment at Merchant Discretion
  - Quarterly Network Scan conducted by an ASV

[^31]: www.pcisecuritystandards.org/documents/SAQ-InstrGuidelines-v3_2_1.pdf?agreement= true&time=1575476486348
[^32]: Level 2 merchants that choose to complete an annual self-assessment questionnaire must ensure that staff engaged in the self-assessment attend PCI SSC ISA Training and pass the associated accreditation program annually in order to continue the option of self-assessment for compliance validation. Alternatively, Level 2 merchants may, at their own discretion, complete an annual onsite assessment conducted by a PCI SSC-approved Qualified Security Assessor (QSA) rather than complete an annual self-assessment questionnaire.
[^33]: Level 3 and Level 4 merchants may alternatively, at their own discretion, engage a PCI SSC-approved QSA for an onsite assessment instead of performing a self-assessment.
[^34]: Level 4 merchants are required to comply with the PCI DSS. Level 4 merchants should consult their acquirer to determine if compliance validation is also required.
