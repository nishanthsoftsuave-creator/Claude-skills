---
id: WAS-C24-002
title: Evaluating Other Data Formats
source_pages: "288"
chapter: 24
concepts: [xml-versus-json, data-format-choice, schema-validation, payload-size, xxe-avoidance, yaml, bson, edn]
related: [WAS-C24-001, WAS-C03-003, WAS-C12-001]
time_sensitive: false
---
# Evaluating Other Data Formats
(Source: PDF pp. 288-289)

## What the section covers
Whether an application can sidestep XXE altogether by using a data format other than XML, with the book's comparison of XML and JSON.

## Why it matters
Depending on use cases, an application may be re-architected to use another format. That can simplify the codebase and remove XXE risk. XML is usually swappable with JSON, so JSON is the default alternative considered (PDF p. 288).

## When and how to apply
JSON is not practical when the application really parses XML, SVG or other XML-derived files. It is practical when the payloads are ordinary hierarchical data that merely happen to be shaped as XML (PDF p. 288).

## Alternatives and trade-offs
Table 24-1 compares the two (PDF p. 288):

| Category | XML | JSON |
|---|---|---|
| Payload size | Large | Compact |
| Specification complexity | High | Low |
| Ease of use | Needs complex parsing | Simple parsing, JavaScript-friendly |
| Metadata support | Yes | No |
| Rendering via HTML-like structure | Easy | Difficult |
| Mixed content | Supported | Unsupported |
| Schema validation | Supported | Unsupported |
| Object mapping | None | JavaScript |
| Readability | Low | High |
| Comment support | Yes | No |
| Security | Lower | Higher |

The text draws three takeaways: JSON is much lighter; it is less rigid but faster and easier to work with; and it maps onto JavaScript objects while XML maps onto DOM trees. It concludes JSON suits lightweight structured data that JavaScript will interpret, while XML remains better when the payload will eventually be rendered (PDF p. 288).

The next page adds that XML's schema validation helps where a rigid structure is needed, whereas JSON's looseness suits APIs under ongoing development because the client-server contract needs less upkeep. XML's risk comes mostly from the power of its specification, which can pull in external files and multimedia, so it is naturally less secure than JSON's plain key/value strings. Organizations unwilling to adopt JSON can consider YAML, BSON or EDN, but each needs a similar analysis first (PDF p. 289).

## Relations
Follows the parser fix in WAS-C24-001; JSON is introduced in WAS-C03-003 and the attack in WAS-C12-001.
