---
title: "Annual PCI DSS Assessment"
book: pci-dss-integrated-data-security-standard-guide
chapter: 16
source_pages: "497-504"
format: source-text
---
# Annual PCI DSS Assessment
(Source: PDF pp. 497-504)

<!-- PDF p. 497 (book p. 478) -->

Now that you understand what “Good” looks like, you are better placed to work in conjunction with your PMCSPs (QSACs). Whether you are a level 1 Merchant or Service Provider, you need to ensure that you are able to maintain your PCI DSS compliance. To achieve this, you need to be well prepared, which involves early planning and engagement and obtaining agreed guarantees from your chosen PMCSP (QSAC).

<!-- PDF p. 498 (book p. 479) -->

## Planning and Preparation

Having successfully achieved your annual PCI DSS compliance after a short period of recovery, it is important to review the findings/observations identified during the assessment and to take the opportunity to implement opportunities for improvement.

Next, as a team effort, start planning your schedule for the following year’s PCI DSS activities by identifying and scheduling the mandatory control actions (e.g., CTRL F of the latest version of PCI DSS).

See the following data for example.

Quarterly Activities

Data Discovery

- Identify person responsible for activity.
  - Schedule dates for activity.
- Identify and agree methodology to be used.
- Identify person responsible for review (Governance).
  - Schedule dates for review.
- Identify location for secure storage of supporting evidence (ASV reports, review comments, re-scans, etc.).

Rogue Wireless Checks

- Identify person responsible for activity.
  - Schedule dates for activity.
- Identify and agree methodology to be used.
- Identify person responsible for review (Governance).
  - Schedule dates for review.

Internal Vulnerability Scans

- Identify person responsible for activity.
  - Is the individual still independent, suitably trained, and skilled?
    - Schedule dates for activity.
- Identify person responsible for review (Governance).
  - Schedule dates for review.
- Identify personnel responsible for remediation activities.
  - Schedule potential deadlines for remediation activities.
    - Schedule potential dates for confirmatory re-scans.
- Identify location for secure storage of supporting evidence (ASV reports, review comments, re-scans, etc.).

(*continued*)

<!-- PDF p. 499 (book p. 480) -->

External Vulnerability (ASV) Scans

- Identify approved Scanning Vendor (aSV) responsible for activity.
  - Identify approved Scanning Vendor.
    - Consider 3 x potential vendors for the delivery of 4 x ASV scans over the year.
  - ensure that the vendors are on the approved list.[^8]
  - review contracts.
  - procure services of preferred aSV.
    - agree and schedule dates for activity.
- Identify person responsible for review (Governance).
  - Schedule dates for review.
- Identify personnel responsible for remediation activities.
  - Schedule potential deadlines for remediation activities.
    - Schedule potential dates for confirmatory re-scans.
- Identify location for secure storage of supporting evidence (ASV reports, review comments, re-scans, etc.).

Periodic Supplier Security Management

- Identify third-party suppliers.
  - review outsourced controls.
  - Identify Supplier relationship managers.
- engage with third-party Suppliers relationship managers.
- request evidence of the effectiveness of the management of their control responsibilities.

Internal Audits

- Identify person responsible for activity.
  - Schedule dates for activity.
- Identify and agree methodology to be used.
- Identify person responsible for review (Governance).
  - Schedule dates for review.
- Identify location for secure storage of supporting evidence (Reports, review comments, re-scans, etc.).

Security and Risk Steering Committee meetings

- review and discuss the results of the quarterly activities.
  - Document meeting minutes.

(*continued*)

[^8]: www.pcisecuritystandards.org/assessors_and_solutions/approved_scanning_vendors

<!-- PDF p. 500 (book p. 481) -->

½ Yearly Activities

| Firewall ruleset reviews | • Identify person responsible for activity.<br>• Identify and agree methodology to be used.<br>• Identify person responsible for review (Governance).<br>• Identify location for secure storage of supporting evidence (Reports, review | • Schedule dates for activity.<br>• Schedule dates for review. comments, re-scans, etc.). |
|---|---|---|
| Terminated User<br>Accounts | • Confirmation of six-month retention records of terminated user accounts. | • Identify person responsible for activity.<br>• Schedule dates for activity.<br>• Identify and agree methodology to be used.<br>• Identify person responsible for review (Governance).<br>• Schedule dates for review.<br>• Identify location for secure storage of supporting evidence (Reports, review comments, re-scans, etc.). |
| Network<br>Segmentation<br>Testing | • Identify person/vendor responsible for activity.<br>• Identify and agree methodology to be used.<br>• Identify person responsible for review (Governance).<br>• Identify location for secure storage of supporting evidence (Reports, review comments, re-scans, etc.). | • Schedule dates for activity.<br>• Schedule dates for review. |
| PMCSP (QSA)<br>Preparations | • Identify 3 X pmCSp (QSas) from the pCI SSC approved list:[^9] | • ensure that they are listed for your payment card processing environments.<br>• Issue request for tenders.<br>• review tenders and select best option.<br>(continued) |

