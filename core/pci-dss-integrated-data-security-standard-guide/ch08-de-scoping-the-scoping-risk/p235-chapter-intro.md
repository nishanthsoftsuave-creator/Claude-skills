---
title: "Chapter 8: De-scoping the Scoping Risk (opening)"
book: pci-dss-integrated-data-security-standard-guide
chapter: 8
source_pages: "235-238"
format: source-text
---
# Chapter 8: De-scoping the Scoping Risk (opening)
(Source: PDF pp. 235-238)

<!-- PDF p. 235 (book p. 213) -->

Scoping means[^1]

*The PCI DSS security requirements apply to all system components included in or connected to the cardholder data environment. The cardholder data environment (CDE) is comprised of people, processes and technologies that store, process, or transmit cardholder data or sensitive authentication data. “System components” include network devices, servers, computing devices, and applications.*

—PCI DSS v3.2.1,[^2] p. 10

Although de-scoping your CDE from your non-CDE is highly recommended, it is not currently a mandated requirement. However, if you should decide to reduce your PCI DSS burden and the associated risks, it is essential that you understand the effectiveness of any scoping efforts.

As well as reducing your PCI DSS compliance burden, an effectively scoped environment will help reduce the potential risk from an attacker breaching your out-of-scope environment and moving laterally[^3] until they identify a hole in your CDE defenses or leveraging a weakness of connected third parties (Island Hopping[^4]) to gain unauthorized access to your CDE.

[^1]: www.pcisecuritystandards.org/documents/Guidance-PCI-DSS-Scoping-and-Segmentation_v1.pdf
[^2]: www.pcisecuritystandards.org/document_library
[^3]: https://awakesecurity.com/glossary/lateral-movement/
[^4]: www.itpro.co.uk/cyber-attacks/33200/what-is-island-hopping

<!-- PDF p. 236 (book p. 214) -->

Traditionally in the military, they would have two entirely separate and isolated environments – **RED** (subject to stringent control) for the highly sensitive operations *(Top Secret and Secret)* and **BLACK** for the less sensitive operations *(Confidential and Restricted)*.

For example, within a military base (**BLACK**), there could be a highly sensitive center of operations (**RED**), providing critical support services to military operations around the globe. Due to the sensitivity and criticality of these operations, it has its own suite of mitigation controls (e.g., separate access controls, secure rooms, security cabinets, CCTV, alarms, security checks, etc.). Access to this facility is strictly limited based upon specific need to know and need to access requirements. Just because personnel have the right to access the **BLACK** does not give them the automatic right to gain access to the **RED**.

The **RED** was further enhanced through the application of additional mitigation controls that were applied for the defense of the **BLACK**.

*[Figure omitted]*

**Figure 8-1.** *Secure Enclave Within a Military Base*

It is unlikely that your business will have the desire or budget to build military grade defenses by dedicating an entirely separate and isolated environment. However, similar principles can be applied to your business through the use of segmentation. Think of your CDE as being **RED** assets, any out-of-scope assets as being **BLACK** assets, and any <!-- PDF p. 237 (book p. 215) --> that set within a buffer zone as being **BROWN** assets. As well as having identified and documented all your **RED** and **BLACK** assets, it is important to ensure that any potential impacting **BROWN** assets are identified, **for example, Network and Systems.**

*[Figure omitted]*

**Figure 8-2.** *Network De-scoping*

<!-- PDF p. 238 (book p. 216) -->

Understandably, there needs to be a clear delineation area between the **RED** and **BLACK** assets for you to consider these to be out-of-scope for your PCI DSS program and that this does not only apply to networks and systems but also your third parties *(e.g., VPN entry/egress connections, within an infrastructure as a service (IAAS) provider)*, infrastructure *(e.g., open plan offices, where payment card operations are carried out)*, and personnel *(e.g., maintenance personnel with access to all areas of the business).*

Remember, as the entity, you are responsible for ensuring that the de-scoping of your environment is accurate and there is not potential “muddying of the waters” by omitting assets that could be leveraged by an attacker against your CDE.
