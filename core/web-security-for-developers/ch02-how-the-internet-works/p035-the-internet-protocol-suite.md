---
id: WS-C02-002
title: The Internet Protocol Suite
source_pages: "35-36"
chapter: 2
concepts: [arpanet, tcp, packets, sequence-numbers, checksum, udp, ip-address, ipv4, ipv6, icann, dns, dns-poisoning, ttl, cname, mx-record]
related: [WS-C02-001, WS-C02-003, WS-C16-001]
time_sensitive: true
---
# The Internet Protocol Suite
(Source: PDF pp. 35-36, tail PDF p. 37. The section starts part-way down PDF p. 35, below the chapter introduction in WS-C02-001. On PDF p. 37 only the text above the heading "Application Layer Protocols" belongs here; the rest is WS-C02-003.)

## What the section covers
Why TCP was invented, how it makes unreliable networks dependable, how IP addresses are issued and written, and how the Domain Name System maps names to addresses, including the DNS poisoning risk.

## Why TCP exists
- The first message ever sent over ARPANET, the forerunner of the internet, was a LOGIN command to a remote computer at Stanford. Only the first two letters, "LO", arrived before the network crashed. Early data exchange was therefore unreliable (PDF p. 35).
- The US military wanted remote computers connected so that they could keep exchanging information even if a Soviet nuclear strike knocked out parts of the network (PDF pp. 35-36).
- Engineers developed the Transmission Control Protocol (TCP) to ensure reliable exchange between computers. TCP is one of about 20 protocols that together form the internet protocol suite (PDF p. 36).

## How TCP works
- A message is split into data packets, each carrying a destination address. The machines making up the internet push each packet towards its destination without needing to process the whole message (PDF p. 36).
- On arrival the recipient reassembles packets into order using the sequence number on each. It sends a receipt for every packet. If a packet is not acknowledged, the sender resends it, possibly along a different network path. This lets computers deliver data across a network that is expected to be unreliable (PDF p. 36).
- Improvements as the internet grew: packets now carry a checksum so recipients can detect corruption and decide whether to request a resend. Senders also adjust their sending rate in advance to match how fast data is consumed, because servers are usually far more powerful than the clients receiving from them and must avoid swamping them (PDF p. 36).
- Note: TCP is still the most common protocol thanks to its delivery guarantees, but others are used too. The User Datagram Protocol (UDP), a newer protocol, deliberately lets packets be dropped so data can stream at a steady rate. It is common for live video, where viewers prefer a few lost frames over a delayed feed when the network is congested (PDF p. 36).

## Internet Protocol addresses
- Packets are sent to Internet Protocol (IP) addresses, numbers assigned to individual connected computers. Each must be unique, so they are issued in a structured way (PDF p. 36).
- At the top, ICANN (the Internet Corporation for Assigned Names and Numbers) allots blocks to regional authorities, which grant blocks to internet service providers and hosting companies in their region. Your ISP gives your computer an address that stays fixed for a few months before being rotated. Hosting companies receive an address for each server they connect (PDF p. 36).
- IP addresses are binary numbers, usually written in IPv4 form, which allows 2^32 (4,294,967,296) addresses. The book gives Google's name server address, 8.8.8.8, as an example (PDF p. 37).
- Because IPv4 addresses are running out unsustainably, the internet is moving to IPv6 (to allow for more connected devices), written as eight groups of four hexadecimal digits separated by colons; the book's example is 2001:0db8:0000:0042:0000:8a2e:0370:7334 (PDF p. 37).

## The Domain Name System (DNS)
- IP addresses are hard for people to remember, so a global directory, the Domain Name System, translates readable domains like example.com into addresses like 93.184.216.119. A domain is just a placeholder for an IP address. Domains are unique and must be registered with private organisations called domain registrars (PDF p. 37).
- On first meeting a domain, a browser asks a local domain name server, typically run by the ISP, and caches the result to avoid slow future lookups. Caching means new or changed domains take a while to propagate. How long is set by the time-to-live (TTL) value on the DNS record, which tells caches when to expire it (PDF p. 37).
- Risk: DNS caching enables DNS poisoning, where a local cache is deliberately corrupted so that traffic goes to a server the attacker controls (PDF p. 37).
- Besides addresses, name servers hold other records: canonical name (CNAME) records, which let several domain names point at one IP address, and mail exchange (MX) records, which help route email. Chapter 16 looks at how DNS records can help fight spam (PDF p. 37).

## Relations
Follows the framing in WS-C02-001 and is followed by WS-C02-003, which builds higher-level protocols on top of TCP. The spam point is developed in the book's Chapter 16 (Don't Be an Accessory).

## Time-sensitive statements
IPv4 exhaustion and the ongoing shift to IPv6, the 8.8.8.8 address, and the roughly 20-protocol count describe the state of the internet in 2020.
