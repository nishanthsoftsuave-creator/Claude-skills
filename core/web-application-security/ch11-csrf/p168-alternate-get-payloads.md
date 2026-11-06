---
id: WAS-C11-002
title: CSRF via Alternate GET Payloads
source_pages: "168"
chapter: 11
concepts: [csrf, http-get, image-tag, video-tag, src-attribute, no-user-interaction, automatic-requests, state-changing-get]
related: [WAS-C11-001, WAS-C11-003, WAS-C23-001, WAS-C23-005]
time_sensitive: false
---
# CSRF via Alternate GET Payloads
(Source: PDF p. 168; the section's last lines sit on the next page)

## What the section covers
How a forged GET request can be delivered without any click at all, by using page elements that the browser fetches on its own. This extends the hyperlink version in WAS-C11-001.

## Meaning (PDF p. 168)
- Because a GET is the browser's default kind of request, many HTML tags that take a URL fire a GET automatically, either when the user interacts with them or as soon as they are loaded into the DOM. This is why GET endpoints are the easiest target for CSRF.
- The earlier examples used an anchor link, which needs the user to click. The book's alternative is an image tag whose source points at the vulnerable state-changing route, with the parameters carried in the URL. The example in the book is made invisible by giving it zero width and height and no border.
- When the browser meets an image tag it requests the address in its source attribute, since that is how images are loaded. The request goes out with the user's existing session, exactly as in the link case, but nobody has to do anything: loading the page is enough.
- Figure 11-2 (PDF p. 168) shows the flow. User #1 posts an image element that links to an HTTP GET endpoint; User #2 loads the image; a GET is made on behalf of User #2; the server processes it with User #2's authentication cookie; server state changes as if User #2 had changed it, although User #2 is unaware of what happened.
- The book describes the key effect plainly: an invisible image can start a CSRF with no user interaction required.

## Other tags with the same property (PDF pp. 168-169)
The section then points out that most other HTML tags that accept a URL attribute can be abused in the same way. Its second example is the HTML5 video element, whose source child names the same kind of address. Videos typically load into the DOM straight away, depending on the browser's configuration, although some mobile browsers wait until the element is interacted with. The book states that this behaves the same as the image case. Its advice to the reader: watch for any tag that requests data from a server through a source attribute, because most of them can be turned into a CSRF vehicle.

## Why it works
- INTERPRETATION: the weakness is the same trust relationship as in WAS-C11-001. The server cannot tell a request the user meant to make from one the browser made while rendering content, because both carry the same session credentials.
- INTERPRETATION: the attacker only needs a place where their element will be rendered in the victim's browser. Figure 11-2 shows the element posted inside the target application itself; an attacker-run page or an email are other possible places.

## How to recognise and defend
- INTERPRETATION: any state-changing action reachable by GET is a candidate, because a GET can be provoked by any element that loads a URL.
- Defences are developed in Part III: checking the origin and referer headers (WAS-C23-001) and never changing server state in a GET request (WAS-C23-005).

## Relations
Builds on WAS-C11-001; the POST variant, which cannot use these tags, is WAS-C11-003.
