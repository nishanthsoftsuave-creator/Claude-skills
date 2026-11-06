---
id: WAS-C22-006
title: Sanitizing Hyperlinks
source_pages: "271"
chapter: 22
concepts: [hyperlink-sanitisation, window-location, anchor-element, encodeuricomponent, url-scheme, browser-sanitisation]
related: [WAS-C22-002, WAS-C22-005, WAS-C22-007]
time_sensitive: false
---
# Sanitizing Hyperlinks
(Source: PDF p. 271, continuing on the tail page 272)

## What the section covers
How to handle a link target that comes from user input when script code, not an anchor tag, does the navigation, by borrowing the browser's own link filtering.

## The problem
Suppose you let users create JavaScript buttons that link to a page taken from user input. The button calls a function that sets window.location.href to your site plus the user's value. If the value is a script tag, the browser goes to an address containing script markup. The pseudo-scheme risk has already been covered, but any HTML in the value also has to be sanitised (PDF p. 271).

## Using a dummy anchor
- Create an anchor element, assign the user value to its href, and use what the anchor reports when building the navigation address (PDF p. 272).
- Major browsers already strip or encode script markup in anchor links. A script on the linked-to page that interpreted window.location.href could have been susceptible to the first version, but the dummy anchor reuses that well-tested filtering, so tags are sanitised and filtered (PDF p. 272).
- The result is also limited to schemes that are legal for anchors, and invalid or improper URLs are blocked (PDF p. 272).
- The example output shown is an address ending in percent-encoded strong tags (PDF p. 272).
INTERPRETATION: the printed code reads a property called a on the dummy element, and the output uses different sample text from the input shown, so the example is not a literal working listing; the idea is what matters.

## encodeURIComponent
The same filtering idea applies to specific parts of a URL: encodeURIComponent turns a bold tag into percent-encoded text. It is theoretically possible to escape such encoders, but they are well tested and likely far safer than a home-made one (PDF p. 272). It cannot be used on a whole URL: the origin (scheme, hostname and port) would be encoded and no longer be readable by browsers, so it would become a different origin (PDF p. 272).

## Relations
Follows the Blob sink (WAS-C22-005) and precedes entity encoding (WAS-C22-007). It belongs to the sanitising theme of WAS-C22-002.
