---
id: WAS-C18-001
title: Analyzing Feature Requirements
source_pages: "225-226"
chapter: 18
concepts: [secure-architecture, feature-requirements, risk-analysis, megamerch, nist-cost-estimate, security-and-rd-collaboration, authentication-authorization]
related: [WAS-C17-002, WAS-C18-002, WAS-C18-006, WAS-C18-007]
time_sensitive: false
---
# Analyzing Feature Requirements
(Source: PDF pp. 225-226, with the Authentication and Authorization lead-in on PDF p. 227)

## What the section covers
The opening of the architecture chapter and its first technique: collect the business requirements of a feature, and derive from them the risk areas the design must address. It uses a worked example, an ecommerce store called MegaMerch.

## Chapter opening: why architecture comes first
- Securing any web application starts in the architecture phase (PDF p. 225).
- A cross-functional team of software engineers and product managers usually looks for a technical model that serves a specific business goal efficiently. The architect designs modules at a high level and decides how they communicate, where data is stored, which third-party dependencies to rely on, and which programming paradigm should dominate.
- Like building architecture, software architecture is delicate and risky, since redoing it after the application exists is expensive. Security architecture has the same profile: planning in this phase prevents many vulnerabilities, while too little planning forces re-architecture at large cost.
- The author cites NIST's claim, based on a study of popular web applications, that removing a security vulnerability in the design phase costs 30 to 60 times less than removing it in production.

## Technique: collect and evaluate requirements
- The first step is to collect everything the product or feature must do. Business requirements can be evaluated for risk before their integration is even considered (PDF p. 225).
- A tip printed on PDF p. 226 says organizations with separate security and R&D teams should build communication paths into development. Features cannot be analyzed in a silo, so analysis should include stakeholders from engineering and from product development.

## Worked example: MegaMerch
MegaBank, having cleaned up several security holes, launches a merchandising brand, MegaMerch, selling cotton T-shirts, cotton and elastic sweatpants, and swimwear with the logo (PDF p. 226). Its ecommerce application must let users:
- create accounts and sign in;
- hold accounts that contain full name, address and date of birth;
- see a front page showing items;
- search for items;
- save credit cards and bank accounts for later use.

A high-level reading of these requirements gives five facts: credentials are stored, personal identifier information is stored, users have elevated privileges compared with guests, users can search items, and financial data is stored. From them the book derives three risk areas:
- Authentication and authorization: how sessions, logins and cookies are handled.
- Personal data: whether it is handled differently from other data and whether laws affect it.
- Search engine: how it is implemented and whether it reads from the primary database as the single source of truth or from a separate cached database.

## Lead-in to authentication and authorization (PDF p. 227)
Each risk raises implementation questions, and those questions are the surface where a security engineer can steer the design. Because credentials are stored and guests and registered users are treated differently, the application needs both an authentication system and an authorization system. Credentials travel over the network and sit in a database. So three questions follow: how data in transit is handled, how credentials are stored, and how different authorization levels of users are handled.

## When and how to apply
INTERPRETATION: write requirements as a list, mark each line with the kind of data or privilege it introduces, and treat each mark as a prompt for a design question.

## Relations
Builds on the architecture step in WAS-C17-002. The risks named here are taken up in WAS-C18-002 (transit), WAS-C18-006 (personal and financial data) and WAS-C18-007 (search).
