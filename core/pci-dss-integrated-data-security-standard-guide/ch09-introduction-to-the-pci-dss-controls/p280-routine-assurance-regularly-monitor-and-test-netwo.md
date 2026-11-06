---
title: "Routine Assurance (Regularly Monitor and Test Networks)"
book: pci-dss-integrated-data-security-standard-guide
chapter: 9
source_pages: "280-284"
format: source-text
---
# Routine Assurance (Regularly Monitor and Test Networks)
(Source: PDF pp. 280-284)

<!-- PDF p. 280 (book p. 258) -->

Monitor and Detect

*[Figure omitted]*

<!-- PDF p. 281 (book p. 259) -->

This is compartmentalized into two sections:

**Part 1:** This is your early warning and alerting component of the PCI DSS controls framework, and it relies on the aforementioned areas having been correctly configured and implemented, so that an organization can easily identify and respond to investigate suspicious activities associated to the CDE and personnel with authorized access.

Note under v3.2.1, the following requirements are listed under part 2 of this particular section.

- Use the strategic placement of Intrusion Detection Systems (IDS)/Intrusion Prevention Systems (IPS) to detect and prevent unauthorized incursions into the CDE.
- Employ change detection technologies to provide alerts against any changes to the supporting network and systems.

**Part 2:** Consider this to be your routine internal and external patrols, checking for exploitable weaknesses. This involves the mandatory routine testing of the CDE to provide assurance that the CDE remains to be secure.

Testing includes

- Mandatory testing/physical inspections to detect rogue devices
  - Rogue personnel with authorized access may choose to connect rogue devices in order to bypass the defenses, for example, creating a Wi-Fi connection (N.B. Applicable whether or not the CDE has Wi-Fi infrastructure).
- Mandatory vulnerability scanning and confirmation of effective and timely remediation on internal and external facing IT systems
  - Additional scanning may be required after a significant change has occurred.
- Mandatory intrusion (penetration) and web application testing to validate that no exploitable vulnerabilities remain on internal or external facing IT systems
  - Additional testing may be required after a significant change has occurred.

<!-- PDF p. 282 (book p. 260) -->

Note under v.3.2.1 web application testing is included in the Secure development operations and is separate to the penetration testing requirement.

- Network and Systems Segmentation testing

## Reality Bites

During deployments into hostile environments, the importance of effective monitoring and testing was abundantly apparent. However, it became increasingly clear that the insurgents were doing exactly the same.

While carrying out security patrols of the internal zone, adjacent to the external perimeter fence *(stretching for 15 km)*, the dog patrols needed to be covertly deployed to enable the protection of a more condensed region around a weapon storage facility. The morning following one of the nightly patrols, the area upwind and outside of my internal patrol area had been compromised. The opportunist insurgents had cut through the perimeter fence and broken into an isolated storage building, stealing some low-value items. It is likely that these insurgents had spent many hours, days, or months monitoring our patrol activities.

<!-- PDF p. 283 (book p. 261) -->

*[Figure omitted]*

Your attackers will test your “rules of engagement”[^23] (RoE) and understand what your NORMAL activities look like. This will help them develop their skills to improve their chances of evading detection and to successfully compromise your network and

**Figure 9-17.** *Patrol Dog “Snap” (a.k.a. “The Hound of Basrahville”* [^22]*)*

[^22]: www.mirror.co.uk/news/uk-news/the-hound-of-basraville-561573
[^23]: www.businessdictionary.com/definition/rules-of-engagement.html

<!-- PDF p. 284 (book p. 262) -->

sensitive data assets. Remember that not every attacker’s activities are intended to compromise or steal your data and that a great deal of their actions can be part of their reconnaissance and testing of your business environment.

During a CIFT tour in Afghanistan, I experienced the insurgents carrying out exactly the same tactics approach. On one occasion, the external main access point observed a lone female walking directly toward them, across an expansive, arid, and isolated desert landscape. This lone female was wearing open-toed casual sandals *(not suitable for many miles of hiking across this hostile terrain)*, with a shawl covering her arms crossed across her body, head down, and muttering in a non-local language *(neither Pashto or Dari)*. Despite escalating challenges for her to halt, she continued walking directly toward the perimeter security post – everything you might associated with the actions of a suicide bomber.

Fortunately, the CIFT interpreter was able to speak five languages and recognized that this lone female’s mutterings *(translated as “I’m going to Mecca”)* were in Urdu *(a language native to Northern Pakistan – over 900 km),* and we were able to de-escalate the situation before it got out of hand. Further investigations with the ANP identified the lone female to have mental health issues, who had been picked up and transported from Northern Pakistan by persons unknown, dropped off adjacent to the military base, and she was told that Mecca was in the direction of the base.

It is extremely likely that the insurgents were observing from a distance and were using this lone vulnerable female to test our RoEs.

If your attackers have recognized the importance of monitoring and testing your activities, then should you not be doing the same to identify their **ABNORMAL** activities?
