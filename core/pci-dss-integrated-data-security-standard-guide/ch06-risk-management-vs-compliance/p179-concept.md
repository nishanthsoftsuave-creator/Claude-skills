---
title: "Concept"
book: pci-dss-integrated-data-security-standard-guide
chapter: 6
source_pages: "179-185"
format: source-text
---
# Concept
(Source: PDF pp. 179-185)

<!-- PDF p. 179 (book p. 156) -->

Rather than regarding the protection of your consumers’ payment card information as a mandatory obligation, look at this as being a business investment to ensure that your most critical business systems and operations are secured to a level that your business feels comfortable with *(Risk Appetite, Risk Tolerance, etc.)*.

Within your business, you will have a number of critical data paths (e.g., Intellectual Property, Customer data, Account information, Marketing, etc.), and for the payment card industry, these are termed as payment channels[^5] (e.g., e-Commerce, mail order telephone order (MOTO), face to face, mobile, etc.). It is essential that these critical data paths be appropriately risk managed and protected by a company-wide security strategy, with the payment channels (involving payment card) having the PCI DSS security controls applied against them.

Essentially, you are likely to have a hierarchy of different critical data paths where you may choose to use a single data security controls framework or a “mix and match” suite of data security controls framework to ensure that your business has a suitable defensive profile, for example:

- **Corporate Governance**
  - COBIT 2019[^6]
- **Cyber Resiliency**
  - NIST SP 800-160, v2[^7]
- **Public-facing, Internet-facing, business operations**
  - CIS 20 Critical Security Controls, v7.1[^8]
- **MOTO and e-Commerce**
  - PCI DSS, v3.2.1[^9]

[^5]: https://blog.pcisecuritystandards.org/securing-emerging-payment-channels
[^6]: www.isaca.org/cobit/pages/default.aspx
[^7]: https://csrc.nist.gov/publications/detail/sp/800-160/vol-2/final
[^8]: www.cisecurity.org/controls/cis-controls-list/
[^9]: www.pcisecuritystandards.org/documents/PCI_DSS_v3-2-1.pdf?agreement=true&t ime=1579004557174

<!-- PDF p. 180 (book p. 157) -->

- **Financial data**
  - Sarbanes-Oxley Act 2002 (SOX)[^10]
- **Health Information**
  - Health Insurance Portability and Accountability Act 1996 (HIPPA)[^11]
- **Manufacturing systems**
  - NIST SP800-82, r2[^12]
- **Customer Personal Data Records**
  - ISO/IEC 27701:2019[^13]
  - NIST Privacy Framework[^14]
- **Company Sensitive Data Records**
  - ISO/IEC 27001:2013[^15]
- **Securing Cloud Services**
  - ISO/IEC 27017:2015[^16]
- **Personal Data Processing in Public Clouds**
  - ISO/IEC 27018:2019[^17]
- **External Audit: Third-Party/Supplier Assurance**[^18]
  - NIST Cyber Security Framework, v1.1[^19]

[^10]: www.soxlaw.com/
[^11]: www.hhs.gov/hipaa/index.html
[^12]: https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-82r2.pdf
[^13]: www.iso.org/standard/71670.html
[^14]: www.nist.gov/privacy-framework
[^15]: www.iso.org/standard/54534.html
[^16]: www.iso.org/standard/43757.html
[^17]: www.iso.org/standard/76559.html
[^18]: www.prevalent.net/compliance/nist-sp-800-53r4-and-nist-csf-v1-1-compliance/
[^19]: www.nist.gov/cyberframework

<!-- PDF p. 181 (book p. 158) -->

Each of these controls frameworks will have commonalities and need to be mapped against each other to ensure that there are no duplication of efforts and to ensure that a single common control[^20] can be applied, where the control requirement is applied against multiple critical data paths. Without this, you will increase the potential for confusion and misinterpretation of the rules that apply to specific business operations.

Just the data privacy and security frameworks are complicated enough, without considering any other industry controls frameworks that may provide additional assurance and potential benefits to your business, for example:

- **Corporate Risk Management**
  - ISO 31000:2018[^21]
- **Occupational Health and Safety**
  - ISO 45001:2018[^22]
- **Quality Management**
  - ISO/IEC 9000[^23]

Whichever standards or controls frameworks you are mandated, or choose, to apply, you need to ensure that they are effectively being applied to reduce your inherent risks to an acceptable level and that they can provide both continued assurance to your key stakeholders and any evidence needed for your compliance requirements.

In addition, it is important to remember that your data privacy and security programs are heavily reliant on the “Human Factor” and, as such, it is almost inevitable that mistakes will happen. Therefore, it is important that your various security controls frameworks can be periodically tracked and monitored against their effectiveness to reduce your business’s inherent risks.

