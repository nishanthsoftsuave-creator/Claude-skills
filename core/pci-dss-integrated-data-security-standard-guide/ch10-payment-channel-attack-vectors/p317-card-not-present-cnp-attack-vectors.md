---
title: "Card Not Present (CNP) Attack Vectors"
book: pci-dss-integrated-data-security-standard-guide
chapter: 10
source_pages: "317-328"
format: source-text
---
# Card Not Present (CNP) Attack Vectors
(Source: PDF pp. 317-328)

<!-- PDF p. 317 (book p. 295) -->

The increased use of online digital shopping has provided significant consumer convenience, with purchases being able to be made with a simple click (or swipe) on their Internet-connected devices.

As much as the Internet-connected digital advances has distanced the consumer from the shop, the criminal has been distanced from the victim. Consequently, attackers increasingly regard CNP attacks as being victimless crimes, with no apparent regard for the consequences of their actions.

<!-- PDF p. 318 (book p. 296) -->

This is well-known psychological consequence of using the Internet and can be demonstrated in the “Trolley/Train/Tram Experiment”:[^21]

- **Scenario 1**

A runaway Trolley/Train/Tram is hurtling down the tracks, directly toward the path of five railways workers. You have to make the decision whether to pull an adjacent switch or divert the runaway along another track. However, on the diverted route, there is a lone worker who will be killed.

- Do you pull the switch to divert the runaway?
  - *Sacrifice* **1** *to save* **5***.*
- **Scenario 2**

A runaway Trolley/Train/Tram is hurtling down the tracks, directly toward five rail workers. You have to make the decision whether to push a single person from a bridge (to their certain death) into the path of the runaway to derail it and save the lives of five rail workers.

- Do you push the person into the path of the runaway?
  - *Sacrifice* **1** *to save* **5**.

**Table 10-2.** *The Runaway Trolley Conundrum*

Scenario 1[^22] Scenario 2[^23]

*[Figure omitted]*

*[Figure omitted]*

[^21]: https://towardsdatascience.com/trolley-problem-isnt-theoretical-2fa92be4b050
[^22]: https://images.app.goo.gl/XtdRY8Ponz4ZWBf49
[^23]: https://images.app.goo.gl/75tkS3uTBkPy46ye6

<!-- PDF p. 319 (book p. 297) -->

This distancing effect, provided by the Internet, presents significantly differing attacking intent, ranging from the amateur hacker to the state-sponsored and organized criminal groups. The amateur (have a go) hackers may have distanced themselves from the potential damage they are having on their victim and, as such, may not be attacking you for financial gain. However, their actions could inadvertently provide opportunities for criminals to profit from, for example, making stolen data available on the dark Web or bragging about the vulnerabilities that they have found within your corporate network or web applications.

Traditionally, attackers would seek to exploit vulnerabilities in the network infrastructures. However, the changing face of web-based business means that increasingly the Web and email have become alternative avenues of attack.

An attacker is only limited by their imagination and the types of attack are continually enhanced and changed. Therefore, the following are a representation of some of the types of attacks, and it is essential that you maintain an understanding of the attacker’s tactics, techniques, and protocols (TTPs) using some of the available resources:

- Security Threat Intelligence Services[^24]
- Mitre Att&ck[^25]
- US-CERT CISA[^26]
- Exploit.db[^27]

[^24]: www.gartner.com/reviews/market/security-threat-intelligence-services
[^25]: https://attack.mitre.org/
[^26]: www.us-cert.gov/
[^27]: www.exploit-db.com/

## “Payload” Delivery Attacks

If a criminal is unable to gain unauthorized access to a corporate network via traditional methods, they will seek other approaches. One such way is through the exploitation of human nature, where they are able to use the data freely available on social media to craft emails, containing malicious payloads, which entice the recipients to read and download the email.

<!-- PDF p. 320 (book p. 298) -->

The development of malicious emails is becoming increasingly difficult to identify, as criminals are developing increasingly well-crafted and sophisticated emails. No longer are they the traditional, poorly written emails relating to your lately departed long lost Uncle.

*[Figure omitted]*

Among the known Spear Phishing-style tactics, the most common are

- **Spear Phishing Attachment**

The use of malware attached to an email. In this scenario, adversaries attach a file to the spear phishing email and normally rely upon End User Execution to gain execution.

<!-- PDF p. 321 (book p. 299) -->

- **Spear Phishing Link**

