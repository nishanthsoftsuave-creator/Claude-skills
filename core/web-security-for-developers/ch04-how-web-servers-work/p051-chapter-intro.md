---
id: WS-C04-001
title: How Web Servers Work - Chapter Introduction
source_pages: "51"
chapter: 4
concepts: [web-server, http-request, dynamic-content, html-generation, database-backed-pages, server-side-code, chapter-scope]
related: [WS-C03-001, WS-C04-002, WS-C04-005, WS-C05-001]
time_sensitive: false
---
# How Web Servers Work - Chapter Introduction
(Source: PDF p. 51)

## What the section covers
The opening framing of Chapter 4: how it follows from the browser chapter, what a web server is at its simplest and in modern practice, and what the chapter will cover (PDF p. 51). The chapter-opening page also carries a chapter-number and title graphic, which holds no further content.

## Meaning
- Chapter 3 explained how browsers talk over the internet and render HTML pages and other resources. Chapter 4 turns to the other side: how those same HTML pages are built by web servers (PDF p. 51).
- Simplest definition: a web server is a computer program that returns HTML pages in answer to HTTP requests (PDF p. 51).
- Modern web servers do far more than that definition suggests. When a browser sends an HTTP request, the server can run code that generates the page HTML on the fly, and that code frequently pulls in content from a database (PDF p. 51).

## Why it matters
Writing and testing this kind of server-side code is where a web developer spends most of their time (PDF p. 51). INTERPRETATION: this is why the chapter's security focus is placed on server-side code.

## What the chapter promises
- How developers organise code and resources inside a web server (PDF p. 51).
- The common weak points in web servers that let security vulnerabilities occur, and how to avoid those pitfalls (PDF p. 51).

## Relations
Builds on the browser material in WS-C03-001. The two kinds of content the chapter then sets out are defined in WS-C04-002, and the chapter is recapped in WS-C04-005. The following chapter, WS-C05-001, moves from servers to the development process.
