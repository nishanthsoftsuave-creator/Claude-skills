---
id: WAS-C19-005
title: Secure-Coding Anti-Patterns - Blacklists
source_pages: "243"
chapter: 19
concepts: [anti-patterns, blacklists, whitelists, incomplete-mitigation, domain-filtering, allowlist-maintenance, partner-vetting]
related: [WAS-C19-004, WAS-C19-006, WAS-C25-007]
time_sensitive: false
---
# Secure-Coding Anti-Patterns: Blacklists
(Source: PDF p. 243, with the end of the section on PDF p. 244 above the Boilerplate Code heading)

## What the section covers
The opening of the anti-pattern discussion and its first anti-pattern: using a blacklist where a whitelist is needed.

## Introduction to anti-patterns
- Security reviews at the code level share similarities with architecture reviews before code is written. They differ because code review is the real point at which to find vulnerabilities, whereas in architecture review the vulnerabilities are only hypothetical (PDF p. 243).
- Many anti-patterns are simply hastily built solutions, or solutions built without the right prior knowledge. Knowing how to spot them speeds up a review.
- The anti-patterns listed are all common, and each can cause serious damage if it reaches a production build.

## Meaning of the blacklist anti-pattern
- In security, temporary mitigations should often be ignored in favor of a permanent solution, even if that takes longer. A temporary or incomplete solution is acceptable only with a preplanned timeline for a complete one. Blacklists are an example of a temporary or incomplete solution (PDF p. 243).
- The book's example is a server-side filter for acceptable integration domains that stores an array of two bad domains and accepts any domain not in the array.
- It looks like a solution, but is incomplete unless every domain is known, and temporary because new bad domains can appear. A blacklist protects only with perfect knowledge of all current and future inputs; without it, a hacker can usually get around it, here by buying another domain.

## The preferred alternative
- Whitelists are always preferable in security. Flipping the check so that only domains in a short approved array are accepted makes the process much more secure (PDF p. 244).
- Engineers sometimes argue that whitelists make development harder because they need continual manual or automated upkeep as they grow. Manual upkeep is a burden, but combining manual and automated effort keeps most of the benefit and eases the work (PDF p. 244).
- In the example, requiring integrating partners to submit their website and business license for review before whitelisting makes it very hard for a malicious integration to slip in. If one did, removal from the list would make a return difficult, since it would need a new domain and license.

## When and how to apply
INTERPRETATION: when a code review finds a deny list guarding input, ask what the full set of acceptable values is and whether an allow list can replace it.

## Relations
Starts the anti-pattern series; next is boilerplate code (WAS-C19-006). The injection chapter on defending commands uses the same whitelist idea (WAS-C25-007).
