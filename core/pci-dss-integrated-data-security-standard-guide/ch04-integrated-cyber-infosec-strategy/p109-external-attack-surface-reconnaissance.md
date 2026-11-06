---
title: "External Attack Surface Reconnaissance"
book: pci-dss-integrated-data-security-standard-guide
chapter: 4
source_pages: "109-122"
format: source-text
---
# External Attack Surface Reconnaissance
(Source: PDF pp. 109-122)

<!-- PDF p. 109 (book p. 85) -->

Hackers will look to surveil your external facing attack surfaces, looking to identify any possible opportunities to infiltrate the web application and Internet-facing technologies. Consequently, it is essential that you do the same and start to trace your consumer journeys to identify the external facing technologies that support the Points of Interaction through to the entry into your corporate network. It is important to note that the traditional hack through the network infrastructure are not the only Tactics, Techniques, and Protocols employed by hackers today, for example:

- **Avast**[^12]

Compromised employee’s VPN credentials (no additional multi-factor authentication (MFA)), gaining access to their account.

- **Equifax**[^13]

The credit agency failed to update an external facing web server, which provided the attackers with unauthorized access, enabling them to move laterally across the corporate network.

- **Multiple Examples**
  - **2019 Application Security Risk Report**[^14]
    1. There has been a reduction in the number of reported new High-severity vulnerabilities.
    2. Open source: A clear and present danger.
    3. Nearly all web apps have bugs in their security features.
    4. Mobile apps have shown a sharp increase in some vulnerability types.
    5. The adoption of DevOps approaches is increasing.
    6. Bug bounty programs have delivered a limited impact.

[^12]: www.zdnet.com/article/avast-says-hackers-breached-internal-network-through-compromised-vpn-profile/
[^13]: www.warren.senate.gov/imo/media/doc/2018.09.06%20GAO%20Equifax%20report.pdf
[^14]: https://content.microfocus.com/application-security-risk-tb/app-security-risk-takeaways?lx=qatC0j?utm_source=techbeacon&utm_medium=techbeacon&utm_campaign=00134846

<!-- PDF p. 110 (book p. 86) -->

## Information Gathering

How well do you understand your business’s digital footprint and what type of data is available to the opportunist attacker?

*[Figure omitted]*

**Figure 4-5.** *DNS Dumpster*[^15]

[^15]: https://dnsdumpster.com/

<!-- PDF p. 111 (book p. 87) -->

*[Figure omitted]*

**Figure 4-6.** *Zoom Eye*[^16]

*[Figure omitted]*

**Figure 4-7.** *VirusTotal*[^17]

[^16]: www.zoomeye.org/
[^17]: www.virustotal.com/graph/

<!-- PDF p. 112 (book p. 88) -->

*[Figure omitted]*

**Figure 4-8.** *Visual Site Mapper*[^18]

*[Figure omitted]*

**Figure 4-9.** *ExtraHop*[^19]

*[Figure omitted]*

**Figure 4-10.** *Qualys*[^20]

[^18]: http://visualsitemapper.com/
[^19]: www.extrahop.com/
[^20]: https://qualysguard.qualys.com/qwebhelp/fo_portal/maps/mapping_basics.htm

<!-- PDF p. 113 (book p. 89) -->

*[Figure omitted]*

*[Figure omitted]*

In order to effectively safeguard the interaction points, it is essential that the perimeter assets be differentiated from the internal technologies.

Within the PCI DSS controls framework, this is covered in the requirement to document your network assets and data flows, and you have a layered network.

**Figure 4-11.** *Open-AudIT* [^21]

**Figure 4-12.** *NMAP*[^22]

[^21]: www.open-audit.org/
[^22]: https://nmap.org/

<!-- PDF p. 114 (book p. 90) -->

Consequently, to ensure that you understand the potential impact of your assets and you are able to prioritize your compliance activities, I recommend that you categorize your technologies, for example:

1. **Perimeter technologies** a. Web Servers b. Web Applications c. Perimeter Firewall d. Perimeter Intrusion Detection System (PIDS) e. External facing Server f. PIN Transaction Security (PTS) Devices

2. **Payment Card Data processing technologies** a. Databases b. Payment Applications c. Internal Firewalls d. Laptops e. Mainframes f. Intrusion Detection Systems (IDS) g. Internal Servers

3. **Supporting internal technologies**

Such an approach will greatly assist you in your ongoing Business-As-Usual (BAU) compliance efforts while aiding the vulnerability and risk management, more importantly helping to piece together the technology chains, so that any monitoring will improve the ability to readily detect malicious activities moving along the various customer journeys – toward the “Crown Jewels.”

