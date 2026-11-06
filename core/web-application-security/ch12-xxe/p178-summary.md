---
id: WAS-C12-003
title: Chapter 12 Summary - XXE
source_pages: "178"
chapter: 12
concepts: [xxe, xml-parser, configuration, summary, external-entity, server-compromise]
related: [WAS-C12-001, WAS-C12-002, WAS-C24-004]
time_sensitive: false
---
# Chapter 12 Summary: XML External Entity
(Source: PDF p. 178)

## What the section covers
The closing summary of the XXE chapter.

## Meaning (PDF p. 178)
- XXE attacks are simple to understand and often simple to start. They deserve attention because of how powerful they are, since they can compromise a whole web server, let alone the application on top of it.
- They depend on a standard that is weak on security but widely adopted and relied on across the internet.
- They are easy to fix: often a single configuration line stops the parser from referencing external entities.
- Even so, the book says these attacks should always be tried against new applications, because one missing configuration line in an XML parser can cause so much damage.

## Why it matters
The chapter's two points are the size of the possible damage and how small the fix is. INTERPRETATION: that mismatch is why this class of flaw keeps appearing in production code.

## Relations
Recaps WAS-C12-001 and WAS-C12-002. The defence chapter's wrap-up is WAS-C24-004.
