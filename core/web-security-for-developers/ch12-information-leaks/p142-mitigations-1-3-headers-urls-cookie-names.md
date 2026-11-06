---
id: WS-C12-002
title: "Mitigations 1-3: Headers, URLs and Cookie Names"
source_pages: "142"
chapter: 12
concepts: [server-header, clean-urls, file-extensions, session-cookie-name, jsessionid, metasploit, technology-fingerprinting, generic-names]
related: [WS-C12-001, WS-C12-003, WS-C12-005, WS-C10-002]
time_sensitive: false
---
# Mitigations 1-3: Headers, URLs and Cookie Names
(Source: PDF p. 142)

## What the section covers
The first three ways a web server gives away its technology and how to stop each: telltale response headers, URLs with implementation-specific file suffixes, and session cookie names that identify the server-side platform (PDF p. 142).

## Mitigation 1: disable telltale server headers
- Turn off, in the web server configuration, any HTTP response headers that reveal the server technology, language or version (PDF p. 142).
- By default most web servers attach a Server header to every response naming the software on the server side. The vendor gets free advertising, but the browser does not use the header; it only tells an attacker which vulnerabilities to try (PDF p. 142).
- The configuration should suppress this header. The book jokes that you could even make it report a wrong server technology (PDF p. 142).

## Mitigation 2: use clean URLs
- Avoid file suffixes such as .php, .asp and .jsp in URLs, which expose how the site is built (PDF p. 142).
- Use clean URLs, meaning addresses that give away no implementation details. Extension-bearing URLs are typical of older web servers that reference template filenames directly, so avoid them (PDF p. 142).

## Mitigation 3: use generic cookie parameters
- The name of the cookie holding session state often reveals the server-side technology. Java web servers usually store the session ID in a cookie called JSESSIONID, and attackers inspect cookie names like this to identify servers (PDF p. 142).
- Listing 12-1 is code from the hacking tool Metasploit that is trying to detect and compromise an Apache Tomcat server. It checks whether the response cookies match the JSESSIONID name; if so, it takes the session ID value and posts a username and password to an administrative login path (a security-check URL under /admin), sending that session cookie along (PDF p. 142). The point the book makes is that the tool's first move is to test the session cookie name (PDF p. 142).
- Fix: configure the server so that nothing in its cookies hints at the technology stack, and give the session cookie a generic name such as "session" (PDF p. 142).

## When and how to apply
Apply all three in the web server and application configuration.
INTERPRETATION: after changing them, inspect a real response in browser developer tools and confirm that headers, URL paths and cookie names no longer name a vendor or language.

## Relations
Continues in WS-C12-003 (mitigations 4-6). Session cookies and their security are treated in Chapter 10 (see WS-C10-002).
