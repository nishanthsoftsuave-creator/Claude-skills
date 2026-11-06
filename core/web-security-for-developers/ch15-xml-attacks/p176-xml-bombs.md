---
id: WS-C15-004
title: XML Bombs
source_pages: "176"
chapter: 15
concepts: [xml-bomb, billion-laughs, internal-entity, entity-expansion, denial-of-service, inline-dtd, memory-exhaustion]
related: [WS-C15-003, WS-C15-005, WS-C15-006, WS-C17-002]
time_sensitive: false
---
# XML Bombs
(Source: PDF p. 176, tail PDF p. 177. The text at the top of PDF p. 176 above the "XML Bombs" heading is the end of WS-C15-003. The text on PDF p. 177 above the "XML External Entity Attacks" heading belongs here.)

## What the section covers
How an inline DTD can make a parser's memory use explode, built up from the harmless internal entity feature to the nested "billion laughs" example.

## Meaning
- An XML bomb uses an inline DTD to blow up an XML parser's memory use. The goal is to exhaust all memory on the server so it crashes and goes offline (PDF p. 176).
- The attack relies on internal entity declarations: simple string-substitution macros defined in the DTD and expanded at parse time. If a snippet of text recurs, you declare it once and use the entity name as shorthand (PDF p. 176).

## How it works
- Listing 15-3 is an employee-records document whose DTD declares an entity named company with the value "Rock and Gravel Company". Two employee entries each reference that entity by name, written with an ampersand before and a semicolon after (PDF p. 176).
- On parsing, every reference is replaced by the declared text. Listing 15-4 shows the resulting document, with the company name written out in both employee entries and no DTD left (PDF p. 176).
- Internal entities are useful but rarely used. Trouble starts when one internal entity refers to other internal entities (PDF p. 177).
- Listing 15-5 is the billion laughs attack. It declares an entity lol holding the text "lol", then lol2 as ten copies of lol, lol3 as ten copies of lol2, and so on up to lol9 as ten copies of lol8. The document body is a single lolz tag containing a reference to lol9 (PDF p. 177).
- Parsing expands lol9 into ten lol8 references, each of those into ten lol7 references, and so on down. The final tag holds over a billion occurrences of the string, and this short file needs more than 3 GB of memory when the DTD is fully expanded, enough to crash the parser (PDF p. 177).

## Why it matters
- Using up the parser's memory takes the web server offline, so an XML bomb is an effective denial-of-service attack (PDF p. 177).
- The attacker only needs to find a URL on your site that accepts XML uploads and can then knock you offline "with a click of a button" (PDF p. 177).
- Parsers that accept inline DTDs have a second, sneakier weakness based on a different use of entity definitions, covered in WS-C15-005 (PDF p. 177).

## Limitations and failure modes
The bomb's input is tiny while its expanded size is huge, which is the same request-versus-processing asymmetry that denial-of-service attacks generally exploit (WS-C17-002). The defence is to disable inline DTD processing (WS-C15-006).

## Relations
Follows WS-C15-003; the chapter 17 list of application-layer attacks refers back to XML bombs (WS-C17-002).
