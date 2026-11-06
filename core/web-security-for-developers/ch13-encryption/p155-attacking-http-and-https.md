---
id: WS-C13-004
title: Attacking HTTP (and HTTPS)
source_pages: "155-156"
chapter: 13
concepts: [man-in-the-middle, vpnfilter, downgrade-attack, rogue-wifi-hotspot, isp-ad-injection, nsa, certificate-abuse, wireless-routers]
related: [WS-C13-003, WS-C13-005, WS-C02-005]
time_sensitive: true
---
# Attacking HTTP (and HTTPS)
(Source: PDF pp. 155-156, tail PDF p. 157. The section begins at its heading near the bottom of PDF p. 155; the text above it belongs to WS-C13-003. The tail is the "Government Agencies" subsection at the top of PDF p. 157, above the "Summary" heading, which begins WS-C13-005.)

## What the section covers
What can go wrong if a site does not use HTTPS, shown through real examples of man-in-the-middle attacks by hackers, internet service providers and governments (PDF pp. 155-157).

## Meaning
Weakly encrypted or unencrypted internet communication lets an attacker mount a man-in-the-middle attack, tampering with or snooping on the HTTP conversation. The book answers the question "what is the worst that can happen without HTTPS?" with the examples below (PDF p. 155).

## How it works: examples
### Wireless routers (PDF p. 156)
- Routers are a common target. Most contain a bare-bones Linux installation that routes traffic to the ISP and hosts a simple configuration interface. That Linux is typically never patched, and the same version runs in many thousands of homes, which makes it attractive to hackers (PDF p. 156).
- In May 2018 Cisco security researchers found that over half a million Linksys and Netgear routers were infected with malware called VPNFilter. It snooped on HTTP traffic passing through the router and stole website passwords and other sensitive data for an unknown attacker thought to be linked to the Russian government (PDF p. 156).
- VPNFilter also tried downgrade attacks: interfering with the initial TLS handshake to popular sites so the browser would choose weaker encryption or none (PDF p. 156).
- Sites using HTTPS would have been immune, because HTTPS traffic can be read only by the recipient site. Traffic to other sites was likely stolen and mined for sensitive data (PDF p. 156).

### Wi-Fi hotspots (PDF p. 156)
- A low-tech attack is setting up a rogue Wi-Fi hotspot in a public place such as a cafe or hotel lobby. People rarely check hotspot names, so unwary users connect (PDF p. 156).
- Their TCP traffic flows through the attacker's device, which records it to disk and searches it for credit card numbers and passwords. The only sign to victims is when the attacker leaves and shuts the hotspot down. Encrypting traffic defeats this, since captured traffic cannot be read (PDF p. 156).

### Internet service providers (PDF p. 156, tail PDF p. 157)
- ISPs sit in a position of enormous trust, yet some tamper with traffic. Comcast, one of the largest US ISPs, injected JavaScript advertisements into HTTP traffic for many years (PDF p. 156).
- Comcast said it was a service, since many of the ads told users how much of their monthly data plan they had used. Digital rights campaigners likened it to a mail carrier slipping advertising into sealed letters (PDF p. 156).
- HTTPS sites are immune to this tampering because request and response contents are opaque to the ISP (PDF p. 157).

### Government agencies (PDF p. 157)
- The book says plenty of evidence shows governments snoop on traffic. The US National Security Agency (NSA) has carried out man-in-the-middle attacks for surveillance (PDF p. 157).
- A leaked internal presentation from former NSA contractor Edward Snowden described the spying on Brazil's state-run oil company Petrobras: the NSA obtained digital certificates for Google websites and hosted look-alike sites that harvested user credentials while proxying traffic to Google (PDF p. 157).
- How widespread such programs are is unknown. (The author closes with an ironic aside that is not a substantive claim.) INTERPRETATION: this example is an attack on HTTPS itself, through certificates, which may be why the section title includes "(and HTTPS)".

## Why it matters
The book states that HTTPS defeats the router, hotspot and ISP examples because the traffic is unreadable to anyone but the site (PDF pp. 156-157). In the government example, by contrast, the NSA obtained certificates for Google sites (PDF p. 157). INTERPRETATION: that is why this attack was not stopped by encryption alone.
INTERPRETATION: VPNFilter's downgrade attempts show that HTTPS protects only if the client actually negotiates it, which is why the redirects and HSTS in WS-C13-003 matter.

## Time-sensitive statements
- May 2018 VPNFilter infection of over 500,000 Linksys and Netgear routers (Cisco researchers).
- Comcast ad injection "for many years"; the Snowden-leaked NSA presentation about Petrobras.

## Relations
Motivates WS-C13-003; recapped in WS-C13-005. Chapter 2 introduced man-in-the-middle concepts (WS-C02-005).
