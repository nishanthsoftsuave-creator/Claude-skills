---
id: WAS-C07-001
title: Identifying Weak Points in Application Architecture - Chapter Introduction
source_pages: "131"
chapter: 7
concepts: [recon-notes, documentation, application-architecture, prioritization, attack-planning, vulnerability-sources]
related: [WAS-C02-002, WAS-C07-002, WAS-C07-005]
time_sensitive: false
---
# Identifying Weak Points in Application Architecture - Chapter Introduction
(Source: PDF p. 131; the introduction continues onto the next page)

## What the section covers
How the separate recon techniques of Part I are combined into one organised set of notes, and what those notes should hold, as the basis for finding architectural weak points.

## Meaning
- Earlier chapters showed how to identify the components of a web application, work out the shape of its APIs, and learn how it expects to interact with a browser. Each technique is useful alone, but more value comes when the findings are combined in an organised way (PDF p. 131).

## Why it matters
- Some applications are so large that exploring all their functionality could take months, so proper documentation of your research is described as integral (PDF p. 131).
- How much you document is up to you, whether you are a tester, hacker, hobbyist or engineer. More is not always more useful if it is not prioritised, but the book still says more data beats none (PDF p. 131).

## How it works: what the notes should cover
The page lists the content of a well-organised set of notes (PDF p. 131):
- technology used in the web application;
- API endpoints grouped by HTTP verb;
- endpoint shapes, where available;
- functionality, such as comments, authentication and notifications;
- domains used by the application;
- configurations found, for example a Content Security Policy.
The list continues on the next page with authentication and session management systems.

## When and how to apply
The next page goes on to say that the finished list is used to prioritise attacks or the search for vulnerabilities. It then claims that most vulnerabilities come from badly designed architecture rather than badly written individual methods, which leads straight into the first section of this chapter. The book backs this with a comparison: some applications have dozens of XSS vulnerabilities while similarly sized applications in the same industry have nearly none, so the architecture of an application and of the modules and dependencies inside it marks where vulnerabilities are likely to appear. These points are printed on the following page, so the introduction simply continues there.

## Relations
The mapping habit starts in WAS-C02-002. The chapter's first section is WAS-C07-002, and the chapter closes in WAS-C07-005.
