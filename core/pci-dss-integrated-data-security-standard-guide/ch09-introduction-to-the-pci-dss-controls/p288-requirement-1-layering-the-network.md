---
title: "Requirement 1: Layering the Network"
book: pci-dss-integrated-data-security-standard-guide
chapter: 9
source_pages: "288-291"
format: source-text
---
# Requirement 1: Layering the Network
(Source: PDF pp. 288-291)

<!-- PDF p. 288 (book p. 266) -->

Filtering traffic as it passes between trusted and internal network zones, ensuring that the firewalls and routers (or their equivalent) are appropriately configured. These act as the “Gate Keepers” to prevent transmissions, that do not adhere to specific security criteria, and also identifying/preventing the connection of rogue/unauthorized devices (*including wireless*). Either of which could compromise the layered network defenses.

Understanding the network topology is essential, and each system component must be identified and visualized in network diagrams to show both the Cardholder Data Environment (CDE) and the delineation of this from the non-CDE. Additionally, the Data Flow Diagram will further visualize the interaction of these CDE systems with CHD.

Any changes to the network should be subject to the change management process, so as to identify the potential impact and rollback options. Remember, the impact decision is essential as this will identify the potential for this being a “Significant Change,” which will invoke additional measures *(vulnerability scanning, penetration testing, etc.)* to confirm that this change has not impacted the integrity of the environment.

All systems identified in the network diagram must correlate with an inventory (as part of requirement 2).

<!-- PDF p. 289 (book p. 267) -->

*[Figure omitted]*

**Figure 9-21.** *Layered Defenses*[^26]

*[Figure omitted]*

**Figure 9-22.** *De-militarized Zone (DMZ) – 1.5 km*

[^26]: https://atwar.blogs.nytimes.com/2010/05/26/the-poo-pond/

<!-- PDF p. 290 (book p. 268) -->

*[Figure omitted]*

**Figure 9-23.** *Filtered Access*[^27]

[^27]: www.raf.mod.uk/our-organisation/force-protection/news/raf-leeming-based-34-squadron-raf-regiment-returns-to-cyprus/

<!-- PDF p. 291 (book p. 269) -->

*[Figure omitted]*

**Figure 9-24.** *CSET*[^28] *Created Network Diagram*

[^28]: www.us-cert.gov/ncas/current-activity/2019/11/04/cset-version-92-now-available
