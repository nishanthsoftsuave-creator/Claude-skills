---
title: "Chapter 11: Compliance – A Team Effort (opening)"
book: pci-dss-integrated-data-security-standard-guide
chapter: 11
source_pages: "344-349"
format: source-text
---
# Chapter 11: Compliance – A Team Effort (opening)
(Source: PDF pp. 344-349)

<!-- PDF p. 344 (book p. 323) -->

Throughout my 22-year career in the RAF Police, I was continually reminded of the importance the concept of teamwork plays in developing and maintaining effective defenses.

Be this in the form of me providing the first line of defense *(providing covert nightly security patrols of the perimeter fence delineation between the Badlands in Basra, Iraq (Working as a team of two dog units (one on foot and one in mobile support-driving in complete darkness to avoid detection)))* right through to working as the counter intelligence field team (CIFT) component of a deployed Force Protection regiment, in Afghanistan – each and every role was an essential component of the defensive efforts and was heavily reliant on the personnel receiving the initial level of training to deliver their roles and responsibilities and continuing a high level of investment in continual training, to meet the ever-evolving and demanding challenges of the assignments.

However, since entering the corporate environment, I have rarely observed businesses appreciate the need to invest in the development and maintenance of cohesive team approaches to effectively defend their realms. In contrast, many organizations appear to under invest in training and team building of their defensive units and with many working in conflict against each other – almost in a state of blame gaming, rather than as a cohesive unit.

This is probably the single most important element of the PCI DSS integrated framework. Unfortunately *(much like other industry security standards/frameworks)*, the current version of the standard does not articulate its importance for reducing the risks associated with poorly integrated processes (a.k.a. Teamwork). This chapter will explain the reason for my approach of making requirement 1 the layer that underlies all the others.

<!-- PDF p. 345 (book p. 324) -->

*[Figure omitted]*

This approach is designed to be complementary to, and should not be confused with, the Payment Card Industry Security Standards Council’s (PCI SSC’s) prioritized approach,[^1] which prioritizes the controls in order of milestones, based upon the perceived risks:

1. Remove sensitive authentication data and limit data retention.

2. Protect systems and networks and be prepared to respond to a system breach.

3. Secure payment card applications.

4. Monitor and control access to your systems.

5. Protect stored cardholder data.

6. Finalize remaining compliance efforts and ensure all controls are in place.

**Figure 11-1.** *Requirements’ Pyramid*

[^1]: www.pcisecuritystandards.org/documents/Prioritized-Approach-for-PCI-DSS-v3_2_1.pdf ?agreement=true&time=1577538686226

<!-- PDF p. 346 (book p. 325) -->

Any effective Data Privacy and Security program is heavily reliant on the human factor; however, businesses still too often regard compliance as being IT systems focused. Unfortunately, this reluctance to invest into the people skills can significantly increase the risks of something going wrong, which could lead to a compromised system or data breach. In recent reports[^2] the human factor was cited as being the cause of between **67%** and **90%** of all security incidents.

In reality, the human factor is more likely to be the **100%** causal reason behind every compromised system, incorrect transmission, or data breach.

How can this be? It is difficult to find a single reported data breach where the human factor has not had an influence on the cause of security incident. Let’s take a look at some of the notable events from 2019:

1. **Adobe Inc**[^3]

- *Poorly configured Elasticsearch database –* **7.5 million** *compromised records*

2. **Canva**[^4]

- *On discovery of the attack, Canva immediately took action to fix the cause of the breach (exposed data included usernames, email addresses, and encrypted passwords, which were salted and hashed with the bcrypt algorithm). However, this action did not prevent the unauthorized access to and exfiltration of customers’ sensitive data –* **139 million** *compromised records.*

3. **Capital One**[^5]

- *An Amazon Web Services third-party contractor carried out the deliberate extraction of data stored on Amazon’s servers –* **106 million** *compromised records.*

[^2]: www.csoonline.com/article/3504813/the-human-factor-of-cyber-security.html
[^3]: www.comparitech.com/blog/information-security/7-million-adobe-creative-cloud-accounts-exposed-to-the-public/
[^4]: www.zdnet.com/article/australian-tech-unicorn-canva-suffers-security-breach/
[^5]: https://edition.cnn.com/2019/07/29/business/capital-one-data-breach/index.html

<!-- PDF p. 347 (book p. 326) -->

