---
id: WS-C03-002
title: Web Page Rendering
source_pages: "43-45"
chapter: 3
concepts: [rendering-pipeline, dom, dom-tree, css, stylesheets, selectors, forgiving-parsing, external-resources, acid3, style-precedence]
related: [WS-C03-001, WS-C03-003, WS-C03-004]
time_sensitive: false
---
# Web Page Rendering
(Source: PDF pp. 43-45, tail PDF p. 46. The section starts part-way down PDF p. 43 at its heading. On PDF p. 46 only the text above the heading "JavaScript" belongs here.)

## What the section covers
How a browser converts an HTTP response containing HTML into pixels: the rendering pipeline, the Document Object Model, and how styling is applied.

## Meaning
- The rendering pipeline is the browser component that turns a page's HTML into the visual form you see. It parses the HTML, works out the document's structure and content, and converts it to a series of drawing operations the operating system understands (PDF pp. 43-44).
- Early pages were simple: very little styling (colour, font, size), so rendering meant loading text and images and drawing them in document order. HTML was conceived as a markup language, breaking a page into semantic elements and annotating how information is structured. The early web looked crude but was efficient for text (PDF p. 44).
- Today, styling lives in separate Cascading Style Sheets (CSS) files that say exactly how each element should look. A modern browser such as Chrome contains several million lines of code to interpret HTML and resolve conflicting style rules quickly and uniformly. Knowing the pipeline stages helps appreciate that complexity (PDF p. 44).

## How it works: overview (PDF p. 44)
1. The browser receives an HTTP response and parses the body's HTML into a Document Object Model (DOM), an in-memory structure of how the browser understands the page. The DOM is an interim step, because layout cannot be decided until all the HTML is parsed; tag order does not necessarily fix where content appears.
2. Before anything is drawn, styling rules are applied to every DOM element: foreground and background colour, font style and size, position, alignment and so on.
3. Finally, with structure and styling settled, the page is drawn. This takes a fraction of a second and repeats in a loop as the user interacts.
4. In parallel, the browser loads and executes any JavaScript it meets while building the DOM. JavaScript can change the DOM and the styling rules, before rendering or in response to user actions.

## The Document Object Model (PDF p. 45)
- The DOM describes the HTML as nested elements called DOM nodes. Some nodes map to things drawn on screen, such as input boxes and paragraphs; others, such as script and style elements, control behaviour and layout.
- Each node is roughly one tag of the original HTML. Nodes can hold text or other nodes, mirroring nested tags, and because they branch, developers speak of the DOM tree.
- Tags like script, style, image, font and video can reference an external URL through an attribute. Parsing these makes the browser import the resource, which means another HTTP request. Modern browsers do these requests in parallel with rendering to cut page-load time.
- DOM construction is built to be robust. Browsers tolerate malformed HTML by closing unclosed tags, inserting missing ones and ignoring corrupted ones; vendors do not punish users for site errors.

## Styling information (PDF pp. 45-46)
- Once the DOM tree exists, the browser works out which nodes correspond to on-screen elements, how they are laid out relative to each other, and which styling applies. Rules can be written inline, but developers prefer separate CSS files. This makes restyling easier, keeps HTML clean and semantic, and makes HTML easier to parse for alternative technologies such as screen readers (PDF p. 45).
- With CSS, a developer writes one or more stylesheets. The HTML imports them with a tag pointing to the stylesheet's external URL; the book, as printed, names this the style tag (in common practice stylesheets are linked with a link tag, but the book says style). Each stylesheet has selectors that pick tags in the HTML and assign styling such as font size, colours and position. A selector may be simple, such as rendering an h1 heading in blue, or complicated, such as defining how fast a hyperlink changes colour on mouse hover (PDF p. 45).
- The pipeline needs a lot of logic to work out final styles, since strict precedence rules apply: a selector can match many elements and an element is often styled by several selectors (PDF p. 46).
- Cross-browser consistency was an early growing pain. Modern browsers are mostly consistent but still differ. The industry benchmark for standards compliance is the Acid3 test (Figure 3-1), which few browsers pass with a 100 score. Its caption jokes that it checks browsers can draw coloured rectangles, in use since 2008 (PDF p. 46).
- DOM construction and styling run in parallel with processing of any page JavaScript, which can change structure and layout even before rendering. This leads to the next section (PDF p. 46).

## Relations
Opens from WS-C03-001; the JavaScript execution model is WS-C03-003, and the wider browser responsibilities are WS-C03-004.
