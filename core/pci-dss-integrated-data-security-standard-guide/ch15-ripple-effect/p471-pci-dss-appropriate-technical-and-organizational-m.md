---
title: "PCI DSS: Appropriate Technical and Organizational Measures"
book: pci-dss-integrated-data-security-standard-guide
chapter: 15
source_pages: "471-483"
format: source-text
---
# PCI DSS: Appropriate Technical and Organizational Measures
(Source: PDF pp. 471-483)

<!-- PDF p. 471 (book p. 451) -->

Okay, so we should now know that compliance with PCI DSS is extremely prescriptive, whereas compliance with your personal data laws and regulations is far less prescriptive and the responsibility is down to your organization to apply defensive measures that are commensurate with the risk.

However, how do you ensure that these are suitable and commensurate to the risk? Are there further lessons that can be taken from your PCI DSS compliance program? Well, payment card data is both financial data and personal data that is a high-value data asset for criminals and needs to be safeguarded as you might protect high volumes of cash, for instance, layering your physical security measures, keeping the cash under lock and key (when stored or in transit), minimizing retention periods, restricting access, and ensuring that supporting systems are well maintained to minimize the risk of failure/compromise.

We know that today’s criminals are scavengers, seeking to exploit opportunities to harvest together pieces of the “Identity jigsaw” puzzles in order to monetarize personal data (Identity Theft). Consequently, all pieces of the “Identity Jigsaw” have an intrinsic value, and the greater the number of pieces they are able to harvest, the greater their aggregated value.

<!-- PDF p. 472 (book p. 452) -->

*[Figure omitted]*

In a recent report by the University of Texas (2019 International Identity Theft Assessment and Prediction Report[^13]), digital vulnerabilities were perceived to represent almost **75%** of the cases of Identity theft.

**Figure 15-3.** *Piecing Together the “Identity Jigsaw”*

*[Figure omitted]*

**Figure 15-4.** *Digital vs. Non-digital*

In addition, according to UK Finance,[^14] unauthorized financial fraud losses across payment cards, remote banking, and checks totaled **£844.8 million** in 2018, an **increase of 16%** *(compared with 2017)* – both of which need a combination of personal data and <!-- PDF p. 473 (book p. 453) --> payment card data to enable the criminals to monetarize their activities and make it a profitable business.

[^13]: https://identity.utexas.edu/assets/uploads/publications/CID_ITAP_Report_2019.pdf
[^14]: www.ukfinance.org.uk/system/files/Fraud%20The%20Facts%202019%20-%20FINAL%20 ONLINE.pdf

Each year the Federal Trade Commission’s (FTC’s) Consumer Sentinel Network Data Books[^15] continue to confirm that identify theft remains a consistent and ever-present threat to today’s businesses and consumers:

- 2018 – **3 Million** reported incidents

Top Three Categories

1. Imposter scams

2. Debt collection

3. Identity theft

*[Figure omitted]*

**Figure 15-5.** *Types of ID Theft*

At the heart of all these cases is the misuse of personal data, so with this being the case, do businesses need to do more for the protection of their consumers and employees?

If so, can we apply lessons learned from the PCI DSS requirements?

[^15]: www.ftc.gov/reports/consumer-sentinel-network-data-book-2018

<!-- PDF p. 474 (book p. 454) -->

## Requirement 1: Install and Maintain a Firewall Configuration to Protect Sensitive Data

Increasingly we are seeing reported instances of cyber criminals gaining a persistent presence within corporate network environments. Often, once the criminals have managed to compromise a poorly managed perimeter asset or third-party-connected asset, they will then seek to identify opportunities to move laterally across the compromised networks.

During this period of Command and Conquer, the criminals are known to carrying out reconnaissance of the internal systems and connections. Having identified all the systems, the criminals then seek to map their potential attack pathways to intercept data in transit or at rest. They are seeking to identify points of potential ingress and egress, where they are more likely to identify the weaker areas of a network and the location of the corporation’s “Crown Jewels.” It is worrying that the criminals will not be deterred by encrypted data and, in the impact of not being able to profit from their actions, are reported to resort to impacting the business operations through the disabling of business critical systems[^16] – essentially the criminals are making a statement:

*If we can’t make use of your data/IT systems, neither can you!*

