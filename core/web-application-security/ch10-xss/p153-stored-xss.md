---
id: WAS-C10-003
title: Stored XSS
source_pages: "153-154"
chapter: 10
concepts: [stored-xss, persistent-xss, database-storage, detection, scanning, csp, mitigation-limits]
related: [WAS-C10-002, WAS-C10-004, WAS-C10-005, WAS-C22-001]
time_sensitive: false
---
# Stored XSS
(Source: PDF pp. 153-154, plus the part of PDF p. 155 above the next heading)

## What the section covers
What makes a stored XSS attack distinctive, why it is often the most dangerous variety, why it is also the easiest to spot, and why scanning stored data is a useful but incomplete mitigation.

## Meaning
- A stored XSS attack is one where the malicious payload is kept in the application's database and served to users later. The book calls it probably the most common type of XSS (PDF p. 153).
- The only requirement for the "stored" label is that the payload lives in the database. The payload does not have to be valid JavaScript, and the client does not have to be a web browser (PDF p. 155).

## How it works (PDF pp. 153-154)
Figure 10-1 describes the chain. One user submits a form, the API receives the data and stores it in the database, a second user asks to view the first user's data, the API fetches it from the database and sends it to the second user's client, the data is injected into the browser's DOM, and a script inside the data is read as a script and runs on the second user's device (PDF p. 154).

## Why it matters
- A stored database object can be seen by many users, and a globally shown object can expose every user. The book's example: if a video-hosting site features a video on its front page, an XSS hidden in that video's title could hit every visitor for as long as the video stays featured (PDF p. 154).
- For this reason, the book says stored XSS can be extremely deadly to an organisation.

## Detection and mitigation
- The permanence of a stored XSS makes it easy to detect. The script executes on the client, but it sits on the server side in a database as plain text and is not evaluated there. The book adds one exception: with some Node.js servers the stored text could be evaluated, which becomes remote code execution, a topic covered later (PDF p. 154).
- Because the text is stored server-side, regularly scanning database entries for signs of stored script is a cheap and efficient mitigation for sites that keep much user-provided data, and security-minded companies use it among several techniques (PDF pp. 154-155).
- It cannot be the final answer. Advanced payloads need not be plain text; they might be base64 or binary, or be kept in several places and become dangerous only when a specific service joins them for use in the client. Experienced hackers use such tricks to get around developers' defenses (PDF p. 155).
- The earlier example injected a script tag into the DOM, which is the most common approach and also the one most often stopped. A simple regular expression banning script tags, or a Content Security Policy rule against inline script execution, would have stopped that attack (PDF p. 155).

## Alternatives and wider scope
There are many alternatives to script tags that still lead to compromised data or script execution. Many clients also request data through a web server, so browsers are only the most common target of a stored XSS, not the only one (PDF p. 155).

## Relations
The setup scenario is in WAS-C10-002. The non-stored variants follow in WAS-C10-004 (reflected) and WAS-C10-005 (DOM-based). Defenses are developed at WAS-C22-001.
