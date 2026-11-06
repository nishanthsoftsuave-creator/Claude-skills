---
id: WS-C16-007
title: "Chapter 16 Summary: Don't Be an Accessory"
source_pages: "189-190"
chapter: 16
concepts: [chapter-summary, spf, dkim, open-redirect, content-security-policy, ssrf, botnet, outbound-whitelist]
related: [WS-C16-002, WS-C16-003, WS-C16-004, WS-C16-005, WS-C16-006, WS-C17-001]
time_sensitive: false
---
# Chapter 16 Summary: Don't Be an Accessory
(Source: PDF pp. 189-190; the text at the top of PDF p. 189 above the "Summary" heading is the end of WS-C16-006. PDF p. 190 is blank in the extracted text.)

## What the section covers
A five-point checklist for avoiding becoming an accessory to attacks on others, and the hand-off to the denial-of-service chapter.

## The recap
The book frames the summary as a list of actions (PDF p. 189):
1. Protect the email you send by implementing SPF and DKIM in your domain name records (the book's bullet calls them "headers"; elsewhere in the chapter they are DNS records) (see WS-C16-002).
2. Make sure your site has no open redirects (see WS-C16-003).
3. Prevent your site from being hosted inside an iframe by setting a content security policy (see WS-C16-004).
4. Audit your code so the server cannot be tricked into sending HTTP requests to an external URL chosen by an attacker, and whitelist outbound network access to avoid being used in server-side request forgery (see WS-C16-005).
5. Use virtualized servers, virus scanners or vulnerability-scanning tools to find and remove bots (see WS-C16-006).

## Relations
The next chapter turns to a brute-force technique that can take your server offline: the denial-of-service attack (PDF p. 189). See WS-C17-001.
