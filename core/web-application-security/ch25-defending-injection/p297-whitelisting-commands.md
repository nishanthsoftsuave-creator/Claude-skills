---
id: WAS-C25-007
title: Whitelisting Commands
source_pages: "297"
chapter: 25
concepts: [command-whitelisting, allowlist, user-supplied-commands, cli-input, blacklist-risk, injection-prevention]
related: [WAS-C25-006, WAS-C25-008, WAS-C19-005]
time_sensitive: false
---
# Whitelisting Commands
(Source: PDF pp. 297-298)

## What the section covers
Why users should not send arbitrary commands to a server, and how a whitelist narrows what they may run.

## Why it matters
The largest injection risk is functionality where the client sends commands for the server to execute. The book calls this bad architecture to avoid at all costs. When user-chosen commands must run in a context where misuse could cause damage or change state, extra steps are needed (PDF p. 297).

## How it works
Instead of interpreting user commands literally, define a whitelist of commands users may issue, together with an acceptable syntax (order, frequency, parameters). Both should be stored as a whitelist rather than a blacklist (PDF p. 297).

The example is a page with a text input for a command list and a button that sends it. The server handler passes the submitted commands straight to a CLI library's run call (PDF p. 297). As the next page explains, this lets the client run anything the library supports, including commands the developer never meant to expose. Even when every command is allowed, their syntax, order and frequency could combine into unintended behavior (PDF p. 298).

The quick mitigation keeps an array of five commands (print, cut, copy, paste, refresh), checks each submitted command against it, and answers 400 on a miss before running the CLI (PDF p. 298).
INTERPRETATION: in the printed handler the 400 is returned inside a loop callback, which exits only the callback, so the CLI call that follows would still run; a working version must stop the handler itself.

## Alternatives and trade-offs
It may not cure order or frequency problems, but it stops unintended commands. A blacklist is avoided because applications evolve: a new command added later would silently become available. When user input must reach a CLI, choose a whitelist (PDF p. 298).

## Relations
Builds on WAS-C25-006; the closing summary is WAS-C25-008; WAS-C19-005 criticizes blacklists in general.
