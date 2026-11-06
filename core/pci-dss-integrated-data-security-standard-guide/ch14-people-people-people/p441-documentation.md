---
title: "Documentation"
book: pci-dss-integrated-data-security-standard-guide
chapter: 14
source_pages: "441-453"
format: source-text
---
# Documentation
(Source: PDF pp. 441-453)

<!-- PDF p. 441 (book p. 420) -->

*[Figure omitted]*

Your supporting documentation to your Data Privacy and Security strategy will have a natural hierarchy. This is especially true with PCI DSS, where specific policies and procedures may have an impact on other control areas and where some policies are applicable to all and others are role specific.

The Document Hierarchy Tree can be seen in Figure 14-5.

**Figure 14-4.** *Documentation*

<!-- PDF p. 442 (book p. 421) -->

*[Figure omitted]*

Your document sets should be sequential and complementary to each other and should not act in conflict to another document within the document hierarchy. Consequently, you may find the identification and mapping of your policies, procedures, and supporting documents into a hierarchy tree extremely useful in ensuring that you can trace the documents to their relevant departments and the inter-related documents.

I’m still amazed to see organizations who “Tick the Box” for compliance, by thinking that just maintaining a suite of supporting policies and operational procedures and making them available on their corporate intranet makes them compliant and, more importantly, secure. Just having a new starter read and acknowledge the policies at the start of their employment does not help when the technology changes, or they have been employed for several years, picking up multiple bad habits along the years.

The effectiveness of your documentation is enhanced through the periodic reminders of the dangers being mitigated by the policies/procedures and the risks to the business, in the event of the policies/procedures not being followed.

**Figure 14-5.** *Document Hierarchy Tree*

<!-- PDF p. 443 (book p. 422) -->

The creation and maintenance of effective policies and procedures should be done in conjunction with the target audience, with feedback being encouraged to ensure that they remain effective and relevant to your business operations.

## Policies Development (Establishing the Laws)

Your supporting policies do not need to be “War and Peace” and need to be relevant to your organization. Therefore, if you are considering purchasing “Out of the Box” policy templates, ask yourself how much tailoring of the policies you will need to make them a comfortable fit for your company.

Could you create better rules through the use of a number of short policy statements within a single document which clearly outlines the following?

### 5WH

- **W**hat is the purpose?
- **W**hy is it important?
- **W**ho it applies to?
- **W**hen it must be followed?
- **W**here is it applicable to?
- **H**ow personnel refresh their understanding and how and when to report incidents?

At a minimum the contents of your policy should clearly describe the following using simple/high-level terminologies which are easy for all the intended audience to understand:

1. **Purpose**

First state what the purpose of the policy is.

2. **Audience**

Define who the audience is, to whom the policies apply.

3. **Information security objectives**

Provide agreed-on and well-defined objectives for strategy and security.

<!-- PDF p. 444 (book p. 423) -->

4. **Authority and access control**

Who is the owner and approver of the policies?

5. **Data classification**

Classification helps clarify what data is important and why.

6. **Data support and operations**

Where the policy applies.

7. **Security awareness and behavior**

How personnel are expected to act and the potential consequences for non-adherence to these rules.

8. **Responsibilities, rights, and duties of personnel**

Who is involved and what are their responsibilities?

Remember:

- the longer and more complex that you make your policies, the less chance of your intended audience being able to remember it and the greater the chance that the readers will skip through the content.
- Consider tailoring the policy statement contents to suit the full ranges of your target audiences.
- Consider the potential benefits of using local languages (if applicable).
- Consider the potential benefits of supplementing your policy statements with a pictorial representation.
- a picture paints a thousand words.

<!-- PDF p. 445 (book p. 424) -->

In order to set the “Tone at the Top,” your policies should be subject to periodic review and approval by senior management and a record to these changes be maintained and recorded in the policies, for example:

