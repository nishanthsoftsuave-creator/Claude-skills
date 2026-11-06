---
id: WS-C15-007
title: "XML Attacks: Other Considerations"
source_pages: "180"
chapter: 15
concepts: [least-privilege, outbound-network-lockdown, domain-whitelist, chroot-jail, directory-restriction, defense-in-depth]
related: [WS-C15-005, WS-C15-006, WS-C16-005, WS-C11-002]
time_sensitive: false
---
# XML Attacks: Other Considerations
(Source: PDF p. 180; this row covers the "Other Considerations" text only, which ends where the "Summary" heading begins)

## What the section covers
Operating-system and network restrictions that limit the harm from external entity attacks even if the parser is misconfigured.

## Meaning
- External entity attacks show why the principle of least privilege matters. The principle says software components and processes should receive only the minimum permissions they need to do their work (PDF p. 180).

## When and how to apply
- Network: an XML parser rarely has a good reason to make outbound network requests, so consider locking down outbound requests for the whole web server. If the server must call out, for example to third-party APIs, whitelist those APIs' domains in the firewall rules (PDF p. 180).
- Disk: restrict which directories on disk the web server can reach. On Linux, run the server process in a chroot jail, which ignores attempts by the process to change its root directory. On Windows, manually whitelist the directories the server may access (PDF p. 180).

## Why it matters
INTERPRETATION: these controls act as a second layer behind the parser fix of WS-C15-006; if the process cannot reach the network or sensitive directories, an external entity has little to read or call.

## Relations
Supports WS-C15-005 and WS-C15-006; the same outbound whitelisting returns as an SSRF defence in WS-C16-005 and as a commandment in WS-C18-001.
