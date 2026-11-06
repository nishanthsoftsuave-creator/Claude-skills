---
id: WAS-C03-012
title: Authentication and Authorization Systems (Section Lead-In)
source_pages: "78"
chapter: 3
concepts: [authentication, authorization, identity, access-control, persisted-data, user-resources, security-controls]
related: [WAS-C03-013, WAS-C03-014, WAS-C03-011]
time_sensitive: false
---
# Authentication and Authorization Systems (Section Lead-In)
(Source: PDF p. 78 from the "Authentication and Authorization Systems" heading)

## What the section covers
The short introduction that defines authentication and authorization and why a client-and-server application needs both. The two kinds of system are detailed in the next two sections.

## Why the systems exist
- In a world where most applications consist of clients (browsers or phones) and servers, and where servers persist data that was originally sent from a client, systems must make sure that later access to the persisted data comes from the correct user (PDF p. 78).

## Meaning
- **Authentication** names a flow that lets a system identify a user. In the book's words, an authentication system confirms that "joe123" really is joe123 and not "susan1988" (PDF p. 78).
- **Authorization** names a flow inside the system for deciding which resources a given user may access. Example: joe123 should be able to reach his own uploaded private photos, and susan1988 should reach hers, but neither should be able to access the other's photos (PDF p. 78).

## Why it matters
Both processes are critical to the functioning of a web application, and both are functions where proper security controls are critical (PDF p. 78).

## When and how to apply
INTERPRETATION: keep the two questions separate when reviewing or testing. Authentication asks "who is this?", authorization asks "what may they touch?", and a flaw in one does not imply a flaw in the other.

## Relations
Authentication techniques are in WAS-C03-013, authorization design in WAS-C03-014. The preceding section, on SPA frameworks, is WAS-C03-011.