Considerable components of requirement 1 are similar to the content of the United Kingdom’s National Cyber Security Centre’s (NCSC’s) Network Security section of their recommended ten steps to Cyber Security[^17]:

- **Manage the network perimeter.**

*“Manage access to ports, protocols and applications by filtering and inspecting all traffic at the network perimeter to ensure that only traffic which is required to support the business is being exchanged. Control and manage all inbound and outbound network connections.”*

[^16]: www.europol.europa.eu/newsroom/news/cybercrime-becoming-bolder-data-centre-of-crime-scene
[^17]: www.ncsc.gov.uk/collection/10-steps-to-cyber-security?curPage=/collection/10-steps-to-cyber-security/the-10-steps/network-security

<!-- PDF p. 475 (book p. 455) -->

- **Protect the internal network.**

*“Ensure that there is no direct routing between internal and external networks (especially the Internet), which limits the exposure of internal systems to network attack from the Internet.”*

- **Segregate networks as sets.**

*“Identify, group and isolate critical business systems and apply appropriate network security controls to them.”*

- **Secure wireless access.**

*“All wireless access points should be appropriately secured, only allowing known devices to connect to corporate Wi-Fi services. Security scanning tools may be useful to detect and locate unauthorized or spoof wireless access points.”*

Clearly the criminals see a value in identifying and documenting your corporate network, so it is essential that your business does the same.

Do you maintain periodic scans of your perimeter and internal systems and connecting systems so that you understand?

- Data flows
- Critical business systems
- Personal data processing systems
- Personal data storage systems
- Interconnecting systems
- Internal gateways
- Delineations between trusted and untrusted environments
- Any potential exploitation opportunities

<!-- PDF p. 476 (book p. 456) -->

## Requirement 2: Do Not Use Vendor-supplied Defaults for System Passwords and Other Security Parameters

Step 2 of the NCSC’s ten steps to Cyber Security[^18] shows a strong affiliation to PCI DSS requirement 2 and clearly demonstrates the integrated nature of the PCI DSS controls framework:

- **Create and maintain hardware and software inventories.**

*“Create inventories of all authorized hardware and software used across the organization. Ideally the inventory should capture the physical location, business owner and purpose of hardware together with the version and patch status of all software. Tools can be used to help identify unauthorized hardware or software.”*

- **Manage your operating systems and software.**

*“Implement a secure baseline build for all systems and components, including hardware and software. Any functionality or application that does not support a user or business need should be removed or disabled. The secure build profile should be managed by a configuration control process and any deviation from the standard build should be documented and approved.”*

Requirements 1 and 2 combine to make the unauthorized infiltration and extraction increasingly more difficult for opportunist attackers. The network architecture should be visualized in network and data flow diagrams, with the identified systems being correlated against the asset inventory and with all changes being subjected to documented approval. Anything not confirming to these records would require immediate investigation, and any systems approaching their end-of-life (EOL) or end-of-support (EOS) were subject to risk assessment practices.

[^18]: www.ncsc.gov.uk/collection/10-steps-to-cyber-security/the-10-steps/secure-configuration

<!-- PDF p. 477 (book p. 457) -->

## Requirement 3: Protect Stored Sensitive Data

If you need to store sensitive data, ensure that unnecessary retention is avoided and that all aggregated/high-value sensitive data is kept in a vault under, strictly controlled, lock and key, so that if your corporate network is compromised, the sensitive data remains protected.

Periodic checks should be carried out to ensure that unnecessary or ad hoc data storage (outside your vaults) is avoided and to ensure that all personal data stores are identified to ensure that the retention remains within your business’s risk tolerances. How well do you understand?

- The nature, scope, context, and purposes of the processing
- The necessity, proportionality, and compliance measures
- The risks to individuals
- Any additional measures to mitigate those risks

It is important to ensure that you have identified all potential areas where payment card data may have been deliberately, or accidentally, retained. This can be achieved through the use of automated sensitive data discovery scanning solutions, such as

- Memoryze[^19]
- Groundlabs[^20]
- DataSecurity Plus[^21]
- Spirion[^22]

[^19]: www.fireeye.com/services/freeware/memoryze.html
[^20]: www.groundlabs.com/
[^21]: www.manageengine.com/data-security/index.html?topMenu
[^22]: www.spirion.com/sensitive-data-discovery/

<!-- PDF p. 478 (book p. 458) -->