The use of links to download malware contained in email, instead of attaching malicious files to the email itself, to avoid defenses that may inspect email attachments

- **Spear Phishing via Service**

The use of third-party services rather than directly via enterprise email channels. The attacker builds rapport with a target via social media, then sends content to a personal webmail service that the target uses on their work computer.

- This allows an adversary to bypass some email restrictions on the work account, and the target is more likely to open the file since it’s something they were expecting.
- If the payload doesn’t work as expected, the adversary can continue normal communications and troubleshoot with the target on how to get it working.

Unfortunately, employees and consumers fail to recognize the importance the criminals place on carrying out “hostile reconnaissance” on their targets, and as a result, people can be far too complacent with the type of data they make freely available to their enemies:

### Social Media Intelligence Gathering Tools

#### Facebook

- Facebook scanner
- Socmint
- Lookup ID
- FindMyFbid
- Facebook JSON Search
- LikeAlyzer
- Face Live
- Who posted what?
- ExtractFace

<!-- PDF p. 322 (book p. 300) -->

#### Twitter

- Twitter search home
- Twitter advanced search page
- Twitter Deck
- All My Tweets
- Trendsmap
- Foller
- First Tweet
- Social bearing
- Twicsy
- Follower wonk
- Sleeping Time
- Simple Twitter Profile Analyzer (Python script)
- Tag board
- Tinfoleak
- Spoonbill
- Export Tweet

#### LinkedIn

- Searching LinkedIn using Google custom search
- Recently Updated Profiles
- LinkedIn Contact Extractor
- LinkedIn Résumés
- LinkedIn People Finder (International)

<!-- PDF p. 323 (book p. 301) -->

#### Instagram

- Iconosquare
- Picodash
- ToFo

#### Reddit

- Mostly Harmless
- redditarchive
- Reddit Enhancement Suite
- Reddit investigator
- Reddit metrics
- atomiks
- SnoopSnoo
- Reddit Comment Search

Any of these resources can be used to create an air of enhanced credibility for a malicious email, which have been designed to create an urgency or desire to access the contents of the email. These are the attackers’ opportunity to create a remote access point or deliver malicious software, all to undermine or bypass the existing defensive measures. These tactics are nothing new, when during the siege of the City of Troy the Greek commander Odysseus is believed to have conceived the very first “Trojan Horse”[^28] style of attack.

Following 10 years of unsuccessful attempts to breach the City of Troy’s defenses, the Greek Army left an attractive wooden horse as a gift to the residents of Troy. Once the “gift” had been wheeled through to the heart of the city, the gift remained dormant until the quiet of the night when it delivered its clandestine payload – the enemy!

[^28]: www.nationalgeographic.org/thisday/apr24/fall-troy/

<!-- PDF p. 324 (book p. 302) -->

A fresh Greek Army then attacked from within and were able to undermine the defenses, allowing additional unauthorized access for further armies to attack.

Once inside a target user’s email inbox, the attacker has access to a wealth of data *(through numerous messages, application account resets, etc.)*, which proves to be a valuable resource for further reconnaissance, data harvesting, and attack planning.

## CNP Perimeter Attacks

The very nature of CNP business operations requires your organization to make a public interface available, so as to enable your consumers to buy goods or services from you. However, by making this interface available to your customers, you are also making it available to your attackers.

As well as attempting to circumvent the existing security defenses, through the exploitation of your user’s weaknesses, the attackers will seek to identify potential infiltration opportunities that are presented by poorly managed or configured external/ public-facing network infrastructures. Consequently, your attackers will start by carrying out extensive reconnaissance of your perimeter. The attacker’s reconnaissance will target the supporting network layer, as well as the web application interface.

## Perimeter Network Attacks

The easiest gateway into your supporting network infrastructure is via unused/insecure Services,[^29] Protocols,[^30] or Ports[^31] *(easily identified through a simple scan)* or poorly configured firewall/router ruleset filtering *(allowing uncontrolled traffic flows)*. Other perimeter-style attacks include External Remote Services.

- **External Remote Services**

Exploiting external remote services (e.g., VPN, Citrix, etc.) to gain initial access and/or persist within a network

[^29]: www.owasp.org/index.php/Top_10_2014-I3_Insecure_Network_Services
[^30]: www.newnettechnologies.com/downloads/NNT-Open-Port-Hardening-Guide.pdf
[^31]: www.speedguide.net/ports.php?filter=risk

