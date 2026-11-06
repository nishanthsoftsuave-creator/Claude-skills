---
id: WAS-C22-001
title: Anti-XSS Coding Best Practices
source_pages: "267-268"
chapter: 22
concepts: [xss-defence, dom-injection, string-detection, string-like-objects, innertext, innerhtml, user-supplied-data, secure-coding]
related: [WAS-C22-002, WAS-C22-012, WAS-C10-002, WAS-C10-005, WAS-C20-002]
time_sensitive: false
---
# Anti-XSS Coding Best Practices
(Source: PDF pp. 267-268, with the end of the section on the tail page 269)

## What the section covers
The chapter opening and its central coding rule for defending against XSS: do not let user-supplied data reach the DOM except as text. It also shows how to check that a value is a string or string-like, and why innerText is safer than innerHTML.

## Why it matters
Part II showed XSS exploiting the browser's ability to run JavaScript on a user's device. XSS is widespread and can do a lot of damage because script execution has such a wide range of possible effects. The book's reassurance is that it is also easy to mitigate or prevent through secure coding and XSS-specific techniques, and the chapter is about protecting a codebase from it (PDF p. 267).

## The central rule
- The one rule that dramatically lowers the chance of XSS in a team's code: do not allow any user-supplied data to be passed into the DOM except as strings (PDF p. 267).
- Many applications have features that move user data into the DOM, so the rule is restated more narrowly: never pass unsanitised user-supplied data into the DOM (PDF p. 267).
- Putting user data into the DOM should be a last-resort fallback, not the first option, because that functionality leads to accidental XSS. Where other options exist, choose them (PDF p. 267).
- When user data must reach the DOM, pass it as a string if possible. Where HTML or DOM is not required and the data is displayed as text, make sure it is interpreted as text and not as DOM (PDF p. 267). Figure 22-1 is a flowchart: the user enters text, JavaScript tries to append it to the DOM, and the branch "append as text" ends in Safe while "append as DOM" ends in Compromised. The caption says most, but not all, XSS comes from user-supplied text being wrongly injected into the DOM (PDF p. 268).

## How to check for strings
- These checks can be made in many ways, on client and server (PDF p. 268).
- String detection in JavaScript is easy: a value is a string if its type is string or it is an instance of the String object (PDF p. 268).
- That check fails for numbers, which are also safe to put in the DOM. The book therefore groups strings and numbers as "string-like" objects (PDF p. 268).
- To test for string-like values it uses a side effect of JSON.parse: parse the value, convert it back to text, and compare it with the original, catching errors and logging that the value is not string-like. Numbers and strings pass; complex objects such as functions fail, because they do not fit JSON (PDF p. 268).
INTERPRETATION: as printed, the comparison works for values that are valid JSON text, so a plain unquoted word would be rejected by the parser. Treat the helper as an illustration of the idea.
- Even a string or string-like value must still be interpreted by the DOM as a string. String objects are not DOM themselves, but can be interpreted as, or converted to, DOM, which is to be avoided (PDF p. 268).

## innerText versus innerHTML (tail page)
- User data generally enters the DOM through innerText or innerHTML. If HTML tags are not needed, innerText is much safer because it tries to sanitise anything that looks like a tag by showing it as a string (PDF p. 269).
- The less safe example assigns a string containing a bold tag to innerHTML, and the tags are interpreted as DOM; the safer example assigns it to innerText, and the tags appear as text (PDF p. 269).
- The best practice is to use innerText whenever you append true strings or string-like values. innerHTML does no such sanitising and treats tags as tags (PDF p. 269).
- innerText is not failsafe. Each browser implements it a little differently, and a quick search finds current and historical bypasses (PDF p. 269).

## Relations
Opens the XSS defence chapter. When tags must be allowed, see sanitising in WAS-C22-002. The attack side is in WAS-C10-002 and WAS-C10-005, and static detection of innerHTML use is in WAS-C20-002. The chapter's recap is WAS-C22-012.
