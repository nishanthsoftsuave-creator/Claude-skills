---
title: "Secure Data at Rest and in Transit (Protect Cardholder Data)"
book: pci-dss-integrated-data-security-standard-guide
chapter: 9
source_pages: "274-276"
format: source-text
---
# Secure Data at Rest and in Transit (Protect Cardholder Data)
(Source: PDF pp. 274-276)

<!-- PDF p. 274 (book p. 252) -->

THINK: SECURING THE VAULT THINK: CASH IN TRANSIT

*[Figure omitted]*

*[Figure omitted]*

The first consideration here is to decide whether there is a need for the persistent storage of CHD or are there other measures that can be applied to further reduce the risks and burden associated with having to maintain a vault, for example:

- Transferring the risk through the use of PCI DSS-compliant Payment Service Providers
  - *Securely redirecting, or using an embedded iFrame, to ensure that all customers’ payment card details go through a PCI DSS- compliant third-party Service Provider’s interface (no business systems or personnel interaction with payment card data – fully outsourced).*
- Terminating the risk through the use of Dual-Tone Multi-Frequency (DTMF) technologies
  - *Your consumers enter their CHD via their own phone keypad, rather than needing to be passed verbally to a call agent and then manually entered into the application via the business IT system interface (no business systems or personnel interaction with payment card data – fully outsourced).*

<!-- PDF p. 275 (book p. 253) -->

- Treating the risk through encryption or tokenization. In the event that the vault gets compromised, the keys needed to unlock and the system needed to untokenized the CHD are completely independent and protected.
  - All customers’ payment card data operations are carried out in house and the payment card data is securely stored (in a vault), protected by encryption (kept under lock and key). The use of encryption makes the stored payment card data useless in the event of a compromise. However, this is heavily reliant of good key management practices.
  - *Customers’ payment card information is exchanged for tokenized data (carried out by a third party) to ensure that only tokenized payment card data is processed by the business systems, supporting the payment card operations.*

Within your trusted network, it is currently permitted for an organization to move the CHD unencrypted *(This may well change with the release of v.4.0)*. However, at any point that an organization needs to move it across a public-facing environment, this needs to be kept under lock and key.

## Reality Bites

Having issued out the security containers for use, each one had their locks re-configured to unique settings that were only known to authorized personnel. However, in my role as the station CI operative, I had the responsibility to securely manage the rotation of their supporting keys and combination changes and to securely store the duplicates.

I did not have a need to access these duplicates, so they were securely sealed and securely stored in a separate security container, away from the in-use security containers.

Periodically, I would manage the mustering and changing of the keys and combinations and respond to potential compromises. Additionally, in the event of a compromised key, forgotten combination, or in the event of the need for emergencies, I would be responsible for ensuring that safe and secure changes were made.

<!-- PDF p. 276 (book p. 254) -->

All these combination and key management procedures were essential for the maintenance of the integrity of the security containers and to ensure that the enclosed highly sensitive data assets retained their confidentiality, integrity, and availability (CIA).

This principle is similar to that needed to meet the compliance requirements for safeguarded stored payment card data through the application of encryption.
