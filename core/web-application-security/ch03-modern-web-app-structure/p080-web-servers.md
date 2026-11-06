---
id: WAS-C03-015
title: Web Servers
source_pages: "80"
chapter: 3
concepts: [web-servers, apache, nginx, microsoft-iis, linux-servers, server-misconfiguration, server-software-stack]
related: [WAS-C03-016, WAS-C03-001, WAS-C06-005]
time_sensitive: true
---
# Web Servers
(Source: PDF p. 80 from the "Web Servers" heading, plus the top of PDF p. 81 above "Server-Side Databases")

## What the section covers
The layers a server-side application runs on and the three web server software packages the book considers most important: Apache, Nginx and Microsoft IIS.

## The stack
Application logic runs on top of a software-based web server package, so developers do not have to handle requests and process management themselves. The web server runs on an operating system, usually a Linux distribution such as Ubuntu, CentOS or RedHat, which in turn runs on physical hardware in a data center (PDF p. 80).

## The big players
- **Apache.** Serves nearly half of the websites in the world, so by the book's reasoning probably the majority of web applications too. It is open source, has been in development for about 25 years, and runs on nearly every Linux distribution as well as some Windows servers (PDF p. 80). Figure 3-5 (rendered and read) shows the Apache HTTP Server Project page: headings for the number one HTTP server on the internet, a version 2.4.x release dated August 2019, and the end-of-life notice for the 2.2 line dated January 2018. The caption says Apache has been in development since 1995. Apache is valued for its large contributor community, open source nature and being easily configurable and pluggable (PDF p. 80).
- **Nginx** ("Engine X"), Apache's biggest competitor, runs around 30% of web servers and is growing rapidly. It is free to use, but its parent company, F5 Networks at the time of writing, sells support and extra functionality under a "paid+" model (PDF p. 80).
- Nginx is used for high-volume applications with a large number of unique connections rather than a few connections moving a lot of data. Applications serving many simultaneous users may see large performance gains moving from Apache to Nginx, because its architecture has much less overhead per connection (PDF p. 81).
- **Microsoft IIS** comes behind Nginx. Windows-based servers have lost popularity because of expensive licences and poor compatibility with Unix-based open source software. IIS is the right choice with many Microsoft-specific technologies but can burden companies building on open source (PDF p. 81).

## Smaller servers and why it matters
Many smaller web servers exist, each with its own security benefits and downsides. Becoming familiar with the big three helps later, when finding vulnerabilities that stem from improper configuration rather than flaws in application logic (PDF p. 81).

## Time-sensitive statements
The market-share figures (nearly half, around 30%), the 25 years of Apache development, version dates in Figure 3-5 and the F5 Networks ownership of Nginx date from the time of writing.

## Relations
Server software is one layer of the modern stack in WAS-C03-001. Databases, the next layer, are in WAS-C03-016. Detecting a server through headers and default pages is in WAS-C06-005.
