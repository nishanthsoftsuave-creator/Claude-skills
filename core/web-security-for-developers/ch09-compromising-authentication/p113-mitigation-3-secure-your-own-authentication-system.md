---
id: WS-C09-005
title: Mitigation 3 - Secure Your Own Authentication System
source_pages: "113-119"
chapter: 9
concepts: [own-authentication, email-validation, validation-token, password-reset, password-complexity, password-hashing, bcrypt, salting, rainbow-tables, multifactor-authentication, logout, user-enumeration, captcha]
related: [WS-C09-002, WS-C09-003, WS-C09-004, WS-C09-006, WS-C10-002, WS-C02-003]
time_sensitive: true
---
# Mitigation 3 - Secure Your Own Authentication System
(Source: PDF pp. 113-119, tail PDF p. 120. This row begins at the "Mitigation 3" heading part-way down PDF p. 113; the text above it is the end of WS-C09-004. The tail page content above the "Summary" heading, the end of the CAPTCHA discussion, belongs here.)

## What the section covers
The design decisions and defences needed when you build sign-up, login, logout and password management yourself: identifiers, email validation, password resets, password rules, hashed and salted storage, multifactor authentication, logout, and prevention of user enumeration.

## Why it matters
Third-party login is usually more secure, but relying on it alone can limit your audience, since not everyone has a social media account or Gmail address. Everyone else needs to sign up with a chosen username and password (PDF p. 113). That means building pages for sign-up, login and logout, code that stores and updates credentials and checks them on re-entry, and most likely a password-change feature. The book stresses that this is a lot of functionality and that some design decisions must be right before coding starts (PDF p. 113).

## Usernames, email addresses, or both
- Users pick a username and password at sign-up. Most sites also require a valid email address so a password-reset message can be sent (PDF p. 113).
- On many sites the email address doubles as the username. Since each address must be unique to one account, a separate username would be redundant (PDF p. 113).
- Exception: sites where users are visible to others (public profiles, comment sections) need a separate display name. Using the email address as a display name is bad practice because it invites harassment and spam (PDF p. 113).

## Validating email addresses
- If the site sends email, for instance for resets, each address must be confirmed to belong to a working mailbox. Emails sent in response to user actions are called transactional emails. Sending them to unverified addresses can quickly get you blacklisted by your email provider, which is wary of spammers (PDF p. 113).
- Step one is a surface check: the address should contain only allowed characters (letters, digits and a set of special characters) (PDF p. 113). It must have an at sign followed by a valid internet domain (PDF p. 114).
- The domain should normally correspond to a website, though not always. At a minimum, DNS (discussed in Chapter 2, see WS-C02-003) must hold a mail exchange (MX) record for the domain, saying where to route mail. Listing 9-3 shows a short Python function that uses a DNS resolver library to look up the MX record and returns true if one exists (PDF p. 114).
- Only sending a message and seeing that it arrives is fully reliable. The site emails a verification link carrying a validation token: a large random string stored in the database against that address. When the user clicks, the site compares the token with the one it issued, proving the user can read that mailbox (PDF p. 114).
- Some sites force validation before sign-up completes; others allow limited features in the meantime to reduce friction. Never assume a user controls an address before validation, and until then send no other transactional email and do not add them to mailing lists (PDF p. 114).

## Banning disposable email accounts
- Some people avoid giving a real address and use temporary mailbox services such as 10 Minute Mail or Mailinator (Figure 9-2 shows one such site). These mailboxes receive a few messages and then vanish. The usual motive is fear of being added to mailing lists, which the book calls a reasonable worry (PDF p. 114).
- You may still need to ban them, for example if people create throwaway accounts to harass others. Use well-maintained blacklists of disposable-email domains to detect and reject them at sign-up (PDF p. 114).

## Securing password resets
- A validated address lets you handle forgotten passwords: email a reset link containing a fresh validation token; when the user clicks, validate the token and let them choose a new password (PDF p. 115).
- Reset links should be short-lived and should expire once used. The rule of thumb is to expire reset tokens after 30 minutes. Reason: if an attacker breaks into a victim's mailbox, they must not be able to search it for old reset links and use them to take over the account on your site (PDF p. 115).

## Requiring complex passwords
- Complex passwords are harder to guess, so require standards for the user's own protection: mix numbers, symbols and letters, upper and lower case, and favour length. Enforce at least eight characters, and longer is better. The book cites studies showing length matters more than unusual characters (PDF p. 115).
- Too-strict rules backfire: users forget complex passwords and reuse one from another site. Some secure sites forbid reuse of earlier passwords, but most users just append a number to a familiar password, which is hardly harder to guess (PDF p. 116).
- The book's stance is that each user is ultimately responsible for their own security, so nudge rather than force. A JavaScript library such as the password-strength-calculator can rate a password while it is typed and flag commonly used ones, on sign-up and reset screens (PDF p. 116).

