---
id: WS-C05-004
title: Phase 3 - Pre-Release Testing
source_pages: "66-67"
chapter: 5
concepts: [pre-release-testing, manual-testing, unit-tests, test-coverage, continuous-integration, test-environment, staging, network-segregation, data-scrubbing, integration-testing]
related: [WS-C05-003, WS-C05-005, WS-C05-008]
time_sensitive: false
---
# Phase 3 - Pre-Release Testing
(Source: PDF pp. 66-67, tail PDF p. 68. The row starts part-way down PDF p. 66 at the "Phase 3" heading; the branching and review text above it is WS-C05-003. On the tail page, content above the "Phase 4: The Release Process" heading belongs here, and Phase 4 is WS-C05-005.)

## What the section covers
The third SDLC phase: testing code before release, through manual checks, unit tests, coverage and continuous integration, and a dedicated test environment (PDF pp. 66-68).

## Why it matters
Release only code you have tested thoroughly. A good testing strategy is key to catching defects, above all security vulnerabilities, before users hit them or hackers exploit them (PDF p. 66). Catching defects early in the life cycle saves much time and effort (PDF p. 67).

## How it works
### Manual testing
Anyone changing code should manually test the site's functionality before merging or releasing. This is a baseline level of diligence expected of every team member (PDF p. 66).

### Unit tests
- Complement manual testing with unit tests: small scripts in the codebase that make basic assertions about behaviour by running parts of the code and checking the output. Run them as part of the build, and write them for particularly sensitive or frequently changing areas (PDF p. 67).
- Keep each test simple and focused on one isolated function. Complex tests covering several features at once are brittle and break as the code changes (PDF p. 67).
- Good examples: assert that only authenticated users can view certain areas of the site, or that passwords meet a minimum complexity rule. Good unit tests also serve as documentation of how correct code should behave (PDF p. 67).

### Coverage and continuous integration
- Coverage is the percentage of the codebase executed when all the unit tests run. Aiming for 100 percent is laudable but often impractical, so choose carefully what to test. Full coverage does not guarantee correct code: executing every code path does not mean every scenario is covered (PDF p. 67).
- Writing good tests is a matter of judgment within a wider risk-assessment strategy. Rule of thumb: when you find a bug, first write a unit test asserting the correct behaviour, then fix the bug, which stops it coming back (PDF p. 67).
- Once coverage is adequate, set up a continuous integration server. It connects to the source repository and, whenever code changes, checks out a fresh copy, runs the build and executes the unit tests. If the build fails, for instance because tests fail, the team is alerted. This surfaces defects early so they are dealt with promptly (PDF p. 67).

### Test environments
- After finishing all changes for a release, deploy them to a test environment for final testing. Also called a staging, pre-production or quality assurance environment, it should be a fully working copy of the website on dedicated servers, and is essential for finding defects such as vulnerabilities before release. Large teams often have quality assurance (QA) staff dedicated to testing there. Combining different sets of changes there is sometimes called integration testing (PDF p. 67).
- It should mirror production as closely as possible so tests are meaningful: same server and database technologies, differing only in configuration and the code version. Still use common sense; for example a test environment must not be able to email real users, so impose deliberate limits where needed (PDF pp. 67-68).
- The book compares this to a theatre dress rehearsal before a small test audience, where the cast works out the last kinks in a low-stakes setting that matches opening night in every detail (PDF p. 68).

## Limitations and failure modes
- Test environments bring their own security risks if unmanaged. They must be segregated from production at the network layer, meaning no communication between them is possible, so attackers cannot hop from an unsecured test system into production (PDF p. 68).
- Test environments usually have their own database needing realistic data. A common way to get it is copying production data. If you do, scrub the copy of sensitive information, including names, payment details and passwords. Many high-profile data leaks in recent years came from attackers finding poorly scrubbed data in a test environment (PDF p. 68).

## Relations
Follows code writing and review (WS-C05-003); the next phase, the release process, is WS-C05-005. The chapter summary restates the test environment guidance (WS-C05-008).
