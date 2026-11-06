---
id: WAS-C06-003
title: Detecting JavaScript Libraries
source_pages: "122"
chapter: 6
concepts: [javascript-libraries, jquery, lodash, underscore, queryselectorall, script-enumeration, global-namespace, version-detection]
related: [WAS-C06-002, WAS-C06-004, WAS-C03-010]
time_sensitive: true
---
# Detecting JavaScript Libraries
(Source: PDF p. 122; the code listing and its output finish on PDF p. 123)

## What the section covers
How to find which JavaScript helper libraries a page uses, either through well-known globals or by listing every external script the page loads.

## Meaning
- Many helper libraries exist. Some expose globals; others work without any visible trace (PDF p. 122).
- Libraries that use the top-level namespace are easy to detect and iterate over. Figure 6-2 shows a console where typing the dollar symbol returns the jQuery function and reading its fn.jquery property reveals the version (the figure prints 3.3.1) (PDF p. 122).
- The text says Underscore and Lodash use "the underscore symbol" and prints a dollar sign for it, then says jQuery uses the dollar namespace. INTERPRETATION: the underscore character was probably intended for Underscore and Lodash; the page is recorded as printed.

## How it works
1. For libraries that leave no global, query the DOM for every script element (PDF p. 122).
2. The helper getScripts() calls document.querySelectorAll('script'). The book explains selector syntax: a leading dot means a CSS class, a hash means an id attribute, and no prefix means an HTML element (PDF p. 122).
3. It iterates the result and logs each element whose src attribute is not empty (PDF p. 122).
4. The sample output lists a Google Analytics script, Google Tag Manager, Stripe, jQuery 3.4.1, D3 5.9.7 from a CDN, and a local main.js (PDF p. 123). The book then says each script must be opened individually to learn ordering and configuration (PDF p. 123).

## When and how to apply
Use the global check for a fast answer, and the script listing when the globals are absent or when you need the complete third-party inventory for your recon map.

## Limitations
INTERPRETATION: the list only covers scripts present in the page at the time of the query. The introduction to server-side detection in the next row (WAS-C06-005) notes that scripts loaded conditionally or asynchronously can still be reached if you trigger the right conditions.

## Relations
Preceded by SPA detection (WAS-C06-002), followed by stylesheet detection (WAS-C06-004). The browser DOM is described in WAS-C03-010.

## Time-sensitive statements
Library versions and the example script URLs (jQuery 3.3.1 and 3.4.1, D3 5.9.7, a Google Analytics ID) are dated.
