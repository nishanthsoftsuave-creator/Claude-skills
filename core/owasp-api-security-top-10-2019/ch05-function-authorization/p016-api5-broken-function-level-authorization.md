---
id: A05-001
title: API5:2019 Broken Function Level Authorization
source_pages: "16-17"
chapter: api5
concepts: [broken-function-level-authorization, bfla, administrative-endpoints, role-based-access-control, deny-by-default, http-method-tampering, forced-browsing, privilege-escalation]
related: [A00-006, A00-007, A01-001, A09-001]
time_sensitive: false
---
# API5:2019 Broken Function Level Authorization
(Source: PDF pp. 16-17)

## What the section covers
Authorization at the level of operations rather than objects: ordinary or anonymous users reaching functions reserved for administrators or for another group. The chapter explains why APIs make these flaws easy to find, gives three diagnostic questions, two scenarios and a prevention approach built around a single authorization module.

## Risk scores
Exploitability 3, prevalence 2, detectability 1, technical impact 2; business impact is business-specific (PDF p. 16). (Scales: A00-006.)

## Why it matters
- Threat agents and attack vectors: the attacker sends legitimate-looking API calls to an endpoint they should not be able to use. Such endpoints may be reachable by anonymous users or by regular, non-privileged users. APIs make the flaw easier to discover than classic web applications because they are more structured and the way to reach a function is more predictable; the document's examples are switching the HTTP method from GET to PUT, or replacing "users" in a URL with "admins" (PDF p. 16).
- Security weakness: function or resource authorization is usually managed in configuration and sometimes in code. Getting it right is confusing because modern applications have many roles and groups and complex user hierarchies, such as sub-users or users with more than one role (PDF p. 16).
- Impacts: access to functionality the caller is not entitled to; administrative functions are the prime target (PDF p. 16).

## Is the API vulnerable?
The document says the best way to find these flaws is a deep analysis of the authorization mechanism with the user hierarchy and the application's roles and groups in mind, asking (PDF p. 16):
- Can a regular user reach administrative endpoints?
- Can a user perform sensitive actions (create, modify, erase) they should not have, simply by changing the HTTP method, for example GET to DELETE?
- Can a user from group X reach a function meant only for group Y by guessing the endpoint URL and parameters, for example an export-all users endpoint?

Two warnings follow: do not judge whether an endpoint is regular or administrative from its URL path, and expect administrative endpoints to appear under ordinary paths such as an `api/users` prefix rather than only under something like `api/admins` (PDF p. 16).

## How it works: the attack scenarios
1. **Inviting yourself as an admin.** In an invitation-only application, the mobile app fetches an invite with a GET request to an invites endpoint keyed by the invite's GUID; the response includes the invited user's role and email. The attacker replays the request with the method and path changed to a POST on the "new invite" endpoint, which is meant for the admin console only and has no function-level check. The attacker posts an invite for an attacker-controlled email address with the role set to admin and thereby creates an admin account (PDF p. 16).
2. **Guessing the all-users admin endpoint.** An API has an administrators-only endpoint under an admin path that returns every user's details and has no function-level check. An attacker who has learned the API's structure guesses the path and reads the sensitive details of all users (PDF p. 17).

## How to prevent
The application should have one consistent, easy-to-analyse authorization module that every business function calls; often that protection is provided by components outside the application code (PDF p. 17). Specifically (PDF p. 17):
- The enforcement mechanism should deny all access by default and require explicit grants to specific roles for every function.
- Review the API's endpoints for function-level authorization flaws with the business logic and the group hierarchy in mind.
- Make every administrative controller inherit from an abstract administrative controller that performs authorization checks based on the user's group or role.
- Make administrative functions that live inside regular controllers perform the same group- and role-based checks.

## When and how to apply
INTERPRETATION: build a matrix of endpoints against roles from the code or the API definition, then test each cell with a low-privilege and an anonymous session, including method variations on the same path; a 2xx response outside the intended cells is a finding. Where authorization is enforced by an external gateway, confirm the gateway's rules cover every route, not just those under an admin prefix.

## References the section lists
OWASP: the article on Forced Browsing, OWASP Top 10 2013 A7 Missing Function Level Access Control, and the Development Guide chapter on Authorization. External: CWE-285 Improper Authorization (PDF p. 17).

## Relations
A01-001 is the object-level counterpart; A06-001 covers client-supplied properties such as a role being written when binding is unfiltered, a related but different flaw from the missing function check in scenario 1; A09-001 covers forgotten hosts where such checks may be absent entirely; A00-007 holds the one-line summary.
