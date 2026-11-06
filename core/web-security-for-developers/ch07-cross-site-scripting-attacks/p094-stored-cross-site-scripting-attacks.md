---
id: WS-C07-002
title: Stored Cross-Site Scripting Attacks
source_pages: "94-97"
chapter: 7
concepts: [stored-xss, html-escaping, entity-encoding, template-auto-escaping, content-security-policy, inline-javascript, csp-report-only, defense-in-depth]
related: [WS-C07-001, WS-C07-003, WS-C07-004, WS-C06-002, WS-C07-005]
time_sensitive: true
---
# Stored Cross-Site Scripting Attacks
(Source: PDF pp. 94-97, tail PDF p. 98. The tail page text above the "Reflected Cross-Site Scripting Attacks" heading belongs here; the rest of PDF p. 98 is WS-C07-003.)

## What the section covers
How script planted in a database ends up running in other users' browsers, and the two mitigations: escaping HTML characters and setting a content security policy (PDF pp. 94-98).

## Meaning
- Sites generate HTML from database content: retail sites store product data, social sites store conversations. The server selects content by the URL requested and interpolates it into the page (PDF p. 94).
- Any page content from the database is a possible attack vector. Attackers try to get JavaScript into the database so the server writes it out when rendering. In a stored XSS attack the script is written to the database but executed in the victim's browser when they view the affected page (PDF p. 94).
- Malicious script can be planted through SQL injection (Chapter 6), but more commonly via legitimate features. A comment form is typical: the site stores the comment and shows it to everyone viewing the thread, so a comment containing a script tag is stored and, if the site builds HTML insecurely, written out to other users and executed (PDF p. 94).

## How it works: the example
- The imaginary site is a baking community forum, breddit.com, where users produce most of the content: posts are saved to the database and displayed to others in the thread (PDF p. 94).
- Figure 7-1 shows the attacker posting a comment that consists of a script tag calling the alert function with a silly message about croissants, in a thread titled about how much people like bread, below other users' ordinary comments (PDF p. 94).
- If the site does not escape the injected script when rendering, the next visitor's browser receives the script tag and runs it. Figure 7-2 shows that visitor seeing a browser alert dialog with the croissant message, and the victim reacting with a cartoon "Rude." (PDF p. 95).
- A rogue alert dialog is more annoyance than threat, but attackers often start with it to test whether XSS is possible. If alert() runs, they can escalate to stealing other users' sessions or redirecting victims to harmful sites (PDF p. 95).
- Comments are not the only place. Any user-controlled content is a potential avenue; attackers have injected script tags into usernames, profile pages and online reviews (PDF p. 95).

## Mitigation 1: escape HTML characters
- Escape all dynamic content from a datastore so the browser treats it as the content of tags, not raw HTML. Escaping replaces HTML control characters with their entity encodings (PDF p. 95).
- Table 7-1 lists the mappings: double quote to &quot;, ampersand to &amp;, single quote to &apos;, less-than to &lt;, greater-than to &gt; (PDF p. 96).
- Browsers recognise entity encodings, display them as the visible character, but do not treat them as HTML tags. Listing 7-1 shows the attacker's comment rendered safely: the output contains &lt;script&gt;alert(&quot;HAXXED&quot;)&lt;/script&gt; inside the comment div, so it appears as visible text (PDF p. 96). The listing's bold marking highlights the characters that could have formed HTML tags. As printed, the listing's escaped text uses the message HAXXED, whereas the comment in Figures 7-1 and 7-2 carries the croissant message; the book does not remark on the difference, so it is recorded as printed (PDF pp. 94-96).
- The conversion from entity to character happens after the browser has built the DOM, so the script tag is not executed. Escaping this way closes the door on most XSS attacks (PDF p. 96).
- Modern web frameworks escape dynamic content by default, especially templates that escape interpolated values without being asked. In an Embedded Ruby (ERB) template, the standard interpolation syntax (Listing 7-2) auto-escapes sensitive characters (PDF p. 96).
- To write raw, unescaped HTML in ERB you must explicitly call the raw function (Listing 7-3), which is what makes a template vulnerable (PDF p. 96).
- All secure templating languages share this design: dynamic content is escaped implicitly unless the developer explicitly chooses raw HTML. Understand how escaping works in your templates and check for it in code reviews. In particular, check helper functions or methods that build raw HTML for templates so an attacker cannot abuse their inputs (PDF p. 97).

## Mitigation 2: implement a content security policy
- Modern browsers let a site set a content security policy (CSP) that locks down JavaScript execution. XSS depends on the attacker running script on the victim's page, usually by inserting script tags inside the page's HTML, known as inline JavaScript. The attack in Figure 7-2 uses inline script written as comment text (PDF p. 97).
- Setting a CSP in the HTTP response headers tells the browser never to run inline JavaScript; it runs script only when imported through a src attribute on a script tag (PDF p. 97).
- Listing 7-4 shows a typical header: it allows scripts from the site's own domain ("self") and from one named Google API domain, while inline script is not run (PDF p. 97).

```
Content-Security-Policy: script-src 'self' https://apis.google.com
```

- Listing 7-5 shows the equivalent policy set in a meta tag with http-equiv in the head element of the page (PDF p. 97).
- By whitelisting domains that scripts may load from, you implicitly forbid inline JavaScript. In the example only the named Google domain and the site's own domain (for example breddit.com) may supply script. To allow inline script the policy would have to include the keyword unsafe-inline (PDF p. 97).
- The cost: inline script on your pages must move to separate files referenced by a src attribute. That separation is the preferred practice anyway for an organised codebase, and inline script tags are considered bad practice, so banning them pushes the team toward good habits (PDF pp. 97-98).
- Legacy sites often have many inline tags, and refactoring templates can take time. For this, use CSP violation reporting: with a report-only header carrying a report-uri directive (Listing 7-6, which pairs a script-src of the site's own domain with a report-uri pointing at a reports address on an example domain), the browser notifies you of violations instead of blocking the script. Collecting reports in a log shows which pages must be rewritten to satisfy the proposed policy (PDF p. 98).
- Set a CSP in addition to escaping HTML. An attacker then has to find unescaped content and also smuggle a malicious script onto your whitelisted domains, which is hard. Using multiple layers against the same vulnerability is defense in depth, introduced in Chapter 6 and a recurring theme (PDF p. 98).

## When and how to apply
INTERPRETATION: Roll out CSP in report-only mode first, fix reported pages, then enforce, while keeping auto-escaping templates as the primary control.

## Relations
SQL injection as a route into the database is in WS-C06-002. Reflected and DOM-based variants follow in WS-C07-003 and WS-C07-004; the chapter recap is WS-C07-005.

## Time-sensitive statements
- Example site breddit.com and the Google API domain in the CSP listings are illustrative; CSP syntax and directive support such as report-uri reflect the browser features at the time of the book (PDF pp. 97-98).
