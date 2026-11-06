---
id: WS-C04-002
title: Static and Dynamic Resources
source_pages: "52"
chapter: 4
concepts: [static-resource, dynamic-resource, url-mapping, web-server-configuration, templates-and-scripts]
related: [WS-C04-001, WS-C04-003, WS-C04-004, WS-C04-005]
time_sensitive: false
---
# Static and Dynamic Resources
(Source: PDF p. 52. The "Static Resources" subsection that begins lower on the same page is covered in WS-C04-003.)

## What the section covers
The top-level distinction the chapter is built around: the two kinds of content a web server can return for an HTTP request (PDF p. 52).

## Meaning
- A static resource is an HTML file, an image, or some other kind of file that the server sends back exactly as stored, without altering it (PDF p. 52).
- A dynamic resource is code, a script or a template that the server runs or interprets when the request arrives, so the response is produced by execution rather than read from disk (PDF p. 52).
- Modern servers can host both kinds side by side (PDF p. 52).

## How it works
- Which of the two the server uses to answer a request is decided by the URL in the HTTP request (PDF p. 52).
- The server resolves URLs using a configuration file that maps URL patterns to particular resources (PDF p. 52). The same mapping idea is developed further for static files in WS-C04-003.
- The introduction closes by saying the following subsections look at how servers handle each type (PDF p. 52).

## Relations
Static handling continues in WS-C04-003 and dynamic handling in WS-C04-004. The chapter summary, WS-C04-005, repeats this two-way split. Introduced by the chapter framing in WS-C04-001.
