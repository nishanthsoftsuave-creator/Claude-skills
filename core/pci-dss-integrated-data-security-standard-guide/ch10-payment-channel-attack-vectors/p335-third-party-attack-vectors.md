---
title: "Third-Party Attack Vectors"
book: pci-dss-integrated-data-security-standard-guide
chapter: 10
source_pages: "335-336"
format: source-text
---
# Third-Party Attack Vectors
(Source: PDF pp. 335-336)

<!-- PDF p. 335 (book p. 313) -->

Increasingly, if an attacker is unable to directly target an organization, they will seek to identify associated company relationships, where they can exploit vulnerabilities/poor practices of a third party in order to gain lateral movement or access to the data of their primary targets:

- **Supply Chain Compromises**

Supply chain compromise is the manipulation of products or product delivery mechanisms prior to receipt by a final consumer for the purpose of data or system compromise.

Attacks on your Supply chains can take place at any stage including

- Manipulation of development tools
- Manipulation of a development environment
- Manipulation of source code repositories (public or private)
- Manipulation of source code in open source dependencies
- Manipulation of software update/distribution mechanisms
- Compromised/infected system images
- Replacement of legitimate software with modified versions
- Sales of modified/counterfeit products to legitimate distributors
- Shipment interdiction

While supply chain compromises can impact any component of hardware or software, attackers will often focus on using malicious additions to legitimate software, within the software distribution or update channels.

The distribution of malicious software can be distributed to a broad set of consumers but only move on to additional tactics on specific victims or to specific individuals.

<!-- PDF p. 336 (book p. 314) -->

- Extra caution should be applied when considering the use of popular open source projects, as these may have been targeted for the delivery of malicious software.
  - Only use authorized/approved software from reputable sources.
- **Trusted Relationships**

Attackers seek to gain unauthorized access through trusted third- party relationship, exploiting existing connections, which may not be protected or are subject to less scrutiny than standard mechanisms of gaining access to a network.

It is common for businesses to allow elevated access to second-or third-party external providers, in support of the management internal systems, as well as cloud-based environments, for example:

- IT services contractors
- Managed security providers
- Infrastructure contractors

Third-party access should be treated in exactly the same manner as all other access management procedures, ensuring that all access requests are approved and based on strict restrictions, against specific role requirements, and all third-party access is subject to periodic reviews (confirm that the access remains appropriate).
