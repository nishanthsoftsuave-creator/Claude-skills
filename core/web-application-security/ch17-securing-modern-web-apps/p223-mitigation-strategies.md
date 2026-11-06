---
id: WAS-C17-008
title: Mitigation Strategies
source_pages: "223"
chapter: 17
concepts: [mitigation, secure-by-default, secure-coding-practices, ssdl, defense-in-depth, regression-framework]
related: [WAS-C17-007, WAS-C17-009, WAS-C18-001]
time_sensitive: false
---
# Mitigation Strategies
(Source: PDF p. 223; the closing sentence continues on the next page)

## What the section covers
The overall best practice for a security-friendly company: make an active, continuing effort to lower the chance that a vulnerability appears in the codebase at all, from the architecture phase through to regression testing.

## Meaning
- Mitigation is not one step but a practice that runs across the whole life cycle, from architecture design to the regression testing phase (PDF p. 223).
- The author pictures strategies as a net meant to catch as many fish as possible: they should be widespread. In crucial parts of an application they should also run deep.

## The forms mitigation takes
The book lists:
- Secure coding best practices.
- Secure application architecture.
- Regression testing frameworks.
- The secure software development life cycle (SSDL).
- A secure-by-default developer mindset and secure-by-default development frameworks.

The following chapters teach ways to mitigate, and sometimes to remove entirely, the risk a specific vulnerability type brings (PDF p. 223).

## Benefits
Practicing all of the steps in the chapter greatly improves the security of any codebase. The final sentence of the section, printed on the next page, adds that doing so removes large risk from the organization, saves money and protects against brand damage that would otherwise arrive in due time. It carries no page cite here.

## When and how to apply
INTERPRETATION: pair broad, cheap defaults (framework settings, linters) with deeper controls on the most sensitive code paths, as the net image suggests.

## Relations
Builds on regression testing (WAS-C17-007) and closes the list of defensive steps before the note on applied recon (WAS-C17-009). Architecture is developed further in WAS-C18-001.
