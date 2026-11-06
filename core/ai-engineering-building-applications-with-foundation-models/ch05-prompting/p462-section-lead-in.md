---
id: C05-014
title: Defensive Prompt Engineering (Lead-in)
source_pages: "462-463"
chapter: 5
concepts: [defensive-prompt-engineering, prompt-attacks, prompt-extraction, jailbreaking, prompt-injection, information-extraction, brand-risk]
related: [C05-013, C05-015]
time_sensitive: false
---
# Defensive Prompt Engineering (Lead-in)
(Source: PDF pp. 462-463, plus the first part of PDF p. 464 above the "Proprietary Prompts and Reverse Prompt Engineering" heading. The top of PDF p. 462 is the end of the previous section on prompt catalogs and is not covered here.)

## What the section covers
The introduction to defensive prompt engineering: why a deployed application attracts malicious users, the three main kinds of prompt attack, and a list of risks these attacks create for an application. Detailed treatment of each attack follows in later subsections.

## Why it matters
Once an application is public it can be used by intended users and also by attackers trying to exploit it (PDF p. 462). The book adds that as AI grows more capable these risks become increasingly critical, and that the next subsections show how each risk can arise from each type of prompt attack (PDF p. 464).

## Meaning: the three main prompt attacks (PDF p. 462)
- Prompt extraction: pulling out the application's prompt, including the system prompt, in order to copy or exploit the application.
- Jailbreaking and prompt injection: getting the model to do bad things.
- Information extraction: getting the model to reveal its training data or information supplied in its context.

## Risks posed by prompt attacks
The book notes that some risks are more devastating than others and lists the following (PDF pp. 462-464).
- Remote code or tool execution: when the application has access to powerful tools, attackers may trigger unauthorized code or tool use. Examples: getting the system to run an SQL query that exposes all users' sensitive data, or send unauthorized emails to customers. A second example: an AI-assisted research setup that generates experiment code and runs it locally could be steered into generating malicious code that compromises the machine (PDF p. 463).
- Data leaks: attackers extract private information about the system and its users (PDF p. 463).
- Social harms: models can give attackers knowledge and tutorials on dangerous or criminal activity, such as making weapons, evading taxes, and exfiltrating personal information (PDF p. 463).
- Misinformation: attackers may manipulate the model into emitting misinformation that supports their agenda (PDF p. 463).
- Service interruption and subversion: includes granting access to a user who should not have it, giving high scores to bad submissions, or rejecting a loan application that should have been approved. A malicious instruction telling the model to refuse every question can interrupt service (PDF p. 464).
- Brand risk: politically incorrect or toxic statements beside your logo can trigger a PR crisis. Examples given: Google AI search urging users to eat rocks (2024) and Microsoft's chatbot Tay producing racist comments (2016). People may understand the offense was unintended, yet still blame the company for not caring about safety or for incompetence (PDF p. 464).

## Relations
Follows prompt organization and versioning (C05-013). The next row, C05-015, starts the detailed discussion with proprietary prompts and reverse prompt engineering, which is the first attack (prompt extraction).
