---
title: "Requirement 3: The Vault"
book: pci-dss-integrated-data-security-standard-guide
chapter: 9
source_pages: "293-295"
format: source-text
---
# Requirement 3: The Vault
(Source: PDF pp. 293-295)

<!-- PDF p. 293 (book p. 271) -->

In the event that you need to store CHD (or with a legitimate need) Sensitive Authentication Data (SAD), this requirement is designed to minimize the impact of an attacker managing to compromise your network and system components to gain unauthorized access to your data stores.

In order to effectively reduce the risk, it is essential that data retention is kept to an absolute minimum and the retained data is saved in a manner that the attacker is unable to profit from these data stores, for example, Encryption, Tokenization (with effective supporting practices), and so on.

Remember, gaining unauthorized access to the vault and being able to unlock the safety deposit boxes is the criminals’ Return On Investment (ROI), enabling them

**Figure 9-25.** *Secure by Default/Design*[^29]

[^29]: www.army-technology.com/contractors/infrastructure/hesco/

<!-- PDF p. 294 (book p. 272) -->

to exploit these details for their gain. In 2019, the Ponemon Institute[^30] estimated the average cost of a data breach to be at **$150 per record** (Globally) or **$242 per record** (United States).

*[Figure omitted]*

**Figure 9-26.** *Data Breach Calculator*

Therefore, the retention of surplus data or unnecessary data may prove to be a risk that when assessed could exceed your tolerances and which could be better risk managed:

- **T**reat: Encryption and Key Management – Limited Storage
- **T**erminate: No CHD usage – No storage
- **T**ransfer: PCI DSS Compliant Third-Party Services (e.g., Tokenization, Payment Service Providers (PSP), Dual-Tone Multi-Frequency (DTMF), etc.) – No storage
- **T**olerate: After effective application of PCI DSS, requirement 3 controls – Limited storage

[^30]: www.ibm.com/security/data-breach

<!-- PDF p. 295 (book p. 273) -->

Much like your CDE storage environments, within a deployed operation base, there was a need to have further enhanced secure enclaves, where the most valued assets are securely housed. Figure 9-27 shows an example of a secure enclave, within a deployed operation, with heightened and more robust security controls and with everything held under lock and key.

*[Figure omitted]*
