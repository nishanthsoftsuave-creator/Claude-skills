---
title: "Data Privacy"
book: pci-dss-integrated-data-security-standard-guide
chapter: 4
source_pages: "103-107"
format: source-text
---
# Data Privacy
(Source: PDF pp. 103-107)

<!-- PDF p. 103 (book p. 79) -->

Changing personal data regulations requires organizations to ensure that personal data is handled responsibly and in a manner that the data subject would approve and to ensure that their personal data is securely retained, processed, and transmitted in a manner that will ensure that it is adequately protected across its data life cycle.

Varonis[^9] defines Data Privacy as

**Figure 4-3.** *An Integrated Data Security Strategy*

[^9]: www.varonis.com/blog/data-privacy/

<!-- PDF p. 104 (book p. 80) -->

Data privacy or information privacy is a branch of data security concerned with the proper handling of data – consent, notice, and regulatory obligations. More specifically, practical data privacy concerns often revolve around:

Whether or how data is shared with third parties.

How data is legally collected or stored.

Regulatory restrictions such as GDPR, HIPAA, GLBA, or CCPA.

Numerous updates to global data privacy laws now legislate that payment card data is deemed to be personal data, for example:

- **Article 4: European Union General Data Protection Regulation (EU GDPR)**

“Personal data” means any information relating to an identified or identifiable natural person (“data subject”); an identifiable natural person is one who can be identified, directly or indirectly, in particular by reference to an identifier such as a name, an identification number, location data, an online identifier, or to one or more factors specific to the physical, physiological, genetic, mental, economic, cultural, or social identity of that natural person.

- A payment card uses the PAN as an Identification number and contains the Initials and Surname of the cardholder.
- **Personal Information Protection and Electronic Documents Act (PIPEDA)**

“Information about an identifiable individual,” essentially any data obtained in the course of a commercial activity.

- Payment card data is used in the course of commercial activities.
- **California Consumer Privacy Act (CCPA)**

<!-- PDF p. 105 (book p. 81) -->

Information that identifies, relates to, describes, is reasonably capable of being associated with, or could reasonably be linked, directly or indirectly, with a particular consumer or household; such as a real name, alias, postal address, unique personal identifier, online identifier Internet Protocol address, email address, account name, social security number, driver’s license number, passport number, or other similar identifiers.

- Payment cards absolutely relate to a specific consumer.

Consequently, any business handling payment card data needs to ensure that it is handled in accordance with their appropriate Data Privacy regulations/laws, and the easiest way to achieve this is to apply and align with a suite of Privacy Principles and incorporate PCI DSS into these principles. To better aid your business’s data privacy program in meeting the requirements of the various privacy regulations, ISACA recommends the use of their 14 privacy principles:[^10]

1. Choice and Consent

2. Legitimate purpose specification

- PCI DSS
  - *Requirement 3*

3. Personal information and sensitive information life cycle

- PCI DSS
  - *Requirement 3*

4. Accuracy and Quality

5. Openness, Transparency, and Notice

6. Individual Participation

[^10]: https://next.isaca.org/bookstore/cobit-5/ipp

<!-- PDF p. 106 (book p. 82) -->

7. Accountability

- PCI DSS
  - *Requirement 12*

8. Security Safeguards

- PCI DSS
  - *Requirement 1*
  - *Requirement 2*
  - *Requirement 3*
  - *Requirement 4*
  - *Requirement 5*
  - *Requirement 6*
  - *Requirement 9*

9. Monitoring, Measuring, and Reporting

- PCI DSS
  - *Requirement 10*
  - *Requirement 11*
  - *Requirement 12*

10. Preventing Harm

- PCI DSS
  - *Requirement 12*

11. Third-party/Vendor Management

- PCI DSS
  - *Requirement 12*

12. Breach Management

- PCI DSS
  - *Requirement 12*

13. Security and Privacy By Design

<!-- PDF p. 107 (book p. 83) -->

- PCI DSS
  - *Requirement 1*
  - *Requirement 2*

14. Free flow of Information and Legitimate Restriction

- PCI DSS
  - *Requirement 7*
  - *Requirement 8*
  - *Requirement 9*

As you can see, approximately **71%** of the data privacy regulatory requirements can be covered through the application of solely the PCI DSS controls framework. However, if you were to bolster this through using the ISACA privacy principles, you will be able to considerably reduce your data privacy and security risks. If all personal data is processed through PCI DSS compliant (or an equivalent standard) business operations, the remaining data privacy obligations are limited to maintaining the “Rights” of the Data Subject.

The identified **71%** will be further divided and explored in the following sections (Cyber Security, Information Security, Physical Security and Resilience) of this chapter.