It is interesting to see that the Canadian Government have introduced the concept of Baseline Security Controls[^24] as a recommended way for Canadian businesses to enhance their security profiles.

[^20]: https://commoncontrolshub.com/
[^21]: www.iso.org/iso-31000-risk-management.html
[^22]: www.iso.org/standard/63787.html
[^23]: www.iso.org/iso-9001-quality-management.html
[^24]: https://cyber.gc.ca/en/introduction-baseline-controls

<!-- PDF p. 182 (book p. 159) -->

In the case event of an event, system compromise, or data breach, how much support will your various controls programs provide to your business and how can these programs deliver the assurance expectations of your key stakeholders?

## How Is This Achieved?

Measuring the effectiveness of your numerous controls should not be limited to a linear response (In Place/Not In Place) and especially not when you are measuring the effectiveness of a process. Therefore, it is beneficial that the “Human Factor” is measured based on the perceived maturity[^25] of the process.

Periodic risk and control effectiveness reporting should be produced in the form of Information Security performance metrics[^26] (e.g., key risk indicators (KRIs) and key performance indicators (KPIs)) to ensure that the key decision-makers are fully apprised of any issues that may potentially impact your business operations and to ensure that timely intervention and investment can be actioned.

**Table 6-2.** *Vehicle Warning Lights*

Think of it like the warning lights on your motor vehicle….

Anti-Lock Brake Warning

*[Figure omitted]*

Braking System Warning

*[Figure omitted]*

(*continued*)

[^25]: https://cmmiinstitute.com/pm
[^26]: https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-55r1.pdf

<!-- PDF p. 183 (book p. 160) -->

Think of it like the warning lights on your motor vehicle….

Low Fuel Warning

*[Figure omitted]*

Low Oil Warning

Engine Warning

*[Figure omitted]*

Seatbelt Warning

*[Figure omitted]*

Low Coolant Warning

*[Figure omitted]*

- Much the same as your data privacy and security strategies, these warning lights

remain invisible until they need to illuminate to warn you that you may have an issue that needs to be investigated.

- Without these KPI/KRI warning lights, you will remain oblivious to the potential risks or

dangers that require further investigation.

- If your vehicle has automated monitoring, why would you not consider doing the same

for your business?

**Table 6-2.** (*continued*)

<!-- PDF p. 184 (book p. 161) -->

The integration of your various controls should be aligned with your corporation’s risk management framework and, ideally, managed within a centralized risk solution, enabling appropriate access for the business managers and key stakeholders to instantly access the “State of the Nation” data that is of concern to them.

However, it is important to note that this can also be achieved through a more manual and labor-intensive collation of numerous spreadsheets, presentations, and documents.

When considering the advantages and disadvantages of using a commercial of the shelf (COTS) solution vs. a more manual approach, it is important to remember to create a business case. This will ensure that your organization appreciates the potential advantages or resources disadvantages associated with the automated vs. manual (in- house) options that are available to the business.

## Qualitative vs. Quantitative Risk Assessment

Additionally, you will need to decide on whether you will present the results of your risk assessments as Qualitative or Qualitative risk assessments.

### Qualitative Risk Assessments

The qualitative risk assessment is the most common form of risk assessment.

Through the use of ordinal rating scales (e.g., 1–5) or assigning relative ratings (high, medium, low or red, yellow, green), various risks can be plotted on a heat map with Likelihood (or Probability) on one axis and the impact on the other.

Where the risks are placed in a qualitative assessment is inherently subjective and makes the prioritization of risks extremely difficult. For example, if you have ten red (5 x 5) risks, which is the most urgent? In addition, a qualitative approach does not provide a systemic approach to aggregate risks.

Finally, these risk assessments tend to be drawn toward worst case loss scenarios, based upon the specific values that are available, as opposed to assigning a value from a scale.

<!-- PDF p. 185 (book p. 162) -->

## Quantitative Risk Assessments

Qualitative risk assessments utilize knowledge and experience to determine the risk probability, while a quantitative risk assessment relies on objective, measurable data to provide insights into your risk management process.

A quantitative risk assessment gives you the data you need to accurately predict future outcome and helps strengthen your risk management strategy moving forward by communicating to you any contingency you need to properly address a risk to your satisfaction.

As long as the information you have is dependable, a quantitative risk assessment can create more realistic targets than a qualitative assessment.

## Risk Appetite/Tolerance

It is important that your business defines the acceptable risk appetites/tolerance[^27] across the different hierarchy levels within your organization. Where the perceived risks (post risk assessment) are within a business manager’s appetite/tolerance, they are permitted to sign off a suitable risk treatment option. However, where this exceeds their risk appetite/tolerance, it must be escalated for more senior sign off.

[^27]: www.theirm.org/what-we-say/thought-leadership/risk-appetite-and-tolerance/
