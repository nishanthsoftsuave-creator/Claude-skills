---
id: WAS-C04-007
title: Zone Transfer Attacks
source_pages: "97-98"
chapter: 4
concepts: [zone-transfer, dns, nameserver, zone-file, subdomain-discovery, dns-misconfiguration, recon, authorization]
related: [WAS-C04-001, WAS-C04-006, WAS-C04-008, WAS-C04-010]
time_sensitive: false
---
# Zone Transfer Attacks
(Source: PDF pp. 97-98, with the end of the section at the top of PDF p. 99)

## What the section covers
A recon technique for finding subdomains that no public page links to: asking a domain's own nameservers to hand over their full record list. The section explains why the technique works only against misconfigured servers, what success and failure look like, and why it is still worth a quick try. The section heading sits part-way down PDF p. 97; the text above it belongs to the preceding social-media discussion.

## Meaning
- A zone transfer attack is described as a recon trick that works against improperly configured Domain Name System (DNS) servers. The book stresses it is not really a "hack" despite the name; it is an information-gathering technique that takes little effort (PDF p. 97).
- At its core, it is a specially formatted request that is designed to look like a valid zone transfer request from a legitimate DNS server (PDF p. 97).
- DNS servers translate human-readable domain names into machine-readable IP addresses, stored hierarchically in a common pattern so they can be requested and traversed. This lets a server's IP address change without users having to know, since visitors keep using the same name (PDF p. 97).
- DNS servers must keep each other's records in step. A zone transfer is the standardised way servers share records, and the records travel in a text-based format called a zone file (PDF p. 97).

## Why it matters
Zone files often hold configuration data that was never meant to be easy to reach (PDF p. 98). The book says that walking through a public-facing web application and analyzing its network requests only gets the tester so far, and that the aim here is to find subdomains not linked to the public application in any way (PDF p. 97). Its example output lists a mail host, an admin host and an internal host under the bank's domain (PDF p. 98).

## How it works
- A properly configured primary DNS server (the book says master, with slave servers for the secondaries) should answer transfer requests only from the specific secondary servers it is set up to serve. A server that answers anyone is vulnerable to bad actors (PDF p. 98).
- To try the technique against a target the tester must act like a secondary server asking for the zone file. First the tester finds which nameservers are responsible for the target domain, using a standard DNS lookup utility available on most Linux distributions and recent macOS versions (PDF p. 98).
- The book's first example shows that lookup returning two nameservers for the fictional bank domain. A second command then asks one of those nameservers for a transfer of the whole zone (PDF p. 98).
- The book's success example shows a returned list of every record in the zone: the main domain, its nameservers, and several other hosts (a mail host, an admin host and an internal host), each with a public IP address. The book's reading is that the tester now has a list of other web applications under the domain and their addresses, and could browse to those hosts to see what resolves, which can greatly broaden the attack surface (PDF pp. 98-99).

## When and how to apply
- Because the attempt takes only a few lines of shell, the book says it is almost always worth trying; if it succeeds, it yields subdomains that might not have been found any other way (PDF p. 99).
- The book's standing warning from the introduction to recon applies here too: techniques like this can get an IP address flagged and, in the worst case, lead to bans or legal action, so they should be run only against applications the tester owns or has written permission to test. That warning is printed in an earlier chapter, so it carries no page cite here.
- INTERPRETATION: because the request is a single, cheap query, it fits at the start of the subdomain recon sequence, before the slower brute force and dictionary methods in later rows (see WAS-C04-008).

## Limitations and failure modes
- Many servers are configured correctly, so the attempt often fails. A refused transfer is reported by the lookup utility as a failure instead of a record list, (PDF p. 99).
  INTERPRETATION: a refusal tells the tester only that this nameserver does not hand out its zone.
- The book calls the attack "easy to stop" and says many applications are already set up to reject it (PDF p. 99). INTERPRETATION: a failed attempt therefore rules out this one technique and nothing more; the other discovery methods in the chapter still apply.

## Defence
The book frames the defence in terms of its cause: transfers should be allowed only to the designated secondary servers, and anything else should be refused (PDF p. 98). A server that does so answers a stranger's request with a failure message, as in the book's second example (PDF p. 99).
SUPPLEMENTARY: DNS server software usually has an allow-list setting for zone transfers (for example the allow-transfer option in the BIND documentation); the book names no product or setting, so check the documentation of the DNS software in use.

## Relations
Follows the public-records techniques in WAS-C04-006 and precedes brute forcing in WAS-C04-008. The chapter's overview of why subdomain mapping matters is in WAS-C04-001, and its summary is in WAS-C04-010.