## Securely storing passwords
- Never store a password as plain cleartext. If a database holding cleartext passwords is breached, every account falls, along with the same users' accounts on other sites that share the password (PDF p. 116).
- Hashing: pass the password through a cryptographic hash function that yields a fixed-length bit string and cannot feasibly be reversed, then store that hash next to the username. Hashing is one-way; the only practical way to find an input for a given hash is to try inputs one by one. At login, hash the re-entered password and compare it with the stored hash (PDF p. 116).
- Many algorithms exist, with different strengths. A good one is fast but not too fast; otherwise growing computing speed makes brute-force enumeration practical. The book recommends bcrypt, which allows extra iterations over the years so hashing stays slow as hardware gets cheaper (PDF p. 116).
- Listing 9-4 (Python): hash with a call that takes the password and a freshly generated salt, with a "rounds" parameter set to 14, then use the library's check function to compare a candidate against the stored hash and print a match or non-match message. Raising the rounds value strengthens the hashes (PDF p. 117).

```python
hashed = bcrypt.hashpw(password, bcrypt.gensalt(rounds=14))
bcrypt.checkpw(password, hashed)  # True when it matches
```

- Result: nobody with database access, including you, can read the passwords directly, yet your site can still verify them. Even if the database is stolen, hashed passwords are of little use to the attacker (PDF p. 117).

## Salting hashes
- Users are unimaginative, so attackers crack leaked hash lists with rainbow tables: precomputed hashes of common passwords under a known algorithm. Matching against them cracks many or most entries (PDF p. 117).
- Defence: salt the hashes by adding randomness so the password alone does not determine the hash. A salt can be kept in configuration, but better is a separate salt per user stored beside their hash. The attacker would then need to rebuild the whole rainbow table for every salt, which is too slow to be practical (PDF p. 117).

## Requiring multifactor authentication
- Password systems stay open to brute-force guessing however well passwords are stored, so consider multifactor authentication (MFA): the returning user proves identity with at least two of three categories, something they know, something they have, something they are (PDF p. 117).
- Examples: a bank ATM (PIN plus card) and smartphone fingerprint scanning (biometrics, the thing they are) (PDF pp. 117-118).
- On the web it usually means username and password (known) plus an authenticator app on the user's phone (possessed). The user syncs the app at sign-up, typically by photographing a QR code, and afterwards supplies the six-digit random number it generates at each login (Figure 9-3 shows the code) (PDF p. 118).
- The attacker then needs both the credentials and the phone, an unlikely pairing. MFA is increasingly standard because smartphones are everywhere. Sites that process financial transactions should definitely implement it, and many code libraries make that easy (PDF p. 118).

## Implementing and securing logout
- Provide a logout function. It may seem old-fashioned when social media users stay signed in forever, but it matters for people on shared devices such as family laptops or reused company computers (PDF p. 118).
- Logging out should clear the session cookie in the browser and invalidate the session identifier if it is stored server-side. This defeats an attacker who captures a session cookie later and tries to resume the session (PDF pp. 118-119).
- Clearing the cookie is done by sending a response with a Set-Cookie header whose value for the session parameter is blank (PDF p. 119).

## Preventing user enumeration
- Enumeration means testing usernames from a list to see which exist on your site. Attackers often take usernames from earlier breaches, find which ones match accounts, then guess passwords only for those (PDF p. 119).
- Login pages: if the error for a wrong password differs from the error for an unknown user, responses reveal which accounts exist. Keep one generic message, for example that an incorrect username or password was entered, in both cases (PDF p. 119).
- Timing attacks: hashing a password takes measurable time (usually under a second). If the site hashes only when the username is valid, response times reveal which accounts exist. So compute a password hash during authentication even for invalid usernames (PDF p. 119).
- Password-reset screens must not reveal whether an address is registered either. After a user requests a reset link, show a neutral message, for example telling them to check their inbox (PDF p. 119).

## Implementing CAPTCHA
- A CAPTCHA (Completely Automated Public Turing test to tell Computers and Humans Apart) asks for image-recognition tasks that are easy for people and hard for programs, making hacking scripts against a page impractical (Figure 9-4 shows an example) (PDF p. 119).
- They are imperfect: attackers can defeat them with sophisticated machine learning or by paying humans to solve them. Still, they deter most attempts and are simple to add. Google's reCAPTCHA widget can be installed with a few lines of code (PDF pp. 119-120).

## When and how to apply
INTERPRETATION: Treat the sections above as a checklist for any in-house login system, and combine the generic login and reset messages, the hash-even-for-unknown-usernames rule and CAPTCHA, since each addresses a different enumeration route the book describes.

## Time-sensitive statements
- Named services: 10 Minute Mail, Mailinator, Google reCAPTCHA, bcrypt, and the password-strength-calculator library (PDF pp. 114, 116, 120).
- The 30-minute expiry and eight-character minimum are the book's rules of thumb as written; such thresholds tend to change over time (PDF p. 115).
- The Python listings (3 and 4) depend on the dns resolver and bcrypt library APIs as the book used them (PDF pp. 114, 117).

## Relations
Summarised in WS-C09-006. The session cookie that logout must clear is explained in WS-C10-002.
