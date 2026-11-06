---
id: WAS-C18-006
title: PII and Financial Data
source_pages: "233"
chapter: 18
concepts: [pii, financial-data, credit-card-numbers, data-protection-law, data-breach, data-outsourcing, megamerch]
related: [WAS-C18-001, WAS-C18-005, WAS-C18-007]
time_sensitive: false
---
# PII and Financial Data
(Source: PDF p. 233)

## What the section covers
The architectural concerns that come with storing personally identifiable information and financial data such as card numbers.

## Meaning and concerns
- Personally identifiable information (PII) about a user may only be stored if that storage is legal in the countries where the application operates, and if the operator follows the laws that apply to PII there (PDF p. 233).
- Beyond legality, the operator wants a database breach or server compromise not to expose the PII in a form that is easy to abuse.
- Financial data such as credit card numbers follows similar rules to PII, and in some countries is covered by PII laws directly.

## Alternatives and trade-offs
- A smaller company may decide that, rather than storing PII and financial details itself, it is better to outsource their storage to a compliant business that specializes in that kind of data (PDF p. 233).

## When and how to apply
INTERPRETATION: for MegaMerch, the requirements list in WAS-C18-001 holds names, addresses, dates of birth and saved cards, so this concern applies directly. List each PII and payment field, the country law that applies to it, and whether it truly needs to be stored at all before choosing between in-house and outsourced storage.

## Relations
Follows 2FA (WAS-C18-005). Comes from the risk areas set out in WAS-C18-001. The related concern about copies of data in a search index is in WAS-C18-007.
