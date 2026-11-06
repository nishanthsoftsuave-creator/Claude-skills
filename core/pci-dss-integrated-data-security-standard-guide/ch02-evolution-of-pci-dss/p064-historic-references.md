---
title: "Historic References"
book: pci-dss-integrated-data-security-standard-guide
chapter: 2
source_pages: "64-73"
format: source-text
---
# Historic References
(Source: PDF pp. 64-73)

<!-- PDF p. 64 (book p. 40) -->

The original version of the PCI DSS controls framework was first released in December 2004.[^19] However, the source of some of the content are clearly evident before 2004.

[^19]: www.davidfroud.com/wp-content/uploads/2016/07/PCI-DSS-v1.0.pdf

## Build and Maintain a Secure Network

Your network infrastructure should be configured so as to prevent the misuse of unused Ports, Services, Protocols, and unchanged vendor default settings and to filter the network traffic between the untrusted and untrusted zones.

Each layered network interface (e.g., Internet connection, De-militarized zone (DMZ), and the internal network zones) requires a securely configured Firewall/Router to act as a “Gatekeeper” to help control the data flows.

You need only look at the structure of any medieval castle or a Cold War (1947– 1991) military weapons storage facility to see this concept successfully applied for the protection of valued, sensitive, or critical assets.

During my time as an RAF Police Dog handler (1989–1994), I patrolled numerous RAF bases that had exactly the same principles applied to produce a layered security architecture.

<!-- PDF p. 65 (book p. 41) -->

For example, at one high-risk establishment, there were a number of access/egress points around the perimeter of the base. However, these were strictly controlled and locked down, with the only entrance/egress being allowed through a permanently manned, main controlled access point.

Only authorized personnel were granted access to the facility, but this access did not provide them with automatic authorized access to the Cold War Special Weapons storage facility. This was a separate secure silo facility located within the confines of the main RAF base and which had its own security defenses and access control measures.

RAF Base: Perimeter

*[Figure omitted]*

Perimeter Access Control

*[Figure omitted]*

<!-- PDF p. 66 (book p. 42) -->

Cold War Special Weapons Site

*[Figure omitted]*

Additionally, a great deal of the content from requirement 1 regarding Firewall configurations can be seen in the very first NIST SP800-41 (*Guidelines on Firewalls and Firewall Policy*),[^20] which was published in January 2002 and superseded with version 1.0 in September 2009.

[^20]: https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-41.pdf

<!-- PDF p. 67 (book p. 43) -->

*[Figure omitted]*

**Figure 2-10.** *NIST SP800-41*

<!-- PDF p. 68 (book p. 44) -->

*[Figure omitted]*

The elements of requirement 2 can be seen within the Carnegie Mellon Software Engineering Institute’s “Securing Network Servers” report, published in April 2000.[^21]

**Figure 2-11.** *NIST SP800-41, r1*

[^21]: ftp://ftp.sei.cmu.edu/pub/documents/00.reports/pdf/sim010.pdf.

<!-- PDF p. 69 (book p. 45) -->

*[Figure omitted]*

## Protect Cardholder Data

As detailed in the SANS’s History of Encryption Paper,[^22] from January 2002, encryption is one of the oldest forms of science that has been carried out by the human race, and from Egyptian times to modern times, it concerns the desire to disguise, masquerade, or protect certain sensitive information from inquisitive eyes.

**Figure 2-12.** *“Securing Network Servers” Extract*

[^22]: www.giac.org/paper/gsec/1555/history-encryption/102877

<!-- PDF p. 70 (book p. 46) -->

Consequently, being that the objective of PCI DSS is to safeguard customer cardholder data, if you are storing or transmitting over public networks, it makes sense to ensure that it remains under lock and key.

*[Figure omitted]*

## Maintain a Vulnerability Management Program

Malware software has been an ever-present risk since 1971 with the Creeper and Reaper viruses,[^23] whereas the birth of the term Trojan horse spans back the successful use of a hidden payload in the first Trojan Horse during the siege of the City of Troy. NIST produced some comprehensive guidance, in November 2005, with the publication of their NIST Special Publication 800-83 (*Guide to Malware Incident Prevention and Handling*)[^24] and which was superseded with r1 in July 2013.[^25]

Since the late 1940s, the Royal Air Force Police have employed arms and explosives search (AES) dogs,[^26] as well as manual entry searches to help identify suspicious payloads. In 1970 *(in response to an increase in the incidence of hijackings during the late 1960s and early 1970s)*, the United States’ civilization aviation industry started using X-ray and metal detector machines[^27] to augment their use of search dogs and manual searches.

**Figure 2-13.** *Encrypted Storage and Transmission*

[^23]: https://pandorafms.com/blog/creeper-and-reaper/
[^24]: https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-83.pdf
[^25]: https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-83r1.pdf
[^26]: www.k9history.com/uk-royal-air-force-police-dog-history.htm
[^27]: www.nap.edu/read/5116/chapter/3

<!-- PDF p. 71 (book p. 47) -->

The need to apply regular updates can be seen in the NIST Special Publication 800-40 (*Procedures for Handling Security Patches*),[^28] which was first published in August 2002 and which has been subsequently superseded with the latest revision (R3, *Guide to Enterprise Patch Management Technologies*[^29]).

*[Figure omitted]*

The Open Web Application Security Project (a.k.a. OWASP) was established in 2001[^30] in response to an increasing number of data breaches being attributed to vulnerabilities created through insecure software development practices (e.g., SQL injection attacks

**Figure 2-14.** *NIST SP800-40 Extract*

[^28]: https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-40.pdf
[^29]: https://csrc.nist.gov/publications/detail/sp/800-40/rev-3/final
[^30]: www.owasp.org/index.php/History_of_OWASP

<!-- PDF p. 72 (book p. 48) -->

in 1998[^31]). As a result, OWASP began to develop top 10 lists of the most critical web application security risks[^32] and supporting guidance/mitigation advice.

Mitigating the risks associated with poor software development practices continues to be the cause of a high volume of web site compromises and data breaches. Consequently, both the Payment Card Industry Security Standards Council (PCI SSC)[^33] and NIST[^34] have produced supporting guidance/standards.

**Figure 2-15.** *Comparison of 2003, 2004, 2007, 2010, and 2013 Releases*

[^31]: www.esecurityplanet.com/network-security/how-was-sql-injection-discovered.html
[^32]: www.owasp.org/images/7/72/OWASP_Top_10-2017_%28en%29.pdf.pdf
[^33]: www.pcisecuritystandards.org/documents/PCI-Secure-Software-Standard-v1_0.pdf?agre ement=true&time=1576693614480
[^34]: https://csrc.nist.gov/CSRC/media/Publications/white-paper/2019/06/07/mitigating-risk-of-software-vulnerabilities-with-ssdf/draft/documents/ssdf-for-mitigating-risk-of-software-vulns-draft.pdf

<!-- PDF p. 73 (book p. 49) -->

Despite Injection[^35] attacks remaining at the very top of the OWASP top 10 risks *(since 2010)*, the Magecart Hacking Group[^36] continues to be extremely successful at leveraging this style of attack against e-Commerce businesses.

[^35]: www.owasp.org/index.php/Top_10-2017_A1-Injection
[^36]: https://threatpost.com/magecart-infestations-saturate-web/148911/
