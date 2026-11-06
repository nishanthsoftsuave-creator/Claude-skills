---
title: "Asset Management"
book: pci-dss-integrated-data-security-standard-guide
chapter: 13
source_pages: "407-414"
format: source-text
---
# Asset Management
(Source: PDF pp. 407-414)

<!-- PDF p. 407 (book p. 386) -->

- Identification
- Categorization
- Prioritization
- Linkages

<!-- PDF p. 408 (book p. 387) -->

- Secure Configurations
- Life-Cycle Management

NIST have recognized the importance of having an effective IT Asset Management[^4] process to complement existing asset management, security, and network systems. Much like Market Business News’ Asset Management[^5] definition, assets supporting critical business operations need to be effectively maintained for optimal efficiency and effectiveness across their life cycles.

asset management refers to the management of people’s assets. the term also applies to dealing with other organizations’ or companies’ investments. assets include either intangible or intangible assets.

intangible assets are things we cannot touch such as intellectual property, goodwill, financial assets, or human capital. tangible assets, on the other hand, are things we can touch, including buildings, land, computers, and office equipment.

As a student in Counter Intelligence operations, I was taught the value of asset management within any defense strategy, and despite being hundreds of years old, the concept still rings true in the modern era. Medieval castles would be designed so that the infrastructures supported layered and segmented environments.

Consequently, it is essential that you are able to trace the data journeys, through your infrastructure, from the point of being used, right through to be securely stored, handed off to an approved third party, or securely destroyed/disposed of once the data is no longer needed.

Each of the industry security controls frameworks has prioritized Asset Management. The following data is an example.

[^4]: https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.1800-5.pdf
[^5]: https://marketbusinessnews.com/financial-glossary/asset-management/

<!-- PDF p. 409 (book p. 388) -->

Asset Management

- NIST CSF – ID.AM[^6] (Stage 1: IDENTIFY)
  - ID.AM-1

physical devices and systems within the organization are inventoried.

- ID.AM-2

software platforms and applications within the organization are inventoried.

- ID.AM-3

organizational communication and data flows are mapped.

- ID.AM-4

external information systems are catalogued.

- ID.AM-5

resources (e.g., hardware, devices, data, time, personnel, and software) are prioritized based on their classification, criticality, and business value.

- ID.AM-6

Cyber security roles and responsibilities for the entire workforce and third-party stakeholders (e.g., suppliers, customers, partners) are established.

- PCI DSS[^7] – Requirements
  - 1.1.1; 1.1.2; 1.1.3; 2.4; 9.6.1; 9.9; 11.1.1; 12.2; 12.3.3; 12.3.7; 12.4, 12.5, 12.8, and 12.9
- CIS 20 Critical Security Controls – 1 and 2 (Basic Controls)
  - CIS Control 1 – Inventory and Control of Hardware Assets[^8]

actively manage (inventory, track, and correct) all hardware devices on the network so that only authorized devices are given access and unauthorized and unmanaged devices are found and prevented from gaining access.

[^6]: www.nist.gov/cyberframework/framework
[^7]: www.pcisecuritystandards.org/document_library
[^8]: www.cisecurity.org/controls/inventory-and-control-of-hardware-assets/

<!-- PDF p. 410 (book p. 389) -->

- CIS Control 2 – Inventory and Control of Software Assets[^9]

actively manage (inventory, track, and correct) all software on the network so that only authorized software is installed and can execute and that unauthorized and unmanaged software is found and prevented from installation or execution.

- ISO/IEC 27001:2013[^10] – A8: Asset Management
  - A.8.1

the responsibility for assets. the objective in this annex is to identify information assets in-scope for the management system and define appropriate protection responsibilities.

- A.8.2

to ensure that information receives an appropriate level of protection in accordance with its importance to the organization (and interested parties such as customers) to prevent unauthorized disclosure, modification, removal, or destruction of information stored on media

- Standards of Good Practice (SoGP) 2018[^11] – Physical Asset Management
  - Principle

robust, reliable hardware should only be acquired (e.g., purchased or leased) following consideration of security requirements and identification of security deficiencies.

- Objective

to ensure that hardware provides the required functionality and does not compromise the security of critical or sensitive information and systems

[^9]: www.cisecurity.org/controls/inventory-and-control-of-software-assets/
[^10]: www.iso.org/isoiec-27001-information-security.html
[^11]: www.securityforum.org/tool/the-isf-standard-good-practice-information-security-2018/

