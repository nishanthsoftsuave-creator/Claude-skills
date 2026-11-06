---
id: WS-C15-005
title: XML External Entity Attacks
source_pages: "177"
chapter: 15
concepts: [xxe, external-entity, inline-dtd, file-disclosure, ssrf, error-message-leak, file-protocol, local-file-read]
related: [WS-C15-003, WS-C15-004, WS-C15-006, WS-C16-005, WS-C12-003]
time_sensitive: false
---
# XML External Entity Attacks
(Source: PDF p. 177, tail PDF p. 178. The text on PDF p. 178 above the "Securing Your XML Parser" heading is the end of this section and is covered here.)

## What the section covers
What an external entity is, how a parser handles one, why this is a "security disaster", and the two ways attackers exploit it: reading local files through error messages, and forcing the server to make network requests.

## Meaning
- DTDs can pull in content from external files. If a parser processes inline DTDs, an attacker can use external entity declarations to explore the local filesystem or to trigger network requests from the web server itself (PDF p. 177).
- Listing 15-6 shows a typical one. A copyright-style document declares an entity named copy with the PUBLIC keyword and a web address of a W3C-hosted copyright file, and the body references that entity to include boilerplate text (PDF p. 177).
- Per the XML 1.0 specification, the parser must read the file named by the entity and insert its contents wherever the entity is referenced. Here the data at that web address would replace each copy reference (PDF p. 178).
- The address can use different network protocols according to its prefix. The example uses http://, which makes the parser issue an HTTP request. The specification also allows local disk reads via a file:// prefix, which is why the book calls external entity definitions a security disaster (PDF p. 178).

## How it works: how hackers exploit external entities (PDF p. 178)
- Reading files: when a parser throws an error, the message often includes the XML document being parsed. A malicious file can reference a sensitive local file, for example the Linux password file. When the parser inserts that file's contents the document becomes malformed, parsing fails, and the error response helpfully contains the file's contents. This lets attackers read files holding passwords and other confidential data. (The book prints the path as file://etc/passwd.)
- Server-side request forgery (SSRF): an attacker can make your server send malicious HTTP requests. A naively configured parser makes a network request whenever it meets an external entity URL with a network prefix. Being able to make your server request a URL of their choosing is a boon for attackers, who have used it to probe internal networks, to launch denial-of-service attacks on third parties, and to disguise malicious URL calls.
- The book defers the broader SSRF risks to the next chapter (WS-C16-005).

## Why it matters
Anywhere your site accepts XML, the parser's entity handling decides whether an uploaded document can reach your filesystem or your network. The fix is to turn off inline DTD processing (WS-C15-006).

## Relations
Follows XML bombs (WS-C15-004). The sibling error-leak risk is discussed in chapter 12 (WS-C12-003), and SSRF is treated in WS-C16-005.
