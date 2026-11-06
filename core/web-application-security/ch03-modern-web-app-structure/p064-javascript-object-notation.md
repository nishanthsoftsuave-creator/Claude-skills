---
id: WAS-C03-003
title: JavaScript Object Notation
source_pages: "64"
chapter: 3
concepts: [json, data-interchange-format, json-parse, client-server-communication, lightweight-format, human-readable-data, rest-data-format]
related: [WAS-C03-002, WAS-C03-004, WAS-C05-003, WAS-C24-002]
time_sensitive: false
---
# JavaScript Object Notation
(Source: PDF p. 64, plus the top of PDF p. 65 before the "JavaScript" heading)

## What the section covers
Why modern clients and servers need a standard in-transit data format, what JSON offers, a sample JSON record and its conversion into a JavaScript object, and the author's advice to become fluent at reading JSON.

## Meaning and background
- REST is an architecture specification that says how HTTP verbs map to resources on a server. Most REST APIs today use JSON as the format for data in transit (PDF p. 64).
- An application's API server must talk to its client, usually code in a browser or mobile app. Without a client/server relationship you cannot keep state across devices or keep it between accounts, because all state would have to live locally (PDF p. 64).
- Modern applications exchange a great deal of data downstream and send many requests upstream in the form of HTTP verbs, so ad hoc formats are not feasible. The in-transit format has to be standardised (PDF p. 64).

## Why JSON fits
JSON is an open-standard (not proprietary) file format. The book lists the properties that suit it (PDF p. 64):
- very lightweight, which reduces network bandwidth;
- needs very little parsing, which reduces server and client load;
- easy for humans to read;
- hierarchical, so it can represent complex relationships between data;
- written very similarly to JavaScript objects, which makes consuming JSON and building new JSON in the browser easy.

All major browsers parse JSON natively and quickly, which together with the points above makes it a good format for moving data between a stateless server and a browser (PDF p. 64).

## How it works: example
- The sample record (PDF p. 64) describes a person with first and last name, email, role (an engineering manager), company, and a nested location object holding country, state, address and a numeric zip code.
- On the browser side the record arrives as a string and one call to the built-in JSON parse function turns it into a JavaScript object (PDF p. 65). In the printed listing the email line lacks the colon between key and value, so as printed that string would not parse; treat it as a typo in the book's listing.

## Trade-offs
JSON is flexible, lightweight and easy, but like any lightweight format it has trade-offs against heavyweight alternatives. The book defers the specific security differences between JSON and its competitors to later chapters, and for now only asks the reader to grasp that a significant number of browser-to-server requests are sent as JSON (PDF p. 65).

## When and how to apply
- Get comfortable reading JSON strings, and consider a browser or editor plug-in that formats JSON. Being able to scan for specific keys quickly is valuable when penetration testing many APIs in a short time (PDF p. 65).

## Relations
Follows the REST discussion (WAS-C03-002) and leads into the JavaScript language overview (WAS-C03-004). Recording recon notes in a JSON-like shape appears in WAS-C02-002, and the XML-versus-JSON security comparison appears in the XXE defence chapter (WAS-C24-002).
