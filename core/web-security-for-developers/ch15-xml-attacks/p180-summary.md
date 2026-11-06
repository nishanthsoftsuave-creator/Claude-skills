---
id: WS-C15-008
title: "Chapter 15 Summary: XML Attacks"
source_pages: "180"
chapter: 15
concepts: [xml, inline-dtd, xml-bomb, xxe, hardened-parser, chapter-summary, good-internet-citizen]
related: [WS-C15-004, WS-C15-005, WS-C15-006, WS-C15-007, WS-C16-001]
time_sensitive: false
---
# Chapter 15 Summary: XML Attacks
(Source: PDF p. 180; the "Other Considerations" text above the "Summary" heading on this page is WS-C15-007)

## What the section covers
The chapter's closing recap and the hand-off to the next chapter.

## The recap
- XML is a flexible data format widely used to exchange machine-readable data across the internet (PDF p. 180).
- A parser may be vulnerable if it is configured to accept and process inline document type definitions (PDF p. 180).
- XML bombs use inline DTDs to explode the parser's memory use, which can crash the web server. This is the subject of WS-C15-004 (PDF p. 180).
- XML external entity attacks refer to local files or network addresses and can trick the parser into revealing sensitive information or making malicious network requests. This is WS-C15-005 (PDF p. 180).
- The takeaway: use a hardened XML parser that disables inline DTD parsing, as set out in WS-C15-006 (PDF p. 180).

## Relations
The next chapter builds on an idea touched here: how flaws in your web server let attackers launch attacks on third parties, so that even when you are not the direct victim you should be a good internet citizen and stop attacks that use your system (PDF p. 180). See WS-C16-001.
