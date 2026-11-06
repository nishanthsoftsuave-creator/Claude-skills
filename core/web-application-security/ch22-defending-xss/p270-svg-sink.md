---
id: WAS-C22-004
title: SVG Sink
source_pages: "270"
chapter: 22
concepts: [svg, xml-script-execution, scalable-vector-graphics, dom-sinks, image-upload, onload]
related: [WAS-C22-002, WAS-C22-003, WAS-C22-005, WAS-C11-002]
time_sensitive: false
---
# SVG Sink
(Source: PDF p. 270; the section continues at the top of the next page)

## What the section covers
Why SVG images (and Blobs) are riskier than ordinary images, because they hold arbitrary data and can still execute code.

## Opening statement
Blob and SVG carry significant risk as sinks because they store arbitrary data and yet can execute code (PDF p. 270).

## Rest of the section (next page)
The section continues on the following page, so no page cite applies to what follows. The book gives a small SVG document that draws a red circle and also contains a script element that writes a message to the console. It says Scalable Vector Graphics are excellent for showing images the same way on many devices, but, because they rely on the XML specification, which allows script execution, they are far riskier than other image types. It recalls from Part II that the image tag could launch CSRF because it fetches a URL (the book says the tag supports an href, as printed), and says SVGs can run any JavaScript when they load, which makes them considerably more dangerous.

## When and how to apply
INTERPRETATION: do not accept or render user-supplied SVG as markup unless its content is sanitised or the file is served in a way that blocks script, as the book's rule on avoiding SVG as a sink implies.

## Relations
Listed as a sink in WAS-C22-002. The earlier image-tag CSRF discussion is in WAS-C11-002. Blob is in WAS-C22-005.