| Version<br>No. | Date of<br>Review | Date of<br>Approval | Reviewed/<br>Changed by | Approved by | Summary of<br>Changes |
|---|---|---|---|---|---|
| V1.0 | December<br>10, 2017 | December<br>10, 2017 | Information<br>Security Manager | Finance<br>Director | Initial release |
| V1.1 | December<br>09, 2018 | December<br>09, 2018 | Information<br>Security Manager | Finance<br>Director | annual review |
| V1.2 | December<br>09, 2019 | December<br>09, 2019 | Information<br>Security Manager | Finance<br>Director | annual review |
| V2.0 | June 01,<br>2019 | June 01,<br>2019 | Information<br>Security Manager | Finance<br>Director | Changes to scope statement, following an acquisition |

As you can see, the secondary digit reflects the recording of minor changes to the policies, whereas a change in the primary digit reflects a significant change to policy:

- Significant changes to a policy statement should be communicated out to all applicable personnel, and all personnel should make note of the changes that have been made.
- Personnel should be encouraged to periodically refresh their knowledge of the rules outlined within the policy statements that apply to an individual’s roles and responsibilities.

In the event of an incident, as part of the post-incident reviews, it is important to include a review of any supporting policy statements. The purpose is to confirm that the policy statement remains effective and to validate whether this was a willful or negligent act.

Representative feedback should be encouraged from across the intended target audience to ensure that the content remains appropriate and relevant while clearly articulating what is needed to reduce the associated risks.

<!-- PDF p. 446 (book p. 425) -->

Senior Management will be accountable for the approval of the policy statements, while a security steering committee should be responsible for ensuring contributing and reviewing the content.

| Requirement | Policy Statements |
|---|---|
| 1 | • Mobile Device |
| 2 | • Secure Systems configuration |
| 3 | • Secure Data handling, Storage, and Disposal<br>• encryption Key life-cycle Management |
| 4 | • Secure transmission |
| 5 | • anti-virus |
| 6 | • Vulnerability, patch, and risk Management<br>• Change Management<br>• Secure Software Development |
| 7 | • access Control |
| 8 | • access Control |
| 9 | • physical Security<br>• Media handling, storage, and disposal |
| 10 | • Monitoring |
| 11 | • Security testing |
| 12 | • Information Security<br>• acceptable Usage<br>• pCI DSS Charter<br>• Security Vetting<br>• third-party Management<br>• Security Incident response and Breach reporting<br>• Security auditing |

<!-- PDF p. 447 (book p. 426) -->

## Procedures

Think of your procedures as being your “Standard Operating Procedures” (SOPs), which clearly document the steps that all personnel must adhere to.

Your SOPs are designed to be at a department level, developed to articulate the steps that everyone must follow.

The SOPs should align to the overarching policy statements, so that if all personnel are trained and strictly adhere to the appropriate process steps, they will automatically be meeting the objective of the policy statement:

- It may be that there are multiple SOPs that are associated with a single policy statement.

The department/team managers will be accountable for ensuring that the SOPs remain aligned to meet the objectives of the overarching policy statements and that the content is appropriate for their team members and that all their team members adhere to their SOPs.

Team members should be encouraged to provide feedback on the suitability of the content to their duties.

There are no formal template requirements and can be as simple as a process flow diagram.

<!-- PDF p. 448 (book p. 427) -->

*[Figure omitted]*

**Figure 14-6.** *Example Firewall Change Process Flow*

<!-- PDF p. 449 (book p. 428) -->

| Requirement | Procedures |  |
|---|---|---|
| 1 | • Firewall/router secure configuration build standards<br>• Firewall/router change Sops |  |
| 2 | • Secure System configuration build standards<br>• Secure System configuration build Sops<br>• Secure Wireless configuration build standards<br>• Secure Wireless configuration Sops |  |
| 3 | • Secure Data handling and Disposal Sops<br>• Key Management Sops | • Secure key life-cycle management |
| 4 | • Secure transmission Sops |  |
| 5 | • anti-virus Sops |  |
| 6 | • Vulnerability, patch, and risk Management Sops<br>• Change Management Sops<br>• Secure Software Development Sops |  |
| 7 | • role-Based access Control (rBaC) Sops |  |
| 8 | • access Control Sops |  |
| 9 | • operational requirements (ors)<br>• physical access Control Sops<br>• physical Security Sops<br>• Visitor Sops<br>• Media handling Sops<br>• physical inspection Sops |  |
| 10 | • Monitoring Sops |  |
| 11 | • rogue device inspection and response Sops<br>• Security testing Sops | • Vulnerability detection and remediation<br>• penetration testing<br>• Segmentation testing<br>• alerting response<br>(continued) |

