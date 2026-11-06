---
id: WAS-C01-003
title: Automated Enigma Code Cracking, Circa 1940 - Lead-in
source_pages: "37-38"
chapter: 1
concepts: [alan-turing, bletchley-park, gc-cs, dilly-knox, scalable-cryptanalysis, general-purpose-solution, turing-test]
related: [WAS-C01-002, WAS-C01-004]
time_sensitive: false
---
# Automated Enigma Code Cracking, Circa 1940 - Lead-in
(Source: PDF pp. 37-38)

## What the section covers
The introduction to Alan Turing's cryptography work at Bletchley Park, before the section on his Bombe machine. It explains why manual and highly specialised Enigma attacks stopped being enough.

## Who Turing was
- Alan Turing was an English mathematician best known for the Turing test, which rates machine-generated conversation by how hard it is to tell it from human conversation. The test is often counted among the foundational ideas of artificial intelligence (PDF p. 37).
- Before and during the Second World War, though, his research focused mainly on cryptography and automation, not AI. From September 1938 he worked part time at the Government Code and Cypher School (GC&CS) (PDF p. 37).

## The setting
- GC&CS was a research and intelligence agency funded by the British Army, based at Bletchley Park in England. Turing studied Enigma cryptography there with his then mentor Dilly Knox, an experienced cryptographer (PDF p. 38).
- They wanted to break the now much stronger German Enigma encryption. Through a partnership with the Polish Cipher Bureau they could use all of the research Rejewski's team had produced nearly ten years earlier, so they already understood the rotors, the wiring, and how device configuration relates to the encrypted output. Figure 1-2 shows a pair of Enigma rotors used to set the machine's transmission configuration, which the book likens to changing the primary key of a digital cipher (PDF p. 38).

## The scaling problem
Rejewski's pattern-based guesses did not scale once the number of rotors had grown as much as tenfold. By the time every combination could be tried, a new configuration would already have been issued. Turing and Knox therefore looked for a different kind of solution: one that scaled, could break new kinds of encryption, and was general-purpose rather than specialised (PDF p. 38).

## Relations
This sets up the machine described in WAS-C01-004. The earlier Polish work is in WAS-C01-002.
