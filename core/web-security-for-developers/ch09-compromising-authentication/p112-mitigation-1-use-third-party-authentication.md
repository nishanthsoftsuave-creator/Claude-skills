---
id: WS-C09-003
title: Mitigation 1 - Use Third-Party Authentication
source_pages: "112"
chapter: 9
concepts: [third-party-authentication, oauth, openid, social-login, delegated-authentication, password-storage-avoidance]
related: [WS-C09-002, WS-C09-004, WS-C09-005]
time_sensitive: true
---
# Mitigation 1 - Use Third-Party Authentication
(Source: PDF p. 112; the page opens with the end of the previous section, covered in WS-C09-002. This row begins at the "Mitigation 1" heading.)

## What the section covers
The first defence against account compromise: let a third party handle authentication.

## Meaning and rationale
- The book's central claim is that the most secure authentication system is the one you never write (PDF p. 112).
- Instead of building your own, you can offer a service such as Facebook Login, letting users sign in with their social media identity. That is convenient for users and spares you from ever storing their passwords (PDF p. 112).

## How it works
- Many large technology companies offer similar services. Most rely on the open authentication (OAuth) or OpenID standards, which are widely implemented protocols for delegating authentication to another party (PDF p. 112).
- Providers are generally easy to integrate, and you can combine several, choosing whichever suit your user base (PDF p. 112).
- Examples the book gives: an email-related service can use Google OAuth to request access to users' Gmail accounts; a technical service can use GitHub OAuth. Twitter, Microsoft, LinkedIn, Reddit, Tumblr and hundreds of other sites also provide authentication (PDF p. 112).

## Limitations
The book revisits the drawback on the next page: relying only on third-party login can shrink your audience, which is why WS-C09-005 covers running your own system too.

## Time-sensitive statements
The named providers (Facebook Login, Google, GitHub, Twitter, Microsoft, LinkedIn, Reddit, Tumblr) reflect the landscape when the book was written (PDF p. 112).

## Relations
Companion options: WS-C09-004 (single sign-on) and WS-C09-005 (own system).
