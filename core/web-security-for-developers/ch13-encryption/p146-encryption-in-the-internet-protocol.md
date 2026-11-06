---
id: WS-C13-002
title: Encryption in the Internet Protocol
source_pages: "146-149"
chapter: 13
concepts: [tls, https, symmetric-encryption, asymmetric-encryption, public-key-cryptography, hash-function, message-authentication-code, tls-handshake, cipher-suite, session-key]
related: [WS-C13-001, WS-C13-003, WS-C13-005, WS-C02-005, WS-C09-005]
time_sensitive: true
---
# Encryption in the Internet Protocol
(Source: PDF pp. 146-149, tail PDF p. 150. The section begins at its heading part-way down PDF p. 146. The tail is the text at the top of PDF p. 150 above the "Enabling HTTPS" heading, which begins WS-C13-003.)

## What the section covers
How TLS secures HTTP traffic: the problem with plain TCP, the families of cryptographic algorithm (symmetric, asymmetric, hash functions, message authentication codes), cipher suites, and the steps of the TLS handshake (PDF pp. 146-150).

## Meaning
- Messages on the internet are split into data packets and routed to their destination using the Transmission Control Protocol (TCP); the recipient reassembles them (PDF p. 146). TCP does not say how the data should be interpreted (a higher-level protocol such as HTTP does that) and does not disguise packet contents (PDF p. 146).
- Unsecured TCP conversations are open to man-in-the-middle attacks, where a malicious third party intercepts and reads packets in transit (PDF p. 146).
- Transport Layer Security (TLS) secures HTTP conversations between browser and server. It gives privacy (packets cannot be deciphered by a third party) and data integrity (tampering in transit is detectable). HTTP carried over TLS is HTTP Secure, HTTPS (PDF p. 146).
- When a browser connects to an HTTPS site, the two sides negotiate the encryption algorithms in the TLS handshake, the exchange of packets that starts a TLS conversation (PDF p. 146).
- An encryption algorithm scrambles input data using an encryption key, a secret shared between two parties who want secure communication. The output is unreadable without the matching decryption key. Data and keys are normally binary, though keys can be written as text for readability (PDF p. 146).
- Algorithms fall into categories: symmetric and asymmetric encryption (ciphering data), hash functions (fingerprinting data and building other algorithms), and message authentication codes (ensuring integrity) (PDF p. 146).

## How it works: the algorithm families
### Symmetric encryption
- Uses the same key to encrypt and decrypt. Usually implemented as block ciphers that split input into fixed-size blocks, padding an undersized last block, which suits streams such as TCP packets (PDF p. 147).
- Designed for speed. The major flaw: the decryption key must be given to the receiver before decryption, and if it travels over the internet an attacker can steal it and decrypt all later messages (PDF p. 147).

### Asymmetric encryption
- Uses different keys to encrypt and decrypt, developed in response to the key-theft threat (PDF p. 147).
- A server can publish its encryption key openly and keep its decryption key secret. Any client can encrypt messages with the published key, knowing nobody (not even the sender) can decrypt them without the secret key. This is public-key cryptography: the public key is the encryption key, the private key is the decryption key (PDF p. 147).
- Asymmetric algorithms are far more complex and slower than symmetric ones, so Internet Protocol encryption combines both (PDF p. 147).

### Hash functions
- A cryptographic hash function can be seen as encryption whose output cannot be decrypted. Its output (the hashed value) always has a fixed size regardless of input size, and the chance that different inputs give the same output is astronomically small (PDF p. 147).
- Use: a "fingerprint" for data. To check that two inputs are equal without storing the raw input, compare their hashes (PDF p. 147).
- Password storage example (from Chapter 9): the server stores only the hash of the password and discards the password itself. On the next login it hashes the entered password and compares with the stored hash; a mismatch means a wrong password and the credentials are rejected. Storing plaintext passwords is hazardous because a database breach exposes every user's password (PDF pp. 147-148).

