---
id: WAS-C03-001
title: Modern Versus Legacy Web Applications
source_pages: "59-60"
chapter: 3
concepts: [modern-web-applications, legacy-web-applications, ajax, rest-api, spa, web-technology-stack, attack-surface, recon-prerequisites]
related: [WAS-C03-002, WAS-C03-011, WAS-C03-015, WAS-C03-016, WAS-C02-002]
time_sensitive: true
---
# Modern Versus Legacy Web Applications
(Source: PDF pp. 59-60, plus the top of PDF p. 61 before the "REST APIs" heading)

## What the section covers
The opening of Chapter 3, "The Structure of a Modern Web Application". It explains why a tester or defender should first know the technologies that most web applications share, contrasts how applications were built about a decade ago with how they are built now, and lists the technologies a typical modern application combines.

## Why the chapter exists
- Before evaluating an application for recon, it helps to understand the technologies many applications share as dependencies. These range from JavaScript helper libraries and predefined CSS modules all the way down to web servers and operating systems (PDF p. 59).
- Knowing what each dependency does and how it is usually deployed makes it much quicker to identify the dependency in a target and to look for misconfigurations (PDF p. 59).

## Legacy versus modern architecture
- Roughly ten years before the book, most web applications were produced by server-side frameworks. The server rendered a page of HTML, JavaScript and CSS and sent it to the client. When the client needed an update it simply asked the server for another rendered page, delivered over HTTP (PDF p. 59).
- Shortly afterwards, Ajax (asynchronous JavaScript and XML) arrived. It let JavaScript make network requests from inside an existing page session, so HTTP was used more often and more flexibly (PDF p. 59).
- Today a "web application" is frequently better described as two or more applications that talk to each other over a network protocol, not one monolithic program. The book names this as a major architectural difference from a decade earlier (PDF p. 59).
- The pieces are often joined by a REST API (Representational State Transfer). Such APIs are stateless and exist only to satisfy requests from one application to another, so they keep no information about who is asking (PDF p. 60).
- Client (user interface) applications now run in the browser in a way that resembles a desktop program. They manage their own life-cycle loops, request their own data, and need no page reload once the initial bootstrap has finished (PDF p. 60).
- A standalone browser application may talk to several servers. The book's illustration is an image-hosting application with one specialised hosting and distribution server at one URL and a separate URL that manages the database and logins (PDF p. 60).
- The book credits this "many separate but symbiotic applications" shape to better defined network protocols and API architecture patterns (PDF p. 60).

## The typical modern technology list (PDF p. 60)
The average modern application probably uses several of these:
- a REST API;
- JSON or XML as the data format;
- JavaScript;
- an SPA (single-page application) framework such as React, Vue, EmberJS or AngularJS;
- an authentication and authorization system;
- one or more web servers, typically on Linux;
- one or more web server software packages (ExpressJS, Apache, Nginx);
- one or more databases (MySQL, MongoDB and similar);
- a local data store on the client (cookies, web storage, IndexedDB).

A note on the page says the list is not exhaustive. With billions of websites it is not feasible to cover every technology, and the reader is pointed to other books and sites such as Stack Overflow for any technology not covered (PDF p. 60).

## What changed in those technologies (continuation on the next page)
The page after this range continues the discussion without a heading change. Some listed technologies existed ten years earlier but have changed. NoSQL databases and client-side databases are recent. Full stack JavaScript applications only became possible once NodeJS and npm were widely adopted. The author also looks ahead to the Cache API for storing requests locally, Web Sockets as an alternative client-to-server (or client-to-client) protocol, and WebAssembly, which would let non-JavaScript languages run in the browser. Each new technology brings new security holes to find and exploit "for good or for evil", and the rest of the chapter introduces the listed technologies, so readers can focus on the ones they do not yet know (PDF p. 61).

## When and how to apply
INTERPRETATION: when mapping a target, use the list above as a checklist of layers to look for (data format, framework, auth system, web server, database, client storage) and note the answer for each in the recon map.

## Limitations
The list is a sample, not a catalogue, and the author states the book cannot cover all web technologies.

## Relations
The next section details REST, the first listed technology (WAS-C03-002). SPA frameworks, web servers, databases and client stores each get their own later section (WAS-C03-011, WAS-C03-015, WAS-C03-016, WAS-C03-017). The recon idea of mapping an application is in WAS-C02-002.

## Time-sensitive statements
The named frameworks and servers, the "ten years ago" comparison, and the technologies described as upcoming (Cache API, Web Sockets, WebAssembly) reflect the time of writing (2019-2020).
