---
id: WAS-C22-002
title: Sanitizing User Input - Overview
source_pages: "269"
chapter: 22
concepts: [sanitisation, javascript-pseudo-scheme, dom-sinks, allowed-tags, sanitizer-bypass, polyfill, dom-xss]
related: [WAS-C22-001, WAS-C22-003, WAS-C22-004, WAS-C22-005, WAS-C22-006, WAS-C22-007, WAS-C10-005]
time_sensitive: false
---
# Sanitizing User Input: overview
(Source: PDF p. 269, continuing on the tail page 270)

## What the section covers
Why sanitising user-supplied markup is hard, a bypass example that uses no script tag or quote, and a list of DOM APIs to avoid.

## When sanitising is needed
Sometimes innerText cannot be used, in particular when some tags must be allowed but not others. The example is allowing strong and italic tags but never script tags. In that case user data must be thoroughly sanitised before it goes into the DOM, making sure that no malicious tags are present and that nothing tries to escape the sanitiser itself (PDF p. 269).

## Example: the JavaScript pseudo-scheme
- Suppose a sanitiser blocks single and double quotes and script tags. A link whose address starts with the JavaScript pseudo-scheme and calls an alert on the document cookie still runs (PDF p. 269).
- The DOM specification is huge and complex, so cases where script can execute are more common than expected. The pseudo-scheme, a URL scheme the book says to avoid, runs a string without any script tag or quote (PDF p. 269).
- Combined with other DOM methods it can even get around the quote filter. A link that builds its alert text from character codes (String.fromCharCode with 88, 83, 83) alerts "XSS" as though it were a literal string (PDF p. 270, tail page).

## How hard sanitising is
The book states that sanitising is quite hard and that complete sanitising is extremely hard. DOM XSS is harder again to mitigate because it depends on methods outside your control, unless you extensively polyfill and freeze objects before rendering (PDF p. 270).

## Rule of thumb and APIs to avoid
Anything that converts text to DOM, or text to script, is a potential XSS attack vector. Where possible, stay away from (PDF p. 270):
- element.innerHTML and element.outerHTML (the printed list shows the first name with a typographical slip)
- Blob
- SVG
- document.write and document.writeln
- DOMParser.parseFromString
- document.implementation

The next modules cover the DOMParser, SVG and Blob sinks in turn.

## Relations
Follows WAS-C22-001 and leads into WAS-C22-003, WAS-C22-004, WAS-C22-005, hyperlink sanitising (WAS-C22-006) and entity encoding (WAS-C22-007). DOM-based XSS is described in WAS-C10-005.
