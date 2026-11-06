---
id: WAS-C18-002
title: Secure Sockets Layer and Transport Layer Security
source_pages: "227-228"
chapter: 18
concepts: [ssl, tls, data-in-transit, man-in-the-middle, https, certificate-authority, lets-encrypt]
related: [WAS-C18-001, WAS-C18-003]
time_sensitive: true
---
# Secure Sockets Layer and Transport Layer Security
(Source: PDF pp. 227-228)

## What the section covers
Why data in transit is the first architectural decision for MegaMerch, what SSL and TLS are, and how encryption on the wire is shown to users and put in place.

## Why it matters
- Handling data in transit is an important early decision during architecture review, since it affects the flow of all data through the application (PDF p. 227).
- A first requirement is that all data sent over the network be encrypted en route. That lowers the risk of a man-in-the-middle attack, which could steal user credentials and make purchases on the user's behalf, because MegaMerch stores financial data.

## Meaning
- SSL (Secure Sockets Layer) and TLS (Transport Layer Security) are the two main cryptographic protocols for protecting in-transit data from eavesdroppers on a network (PDF p. 227).
- Netscape designed SSL in the mid-1990s, and several versions followed.
- RFC 2246 defined TLS in 1999, with better security in response to architectural problems in SSL. The book says TLS cannot work with older SSL versions because the two differ so much in architecture. It describes TLS as giving the most rigid security, while SSL has wider adoption but several vulnerabilities that weaken it.
- Figure 18-1 shows the Let's Encrypt site, a free, automated and open certificate authority backed by a nonprofit; its caption calls it one of only a few nonprofit security authorities that provide certificates for TLS encryption (PDF p. 228).

## How it works and shows up
- Browsers show a lock icon in the address bar when a site's traffic is secured by SSL or TLS (PDF p. 228).
- The HTTP specification offers HTTPS, a URI scheme that requires TLS or SSL before any data is sent. Browsers that support HTTPS warn the user if the connection is compromised during an HTTPS request.

## When and how to apply
For MegaMerch, all data should be encrypted and TLS compatible before it is sent. How TLS is configured depends on the server, but every major web server package offers an easy way to start encrypting traffic (PDF p. 228).

## Time-sensitive statements
The statement that SSL has the highest adoption, and the description of Let's Encrypt as one of only a few nonprofit authorities, reflect the time of writing.

## Relations
Answers the data-in-transit question raised in WAS-C18-001. Credential handling follows in WAS-C18-003.
