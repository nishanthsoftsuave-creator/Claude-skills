---
id: WAS-C16-001
title: Part II Summary
source_pages: "215-216"
chapter: 16
concepts: [offense-summary, vulnerability-archetypes, business-logic, recon-and-offense, mitigations-not-fixes, authorized-testing, ethics]
related: [WAS-C09-001, WAS-C09-002, WAS-C17-001]
time_sensitive: false
---
# Part II Summary
(Source: PDF pp. 215-216)

## What the section covers
The closing chapter of the offense part: how common archetypes relate to application-specific logic bugs, how Part II builds on recon, a preview of defense, and the author's warning about authorized use of the techniques.

## Key points
- Web applications host many kinds of vulnerabilities. Some are easy to classify, like those tested in this part. Others are niche, unique to one application that has an uncommon security model or features with unusual architecture (PDF p. 215).
- Thorough testing needs knowledge of common archetypes, critical thinking and domain knowledge so that deep logic vulnerabilities outside the common archetypes can be found. The foundations in Parts I and II are meant to be enough to get started on any web application penetration-testing project (PDF p. 215).
- Testers should pay attention to the business model of any application they test. Every application is at risk from XSS, CSRF or XXE, but advanced and specific vulnerabilities are found only by understanding the underlying business model and logic (PDF p. 215).
- If the vulnerabilities in Part II seem hard to apply in practice, consider why. The application may be thoroughly hardened, but more likely the reader needs to improve or apply recon skills to find where the attacks can be deployed. Part II builds directly on Part I (PDF p. 215).

## Bridge to defense
- Readers should keep both recon and offensive techniques in mind through the defense part, and while working through defense examples think about how a hacker would find and exploit an application with and without the defenses (PDF p. 216).
- Defenses are often broken, which is why they are called mitigations rather than fixes. Part I and Part II knowledge may help find ways to bypass or soften specific defenses. The defenses in Part III are mostly industry best practice, but many are not bulletproof, and several should often be combined (PDF p. 216).

## Ethics and limits
- The techniques in Part II are dangerous. They are real attacks used regularly by real attackers. Readers may test them on their own web applications but should not test them on applications owned by others without explicit written permission from the owner (PDF p. 216).
- The techniques can be used for good or evil, so their application and use should be thought through carefully and not deployed on a whim (PDF p. 216).
- Several techniques can compromise servers or client machines even with the owner's permission. Consider the impact of each attack and make sure the owner understands the risks of live testing before starting (PDF p. 216).

## Relations
Builds on the hacker mindset and applied recon (WAS-C09-001, WAS-C09-002) and leads into the defense part (WAS-C17-001).
