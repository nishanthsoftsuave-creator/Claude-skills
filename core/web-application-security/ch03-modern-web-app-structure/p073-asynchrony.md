---
id: WAS-C03-009
title: Asynchrony
source_pages: "73-75"
chapter: 3
concepts: [asynchrony, callbacks, promises, async-await, synchronous-programming, network-latency, javascript-concurrency, error-handling]
related: [WAS-C03-008, WAS-C03-010, WAS-C04-008]
time_sensitive: false
---
# Asynchrony
(Source: PDF pp. 73-75 from the "Asynchrony" heading, plus the top of PDF p. 76 above "Browser DOM")

## What the section covers
Why network programming on the web relies on asynchronous code, and the three generations of JavaScript syntax for it: callbacks, promises and async functions.

## Meaning
- Asynchrony is described as one of those "hard to figure out, easy to remember" concepts that recur in network programming. Browsers constantly communicate with servers and the time between request and response varies with payload size, latency and server processing, so the web handles that variation asynchronously (PDF p. 73).
- In a **synchronous** model operations run in the order they occur. Three log calls for "a", "b", "c" always print in that order (PDF p. 73).
- In an **asynchronous** model the interpreter reads the three calls in order, but they may not resolve in the same order. With an asynchronous log function the book shows three attempts: the first and third print a, b, c; the second prints a, c, b (PDF p. 73).

## Why it matters
Network requests take variable time, time out and behave unpredictably. Rather than waiting for one request to finish before starting another, JavaScript applications start them together and define in advance what to do on resolution. The book says this can be dozens of times faster than the synchronous alternative (PDF p. 74).

## How it works: three styles
1. **Callbacks** (older JavaScript). The example fetches a user, then the user's profile, then sets a profile configuration, then logs "success!", with each step nested in the previous step's function. Callbacks are very fast and efficient compared to a synchronous model but very difficult to read and debug (PDF p. 74).
2. **Promises.** A later philosophy was a reusable object that calls the next function when the previous one finishes. The same flow is rewritten with a promise whose steps are chained with then and a final catch (PDF pp. 74-75). The logic is identical to the callback version; the difference is readability and organisation. The promise version grows vertically rather than horizontally and makes error handling easier. Promises and callbacks are interoperable and can be mixed by programmer preference (PDF p. 75).
3. **Async functions** (the latest approach). They are designed to make asynchrony easy. In the example, an async function awaits the user, then the user profile, then the profile update. Each `await` halts execution within that function until the call resolves, while code outside the function runs normally. This is easier to read, which is the point (PDF p. 75).

## Further points
The async function effectively turns a normal function into a promise. The author expects to see these more and more in client-side code and JavaScript-based server-side code (PDF p. 76).

## Limitations and notes on the listings
INTERPRETATION: the printed listings use identifiers (such as the privacy value and the resolve and reject functions) that are not defined inside the snippets, so they illustrate structure, not runnable code as printed.

## Relations
The previous language topics are in WAS-C03-005 through WAS-C03-008. The brute-force subdomain code in Chapter 4 uses promises to fire many DNS queries at once (WAS-C04-008). The browser DOM comes next (WAS-C03-010).