Additionally, early detection will help you respond in a timely manner so that you have improved chances of intercepting and blocking the activities of an attacker.

<!-- PDF p. 115 (book p. 91) -->

Remember, you are looking to be able to detect and block malicious “Inbound” and “Outbound” network traffic and unauthorized actions.

Attackers will look to gain a persistent presence within your network and will not always, necessarily, attempt to brute force their way through the “Main Gate.”

Thinking like an attacker, carrying out periodic reconnaissance results should be compared against categorized external assets.

## PCI DSS Applicable Controls – External Technologies

It is essential that you understand what is needed to maintain a secure perimeter, so as to reduce the opportunities for your attackers to exploit. Consequently, I have collated together a suite of example external technology-related PCI DSS controls, as well as some suggested supporting resources.

These will provide you with some resources that could help you create a schedule of auditing, will enhance your defensive efforts, and help identify and defend against any potential infiltration opportunities.

- **Requirements 1.1 to 1.5 – External facing Network Topologies**
  - “Detailed” Network Diagrams
    - *Visual Paradigm*[^23]
    - Open-AudIT[^24]
    - NMAP[^25]

[^23]: https://online.visual-paradigm.com/diagrams/solutions/free-network-diagram-software/
[^24]: www.open-audit.org/
[^25]: https://nmap.org/

<!-- PDF p. 116 (book p. 92) -->

- Summary Network Diagrams
  - Showing the interconnections between numerous environments
    - “In-Scope” Payment Channels
    - “Out-of-Scope” BAU network components
  - It is extremely important that you are able to clearly identify the “Air Gaps” between the “In-Scope” and “Out-of-Scope” network topologies.
- Data Flow Diagrams
  - Gliffy[^26]
  - DrawIO[^27]
- Firewall Rulesets
  - *Titania Nipper Studio*[^28]
- Network Traffic Analysis
  - *Dsniff* [^29]
  - *NetWitness NextGen*[^30]
  - *Argus*[^31]
  - *P0f* [^32]
- Wireless Analysis
  - Aircrack[^33]

[^26]: www.gliffy.com/
[^27]: www.draw.io/
[^28]: www.titania.com/products/nipper/
[^29]: https://sectools.org/tool/dsniff/
[^30]: https://sectools.org/tool/netwitness/
[^31]: https://sectools.org/tool/argus/
[^32]: https://sectools.org/tool/p0f/
[^33]: https://sectools.org/tool/aircrack/

<!-- PDF p. 117 (book p. 93) -->

- Approved Services, Ports, and Protocols
  - *Command Prompt*
- Software Firewalls enabled on portable devices
  - *ZoneAlarm*[^34]
- **Requirement 2 – Securely configured external facing IT Assets**
  - Categorized Asset Inventory
    - “In-Scope” assets (supporting customer journeys)
    - “Out-of-Scope” (adjoining assets with the potential to impact)
  - Securely configured wireless technologies
  - Secure Configuration Standards
    - *CIS Benchmarks*[^35]
    - *Titania PAWS*[^36]
- **Requirement 4.1 – Encryption over public-facing networks**
  - Secure transmission
    - Wireshark[^37]
    - SSL Labs[^38]
- **Requirement 5.1 – External technologies protected by effective Anti-Malware software**
  - Checks to confirm that the AV software is active and effective
    - *Wicar Test Virus*[^39]

[^34]: www.zonealarm.com/software/free-firewall/?AID=11556579&PID=6361382&SID= trd-5293610212650605605&network=cj
[^35]: www.cisecurity.org/cis-benchmarks/
[^36]: www.titania.com/products/paws/
[^37]: https://sectools.org/tool/wireshark/
[^38]: www.ssllabs.com/ssltest/
[^39]: www.wicar.org/test-malware.html

<!-- PDF p. 118 (book p. 94) -->

- **Requirements 6.1 to 6.6 – Manage Secure web sites and Applications**
  - Vulnerability Risk Management
    - Tenable.io[^40]
    - Cequence.ai[^41]
  - Inventory
    - “In-Scope” web sites (supporting payments)
    - “Out-of-Scope” web sites (potential to impact, e.g., Man-In-The- Middle (MITM), where the customer journey can be redirected)
  - All changes to external systems formally managed to ensure that impact and rollback decisions are applied
  - Secure Software Development Operations
    - *Open Web Application Security Project (OWASP)*[^42]
    - *OWASP Top 10*[^43]
    - *OWASP Appendix A Testing Tools*[^44]
    - *Application Security Platform*
      - *Cequence Security*[^45]