<!-- PDF p. 325 (book p. 303) -->

- Access to Valid Accounts to use the service is often a requirement, which could be obtained through credential pharming or by obtaining the credentials from users after compromising the enterprise network.
- Access to remote services may be used as part of Redundant Access during an operation.
- For example, Pwned[^32] accounts
- **Hardware Additions**

Attackers gaining physical access to an environment can introduce computer accessories, computers, or networking hardware into a system or network that can be used as a vector to gain access.

- Numerous commercial and open source products[^33] are readily available that provide various functionalities, for example:
  - Passive network tapping
  - Man-in-the middle encryption breaking
  - Keystroke injection
  - Kernel memory reading via DMA
  - Wireless access points
- Replication Through Removable Media

Attackers may utilize disconnected or air-gapped networks, using malware copied to removable media and taking advantage of Autorun features to gain unauthorized access to systems.

- When the media is inserted into a system and executes
  - In the case of Lateral Movement, this may occur through modification of executable files stored on removable media or by copying malware and renaming it to look like a legitimate file to trick users into executing it on a separate system.

[^32]: https://haveibeenpwned.com/
[^33]: https://shop.hak5.org/

<!-- PDF p. 326 (book p. 304) -->

- In the case of Initial Access, this may occur through manual manipulation of the media, modification of systems used to initially format the media, or modification to the media’s firmware itself.
- **Valid Accounts**

Attackers steal the credentials of a specific user or service account using Credential Access techniques or capture credentials earlier in their reconnaissance process through social engineering for means of gaining Initial Access.

- Accounts that an adversary may use can fall into three categories:
  - **Default**

Default accounts are those that are built into an OS such as Guest or Administrator account on Windows systems or default factory/provider set accounts on other types of systems, software, or devices.

- Default accounts are also not limited to Guest and Administrator on client machines; they also include accounts that are preset for equipment such as network devices and computer applications whether they are internal, open source, or COTS.
  - Appliances that come preset with a username and password combination pose a serious threat to organizations that do not change it post installation, as they are easy targets for an adversary.
- **Local**

Local accounts are those configured by an organization for use by users, remote support, services, or for administration on a single system or service.

- **Domain accounts**

Domain accounts are those managed by Active Directory Domain Services where access and permissions are configured across systems and services that are part of that domain. Domain accounts can cover users, administrators, and services.

<!-- PDF p. 327 (book p. 305) -->

Compromised credentials may be used to bypass access controls placed on various resources on systems within the network and may even be used for persistent access to remote systems and externally available services, such as VPNs, Outlook Web Access, and remote desktop. Compromised credentials may also grant an adversary increased privilege to specific systems or access to restricted areas of the network.

- Attackers may choose not to use malware or tools in conjunction with the legitimate access those credentials provide to make it harder to detect their presence.

## Perimeter Web Attacks

Historically, web interfaces were developed for the presentation of information. However, the world of web-based business has changed significantly over the past 15 years, and now the Web has become far more consumer interactive. As a result, web-based attacks have become a preferred choice for the attackers seeking alternative options to gain unauthorized access to data and the supporting network infrastructures. Such tactics include

- **Drive by compromises**

An attacker gains access to a system through a user visiting a web site over the normal course of browsing. In this style of attack, the user’s web browser is typically targeted for exploitation, but attackers may also use compromised web sites for non-exploitation behavior, for example:

- Acquiring application access tokens

Multiple ways of delivering exploit code to a browser exist, including

- A legitimate web site is compromised where attackers have injected some form of malicious code, for example:
  - JavaScript
  - iFrames
  - Cross-site scripting

<!-- PDF p. 328 (book p. 306) -->

- Using malicious paid-for advertising provides built-in web application interfaces, which are used to insert any other kind of object, and that can be used to display web content or contain a script that executes on the visiting client, for example:
  - Forum posts
  - Comments
  - Other user controllable web content

Typically, the attackers’ web sites are targeted against a specific community, where the goal is to compromise a specific user or set of users based on a shared interest.

- A strategic web compromise
- Watering hole attack
- Exploit Public-Facing Applications

An attacker uses software, data, or commands to take advantage of a vulnerability in an Internet-facing computer system or program in order to cause unintended or unanticipated behavior, for example:

- Coding bugs
- Coding glitches
- Design vulnerabilities

These applications are often web sites, but can include databases and any other applications with Internet accessible open sockets (e.g., Web servers and related services).
