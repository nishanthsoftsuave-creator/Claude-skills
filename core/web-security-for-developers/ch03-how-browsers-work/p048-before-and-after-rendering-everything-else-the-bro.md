---
id: WS-C03-004
title: Before and After Rendering - Everything Else the Browser Does
source_pages: "48"
chapter: 3
concepts: [browser-responsibilities, dns-resolution, dns-cache, tcp-handshake, tls-handshake, https, post-request, set-cookie, login-flow]
related: [WS-C03-003, WS-C03-005, WS-C02-002, WS-C02-005, WS-C02-004]
time_sensitive: true
---
# Before and After Rendering - Everything Else the Browser Does
(Source: PDF p. 48. The "Summary" heading lower on the same page belongs to WS-C03-005.)

## What the section covers
A reminder that a browser does far more than render HTML and run JavaScript, followed by a step-by-step walk-through of a user logging in to a major retail site that ties together DNS, TCP, TLS, HTTP and cookies.

## Meaning
Beyond rendering and scripting, browsers work with the operating system to resolve and cache DNS addresses, interpret and verify security certificates, wrap requests in HTTPS where needed, and store and send cookies according to server instructions (PDF p. 48).

## How it works: logging in to Amazon (PDF p. 48)
1. The user visits the site's address in their browser.
2. The browser tries to resolve the domain to an IP address. It checks the operating system's DNS cache first. If there is no hit, it asks the ISP to look in the ISP's DNS cache. In the unlikely case that no one at the ISP has visited before, the ISP resolves it at an authoritative DNS server.
3. With the IP address known, the browser starts a TCP handshake with the matching server, in order to establish a secure connection.
4. Once the TCP session is up, the browser builds an HTTP GET request for the site. TCP splits it into packets, sends them, and the server reassembles them.
5. The conversation then upgrades to HTTPS: browser and server perform a TLS handshake, agree on a cipher and exchange keys.
6. Over the secure channel the server sends an HTTP response containing the HTML of the front page. The browser parses and shows it, usually triggering many more GET requests.
7. The user goes to the login page, enters credentials and submits the form, which creates a POST request.
8. The server validates the credentials and creates a session by returning a Set-Cookie header. The browser stores the cookie for the stated time and sends it with later requests to the site. After this the user can access their account.

## Relations
Ties together WS-C02-002 (DNS, TCP), WS-C02-005 (TLS and HTTPS) and WS-C02-004 (cookies and sessions). The chapter recap is WS-C03-005.

## Time-sensitive statements
The example uses a specific commercial site (Amazon) as of the book's 2020 writing; the sequence of steps is general.
