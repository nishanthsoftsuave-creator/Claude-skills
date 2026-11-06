---
id: WS-C15-006
title: Securing Your XML Parser
source_pages: "178-179"
chapter: 15
concepts: [disable-inline-dtd, hardened-parser, defusedxml, nokogiri, nodejs-xml, java-secure-processing, dotnet-prohibitdtd, dependency-tree]
related: [WS-C15-004, WS-C15-005, WS-C15-007, WS-C14-002]
time_sensitive: true
---
# Securing Your XML Parser
(Source: PDF pp. 178-179; the text at the top of PDF p. 178 above the "Securing Your XML Parser" heading is the end of WS-C15-005 and is not covered here)

## What the section covers
The single fix for XML bombs and external entity attacks, and how to apply it in Python, Ruby, Node.js, Java and .NET.

## Meaning
- The fix is simple: turn off processing of inline DTDs in the parser configuration. DTDs are a legacy technology and inline DTDs are "a bad idea, period" (PDF p. 178).
- Many modern parsers are hardened by default, which means they ship with the attackable features disabled, so you may already be safe. If unsure, check which XML parsing technology you use (PDF p. 178).
- Even if your own code never parses XML, your third-party dependencies probably do. Analyze the whole dependency tree to see which libraries get loaded when the web server starts (PDF p. 178).

## When and how to apply: per language
- Python: the defusedxml library explicitly rejects inline DTDs and is a drop-in replacement for the standard XML parsing library, so use it instead of the standard module (PDF p. 179).
- Ruby: the de facto parser is the Nokogiri library, hardened against XML attacks since version 1.5.4. Make sure you use that version or higher (PDF p. 179).
- Node.js: several modules exist, including xml2js, parse-xml and node-xml. Most skip DTD processing by design, but consult the documentation of the one you use (PDF p. 179).
- Java: spec-compliant parsers usually start from the DocumentBuilderFactory class. Listing 15-7 secures it wherever it is created: make the factory with its default constructor method, then set the secure-processing feature (XMLConstants.FEATURE_SECURE_PROCESSING) to true (PDF p. 179).

```
DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
factory.setFeature(XMLConstants.FEATURE_SECURE_PROCESSING, true);
```

- .NET: parsing classes live in the System.Xml namespace. XmlDictionaryReader, XmlNodeReader and XmlReader are safe by default, as are XElement and XDocument from System.Xml.Linq. XmlDocument, XmlTextReader and XPathNavigator have been secured since .NET 4.5.2. On an earlier version, switch to a secure parser or disable inline DTD processing; Listing 15-8 does so by setting the ProhibitDtd flag on an XmlTextReader to true (PDF p. 179).

```
XmlTextReader reader = new XmlTextReader(stream);
reader.ProhibitDtd = true;
```

## Time-sensitive statements
Library and framework version facts (Nokogiri 1.5.4, .NET 4.5.2, the named Node.js modules and the ProhibitDtd flag) are the book's statements as of its writing; they may have changed since, and the book gives no later update.

## Relations
Remedies the attacks of WS-C15-004 and WS-C15-005; complements the defence-in-depth advice in WS-C15-007 and the dependency advice of chapter 14 (WS-C14-002).
