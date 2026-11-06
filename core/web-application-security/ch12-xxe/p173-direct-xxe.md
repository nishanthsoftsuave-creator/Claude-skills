---
id: WAS-C12-001
title: XML External Entity - Direct XXE
source_pages: "173-176"
chapter: 12
concepts: [xxe, xml-external-entity, xml-parser, external-entity, svg, screenshot-feature, direct-xxe, file-disclosure]
related: [WAS-C12-002, WAS-C12-003, WAS-C03-002, WAS-C24-001, WAS-C24-003]
time_sensitive: false
---
# XML External Entity: Direct XXE
(Source: PDF pp. 173-176; the section's closing sentence is on the next page)

## What the section covers
The chapter introduction on XML External Entity (XXE) attacks, then the direct form, where the attacker sends XML straight to an endpoint, using a screenshot feature of the fictional bank as the example.

## Meaning (PDF p. 173)
- XXE is an attack classification that is often simple to carry out but has severe results. It relies on an improperly configured XML parser in the application's code.
- Almost every XXE vulnerability sits on an API endpoint that accepts an XML or XML-like payload. The book warns that endpoints taking XML may be commoner than assumed, since XML-like formats include SVG, HTML/DOM, PDF (XFDF) and RTF, and many XML parsers also accept them.
- The core of the attack is a feature of the XML specification: a special annotation for importing external files, called an external entity. It is resolved on the machine that evaluates the XML. A specially crafted payload sent to a server's XML parser can therefore expose files in that server's file structure.
- Typical uses are reading other users' files, or reading files that hold credentials needed for a Unix-based server to work.

## Direct XXE (PDF pp. 173-176)
- Figure 12-1 (PDF p. 174) shows the cycle: a user sends an XML payload to a server endpoint; a parser processes it; the external-entity directive is resolved and a file from the server is reflected into the parsing result; the local file, with the request's result, goes back to the user.
- The scenario (PDF pp. 173-175): the bank has a utility that lets customers send screenshots of their portal to customer support. The client page serialises part of its current DOM to XML, posts it to a utility service that converts XML to a JPG image, then sends that image to support through another API.
- The book notes the code has other flaws: for example the client could call the support-sending function with images of its own, and an image is harder to validate than XML.
- On the server a route takes the posted XML, runs it through an XML-to-JPG converter, and returns the image (PDF pp. 175-176). Conversion requires an XML parser that follows the XML specification.
- The payload the client sends is normally just DOM turned into XML, so ordinary use is harmless. But a tech-savvy user can alter the DOM sent, or forge the network request entirely and send a payload of their own.
- The book's forged request uses a hand-built XML string that exploits the external-entity facility, naming a sensitive local file of the server. The book says the server's parser evaluates the XML and returns an image, and that if the parser does not explicitly disable external entities, the text of that file shows up in the returned screenshot (PDF p. 177, the tail page).
- Handling note: this module describes what the example shows and leaves out the payload and the file's path.

## How to recognise and defend
- INTERPRETATION: endpoints that accept XML or XML-like uploads, or that convert such documents, are the ones to check first.
- The defence is covered in Part III: disable external entities in the parser (WAS-C24-001) and consider other data formats (WAS-C24-002).

## Alternatives and trade-offs
INTERPRETATION: chapter 24 (WAS-C24-002) compares JSON with XML; using JSON where the application does not need XML features avoids the XML parser, at the cost of features such as schema validation.

## Relations
The indirect variant is WAS-C12-002; chapter recap is WAS-C12-003; background on REST and XML versus JSON is WAS-C03-002.
