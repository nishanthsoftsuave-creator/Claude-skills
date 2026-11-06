---
title: "Lessons Learned from History"
book: pci-dss-integrated-data-security-standard-guide
chapter: 8
source_pages: "239-240"
format: source-text
---
# Lessons Learned from History
(Source: PDF pp. 239-240)

<!-- PDF p. 239 (book p. 217) -->

These types of incidents are not new and are not the only occasions that attackers have managed to compromise an environment, using the out-of-scope areas. Take, for instance, in 2013, when the 15-year-old Russian hacker that managed to compromise Target’s[^11] CDE, through the “piggy-backing” onto the connection from a third-party air conditioning company's network connection.

Looking further back into history, the City of Troy[^12] suffered a similar fate to their physical security defenses around 1200 BC, when their outer defenses were compromised after a clandestine army was wheeled inside. This enabled a refreshed enemy to launch an offensive from inside the perimeter, leaving the Troy army little time to respond and react.

[^11]: https://arxiv.org/pdf/1701.04940.pdf
[^12]: www.livescience.com/38191-ancient-troy.html

<!-- PDF p. 240 (book p. 218) -->

*[Figure omitted]*

When de-scoping your PCI DSS scope, it is extremely important to apply the lessons from history and the military, so that you understand and apply the principles of having concentrated security controls *(using the PCI DSS controls framework)* on your **RED** environment but without neglecting the need to protect your **BLACK** environments *(perhaps through the use of a separate security controls framework, e.g., NIST CSF*[^13] *or CIS 20 CSC*[^14]*)*. You would validate that your CDE is secure through the accurate validation of the de-scoping of the environment (**RED**) and to validate that this environment is protected and assessed against the PCI DSS controls framework. Additional defensive layers would be applied to the outer environment (**BLACK**) through the application and validation of a secondary controls framework. Where controls are commonly applied across the **BLACK** and **RED**, the default defensive control would be the more robust control.

[^13]: www.nist.gov/cyberframework
[^14]: www.cisecurity.org/controls/cis-controls-list/
