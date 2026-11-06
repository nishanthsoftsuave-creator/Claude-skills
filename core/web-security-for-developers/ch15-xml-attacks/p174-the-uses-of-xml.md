---
id: WS-C15-002
title: The Uses of XML
source_pages: "174"
chapter: 15
concepts: [xml, self-describing-data, apis, json, yaml, configuration-files, xml-parsing, validation]
related: [WS-C15-001, WS-C15-003, WS-C02-003]
time_sensitive: false
---
# The Uses of XML
(Source: PDF p. 174; the text above the "The Uses of XML" heading on this page, including Listing 15-1, belongs to WS-C15-001)

## What the section covers
Where XML is commonly used, the alternatives that have gained ground, and the point that XML parsing still has to be secured on every web server.

## Meaning
- Like HTML, XML wraps data items in tags and lets tags nest inside one another. The author chooses meaningful tag names, so the document describes itself (PDF p. 174).
- Because it is readable, XML was widely adopted to encode data that other applications consume (PDF p. 174).

## How it works: typical uses
- APIs that let client software call functions over the internet frequently accept and return XML (PDF p. 174).
- JavaScript in web pages that talks to the server asynchronously often uses XML (PDF p. 174).
- Many applications, web servers among them, read XML-based configuration files (PDF p. 174).

## Alternatives and trade-offs
- In the past decade some of these applications moved to formats that suit the job better and are less verbose. JSON is the more natural way to encode data in JavaScript and other scripting languages, and YAML, which relies on meaningful indentation, is simpler for configuration files (PDF p. 174).
- Even so, every web server implements XML parsing in some form, so every server needs protection against XML attacks (PDF p. 174).

## Why it matters
The book states that XML vulnerabilities generally arise during validation, and closes the page by promising to explain what validation means when an XML document is parsed. That explanation is the next row, WS-C15-003 (PDF p. 174).

## Relations
Follows WS-C15-001 and leads into WS-C15-003.
