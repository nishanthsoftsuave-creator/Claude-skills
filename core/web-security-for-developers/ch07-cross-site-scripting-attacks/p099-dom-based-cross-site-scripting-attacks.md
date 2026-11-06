---
id: WS-C07-004
title: DOM-Based Cross-Site Scripting Attacks
source_pages: "99-100"
chapter: 7
concepts: [dom-based-xss, uri-fragment, single-page-app, url-structure, client-side-escaping, react-dangerouslysetinnerhtml, server-logs]
related: [WS-C07-002, WS-C07-003, WS-C07-005]
time_sensitive: true
---
# DOM-Based Cross-Site Scripting Attacks
(Source: PDF pp. 99-100, tail PDF p. 101. The text on PDF p. 99 above the "DOM-Based Cross-Site Scripting Attacks" heading belongs to WS-C07-003. On PDF p. 101 the text above the "Summary" heading belongs here; the Summary is WS-C07-005.)

## What the section covers
How script can be smuggled into a page through the URI fragment and run entirely client-side, why server defences cannot stop it, and how to mitigate it in client code and frameworks (PDF pp. 99-101).

## Meaning
- Most XSS defence means inspecting and securing server-side code. The rise of rich client-side frameworks has produced DOM-based XSS, in which attackers sneak malicious JavaScript into a user's page through the URI fragment (PDF p. 99).

## How it works: URLs and URI fragments
- A URL (universal resource locator) is the address in the browser bar. Figure 7-3 labels the parts of a typical URL with a protocol (https), a domain, a path, a query string beginning after a question mark, and a URI fragment beginning after the hash sign. The sample is a glossary page on hacksplaining.com with ref and top parameters and the fragment "details" (PDF p. 99).
- The URI fragment is the optional part after the # sign. Browsers use it for in-page navigation: if a tag on the page has an id matching the fragment, the browser scrolls to it after loading. Loading the Wikipedia cat article with the fragment Grooming opens the page and scrolls to the Grooming section, because the heading tag carries that id (Listing 7-7). This lets users link directly to page sections (PDF p. 100).
- Single-page apps, written in frameworks such as Angular, Vue.js and React, are JavaScript-heavy pages that try to avoid the rendering blink of a page reload. One way is to load the whole app under a static URL that never changes, since a changed URL normally causes a reload. But refreshing at an unchanging URL resets the page and loses the user's state (PDF p. 100).
- Many single-page apps therefore store state in the URI fragment, surviving refreshes. For instance, with infinite scrolling, where images load as the user scrolls, the fragment records how far the user has scrolled, and after a refresh the JavaScript reads the fragment and loads that many images (PDF p. 100).
- By design, browsers do not send the fragment to the server. The browser notes the fragment, strips it from the URL and sends the stripped URL. JavaScript on the page can read it, and the full URL goes into browser history or a bookmark (PDF p. 100).
- Consequently server-side code never sees fragments, so securing server code cannot stop DOM-based XSS. Client-side code that interprets fragments must treat them carefully: if the content is written unescaped into the page DOM, an attacker can smuggle script through this channel. They craft a URL with script in the fragment and trick a user into visiting it (PDF p. 100).

## Why it matters
- DOM-based XSS is described as relatively new and particularly dangerous: the injection happens wholly on the client, so it cannot be detected by examining web server logs. Be keenly aware of it in code reviews (PDF p. 101).

## Mitigation: escape dynamic content from URI fragments
- Any in-browser JavaScript that takes part of the fragment and builds HTML is prone to the attack. Escape whatever comes from the fragment before interpolating it into HTML in client-side code, just as on the server (PDF p. 101).
- Authors of modern JavaScript templating frameworks know the risk and discourage building raw HTML. In React, writing unescaped HTML requires calling dangerouslySetInnerHTML (Listing 7-8), so the unsafe choice is explicit (PDF p. 101).
- If client-side JavaScript is complex, consider moving to a modern framework: it should make the codebase more manageable and security considerations more apparent. As always, set an appropriate content security policy (PDF p. 101).

## Relations
Escaping and CSP are the same defences as in WS-C07-002 and WS-C07-003. The chapter recap is WS-C07-005.

## Time-sensitive statements
- Frameworks named: Angular, Vue.js, React (PDF p. 100); the book calls DOM-based XSS relatively new.
