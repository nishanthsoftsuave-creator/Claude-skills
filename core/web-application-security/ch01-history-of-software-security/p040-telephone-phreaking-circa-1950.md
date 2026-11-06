---
id: WAS-C01-005
title: Telephone Phreaking, Circa 1950
source_pages: "40-41"
chapter: 1
concepts: [phone-phreaking, tone-dialing, 2600-hz, blue-box, best-case-design, worst-case-design, john-draper, joe-engressia]
related: [WAS-C01-004, WAS-C01-006]
time_sensitive: false
---
# Telephone Phreaking, Circa 1950
(Source: PDF pp. 40-41, with the end of the section on PDF p. 42)

## What the section covers
How automated tone dialing created the first telecom hacking scene, the famous 2600 Hz trick, and the design lesson the author draws.

## Tone dialing (PDF p. 40)
- After Enigma, the next major event is the telephone. Telephones let ordinary people communicate over long distances at speed, and the networks needed automation to scale (PDF p. 40).
- In the late 1950s telecoms such as AT&T introduced phones that were routed automatically to a destination number from audio signals emitted by the handset. Each key press sent a specific frequency down the line, interpreted by a machine in a switching centre that translated sounds into numbers and routed the call (PDF p. 40).
- This tone dialing was essential for scale. Without a manual operator connecting each call, one operator watching the network for problems could handle hundreds of calls in the time one call used to take (PDF p. 40).

## Phreakers (PDF p. 41)
- Small groups soon saw that any system built on interpreting audio tones was easy to manipulate. Learning to reproduce the same frequencies near the handset could interfere with its intended function. Hobbyists who experimented with this became known as phreakers, an early type of hacker specialising in breaking telephone networks (PDF p. 41).
- The true origin of "phreaking" is unknown; the usual view is a blend of "freaking" and "phone". The author prefers a different derivation, "audio frequency", because the term appeared close in time to AT&T's tone dialing release and, before tone dialing, calls were harder to tamper with since an operator connected each pair of lines (PDF p. 41).
- The most notorious early case was the 2600 Hz tone. AT&T used it internally to signal that a call had ended, effectively an admin command in the dialing system. Sending it made a switch think a call that was still live had ended, allowing costly international calls without any bill being recorded (PDF p. 41).
- Discovery is credited to two events. A young boy, Joe Engressia, could whistle at 2600 Hz and reportedly showed friends he could stop phones dialling, which some call the accidental start of phone phreaking. His friend John Draper later found that toy whistles included in Cap'n Crunch cereal boxes mimicked 2600 Hz, so careful use of the whistle gave free long-distance calls (PDF p. 41).
- The technique spread across the Western world and led to hardware that produced specific frequencies at the press of a button. The first such device was the blue box, which played a nearly perfect 2600 Hz signal. Later phreakers tampered with pay phones, stopped billing cycles from starting without needing 2600 Hz, imitated military signals and even faked caller ID (PDF p. 41).

## The design lesson (PDF pp. 41-42)
- Early telephone architects had considered only normal people and their communication goals. Today this is known as best-case scenario design, a fatal flaw, and the book states the lasting lesson: always consider the worst-case scenario first when designing complex systems (PDF pp. 41-42).
- Knowledge of the weaknesses in tone dialing eventually spread, and budgets were allocated for countermeasures to protect telecom profits and call integrity against phreakers (PDF p. 42).

## Relations
The countermeasure is described in WAS-C01-006. The worst-case lesson recurs in the chapter recap in WAS-C01-009.
