---
id: WS-C06-001
title: Chapter 6 Introduction - Injection Attacks
source_pages: "77"
chapter: 6
concepts: [injection-attack, client-server-architecture, http-request, user-agent-spoofing, untrusted-input, hacking-tools]
related: [WS-C01-003, WS-C06-002, WS-C06-003, WS-C06-004, WS-C06-005, WS-C06-006]
time_sensitive: false
---
# Chapter 6 Introduction - Injection Attacks
(Source: PDF p. 77, tail PDF p. 78. The text on PDF p. 78 below the "SQL Injection" heading belongs to WS-C06-002.)

## What the section covers
The opening framing of the chapter on injection attacks: what an injection attack is, why a server cannot tell who sent a request, and the four kinds of injection the chapter will examine (PDF pp. 77-78).

## Meaning
- An injection attack is one where the attacker injects external code into an application in order to take control of it or to read sensitive data (PDF p. 77).
- The chapter moves from how the internet works (the earlier chapters) to specific vulnerabilities and the methods hackers use to exploit them (PDF p. 77).

## How it works: why servers can be tricked
- The internet is a client-server architecture. One web server handles connections from many clients at once; most clients are browsers that generate HTTP requests as the user navigates, and the server answers with HTTP responses carrying the HTML of the pages (PDF p. 77).
- Because the server controls the site's content, its code expects particular interactions and therefore particular requests: a GET request to a new URL each time a user clicks a link, or a POST request when the user enters login credentials and submits (PDF pp. 77-78).
- Nothing forces a browser to send only these expected requests, and servers accept requests from any client, not just browsers. A programmer with an HTTP client library can script requests to arbitrary URLs, which is exactly what the hacking tools introduced in Chapter 1 do (PDF p. 78).
- The server cannot reliably tell whether a script or a browser produced a request, because the request contents look the same either way. The most it can do is inspect the User-Agent header, which is meant to say what kind of agent sent the request, but scripts and hacking tools usually spoof that header so it looks like a browser's (PDF p. 78).
- Attackers therefore commonly place malicious code inside an HTTP request so that the server is tricked into executing it. That is the basis of an injection attack (PDF p. 78).

## Why it matters
- Injection attacks are described as astonishingly common and, when successful, devastating (PDF p. 78).
- A web developer needs to know every way they can occur and how to defend against them. When writing site code, consider what could arrive in the HTTP requests the site handles, not merely what you expect to arrive (PDF p. 78).

## Scope of the chapter
Four types are covered: SQL injection, command injection, remote code execution, and attacks that exploit file upload vulnerabilities (PDF p. 78). They are taken up in WS-C06-002, WS-C06-003, WS-C06-004 and WS-C06-005, and recapped in WS-C06-006.

## Relations
The hacking tools mentioned are introduced in WS-C01-003. The "never trust request contents" stance here is the common thread of the whole chapter.
