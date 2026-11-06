---
title: "Implement Strong Access Control Measures"
book: pci-dss-integrated-data-security-standard-guide
chapter: 2
source_pages: "73-78"
format: source-text
---
# Implement Strong Access Control Measures
(Source: PDF pp. 73-78)

<!-- PDF p. 73 (book p. 49) -->

If something is deemed to be of value either to your business or to your customers, it is essential that these assets are secured behind a lock and key *(whether physical or logical)*. The requirements for convenient access control measures have been around for far longer than you might imagine. In fact, the very first keyless (combination and rotation) locks were used in the year **1206 AD**.[^37] The higher the value of the asset, the greater the need for a robust access control system.

During my RAF Police Special Weapons protection duties, in the late 1980s, I was taught a very valuable phrase which remains current today:

Sir,

Please don’t confuse your rank with my authority!

Despite the fact that an RAF officer may have been a higher rank to myself, my job provided me with the authority of the Provost Marshal of the Royal Air Force Police in order that I was able to restrict access based upon strict Need to Know/Need to Access criteria. Consequently, if their details were not on the approved access list, they would be denied access to the Special Weapons facility. In PCI DSS, the same principle applies, with access to the cardholder data environment (CDE) needing to be strictly limited to approved personnel only and those with the formal approval having their access appropriately managed. This applies to both physical and logical CDEs.

The “Need to Know” principle is not a new term, having been applied during World War II and is referenced in the original NIST SP800-12 (*An Introduction to Computer Security: the NIST Handbook*)[^38] – first published in October 1995.

[^37]: https://prezi.com/oqwyu-nb9yym/the-history-of-combination-locks-and-rotations/
[^38]: https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-12.pdf

<!-- PDF p. 74 (book p. 50) -->

“the lan server operating system’s access controls provide extensive features for controlling access to files. these include group-oriented controls that allow teams of users to be assigned to named groups by the System administrator. Group members are then allowed access to sensitive files not accessible to nonmembers. each user can be assigned to several groups according to need to know.”

Having a secure network and systems is significantly undermined by poor access control facilities or poor access practices. Consequently, it is essential that the access control measures are appropriate to the sensitivity of the payment CDEs. For example, in a data center the systems risk has an aggravated value, and Privileged user accounts and user accounts that have authorized access into the CDE are a high priority target for criminals. Consequently, these accounts need to employ robust access controls applied to ensure that the Need to Know/Need to Access principles are applied.

Think of your access control measures as being like you lending your expensive car to your son/daughter and discovering that while you had loaned your car to them, the car had been stolen. The theft had occurred, as the result of your son/daughter been careless with the keys and had left the keys in the ignition of your car while they went into the Petrol/Gas station to pay for fuel, after having refueled the car. Your son/ daughter had not regarded this as being a high-risk act and it had been more convenient to them. However, being convenient to them also made it extremely convenient to the opportunist criminal, who happened to be walking by at the time.

The act of bypassing access controls is nothing new, with the term “*husbryce*” (House Breach)[^39] being used in Anglo-Saxon England. Consequently, it is a requirement that all authorized users be given individual access credentials, so that should an investigation be needed, you are able to identify the time, location, and person accessing the CDE.

In terms of physical access controls, the physical environment should be robust enough so as to ensure that access can only be gained through the official, recorded, access points. Remember that the integrity of a physical space is interdependent on each other.

[^39]: https://englishlegalhistory.wordpress.com/2013/05/30/history-of-burglary/

<!-- PDF p. 75 (book p. 51) -->

*[Figure omitted]*

When reviewing the effectiveness of your physical security measures, it is important to look at it from multiple dimensions. The attacker may not always look for opportunities via the main access/egress points and may look to exploit weaknesses in the ceiling or underfloor spaces or seek to exploit vulnerabilities in the fitting of the door/window frames, hinges, or locking mechanisms. More importantly, the integrity of your physical security measures is undermined by the “Human Firewall”:

- Propping open doors/windows
- Sharing access cards
- Tailgating
- The ability to clone telemetry access cards[^40]

