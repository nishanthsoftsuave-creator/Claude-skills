---
id: WAS-C03-004
title: JavaScript Overview (Section Lead-In)
source_pages: "65"
chapter: 3
concepts: [javascript, client-server, browser-scripting, nodejs, developer-console, dom-quirks, server-versus-client]
related: [WAS-C03-003, WAS-C03-005, WAS-C03-010]
time_sensitive: false
---
# JavaScript Overview (Section Lead-In)
(Source: PDF p. 65 from the "JavaScript" heading onward, plus the top of PDF p. 66 before "Variables and Scope")

## What the section covers
The introductory text of the JavaScript section: how the book uses the words "server" and "client", why JavaScript is the one language every browser runs, and why the book writes most of its examples in JavaScript.

## Meaning: server and client
- Throughout the book the author keeps discussing client and server applications (PDF p. 65).
- A **server** is a computer, typically a powerful one, in a data center (sometimes called the cloud) that handles requests to a website. It may really be a cluster of many servers, or a single lightweight server used for development or logging (PDF p. 65).
- A **client** is any device a user manipulates to use a web application: a phone, a mall kiosk, even a touch screen in an electric car. For the book's purposes it is usually a web browser (PDF p. 65).

## Why JavaScript
- Servers can run almost any software in almost any language: the book names Python, Java, JavaScript and C++ for web servers (PDF p. 65).
- Clients, and in particular the browser, do not have that freedom. JavaScript is both a programming language and the sole programming language for client-side scripting in web browsers. It is a dynamic language originally designed for internet browsers, now used far beyond them, from mobile applications to the internet of things (IoT) (PDF p. 65).
- Because of this, many code examples in the book are JavaScript. Where possible the backend examples use JavaScript syntax too, so no time is lost switching contexts (PDF p. 66).

## How it is presented
- Figure 3-2 (rendered and read) shows the browser developer tools open on the Console tab. The user typed a call that logs "Hello, World!"; the console printed that text and then "undefined", which is the return value of the logging call (PDF p. 66).
- The author promises to keep the JavaScript clean and simple, but warns he may use constructs that other languages do not popularise (PDF p. 66).
- JavaScript's development is tied to the growth of the browser and its partner, the Document Object Model (DOM). Because of that, the language has quirks to know before moving on, which the following subsections cover: variables and scope, functions, context, prototypal inheritance, asynchrony and the DOM (PDF p. 66).

## When and how to apply
INTERPRETATION: the developer console shown in Figure 3-2 is the place to try the snippets in this chapter and, later, to inspect framework globals during recon.

## Relations
The quirks begin with scope in WAS-C03-005; the DOM itself is covered in WAS-C03-010. The data format that JavaScript reads natively was covered just before (WAS-C03-003).
