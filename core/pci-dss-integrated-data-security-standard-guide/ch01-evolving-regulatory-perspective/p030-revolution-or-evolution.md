---
title: "Revolution or Evolution?"
book: pci-dss-integrated-data-security-standard-guide
chapter: 1
source_pages: "30-36"
format: source-text
---
# Revolution or Evolution?
(Source: PDF pp. 30-36)

<!-- PDF p. 30 (book p. 6) -->

Often regarded as the revolution of data privacy laws, in May 2018 the European Union (EU) introduced 99 Principles of data privacy that applied to ALL organizations provisioning goods or services to EU members or monitoring the behavior of EU members.[^7]

**Figure 1-6.** *UK Motoring Timeline*

[^7]: https://gdpr-info.eu/art-3-gdpr/

<!-- PDF p. 31 (book p. 7) -->

This was the EU General Data Protection Regulation (GDPR),[^8] which had a global reach and had considerably larger administrative fines:[^9]

- **Tier 1**

Up to €**10 Million** or, in the case of an undertaking, up to **2%** of the total worldwide annual turnover of the preceding financial year, whichever is higher

- **Tier 2**

Up to **€20 Million** or, in the case of an undertaking, up to **4%** of the total worldwide annual turnover of the preceding financial year, whichever is higher

This includes the requirement to maintain secure data processing:

- The basic principles for processing, including conditions for consent, pursuant to Articles 5, 6, 7, and 9
  - *Processed in a manner that ensures appropriate security of the personal data, including protection against unauthorized or unlawful processing and against accidental loss, destruction or damage, using appropriate technical or organizational measures (“integrity and confidentiality”)*

Previously, under the earlier legislation, the administrative fines had been limited to a maximum of **€1 Million**. Suddenly, businesses were starting to recognize the need to embed security into their Business-As-Usual (BAU) processes – something that was introduced into PCI DSS, in November 2013, with the release of version 3.0.

The enhancement to the EU Data Privacy laws included the requirement for Data Controllers and Data Processors to notify both the Regulators and the affected Data Subjects within 72 hours of a data breach that is suspected to impact the Data Subjects. This particular requirement is a game changer for data privacy, as it supports timely mitigation against data theft, allowing the monitoring to detect and deny potential malicious use.

The introduction of the EU GDPR created a ripple effect across the globe,[^10] with other countries enhancing or implementing additional data privacy laws being introduced.

[^8]: https://gdpr.eu/
[^9]: https://gdpr-info.eu/issues/fines-penalties/
[^10]: www.dlapiperdataprotection.com/

<!-- PDF p. 32 (book p. 8) -->

## Europe

- UK Data Privacy Act 2018
  - Aligned with EU GDPR
- EU Directive on Security of Network and Information Systems (“NIS Directive”)[^11]
  - **Scope**
    - “Operators of Essential Services” (OES)
    - “Relevant Digital Service Providers” (RDSPs)
  - **Penalties**
    - **€20 million** or **4%** of annual global turnover – whichever is higher
- EU Privacy and Electronic Communications Regulations (PECR)[^12]
  - **Scope**
    - Organizations that provide a public electronic communications network or service
    - Organizations that market by phone, email, text, or fax; use cookies or a similar technology on your web site; or compile a telephone directory (or a similar public directory)
  - **Penalties**
    - Up to £500,000

[^11]: https://ec.europa.eu/commission/presscorner/detail/en/MEMO_16_2422
[^12]: https://ico.org.uk/for-organisations/guide-to-pecr/

## Canada

- Personal Information Protection and Electronic Documents Act (PIPEDA)[^13]

[^13]: www.priv.gc.ca/en/privacy-topics/privacy-laws-in-canada/the-personal-information-protection-and-electronic-documents-act-pipeda/

<!-- PDF p. 33 (book p. 9) -->

## United States

- US Federal Trade Commission (FTC)
  - Has jurisdiction over a wide range of commercial entities under its authority to prevent and protect consumers against unfair or deceptive trade practices, including materially unfair privacy and data security practices
  - California Consumer Privacy Act of 2018 (CCPA)
    - Effective January 1, 2020
  - Massachusetts MA 201 CMR 1[^14]
    - The objectives of 201 CMR 17.00 are to ensure the security and confidentiality of customer information in a manner fully consistent with industry standards, protect against anticipated threats or hazards to the security or integrity of such information, and protect against unauthorized access to or use of such information that may result in substantial harm or inconvenience to any consumer.
  - Illinois 815 ILCS 530 – Personal Information Protection Act (PIPA)[^15]
  - New York[^16]
    - SHIELD Act[^17]
    - Identity Theft Protection and Mitigation Services Act[^18]

