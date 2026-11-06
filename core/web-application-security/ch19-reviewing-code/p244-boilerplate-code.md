---
id: WAS-C19-006
title: Secure-Coding Anti-Patterns - Boilerplate Code
source_pages: "244"
chapter: 19
concepts: [boilerplate-code, default-configuration, mongodb-exposure, framework-defaults, version-disclosure, secure-by-default, framework-abstraction]
related: [WAS-C19-005, WAS-C19-007, WAS-C06-006]
time_sensitive: true
---
# Secure-Coding Anti-Patterns: Boilerplate Code
(Source: PDF p. 244, with the conclusion on PDF p. 245 above the next heading)

## What the section covers
The danger of shipping default or boilerplate framework code and configuration into production without evaluating it.

## Meaning
- The anti-pattern is the use of boilerplate or default framework code. It is easy to miss because frameworks and libraries often take extra effort to tighten security, when they should come hardened and require loosening instead (PDF p. 244).

## Examples
- A classic case is a configuration mistake in MongoDB that made older versions reachable over the internet by default when installed on a web server. With no mandatory authentication on the databases, scripts hijacked tens of thousands of MongoDB databases and demanded Bitcoin for their return. A couple of lines in a configuration file, making MongoDB reachable locally only, would have prevented it (PDF p. 244).
- Similar problems exist in most major frameworks. Using the default Ruby on Rails 404 page can reveal the version of Ruby on Rails in use, and EmberJS ships a default landing page meant to be removed in production applications.

## Why it happens and what to do
- Frameworks abstract away difficult, routine work for developers. If developers do not understand the abstraction, it may be done wrongly and without proper security controls (PDF p. 245).
- Therefore avoid launching boilerplate code into production unless that code has been evaluated and configured properly.

## When and how to apply
INTERPRETATION: in review, list each framework's defaults that touch network exposure, authentication, error pages and sample content, and confirm each was changed or consciously kept.

## Time-sensitive statements
The MongoDB default and the framework examples reflect versions at the time of writing; later versions may differ.

## Relations
Follows blacklists (WAS-C19-005). The book showed how default 404 pages reveal versions during recon (WAS-C06-006). Next is the permissions anti-pattern (WAS-C19-007).