<!-- PDF p. 411 (book p. 390) -->

Each of these controls frameworks recommends that business prioritize Asset Management, which means identifying, cataloguing, and visualizing your assets.

Essential to effective asset management is ensuring that you are able to identify the importance of the assets to your business’s objectives and goals. Categorize the assets based upon which are the most important (life support) and which could impact these systems.

This is not as easy as it sounds and may need input from various team members and certainly not limited to your IT team.

Let me give you a real-life example. In 2002, having successfully completed my Counter Intelligence (CI) course, I was assigned my first CI job – CI Junior Non-Commissioned Officer (JNCO) for an RAF Station, whose mission statement was to

*“Train the pilots of the future!”*

With all this new knowledge, my first job was to put this theory into practice and to establish an effective Asset Management process that supported the mission statement.

My first port of call was to speak with the Chief Instructor, so as to ascertain how many aircraft were needed to sustain the pilot training course. Out of a fleet of 30 aircraft, 22 aircraft needed to remain serviceable. With this in mind, 22 aircraft were added to my “Critical Asset Register” and 8 aircraft were added to the “Unit Asset Register.” When aircraft were deployed or became unserviceable, this would be reflected in their associated asset registers. When the available spare aircraft (from the “Unit Asset Register”) started to exceed the risk tolerances, this could be escalated to Command, ensuring that we had the support to maintain the mission statement.

Failure to maintain the mission statement had the potential for serious collateral damage, with the student pilots being unable to complete their training on time and, thus, being able to move onto their specialist pilot training (e.g., Fast Jets, Transports, Helicopters, etc.). This, in turn, could have the greater potential impact to the RAF not having sufficient numbers of pilots to support the RAF’s Strategy.[^12]

Purpose to deliver air and space power for the United Kingdom.

Goal harness the full potential of our people, our aircraft, and our systems.

[^12]: www.raf.mod.uk/documents/PDF/Royal-Air-Force-Strategy/

<!-- PDF p. 412 (book p. 391) -->

However, that was not a problem for me as I had my Asset Management process in place and everything was running smoothly, with me being fully informed of the risks associated with any assets that might impact the mission statement.

How wrong could I have been? A few months later, I was in the tea bar of the aircraft ground engineers, having a chat, over a coffee, with one of the support engineers. During my chat, I happened to mention my “*awesome”* Asset Management process, only for the engineer to reach under the coffee table, pull out a tatty, unzipped, tool bag. The engineer proceeded to pull out an extremely worn and dirty socket head. He proceeded to ask me whether I had listed this item in my “*awesome”* Asset Registers. I had to confess that I had not!

Imagine my shock when I learned the importance of this socket head. To remain serviceable, each of the aircraft needed to have a number of bolts torqued up to a certain pressure. This socket head turned out to be a bespoke item for the aircraft and this was their last remaining one available to the engineers, and ordering and obtaining replacements could take between 3 to 4 months.

Suddenly, I had a single “more” critical asset to add, and in case of loss or breakage, I had no replacements.

Consequently, you should ensure that you have “sliced n diced” your environment to ensure that you understand each data flow and all the assets that support it.

**Network Diagram**

*[Figure omitted]*

<!-- PDF p. 413 (book p. 392) -->

**Asset Management**

*[Figure omitted]*

Note network Diagrams and asset inventory can be easily created using the national Cyber security and Communications integration Center (nCCiC) Cyber security evaluation tool.[^13]

The InfoSec Institute[^14] describes assets as follows:

*In the realm of information security and information technology, an asset is anything of value to a business that is related to information services. These can take the form of a device, data or information, or even as people or software systems within the structure of a business. Anything that has value and supports the operation of a business can be considered an asset.*

[^13]: www.us-cert.gov/sites/default/files/FactSheets/NCCIC%20ICS_FactSheet_CSET_S508C.pdf
[^14]: https://resources.infosecinstitute.com/asset-management-guide-information-security-professionals/#gref

<!-- PDF p. 414 (book p. 393) -->

Note assets are not limited to information technology[^15] and can come in various guises.

*[Figure omitted]*

[^15]: www.nccoe.nist.gov/sites/default/files/library/sp1800/fs-itam-nist-sp1800-5-draft.pdf
