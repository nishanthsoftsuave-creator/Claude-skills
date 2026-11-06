---
id: WAS-C22-008
title: CSS as an Attack Vector
source_pages: "273"
chapter: 22
concepts: [css-injection, user-uploaded-css, data-exfiltration, background-url, attribute-selectors, stylesheet-sanitisation]
related: [WAS-C22-007, WAS-C22-009, WAS-C22-002, WAS-C11-002]
time_sensitive: false
---
# CSS as an Attack Vector
(Source: PDF p. 273, continuing on the tail page 274)

## What the section covers
How stylesheets that come from users can leak data, and three ways of preventing it.

## Why CSS is a target
CSS is usually thought of as display only, but its capability makes it an alternative way for skilled hackers to deliver XSS and other attack payloads (PDF p. 273).

## How the risk arises
- Applications often store user data on a server for other users to read; the standard example is a comment box. Some sites offer the same flow with styles: a user uploads a stylesheet to customise a profile, and visitors download it to see the personalised page (PDF p. 273).
- CSS is less powerful than a programming language like JavaScript, but it can still be an attack vector for stealing data from a page (PDF p. 273).
- Whenever an image from another origin loads, whether from HTML, JavaScript or CSS, a GET request is made, as seen earlier with the image tag. In CSS the background url property loads an image from a chosen domain, and being a GET it can carry query parameters (PDF p. 273).
- CSS can also style by the state of a form. The book's example applies a background only when an income field has the value over 100k, and the background points at an attacker's address with the amount in the query string. When the value matches, the browser sends a GET request that leaks the form data to another site (PDF p. 274).

## Prevention
CSS is much harder to sanitise than JavaScript, so the book suggests not allowing stylesheet uploads, or generating stylesheets yourself and only letting users change permitted fields that cannot start GET requests. It ranks the options (PDF p. 274):
- Easy: do not allow user-uploaded CSS.
- Medium: allow only specific fields to be changed, and generate the custom stylesheet on the server from those fields.
- Hard: sanitise every CSS attribute that can start an HTTP request, such as background url.

## Relations
Follows entity encoding (WAS-C22-007) and precedes the Content Security Policy sections (WAS-C22-009). The image-tag GET technique is in WAS-C11-002.
