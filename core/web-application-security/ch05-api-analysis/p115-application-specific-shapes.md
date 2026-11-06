---
id: WAS-C05-004
title: Endpoint Shapes - Application-Specific Shapes
source_pages: "115"
chapter: 5
concepts: [application-specific-shapes, error-message-leakage, solution-space, trial-and-error, payload-discovery, parameter-rules, generic-errors]
related: [WAS-C05-003, WAS-C05-002, WAS-C05-005]
time_sensitive: false
---
# Endpoint Shapes: Application-Specific Shapes
(Source: PDF p. 115, with the end of the section on the top of PDF p. 116)

## What the section covers
How to work out the payload an endpoint expects when it does not follow a public standard: error-message hints, copying shapes from your own account's traffic, and narrowing the space of possible values.

## Meaning
Application-specific shapes are much harder to determine than shapes based on public specifications. You may need several recon techniques and slowly learn an endpoint through trial and error (PDF p. 115).

## How it works
1. Read error messages. Insecure applications may hint at the shape in their HTTP errors. In the book's example a request to a user-configuration endpoint with a user id and a privacy setting (a public-profile flag) would likely return a 401 not authorized or a 400 internal error. If the status comes with a message saying the auth token was not supplied, you may have stumbled onto a missing parameter (PDF p. 115).
2. Iterate on the message. Sending a correct auth token might yield a different message: the public-profile field accepts only two named values. The book comments "Bingo" because each message exposes more of the expected shape (PDF p. 116).
3. Expect secure apps to withhold this. More secure applications will probably return a generic error, and you will need other techniques (PDF p. 116).
4. Use your own traffic. If you have a privileged account, repeat the request against your own account through the UI before attempting it against another account, to see what the outgoing shape looks like. It can be read in the developer tools Network tab or with a monitoring tool such as Burp (PDF p. 116).
5. Brute force values. If you know a variable's name but not its value, repeat the request with variations until one works. This is slow by hand, so a script speeds it up (PDF p. 116).

## Reducing the search
- The more rules you learn about a variable, the better: for instance, knowing an auth token is always 12 characters is good, and knowing it is hexadecimal is better (PDF p. 116).
- The list of possible combinations for a field is the solutions space, and the aim is to shrink it to the smallest viable search space (PDF p. 116).
- Rather than searching for valid solutions only, you can try to find invalid ones. These may reduce the solutions space and can even uncover bugs in the application code (PDF p. 116).

## When and how to apply
INTERPRETATION: try the cheap, low-noise methods first (error messages and your own account's traffic) before any value brute forcing, which is more detectable.

## Limitations
Hardened applications give generic errors, and brute forcing values is slow and noisy (PDF p. 116).

## Relations
Contrasts with the standard-based case in WAS-C05-003. The chapter wrap-up is WAS-C05-005.
