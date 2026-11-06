---
id: C06-008
title: Agent Overview
source_pages: "536-539"
chapter: 6
concepts: [agent-definition, environment, actions, tools, swe-agent, compound-mistakes, agent-planning-loop]
related: [C06-006, C06-007, C06-009]
time_sensitive: false
---
# Agent Overview
(Source: PDF pp. 536-539; the heading "Agent Overview" appears part-way down PDF p. 536, and the discussion of why agents need stronger models continues onto the next page, which is outside this row)

## What the section covers
A definition of an agent, its two defining parts (environment and actions), how tools extend actions, an example coding agent, a worked step-by-step example using the Kitty Vogue tabular RAG system, and the first of the reasons why agents typically need more powerful models.

## Meaning
- The word "agent" is used in many engineering contexts: software agent, intelligent agent, user agent, conversational agent, reinforcement learning agent (PDF p. 536).
- Definition: an agent is anything that can perceive its environment and act upon it. An agent is therefore characterized by the environment it works in and the set of actions it can perform (PDF pp. 536-537).
- The environment is set by the use case: a game (Minecraft, Go, Dota) for a game-playing agent; the internet for a document-scraping agent; the kitchen for a cooking robot; the road system and surrounding areas for a self-driving car (PDF p. 537).
- An agent's actions are augmented by the tools it can use. Many daily generative AI applications are agents with simple tools. ChatGPT is an agent (searches the web, runs Python, generates images). RAG systems are agents, with text retrievers, image retrievers and SQL executors as tools (PDF p. 537).
- Environment and tools depend on each other. The environment determines which tools could be used; in chess, the only possible actions are valid chess moves. Conversely the tool inventory limits the environment: a robot whose only action is swimming is confined to water (PDF p. 537).

## Example: SWE-agent
Figure 6-8 shows SWE-agent (Yang et al., 2024), a coding agent built on GPT-4. Its environment is the computer, with its terminal and file system. Its actions are navigating the repo, searching files, viewing files and editing lines. The figure shows an LM agent connected through an "agent-computer interface" of LM-friendly commands to the computer (terminal and file system), with LM-friendly environment feedback flowing back to the agent (PDF pp. 537-538).

## The role of AI in an agent
An agent is meant to accomplish tasks usually given by users as input. AI acts as the brain: it processes what it receives, including the task and feedback from the environment, plans a sequence of actions to achieve the task, and decides whether the task has been accomplished (PDF p. 538).

## How it works: a worked example
The Kitty Vogue tabular RAG system is a simple agent with three actions: response generation, SQL query generation and SQL query execution (PDF p. 538). For the query "Project the sales revenue for Fruity Fedora over the next three months", the agent might go through these steps (PDF pp. 538-539):
1. Reason about the task; it may decide it needs the last five years of sales numbers first. The reasoning is shown as an intermediate response.
2. Invoke SQL query generation to write the query for those sales numbers.
3. Invoke SQL query execution.
4. Reason about the outputs; it may judge the numbers insufficient for a reliable projection, perhaps because of missing values, and decide it also needs data on past marketing campaigns.
5. Invoke SQL query generation for the marketing campaign queries.
6. Invoke SQL query execution.
7. Reason that the new information is sufficient and generate a projection.
8. Reason that the task has been completed successfully.

## Why agents need more powerful models
Compared with non-agent uses, agents typically need stronger models. The first reason given is compound mistakes: an agent often takes multiple steps, and overall accuracy falls as steps increase. At 95% accuracy per step, accuracy over 10 steps drops to about 60%, and over 100 steps to only about 0.6% (PDF p. 539). The book says there are two reasons; the second begins on the next page and is not part of this row.

## Relations
Builds on the tabular RAG example in C06-006 and the section introduction in C06-007; the tools and planning discussion follows (C06-009).
