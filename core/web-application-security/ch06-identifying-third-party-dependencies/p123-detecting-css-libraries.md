---
id: WAS-C06-004
title: Detecting CSS Libraries
source_pages: "123"
chapter: 6
concepts: [css-libraries, stylesheets, link-element, queryselectorall, dom-traversal, dependency-detection]
related: [WAS-C06-003, WAS-C06-005]
time_sensitive: false
---
# Detecting CSS Libraries
(Source: PDF p. 123; the sample output finishes on PDF p. 124)

## What the section covers
A small variation on the script-listing helper that lists the stylesheets a page imports.

## How it works
- The page says that, with minor changes, the script detector can find CSS as well (PDF p. 123).
- The helper getStyles() queries the document for every link element (PDF p. 123).
- It keeps only those whose rel attribute equals stylesheet and logs the href attribute of each (PDF p. 123).
- The book points out that link is a multipurpose element. Its most common job is loading stylesheets, but it is also used for preloading, icons and search (PDF p. 123), which is why the rel check matters.
- The printed output lists jquery-ui.css and a bootstrap file (spelled "boostrap" in the book) first (PDF p. 123), then main.css, components.css and reset.css (PDF p. 124).

## Why it matters
Stylesheet names reveal which CSS frameworks and UI kits a site depends on, which feeds the version lookup described in WAS-C06-001.

## When and how to apply
INTERPRETATION: run it together with the script listing so that your dependency notes cover both code and styling files.

## Limitations
INTERPRETATION: only link elements with rel stylesheet are shown, so styles injected from scripts or written inline will not appear.

## Relations
Same technique family as WAS-C06-003. The chapter then moves from the client to the server in WAS-C06-005.
