---
title: "Secure Architecture (Build and Maintain a Secure Network)"
book: pci-dss-integrated-data-security-standard-guide
chapter: 9
source_pages: "267-273"
format: source-text
---
# Secure Architecture (Build and Maintain a Secure Network)
(Source: PDF pp. 267-273)

<!-- PDF p. 267 (book p. 245) -->

Having aligned your payment channels to the applicable controls, now is the time to visualize and harden the supporting IT systems which support the CHD life cycles from the point of origin, right through to the secure disposal/destruction (after the legitimacy for retention has ended).

By the very nature, IT systems (Servers, Databases, Switches, Routers, Firewalls, etc.) are supplied in an insecure state.

Therefore, these systems need to be linked together and locked down to ensure that they are secured (eliminating any unnecessary functionality) and to prevent unauthorized network traffic being able to pass between the network zones.

In the event that your network gets breached, a layered and secure architecture will help apply the 5 Ds of Defense:

- **Deter**
- **Detect**
- **Delay**
- **Deny**
- **Defend**

<!-- PDF p. 268 (book p. 246) -->

## Layered Defenses

*[Figure omitted]*

*[Figure omitted]*

*[Text inside a figure could not be extracted]*

*[Figure omitted]*

Although PCI DSS does not prohibit the use of “Flat Networks,” the very fact that PCI DSS applies to any systems that process, store, or transmit CHD (or any systems that could impact these systems) makes achieving PCI DSS considerably more difficult.

The concept of layered defenses has been seen to be extremely effective for the physical defenses to control who was permitted to go where, and this can be seen being successfully applied in castle structures, as well as in modern military defenses.

Given today’s threats to cardholder data, the benefits of a layered architecture have proven itself for centuries. However, in today’s data technology environments, there is a need to be mindful of rogue devices providing alternative access routes – rather than a direct attack through the main entrances (firewalls).

**Figure 9-10.** *Secure Architecture121314*

[^12]: www.twcenter.net/forums/showthread.php?575311-The-Dukedom-of-York-York-Castle-York
[^13]: www.pontefractheritagegroup.org.uk/page2.html
[^14]: www.bbc.co.uk/news/world-19635544#panel7

<!-- PDF p. 269 (book p. 247) -->

## Identify and Manage IT Assets

*[Figure omitted]*

**Figure 9-11.** *Seven-Layer OSI Model*

Having identified all the people involved in supporting the payment channels, the next crucial step is to accurately identify and manage the IT assets involved in the processing, transmission, and storage of the consumers’ CHD.

All the identified IT assets, across the entirety of the Open System Interconnection (OSI) seven-layer network reference model,[^15] need to be securely configured to ensure that any attacks are unable to circumvent the protective measure applied at the software layers through the manipulation of the hardware layers.

[^15]: www.w3schools.in/cyber-security/osi-security-layers-and-their-significance/

<!-- PDF p. 270 (book p. 248) -->

## Traffic Control

**Traffic Filtering (Between Untrusted and Trusted Zones)**

*[Figure omitted]*

*[Figure omitted]*

**Figure 9-12.** *World War II Internal Access Control*

**Figure 9-13.** *TSA Security Checkpoint*

We all know that the safest and most secure business operations are those that are permanently locked and which prohibit any access. Unfortunately, this model does not work in the PCI DSS environments as businesses are heavily reliant on the processing and storage of CHD. Consequently, the traffic needs to be strictly controlled – checking the authority for all network traffic ingress/egress. In the physical environment, this is established by the issuance of access cards/fob/keys (based upon their role) or access control lists:

“If your name is not down, you’re not coming in!”

An example would be to ensure that your firewalls and routers have their rulesets configured to implicitly deny, so as to prevent any traffic that is not specifically recognized from passing between your untrusted and your trusted network environments.

<!-- PDF p. 271 (book p. 249) -->

Just having the rights to enter an environment should not automatically elevate their rights to transit anywhere. Traffic flow access needs to be filtered based upon legitimate access needs.

For example, when travelling, the purchase of a “Boarding Card” does not allow you uncontrolled access to anywhere within the airport architecture. The same should be applied to networks supporting payment channels.

## Reality Bites