## Requirement 4: Encrypt Transmission of Sensitive Data Across Open, Public Networks

In order to make use of sensitive data, your business will need to ensure that this data remains under lock and key while in transit. Modern criminals have become increasingly proficient at intercepting sensitive data while in transit. Consequently, in the event that these transmissions are intercepted, the sensitive data should remain under lock and key to ensure that it cannot be used by criminals. Public-facing technologies (e.g., Web, virtual private networks (VPNs), email, etc.) are easy targets for opportunist criminals.

Therefore, you should periodically identify the public-facing points of egress/ingress, where sensitive data assets will be moved from one corporate environment to another.

This can be easily achieved and included into your data privacy and security program using tools such as

- ExtraHop[^23]
- Glassware[^24]
- Wireshark[^25]
- Qualys SSL Labs[^26]
- SSL Checker[^27]
- GeekFlare[^28]
- Wormly[^29]
- DigiCert[^30]

[^23]: www.extrahop.com/products/security/
[^24]: www.glasswire.com/
[^25]: www.wireshark.org/
[^26]: www.ssllabs.com/ssltest/
[^27]: www.thesslstore.com/ssltools/ssl-checker.php
[^28]: https://gf.dev/tls-test
[^29]: www.wormly.com/test_ssl
[^30]: www.digicert.com/help/

<!-- PDF p. 479 (book p. 459) -->

## Requirement 5: Protect All Systems Against Malware and Regularly Update Anti-virus Software or Programs

This is another of the UK NCSC’s top 10 steps for cyber security:

- **Malware Prevention**

*“Malicious software, or malware is an umbrella term to cover any code or content that could have a malicious, undesirable impact on systems. Any exchange of information carries with it a degree of risk that malware might be exchanged, which could seriously impact your systems and services. The risk may be reduced by implementing appropriate security controls as part of an overall ‘defense in depth’ approach.”*

- Malware threats remained an ever-present threat[^31] during 2019.[^32]
- Botnets, Ransomware, and Cryptomining/Jacking were reported as the top 3 malware threats of 2019.[^33]

[^31]: www.cybok.org/media/downloads/Malware__Attack_Technology_issue_1.0.pdf
[^32]: https://threatpost.com/biggest-malware-threats-of-2019/151423/
[^33]: www.eweek.com/security/webroots-listing-of-the-nastiest-malware-of-2019

## Requirement 6: Develop and Maintain Secure Systems and Applications

A common avenue of attack is through poorly managed IT systems and software applications. Consequently, it is essential that any sensitive data processing systems are not exposed to being exploited. Frequently, out-of-date software and hardware provide criminals the opportunity to infiltrate your corporate environment, either via a public-facing system or web-coding error that allows the criminal unauthorized access to the supporting system layers.

It is important to ensure that any newly identified vulnerabilities are risk assessed and prioritized for timely remediation, based upon their criticality, and that the web developers use SecDevOps[^34] best practices to ensure that they do not inadvertently <!-- PDF p. 480 (book p. 460) --> introduce any new exploitable vulnerabilities to the external facing, high-risk interfaces. Remember, the web-based customer interfaces have significantly changed, and they are now increasingly used as customer interfaces and not just information “read-only” interfaces.

[^34]: www.pcisecuritystandards.org/documents/PCI-Secure-Software-Standard-v1_0.pdf?agre ement=true&time=1547813202710

Of course, as with anything related to systems or software integrity, any changes need to be strictly controlled, risk assessed, and monitored.

## Requirement 7: Restrict Access to Sensitive Data by Business Need to Know

The Need to Know/Need to Access principles should be based upon least privilege, so as to minimize the potential impact and risk. As a consequence, this is another of the UK NCSC’s top 10 steps to cyber security:[^35]

- **Limit user privileges.**

*“Users should be provided with the reasonable minimum rights and permissions to systems, services and information that they need to fulfill their business role.”*

[^35]: www.ncsc.gov.uk/collection/10-steps-to-cyber-security/the-10-steps/managing-user-privileges

## Requirement 8: Identify and Authenticate Access to System Components

Why wouldn’t you limit and control access management to your estate? Very few would have unrestricted access to the keys to your house or motor vehicle, so why would we do this with access to our corporate network and sensitive data processing systems? All personnel should be strictly limited and educated as to the importance of creating and managing robust access credentials.

