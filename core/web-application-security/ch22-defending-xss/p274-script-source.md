---
id: WAS-C22-009
title: Content Security Policy - Overview and Script Source
source_pages: "274"
chapter: 22
concepts: [content-security-policy, script-src, whitelisting-origins, self-keyword, wildcard-hosts, csp-violation, xss-mitigation]
related: [WAS-C22-008, WAS-C22-010, WAS-C22-011, WAS-C22-012]
time_sensitive: false
---
# Content Security Policy: overview and Script Source
(Source: PDF p. 274, continuing on the tail page 275)

## What the section covers
The section's opening on what CSP is (the heading's introductory text is printed on this page above the Script Source heading), followed by the script-src directive and its pitfalls.

## What CSP is
CSP is a security configuration tool that all major browsers support. It gives developers settings to loosen or tighten the rules about which code may run in the application. Its protections cover which external scripts can be loaded, where they can be loaded from, and which DOM APIs may execute script. The section looks at configurations that reduce XSS risk (PDF p. 274).

## Script Source: the idea
The danger of XSS is that a script you did not write runs. Your own scripts are assumed to be written with your users' interests in mind, but a script written by another user cannot be assumed to be (PDF p. 274). One mitigation, stated at the top of the next page, is to reduce the number of permitted script sources (PDF p. 275).

## Example
MegaBank's support portal, support.mega-bank.com, would plausibly use scripts from across the organisation, so you could name the specific origins, for example mega-bank.com and api.mega-bank.com (PDF p. 275).

## How it works
- CSP lets you whitelist the URLs that scripts may be loaded from, using script-src. A simple policy has the form Content-Security-Policy with script-src set to self plus https://api.mega-bank.com (PDF p. 275).
- Trying to load a script from api2.mega-bank.com then fails and the browser raises a CSP violation error, so scripts from unknown sources such as hacker.com cannot load and run (PDF p. 275).
- Because the browser enforces CSP, and browser test suites are comprehensive, it is hard to bypass (PDF p. 275).
- self means the URL the policy came from and that serves the protected document, so script-src defines two things: safe URLs to load scripts from, and the current URL (PDF p. 275).

## Wildcard risk
CSP supports wildcard host matching, but any wildcard whitelist has inherent risk. Whitelisting every subdomain of mega-bank.com may seem fine today if no malicious scripts run on a MegaBank domain, but if the domain is later reused for something that accepts user-uploaded scripts, such as a hosting subdomain where users upload documents, such a wide net could harm security (PDF p. 275).

## Relations
Follows CSS (WAS-C22-008). The next directives are in WAS-C22-010 and deployment is in WAS-C22-011. WAS-C22-012 recaps the chapter.
