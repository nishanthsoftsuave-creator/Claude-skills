---
title: "Security Information and Event Management (SIEM)"
book: pci-dss-integrated-data-security-standard-guide
chapter: 13
source_pages: "421-424"
format: source-text
---
# Security Information and Event Management (SIEM)
(Source: PDF pp. 421-424)

<!-- PDF p. 421 (book p. 400) -->

- Identification
  - Critical Systems connections
  - User activities against critical systems connections
- Alignment to pillars 1, 2, and 3

<!-- PDF p. 422 (book p. 401) -->

The purpose of an effective SIEM process is to ensure the timely identification of abnormal activities. However, to enable this, you need to have refined and matured the aforementioned pillars (1, 2, and 3). It is important to remember that your attackers are extremely unlikely to act quickly and will prefer to achieve a persistent presence within your corporate environment, taking their time to carry out clandestine reconnaissance and planning before making their move.

TechTarget[^36] explains the concept of SIEM as:

security information and event management (SIEM) is an approach to security management that combines SIM (security information management) and SEM (security event management) functions into one security management system. The acronym SIEM is pronounced “sim” with a silent e.

the underlying principles of every SIEM system is to aggregate relevant data from multiple sources, identify deviations from the norm and take appropriate action. For example, when a potential issue is detected, a SIEM might log additional information, generate an alert and instruct other security controls to stop an activity’s progress.

at the most basic level, a SIEM system can be rules-based or employ a statistical correlation engine to establish relationships between event log entries. Advanced SIEMs have evolved to include user and entity behavior analytics (UEBA) and security orchestration and automated response (SOAR).

[^36]: https://searchsecurity.techtarget.com/definition/security-information-and-event-management-SIEM
[^37]: www.zdnet.com/article/marriott-ceo-shares-post-mortem-on-last-years-hack/

<!-- PDF p. 423 (book p. 402) -->

Some examples of the value of having an effective SIEM process can be seen through the following incidents:

- **Marriott**[^37]
- Following the acquisition of the Starwood company, Marriott inherited Remote Access Trojan (RAT)[^38] and Mimikatz[^39] malicious software. An abnormality was detected through the monitoring being carried out by the IBM Guardian software, which alerted Marriott to the presence of malicious activity occurring within their corporate environment. It is believed that the attackers had remained undetected for around 4 years,[^40] and given the length of time, they remained undetected, and the root cause/delivery method was never identified.
- **Citrix**[^41]
- Attackers gained access to the Citrix internal network through password spraying, a technique that exploits weak passwords. Once within the network, the attackers intermittently accessed and stole business documents and files from a company shared network drive that has been used to store current and historical business documents, as well as a drive associated with a web-based tool used in their consulting practice. It is reported that the attackers remained undetected for a period of 6 months.[^42]

Bearing in mind the fact that criminals will attempt to remain undetected for long periods of time, maintaining secure log records covering a sufficient period of time is essential in trying to identify the actions taken by the attackers and the potential root causes.

[^38]: https://searchsecurity.techtarget.com/definition/RAT-remote-access-Trojan
[^39]: www.varonis.com/blog/what-is-mimikatz/
[^40]: https://krebsonsecurity.com/2018/11/marriott-data-on-500-million-guests-stolen-in-4-year-breach/
[^41]: www.zdnet.com/article/hackers-lurked-in-citrix-systems-for-six-months/
[^42]: www.bankinfosecurity.com/citrix-hackers-camped-in-tech-giants-network-for-6-months-a-12436

<!-- PDF p. 424 (book p. 403) -->

For PCI DSS compliance, the current mandatory log retention periods are **3 months immediately available** for analysis, with **at least 1 year of auditable history** *(e.g., online, archived, or restorable from backup)*. Given the known TTPs of attackers remaining dormant for many months, and even years, you may want to choose longer archive retention periods.
