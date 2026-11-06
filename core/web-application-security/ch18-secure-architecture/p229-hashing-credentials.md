---
id: WAS-C18-004
title: Hashing Credentials
source_pages: "229-231"
chapter: 18
concepts: [password-hashing, bcrypt, pbkdf2, rainbow-tables, key-stretching, hash-collisions, slow-hashing, md5]
related: [WAS-C18-003, WAS-C18-005]
time_sensitive: true
---
# Hashing Credentials
(Source: PDF pp. 229-231)

## What the section covers
Why passwords must be stored as hashes, how hashing differs from encryption, three breach scenarios, and the two hashing algorithms the book recommends, BCrypt and PBKDF2.

## Meaning and reasons to hash
- Sensitive credentials should never be stored in plain text. The password is hashed the first time it is seen and only the hash is stored (PDF p. 229).
- Hashing algorithms are not reversible, unlike most encryption. That means even the organization's own staff cannot steal user passwords that those users might reuse elsewhere, and a rogue employee is not a liability on that front.
- Modern hashing is very efficient: strings of many megabytes reduce to between 128 and 264 bits, as the book states. At login the password is hashed again and compared with the stored hash, so even a huge password is checked quickly.
- Modern algorithms have almost no collisions in practical use: either zero, or odds the book writes as statistically approaching 0, with 1 in 1,000,000,000 or more given as the figure (PDF p. 230). The chance that two passwords share a hash is extraordinarily low, so a hacker "guessing" a password only succeeds by guessing a user's exact password.
- If a database is breached, properly hashed passwords protect the users, since the hacker holds only hashes and is unlikely to reverse even one.

## Three breach cases for MegaMerch
- Plain text: every password is compromised.
- Hashed with MD5: a hacker can crack some using rainbow tables, which are precomputed tables from hash to password. Weaker algorithms are open to them.
- Hashed with BCrypt: it is unlikely that any password is cracked.

## Choosing an algorithm: it should be slow
- Every password should be hashed, and the algorithm judged on its mathematical integrity and on how it scales with modern hardware. Algorithms should be slow on modern hardware, which cuts the number of guesses per second (PDF p. 230).
- Attackers automate the password-to-hash process, and a matching hash means the password is breached, collisions aside. Extremely slow algorithms such as BCrypt can take years or more to crack one password on modern hardware.

## BCrypt (PDF p. 231)
- The name combines the Blowfish Cipher, a general-purpose open source symmetric-key block cipher developed by Bruce Schneier in 1993, with Crypt, the default hashing function shipped with Unix operating systems.
- Crypt was written for early Unix hardware, which hashed fewer than 10 passwords per second. Modern hardware hashes tens of thousands per second, so Crypt-hashed passwords are easy for a current hacker to break.
- BCrypt iterates on both and, per the book, becomes slower on faster hardware, so it scales into the future and makes brute forcing a complex password nearly impossible today.
SUPPLEMENTARY: in the published bcrypt design (Provos and Mazieres, 1999, "A Future-Adaptable Password Scheme") the slowdown is set by a configurable cost parameter that has to be raised over time as hardware improves; the book describes the property as if it happened on its own.

## PBKDF2 (PDF p. 231)
- An alternative when BCrypt-like algorithms are not available, based on key stretching: the first hash is fast but each further attempt gets slower, making brute force computationally expensive.
- It was not designed for password hashing but suffices when needed.
- It takes a setting for the minimum number of iterations. Set it to the highest number your hardware can handle, since you cannot know what hardware an attacker has: that removes extra iterations on faster hardware and any attempts on slower hardware, the book says.

## Decision for the example
MegaMerch hashes passwords with BCrypt and compares only hashes (PDF p. 231).

## Time-sensitive statements
Hash speeds, the status of MD5 and the advice on algorithms reflect the time of writing.

## Relations
Follows password rules (WAS-C18-003); further account protection is 2FA (WAS-C18-005).
