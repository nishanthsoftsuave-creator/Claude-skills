---
id: WS-I-004
title: What's in This Book
source_pages: "25-28"
chapter: intro
concepts: [book-structure, chapter-overview, part-one-fundamentals, part-two-vulnerabilities, injection, xss, csrf, authentication, session-hijacking, encryption, denial-of-service]
related: [WS-I-003, WS-C01-001, WS-C02-001, WS-C03-001]
time_sensitive: false
---
# What's in This Book
(Source: PDF pp. 25-28. Text is on PDF pp. 25-27; PDF p. 28 holds no text in the extraction. The text at the top of PDF p. 25 under "What to Worry About First" belongs to WS-I-003; this section starts at its own heading.)

## What the section covers
The book's layout: two parts and eighteen chapters, each introduced with a short summary of its purpose.

## Structure
Part I covers how the internet works. Part II covers the specific vulnerabilities to guard against (PDF p. 25).

## Part I chapters
- Chapter 1, Let's Hack a Website: shows how easy hacking a site is, hence the author's quip that you did well to buy the book (PDF p. 25).
- Chapter 2, How the Internet Works: the Internet Protocol suite, with a review of TCP, IP addresses, domain names and HTTP, and how data can be passed securely (PDF p. 25).
- Chapter 3, How Browsers Work: users reach your site via the browser, where many vulnerabilities show up. Covers page rendering and how JavaScript runs under the browser security model (PDF p. 25).
- Chapter 4, How Web Servers Work: most of your code runs on a server, a primary hacker target. Covers static content, dynamic content from templates and databases, and a look at major web programming languages with their security considerations (PDF p. 25).
- Chapter 5, How Programmers Work: how to approach writing website code and the habits that reduce bugs and vulnerabilities (PDF p. 25).

## Part II chapters
- Chapter 6, Injection Attacks: a hacker injecting code that runs on your server, often where code meets a SQL database or the operating system, or as remote code in the server process. Also how file upload features can let attackers inject malicious scripts (PDF p. 26).
- Chapter 7, Cross-Site Scripting Attacks: smuggling malicious JavaScript into the browser. There are three methods, stored, reflected and DOM-based, and the chapter shows how to defend each (PDF p. 26).
- Chapter 8, Cross-Site Request Forgery Attacks: tricking users into undesired actions; a common nuisance that you must protect users from (PDF p. 26).
- Chapter 9, Compromising Authentication: treating user accounts securely; ways attackers get past login, from brute-force password guessing to user enumeration, and how to store credentials safely (PDF p. 26).
- Chapter 10, Session Hijacking: accounts taken over after login; building the site and handling cookies securely to reduce this (PDF p. 26).
- Chapter 11, Permissions: stopping privilege escalation into forbidden areas; if URLs reference files, attackers will try directory traversal across the filesystem (PDF p. 26).
- Chapter 12, Information Leaks: you may be advertising weaknesses by leaking information, and this chapter explains how to stop it (PDF p. 26).
- Chapter 13, Encryption: using encryption correctly and why it matters, with some light mathematics (PDF p. 26).
- Chapter 14, Third-Party Code: managing vulnerabilities in other people's code, since most code you run is written by someone else (PDF p. 27).
- Chapter 15, XML Attacks: web servers probably parse XML, which has been a consistently popular attack vector for a couple of decades (PDF p. 27).
- Chapter 16, Don't Be an Accessory: you could be unwittingly helping attacks on others; close these loopholes to be a good internet citizen (PDF p. 27).
- Chapter 17, Denial-of-Service Attacks: how huge volumes of traffic can take a site offline (PDF p. 27).
- Chapter 18, Summing Up: a cheat sheet of the key security elements and the high-level principles of a security-minded approach (PDF p. 27).

## When and how to apply
INTERPRETATION: Use this list as a lookup table from a threat you are worried about to the chapter that covers it; the later WS- chapter modules follow these same chapter numbers.

## Relations
Follows the history in WS-I-003. Chapters 1, 2 and 3 are expanded in WS-C01-001, WS-C02-001 and WS-C03-001.
