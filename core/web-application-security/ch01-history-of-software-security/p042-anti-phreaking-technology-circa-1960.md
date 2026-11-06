---
id: WAS-C01-006
title: Anti-Phreaking Technology, Circa 1960
source_pages: "42"
chapter: 1
concepts: [dtmf, touch-tones, dual-tone-signalling, anti-phreaking, defence-by-design, digital-switching, itu-standard]
related: [WAS-C01-005, WAS-C01-007]
time_sensitive: false
---
# Anti-Phreaking Technology, Circa 1960
(Source: PDF p. 42, with the rest of the section on PDF p. 43)

## What the section covers
Dual-tone multifrequency (DTMF) signalling, the telephone industry's engineering response to phreakers, and what it shows about designing systems that are harder to abuse.

## What DTMF is
In the 1960s phones gained DTMF signalling, an audio-based signalling language developed by Bell Systems and patented under the better-known trademark "Touch Tones". It is tied to the familiar keypad layout of three columns and four rows. Each key emits two specific frequencies rather than the single frequency of original tone dialing (PDF p. 42).

## The frequency grid (PDF p. 42)
The rows carry the low tones and the columns the high tones, as listed in the book's table:
- Row 1 2 3: 697 Hz
- Row 4 5 6: 770 Hz
- Row 7 8 9: 852 Hz
- Row * 0 #: 941 Hz
- Columns: 1209 Hz, 1336 Hz and 1477 Hz.

## Why it was introduced and how it works
- DTMF was developed largely because phreakers were exploiting tone dialing, which was easy to reverse engineer. Bell believed that two very different tones played at once would be much harder for a malicious actor to abuse (PDF p. 42).
- The tones could not easily be reproduced by a human voice or a whistle, so the technology was much more secure than its predecessor. The book calls it a prime example of a successful security development introduced against the hackers of that era (PDF p. 42).
- Mechanically it is simple: behind each key a switch signals an internal speaker to emit two frequencies, one for the key's row and one for its column, hence "dual-tone" (PDF p. 42).

## Adoption and what it teaches (PDF p. 43)
- The International Telecommunication Union (ITU) adopted DTMF as a standard, and it later also marked commercial break times in cable TV as well as dialling phones.
- The lesson: systems can be engineered to be harder to abuse if proper planning is done. DTMF tones were eventually duplicated too, but the effort needed was far greater, and when switching centres later moved from analog to digital inputs, nearly all phreaking ended.

## Relations
It answers the weakness described in WAS-C01-005. The next era of hacking, personal computers, begins in WAS-C01-007.
