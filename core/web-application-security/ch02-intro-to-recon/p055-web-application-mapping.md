---
id: WAS-C02-002
title: Web Application Mapping
source_pages: "55-56"
chapter: 2
concepts: [application-mapping, recon-notes, json-notes, api-endpoint-map, hierarchical-notes, note-taking, application-features]
related: [WAS-C02-001, WAS-C02-003, WAS-T-001]
time_sensitive: false
---
# Web Application Mapping
(Source: PDF pp. 55-56; the section continues onto the next page)

## What the section covers
The idea of a map of an application built during recon, and the author's preferred way of recording it in a JSON-like hierarchy, with an example.

## Meaning and purpose
- The following chapters teach how to build a map representing the structure, organisation and functionality of a web application. Mapping should generally be the first step before trying to hack the application, and with practice each tester develops their own techniques and note formats (PDF p. 55).
- "Map" is an analogy with topography, the study of land features, shapes and surfaces. Web applications have features, shapes and surfaces too, though different from natural ones. Here a map means the data points collected about the code, network structure and feature set of an application (PDF pp. 55-56).
- The next chapters show how to acquire the data to fill it (PDF p. 56).

## Choosing a format
- For a simple application, or a short test, scratch notes may be fine. For bigger applications, or ones tested often and over long periods, a more robust solution is wise (PDF p. 56).
- Any format is acceptable as long as it is easy to traverse and can hold the relevant information and relationships (PDF p. 56).
- The author prefers JSON-like notes: hierarchical structures are very common in web applications and also make notes easier to sort and search (PDF p. 56).

## The worked example (PDF p. 56)
The sample notes describe the API server of a site called mywebsite.com as a hierarchy:
- An api_endpoints group with sign_up, sign_in and reset_password. Each entry records a URL under an auth path, the HTTP method (POST for all three) and a shape: the fields the payload expects, each with its type, whether it is required, and length limits.
- sign_up requires a username of 6 to 18 characters, a password of 6 to 32 characters and a referralCode of exactly 64 characters.
- sign_in requires the username and password with the same limits; reset_password takes the username, password and a newPassword.
- The listing also begins a features group (comments, uploads, file_sharing) and an integrations group (an "oath" key, as printed, with twitter, facebook and youtube) that continue on the next page.
UNVERIFIED: the printed listing has small typos (for example a colon in place of a comma in some limits and the key "oath" for OAuth); the notes are quoted as printed, and the reading of "oath" as OAuth is an INTERPRETATION.

## Tools for recording
The next page names hierarchical note-taking software such as Notion and mind-mapping tools such as XMind as good places to record and organise findings. The advice is to pick a method that keeps you organised and scales past simple applications.

## Relations
The reasons for mapping are in WAS-C02-001 and the recap is in WAS-C02-003.
