---
id: WAS-C24-004
title: Summary - Defending Against XXE
source_pages: "289-290"
chapter: 24
concepts: [xxe-summary, parser-configuration-review, brand-damage, precautions, xml-like-formats]
related: [WAS-C24-001, WAS-C24-002, WAS-C24-003]
time_sensitive: false
---
# Summary: Defending Against XXE
(Source: PDF pp. 289-290; p. 290 is blank, so all content is on p. 289)

## What the section covers
The chapter's closing summary. It begins partway down the page, below the Advanced XXE Risks text.

## Key points
- The author says XXE earned space in the book because improperly configured XML parsers are common in production web applications and an external entity attack puts an organization at great risk (PDF p. 289).
- XXE attacks are often easy to mitigate, yet still widespread. It is therefore imperative to double-check each XML parser's configuration before publishing any application that uses XML or XML-like data types (PDF p. 289).
- XXE attacks are serious and can badly damage an organization, an application or a brand, so all precautions should be taken with a server-side XML parser to keep an accidental XXE out of the codebase (PDF p. 289).

## When and how to apply
INTERPRETATION: add the parser-configuration check to release review for every service that parses XML-like input, including formats such as SVG.

## Relations
Summarizes WAS-C24-001 (parser fix), WAS-C24-002 (other formats) and WAS-C24-003 (impact).