[^9]: www.pcisecuritystandards.org/assessors_and_solutions/qualified_security_assessors

<!-- PDF p. 501 (book p. 482) -->

Penetration/Web Application Testing Preparations

- Identify 3 X testing Services from the pCI SSC approved list:[^10]
- review their proposed methodology to test your environment.
  - Issue request for tenders.
  - review tenders and select best option.

Incident Scenario workshop

- team development of plausible incident scenarios, for your company, based upon the latest threat intelligence feeds.
  - record and document scenarios into your playbook.

3/4 Yearly Activities

PMCSP (QSAC) Annual Assessment Preparations

- engage with pmCSp (QSaC) to agree and schedule the dates for the next annual assessment.
  - ensure that the pmCSp (QSaC) confirms the dates (commencement, onsite, report writing, report Qa, report delivery, etc.) and identifies the QSa/QSas that will be scheduled to complete the assessment.
  - proposal for their methodology.
    - This will enhance the efficiency of the service deliverables and ensure the expectations are agreed.
- Identify internal resources required.
  - Schedule their timings.
- Schedule the commencement date to ensure that the assessment and delivery of the report can be concluded to align with the annual compliance date.

Annual Activities

Policy reviews

- Carry out reviews of all supporting policies, Sops, and supporting documents.
  - record review details.
- ensure in-scope personnel have read and signed as having acknowledged and understood their applicable policies.

Risk reviews

- Carry out review of identified risks, recorded in the risk register.
- Identify and document any new risk assessments.

(*continued*)

[^10]: www.pcisecuritystandards.org/assessors_and_solutions/qualified_security_assessors

<!-- PDF p. 502 (book p. 483) -->

| Annual Security<br>Refresher training | • review records of training/nominal roles to ensure that all in-scope personnel have received pCI DSS refresher training. |
|---|---|
| Supplier<br>Management<br>Review | • Identify all in-scope third-party suppliers.<br>• engage with third-party suppliers.<br>• review contracts.<br>• review quarterly due diligence evidence.<br>• review third-party aoCs.<br>• Confirm understanding of outsourced pCI DSS services.<br>• third-party suppliers acknowledge their pCI DSS controls responsibilities. |
| Annual Security<br>Muster | • review quarterly internal audit reports. |
| Annual Security<br>Incident Response exercise | • test the effectiveness of the incident response plan.<br>• Document the testing and the post-incident review. |
| Asset Inventory review | • review hardware and software asset life-cycle dates.<br>• upcoming end-of-Life (eol)/end-of-Support (eoS) assets should be risk assessed and added to the risk register.<br>• plan to align changes to quieter period of operations and, where possible, scheduled with the annual penetration/web application testing.<br>• Minimize additional cost and impact. |
| Validate the effectiveness of the<br>PCI DSS program | • review output of Business-as-usual (Bau) activities and the internal audits, ensuring that the Sops remain effective. |

## Assessment Process

Having engrained the PCI DSS checks into your routine business operations, you will have all the evidence needed for your QSA to arrive onsite to validate that you are aligned with the PCI DSS controls framework.

<!-- PDF p. 503 (book p. 484) -->

For me, I would always align my approach to conducting a formal onsite PCI DSS assessment in the same manner that I would complete an RAF Police security investigation. This involved the application of a six-step methodical approach:

1. **Briefing**

Before engaging in the commencement of the PCI DSS assessment, I would request a meeting with all the in-scope members of the “In-scope” personnel. This would enable me to brief all considered on what they would I would be expecting from them and allow them the opportunity to ask any questions.

- Confirm agenda, timings, locations, etc.
  - *Typically, starting at requirement 12 and working backward toward requirement 1*
- Inform client of the QSA feedback process.

2. **Documenting reviews**

Next, I would do a “deep dive” analysis of the client’s policies, SOPs, and supporting documents and (if necessary) ask any confirmatory questions on the content.

- The results providing the content needed for the creation of my interview plans

3. **Interviews**

Employing some of the principles from the PEACE investigative interviewing model, each person with responsibilities would be interviewed so that they could provide independent accounts of their duties.

- The notes from these interviews would then be securely retained as supporting evidence.

4. **Processing observations**

Having reviewed the documentation and interviewed the in-scope personnel, each member of the team is then asked to demonstrate the practical application of their policies and SOPs.

- Supporting evidence is collated during these observations.

<!-- PDF p. 504 (book p. 485) -->

5. **Reporting write-up and Quality Assurance review**

Having collected all the supporting evidence and comprehensive notes from the onsite assessment, I was then able to work remotely to write up the draft RoC, following which the RoC would be subject to an independent peer review and returned for finalization of the draft version.

6. **Client Sign Off**

Finally, a review session is completed with the client to ensure that they understand the observations made and to help them identify opportunities for further improvement. Having completed the review session and made any updates, following the review session, the RoC is finalized and provided to the client.
