---
id: WS-C15-001
title: "Chapter 15 Introduction: XML Attacks"
source_pages: "173"
chapter: 15
concepts: [xml, html, markup-language, xml-parsing, parser-attack-surface, default-parsing]
related: [WS-C15-002, WS-C15-003, WS-C15-006, WS-C14-001]
time_sensitive: false
---
# Chapter 15 Introduction: XML Attacks
(Source: PDF p. 173, tail PDF p. 174. The text on PDF p. 174 above the heading "The Uses of XML" belongs to this opening and is covered here.)

## What the section covers
The chapter's opening framing: why XML exists, what it looks like, and why XML parsers are a target even for sites that never intended to handle XML.

## Meaning
- As the web grew explosively in the 1990s, organizations needed to exchange data between computers, which required agreeing on a common data format. Human-readable web documents were marked up in HTML, while machine-readable files were commonly stored in an analogous format, Extensible Markup Language (XML) (PDF p. 173).
- XML can be seen as a more general form of HTML. The document author picks the tag and attribute names, whereas HTML fixes them in its specification (PDF p. 173).
- Listing 15-1 is a small XML catalog of books. A catalog tag wraps book tags, each carrying an id attribute and containing author, title, genre and description tags. It has two example books, one a young-adult novel and one a medical title (PDF pp. 173-174).
- XML parsing is the process of turning an XML file into in-memory code objects (PDF p. 174).

## Why it matters
- Because XML was popular early in the web's history, an XML parser has been built into every browser and web server of the past few decades (PDF p. 174).
- Parsers are a common hacker target. Even a site that does not handle XML by design may have a web server that parses it by default (PDF p. 174).
- The chapter's promise is to show how parsers are attacked and how to defuse those attacks (PDF p. 174).

## Relations
The next row, WS-C15-002, covers what XML is used for. The attacks are described in WS-C15-004 (XML bombs) and WS-C15-005 (external entities), and the fixes in WS-C15-006.
