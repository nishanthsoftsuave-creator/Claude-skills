---
id: WS-C07-003
title: Reflected Cross-Site Scripting Attacks
source_pages: "98"
chapter: 7
concepts: [reflected-xss, http-request-reflection, query-string, search-pages, error-pages, escaping-dynamic-content, code-review]
related: [WS-C07-002, WS-C07-004, WS-C07-005]
time_sensitive: true
---
# Reflected Cross-Site Scripting Attacks
(Source: PDF p. 98, tail PDF p. 99. The text at the top of PDF p. 98 above the "Reflected Cross-Site Scripting Attacks" heading is the end of WS-C07-002. On PDF p. 99 the text above the "DOM-Based Cross-Site Scripting Attacks" heading belongs here.)

## What the section covers
XSS in which the malicious script travels in the HTTP request and is echoed back by the server, a real-world illustration with Google, and the mitigation: escape dynamic content from requests exactly as for database content (PDF pp. 98-99).

## Meaning
- Script in the database is not the only route. If a site takes part of an HTTP request and shows it in the rendered page, the rendering code must guard against script smuggled in through the request. That is a reflected XSS attack (PDF p. 98).
- Virtually every site displays some part of a request in its pages (PDF p. 98).

## How it works: the Google search illustration
- A Google search for "cats" puts the term in the URL query string, and the term appears in the search box above the results (PDF p. 98).
- If Google were less secure, an attacker could replace the search term in the URL with malicious JavaScript, and it would run whenever anybody opened the URL. They could email the URL as a link or trick someone into visiting it by posting it in a comment. Essence: the attacker sends malicious code in the HTTP request and the server reflects it back (PDF p. 98).
- Google employs many security experts, so inserting script tags into its search results does not run them. Even so, hackers have found reflected XSS flaws in the Google Apps admin interface, which shows that big companies get caught too. To keep users safe you must protect against this vector (PDF pp. 98-99).

## Mitigation: escape dynamic content from HTTP requests
- Mitigate it the same way as stored XSS: escape control characters in any dynamic content interpolated into HTML. Whether the content comes from the database or the request, escape it the same way (PDF p. 99).
- Template languages typically escape every interpolated variable regardless of whether it came from the database or the request. The team must still keep the request-injection risk in mind when auditing code. Reviews often miss reflected XSS because reviewers are busy looking for stored XSS (PDF p. 99).
- Common targets are search pages and error pages, which usually show parts of the query string back to the user. Make sure the team knows the risk and how to spot it in code changes (PDF p. 99).

## Alternatives and trade-offs: stored versus reflected
Stored XSS tends to do more harm, since one piece of script in a database table can attack users repeatedly. Reflected attacks are more common because they are easier to carry out (PDF p. 99).

## Relations
Same escaping defence as WS-C07-002. The chapter then turns to a third variant, DOM-based XSS, in WS-C07-004 (the closing sentence of this section on PDF p. 99 introduces it).

## Time-sensitive statements
- The Google search page and the past reflected XSS flaws in the Google Apps admin interface are examples from the time of writing (PDF pp. 98-99).