4. **DoorDash**[^6]

- *Poor security controls allowed a hacker to gain unauthorized access to customers’ data –* **4.9 million** *compromised records.*

5. **First American Corporation**[^7]

- *Insecure by design in one of its production applications, enabled the unauthorized access and exfiltration of sensitive data –* **885 million** *compromised records.*

6. **JustDial**[^8]

- *Four unprotected application program interfaces (APIs) had enabled a hacker to gain unauthorized access to steal customers’ sensitive data – reported to be* **100 million** *compromised records.*

7. **Mobile TeleSystems (MTS)**[^9]

- *During a handover of a data folder, an unnamed third party failed to follow their company’s business processes, security policies, and their personal responsibility to protect the sensitive data –* **100 million (1.7 Tb)** *compromised records.*

8. **Truecaller**[^10]

- *Despite the reports of millions of customer records (all with Truecaller ID apps) being available for sale,*[^11] *Truecaller have denied that their database has been breached. However, they have confirmed that they have discovered evidence of employees carrying out “data scraping*[^12]*” – reported to be between* **100 and 300 million** *compromised records.*

[^6]: https://techcrunch.com/2019/09/26/doordash-data-breach/
[^7]: https://techcrunch.com/2019/09/26/doordash-data-breach/
[^8]: https://economictimes.indiatimes.com/tech/internet/data-breach-at-justdial-leaks-100-million-user-details/articleshow/68930607.cms
[^9]: www.upguard.com/breaches/mts-nokia-telecom-inventory-data-exposure
[^10]: https://analyticsindiamag.com/data-breach-truecaller-exposes-indian-users-data-shows-cracks-in-cyber-security-infrastructure/
[^11]: www.bankinfosecurity.asia/researcher-data-leaked-for-300-million-truecaller-users-a-12519
[^12]: www.techopedia.com/definition/33132/data-scraping

<!-- PDF p. 348 (book p. 327) -->

9. **Zynga**[^13]

- *A poorly configured social mobile game enabled the unauthorized access to a connected database –* **218 million** *compromised records.*

10. **Westpac**[^14]

- *Failure to identify and respond quickly to a brute force attack on a payment platform (PayID) enabled the hacker to compromise customer details before containment was established –* **98,000** *(of 100,000) compromised records.*

It is reported that in the first six months of 2019, a total of **4.1 billion** records were compromised[^15] and with the global average cost of a data breach estimated at **$3.92 million**[^16] and with an average cost of $150 per compromised record, this becomes an ever-increasing risk to today’s digital/Internet-connected businesses. Consequently, it is essential that businesses adopt a team approach to their compliance efforts, ensuring that adequate investment is made to ensure that the team members (game players) have and maintain sufficient motor skills/knowledge to effectively develop and maintain the systems integrity while being able to rapidly respond to unusual events or incidents.

The maintenance of an effective compliance program has very similar similarities to the maintenance of a competitive team sport (e.g., American Football, Baseball, Basketball, Cricket, Football (Soccer), Ice Hockey, Rugby League, Rugby Union, Volleyball, Water Polo, etc.). Consequently, any organization seeking to develop and mature their compliance programs should look at applying some lessons from their favorite team sport.

[^13]: https://venturebeat.com/2019/09/30/words-with-friends-player-data-allegedly-stolen-for-218-million-users/
[^14]: https://finance.nine.com.au/business-news/westpac-data-breach-100000-australian-customers-at-risk/84c91581-90b6-464e-9137-a2d973492614
[^15]: www.forbes.com/sites/daveywinder/2019/08/20/data-breaches-expose-41-billion-records-in-first-six-months-of-2019/#71077994bd54
[^16]: www.ibm.com/security/data-breach?cm_mmc=OSocial_Blog-_-Security_Optimize+the+ Security+Program-_-WW_WW-_-CODB2019Blog_ov70891&cm_mmca1=000000NJ&cm_mmca2= 10000253&_ga=2.155608443.1344017930.1577447996-405938945.1575975888&cm_mc_uid= 69077084300315759758876&cm_mc_sid_50200000=52560441577447996051&cm_mc_sid_5264000 0=74762651577447996076

<!-- PDF p. 349 (book p. 328) -->

Such an approach should make the compliance program more effective and enjoyable, whilst significantly increasing the skill levels and, thus, considerably decrease the potential risk of a compromise system/network or data breach?
