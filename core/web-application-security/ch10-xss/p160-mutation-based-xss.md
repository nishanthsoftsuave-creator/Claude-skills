---
id: WAS-C10-006
title: Mutation-Based XSS
source_pages: "160-161"
chapter: 10
concepts: [mxss, mutation-xss, dompurify, innerhtml, sanitizer-bypass, template-element, noscript, browser-parsing]
related: [WAS-C10-005, WAS-C10-007, WAS-C22-001]
time_sensitive: true
---
# Mutation-Based XSS
(Source: PDF pp. 160-161)

## What the section covers
What mutation-based XSS (mXSS) is, why it defeats well-built filters, and a 2019 case that bypassed a sanitizing library used by a major Google product.

## Meaning
- The author names his friend and colleague Mario Heiderich as the writer of a paper on attacking well-secured web applications through innerHTML mutations, which the book calls one of the first introductions to this classification (PDF p. 160).
- mXSS attacks are possible against all major browsers. They depend on a deep understanding of how a browser optimises and applies conditions when it renders DOM nodes (PDF p. 160).
- At its core, an mXSS payload looks safe to a filter but mutates into an unsafe one after it has passed the filter (PDF pp. 160-161).
- A note on the page says that, just as mXSS was once little known, future technologies may also prove vulnerable. XSS-style attacks can target any client-side display technology, and desktop and mobile technologies could be affected as well (PDF p. 160).

## Why it matters
Although new and often misunderstood, mXSS has been used to get past most strong XSS filters. The book names DOMPurify, OWASP AntiSamy and Google Caja as tools that have been bypassed, and says many major applications, in particular email clients, have been found vulnerable (PDF p. 160).

## How the 2019 case worked (PDF p. 161)
1. In early 2019 the researcher Masato Kinugawa found an mXSS in Google's Closure library, which was used inside Google Search.
2. Closure used DOMPurify, running in the browser, to read a string and filter possible XSS before the string was put into the page via innerHTML. The book calls client-side filtering the most effective approach for innerHTML strings, because browsers and versions vary, so server-side filtering would be less effective. Google expected a filter that worked across old and new browsers.
3. The payload was a short string that opens a noscript element, then a paragraph whose title attribute starts a quote that contains the closing noscript tag and then an image element with a failing source and an error handler that raises an alert.
4. Appended literally, the string should be harmless because the tags and quotes are arranged so no script runs. DOMPurify therefore let it pass.
5. When the same string was loaded in a real browser DOM, optimisations rearranged it so the image element, with its error handler, appeared as a live element.

## Why the mutation happened
DOMPurify uses a template element as its root during sanitising. A template is parsed but not rendered, and element scripting is disabled inside it. With scripting disabled, the noscript tag represents its child elements; with scripting enabled it does nothing. So inside the sanitizer the image's error handler could not run, but in a real browser the paragraph's opening piece was ignored and the image handler became valid (PDF p. 161).

## Takeaway
Browser DOM elements often act conditionally depending on their parents, children and siblings. A hacker can use this to build payloads that are not valid script at filter time but become valid script when the browser runs them (PDF p. 161).

## Continuation
The section continues on the next page with a short closing paragraph saying mXSS is very new and often misunderstood in the industry, that many proof-of-concept exploits exist online and more are likely, and that mXSS is probably here to stay. That page also holds the chapter summary (WAS-C10-007).

## Time-sensitive statements
The 2019 discovery, the named libraries (DOMPurify, AntiSamy, Caja, Closure) and their bypassed status reflect the time of writing.

## Relations
Follows DOM-based XSS (WAS-C10-005). Defensive sanitising and its limits are in WAS-C22-001. The chapter closes in WAS-C10-007.
