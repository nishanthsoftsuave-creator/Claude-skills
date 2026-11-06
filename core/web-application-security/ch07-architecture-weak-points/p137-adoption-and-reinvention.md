---
id: WAS-C07-004
title: Adoption and Reinvention
source_pages: "137-138"
chapter: 7
concepts: [reinventing-the-wheel, adoption, custom-cryptography, hashing-algorithms, sha-3, build-versus-adopt, organizational-risk]
related: [WAS-C07-003, WAS-C18-004]
time_sensitive: true
---
# Adoption and Reinvention
(Source: PDF pp. 137-138)

## What the section covers
The security cost of developers rebuilding technology that already exists, and a rule of thumb for what to reuse and what to build.

## Meaning
- A final risk factor is developers' wish to reinvent existing technology. It usually begins as an organisational problem that later shows up in the application architecture (PDF p. 137).
- Reinvention is common because it lets teams avoid complicated licences, add extra functionality, and create publicity by marketing the new tool. Building also tends to be more fun than reusing an open source or paid tool (PDF p. 137).

## Alternatives and trade-offs
- Reinventing is not always wrong. If the best tool carries a licence with a large commission that makes margins negative, or forbids changes so that essential functionality would be lost, building can bring more benefit than harm (PDF p. 137).
- From a security view, reinvention is risky, from a moderate to an extreme degree depending on what is rebuilt (PDF p. 137).

## How it works: the cryptography example
- Security engineers advise never to write your own cryptography. Skilled engineers may devise their own hashing to avoid public algorithms, but at what cost (PDF p. 138)?
- SHA-3 is open source and was developed over nearly 20 years, tested by the US standards body NIST and by large security firms. Hashes face attacks such as combinator and Markov attacks, so an in-house algorithm must stand up to the same scrutiny (PDF p. 138).
- Matching that testing would cost an organisation tens of millions of dollars, whereas adopting an implementation of SHA-3 from a source such as OpenJDK costs nothing and brings the same benefits. A lone developer will probably not meet those standards, leaving critical data an easy target (PDF p. 138).

## When and how to apply
- A securely built application reinvents only purely functional features, such as a schema for comments or a notification system (PDF p. 138).
- Features needing deep expertise in mathematics, operating systems or hardware, such as databases, process isolation and most memory management, should be left alone (PDF p. 138).
- No one is expert at everything. Good developers work in their field and ask for help outside it; bad ones often reinvent mission-critical parts. Applications full of custom databases, cryptography and hardware-level tuning are often the easiest to break into, with rare exceptions (PDF p. 138).

## Relations
Follows WAS-C07-003; password hashing is treated in WAS-C18-004.

## Time-sensitive statements
The SHA-3 development period ("nearly 20 years") and the cost estimate are dated.