This is an increasingly difficult element to maintain, given the volume of passwords (both business and personal) are expected to commit to memory, ensuring that they are not duplicating credentials or sharing credentials. Additional measures can be applied through the use of multi-factor authentication (MFA) for higher-risk accounts/access (e.g., Privileged users, Remote users, etc.).

<!-- PDF p. 481 (book p. 461) -->

Remember, if it is more convenient for the authorized user, it can become even more convenient for the attacker wishing to gain unauthorized access to your corporate network, information systems, and sensitive data.

To assist your employees, you may wish to consider the benefits of the following resources:

- Password Management Systems (e.g., 1password,[^36] Dashlane,[^37] Lastpass,[^38] etc.)
- Have I Been Pwned[^39]?
  - Pwned Passwords[^40]
- Password strength checker[^41]

[^36]: https://1password.com/
[^37]: www.dashlane.com/
[^38]: www.lastpass.com/
[^39]: https://haveibeenpwned.com/
[^40]: https://haveibeenpwned.com/Passwords
[^41]: https://howsecureismypassword.net/

## Requirement 9: Restrict Physical Access to Sensitive Data

If your attackers are unable to gain a foothold within your virtual environment, they will look for opportunities to gain unauthorized access to your physical environment where the supporting networks, information systems, or removable media may reside. Probably one of the easiest type of attacks, the perpetrator only needs a limited toolset and a combination of guile and imagination to gain unauthorized access to your physical assets.

It is important to note that testing for the non-digital-style attack (social engineering) is not a requirement in the current version of the PCI DSS integrated controls framework. However, this is a well-known tactics for cyber criminals and organized criminal gangs:

- KVM Switch Attack[^42]
- Keylogger Attack[^43]

[^42]: www.theregister.co.uk/2014/04/25/kvm_crooks_jailed/
[^43]: https://securelist.com/keyloggers-how-they-work-and-how-to-detect-them-part-1/36138/

<!-- PDF p. 482 (book p. 462) -->

## Requirement 10: Track and Monitor All Access to Network Resources and Sensitive Data

This is another of the UK NCSC’s recommended top 10 steps to Cyber Security:[^44]

- **Monitoring**

*“System monitoring provides a capability that aims to detect actual or attempted attacks on systems and business services. Good monitoring is essential in order to effectively respond to attacks. In addition, monitoring allows you to ensure that systems are being used appropriately in accordance with organizational policies. Monitoring is often a key capability needed to comply with legal or regulatory requirements.”*

Criminals having a median dwell time of **78 days**[^45] demonstrates that businesses are recognizing the importance of being able to identify and respond to ABNORMAL activities *(reduced from* **416 days** *in 2011).*

[^44]: www.ncsc.gov.uk/collection/10-steps-to-cyber-security/the-10-steps/monitoring
[^45]: https://content.fireeye.com/m-trends

## Requirement 11: Regularly Test Security Systems and Processes

Independent security testing enables you to be reassured that everything continues to operate securely while enabling you to rapidly identify and remediate any vulnerabilities before an attacker has the opportunity to exploit and profit from any poorly maintained network, systems, and practices. Periodic testing should be regarded as an integral and supportive component of your data privacy and security program, ensuring that any identified deviations or issues are investigated to ensure that these are not originated from poor practices.

It is essential that any testing is carried out by independent and suitable skilled personnel to ensure that appropriate testing is established. All periodic testing of critical systems and sensitive data processing systems should be documented, along with the tracking of any remediation activities, ensuring that any lessons learned opportunities can be applied.

<!-- PDF p. 483 (book p. 463) -->

## Requirement 12: Maintain a Policy that Addresses Information Security for All Personnel

You cannot expect your personnel to know what is expected of them and to understand what “good” looks like unless you provide them with the corporate rules and procedures for the specific roles and responsibilities. This is essential for ensuring that they can adhere to these rules and to operate in a safe and secure manner.

However, setting the rules that articulate the “Tone at the top” is only a small part of the job and your personnel should be periodically tested as to the intent and content of your rules and procedures.

Think of it as being licensed to drive a motor vehicle. The extent of the rules and procedures are commensurate with the potential damage/impact that is presented by the vehicle type. Personnel should be policed and periodically re-educated to refresh their understanding of these documented rules and procedures. Failure to adhere to the rules should result in disciplinary or re-education or, in some cases, the removal of their “licenses to drive.”
