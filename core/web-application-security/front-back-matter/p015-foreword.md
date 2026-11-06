---
id: WAS-F-002
title: Foreword
source_pages: "15-16"
chapter: front
concepts: [foreword, dev-security-friction, devops, secops, distributed-applications, attack-surface, secure-design, sdlc, cooperation]
related: [WAS-P-005, WAS-C07-001, WAS-C17-001]
time_sensitive: false
---
# Foreword
(Source: PDF pp. 15-16)

## What the section covers
A short foreword written by the book's sponsor representative. It frames the book around one word, "friction", and argues that the security of modern web applications depends on cooperation between development and security teams. It also previews how the author profiles attacks and then moves to defence.

## Meaning: the friction problem
- The foreword opens with the question of how anyone can be sure a modern web application is secure. Readers are told that everyone agrees the question is hard but nobody agrees on the answer, and that the sponsor's customers keep describing the situation with the word "friction" (PDF p. 15).
- Development and DevOps teams often feel that the security approaches imposed by Security and SecOps teams are needlessly intrusive: they block pipelines and slow down building and deploying applications (PDF p. 15).
- Security and SecOps teams see the same situation from the other side: developers do not grasp that compliance pressure on the business is what makes security urgent, and do not give security enough weight (PDF p. 15).
- Sometimes developers "go rogue" and adopt unapproved tools and processes to sidestep the rules. This can leave applications and the company exposed and breeds resentment on the security side (PDF p. 15).

## Why it matters: the paradigm has changed
- The foreword says the friction is more than a people problem. The security paradigm for applications itself has changed (PDF p. 15).
- Modern applications are harder to secure because of how they are built: they are more open and more distributed, and in practice they are a collection of interactions among different APIs, services, endpoints and devices (PDF p. 15).
- Those interactions cross boundaries inside and outside the organisation, so the attack surface keeps shifting and is hard to defend (PDF p. 15).
- Organisations often try to cover this surface with tools that were not designed for the job or that do not adapt quickly enough to new attack types. The result named in the text is too many tools, approaches and opinions, with limited security effectiveness, a performance cost to the application and, in the worst case, a headline-grabbing attack (PDF p. 15).

## How the book is positioned (PDF p. 16)
- The foreword recommends the book to anyone facing these problems, whether on the development side or the security side (PDF p. 16).
- It says the author starts by profiling the challenges and attacks that modern applications face. Today's attacks are described as slow and methodical: attackers patiently examine the whole surface of a large distributed application for any entry point, and only then design an exploit specifically for that point (PDF p. 16).
- Such attacks are optimised for the application's business model and rely on automated tools that keep probing for different weaknesses (PDF p. 16).
- The author then turns from offence to defence. The defensive strategies are tied to how modern applications are designed and built: good security starts with good design that takes the distributed nature of the application into account (PDF p. 16).
- The foreword stresses that security is not a single event but a process that has to be folded into the entire software development life cycle, and says the book goes into the various security elements to consider as part of it (PDF p. 16).

## When and how to apply
- The lessons are meant for both development teams and security teams. Everyone involved in building modern applications needs to understand how security fits the development life cycle. Stronger alignment, the foreword says, leads to better tool selection and to best practices tailored to the application's own security needs (PDF p. 16).
- The stated goal is strong cooperation between the two teams, and the closing line says that cooperation is the enemy of friction (PDF p. 16).
- The text is signed by the sponsor's director of product management for its security products (PDF p. 16).

## Relations
The distributed-application theme returns in the architecture discussion of Part I (WAS-C07-001) and the defence overview of Part III (WAS-C17-001). The reader profile and book structure are in the preface (WAS-P-005).
