---
title: "Reality Bites"
book: pci-dss-integrated-data-security-standard-guide
chapter: 8
source_pages: "242-245"
format: source-text
---
# Reality Bites
(Source: PDF pp. 242-245)

<!-- PDF p. 242 (book p. 220) -->

An equivalent example would be in the case of the Landry’s data breach,[^17] where their point-to-point (P2P)[^18] technology (**RED**) was undermined when their employees mistakenly swiped customers’ payment cards on devices used to enter kitchen and bar orders (**RED/BROWN/BLACK**), which are different devices than the point-of-sale terminals used for payment processing. Clearly Landry’s had recognized the benefits of de-scoping their payment card operations but did not consider the potential impact the out-of-scope systems would potentially have on their business.

However, Landry’s are not the only restaurant business to have had their point-of-sale (POS) systems compromised by opportunist attackers in 2019.[^19]

| Dates Affected Business Impacted |  | Details |
|---|---|---|
| 2019 | Landry’s | Landry’s, the parent company of over 600 restaurants, casinos, and hotels, including Bubba gump shrimp,<br>Joe’s Crab shack, M grille, and rainforest Cafe, reported that they detected unauthorized access to the network supporting their payment processing systems between<br>March and october of 2019. |
| 2019 | Wawa | over 800 of Wawa’s convenience stores had pos malware planted in their systems that went undetected for 8 months. the malware is said to have harvested payment information, like names, card numbers, and expiration dates. |
| 2019 | Catch hospitality | Catch nYC, Catch steakhouse, and Catch rooftop disclosed the presence of pos malware in their systems between<br>March and october of 2019 that searched for track data, which could include cardholder and card information.<br>(continued) |

[^17]: www.landrysinc.com/CreditNotice/
[^18]: www.pcisecuritystandards.org/assessors_and_solutions/point_to_point_encryption_solutions
[^19]: https://upserve.com/restaurant-insider/pos-data-breaches/

<!-- PDF p. 243 (book p. 221) -->

| Dates Affected Business Impacted |  | Details |
|---|---|---|
| 2019 | DoorDash | in september the company announced that a breach – which occurred on May 4 and affected users who created accounts before april 5, 2018 – affected 4.9 million customers, delivery workers, and merchants who had information stolen by hackers including names, email and delivery addresses, order history, phone numbers, and passwords. |
| 2019 | Checkers and rally’s | Malware planted by hackers collected credit card information from systems at over 100 locations. almost 15% of locations were compromised from software that was installed in september of 2018. |
| 2019 | Mudshark Brewing<br>Company and other arizona restaurants | an investigation of “suspicious activity” led to the uncovering of dozens of arizona restaurants having data breaches that may have compromised customers’ personal information. |

Yet another victim of the Magecart-style attacks, Macy’s online[^20] (www.macys.com) was also the victim of a man-in-the-middle attack. The attackers had injected malicious code into an out-of-scope (**BLACK**) web page in the customers’ e-Commerce journey.

As you can see in Figure 8-4, Macy’s has a large and complex digital web-based footprint.

[^20]: www.documentcloud.org/documents/6552530-MACY-S-NOTICE-OF-DATA-BREACH.html

<!-- PDF p. 244 (book p. 222) -->

*[Figure omitted]*

**Figure 8-4.** *Macys.com Topology – DNS Dumpster*

<!-- PDF p. 245 (book p. 223) -->

*[Figure omitted]*

Consequently, the attackers were able to divert the customers’ journey through their infrastructure, enabling them to carry out harvesting of the customers’ payment card input into the in-scope (**RED**) e-Commerce interface. Although the vulnerable out-of-scope web page was not directly involved in the processing, storage, or transmission of payment card data, it was involved in the journey to hand over to the secure payment interface. Therefore, the attackers were unable to compromise the in-scope (**RED**) interface so had taken the opportunity to exploit vulnerabilities to the adjoining web pages.

Macy’s has complex web interfaces, the greater the need to fortify both your in-scope (**RED**) and out-of-scope (**BLACK**) environments to help reduce the adjoining web pages from turning a muddy **BROWN** color.

**Figure 8-5.** *Macys.com – VirusTotal*
