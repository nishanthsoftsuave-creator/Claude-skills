---
id: WS-C16-006
title: Botnets
source_pages: "188"
chapter: 16
concepts: [bot, botnet, malware, cryptomining, click-fraud, antivirus, integrity-checker, outbound-monitoring, immutable-rebuild]
related: [WS-C16-005, WS-C16-007, WS-C06-003, WS-C06-005, WS-C17-002]
time_sensitive: false
---
# Botnets
(Source: PDF p. 188, tail PDF p. 189. The text on PDF p. 188 above the "Botnets" heading is the end of WS-C16-005. The text on PDF p. 189 above the "Summary" heading is the end of this section and is covered here.)

## What the section covers
Why attackers want bots on servers, what botnets are used for, and how to prevent and detect infection.

## Meaning
- Attackers always want spare computing power. After compromising a server they will often install a bot, malware they control through remote commands. Most bots belong to a peer-to-peer network of bots, a botnet, whose members talk to each other over an encrypted protocol (PDF p. 188).
- Bots commonly infect consumer devices such as laptops, but landing one on a server is a bigger prize because far more computing power is available. Control keys for botnets sell for a good price on the dark web (PDF p. 188).
- Common uses: mining bitcoin, click fraud (artificially inflating a site's page-view counts), generating spam email, and committing denial-of-service attacks (covered in chapter 17) (PDF p. 188).

## When and how to apply: protecting against malware infection
- Keep bots from being installed at all. Chapter 6 covered command injection and file upload flaws that can let an attacker install one; follow its advice (WS-C06-003 and WS-C06-005) (PDF p. 188).
- Run up-to-date antivirus software to spot malware quickly (PDF p. 188).
- Monitor outgoing network traffic. Installed bots periodically poll other IP addresses looking for other bots, which shows up as suspicious activity (PDF pp. 188-189).
- Consider an integrity checker on web servers: software that detects unexpected file changes in sensitive directories (PDF p. 189).
- With virtualized services or containers, a rebuild typically wipes out any malicious software that was installed. Periodically rebuilding from an image does a great deal to keep bot infestations away (PDF p. 189).

## Relations
Follows SSRF (WS-C16-005). Botnets are what power the distributed denial-of-service attacks in WS-C17-002. The chapter recap is WS-C16-007.
