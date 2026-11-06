---
title: "Applying “Team Tactics” to Win the PCI DSS Compliance Game"
book: pci-dss-integrated-data-security-standard-guide
chapter: 11
source_pages: "361-366"
format: source-text
---
# Applying “Team Tactics” to Win the PCI DSS Compliance Game
(Source: PDF pp. 361-366)

<!-- PDF p. 361 (book p. 340) -->

Okay, so hopefully you will now have an appreciation for the value of a cohesive team-based approach to managing your PCI DSS compliance efforts and, thus, reducing the potential opportunities for your opponents to profit from your mistakes.

In the current version of the PCI DSS controls framework (v3.2.1), the “Team Tactics” is partially addressed through the concluding controls of each requirement and throughout requirement 12:

- Requirement-specific supporting policies and operational procedures management
- Security policy management
- Risk management
- Acceptable Usage policy management
- Defined information security responsibilities for all personnel
- Assignment of information security management responsibilities

**Figure 11-9.** *Tactics, Techniques, and Protocols (TTPs)*[^41]

[^41]: https://mitre-attack.github.io/attack-navigator/enterprise/

<!-- PDF p. 362 (book p. 341) -->

- Security Education management
- Security vetting management
- Vendor management
- Incident response management
- Internal audit management

Unfortunately, in its current format, the PCI DSS controls framework aligns to support isolated departmental responsibilities and does not require “team tactics” to be developed and applied.

In fairness, even the more structured three lines of defense (3LOD) model[^42] can often be seen being misapplied in heavily regulated industries (e.g., Financial Services). However, such a model would be most effective when applied to your PCI DSS compliance efforts.

*[Figure omitted]*

[^42]: www.coso.org/Documents/COSO-2015-3LOD.pdf

## 1LOD

Under the 1LOD, operational management has ownership, responsibility, and accountability for directly assessing, controlling, and mitigating risks.

**Figure 11-10.** *3LOD Model*

<!-- PDF p. 363 (book p. 342) -->

## 2LOD

The 2LOD consists of activities covered by several components of internal governance (compliance, risk management, quality, IT, and other control departments).

- This LOD monitors and facilitates the implementation of effective risk management practices by operational management and assists the risk owners in reporting adequate risk-related information up and down the organization.

## 3LOD

Internal audit forms the organization’s 3LOD. An independent internal audit function will, through a risk-based approach to its work, provide assurance to the organization’s board of directors and senior management.

- This assurance will cover how effectively the organization assesses and manages its risks and will include assurance on the effectiveness of the 1LOD and 2LOD.
  - It encompasses all elements of an institution’s risk management framework (from risk identification, risk assessment and response, to communication of risk-related information) and all categories of organizational objectives: strategic, ethical, operational, reporting, and compliance.

The need for a teamwork-based approach has been alluded to, within Appendix A3 of the existing PCI DSS controls framework (v3.2.1), where the Card Brands require greater assurance from the organizations, they deem to be Designated Entities Supplemental Validation (DESV):

- **A3.1 Implement a PCI DSS compliance program.**
  - Executive management are responsible for the protection of cardholder data and a PCI DSS compliance program.
  - Establish a formal PCI DSS compliance program.

<!-- PDF p. 364 (book p. 343) -->

- Define and formally assign PCI DSS compliance roles and responsibilities.
- Establish an up-to-date PCI DSS and InfoSec formal training program.

**For example, develop a cohesive and holistic compliance, which includes the need for**

- *The establishment of a PCI DSS security working group/committee to work in support of the PCI DSS compliance program*
- *Periodic PCI DSS security working group/committee meetings to discuss matters, risks, or issues pertaining to the PCI DSS compliance program*
- *Annotation of a PCI DSS controls responsible, accountable, consulted, informed (RACI) matrix*
- *Periodic general security awareness for all personnel*
- *Periodic PCI DSS-specific payment card security and awareness training*
- *Role specific on the job training*
- **A3.2 Document and validate PCI DSS scope.**
  - Periodically document and confirm the accuracy of PCI DSS scope.
  - Risk assess all changes to systems or networks for any potential impact on the PCI DSS scope.
  - Post changes: Verify any changes against the relevant PCI DSS requirements.
  - Risk assessment of any organizational changes for any potential impact on the PCI DSS scope.
  - Periodic segmentation testing to validate PCI DSS scope.
  - Periodic data discovery audits.
  - Clear text monitoring for unauthorized transmissions.

<!-- PDF p. 365 (book p. 344) -->

**For example, develop a cohesive change management approach to ensure that all changes to the environment are subject to change management approval:**

- *Discussion and approval for any significant changes.*
  - *All changes are documented.*
  - *All changes are risk assessed and rollback considerations made.*
- **A3.3 Validate PCI DSS is incorporated into business-as-usual (BAU) activities.**
  - Monitor and respond to any critical security control failures.
  - Establish system and software life-cycle management.
  - Establish periodic internal auditing.

**For example, develop a cohesive compliance status and performance process:**

- *Periodic key risk indicators (KPIs) and key performance indicators are submitted to the PCI DSS security working group/committee.*
- *The results of the audit program are presented to the PCI DSS security working group/committee for discussion.*
- **A3.4 Control and manage logical access to the cardholder data environment.**
  - Conduct periodic reviews of in-scope standard and privileged user accounts.

**For example, develop a cohesive access management process, which includes the need for**

- *Formal access management practices, where all new and removed accounts are recorded and periodically reviewed by the PCI DSS security working group/committee*
- **A3.5 Identify and respond to suspicious events.**
  - Establish a methodology to rapidly identify and respond to ABNORMAL activities based upon known TTPs.

<!-- PDF p. 366 (book p. 345) -->

**For example, develop a cohesive and holistic monitoring and incident response process, which includes the need for**

- *The monitoring and incident response teams work together as a unit.*
- *The monitoring and incident response teams receive periodic on- the- job training.*
- *A library of scenarios is created and periodically practiced.*
- *A* **BLUE** *Team and* **RED** *Team style approach*[^43] *is embedded into the business.*
- *The penetration testing teams deliver periodic awareness training to the monitoring and incident response team members.*

Although not currently included in the main PCI DSS controls framework, it is extremely likely that elements of a team-based approach will be included in the next release of PCI DSS (v4.0). However, even if it is not added to any updates, it is important to remember that the PCI DSS controls frameworks are your MINIMUM requirements and you should seek to develop a team-based approach, where each team is fully supportive of each other and becomes habitualized into communicating with each other.

[^43]: https://csrc.nist.gov/Glossary/Term/Red-Team-Blue-Team-Approach
