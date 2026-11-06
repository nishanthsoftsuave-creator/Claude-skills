---
id: WAS-C01-002
title: The Enigma Machine, Circa 1930
source_pages: "34-36"
chapter: 1
concepts: [enigma-machine, symmetric-key-encryption, man-in-the-middle, key-management, rotor-cipher, brute-force, marian-rejewski, reverse-engineering]
related: [WAS-C01-001, WAS-C01-003, WAS-C01-004]
time_sensitive: false
---
# The Enigma Machine, Circa 1930
(Source: PDF pp. 34-36, with the end of the section on PDF p. 37)

## What the section covers
How the German Enigma machine worked at a high level, why its key handling was a weakness, how it relates to modern symmetric encryption, and how Polish mathematicians first broke it.

## How the machine worked
- The Enigma used electric-powered mechanical rotors to encrypt and decrypt text messages sent by radio. It came from Germany and became an important technology in the Second World War. Figure 1-1 is a labelled photograph naming its parts: rotors, lampboard, keyboard and plugboard (PDF p. 34).
- It looked like a large mechanical typewriter. Each key press moved the rotors and recorded a seemingly random character, sent to all nearby Enigma machines. The characters were not random: they depended on rotor position and on configuration options that could be changed at any time (PDF p. 35).
- Any machine set to the same configuration as the sender could read ("decrypt") the message, which made the device valuable for sending crucial messages without interception (PDF p. 35).
- The rotary mechanism has no single inventor, but a two-man company, Chiffriermaschinen AG, popularised it by demonstrating it around Germany in the 1920s. The German military adopted it in 1928 to protect top-secret traffic (PDF p. 35).
- Preventing interception of long-distance messages was a radical advance. The book links this to the man-in-the-middle attack on software today and notes that modern software uses similar but much more powerful techniques as defence (PDF p. 35).

## Weaknesses in key management (PDF pp. 35-36)
- Because the only condition for reading a message was an identical configuration, one leaked configuration log, the equivalent of a private key, could make a whole network useless (PDF p. 35).
- Groups therefore changed settings regularly, but reconfiguration was slow. Configuration logs had to be exchanged in person because no secure remote method existed. Two machines and two operators were manageable; a network of 20 machines needed several messengers, each raising the chance that logs were intercepted, leaked or sold (PDF p. 35).
- Adjustments also required a trained person present, as changes meant altering the hardware wiring of the plugboard, and electronics skill was rare in the early 1900s (PDF p. 35).
- As a result updates were typically monthly, and daily on mission-critical lines. A key that was stolen exposed everything transmitted for the rest of that period to a malicious actor, the era's equivalent of a hacker (PDF p. 36).

## Link to modern encryption
- This design is a symmetric key algorithm: a cipher where one key both encrypts and decrypts. The family is still used today to secure data between sender and receiver, with many improvements on the Enigma model (PDF p. 36).
- Software keys can be far more complex, so brute forcing every combination on the fastest modern hardware could easily take more than a million years, and unlike Enigma settings they can change rapidly (PDF p. 36).
- Keys can be regenerated per login, per network request or on a schedule. A leaked key then exposes a single request at best, or a few hours in the worst case for per-session keys (PDF p. 36).
- The author concludes that tracing modern cryptography back leads to the 1930s Enigma, so it was an essential development in what became software security (PDF p. 36).

## The first hackers
- Allied forces felt great pressure to break Enigma encryption. The text says General Eisenhower himself declared it essential for victory (PDF p. 36).
- In September 1932 the Polish mathematician Marian Rejewski was given a stolen Enigma machine, while a French spy, Hans-Thilo Schmidt, supplied valid configurations for September and October 1932. This let him intercept messages and study how Enigma encryption worked mechanically and mathematically (PDF p. 36).
- His method: analyse patterns in the encrypted messages, form theories from the machine's mechanics about which configurations would produce which output, then reconfigure a board with reasonable accuracy and, after several attempts, read traffic. With colleagues Jerzy Rozycki and Henryk Zygalski he reverse engineered the system, and by 1933 the team decrypted Enigma traffic daily (PDF p. 37).
- The author calls Rejewski's team some of the world's earliest hackers, because like today's hackers they intercepted and reverse engineered encryption to reach valuable data produced by someone else (PDF p. 37).
- Germany answered by adding rotors, which raised complexity until Rejewski's team could no longer break traffic in reasonable time. The author presents this as an early picture of the continuing relationship between hackers and those preventing hacking, in which both sides keep improving (PDF p. 37).

## Relations
The next step in that arms race is the automated attack in WAS-C01-003 and WAS-C01-004. The scene-setting for this chapter is WAS-C01-001.
