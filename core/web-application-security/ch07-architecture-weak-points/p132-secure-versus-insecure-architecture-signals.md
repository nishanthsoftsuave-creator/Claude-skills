---
id: WAS-C07-002
title: Secure Versus Insecure Architecture Signals
source_pages: "132-135"
chapter: 7
concepts: [secure-architecture, insecure-architecture, xss-architecture, messaging-example, appendtodom, dompurify, centralized-sanitization, secure-by-default, architecture-review]
related: [WAS-C07-001, WAS-C07-003, WAS-C10-003, WAS-C22-001]
time_sensitive: false
---
# Secure Versus Insecure Architecture Signals
(Source: PDF pp. 132-135; the closing remarks sit on PDF p. 136)

## What the section covers
Why repeated vulnerabilities point to weak architecture, shown with a direct-messaging example, and how a central helper can remove a whole class of XSS risk.

## Meaning
- One XSS bug may come from a poorly written method, but several are probably a sign of weak application architecture (PDF p. 132).
- The comparison uses two small applications that let users send direct text messages. One is vulnerable to XSS and one is not (PDF p. 132).

## How it works
**The insecure design.** It might accept a script when a message is stored through an API endpoint, its database might store it, and the string gets neither filtering nor sanitising. When displayed, the DOM evaluates a message containing a script tag with an alert, and the script runs (PDF p. 132).

**The secure design.** It likely has one or several protections. Adding them one case at a time costs developer time and is easily forgotten, so even skilled engineers will leave holes if the architecture is inherently insecure. A secure application adds security before and during feature development, a mediocre one only while building, and an insecure one may never (PDF p. 132).

**Why repetition hurts.** If one developer writes ten versions of the messaging system over five years, each differs but the risks stay mostly the same (PDF p. 132). Each system needs a write UI, an API endpoint to receive a message, a database table to store it, an endpoint to retrieve messages and UI code to display them (PDF p. 133).

**The minimal code.** The book shows files that make up the example (PDF pp. 133-135):
- a write page with a heading naming the recipient, a text input and a send button;
- a client send function that reads values from the DOM and calls a utility passing the session token, target and message;
- a server post handler that returns 400 if the token, target or message is missing and otherwise saves the message, answering 200 or 400;
- a message model with sender (from the session), recipient and text;
- a server get handler that returns 401 without a token, 400 without a message id, and otherwise returns the message;
- a display page and a client function that fetches a message and appends both text and author to the DOM.
INTERPRETATION: the send function reads the message from the element whose id is the button's, and the display function passes arguments in the opposite order from the helper shown later; the book does not comment on either.

**The central fix.** Many protections should live in the architecture rather than in each case (PDF p. 135). A helper called appendToDOM takes the data, a selector and an unsafe flag defaulting to false. In the default case it assigns the data with innerText, so tags show as text; with the flag on it assigns innerHTML after running the DOMPurify sanitiser. Building the application around this function sharply lowers the odds of XSS (PDF p. 135). The flag is named unsafe, is off by default and is the last parameter, so it is hard to switch on by accident (PDF p. 135).

## Why it matters
Mechanisms like appendToDOM signal secure architecture; applications without them are more likely to contain vulnerabilities. That is why spotting insecure architecture helps both with finding flaws and with prioritising improvements (PDF p. 136).

## Relations
Continues WAS-C07-001; layers of defence follow in WAS-C07-003. XSS itself is covered in WAS-C10-003 and defences in WAS-C22-001.
