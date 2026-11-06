---
id: WAS-C11-001
title: CSRF and Query Parameter Tampering
source_pages: "163-167"
chapter: 11
concepts: [csrf, cross-site-request-forgery, http-get, query-parameters, session-cookie, privilege-escalation, link-distribution, express-routes]
related: [WAS-C11-002, WAS-C11-003, WAS-C11-004, WAS-C10-004, WAS-C23-001, WAS-C23-005]
time_sensitive: false
---
# CSRF and Query Parameter Tampering
(Source: PDF pp. 163-167)

## What the section covers
The chapter introduction on Cross-Site Request Forgery (CSRF), followed by the simplest form of the attack: tampering with query parameters in a hyperlink that triggers an HTTP GET request.

## Meaning and framing (PDF p. 163)
- Sometimes a tester knows an endpoint exists that would do what is wanted, but cannot call it because it needs privileged access such as an admin account.
- The chapter builds CSRF exploits that make an admin or other privileged account perform an operation on the attacker's behalf, instead of using a JavaScript snippet as in XSS.
- CSRF exploits how browsers work and the trust between a website and the browser. By finding API calls that give the browser too much trust, an attacker can craft links and forms that make a user send requests as themselves without knowing it.
- Such requests happen behind the scenes, so the attack often goes unnoticed. It can abuse a privileged user without their knowledge, is among the stealthiest attacks, and has caused havoc since the early 2000s.

## Anatomy of a GET request (PDF p. 164)
- Most hyperlinks on the web trigger an HTTP GET. A valid GET follows a supported version of the HTTP specification, so its structure is the same everywhere.
- It consists of the method, a resource URL, optional query parameters (starting at a question mark and running to whitespace), the protocol version, and on the next line the host.
- The web server routes the request to a handler that receives the parameters plus information about who made the request, which browser they used and what data format they expect back.
- Figure 11-1 shows the CSRF GET chain: an attacker makes a malicious link aimed at a GET endpoint and distributes it by email or website; a second user clicks it; a GET is made on that user's behalf; the server processes it with that user's authentication cookie; and server state changes without the user being aware.

## A concrete route (PDF pp. 165-166)
- The book's first server example is an Express.js route for an account path. It accepts only GET, answers with a 400 error if no query is supplied, and otherwise reflects the query back in JSON.
- SUPPLEMENTARY: in Express the request's query value defaults to an empty object, which counts as present, so this exact check would not trigger the 400 case; the walkthrough assumes it does (Express documentation for the request query property).
- A browser script sending a GET to that path with no query gets the 400 result; adding an id parameter gets the same value back and a 200 status.

## Two marks of a CSRF attack (PDF p. 166)
- Privilege escalation.
- The user whose account sends the request typically does not know it happened.

Most create, read, update, delete web applications use many HTTP verbs, but GET is the least secure and the easiest to turn into a CSRF attack. Both the browser's URL bar and anchor links start GETs. People rarely inspect where a link goes, so a link that shows "My Website" can carry a hidden parameter; whoever clicks it sends that parameter to the server.

## The bank example (PDF pp. 166-167)
- MegaBank has a transfer route that uses GET with parameters. It checks that the session is authenticated and that a target user and an amount are present, runs the transfer from the current user to the named user, and returns a JSON confirmation.
- It looks sound because the user had to be authenticated, so it assumes the request was made by that user for the intended amount and recipient.
- Since it is a GET, a hyperlink to this route can be crafted and sent to an authenticated user.

## Typical steps of a GET parameter attack (PDF p. 167)
1. The hacker discovers that a server uses GET parameters to steer its logic, here the amount and target of a transfer.
2. The hacker builds a URL carrying those parameters, naming the hacker's own account and an amount of 10,000.
3. The hacker chooses distribution: targeted (who is most likely logged in with enough funds) or bulk (reach many people quickly before detection).

Distribution is often by email or social media, and the book notes hackers have even paid for web advertising to spread such links. Because distribution is easy, the damage to a company can be severe.

## Relations
Variations that avoid needing a click are in WAS-C11-002, and a POST version is in WAS-C11-003. The idea of an attacker-crafted URL parameter also appears in reflected XSS (WAS-C10-004). Defenses are in WAS-C23-001 (header checks) and WAS-C23-005 (keeping GET requests free of state changes).
