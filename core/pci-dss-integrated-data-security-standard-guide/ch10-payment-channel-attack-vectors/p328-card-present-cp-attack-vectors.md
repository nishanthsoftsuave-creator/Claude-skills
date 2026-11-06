---
title: "Card Present (CP) Attack Vectors"
book: pci-dss-integrated-data-security-standard-guide
chapter: 10
source_pages: "328-334"
format: source-text
---
# Card Present (CP) Attack Vectors
(Source: PDF pp. 328-334)

<!-- PDF p. 328 (book p. 306) -->

As per the title “Card Present,” this involves payments being made while the cardholder owner is present at the time of the purchase and where they provide their own payment card using a Point-Of-Interaction (POI)/PIN Transaction Security (PTS)/Point-Of-Sale (POS)/Pretty Damn Quick (PDQ) device or using a payment card as a method of authentication, in order to withdraw funds from a “Hole in the Wall” (ATM).

<!-- PDF p. 329 (book p. 307) -->

POI/PTS/POS/PDQ Device ATM

*[Figure omitted]*

*[Figure omitted]*

Usually, this would be a store (e.g., Shop, Gas/Fuel Station, Supermarket, Bar/Public House, Restaurant, Sports Stadium, Hotel, etc.) or an ATM provided in convenient locations for the consumer, typically in public areas (e.g., Shopping Malls/Centers, High Street, Local Bank, etc.). Frequently, the importance of these devices is often misunderstood and underappreciated. However, this is not the case for the criminals who have understood that these are extremely valuable targets, being that they are hardware, software, and even network-connected devices. As a result, this significantly increases their attack options based upon their specific objectives. For instance, consider the reasons to attack an ATM. These are not always just brute force attacks[^34] from your traditional criminals but are also the target of cyber criminals,[^35] where they seek to exploit more system/software vulnerabilities for financial gain or to gain unauthorized access to the supporting Local Area Network (LAN), thus enabling the ability for lateral movement.

There has been a significant increase of attacks on these types of devices.

[^34]: www.finextra.com/newsarticle/34886/abn-amro-shuts-down-half-of-its-atm-estate-in-response-to-escalating-violence
[^35]: www.upguard.com/blog/biggest-threat-to-atm-security-is-misconfiguration

<!-- PDF p. 330 (book p. 308) -->

*[Figure omitted]*

## ATM Attacks

Being that ATMs need to be available for the convenience of consumers’ access, they are made available for public access. This free access makes them an increasingly viable target for criminals. If the criminals can get access to the terminal or supporting network infrastructure, they are seen as being an easy target.

Consequently, most banks have transferred this increasing risk and have outsourced the provision of an ATM service for their consumers. However, this does not transfer all of their compliance obligations, as they need to fulfill their third-party management obligations while ensuring that the physical security of the terminal is maintained and periodic checks are carried out.

Here are some examples of the types of ATM attacks, which need to have appropriate risk mitigation controls applied:

- **Brute Force**

This is the most basic of attacks, where the criminals physically attack the surround physical infrastructure to gain unauthorized physical access (e.g., Ram Raid[^37] or ATM Burglary[^38]) to the

**Figure 10-3.** *European Payment Terminal Crime Report*[^36]

[^36]: www.association-secure-transactions.eu/east-publishes-european-fraud-update-1-2019/
[^37]: www.thisismoney.co.uk/money/news/article-7244023/How-surge-ram-raids-ATMs-fuelling-race-axe-cash.html
[^38]: www.wired.com/2017/04/hackers-emptying-atms-drill-15-worth-gear/

<!-- PDF p. 331 (book p. 309) -->

terminal. Remembering that an ATM is an IT system attached to a cash vault, the target of this style of attack is the cash vault and with the attached IT system becoming the collateral damage for the attack. Post attack, it is essential that the IT system, in-scope for PCI DSS, has not had its integrity compromised.

- **Physical Skimming**[^39]

Freely available on the Dark Web, criminals can purchase Physical Skimming devices that are simply attached to the ATM. The purpose of such devices is to illegally harvest the consumers’ payment card data.

*[Figure omitted]*

**Figure 10-4.** *Ten ATM Skimming Overlay Devices*[^40]

[^39]: https://krebsonsecurity.com/tag/atm-skimmers/
[^40]: https://blog.acolyer.org/2018/09/03/fear-the-reaper-characterization-and-fast-detection-of-card-skimmers/

<!-- PDF p. 332 (book p. 310) -->

- **Malware attacks**[^41]

