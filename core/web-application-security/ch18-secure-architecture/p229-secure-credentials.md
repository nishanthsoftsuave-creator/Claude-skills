---
id: WAS-C18-003
title: Secure Credentials
source_pages: "229"
chapter: 18
concepts: [passwords, entropy, dictionary-attack, brute-force, password-rules, common-passwords, megamerch]
related: [WAS-C18-002, WAS-C18-004]
time_sensitive: false
---
# Secure Credentials
(Source: PDF p. 229)

## What the section covers
What makes a password resistant to attack, why length and special characters are the wrong focus, and the password rules MegaMerch should enforce at sign-up.

## Meaning
- Password security rules exist for good reasons, but the book says most developers do not understand what makes a password hacker-safe (PDF p. 229).
- A secure password depends less on length and the number of special characters and more on the patterns that can be found in it. In cryptography this is entropy, the amount of randomness and uncertainty. Passwords should have a lot of it.

## Why it matters: how attackers go after passwords
- Most passwords used on the web are not unique. When a hacker brute forces logins, the easiest route is to take a list of the most common passwords and run a dictionary attack (PDF p. 229).
- An advanced dictionary attack also tries combinations of common passwords, common password structures and common combinations.
- Classical brute force, trying every possible combination, comes after that.
- Protection therefore comes from the absence of observable patterns and from avoiding common words and phrases, not from length alone.

## How to apply
- Explaining entropy to users is difficult, so the application should make it hard to choose a password that holds well-known patterns by imposing requirements (PDF p. 229).
- Reject any password found in a list of the top one thousand passwords, telling the user it is too common.
- Refuse birthdates, first name, last name or any part of the address.
- For MegaMerch, ask for first name, last name and birthdate at sign-up and block them from appearing inside the password.

## Limitations
INTERPRETATION: a fixed list of one thousand common passwords is a floor, not a guarantee; larger lists and checks for patterns built from the account's own data would extend the same idea.

## Relations
Follows transit encryption (WAS-C18-002). Once a password is accepted, it must be stored safely, which is the subject of WAS-C18-004.
