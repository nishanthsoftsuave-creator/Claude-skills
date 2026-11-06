---
id: WAS-C04-002
title: The Browser's Built-In Network Analysis Tools
source_pages: "86-88"
chapter: 4
concepts: [browser-devtools, network-tab, xhr-requests, subdomain-discovery, request-inspection, side-channel-timing, passive-recon]
related: [WAS-C04-001, WAS-C04-003, WAS-C05-001]
time_sensitive: true
---
# The Browser's Built-In Network Analysis Tools
(Source: PDF pp. 86-88)

## What the section covers
How to find API hosts and other subdomains simply by using the target application and watching the network requests the browser makes, using the developer tools that ship with every major browser.

## Meaning
- The starting idea is to walk through the visible functionality of the application, here MegaBank, and observe which API requests happen in the background. This often reveals a few easily found endpoints (PDF p. 86).
- The requests can be watched in the browser's own network tools, or with a heavier tool; the text names Burp, PortSwigger and ZAP as examples. The book itself avoids specialised tools and relies on the browser (PDF p. 86).
- Figure 4-2 shows the network tab of the developer tools on a Wikipedia page, with an asynchronous HTTP request made to the Wikipedia API. The tools can view, modify, resend and record requests, and the text says such free tools are more capable than many paid network tools were ten years earlier (PDF pp. 86-87).

## Why it matters
- The tools bundled with Chrome, Firefox and Edge are described as so capable that a person can become a proficient hacker without buying third-party tools (PDF p. 87).
- Besides network analysis they provide code analysis, runtime analysis of JavaScript with breakpoints and file references, accurate performance measurement, and minor security and compatibility audits. Performance measurement can itself serve as a hacking tool in side-channel attacks (PDF p. 87).

## How it works: opening the Network tab (Chrome)
1. Open the browser's settings menu with the three-dots control at the top right.
2. Under "More tools", choose "Developer tools".
3. Click the "Network" tab; widen the tools panel if the tab is hidden (PDF p. 87).
Then navigate between pages of any site while the tab is open. New HTTP requests appear, mixed in with many other requests (PDF p. 87).

## Reading the results
- The Network tab shows all traffic the browser handles, which is intimidating on a large site (PDF p. 88).
- The most interesting view is usually the XHR filter beneath it. It lists POST, GET, PUT, DELETE and similar calls made to servers and hides fonts, images, videos and dependency files. Clicking a request in the left pane gives details (PDF p. 88).
- Figure 4-3 is a capture of that XHR-filtered list: each row gives a name, status (for example 200 or 204), type, initiator, size, time in milliseconds and a waterfall bar, with names such as login and an unread-message-count call plus requests to the host of the site being used (the capture is from a large social site, not the bank) (PDF p. 88).
- Selecting a request shows raw and formatted request headers and body. The Preview tab shows a pretty-printed API result, the Response tab the raw payload, and the Timing tab queuing, downloading and waiting times (PDF p. 88).
- The timing metrics matter because a side-channel attack relies on a secondary signal other than the response itself to gauge what code is running on a server, for example the difference in load time between two scripts on a server that are reached through the same endpoint (PDF p. 88).
- The tooling looks daunting but is described as not hard to learn, and readers are encouraged to start using it for recon (PDF p. 88).

## Continuation
The section ends on the next page, where the tester is told to follow a request's headers down to the request URL to see which domain it was sent to or came from. That is often all that is needed to find a site's affiliated servers. This closing sentence sits at the top of the next page, above the next heading, so it carries no page cite here.

## Time-sensitive statements
The menu path and tab names are for Chrome at the time of writing, and the comparison with paid tools of "ten years ago" is dated to the book's writing.

## Relations
Follows WAS-C04-001 and precedes the public-records techniques in WAS-C04-003. The same dev-tools workflow is reused for endpoint discovery in WAS-C05-001.
