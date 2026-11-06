---
id: WS-C16-002
title: Email Fraud
source_pages: "182-183"
chapter: 16
concepts: [smtp, email-spoofing, spam, phishing, spearphishing, ceo-fraud, spf, dkim, transactional-email, dns-txt-record]
related: [WS-C16-001, WS-C16-003, WS-C02-003, WS-C18-001]
time_sensitive: true
---
# Email Fraud
(Source: PDF pp. 182-183, tail PDF p. 184. The text at the top of PDF p. 182 above the "Email Fraud" heading is the end of WS-C16-001. The text on PDF p. 184 above the "Disguising Malicious Links in Email" heading is the end of this section and is covered here.)

## What the section covers
Why email can be forged, the fraud types that result, and how a site owner defends its domain with SPF and DKIM records and by checking every system that sends mail.

## Meaning
- Email travels over the Simple Mail Transfer Protocol (SMTP). A major oversight of its original design is that it has no authentication mechanism: a sender can put any address in the From header, and until relatively recently receiving agents had no way to verify the claim (PDF p. 182).
- Spam: roughly half of all email is spam, the book says, nearly 15 billion messages a day. It is generally unwanted, often misleading marketing (PDF p. 182).
- Phishing: the sender tries to trick the recipient into giving up sensitive details such as passwords or card numbers. A common version sends what looks like a password-reset message whose link leads to a doppelganger domain, a lookalike of the real one hosting a fake site. The fake site harvests the credentials and then redirects the victim to the real site so nothing seems wrong (PDF p. 182).
- Spearphishing tailors the message to a small audience. Fraudsters research victims so they can name-drop or pose as colleagues. CEO fraud, where a scammer poses as a senior executive and asks an employee for a wire transfer, netted over 26 billion US dollars between 2016 and 2019 according to the FBI, counting only victims who reported it (PDF p. 182).
- Mail providers have sophisticated detection. Gmail, for example, scans each incoming message and sends suspicious ones to the junk folder. Filters weigh keywords in the body and subject, the sending domain, and suspicious outgoing links in the body (PDF p. 182).

## Why it matters
Your organization probably sends mail from a custom domain, so the responsibility is yours both to keep your messages from being flagged as spam and to protect users from malicious mail pretending to come from your domain. The book offers two tools, SPF and DKIM (PDF p. 183).

## How it works
- Sender Policy Framework (SPF): you whitelist, in DNS, the IP addresses allowed to send mail for your domain. SMTP runs over TCP, so the sending IP address cannot be faked the way the From header can; receiving agents can therefore check that mail came from a permitted source (PDF p. 183).
- Listing 16-1 is a DNS record added as a TXT record. It starts with a version tag (v=spf1), lists a permitted IPv4 range and a single permitted IPv4 address, includes the "a" mechanism meaning the domain's own address, and ends with -all, which tells providers to reject mail that matched none of the preceding mechanisms (PDF p. 183).
- DomainKeys Identified Mail (DKIM): outgoing messages get a digital signature proving they were sent from your domain and not altered in transit. It uses public-key cryptography. The domain signs with a private key and recipients validate with a public key published in DNS. Only the sender holds the private key, so only the sender can produce valid signatures. The receiving agent recalculates the signature from the message content and your public key, and rejects the mail if it does not match the attached signature (PDF p. 183).
- Implementation: add a DomainKey as a TXT record (the book writes ".txt record", for SPF too). Listing 16-2 shows one, with a key-type field set to rsa and a long public-key field. The public key sits in DNS, while the matching private key must be shared with the application that generates the email (PDF pp. 183-184). The long key string in the listing is not reproduced in this module.

## When and how to apply: practical steps (PDF p. 184)
- Mail comes from several places. Transactional email, sent in response to user actions on your site, is triggered by server software and often produced by services such as SendGrid or Mailgun. Hand-written mail comes from a webmail service such as Gmail or from server software such as Microsoft Exchange or Postfix. Marketing or newsletter tools such as Mailchimp or TinyLetter are another source.
- Read each provider's or server's documentation to generate and add the DNS entries for SPF and DKIM. You may already use DKIM, since many transactional and marketing services require those DNS entries at sign-up.
- When locking down IP ranges and domains for SPF, account for all the software sending mail from your domain.

## Time-sensitive statements
The spam volume (about 15 billion a day), the FBI CEO-fraud figure for 2016-2019, and the named services (Gmail, SendGrid, Mailgun, Microsoft Exchange, Postfix, Mailchimp, TinyLetter) date from the book's writing.

## Relations
Follows the chapter intro (WS-C16-001); malicious links in such mail are the next topic (WS-C16-003). Chapter 18 repeats the SPF and DKIM advice (WS-C18-001).
