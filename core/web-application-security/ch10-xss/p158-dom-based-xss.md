---
id: WAS-C10-005
title: DOM-Based XSS
source_pages: "158-159"
chapter: 10
concepts: [dom-xss, client-side-xss, sources-and-sinks, location-hash, document-write, static-analysis-limits, browser-differences]
related: [WAS-C10-004, WAS-C10-006, WAS-C03-010, WAS-C22-001]
time_sensitive: true
---
# DOM-Based XSS
(Source: PDF pp. 158-159, plus the part of PDF p. 160 above the next heading)

## What the section covers
What a DOM-based XSS is, why it needs both a source and a sink, why scanners miss it, and an investment-portal example where a URL hash feeds a page-writing call.

## Meaning
- DOM-based XSS can be either reflected or stored, but it works through browser DOM sinks and sources. Because browsers implement the DOM differently, some are vulnerable and others are not (PDF p. 158).
- It is far harder to find and use than the other forms, because it demands deep knowledge of the browser DOM and JavaScript (PDF p. 158).
- Its main difference from other forms is that it never needs any interaction with a server. For that reason some people are moving to call it a subset of a category named client-side XSS (PDF p. 158).
- A source is a DOM object that can hold text; a sink is a DOM API that can run script held as text. Both must be present in the browser (PDF p. 158).
- Figure 10-3 shows the sequence: a page lets the user switch filters kept in the location hash; the DOM is rebuilt with the DOM parser's parseFromString call and the result, with a title showing the chosen filter, is appended to the body; the user manually edits the hash to include script; a new script node is created and added with the new body; the script node runs as it loads.

## Why it matters
- Since a server is never touched, it is almost impossible to spot with static analysis tools or other popular scanners (PDF p. 158).
- It is also hard to handle because of how many browsers exist. A bug in one browser's DOM may not be present in another, and an older browser version might be vulnerable where a current one is not. Without enough browser and operating system detail, a company may struggle to reproduce a report. JavaScript and the DOM follow open specifications (TC39 and WhatWG), but implementations differ by browser and often by device (PDF p. 159).

## Example setting (PDF p. 159)
- MegaBank has an investor portal for its 401(k) management service, with a listing page of available funds and a left-hand menu for searching and filtering.
- Searching and sorting happen on the client because the number of funds is small. Searching for "oil" changes the URL to a listing address with a search parameter; filtering for "usa" gives an address ending with a hash and scrolls to US funds.
- A changing URL does not always mean a server request, which is common in apps with their own JavaScript routers because it gives a better user experience.
- Typing a malicious search on this site shows nothing odd by itself. But search parameters are a possible source, available in all major browsers through the location object's search property, and the hash is available through its hash property. A dangerous value in either does nothing unless other code uses it in a way that executes script, hence the need for source plus sink.

## The vulnerable code (PDF p. 159 and the part of PDF p. 160 above the next heading)
The imagined page code reads the hash, calls a helper that counts matching funds, and then writes a sentence containing the match count and the raw hash into the document with document.write. A link ending with a hash that holds a script tag calling an alert on the cookies would then run when written, showing the session cookies; the same route could do far more harm, as earlier examples showed.

## Takeaways
- No server was needed, yet both a source (the hash) and a sink (document.write) were required. The book adds that the same result could come through many other sinks, some needing more or less effort than others.
- A legitimate string would never cause trouble, so the flaw can stay undetected for a very long time (PDF p. 160).

## Time-sensitive statements
The comparison of a 2015 browser with a modern one is illustrative; which browsers are affected changes over time.

## Relations
Compare with reflected XSS (WAS-C10-004). The next variant, which exploits DOM mutation, is WAS-C10-006. The browser DOM is introduced in WAS-C03-010. Defenses, including naming the sinks to avoid, are in WAS-C22-001.
