---
id: WAS-C01-004
title: Introducing the Bombe
source_pages: "39"
chapter: 1
concepts: [bombe, known-plaintext-attack, automated-hacking-tool, general-purpose-algorithm, crib, enigma-cracking, polish-bombe]
related: [WAS-C01-003, WAS-C01-002, WAS-C01-005]
time_sensitive: false
---
# Introducing the Bombe
(Source: PDF p. 39, with the end of the section on PDF p. 40)

## What the section covers
What a bombe was, why the first Polish version failed against newer Enigma machines, and how Alan Turing's general design used predictable message content to break any configuration.

## Meaning
A bombe was an electric-powered mechanical device that tried to reverse engineer the rotor positions of an Enigma automatically, by mechanical analysis of messages sent by such machines. Figure 1-3 shows an early Bletchley Park Bombe with many rows of rotors used to run configuration decryption quickly (PDF p. 39).

## Why the first bombes failed
- The first bombes were built by the Polish to automate Rejewski's work. They were designed to find configurations of Enigma machines with very specific hardware and were ineffective against machines with more than three rotors (PDF p. 39).
- Because they could not scale with more complex Enigma machines, the Polish cryptographers went back to manual methods for German wartime messages (PDF p. 39).

## Turing's assumption (PDF p. 39)
Turing thought the earlier machines failed because they were not general-purpose. To decipher any Enigma configuration regardless of rotor count, he started from one assumption: to design an algorithm that decrypts a message, you must first know a word or phrase that occurs inside it and where. German military communication standards were strict. Every day a detailed regional weather report went out over encrypted Enigma radio, so all units knew the conditions without sharing them publicly. The Germans did not realise Turing's team could work out the purpose and position of those reports.

## How it worked and its results (PDF p. 40)
- Knowing the input (the weather data) passing through a correctly configured Enigma made working out the output algorithmically much easier. Turing used this to design a bombe configuration independent of the rotor count of the target machine.
- He asked for a budget and, once approved, built a bombe of 108 drums that could rotate as fast as 120 RPM. It could run through nearly 20,000 possible Enigma configurations in about 20 minutes, so any new configuration could be compromised quickly and Enigma was no longer a secure means of communication.
- The strategy is today called a known plaintext attack (KPA): an algorithm made far more efficient by being given prior input/output data. Modern hackers use similar techniques against encryption on stored or in-use data.
- The author marks the machine as an important point in history, one of the first automated hacking tools ever built.

## Relations
Follows from the lead-in in WAS-C01-003. The next chapter section moves from codebreaking to telephone systems (WAS-C01-005).