[^14]: www.mass.gov/doc/201-cmr-17-standards-for-the-protection-of-personal-information-of-residents-of-the/download
[^15]: www.ilga.gov/legislation/ilcs/ilcs3.asp?ActID=2702&ChapterID=67
[^16]: www.ropesgray.com/en/newsroom/alerts/2019/08/New-York-Updates-Privacy-Laws?utm_source=Mondaq&utm_medium=syndication&utm_campaign=View-Original
[^17]: https://legislation.nysenate.gov/pdf/bills/2019/S133
[^18]: https://legislation.nysenate.gov/pdf/bills/2019/A2374

<!-- PDF p. 34 (book p. 10) -->

## Australia

- Information Privacy Act 2014 (Australian Capital Territory)
- Information Act 2002 (Northern Territory)
- Privacy and Personal Information Protection Act 1998 (New South Wales)
- Information Privacy Act 2009 (Queensland)
- Personal Information Protection Act 2004 (Tasmania)
- Privacy and Data Protection Act 2014 (Victoria)

## China

- People’s Republic of China (PRC) Cyber security Law

## Japan

- The Act on the Protection of Personal Information (“APPI”)

## Argentina

- Personal Data Protection Law (PDPL)
  - Law 25 § 326
    - Includes the basic personal data rules. It follows international standards and has been considered as granting adequate protection by the European Commission.

## Malaysia

- Personal Data Protection Act 2010 (PDPA)

<!-- PDF p. 35 (book p. 11) -->

## Brazil

- Brazilian General Data Protection Law (LGPD)[^19]

[^19]: www.dlapiperdataprotection.com/index.html?t=law&c=BR

## India

- Personal Data Protection Bill 2018[^20]

[^20]: www.dlapiperdataprotection.com/index.html?t=law&c=IN

## Financial Services

Despite being heavily regulated, the Financial Services industry is not exempt from their applicable data privacy rules. However, if they are involved in the processing of any branded payment cards (Mastercard, Visa, American Express, JCB, Discover), they are expected to align to the PCI DSS and, under the recent changes to the Mastercard Rules (Chapter 2, para 2.2.7),[^21] have a formal Information Security program.

The strength of the PCI DSS controls framework has been recognized by the Regulators (e.g., Information Commissioner’s Office (ICO),[^22] Federal Trade Commission (FTC),[^23] etc.), with it being noted that in the event of a personal data breach, the effectiveness of an organization’s PCI DSS compliance program will be taken into account.

Note it is important to remember that the pCi Dss does not incorporate all of the data privacy requirements and only provides a baseline against the Cyber security, information security, and physical security domains and omits the rights of the individual and the need for resilience. the focus of the pCi Dss is to ensure that the Confidentiality and integrity of the payment card data and supporting information systems are protected.

[^21]: www.mastercard.us/content/dam/mccom/global/documents/mastercard-rules.pdf
[^22]: https://ico.org.uk/for-organisations/guide-to-data-protection/guide-to-the-general-data-protection-regulation-gdpr/security/
[^23]: www.venable.com/insights/publications/2019/02/ftc-2019-insights-and-priorities-for-the-payments

<!-- PDF p. 36 (book p. 12) -->

In the event that a financial services company were to be compromised and personal data is stolen, they could be liable to be penalized from a variety of regulators and, in some countries, private litigation.

This has been highlighted through numerous penalties levied against Financial Services companies:

- **2016**:[^24] Financial Conduct Authority (FCA) fines Tesco Personal Finance plc (Tesco Bank) **£16.4 Million** for failing to exercise due skill, care, and diligence in protecting its personal current account holders against a cyber-attack.
  - 136,000 current accounts frozen, following “online criminal activity,” resulting in the theft of funds from at least 20,000 customers
- **2017**:[^25] Federal Trade Commission (FTC) fines Equifax up to **$700 Million**, as part of a settlement with federal authorities over a data breach in 2017.
  - 209,000 credit card details
- **2018**:[^26] Ireland’s central bank fines the Bank of Montreal, Toronto, **€1.25 million** for breaching license conditions.
  - 90,000 clients of the Canadian banks Simplii and Bank of Montreal (BMO).
  - Simplii and BMO are now facing a class action lawsuit, with those involved arguing that the banks failed to properly protect sensitive information.
- **2019**:[^27] FTC investigating the Capital One breach.
  - **106 Million** credit card customers and credit card applicants in the United States and Canada

[^24]: www.fca.org.uk/news/press-releases/fca-fines-tesco-bank-failures-2016-cyber-attack
[^25]: https://techcrunch.com/2019/07/22/equifax-fine-ftc/
[^26]: www.ctvnews.ca/business/bmo-fined-1-25m-euros-by-ireland-s-central-bank-for-breaching-licence-conditions-1.4399691
[^27]: www.consumer.ftc.gov/blog/2019/07/capital-one-data-breach-time-check-your-credit-report
