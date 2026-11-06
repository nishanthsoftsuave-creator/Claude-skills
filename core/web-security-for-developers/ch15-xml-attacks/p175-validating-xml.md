---
id: WS-C15-003
title: Validating XML
source_pages: "175"
chapter: 15
concepts: [xml-validation, grammar, dtd, xsd, document-type-definition, inline-dtd, pcdata, bnf]
related: [WS-C15-002, WS-C15-004, WS-C15-005, WS-C15-006]
time_sensitive: false
---
# Validating XML
(Source: PDF p. 175, tail PDF p. 176. The text on PDF p. 176 above the "XML Bombs" heading is the end of this section and is covered here.)

## What the section covers
How an XML document's expected structure is described and checked, the two schema formats (DTD and XSD), what a DTD looks like, and why an inline DTD supplied by the document itself is the root of two attack families.

## Meaning
- An XML author may choose any tag names, so a reading application must be told which tags to expect and in what order. The expected structure is often written as a formal grammar, and the document is validated against it (PDF p. 175).
- A grammar file tells a parser which character sequences are valid expressions in the language. For a programming language, a grammar might say variable names are alphanumeric only and that an operator such as + needs two operands (PDF p. 175).
- XML has two main ways to describe expected structure (PDF p. 175):
  - A document type definition (DTD) resembles Backus-Naur Form notation, which is often used for programming-language grammars. (The book spells it "Bachus-Naur".)
  - An XML Schema Definition (XSD) is a more modern and more expressive alternative that can describe a wider set of documents; the grammar itself is written as an XML file.
- Both are widely supported by parsers. The book focuses on DTDs because they contain a couple of features that can expose a parser to attack (PDF p. 175).

## How it works: Listing 15-2
- A DTD specifies the tags, subtags and kinds of data expected. Listing 15-2 is a DTD for the book catalog of Listing 15-1 (PDF p. 175).
- It says the top-level catalog tag holds one or more book tags (the plus sign marks the quantity; the book's prose says "zero or more", though a plus sign normally means one or more). Each book tag holds author, title, genre and description tags and has an id attribute (PDF p. 175).
- Those tags and the attribute are expected to hold parsed character data (#PCDATA) or character data (CDATA), meaning text rather than further tags (PDF p. 175).
- Oddity recorded as printed: in the listing the author, title, genre and description declarations use the ENTITY keyword, while only catalog and book use ELEMENT, although the prose describes all of them as expected tags. The book does not comment on this (PDF p. 175).

## Why it matters: inline DTDs
- A DTD can be embedded inside the XML document so that the document validates itself (PDF p. 175).
- A parser that honors inline DTDs is vulnerable because a malicious uploader controls the DTD contents, instead of the parser supplying a trusted one (PDF pp. 175-176).
- Hackers have used inline DTDs for two things: making a document consume exponentially more server memory while it is parsed (an XML bomb), and gaining access to other files on the server (an XML external entity attack). The next rows explain these (PDF p. 176).

## Relations
Follows WS-C15-002. The memory attack is WS-C15-004, the file and network attack is WS-C15-005, and the remedy is WS-C15-006.
