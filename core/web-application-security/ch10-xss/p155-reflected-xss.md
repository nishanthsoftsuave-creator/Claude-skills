---
id: WAS-C10-004
title: Reflected XSS
source_pages: "155-157"
chapter: 10
concepts: [reflected-xss, url-query-parameters, link-distribution, phishing, search-page, detection-evasion]
related: [WAS-C10-003, WAS-C10-005, WAS-C10-002, WAS-C22-001, WAS-C11-001]
time_sensitive: false
---
# Reflected XSS
(Source: PDF pp. 155-157)

## What the section covers
How reflected XSS differs from stored XSS, a step-by-step discovery example on MegaBank's support search page, how a malicious link can be disguised, and the trade-off between stealth and reach.

## Meaning
- The book notes that many resources teach reflected XSS before stored XSS, but considers reflected attacks harder for new hackers to find and use (PDF p. 155).
- Recap of stored XSS from a developer's view: the client sends a resource, the server stores it, and later another user's browser runs the script unknowingly.
- A reflected XSS operates the same way but is not kept in a database and should not regularly reach a server. It affects the client's code directly, without a server relaying a stored message to be rendered (PDF p. 155).
- Figure 10-2 (PDF p. 156) shows the flow: a user creates a malicious link containing a script in its URL, shares it on the web, a second user clicks it and opens the page, and the URL is reflected into the browser DOM, which causes script execution on that user's own device.

## How it is discovered (PDF pp. 156-157)
1. On the support site at the bank's support subdomain, searching for "open savings account" sends the browser to a search URL whose query parameter holds those words. The results page heading says there are three results for that phrase.
2. Changing the parameter to "open checking account" produces a heading with four results for that phrase. So the heading reflects the URL parameter.
3. Remembering the earlier bold-tag trick, the tester puts a bold tag around one word in the URL. The heading comes out bold.
4. The tester then puts a script tag containing an alert call in the query. Loading the URL shows the results but first pops up an alert box with the word "test" (PDF p. 157).

The book concludes this is an XSS vulnerability that is not stored; the server reads the parameter and sends it back to the client.

## Why it matters
- Stored XSS is easy to find because it sits in a database. Reflected XSS is much harder to detect, since these attacks usually target a user directly and are never stored (PDF p. 157).
- The attacker crafts a malicious link and sends it to the chosen victim by email, web advertisements or other means.

## Disguising the link (PDF p. 157)
The book's sample HTML is a fan-site page with three links: sign up, promotions, and a third labelled "Create a New Checking Account". The first two are real; the third points to the search URL carrying the script. Clicking it would show an alert, but a real attacker could instead work silently, for example gathering enough customer data to impersonate the user or finding a checking or routing number if the support portal displays one.

## Limitations and trade-offs
- This particular attack is easy to distribute because it fits in a URL. Most reflected XSS is not that easy and may need extra steps, such as getting the victim to paste JavaScript into a form (PDF p. 157).
- The book's rule of thumb: reflected XSS is much better at avoiding detection but generally harder to spread to many users.

## Relations
Contrast with stored XSS in WAS-C10-003 and with the browser-only variant in WAS-C10-005. The same idea of attacker-controlled URL parameters appears in CSRF in WAS-C11-001. Defenses are in WAS-C22-001.
