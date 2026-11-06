---
id: WS-C16-004
title: Clickjacking
source_pages: "186"
chapter: 16
concepts: [clickjacking, iframe, z-index, opacity, likejacking, content-security-policy, frame-ancestors]
related: [WS-C16-003, WS-C16-005, WS-C03-002, WS-C18-001]
time_sensitive: false
---
# Clickjacking
(Source: PDF p. 186, tail PDF p. 187. The text at the top of PDF p. 186 above the "Clickjacking" heading is the end of WS-C16-003. The text on PDF p. 187 above the "Server-Side Request Forgery" heading belongs here.)

## What the section covers
How an attacker can layer an invisible element over your framed page to hijack clicks, and the Content-Security-Policy header settings that stop it.

## Meaning
- HTML lets a page contain another page through the iframe tag. This mixes content from different domains in a controlled way, since JavaScript inside the frame cannot reach the containing page. Iframes are commonly used for third-party content, and OAuth and CAPTCHA widgets often use them to secure cookies (PDF p. 186).
- Clickjacking (click hijacking) abuses that: modern CSS can stack elements using z-index, where higher values hide lower ones and get the click first, and can make elements transparent with opacity. A hacker places a transparent div over an iframe and tricks the victim into clicking what is in the div while believing they are clicking the content underneath (PDF p. 186).
- Documented uses: victims tricked into switching on their webcam so the attacker can watch, and likejacking, where a victim unknowingly likes something on Facebook. Selling likes on the dark web for promotion is lucrative (PDF p. 186).

## How it works: preventing it
- Most sites never need to be placed inside an iframe, so say so directly. Modern browsers honor the Content-Security-Policy response header; the frame-ancestors directive with the value none means the page may never be framed (Listing 16-4) (PDF p. 186):

```
Content-Security-Policy: frame-ancestors 'none'
```

- If the site must frame itself, use the same header with the keyword self, which lets your site host iframes of other parts of your own site (Listing 16-5) (PDF p. 187):

```
Content-Security-Policy: frame-ancestors 'self'
```

- If third-party sites need to frame yours, whitelist those domains individually (Listing 16-6, which names example.com and google.com as the permitted hosts) (PDF p. 187):

```
Content-Security-Policy: frame-ancestors example.com google.com
```

## Why it matters
If you run a website, make sure it is not used as bait in someone else's clickjacking attack (PDF p. 186). INTERPRETATION: the book's order of examples suggests forbidding framing by default and relaxing only when there is a specific need.

## Relations
Follows WS-C16-003 and leads into server-side request forgery (WS-C16-005); the commandment form is in WS-C18-001.