[^40]: www.tenable.com/products/tenable-io/web-application-scanning
[^41]: www.cequence.ai/
[^42]: www.owasp.org/index.php/Main_Page
[^43]: www.owasp.org/images/7/72/OWASP_Top_10-2017_%28en%29.pdf.pdf
[^44]: www.owasp.org/index.php/Appendix_A:_Testing_Tools
[^45]: www.cequence.ai/

<!-- PDF p. 119 (book p. 95) -->

- *Web Application Firewall (WAF)*
  - *AppTrana*[^46]
  - *StackPath*[^47]
  - *Sucuri*[^48]
- **Requirement 8.1 – Identify and manage third-party remote/ external access**
  - Manage the remote/external access of vendors
- **Requirement 9.9 – Inventory and Inspection of PTS Devices**
  - Also known as PDQ (Pretty Damn Quick) Devices, an inventory and periodic checks must be carried out.
- **Requirements 10 – Monitoring users and systems use**
  - Based upon the categorized IT systems and users, the monitoring should be able to detect the **ABNORMAL** from NORMAL activities.
  - Centralized monitoring of the various logs sources should be collated to show unauthorized activities, as an attacker carries out reconnaissance to move through your network from the trusted to the untrusted environments.
  - All critical external systems have correct and consistent clock readings, received from secure and industry-accepted external resources.
    - *This is essential in the event of an investigation or forensic examination to piece together an accurate chain of events.*

[^46]: https://apptrana.indusface.com/?utm_source=PPC&utm_medium=Referral&utm_campaign=Comparitech-Product-Listing
[^47]: www.stackpath.com/products/waf/
[^48]: https://sucuri.net/website-firewall/

<!-- PDF p. 120 (book p. 96) -->

- Secure audit trails of all user and external systems activities.
  - *This is essential in the event of an incident to help trace the activities back to the potential “Root Cause.”*
  - *Consider enhanced archiving, exceeding the 12 months between PCI DSS compliance assessments, as attackers are known for remaining dormant for a number of months or years, for example:*
    - *Three months instant, 36 months archive (rather than limiting to the minimum 12 months)*
- Example solutions/products
  - Elastic Stack SIEM[^49]
  - LogRhythm[^50]
  - OSSIM[^51]
  - SIEMonster[^52]
- **Requirement 10.5 – External logs**
  - Logs from external facing systems are written to secure storage systems.
- **Requirement 11.2 – External Vulnerability Scans**
  - Quarterly Approved Scanning Vendor (ASV)[^53] scans

[^49]: www.elastic.co/products/siem
[^50]: https://logrhythm.com/products/nextgen-siem-platform/
[^51]: https://cybersecurity.att.com/products/ossim
[^52]: https://siemonster.com/
[^53]: www.pcisecuritystandards.org/assessors_and_solutions/approved_scanning_vendors

<!-- PDF p. 121 (book p. 97) -->

- **Requirement 11.3 – External Penetration Tests and Segmentation Tests**
  - Confirming the integrity and effectiveness of the external network layers and network segmentation
    - *CREST PTMA*[^54]
- **Requirement 11.4 – Intrusion Detection/Prevention**
  - Alerting on all external systems
    - *OSSEC HIDS*[^55]
    - *Suricata*[^56]
    - *BRO*[^57]
- **Requirement 11.5 – Change Detection**
  - Alerting to notify any potential unauthorized changes made to external systems
- **Requirement 12.4 – Roles and Responsibilities**
  - All personnel with roles and responsibilities for the external systems understand their duties and the potential impact these systems present for the payment card operations.
- **Requirement 12 – People Management**
  - Maintaining a security culture for all personnel responsible for the management of (or with access to) the internal systems and payment card data

[^54]: www.crest-approved.org/2018/07/20/penetration-testing-maturity-assessment-tools/index.html
[^55]: https://sectools.org/tool/ossec/
[^56]: https://suricata-ids.org/
[^57]: https://sourceforge.net/projects/bro-tools/

<!-- PDF p. 122 (book p. 98) -->

- **Requirement 12.10 – An effective Incident Response Process**
  - Having an effective incident response process to rapidly detect and respond to incidents or suspected compromise of external technologies
    - *Demisto*[^58]
    - *CREST IRMA*[^59]
    - *YUDU* [^60]

[^58]: www.demisto.com/
[^59]: www.crest-approved.org/cyber-security-incident-response-maturity-assessment/index.html
[^60]: www.yudu.com/sentinel/emergency-notification