If you are a business that has valuables or sensitive data assets that need to be physically protected, it is essential that the physical barriers to unauthorized access remain effective and that, in the event of an incident, you are able to identify who accessed the facility at the specified time. This can be achieved through an electronic automated access control system (EAACS), with personal identification number (PIN) to identify and validate the access to a particular person and/or the use of a manual lock

**Figure 2-16.** *Physical Security Perspectives*

[^40]: https://totalsecuritysummit.co.uk/industry-spotlight-secure-your-rfid-access-controls-against-card-cloning/

<!-- PDF p. 76 (book p. 52) -->

(or EAACS without PIN) and an appropriately sited closed circuit television (CCTV). The CCTV needs to meet the operational requirements[^41] needed to be able to identify the individual using the manual or EAACS to gain authorized access to the CDE.

Note of caution

When using CCtv, be careful that you are not capturing images of your customers’ cardholder data (ChD) and especially Sensitive authentication Data (SaD).

for example, in retail environments where CCtv is installed for crime reduction that overlooks the physical card reading device, can the ChD be identified/ recovered from the CCtv recording? if so, this may bring you into conflict with pCi DSS and also extend the “in-Scope” environment to include the CCtv monitoring and image storage.

However, it is worth remembering that this is the core of your onion (in-scope) and should be further enhanced by the application of additional outer rings of defense. This will help prevent an opportunist malicious actor from gaining unauthorized access through gaining entry to the facility in which the CDE resides.

Clearly, having created your secure citadels and strictly restricted the numbers of personnel that are granted access, you are going to have occasions where temporary visitor access needs to be allowed. PCI DSS does not prohibit temporary access, as long as their visits are easily identifiable, logged, and escorted at all times.

Technological advancements have not decreased the threat from physical security breaches and have, in fact, increased the threat. Where you have hardened your logical perimeter, preventing unauthorized access, attackers will pounce on any opportunity to circumvent your defenses through gaining physical access to your network and systems.

For instance, for not a great deal of money the attackers may build rogue devices to place on your network or may even purchase commercial products[^42] to help them bypass your defensive efforts. Additionally, the increased use of mobile technologies makes them increasingly valuable to opportunist thieves, where they are not looking at the data value but the resale value of the technology.

[^41]: https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/378443/28_09_CCTV_OR_Manual2835.pdf
[^42]: https://shop.hak5.org/collections/hak5-field-kits

<!-- PDF p. 77 (book p. 53) -->

Finally, in this onion ring, physical security measures need to be applied for the protection of media and pin transaction security (PTS) and point-of-sale (POS) devices.

Versions of the PCI DSS physical security and media protection controls can be seen through many different guidance documents, spanning many generations, to provide barriers and monitoring capabilities for malicious inbound and outbound movements.

*[Figure omitted]*

- **January 2001 – United States: Physical Security (FM 3-19.30)**[^43]
  - **“IDENTIFICATION SYSTEM**

*An ID system is established at each installation or facility to provide a method of identifying personnel. The system provides for personal recognition and the use of security ID cards or badges to aid in the control and movement of personnel activities.”*

**Figure 2-17.** *Physical Security*

[^43]: www.wbdg.org/FFC/ARMYCOE/FIELDMAN/fm31930.pdf

<!-- PDF p. 78 (book p. 54) -->

- **October 1995 – NIST SP800-12 (An Introduction to Computer Security: The NIST Handbook).**
  - **“14.5 Media Controls**

*Media controls include a variety of measures to provide physical and environmental protection and accountability for tapes, diskettes, printouts, and other media. From a security perspective, media controls should be designed to prevent the loss of confidentiality, integrity, or availability of information, including data or software, when stored outside the system. This can include storage of information before it is input to the system and after it is output.*

*The extent of media control depends upon many factors, including the type of data, the quantity of media, and the nature of the user environment. Physical and environmental protection is used to prevent unauthorized individuals from accessing the media. It also protects against such factors as heat, cold, or harmful magnetic fields. When necessary, logging the use of individual media (e.g., a tape cartridge) provides detailed accountability - to hold authorized people responsible for their actions.”*
