---
id: WAS-C12-002
title: XML External Entity - Indirect XXE
source_pages: "177"
chapter: 12
concepts: [xxe, indirect-xxe, hidden-xml, crm-integration, legacy-integration, soap, recon, xml-parser]
related: [WAS-C12-001, WAS-C12-003, WAS-C06-005, WAS-C24-001]
time_sensitive: false
---
# XML External Entity: Indirect XXE
(Source: PDF p. 177, plus the part of PDF p. 178 above the next heading)

## What the section covers
The indirect form of XXE: the user sends something that is not XML, but the server builds XML from it and parses that XML.

## Meaning (PDF p. 177)
- With indirect XXE, some request makes the server generate an XML object that contains parameters supplied by the user, which can include an external-entity tag.
- Figure 12-2 (PDF p. 177) shows the loop: the user sends a payload containing an external-entity directive as a parameter; the server makes an XML file and fits the user's parameters into it; an XML parser reads it; the external entity is resolved and a file from the server comes back in the result; the file and the request's result go back to the user.
- So an endpoint can be vulnerable even though it does not accept XML. The book says a natural first reaction is to try an XXE payload on an endpoint that takes an XML-like object, but an endpoint without an XML payload may still use an XML parser.
- The book's use case: a developer writes an application that asks for a single parameter through a REST endpoint, to be synchronised with an enterprise-grade CRM package already used by the company.

## Continuation (PDF p. 178)
The section carries on over the page break. The CRM may expect XML, so the REST server has to convert the user's parameter into XML before passing it on. This often happens out of view, which makes it hard to see that XML is involved, and it is common because companies upgrade piecemeal, so modern JSON/REST APIs end up talking to XML/SOAP systems. The book suggests ways to detect this without insider knowledge: research the company's large enterprise licences, which are sometimes public; look for other pages that show data from a separate system or domain; and use knowledge of the data-type limits of old CRM, accounting or HR packages to spot oddly formatted fields in a public API.

## How to recognise and defend
- INTERPRETATION: any value that is carried onward into an integration that speaks XML.
- Defence follows WAS-C12-001's: configure every XML parser in the chain to reject external entities (WAS-C24-001), including the one hidden behind an integration.

## Relations
Compare the direct case in WAS-C12-001. Recon techniques for finding out what runs behind a server appear in WAS-C06-005.
