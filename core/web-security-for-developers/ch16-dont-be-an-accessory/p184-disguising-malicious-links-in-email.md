---
id: WS-C16-003
title: Disguising Malicious Links in Email
source_pages: "184-185"
chapter: 16
concepts: [malicious-links, url-shortener, open-redirect, redirect-parameter, relative-url, safe-browsing, blacklist, login-redirect]
related: [WS-C16-002, WS-C16-004, WS-C09-005, WS-C18-001]
time_sensitive: true
---
# Disguising Malicious Links in Email
(Source: PDF pp. 184-185, tail PDF p. 186. The text at the top of PDF p. 184 above the "Disguising Malicious Links in Email" heading belongs to WS-C16-002. The text on PDF p. 186 above the "Clickjacking" heading, the "Other Considerations" paragraph, is the end of this section and is covered here.)

## What the section covers
How scammers hide harmful links, why an open redirect on your site helps them, how to prevent open redirects, and what to do if users must post external links.

## Meaning
- Spam filters look for malicious links, and webmail providers keep current blacklists of known harmful domains. Scanning for such links is a common and effective way to stop dangerous mail (PDF p. 184).
- Scammers therefore disguise links. One method is a URL-shortening service such as Bitly. Filters have caught up and now unroll links from known shorteners and check the final destination (PDF p. 184).
- A subtler method abuses your own site. If any page can send visitors to an arbitrary URL, an open redirect, it works like a URL shortener. Your users become exposed to phishing, and your genuine email may be blacklisted by spam detection (PDF p. 184).
- A redirect is an HTTP response with status 301 or 302 plus a URL the browser should visit instead. The book glosses 301 as a temporary redirect and 302 as permanent; recorded as printed (PDF p. 185). SUPPLEMENTARY: in the HTTP standard (RFC 9110) 301 means moved permanently and 302 means found (temporary), so the book's glosses are reversed; this does not affect the open-redirect advice.
- A very common use: sending an unauthenticated visitor to the login page, then issuing a second redirect back to the original URL after login. The server must remember the destination, often by encoding it in a query parameter of the login URL. If an attacker can place an arbitrary URL in that parameter, so that the second redirect can send a user to any other website, you have an open redirect (PDF p. 185).

## How it works: preventing open redirects (PDF p. 185)
- Most sites never need to redirect to an external address. Wherever your code encodes one URL inside another to redirect, make sure the embedded URL is relative (stays within your site) rather than absolute.
- Relative URLs begin with a forward slash, which is easy to test. Attackers have found ways to dress absolute URLs up as relative ones, so the check must account for that.
- Listing 16-3 is a Python function using a regular expression:

```python
import re
def is_relative(url):
  return re.match(r"^\/[^\/\\]", url)
```

  The pattern demands a leading forward slash and that the second character be neither a forward slash nor a backslash. The second-character rule blocks values like a double-slash address, which browsers treat as absolute and prefix with http or https to match the current page's protocol.
- Alternative: avoid putting URLs in query parameters at all. For a post-login redirect, store the destination in a temporary cookie. Attackers cannot forge a cookie in a victim's browser as easily, which shuts the door on abusive links.

## When and how to apply: sites that need external links (PDF p. 186)
Some sites, such as a social news site, must let users post links to external addresses. In that case, check each URL against a blacklist of harmful sites using the Google Safe Browsing API.

## Time-sensitive statements
Named products (Bitly, Google Safe Browsing API) reflect the book's writing. The book's 301/302 gloss is reversed relative to the standard definitions.

## Relations
Follows email fraud (WS-C16-002). The next topic is protecting pages from being framed (WS-C16-004). Chapter 18 lists the check for redirects as a commandment (WS-C18-001).
