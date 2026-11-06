---
id: WS-C14-004
title: Securing the Services That You Use
source_pages: "166-167"
chapter: 14
concepts: [third-party-services, api-keys, public-private-keys, access-tokens, replay-attack, webhooks, subdomain-takeover, cdn, dns-hygiene]
related: [WS-C14-003, WS-C14-005, WS-C14-006, WS-C09-003]
time_sensitive: true
---
# Securing the Services That You Use
(Source: PDF pp. 166-167, tail PDF p. 168. The section begins at its heading near the bottom of PDF p. 166; the text above it belongs to WS-C14-003. The tail is the "Secure Content Served by Third Parties" subsection at the top of PDF p. 168, above the "Services as an Attack Vector" heading, which begins WS-C14-005.)

## What the section covers
How to safely integrate with services that run on other people's servers: protect API keys and access tokens, secure webhooks, and keep third-party-hosted content from being hijacked under your domain through DNS (PDF pp. 166-168).

## Meaning and framing
- Third-party services are common in modern web development. The book lists Facebook Login for authentication, Google AdSense for ads, Akamai for static content, SendGrid for transactional email and Stripe for payments (PDF p. 166).
- Integration usually means creating an account with the provider, receiving secret access credentials, and changing your code to use the service. Two security concerns follow (PDF p. 166):
  1. Attackers try to steal your access credentials to use your account, for example to mine information about your users, or to start financial transactions in the case of a payment processor (PDF p. 166).
  2. Every third-party service is a potential attack vector into your site, because attackers try to compromise providers to reach a broad range of targets (PDF pp. 166-167). That second concern is the subject of WS-C14-005.
- The remainder of this section deals with the first concern, starting with safe credential storage (PDF p. 167).

## Practices
### Protect your API keys
- Many services give you an API (application programming interface) key that your code presents as an access token on each call. Store it safely: generally in the server's configuration, handled as described in WS-C14-003 (PDF p. 167).
- Some services issue two keys: a public key that may be passed to the browser for JavaScript API calls, and a private key to be kept securely on the server for more sensitive, private calls. The public key carries fewer privileges. Audit the code so the two do not get mixed up and the higher-privilege private key never reaches the client. Even naming config variables SECRET_KEY helps remind the team of the risk (PDF p. 167).
- Other services let you generate a temporary access token to pass to the client. These tokens are usually single-use or valid for a limited time, to curb abuse by a malicious user. They guard against replay attacks, in which an attacker resends HTTP requests to repeat an action, such as duplicating a payment (PDF p. 167).
- Generate such tokens only for users who have already authenticated, or an attacker may be able to mint new tokens on demand (PDF p. 167).

### Secure your webhooks
- Most integrations are HTTPS calls from your server or browser to the provider's API. When the provider must call you, for instance to send notifications, it may ask you to implement a webhook: a simple "reverse API" on your site that the provider calls with HTTPS requests when an event occurs. Examples: a user opens an email you sent, or your payment processor starts a payment (PDF p. 167).
- Webhooks are public URLs, so anyone on the internet can call them, not just the provider. If the provider can send credentials with a webhook call, verify them before processing it (PDF p. 167).
- If a call is purely informational and contains nothing sensitive, it may arrive with no credentials, which makes it easy for an attacker to spoof. Be ready to verify the notification with a further callback to the provider's API before taking any further action (PDF p. 167).

### Secure content served by third parties (tail, PDF p. 168)
- Serving malicious content under someone else's domain is a favourite attacker trick because victims trust sites they know. People are conditioned to trust the padlock icon, so malware deployed under a large company's certificate is more likely to be downloaded (PDF p. 168).
- Many sites use content delivery networks (CDNs) or cloud storage such as Amazon S3 for frequently accessed content. Developers often point a subdomain of their own domain at the service through DNS changes, so the third party's content is encrypted with the site's certificate (PDF p. 168).
- A subdomain takeover works like this: attackers scan the internet for DNS entries for subdomains that point to IP addresses of uninitialized or deactivated services, register with the service provider, and squat on one of the listed addresses. They can then link to malicious content that appears under the victim's domain (PDF p. 168).
- Defence: make sure DNS entries point only to live IP addresses. Make DNS changes only after confirming the service is running under your control, and revoke DNS entries promptly if you change providers (PDF p. 168).
- The book closes by saying it now turns to threats flowing in the other direction (PDF p. 168).

## Time-sensitive statements
- Service names used as examples (Facebook Login, Google AdSense, Akamai, SendGrid, Stripe, Amazon S3).

## Relations
Follows WS-C14-003 (where key storage is described). Third-party authentication providers appear in Chapter 9 (WS-C09-003). Continues with WS-C14-005; recapped in WS-C14-006.
