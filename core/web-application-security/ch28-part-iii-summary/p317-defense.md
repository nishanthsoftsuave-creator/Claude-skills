---
id: WAS-C28-004
title: Part III Summary - Defense
source_pages: "317-320"
chapter: 28
concepts: [defense-summary, secure-architecture, code-review, vulnerability-discovery, vulnerability-management, xss-defense, csrf-defense, xxe-defense, injection-defense, dos-defense, dependency-security]
related: [WAS-C18-001, WAS-C19-002, WAS-C20-001, WAS-C21-001, WAS-C22-001, WAS-C23-001, WAS-C24-002, WAS-C25-001, WAS-C26-002, WAS-C27-008, WAS-C28-003]
time_sensitive: false
---
# Part III Summary: Defense
(Source: PDF pp. 317-320. The block starts below the Defense heading on PDF p. 317.)

## What the section covers
The recap of Part III (defense), one point block per defensive topic, in the order of the chapters: secure architecture, code review, vulnerability discovery, vulnerability management, the defenses against XSS, CSRF, XXE, injection and DoS, and securing third-party dependencies.

## Secure application architecture
- A secure web application starts at the architecture phase. A vulnerability found there can cost as much as 60 times less to fix than one found in production code (PDF p. 317).
- Proper security architecture can give application-wide mitigations for common risks, instead of on-demand mitigations that tend to be inconsistent or forgotten (PDF p. 318).

## Reviewing code for security
After a secure architecture is chosen, a proper security code review process should keep common, easy-to-spot security bugs out of production. A security review is done much like an ordinary code review; what differs is the kind of bug being sought and how files and modules are prioritized when time is limited (PDF p. 318).

## Vulnerability discovery
Ideally vulnerabilities are found before they reach production, but often they are not. Several techniques reduce how many reach production. Besides building an internal discovery pipeline, an organization can use third-party specialists, bug bounty programs and penetration testers. These help find vulnerabilities early and give hackers a reason to report them for payment instead of selling them on the black market or exploiting them (PDF p. 318).

## Vulnerability management
- A found vulnerability should be reproduced and triaged, then scored by its potential impact so its fix can be prioritized (PDF p. 318).
- Several scoring algorithms exist, with CVSS the best known. The book says every organization must adopt one; which one matters less than using one. Each has a margin of error, but if it can tell a severe vulnerability from a low-risk one it will help prioritize work and fixes (PDF p. 318).

## Defending against XSS
- XSS can be mitigated at several levels of the stack: with sanitization functions at the API level, in the database, or on the client. Since XSS attacks the client, the client is the most important place for mitigations (PDF p. 318).
- Simple XSS can be removed by smart coding, especially around the DOM. Advanced XSS, such as that relying on DOM sinks, is much harder to mitigate and may not even be reproducible, so knowing the most common sinks and sources for each XSS type is important (PDF p. 319).

## Defending against CSRF
CSRF exploits the trust between a user and the browser, so it is mitigated by adding rules for state-changing requests that a browser cannot confirm on its own. The mitigations listed include removing state-changing GET requests from the codebase, using CSRF tokens, and requiring 2FA confirmation on elevated API requests (PDF p. 319).

## Defending against XXE
Most XXE is easy both to exploit and to prevent, since all modern XML parsers offer a configuration option to disable external entities. More advanced defense means looking at XML-like formats and parsers (SVG, PDF, RTF and so on) and assessing how they are used the way a true XML parser would be, to see whether any behavior carries over (PDF p. 319).

## Defending against injection
- Injection aimed at SQL databases can be stopped or reduced by configuring SQL correctly and generating queries properly, for example with prepared statements (PDF p. 319).
- Injection aimed at CLI interfaces is harder to detect and prevent. When designing or adopting such tools, best practices such as the principle of least authority and separation of concerns should be strongly considered (PDF p. 319).

## Defending against DoS
- A single-attacker DoS can be mitigated by scanning regular expressions for backtracking problems, keeping user API calls away from functions that use many server resources, and adding rate limits to those functions when needed (PDF p. 319).
- DDoS is harder to mitigate. Mitigation should start at the firewall and work upward: blackholing traffic is one option, and a bandwidth management service that specializes in DDoS is another (PDF p. 319).

## Securing third-party dependencies
- Third-party dependencies are called one of the security banes of modern web applications, because they are included so widely and audited so unevenly; they are a common cause of an application's downfall (PDF p. 320).
- Integrations should be set up so that their permissions and scope are limited to what is needed, and they should be scanned and reviewed before integration, including a look in CVE databases to find out whether others have reported vulnerabilities affecting the integration (PDF p. 320).

## Relations
Condenses Chapters 18 to 27: architecture (WAS-C18-001), code review (WAS-C19-002), discovery (WAS-C20-001), management (WAS-C21-001), XSS (WAS-C22-001), CSRF (WAS-C23-001), XXE (WAS-C24-002), injection (WAS-C25-001), DoS (WAS-C26-002) and dependencies (WAS-C27-008). It mirrors the offense recap in WAS-C28-003.
