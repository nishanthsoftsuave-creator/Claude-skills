---
id: WAS-C06-005
title: Detecting Server-Side Frameworks - Lead-in and Header Detection
source_pages: "124"
chapter: 6
concepts: [server-side-frameworks, header-detection, x-powered-by, server-header, microsoft-iis, information-leakage, fingerprinting]
related: [WAS-C03-015, WAS-C06-006, WAS-C06-004]
time_sensitive: true
---
# Detecting Server-Side Frameworks - Lead-in and Header Detection
(Source: PDF p. 124)

## What the section covers
The introduction to detecting software on the server, and the first technique: reading identifying HTTP response headers. The lead-in has no row of its own, so it is included here.

## Meaning
- Finding what runs in the browser is much easier than finding what runs on the server. The client code is downloaded and held in memory reachable through the DOM; scripts that load conditionally or asynchronously can still be reached if you create the right conditions (PDF p. 124).
- Server-side dependencies are harder to find but often not impossible. They sometimes leave marks on HTTP traffic, such as headers or optional fields, or they expose their own endpoints (PDF p. 124).
- It takes more knowledge of each framework, but a few packages are very widely used. Memorising how to detect the top ones lets you recognise them across many applications (PDF p. 124).

## How it works: header detection
- Some web server packages that are insecurely configured give away too much in their default headers (PDF p. 124).
- The standard example is the X-Powered-By header, which can state the name and version of the server stack. It was often on by default in older Microsoft IIS (PDF p. 124).
- A response from such a server may show X-Powered-By with ASP.NET. With luck it also shows a Server header such as Microsoft-IIS/4.5 and an X-AspNet-Version header such as 4.0.25 (PDF p. 124).

## Limitations
Careful administrators disable these headers and careful development teams remove them from the default setup. The book still says millions of sites expose them (PDF p. 124).

## Relations
Web servers as a technology: WAS-C03-015. The next detection technique, default error pages, is WAS-C06-006.

## Time-sensitive statements
IIS and ASP.NET version strings, and the claim that older IIS enables the header by default, are dated.