<!-- PDF p. 450 (book p. 429) -->

| Requirement | Procedures |
|---|---|
| 12 | • policy reviews Sops<br>• risk assessment Sops<br>• Security education/awareness Sops<br>• Security vetting Sops<br>• third-party management Sops<br>• Security Incident Sops |

## Supporting Documents

Within the PCI DSS controls framework, there is a specific supporting document that is needed to evidence that you have an appropriate formalized data privacy and security program established.

Requirement Procedures

1

- Firewall/router change records
- high-level network diagram
  - In-scope and out-of-scope environment
    - Like a Country Map
      - Showing location of major towns, cities, and connecting roads
      - The delineation of boundaries (between trusted and untrusted)
- Detailed network diagram
  - In-scope environment
  - like a City/town Map
    - Showing housing estates and street level details
    - Detailing the connectivity of internal, in-scope, supporting systems
- Data Flow Diagrams
  - Identifying the support systems that are involved in the processing, storage, or transmission of payment card data (Cat a)
  - Identifying any adjacent support systems (Cat B), which may impact the Cat a systems
- ping tests
- Command prompts
- asset discovery scans (*continued*)

<!-- PDF p. 451 (book p. 430) -->

Requirement Procedures

2

- System configuration audit reports
- asset inventory
  - Cat a systems
  - Cat B systems
    - aligned to network and data flow diagrams

3

- Quarterly data discovery audits
- encryption configuration audits

4

- Secure transmission audits
  - Wireshark
  - SSl labs

5

- anti-virus (aV) policy vendor documents
- anti-virus checks
  - eICar[^7] testing
  - WICar[^8] testing
- anti-virus audit logs.
  - Showing records of any aV alerting.
- anti-virus system configurations

6

- Currently vulnerability and patch reports
- risk assessments
- Change tickets
- Network diagrams showing separation of environments
  - live
  - test
  - Development
- Code review checklists
- Internal Software security test reports
- annual web application test reports
  - Or after any significant changes
- Web application Firewall logs

(*continued*)

[^7]: www.eicar.org/
[^8]: www.wicar.org/

<!-- PDF p. 452 (book p. 431) -->

Requirement Procedures

7

- rBaC requests
- aD Group policy configurations

8

- access request tickets
- User account system configurations
- System access configurations

9

- CCtV recordings
- electronic automated access Control System (eaaCS) logs
- Visitor
- Media log
- Inspection schedule
- Inspection reports

10

- audit logs
- linked audit trails
- File Integrity logs
- time synchronization configurations
- Secure audit storage configurations
- logs and events (minimum 12 months)
- records of investigations/analysis of suspicious events (e.g., helpdesk tickets)

11

- Inventory of wireless enabled devices
- Quarterly internal scan reports
- Quarterly external scan reports
- Follow-up post-remediation scan reports
- annual penetration testing
  - Or after any significant changes
- post-remediation penetration retesting
- Six-month segmentation testing
- alerting tickets
  - IDS/IPS
  - Change Detection

(*continued*)

<!-- PDF p. 453 (book p. 432) -->

Requirement Procedures

12

- policy review/change tables
- annual policies signed acknowledgment
- responsible, accountable, Consulted, Informed (raCI) Matrix
- Job descriptions
- Security Steering committee minutes
- annual training and awareness material
  - PCI DSS
  - Secure software development
- training attendance records
- Security vetting checks
- Contracts
- Due diligence inspections
- aoCs
- pCI DSS controls raCI
- Security incident playbooks
- Security Incident response testing
  - Annually (at a minimum)
- post-incident/testing minutes
- Security audit reports