The ATM attack vectors are a good example where PCI DSS can support “Out-of-Scope” considerations. If you look at the “Jackpotting”[^42] attack, the criminals are not seeking to steal payment card data but to introduce malware to the ATM *(in essence, a computer-connected electronic cash vault)* to illegally withdraw cash from consumer bank accounts.

- **Network attacks**[^43]

Increasingly we are seeing cases where the cyber-attacks have used vulnerabilities in the network-connected ATMs to enable cyber hackers (e.g., APT-37, The Lazarus Group[^44]) to gain unauthorized access to the supporting corporate network for their financial gain.

[^41]: www.association-secure-transactions.eu/tag/atm-malware/
[^42]: www.paymentscardsandmobile.com/threat-actors-demonstrate-persistent-interest-in-atm-malware/
[^43]: www.wired.com/story/north-korean-hacker-group-apt37/
[^44]: https://attack.mitre.org/groups/G0032/

## POI/PTS/POS/PDQ Device Attacks

The styles of attacks[^45] that are carried out against POI devices are very similar to the ATM-style attacks (e.g., Physical Skimming,[^46] Malware,[^47] Network,[^48] etc.). However, unlike the ATM-style attacks, POI devices produce ancillary paper media which contain payment card data (full or partial) – Receipts, which are valuable to the criminals (as they seek to piece together their jigsaw puzzles), and being portable devices, they are easier to be tampered with or exchanged for bogus skimming devices.

[^45]: www.blackhat.com/docs/us-16/materials/us-16-Valtman-Breaking-Payment-Points-of-Interaction.pdf
[^46]: www.pcisecuritystandards.org/documents/Skimming%20Prevention%20BP%20for%20 Merchants%20Sept2014.pdf
[^47]: https://krebsonsecurity.com/2014/07/sandwich-chain-jimmy-johns-investigating-breach-claims/
[^48]: https://rambleed.com/

<!-- PDF p. 333 (book p. 311) -->

Consequently, the hardware devices need to be subject to periodic integrity checks against an asset inventory and hardware life-cycle management,[^49] and all receipts securely managed to ensure the integrity of the POIs.

[^49]: www.pcisecuritystandards.org/assessors_and_solutions/pin_transaction_devices

### Associated Problems

Unfortunately, there can be conflicts between PCI DSS and the business objectives to support the maintenance of good customer service and crime reduction. Frequently, the POI environments will be subject to Closed Circuit Television (CCTV) surveillance in support of customer compliant investigations and in support of crime reduction efforts.

If you are using CCTV, you will be wanting to ensure that the imagery is clear enough to identify individuals, as per the goal of having CCTV monitoring. However, if the recordings overlook the POI devices, you may be recording the Payment Card details and Personal Identification Number (PIN) (a.k.a. Sensitive Authentication Data (SAD)), as the payments are being made.

Remember

- pCI Dss applies to any storage, transmission, or processing of cardholder data.
- the storage of saD is prohibited under pCI Dss.

Consequently, the digital recordings could be a valuable target for the criminals, and the storage systems (and any connected systems) would become part of your PCI DSS scope.

### Ongoing Research

Researchers, such as the Computer Laboratory, University of Cambridge, UK, are continually identifying vulnerabilities[^50] and innovative ways to exploit POI devices:[^51]

- **EMV PIN verification “wedge” vulnerability**

[^50]: www.cl.cam.ac.uk/research/security/banking/ped/
[^51]: www.cl.cam.ac.uk/~osc22/docs/preplay_oakland14.pdf

<!-- PDF p. 334 (book p. 312) -->

*[Figure omitted]*

- **Chip Authentication Program (CAP) vulnerabilities**
- **PIN Entry Device (PED) vulnerabilities**
- **Chip and PIN (EMV) relay attacks**
- **Tamper resistance of Chip and PIN (EMV) terminals**
- **Chip and PIN (EMV) Interceptor**

This shows the risks associated with these devices and the importance of safeguarding these devices from opportunist criminals. Consequently, it is essential that you maintain an inventory of your physical POS/PTS assets *(as well as all your other assets that support your payment processes)* and ensure that you periodically review your asset inventories and ensure that their end-of-life(EoL)/end-of-support (EoS) dates are recorded within the inventory. For PTS devices, you should consult the PCI SSC’s web site.[^53]

**Figure 10-5.** *Cambridge University Research*[^52]

[^52]: www.cl.cam.ac.uk/research/security/banking/
[^53]: www.pcisecuritystandards.org/assessors_and_solutions/pin_transaction_devices
