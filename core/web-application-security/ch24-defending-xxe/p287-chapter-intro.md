---
id: WAS-C24-001
title: Defending Against XXE (Chapter Introduction)
source_pages: "287"
chapter: 24
concepts: [xxe-defense, xml-parser-configuration, external-entities, disable-doctype, java-xml-parsers, parser-defaults, owasp]
related: [WAS-C12-001, WAS-C24-002, WAS-C24-004]
time_sensitive: false
---
# Defending Against XXE (chapter introduction)
(Source: PDF p. 287)

## What the section covers
The core remedy for XML External Entity attacks: configure the XML parser so external entities are not processed. The page also gives the book's warning about Java parsers and a flow figure.

## Meaning
XXE is described as easy to defend against: you turn off external entities in the XML parser. How this is done depends on the parser, but it is typically one line of configuration. The example sets a feature on a parser factory so that document type declarations are disallowed, using a feature name hosted under apache.org (PDF p. 287).
INTERPRETATION: as printed, the feature name refers to disallowing DOCTYPE declarations altogether, which is a stricter setting than only turning off external entities; both aim at the same hole.

## Why it matters
OWASP is cited as noting that XXE is particularly dangerous with Java-based XML parsers because many enable it by default. Whether it is off by default depends on the language and parser in use (PDF p. 287).

## How it works
Figure 24-1 shows a user sending a request with an XML payload that contains an XXE. The server's XML parser processes it. With an improper configuration, server resources are accessed and may be reflected back. With a proper configuration, the parser rejects the entity tag (PDF p. 287).

## When and how to apply
Never assume the setting is off. Check the XML parser's API documentation for the correct option every time (PDF p. 287).

## Relations
The attack is in WAS-C12-001; format alternatives follow in WAS-C24-002, and the chapter closes in WAS-C24-004.
