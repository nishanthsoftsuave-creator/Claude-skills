---
title: "Information Security"
book: pci-dss-integrated-data-security-standard-guide
chapter: 4
source_pages: "122-128"
format: source-text
---
# Information Security
(Source: PDF pp. 122-128)

<!-- PDF p. 122 (book p. 98) -->

Having secured your Cyber Security environment, you still need to ensure that the internal networks are safeguarded from harm. The attackers could be from unauthorized aggressors, who have managed to circumvent your perimeter defenses, or from an authorized employee or trusted contractor. Consequently, it is essential that the internal technologies that support the card payment process are securely maintained.

TechTarget[^61] defines Information Security as:

Information security (infosec) is a set of strategies for managing the processes, tools and policies necessary to prevent, detect, document and counter threats to digital and non-digital information. Infosec responsibilities include establishing a set of business processes that will protect information assets regardless of how the information is formatted or whether it is in transit, is being processed or is at rest in storage.

The purpose of your InfoSec program is to complement the Cyber Security environments, so as to slow the potential infiltration into the data stores/transmissions and exfiltration from your corporate network. Once an external attacker has breached <!-- PDF p. 123 (book p. 99) --> the perimeter defenses, they will seek to gain a clandestine persistent presence within your corporate network, while they figure out the best opportunities to steal your data.

[^61]: https://searchsecurity.techtarget.com/definition/information-security-infosec

At the same time, you need to effectively manage the “Insider Threat,” whether that be from deliberate, malicious, or accidental activities of an authorized individual, contractor, or third party. Consequently, I have collated together a list of some of the complementary controls that relate to the Information Security environment.

- **Requirements 1.1 to 1.5 – Internal facing Network Topologies**
  - Can you identify the demarcation points between the trusted and untrusted environments?
  - Do you have a clearly defined “Buffer Zone” between trusted and untrusted environments?
    - During my deployment to Basrah, Iraq, my role was to use my 42-toothed furry Exocet (military patrol dog) to patrol and defend the “Buffer Zone” between the Badlands *(untrusted environment)* and the internal secure military operational areas. In essence, this involved covert patrolling of the perimeter track which ran parallel to the perimeter fence, so as to provide a proactive defense and first response to any potential incursion attempts *(Firewall/IDS alerting)*.
    - During other deployments into hostile environments, the delineation would be a considerable De-Militarized Zone (DMZ) to act as the “Buffer Zone.” At Camp Bastion, this had consisted of approximately 1.5 km of rough road between the outer perimeter checkpoint and the inner checkpoint. I recall, on one occasion, the effectiveness of the DMZ during the response to an incident. At the internal checkpoint, the Ammunition and Explosives Detection (AED) detection dog had shown an interest on an incoming Non-Potable water tanker. The dog had indicated to the region around an open tool box (located beneath the water tank). Further

<!-- PDF p. 124 (book p. 100) -->

investigation revealed that the water tanker had been repurposed from its former function as a fuel tanker and that the tool box had been closed when the driver had parked up on the previous evening. The uneven drive along the 1.5 km DMZ had shaken free an Improvised Explosive Device (IED) from the former fuel tanker.

- Do you filter your network traffic to ensure that only approved network traffic flows between the trusted and untrusted network environments?
- Internal Firewall/Router configurations.
- Internal Rulesets.
- Detailed Network Diagrams.
- Data Flow Diagrams.
  - During multiple appointments in the RAF Police, the primary defense involved creating secure environments within the confines of the military base (e.g., Hardened aircraft shelters (HAZ), Secure bunkers, Weapons storage facilities, etc.) which had specific access control lists to ensure that only approved vehicles and personnel were granted access.
- **Requirement 2 – Securely configured internal facing IT Assets**
  - Securely configured wireless technologies
  - Securely configured internal IT assets, supporting the data life cycles
  - Asset Inventory (including End-of-Life dates)

<!-- PDF p. 125 (book p. 101) -->

- **Requirement 3 – Secure Data Storage**
  - Data Discovery. You can’t protect what you don’t know.
    - *GroundLabs Card Recon*[^62]
    - Spirion[^63]
    - Memoryze[^64]
  - Encryption Key Management
    - Wireshark[^65]
- **Requirement 5 – Internal IT assets protected by active Anti- Malware software**
- **Requirements 6.1 to 6.5 – Manage Secure Internal Applications**
  - Manage vulnerabilities and updates based upon the identified vulnerabilities, risk assessed against local factors.
  - Secure Software Development on all internal applications that support your payment card processes.
  - All changes to internal systems are formally managed to ensure that impact and rollback decisions are applied.
