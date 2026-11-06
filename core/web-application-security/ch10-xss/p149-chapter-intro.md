---
id: WAS-C10-001
title: Cross-Site Scripting - Chapter Introduction
source_pages: "149"
chapter: 10
concepts: [xss, cross-site-scripting, stored-xss, reflected-xss, dom-based-xss, script-execution, owasp]
related: [WAS-C10-002, WAS-C10-003, WAS-C10-004, WAS-C10-005, WAS-C22-001]
time_sensitive: false
---
# Cross-Site Scripting - Chapter Introduction
(Source: PDF p. 149)

## What the section covers
The opening page of the chapter on Cross-Site Scripting (XSS). It states why XSS is so widespread, what the core mechanism is, and which three categories the rest of the chapter develops (PDF p. 149).

## Meaning
- XSS is among the most common vulnerability types found across the internet. The book ties its spread directly to the growth of user interaction in modern web applications (PDF p. 149).
- At its core, an XSS attack works because web applications run scripts inside users' browsers. Any script that is built dynamically before execution is a risk if someone can contaminate or modify it, and the book singles out end users as the party who may do so (PDF p. 149).
- The book's chapter text spells the abbreviation "XXS" once when it introduces the categories; the rest of the chapter, and the title, use the standard "XSS".

## The three main categories
The chapter groups XSS attacks into three families (PDF p. 149):
- Stored: the attacking code is kept in a database before it is run.
- Reflected: the code is not kept in a database; a server bounces it back to the requester.
- DOM-based: the code is both held and executed inside the browser.

The book acknowledges that other classifications exist, but says these three cover what most modern web applications need to watch for on a regular basis. It also notes that committees such as the Open Web Application Security Project (OWASP) have named them the most common XSS attack vectors on the web (PDF p. 149).

## How the chapter proceeds
Before treating each category separately, the chapter first shows how an XSS attack can be produced and how the bug that enables it can be found (PDF p. 149). That walkthrough is in the next section (see WAS-C10-002).

## Relations
The discovery walkthrough follows in WAS-C10-002, and the three categories are then treated in WAS-C10-003 (stored), WAS-C10-004 (reflected) and WAS-C10-005 (DOM-based). Defenses against XSS are covered in the defense part of the book, beginning at WAS-C22-001.
