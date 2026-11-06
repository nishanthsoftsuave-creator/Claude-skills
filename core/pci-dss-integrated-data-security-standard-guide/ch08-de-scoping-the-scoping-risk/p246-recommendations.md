---
title: "Recommendations"
book: pci-dss-integrated-data-security-standard-guide
chapter: 8
source_pages: "246-249"
format: source-text
---
# Recommendations
(Source: PDF pp. 246-249)

<!-- PDF p. 246 (book p. 224) -->

Ensure that your asset inventory is categorized in a manner that easily shows your in-scope **RED** assets (*e.g., Critical Asset Inventory*), as well as documenting any other assets within your business (*e.g., Business Asset Inventory*).

An example of such an approach can be seen in ISACA’s Open PCI Scoping Toolkit.[^21]

| Cat 1a. | Devices that store, process, or transmit cardholder data |
|---|---|
| Cat 1b. | Devices that do not store, process, or transmit cardholder data, but are “infected by”<br>Category 1a devices due to the absence of controlled access or isolation |
| Cat 2a | system components which, through controlled access, provide security services (e.g., authentication) to a Category 1 device |
| Cat 2b | system components which, through controlled access, can initiate an inbound connection to a Category 1 device |
| Cat 2c | system components which, through controlled access, can only receive a connection from a Category 1 device (i.e., cannot initiate a connection). Category 2x system components which, through indirect and controlled access, have the ability to administer<br>Category 1 devices<br>Note: Category 2x devices have no direct access to/from Category 1 devices. |
| Cat 2x | system components which, through indirect and controlled access, have the ability to administer Category 1 devices<br>Note: Category 2x devices have no direct access to/from Category 1 devices. |
| Cat 3 | system components do not store, process, or transmit cardholder data and are isolated from and do not provide any services to any Category 1 device. |

Having identified and categorized your business assets based upon their criticality, it is then extremely important to visualize their interactions and connections.

This is achieved through the use of asset inventory aligned to Data Flow and Network Diagrams. Think of these as being like State/County and City/Town/District maps.

[^21]: www.isaca.org/Groups/Professional-English/pci-compliance/GroupDocuments/OpenPCIScopingToolkit.pdf

<!-- PDF p. 247 (book p. 225) -->

## High-Level Overview

This provides an overview of all your business assets (e.g., State view), as well as the location of the CDE.

*[Figure omitted]*

## Detailed-Level Overview

This shows the critical assets and their associated connections within the CDE. As a consequence, any **BLACK** assets that may be interacting, connected to, or have a potential impact on the **RED** would become **BROWN** and would need to be investigated further.

**Figure 8-6.** *New York State*

<!-- PDF p. 248 (book p. 226) -->

*[Figure omitted]*

This approach will help you confirm how accurately you have scoped your PCI DSS and help identify any potential **BROWN** assets that could impact your business if neglected or overlooked.

As part of your penetration and segmentation testing, these supporting documents should be periodically reviewed and be provided to the personnel who will carry out the penetration/segmentation testing.

Remember that the identification and maintenance of your scoping should not be limited to your network and systems infrastructure and it remains just as important to extend this process to your physical and applications environments.

**Figure 8-7.** *New York City*

<!-- PDF p. 249 (book p. 227) -->

For example, in regard to your applications, it is highly recommended that you consider the incorporation of the following:

- Maintain a complete list of your applications inventory.
- Identify where these applications hosted in your network.
- Identify the architecture of the applications including programming language, database type used, authentication, and authorization controls.
- Identify the encryption used for secure communications.
- Identify the encryption used in the application and database.

Start by thinking of your business as being completely flat and with everything being interconnected in some way. Much like a flat network, everything is in-scope and needs some form of protection from malicious attackers (both internal and external); however, the amount of protective measures you apply is dependent on the aggregated value of the services that they provide. As you identify the assets and their connections, you should color code them based upon their potential risk/importance to your business. These color-coded assets should then be articulated onto your supporting network and data flow diagrams.

Your identified systems that support your payment card operations are high risk and must be protected using the PCI DSS integrated controls framework, while any other business critical assets should also be protected against any known threats. Although you only need to ensure that your payment card environment is compliant with the PCI DSS integrated control framework, you should consider the additional benefits of fortifying your environments outside the scope of your PCI DSS program.

For example, consider

- The implications of Maersk incident, where their business systems (non-PCI DSS) were impacted by the NotPetya vulnerability[^22]
- The potential impact on your company brand/reputation if a vulnerability in your web interfaces (non-PCI DSS) were to be subjected to digital graffiti or defacement[^23]

[^22]: www.wired.com/story/notpetya-cyberattack-ukraine-russia-code-crashed-the-world/
[^23]: https://blog.radware.com/security/attack-types-and-vectors/2019/09/defacements-the-digital-graffiti-of-the-internet/
