---
id: WAS-C03-017
title: Client-Side Data Stores
source_pages: "82"
chapter: 3
concepts: [client-side-storage, local-storage, session-storage, indexeddb, same-origin-policy, browser-state, sensitive-data-exposure]
related: [WAS-C03-016, WAS-C03-018, WAS-C03-013, WAS-C03-001]
time_sensitive: false
---
# Client-Side Data Stores
(Source: PDF p. 82 from the "Client-Side Data Stores" heading; the section continues on the next PDF page)

## What the section covers
How applications keep state in the browser: local storage, its session-scoped variant and, on the following page, IndexedDB.

## Why client storage is growing
Traditionally very little data was stored on the client because of technical limits and cross-browser compatibility issues. That is changing rapidly. Many applications now keep significant application state on the client, often as configuration data or large scripts that would cause network congestion if downloaded on every visit (PDF p. 82).

## How it works
- **Local storage** is a browser-managed container for key/value data. It follows the browser-enforced Same Origin Policy (SOP), which stops other domains (websites) from reading each other's locally stored data. A web application can therefore keep state even when the browser or tab is closed (PDF p. 82).
- Figure 3-6 (rendered and read) shows the console demonstrating it. A call stores an item named "vehicle" whose value is an object with make "Honda", model "Civic" and year "2003"; the console returns undefined. Printing the storage object shows length 1 and the key vehicle holding the string "[object Object]", and reading the item back returns that same string. The figure therefore shows that the object was converted to a text string when stored (PDF p. 82).
  INTERPRETATION: structured values therefore have to be serialised by the application before they are stored.
- **Session storage** is called a subset of local storage. It operates identically but persists data only until the tab is closed. The book suggests it for data that is more critical and should not persist if another user uses the same machine (PDF p. 82).

## Continuation on the next page
The section carries on past this row's range, without a heading change. It warns that in poorly architected applications client-side stores may reveal sensitive information such as authentication tokens or other secrets. It then introduces IndexedDB, a JavaScript-based object-oriented database supported by all major browsers that can store and query asynchronously in the background. Because it can be queried it offers a far more powerful developer interface than local storage, and it is used in web-based games and interactive applications such as image editors. Typing a short check for the indexedDB property in the developer console shows whether the browser supports it.

## When and how to apply
INTERPRETATION: treat local and session storage as readable by any script running in the page, so one XSS flaw can expose whatever is kept there. Look for tokens and configuration in them during recon.

## Relations
Server-side counterparts are in WAS-C03-016. Authentication tokens, which should not be left in readable storage, are discussed in WAS-C03-013. The chapter's closing synthesis is WAS-C03-018.
