---
title: "Requirement 11: Assurance Testing"
book: pci-dss-integrated-data-security-standard-guide
chapter: 9
source_pages: "302-305"
format: source-text
---
# Requirement 11: Assurance Testing
(Source: PDF pp. 302-305)

<!-- PDF p. 302 (book p. 280) -->

Think of this section as having periodic internal and external patrols to provide independent assurance that all requirements 1–10 and 12 are still active and effectively safeguarding your payment card operations, seeking to identify poor practices, poor configurations, or exploitable vulnerabilities:

- Rogue Wireless Access devices (circumvent the network defenses to create a “backdoor”)
- Internal network vulnerabilities
- Perimeter network vulnerabilities
- Intrusion testing
- Secure Silo testing
- Web Application testing *(relocated from requirement 6)*

Testing your environment should be considered through the eyes of your attacker, seeking to identify potential exploitation opportunities. Remember that your attackers can originate from both outside and inside your corporate environment. Consequently, the testing should look at the perimeter (network and Web), your untrusted environment, and your trusted environment, confirm the effectiveness of any isolated internal network areas, and test both the network and application layers of your environment. Essential to the effectiveness of testing engagements is to work closely with your testers to confirm the accuracy of the scope of each engagement.

One area that is currently not included in the current version is the concept of security testing the “Human Factor” – otherwise known as Physical Penetration Testing (Social Engineering).[^32]

Having tested your environment, it is critical that you can remediate any failings in a timely manner before they have the potential to impact your business and, most importantly, before your enemies have the ability to exploit them.

Your quarterly vulnerability scanning can be likened to the internal and external patrols that would help identify potential weaknesses in the infrastructure that could provide opportunities for exploitation *(e.g., ajar doors and windows)*.

[^32]: www.elsevier.com/books/social-engineering-penetration-testing/watson/978-0-12-420124-8

<!-- PDF p. 303 (book p. 281) -->

*[Figure omitted]*

**Figure 9-33.** *Internal Patrols (Within the Perimeter)*

<!-- PDF p. 304 (book p. 282) -->

*[Figure omitted]*

The vulnerability scans differ from your penetration and segmentation testing, in that you are looking to dig deeper into your vulnerabilities to see whether by acting like an attacker, you are able to further manipulate to allow additional exploitation *(e.g., plying open a door/window, picking the lock, etc.)*.

Think of it as being the difference between looking for visible weaknesses (vulnerability scanning) and acting like an attacker to manipulate additional exploitation opportunities (penetration testing).

**Figure 9-34.** *External Patrols (Outside the Perimeter)*

<!-- PDF p. 305 (book p. 283) -->

Your penetration testing efforts will apply the known tactics, techniques, and protocols (TTPs) that are employed by your attackers. Consequently, you should ensure that your testing includes the following:

External with average dwell times[^33] on external network layers of 184 days, it is extremely important that you can identify and remediate your vulnerabilities that can be leveraged by your attackers.

Internal with average dwell times of 50.5 days, it is essential that you can identify and remediate any exploitable vulnerabilities that could be exploited by an attacker who manages to breach your perimeter.

It is important to ensure that the testing employs a defined methodology to ensure that it includes the testing of the Network *(OSI Layer 3)* and Application *(OSI Layer 7)* layers.

[^33]: https://content.fireeye.com/m-trends
