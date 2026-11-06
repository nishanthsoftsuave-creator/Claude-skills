---
id: WS-C04-003
title: Static Resources
source_pages: "52-54"
chapter: 4
concepts: [static-resource, url-resolution, gzip-compression, cache-headers, access-control, content-delivery-network, content-management-system, third-party-plugins, wordpress, security-patching]
related: [WS-C04-002, WS-C04-004, WS-C11-003, WS-C14-001, WS-C14-005]
time_sensitive: true
---
# Static Resources
(Source: PDF pp. 52-54. The "Static and Dynamic Resources" overview above this heading on PDF p. 52 is covered in WS-C04-002. The Figure 4-2 caption printed at the top of the next page belongs to this section's final discussion.)

## What the section covers
How static files are served, how modern servers resolve URLs to them, content delivery networks, content management systems and plug-in services, and the security issues each brings (PDF pp. 52-54).

## Meaning and history
- Early websites consisted mostly of static resources. Developers wrote HTML files by hand and deployed the site by copying the files to the server and restarting the server process. A visitor typed the URL, the server read it as a request for a file on disk, and returned that file unchanged (PDF p. 52).
- The book's example is the site for the 1996 film Space Jam, still online and made entirely of static files. Its page URLs, such as a sitemap page, end in .html, showing that each page is a file on the server (PDF p. 52).
- Tim Berners-Lee's original vision of the web resembled that site: a network of static files on servers holding the world's information (PDF p. 52).

## How it works: URL resolution
- Current servers still treat static files much like older ones: the resource name appears in the URL and the file is returned from disk. Figure 4-1 is a black-and-white photograph of a hedgehog on a heap of spaghetti, served from a URL naming a PNG file under an images path (PDF pp. 52-53).
- A modern server can map any URL to any static resource. The file need not live where the URL suggests, and the developer can name it anything. Separating URL from file path gives developers freedom to organise code; for instance, every user could have a different profile image behind the same path (PDF p. 53).
- Servers often add to or process static content before sending it. They may compress large files with gzip to save bandwidth, or add caching headers so the browser reuses its local copy within a set time window. This makes the site feel faster and lowers server load (PDF p. 53).

## Limitations and failure modes
- Static files alone rarely have security flaws, but resolving a URL to a file can introduce them. If users mark some files private, such as uploaded images, the server needs access control rules; ways attackers get around them are covered in Chapter 11 (PDF p. 53). See WS-C11-003.

## Content delivery networks
- A content delivery network (CDN) keeps duplicate copies of static files in data centres worldwide and serves each browser from the nearest one. Named examples are Cloudflare, Akamai and Amazon CloudFront (PDF p. 54).
- CDNs shift the load of large files such as images to a third party, so small companies can run responsive sites without heavy server spending. Integration is usually simple and billed monthly by the amount of resources deployed (PDF p. 54).
- Security cost: a CDN lets a third party deliver content under your security certificate, so the integration must be set up securely. Chapter 14 covers this (PDF p. 54). See WS-C14-005.

## Content management systems
- Many sites still hold mostly static content but are built with content management systems (CMSs) instead of by hand. A CMS gives non-technical authors tools to write content, tends to impose a uniform look, and lets administrators edit in the browser (PDF p. 54).
- Plug-ins extend a CMS with analytics, appointment booking, customer support and online stores. This reflects a wider trend of using specialised third-party services: Google Analytics for tracking, Facebook Login for authentication and Zendesk for support, each added with a few lines of code and an API key (PDF p. 54).
- Relying on other people's code theoretically improves security, since those companies employ security staff and have a motive to protect their services. But their ubiquity makes them targets. Many self-hosted WordPress installations, WordPress being the most popular CMS, are rarely patched, and a simple Google search finds vulnerable ones (PDF p. 54).
- Figure 4-2 (printed at the top of the next page) is a screenshot of a Google search for error_log files inside WordPress content folders, showing about 345,000 results that include exposed error logs from many sites; its caption jokes about coming to get your unsecured WordPress instances. It illustrates how easily unpatched, misconfigured installations are found.

## When and how to apply
- When using third-party code you must watch security advisories and apply patches as soon as they are released (PDF p. 54). Chapter 14 returns to the risks of third-party code and services (WS-C14-001).

## Time-sensitive statements
Named products and sites: Space Jam website, Cloudflare, Akamai, Amazon CloudFront, Google Analytics, Facebook Login, Zendesk, WordPress. Popularity claims (WordPress as the most popular CMS) and the Google result count in Figure 4-2 reflect the time the book was written.
