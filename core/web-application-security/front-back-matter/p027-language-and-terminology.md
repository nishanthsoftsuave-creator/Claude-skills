---
id: WAS-P-006
title: Preface - Language and Terminology
source_pages: "27-29"
chapter: preface
concepts: [terminology, glossary, occupations, white-hat, black-hat, red-team, blue-team, acronyms, vulnerability, exploit, payload]
related: [WAS-P-005, WAS-P-007]
time_sensitive: false
---
# Preface - Language and Terminology
(Source: PDF pp. 27-29, with the end of the acronym table on PDF p. 30)

## What the section covers
The shared vocabulary the book relies on, presented as three tables: occupations (P-1), general terms (P-2) and acronyms (P-3).

## Why it exists
The skills taught are rare and valuable but hard to learn, needing focus, aptitude and a new mental model for web applications. The author sets common language so the book and the reader's own communication stay consistent across security and engineering organisations. Each new term is explained when introduced and acronyms are spelled out first, as with Cross-Site Scripting (XSS). Readers meeting an unfamiliar term are told to return to this section (PDF p. 27).

## Table P-1: occupations (PDF p. 28)
- Hacker: breaks into systems, typically to steal data or make the system behave in ways its developers did not intend.
- White hat ("ethical hacker"): uses hacking techniques to help organisations improve security.
- Black hat: the archetypal hacker, breaking in for profit, chaos or personal goals.
- Grey hat: between the two; may break laws, such as attacking without permission, but usually for discovery or recognition rather than profit or chaos.
- Penetration tester: paid to break into systems like a hacker would, reporting bugs and oversights so the owner can fix them before a malicious hacker finds them.
- Bug bounty hunter: a freelance penetration tester. Large companies run responsible disclosure programs that award cash for reported holes, and some hunters work full time though many take part outside their jobs.
- Application (product) security engineer: a software engineer who evaluates and improves an organisation's codebase and application architecture.
- Software security engineer: builds security-related products without necessarily owning security evaluation for the wider organisation.
- Admin (sys admin): technical staff who maintain the configuration and uptime of a web server or application.
- Scrum master: leadership role that helps an engineering team plan and execute work.
- Security champion: a software engineer outside any security organisation, with no security duties, who is interested in improving the organisation's code security.

## Table P-2: terms (PDF pp. 28-29)
- Vulnerability: a software bug, often from an oversight or from unexpected behaviour when modules are joined, that lets a hacker perform unintended actions (PDF p. 28).
- Threat vector or attack vector: a subset of application functionality that a hacker judges to be written insecurely and thus a good target (PDF p. 28).
- Attack surface: as the book prints it, a list of vulnerabilities in an application that a hacker builds when deciding how to attack it (PDF p. 28).
- Exploit: usually a block of code or list of commands used to take advantage of a vulnerability (PDF p. 28).
- Payload: an exploit formatted so it can be sent to a server, often just packaging the exploit into the right network format (PDF p. 28).
- Red team: often penetration testers plus network and software security engineers who attack a company's software to see how it holds up against real hackers (PDF p. 29).
- Blue team: software and network security engineers who improve a company's security, often using red-team feedback to prioritise (PDF p. 29).
- Purple team: does both red and blue work; a general-purpose team that is harder to staff because of the wide skills required (PDF p. 29).
- Website: information documents reachable over the internet, typically via HTTP (PDF p. 29).
- Web application: a desktop-like application delivered over the internet and run in a browser. It differs from a traditional website by having many permission levels, storing user input in databases and often letting users share content (PDF p. 29).
- Hybrid application: a mobile app built on web technology, usually with a library such as Apache Cordova sharing native functionality with the web app on top (PDF p. 29).

## Table P-3: acronyms (PDF pp. 29-30)
- API: functions a code module exposes for other code; in this book usually functions exposed over HTTP that a browser calls on a server (PDF p. 29).
- CSRF: Cross-Site Request Forgery, using a privileged user's permissions to make requests against a server (PDF p. 29).
- CSS: Cascading Style Sheets, styling used with HTML (PDF p. 29).
- DDoS: distributed denial of service, a DoS at scale by many computers at once (PDF p. 29).
- DOM: Document Object Model, an API in every browser that organises HTML and offers history, cookie and URL APIs (PDF p. 29).
- DoS: denial of service, which aims not at stealing data but at consuming server or client resources so the experience degrades or stops (PDF p. 29).
- HTML, HTTP, HTTPS (HTTP over TLS or SSL) and JSON (lightweight hierarchical data format widely used between browser and server) (PDF p. 29).
- OOP: object-oriented programming. OSS: open source software, usually under licences like MIT, Apache, GNU or BSD (PDF p. 29).
- REST: an architecture for stateless APIs that define endpoints as resources rather than functional units; any data format is allowed but JSON is typical (PDF p. 30).
- RTC: real time communication, a newer protocol letting browsers talk to each other and to servers (PDF p. 30).
- SOAP: Simple Object Access Protocol, for function-driven APIs with strict schemas and XML only (PDF p. 30).
- SOP: Same Origin Policy, a browser policy that stops content from one origin loading in another (PDF p. 30).
- SPA: single-page application, a site that manages its own UI and state like a desktop application (PDF p. 30).
- SSDL: secure software development life cycle, a framework for engineers and security engineers to write more secure code (PDF p. 30).
- SSL and TLS: cryptographic protocols securing data in transit; TLS replaced the now deprecated SSL (PDF p. 30).
- VCS: version control system, managing additions and removals in a codebase and sometimes dependencies and collaboration (PDF p. 30).
- XML: strict-rule hierarchical data format, heavier than JSON but more configurable. XSS forces another client, often a browser, to run a hacker's code. XXE abuses a misconfigured XML parser to steal local server files or include malicious files from another server (PDF p. 30).

## Relations
The roles named here are the audience in WAS-P-004 and the structure that uses the vocabulary is WAS-P-005. The preface wrap-up is WAS-P-007.
