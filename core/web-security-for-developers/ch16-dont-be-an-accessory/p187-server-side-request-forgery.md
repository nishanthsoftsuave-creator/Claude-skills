---
id: WS-C16-005
title: Server-Side Request Forgery
source_pages: "187"
chapter: 16
concepts: [ssrf, outbound-requests, third-party-api, url-construction, sdk, defense-in-depth, firewall-whitelist, penetration-testing]
related: [WS-C15-005, WS-C15-007, WS-C16-004, WS-C16-006, WS-C17-002, WS-C14-004]
time_sensitive: false
---
# Server-Side Request Forgery
(Source: PDF p. 187, tail PDF p. 188. The text at the top of PDF p. 187 above the "Server-Side Request Forgery" heading, the end of the clickjacking section, belongs to WS-C16-004. The "Protecting Against Server-Side Forgery" text on PDF p. 188, above the "Botnets" heading, is the end of this section and is covered here.)

## What the section covers
What SSRF is, why attackers want it, how they detect it, and three layers of defence.

## Meaning
- Attackers sending malicious HTTP requests often try to hide where they come from. For example, denial-of-service attacks (next chapter) are more effective when they come from many different IP addresses (PDF p. 187).
- If your server makes outgoing HTTP requests and an attacker can control the destination URLs, you are vulnerable to server-side request forgery (SSRF) and your server can be used to send malicious requests (PDF p. 187).
- Outbound calls are legitimate in themselves. Third-party APIs are generally offered as HTTPS web services, and a server may use them to send transactional email, index content for search, record unexpected errors, or process payments. The problem is an attacker making the server call a URL of their choosing (PDF p. 187).

## How it works
- Typically the vulnerability appears when the outbound URL is insecurely built from part of an HTTP request that arrived at the server (PDF p. 187).
- Detection by attackers: spider through the site, visit every page, and use hacking tools to replace each HTTP parameter with a URL they control. If their trap URL receives a request, it must have come from your server, so you are vulnerable (PDF p. 187).
- They also test whether any part of the site accepts XML, then try XML external entity attacks to achieve SSRF, as discussed in chapter 15 (WS-C15-005) (PDF p. 187).

## When and how to apply: protection at several levels (PDF p. 188)
1. Code audit, the first and most important step. Review every place that makes outbound HTTP requests. You almost always know in advance which domains an API call needs, so build those URLs from domains stored in configuration or code and never from client input. Using the SDK that most APIs provide for free is one way to ensure this.
2. Network level, as defence in depth (protecting yourself in several overlapping ways). Whitelist in the firewall only the domains you need and ban all others, which catches problems code review missed.
3. Penetration testing: hire an external team, or use an automated online tool, to find SSRF holes. You are using the attackers' own tools before they can.

## Relations
Follows clickjacking (WS-C16-004); the same outbound lockdown appears in WS-C15-007. Botnets are next (WS-C16-006), and the chapter summary is WS-C16-007.
