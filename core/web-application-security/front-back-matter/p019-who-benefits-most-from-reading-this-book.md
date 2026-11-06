---
id: WAS-P-004
title: Preface - Who Benefits Most from Reading This Book
source_pages: "19-21"
chapter: preface
concepts: [preface, target-audience, software-engineers, web-application-developers, security-engineers, penetration-testers, bug-bounty-hunters, specialised-tools]
related: [WAS-P-003, WAS-P-005, WAS-P-006]
time_sensitive: false
---
# Preface - Who Benefits Most from Reading This Book
(Source: PDF pp. 19-21, with the closing paragraphs on PDF p. 22)

## What the section covers
The author's description of the target audience, organised by learning goals and professional interests, and the reason the book avoids specialised security tools.

## Intended audience and durability
Readers who fit none of the listed categories can still learn useful or interesting concepts. The book was written to stand the test of time, so its knowledge should stay relevant if the reader later moves into one of the target occupations (PDF p. 19).

## Software engineers and web application developers
- The primary audience is an early- to mid-career software engineer or web application developer interested in either the offensive techniques hackers use or the defensive techniques security engineers use against them. The author notes the two titles are often interchangeable and uses both (PDF p. 20).
- Software engineers: in the author's usage a generalist who can write software for many platforms. Much of the book transfers with little effort to non-web software and to other networked applications, native mobile apps first among them (PDF p. 20). Several exploits abuse server-side integrations between a web application and another component, so any software that interfaces with a web application, such as databases, CRM, accounting or logging tools, can be a threat vector (PDF p. 20).
- Web application developers: specialists in software that runs on the web, subdivided into frontend, backend and full stack. Historically many attacks hit server-side flaws, so the value for backend and full stack developers is obvious (PDF p. 20).
- Frontend developers benefit too, because many of today's attacks start as malicious code running in the browser, and some attackers even abuse the DOM or CSS stylesheets to attack users (PDF p. 20). Frontend developers who never write server code should still know the risks their code can expose and how to reduce them (PDF p. 21).

## General learning goals (PDF p. 21)
- People who want a more security-oriented career, or want to harden the code they or their organisation maintain, are covered.
- The book's structure lets it serve as a security reference without reading any hacking chapter, if defence is the only goal.
- The author recommends reading cover to cover for the best learning, but a reader who only wants a reference on defending against specific hacks can open the book halfway and start there.

## Security engineers, pen testers and bug bounty hunters (PDF pp. 21-22)
- The structure also suits penetration testing, bug bounty hunting and other application-level security work, and such readers may prefer the first half (PDF p. 21).
- The book looks at how exploits work at both the code level and the architecture level instead of running prebuilt open source scripts or paid automation. This gives a second audience: software, IT and network security engineers, penetration testers and bug bounty hunters (PDF p. 21).
- A tip suggests signing up for one of the bug bounty programs mentioned in Part III to develop hacking skills and earn extra money while helping companies (PDF p. 21).
- Existing security professionals who understand how attacks work conceptually can use the book for a deep dive into the systems and code behind a tool or script (PDF p. 21).
- The author observes that penetration testers commonly use many prebuilt exploit scripts, which has led to many paid and open source tools that automate classic attacks and attacks needing no deep knowledge of an application's architecture or the logic in a block of code (PDF pp. 21-22).

## Why no specialised tools are used (PDF p. 22)
- Exploits and countermeasures are shown using the author's own scripts, network requests, standard Unix tooling and the built-in developer tooling of Chrome, Firefox and Edge.
- The author says specialised tools are valuable, even exceptional, and make professional penetration tests easier. The omission is deliberate so attention stays on finding a vulnerability, developing an exploit, prioritising data to compromise and defending against all of that.
- The promised result is that readers can find new types of vulnerability, develop exploits against systems never exploited before, and harden complex systems against persistent attackers.

## Relations
The skills this audience needs are in WAS-P-003, how the parts are organised is in WAS-P-005, and the vocabulary used for the occupations named here is in WAS-P-006.