- **Requirements 7 and 8 – Role-Based Access Control**
  - All access to internal systems is strictly restricted, based upon explicit need to know.
    - John the Ripper[^66]
    - Ophcrack[^67]

[^62]: www.groundlabs.com/card-recon/
[^63]: www.spirion.com/sensitive-data-discovery/
[^64]: www.fireeye.com/services/freeware/memoryze.html
[^65]: www.wireshark.org/
[^66]: https://sectools.org/tool/john/
[^67]: https://sectools.org/tool/ophcrack/

<!-- PDF p. 126 (book p. 102) -->

- Brutus[^68]
- SolarWinds Permissions Analyzer[^69]
- ManageEngine ADManager[^70]
- MaxPowerSoft AD Reports Lite[^71]
- All users that are granted access should be categorized based upon their potential ability to do damage. These categorized and prioritized users should then be monitored as part of requirement 10.
- **Requirements 10 – Monitoring users and systems use**
  - Based upon the categorized IT systems and users, the monitoring should be able to detect the **ABNORMAL** from NORMAL activities.
  - Centralized monitoring of the various logs source should be collated to show unauthorized activities, as an attacker carries out reconnaissance of your internal network.
  - All critical internal systems have correct and consistent clock readings, received from secure and industry-accepted external resources.
  - *Note:*
  - *This is essential in the event of an investigation or forensic examination to piece together an accurate chain of events.*
    - Elastic Stack

[^68]: https://sectools.org/tool/brutus/
[^69]: www.solarwinds.com/free-tools/permissions-analyzer-for-active-directory/registration?program=1323&campaign=70150000000OzCs&CMP= BIZ-TAD-ITT-SW_WW_X_PP_PPD_CQ_EN_HLTH_SW-PAFT-X_X_X_X-Q316
[^70]: www.manageengine.com/products/ad-manager/download. html?utm_source=ITT&utm_medium=ppc&utm_campaign=ADMP_download
[^71]: www.maxpowersoft.com/adreportslite.php

<!-- PDF p. 127 (book p. 103) -->

- Secure audit trails
  - *This is essential in the event of an incident to help trace the activities back to the potential “Root Cause.”*
  - *Consider enhanced archiving, exceeding the 12 months between PCI DSS compliance assessments, as attackers are known for remaining dormant for a number of months or years, for example:*
    - *Three months instant, 36 months archive (as opposed to the minimum 12 months)*
- **Requirement 11.1 – Rogue Wireless Devices**
  - Conduct periodic checks for rogue wireless checks, which can be used to circumvent your network egress controls.
    - *Physical inspections of the internal IT assets*
    - Kismet[^72]
    - NetStumbler[^73]
    - inSSIDer[^74]
- **Requirement 11.2 – External Vulnerability Scans**
  - Scanning of internal systems for vulnerabilities
    - Security Content Automation Protocol (SCAP) tools[^75]
    - Nessus[^76]
    - OpenVAS[^77]

[^72]: https://sectools.org/tool/kismet/
[^73]: https://sectools.org/tool/netstumbler/
[^74]: https://sectools.org/tool/inssider/
[^75]: https://csrc.nist.gov/Projects/scap-validation-program/Validated-Products-and-Modules
[^76]: https://sectools.org/tool/nessus/
[^77]: https://sectools.org/tool/openvas/

<!-- PDF p. 128 (book p. 104) -->

- **Requirement 11.3 – Internal Penetration Tests and Segmentation Tests**
  - Confirming the integrity and effectiveness of the external network layers and network segmentation
    - *CREST PTMA*[^78]
- **Requirement 11.4 – Intrusion Detection/Prevention**
  - Alerting on all internal systems
    - SNORT[^79]
    - Suricata[^80]
    - BRO IDS[^81]
- **Requirement 11.5 – Change Detection**
  - Alerting to notify any potential unauthorized changes made to internal systems
    - *OpenDLP*[^82]
- **Requirement 12 – People Management**
  - Maintaining a security culture for all personnel responsible for the management of (or with access to) the internal systems and payment card data

[^78]: www.crest-approved.org/2018/07/20/penetration-testing-maturity-assessment-tools/index.html
[^79]: www.snort.org/
[^80]: https://suricata-ids.org/
[^81]: https://sourceforge.net/projects/bro-tools/
[^82]: https://code.google.com/archive/p/opendlp/
