---
id: WAS-C28-003
title: Part III Summary - Offense
source_pages: "316"
chapter: 28
concepts: [offense-summary, xss-summary, csrf-summary, xxe-summary, injection-summary, dos-summary, third-party-exploitation]
related: [WAS-C10-001, WAS-C11-001, WAS-C12-001, WAS-C13-001, WAS-C14-002, WAS-C28-004]
time_sensitive: false
---
# Part III Summary: Offense
(Source: PDF p. 316, with the rest of the block on PDF p. 317)

## What the section covers
The recap of Part II (offense), one short point block per attack type: XSS, CSRF, XXE, injection, DoS and exploiting third-party dependencies.

## Cross-Site Scripting (XSS)
- XSS is possible when an application uses user-supplied input in a way that permits script execution (PDF p. 316).
- When the usual forms of XSS have been stopped, by sanitizing DOM elements or at the API level or both, XSS may still be found. XSS sinks exist because of bugs in the browser DOM specification, and sometimes because of third-party integrations that were built badly (PDF p. 316).

## Cross-Site Request Forgery (CSRF)
- CSRF abuses the trust relationship between browser and user. An application that is configured badly may accept elevated-privilege requests on behalf of a user who unknowingly clicked a link or submitted a web form (PDF p. 316).
- If the easy targets, state-changing HTTP GET requests, are already filtered, other attack routes such as web forms should be considered (PDF p. 316).

## XML External Entity (XXE) (printed on the next page)
A weakness in the XML specification lets a wrongly configured XML parser leak sensitive server files in answer to a valid XML request. This is often visible when a request takes XML or XML-like data from the client directly. In more complex applications indirect XXE can occur: the server accepts a payload from the user and then builds an XML file to hand to the parser (PDF p. 317).

## Injection attacks
SQL injection is the best known and most prepared for, yet injection can hit any command-line utility the server uses in response to an API request. SQL databases are usually well guarded and automation is good for the well-documented SQL injection tests. If those fail, the book says to consider image compressors, backup utilities and other CLIs as targets (PDF p. 317).

## Denial of service (DoS)
DoS attacks run from irritating drops in server performance to full interruption for legitimate users. They can aim at regular expression engines, at resource-hungry server processes, or simply at normal application or network functions using heavy traffic or large numbers of requests (PDF p. 317).

## Exploiting third-party dependencies
- These are quickly becoming one of the easiest attack paths, partly because third-party dependencies are audited less closely than first-party code (PDF p. 317).
- Open source CVE databases list vulnerabilities already reported in well-known dependencies, which can then be used against a target unless it has been updated or patched by hand (PDF p. 317).

## Relations
Condenses the chapters on XSS (WAS-C10-001), CSRF (WAS-C11-001), XXE (WAS-C12-001), injection (WAS-C13-001) and DoS (WAS-C14-002). The defense recap follows in WAS-C28-004.
