---
title: "Introduction"
book: pci-dss-integrated-data-security-standard-guide
chapter: 15
source_pages: "468-471"
format: source-text
---
# Introduction
(Source: PDF pp. 468-471)

<!-- PDF p. 468 (book p. 448) -->

I recall the furious rantings of a business Director, who was trying to understand the first-line[^3] Information Security team’s[^4] cyber security strategy and was unable to see how this was delivering a cohesive approach to effectively defend against their known threats. Consequently, they had two consistent responses:

- **“Are we ‘Boiling the Ocean’?”**
  - Are we investing in the highest priority areas or are we trying to fix EVERYTHING?
- **“So what?”**
  - What does this mean? Should I be worried? What is the potential impact on the business?

Until this point, I had never appreciated the frustration of Senior Management, as I had been engrained into the belief that developing and maintaining secure environments just makes common sense. However, in business, a data privacy and security program needs to make business sense, for example:

When considering the purchase of a 24/7 network detection solution, which monitors the potential use of malicious software, this might appear to be an essential investment. However, what if this “standalone” security service has an annual cost of around $500k and does not include the centralized monitoring of the systems logs?

[^3]: www.iia.org.uk/resources/audit-committees/governance-of-risk-three-lines-of-defence/
[^4]: First-line operational management has ownership, responsibility, and accountability for directly assessing, controlling, and mitigating risks.

<!-- PDF p. 469 (book p. 449) -->

- Could this potentially be an extremely expensive service that only notifies me once the attackers have initiated the final step (Actions On Objectives) of their Cyber Kill Chain[^5] without any detection of steps 1 to 6?
- Would this be too late to stop a mass exfiltration of data?
- Does this complement the other security tools and services?

This is where the integrated PCI DSS controls framework differs from the majority of the other Cyber/InfoSec controls frameworks, as each control is compartmentalized against a specific scope (payment card data systems and impacting/connecting IT systems). The Payment Card Industry Security Standards Council have identified the mitigation security controls that are needed to safeguard against the commonly known risks.

Applying these controls supports the creation of secure payment card data processing environments and can help create a team of security-aware personnel *(both in the engine room (IT systems support) and crew (data processing teams))*, who develop a greater understanding of what good practice looks like and who will be able to identify and report instances of ABNORMAL activities.

Even a small PCI DSS scope will provide interactions with other business areas. All of a sudden, you have an embedded security team that are interacting with other areas of the business. As a result, they will be encouraging good practice to other business departments.

Imagine that you are a software development business, which, in addition to providing PCI DSS compliant e-commerce solutions,[^6] provides creative branding, marketing and strategy, interactive, software development services.

As a result of your PCI DSS scope, all your web development services have security considerations embedded into them, something that both your PCI DSS clients and non-PCI DSS clients will appreciate. However, only your in-scope PCI DSS environment is subject to an annual PCI DSS onsite assessment. Additionally, you have more security-aware employees influencing other business departments that may be handling other types of sensitive data (personal, financial, intellectual property, coding, etc.), which may need to be processed, stored, and transmitted in a secure manner.

[^5]: www.lockheedmartin.com/en-us/capabilities/cyber/cyber-kill-chain.html
[^6]: www.gamcreative.com/

<!-- PDF p. 470 (book p. 450) -->

For example, customers’ personal data is increasingly being subject to legal requirements for secure processing:

- **European Union General Data Protection Regulation (EU GDPR: Article 32**[^7]

*“Implement appropriate technical and organizational measures to ensure a level of security appropriate to the risk.”*

- **Canada’s Personal Information Protection and Electronic Documents Act (PIPEDA): Principle 7**[^8]

*“Personal information shall be protected by security safeguards appropriate to the sensitivity of the information.”*

- **Singapore’s Personal Data Protection Act (PDPA): Data Protection by Design**[^9]

*“An organization shall protect personal data in its possession or under its control by making reasonable security arrangements to prevent unauthorized access, collection, use, disclosure, copying, modification, disposal or similar risks.”*[^10]

- **California Consumer Privacy Act of 2018 (CCPA)**[^11]

*“Implement and maintain reasonable security procedures and practices appropriate to the nature of the information to protect the personal information.”*

[^7]: www.privacy-regulation.eu/en/article-32-security-of-processing-GDPR.htm
[^8]: www.priv.gc.ca/en/privacy-topics/privacy-laws-in-canada/the-personal-information-protection-and-electronic-documents-act-pipeda/pipeda-compliance-help/pipeda-compliance-and-training-tools/pipeda_sa_tool_200807/#principle7
[^9]: www.pdpc.gov.sg/-/media/Files/PDPC/PDF-Files/Other-Guides/Guide-to-Data-Protection-by-Design-for-ICT-Systems-(310519).pdf
[^10]: https://sso.agc.gov.sg/Act/PDPA2012#P1VI-
[^11]: www.isipp.com/resources/full-text-of-the-california-consumer-privacy-act-of-2018-ccpa/

<!-- PDF p. 471 (book p. 451) -->

- **Australian Privacy Principles (APP): APP 11 – Security of personal information**[^12]

*“An APP entity must take reasonable steps to protect personal information it holds from misuse, interference and loss, as well as unauthorized access, modification or disclosure.”*

Consequently, with minimal effort, PCI DSS compliance is known to be extremely influential in enhancing other business areas, which may be subject to legal data protection requirements.

[^12]: www.oaic.gov.au/privacy/australian-privacy-principles-guidelines/chapter-11-app-11-security-of-personal-information/