Every military establishment applies these principles. For example, Camp Bastion was the size of the UK city of Reading (approximately 61 km²) and employed multiple internally segmented (trusted) areas, where access was strictly limited based upon legitimate needs to access, with an external perimeter access control (external firewall) where all access was subject to explicit checks, before transiting through the 1.5 km long De-militarized zone (DMZ).

After transiting through the DMZ, the traffic was then faced with more security checks, searches, validation, and approval (at the inner access control) before being granted access to the inner sanctum. However, it did not stop there, as further access restrictions were applied to the more sensitive inner sanctums.

During a 6-month CIFT deployment, my team encountered over 550 reportable security incidents that were identified through the monitoring of these points of access/egress.

## Secure by Design/Secured by Default

Network assets are sold in an open (unlocked) and vulnerable state, as they are designed to be functional. It is essential that all unnecessary settings are disabled so that only essential settings are enabled for the specific service they are providing.

This includes changing default passwords, closing unnecessary ports/protocols, disabling insecure settings, and disabling all surplus services.

<!-- PDF p. 272 (book p. 250) -->

## Reality Bites

During my role as a station CI operative, I was responsible for the management of an extensive library of physical security cabinets. The purpose of these security containers was to provide secure storage facilities for highly sensitive hardcopy data and media, with locking mechanisms that enabled the restriction of access to only authorized personnel, and their use was strictly restricted for the sole purpose of the secure storage of this media and it was prohibited for using these containers to support additional purposes *(e.g., Storing valuable and attractive items or cash)*. These security containers were provided with either Manifoil combination locks (MCL) or Mersey-style locking mechanisms.

*[Figure omitted]*

For ease of use, newly issued security containers were set to the manufacturer’s setting and, when being stored, need to be set to a unique setting that was only to be known by CI personnel.

When being stored or issued out for use, it may be more convenient to leave the setting on the manufacturer’s combination. However, this makes the setting susceptible to compromise or misuse *(The same applies to any assets supporting the payment card operations)*. Additionally, on return from use, it is important that the security combinations are reset to the establishment’s unique setting or returned to manufacturer’s setting before reuse or disposal.

**Figure 9-14.** *Sy Container and MCL and Mersey-Style Locks*

<!-- PDF p. 273 (book p. 251) -->

After recently taking over the responsibilities, I was carrying out a review of my inventory of security containers, only to discover that the previous incumbent had failed to effectively manage the return of these assets. I discovered that approximately half a dozen of these security containers had been secured, without being reset to the unique configuration setting. As a consequence, I was unable to gain authorized access to confirm that these were empty or to reissue them for use and needed to procure the services of a locksmith to brute force access *(rendering the assets as scrap)* to ensure that no sensitive data/media remained within.

Another recent example is the online dating site “Heyyo” was breached[^16] after they left their Elasticsearch server without any password protections (the default setting). This led to the leaking of the private information (e.g., messages, photos, sexual preferences, occupations, etc.) of over 70,000 registered users worldwide. Such a vulnerability may not be discovered as part of your quarterly vulnerability scans and should be addressed as part of the implementation, ensuring that all assets are benchmarked against industry security configuration standards *(e.g., CIS Benchmarks*[^17]*)*.

I would highly recommend incorporating security configuration checks into your vulnerability management practices using (where possible) automated tools *(e.g., Titania Nipper*[^18]*/PAWS,*[^19] *CIS CAT,*[^20] *etc.)*.

[^16]: www.forbes.com/sites/nicolemartin1/2019/09/27/another-dating-app-has-leaked-users-data/#501853c67da6
[^17]: www.cisecurity.org/cis-hardened-image-list/
[^18]: www.titania.com/products/nipper/?utm_term=titania%20 nipper&utm_source=adwords&utm_campaign=titania+brand+ppc&utm_medium=ppc&hsa_acc=2787898520&hsa_tgt=kwd-782740145036&hsa_ver=3&hsa_grp=76079675036&hsa_ad=361430641582&hsa_src=g&hsa_kw=titania%20 nipper&hsa_mt=e&hsa_cam=2058213049&hsa_net=adwords&gclid=cj0kcqiasbrxbrdparisaa nnz_odpq3zxxotchilexggv77l_s0dfa5u9q2cqcfujk-yk1kpsuznygoaaoooealw_wcb
[^19]: www.titania.com/products/paws/
[^20]: https://learn.cisecurity.org/cis-cat-lite
