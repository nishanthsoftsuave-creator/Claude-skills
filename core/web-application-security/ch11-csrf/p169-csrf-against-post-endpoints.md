---
id: WAS-C11-003
title: CSRF Against POST Endpoints
source_pages: "169-170"
chapter: 11
concepts: [csrf, http-post, web-forms, hidden-form-fields, user-interaction, internal-network, disguised-forms, privilege-escalation]
related: [WAS-C11-001, WAS-C11-002, WAS-C11-004, WAS-C23-001, WAS-C23-002]
time_sensitive: false
---
# CSRF Against POST Endpoints
(Source: PDF pp. 169-170; the section's last two paragraphs are printed on the next page)

## What the section covers
CSRF is mostly aimed at GET endpoints, but POST, PUT and DELETE endpoints can also be reached. The section explains how a web form can do this and what extra effort it takes.

## Meaning (PDF p. 169)
- GET endpoints are the usual target because a link, image or other tag can send a GET automatically (WAS-C11-002). A payload against POST, PUT or DELETE takes more work and some mandatory user interaction.
- CSRF through POST is typically built from a browser form, because the form element is one of the few HTML objects that can start a POST without any script.
- The book's example is a form whose action is the bank's transfer route and whose method is POST. It holds hidden inputs for the destination user and the amount, plus a submit button. Hidden inputs let the author seed values that the browser does not display.

## Disguising the form (PDF p. 170)
- Figure 11-3 shows the flow: User #1 builds a malicious form on their own website and distributes it by email; User #2 clicks the link, fills in the form and submits; an HTTP POST is sent to another server; the server processes the POST; application state changes even on an internal network that only User #2 can reach.
- The attacker can make the victim cooperate by adding genuine-looking visible fields next to the hidden ones. The book's example shows a username field and a password field. The user thinks they are logging in to some website, but submitting the form actually sends a request to the bank, and no login is ever attempted.
- The lesson: legitimate-looking HTML components can send requests that ride on the user's current application state in the browser. The user is signed in to the bank, is interacting with an unrelated site, and still the attacker gets elevated operations performed in the user's session.
- UNVERIFIED: the boxes of Figure 11-3 (PDF p. 170) are inconsistent about who the request is made for. One box says the POST is made on behalf of User #1 while the next says the server processes it on behalf of User #2. From the surrounding text, User #2 (the person who submits) is the one whose session is used, but the book does not reconcile the two labels.

## Reaching internal servers (continues on the next page)
The section ends on the following page with two points. A form's creator cannot send requests to servers on an internal network, but a user who is on that network and submits the form sends the request with their own network access, so an internal server can be reached. The book adds that this POST type is more complex than seeding a GET through an anchor tag, but is sometimes needed against a POST endpoint, and forms are then the easiest route.

## How to recognise and defend
- INTERPRETATION: every state-changing POST that relies only on the session cookie, with no secret unique to the user's page, is exposed.
- Defences are in Part III: header verification (WAS-C23-001) and anti-CSRF tokens (WAS-C23-002).

## Relations
Follows WAS-C11-002; chapter wrap-up is WAS-C11-004; the earlier GET material is WAS-C11-001.
