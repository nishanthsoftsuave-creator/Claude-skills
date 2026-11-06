---
id: WAS-C03-010
title: Browser DOM
source_pages: "76"
chapter: 3
concepts: [dom, document-object-model, window-object, document-object, whatwg, browser-standard-library, presentation-layer-vulnerabilities]
related: [WAS-C03-009, WAS-C03-011, WAS-C03-005, WAS-C10-005]
time_sensitive: false
---
# Browser DOM
(Source: PDF p. 76 from the "Browser DOM" heading, plus the top of PDF p. 77 above "SPA Frameworks")

## What the section covers
The last JavaScript topic: the browser's Document Object Model, what role it plays as the language's standard library, and why it matters for finding vulnerabilities.

## Meaning
- The **DOM** is the hierarchical representation data used to manage state in modern web browsers (PDF p. 76).
- Figure 3-3 (rendered and read) shows the `window` object, one of the topmost standard objects defined by the DOM specification (PDF p. 76). The console output shows what appears after typing `window`. It prints the window object expanded into a long list of properties. Items visible include framework globals added by the page (for example `$`, `jQuery`, `CodeMirror`, `JSHINT` and a Google Analytics object), built-in functions (`alert`, `atob`, `btoa`, `blur`, `close`, `confirm`, `fetch`, `find`, `focus`, `getSelection`), and values such as `closed: false`, `devicePixelRatio: 1`, `innerHeight: 937`, `innerWidth: 612`, `isSecureContext: true` and `length: 1`. Also listed are `document`, `history`, `indexedDB`, `crypto` and `caches` (PDF p. 76).
- JavaScript, like any good language, relies on a powerful standard library, and the DOM is that library. It provides well-tested, performant routine functionality, implemented across all major browsers, so code should behave identically or nearly identically whichever browser runs it (PDF p. 77).
- Unlike standard libraries elsewhere, the DOM's main purpose is not to plug gaps in the language. Plugging gaps is a secondary function. Its main job is to give a common interface for defining a hierarchical tree of nodes that represents a web page (PDF p. 77).
- Readers may have called a DOM function while assuming it was part of JavaScript, for instance `document.querySelector()` or `document.implementation` (PDF p. 77).
- The main objects are `window` and `document`, defined in a specification maintained by the organisation WhatWG (PDF p. 77).

## Why it matters
The book says a deep understanding of the browser DOM and its role in a web application is crucial for a JavaScript developer, a pen tester or a security engineer, because it helps spot vulnerabilities visible at the presentation layer. The DOM is the framework from which JavaScript applications are delivered to end users. Not every script-related hole stems from improper JavaScript; some stem from improper browser DOM implementation (PDF p. 77).

## When and how to apply
INTERPRETATION: when investigating a page, treat `window` and `document` as the first things to enumerate in the console, since the extra properties on `window` reveal which libraries and frameworks are loaded (used later in Chapter 6's detection techniques).

## Relations
Variables declared without a keyword end up as `window` properties (WAS-C03-005). Single-page frameworks build on the DOM (WAS-C03-011). DOM-based XSS relies on DOM sources and sinks (WAS-C10-005).
