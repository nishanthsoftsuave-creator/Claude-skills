---
id: WAS-C22-007
title: HTML Entity Encoding
source_pages: "272"
chapter: 22
concepts: [entity-encoding, html-escaping, special-characters, script-context, css-context, url-context, output-encoding]
related: [WAS-C22-002, WAS-C22-006, WAS-C22-008]
time_sensitive: false
---
# HTML Entity Encoding
(Source: PDF p. 272, continuing on the tail page 273)

## What the section covers
Escaping the characters that give HTML its meaning, which five characters matter most, and where entity encoding does not help.

## Meaning
Another preventive measure is HTML entity escaping of every HTML tag found in user-supplied data. Entity encoding lets you choose characters to display in the browser in a form that cannot be read as JavaScript (PDF p. 272).

## The big five (Table 22-1)
The table lists each character and its encoded form: the ampersand becomes the amp entity; the less-than sign becomes the lt entity; the greater-than sign becomes the gt entity; the double quote becomes the numeric entity 034; and the single quote becomes the numeric entity 039 (PDF p. 273). The printed table writes each entity as an ampersand followed by the entity text and a semicolon.

## Effect
These conversions do not alter what the browser displays (the amp entity still shows as an ampersand) while sharply reducing the chance of script execution, outside complicated and rare entity-encoding bypass scenarios (PDF p. 273).

## Limitations
Entity encoding does not protect content injected inside a script tag, in CSS or in a URL. It protects only content placed in a div or div-like DOM node. The reason: a string of entity-encoded text can be arranged so that part of it is still valid JavaScript (PDF p. 273).

## When and how to apply
INTERPRETATION: encode by output context. Entity encoding is the right tool for text nodes; script, style and URL positions need their own treatment, as the neighbouring sections show.

## Relations
Follows hyperlink sanitising (WAS-C22-006) and precedes the CSS section (WAS-C22-008). It is part of WAS-C22-002's sanitising theme.
