---
id: WAS-C22-003
title: DOMParser Sink
source_pages: "270"
chapter: 22
concepts: [domparser, parsefromstring, dom-sinks, createelement, appendchild, xss-prevention]
related: [WAS-C22-002, WAS-C22-004, WAS-C22-005]
time_sensitive: false
---
# DOMParser Sink
(Source: PDF p. 270)

## What the section covers
Why the DOMParser API is an XSS sink and the safer alternative of building nodes one by one.

## Meaning
The APIs listed in the overview let a developer easily generate DOM or script from text, which is why they are easy sinks for XSS execution (PDF p. 270). DOMParser takes a string through its parseFromString method and loads it into DOM nodes that mirror the string's structure. The book's example passes a string containing a script tag that raises an alert (PDF p. 270).

## Legitimate use
The API could be used to fill a page with structured DOM from a server, convenient when a complex DOM string must become properly organised nodes (PDF p. 270).

## Safer alternative
Create each node yourself with document.createElement and arrange them with appendChild. This carries much less risk, because you decide the structure and tag names and the payload can only supply content (PDF p. 270).

## When and how to apply
INTERPRETATION: reserve parseFromString for data you control, and build the DOM node by node whenever any part of the text comes from a user.

## Relations
One of the sinks in WAS-C22-002. The other two sinks with their own sections are SVG (WAS-C22-004) and Blob (WAS-C22-005).
