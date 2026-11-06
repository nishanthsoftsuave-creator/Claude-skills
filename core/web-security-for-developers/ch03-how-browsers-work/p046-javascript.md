---
id: WS-C03-003
title: JavaScript in the Browser
source_pages: "46-47"
chapter: 3
concepts: [javascript, script-tag, defer, browser-security-model, sandbox, event-listeners, cross-site-scripting, remote-code-execution]
related: [WS-C03-002, WS-C03-004, WS-C07-001]
time_sensitive: false
---
# JavaScript in the Browser
(Source: PDF pp. 46-47. The section starts part-way down PDF p. 46 at its heading; the text above it is the tail of WS-C03-002.)

## What the section covers
How JavaScript is included in and executed by a page, the timing problem solved by the defer attribute, and the sandbox rules of the browser security model.

## Meaning
- Modern pages use JavaScript to respond to user actions. It is a full programming language run by the browser's JavaScript engine when pages are rendered (PDF p. 46).
- It is added to an HTML document with a script tag. The code can sit inline in the document, or, more commonly, the tag references a JavaScript file loaded from an external URL (PDF p. 46).

## How it works
- By default the browser runs JavaScript as soon as the script tag is parsed into a DOM node. For an external file, that means as soon as it has loaded (PDF p. 47).
- Problem: if the pipeline has not finished parsing the HTML, the code may try to touch page elements not yet in the DOM. Hence script tags are often marked with the defer attribute, which makes the code run only after the whole DOM has been built (PDF p. 47).

## Security: the browser security model
- Because browsers eagerly run any JavaScript they meet, there are security implications. A hacker's ultimate goal is often remote code execution on someone else's machine, and the internet makes this easier since nearly every computer is networked (PDF p. 47).
- So browsers heavily restrict JavaScript through the browser security model: code runs in a sandbox (PDF p. 47).
- Forbidden in the sandbox (PDF p. 47):
  - starting new processes or accessing existing ones;
  - reading arbitrary system memory (as a managed-memory language, it cannot read outside its sandbox);
  - accessing the local disk (sites may store small amounts of data locally, but through an abstraction rather than the filesystem);
  - accessing the operating system's network layer;
  - calling operating system functions.
- Permitted in the sandbox (PDF p. 47):
  - reading and manipulating the DOM of the current page;
  - listening and responding to user actions by registering event listeners;
  - making HTTP calls on the user's behalf;
  - opening new pages or refreshing the current URL, but only in response to a user action;
  - writing entries to the browser history and moving back and forward in it;
  - requesting the user's location (the book's example prompt is "Google Maps would like to use your location");
  - asking permission to send desktop notifications.

## Limitations and failure modes
- Even under these limits, an attacker who can inject malicious JavaScript into a page can do significant harm through cross-site scripting, such as reading credit card details or credentials as users type them (PDF p. 47).
- Even a tiny injected snippet is a threat because it can add script tags to the DOM to load a larger malicious payload. Defences against this are in Chapter 7 (PDF p. 47).

## Relations
Continues from rendering in WS-C03-002; the wider browser duties follow in WS-C03-004. Cross-site scripting defences are developed in the book's Chapter 7.