### Message authentication codes (MACs)
- A MAC algorithm resembles a hash function, usually built on one, mapping input of any length to a fixed-size output (the MAC). Unlike a plain hash, recalculating a MAC needs a secret key, so only key holders can produce or check valid MACs (PDF p. 148).
- MACs guard packets against forgery or tampering. The two computers share a secret key, typically exchanged during the TLS handshake (itself encrypted before sending). The sender attaches a MAC to each packet; the recipient recalculates it. A mismatch indicates the packet was tampered with, corrupted, or not sent by the original computer, so it is rejected (PDF p. 148).

## The TLS handshake
- TLS combines these tools: most packets are encrypted with a symmetric block cipher for speed; the block cipher's key is itself protected by encrypting it with an asymmetric algorithm; and packets are tagged with a MAC to detect tampering (PDF p. 148).
- In the first stage the browser lists the cipher suites it supports (PDF p. 148).

### Cipher suites
- Under TLS a cipher suite is a set of three algorithms: a key-exchange algorithm (asymmetric, used to swap secret keys), a symmetric block cipher for the packet contents, and a MAC algorithm for authenticating the encrypted messages (PDF p. 149).
- Example: a modern browser such as Chrome with TLS 1.3 offers many suites; at the time of writing one is named ECDHE-ECDSA-AES128-GCM-SHA256. The book describes it as using ECDHE-RSA for key exchange, AES-128-GCM as the block cipher and SHA-256 for the MAC. The printed text says "ECDHE-RSA" although the suite name contains ECDSA; the book's wording is recorded as printed and this looks like an inconsistency in the book (PDF p. 149).
- Name decoding given by the book: ECDHE is Elliptic Curve Diffie-Hellman Exchange, a modern way to establish a shared secret over an insecure channel; RSA is Rivest-Shamir-Adleman, the first practical asymmetric algorithm, from the 1970s; AES is the Advanced Encryption Standard, designed by two Belgian cryptographers and selected by NIST after a three-year review, here with a 128-bit key in Galois/Counter Mode (GCM); SHA-256 is the Secure Hash Algorithm with a 256-bit word size (PDF p. 149).
- Standards keep changing: suites are added, and as weaknesses surface and computing gets cheaper, researchers update TLS. A developer need not understand the algorithms but must keep web server software up to date to support the newest secure ones (PDF p. 149).

### Session initiation
1. The server picks the most secure cipher suite it supports and tells the browser to use those algorithms. It also returns a digital certificate holding the server name, the trusted certificate authority vouching for it, and the server's encryption key for the key-exchange algorithm. Certificates are explained in WS-C13-003 (PDF p. 149).
2. Once the browser verifies the certificate, both sides establish a session key for encrypting the conversation with the chosen block cipher. This TLS session key differs from the HTTP session identifier of earlier chapters; the TLS handshake happens at a lower level, before the HTTP conversation begins (PDF pp. 149-150).
3. The session key is a large random number generated by the browser, encrypted with the public key from the certificate using the key-exchange algorithm, and sent to the server (PDF p. 150).
4. The TLS conversation then begins. Everything after this is encrypted with the block cipher and the shared session key, in both directions, so a snooper sees indecipherable packets; MACs make packets authenticated and tamper-proof (PDF p. 150). (The book's wording at one point says "shared session identifier" for this key.)

## When and how to apply
The practical conclusion is that the complex mathematics is hidden from developers: enabling HTTPS is much simpler (PDF p. 150). INTERPRETATION: the maintenance duty that follows from this section is to keep server software and TLS configuration current so modern suites are available.

## Time-sensitive statements
- Chrome with TLS 1.3 and the suite ECDHE-ECDSA-AES128-GCM-SHA256 reflect the state of the art when the book was written.

## Relations
Follows the chapter intro (WS-C13-001). Chapter 2 gives the earlier introduction to encryption (WS-C02-005) and Chapter 9 the password hashing context (WS-C09-005). Certificates and installation follow in WS-C13-003.
