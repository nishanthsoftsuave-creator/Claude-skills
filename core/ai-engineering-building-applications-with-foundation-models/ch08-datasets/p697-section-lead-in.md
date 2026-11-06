---
id: C08-002
title: Data Curation (Section Lead-in)
source_pages: "697-703"
chapter: 8
concepts: [data-curation, finetuning-data-formats, chain-of-thought-data, tool-use-data, single-turn-vs-multi-turn, unlearning-bad-behavior, data-quality-coverage-quantity]
related: [C08-001, C08-003, C08-004]
time_sensitive: false
---
# Data Curation (Section Lead-in)
(Source: PDF pp. 697-703; starts at the "Data Curation" heading part-way down PDF p. 697, the text above it belongs to C08-001)

## What the section covers
The opening of the data-curation section, before its three criteria: why data matters, who builds datasets, which data formats each finetuning goal needs, why complex behaviors (chain-of-thought and tool use) are costly to annotate, single-turn versus multi-turn data, curation as removal as well as addition, and the introduction of the three criteria quality, coverage and quantity.

## Why it matters
- Not every model problem can be fixed with data, but data is often a key part of the fix. The right data can make a model more capable, safer and able to handle longer contexts; poor data can amplify bias and hallucination. Data mistakes harm the model and waste resources (PDF p. 697).
- Curation is described as a science needing an understanding of how the model learns and what resources can help it learn (PDF p. 697).

## Who does it
Dataset builders should work closely with application and model developers. In a small team they may be one person, the one who trains the model also acquires its data. Organisations with heavy data needs often use specialised roles (PDF pp. 697-698).

## Meaning: data formats by training goal
The needed data depends on the task and what you want to teach (PDF p. 698):
- Self-supervised finetuning: sequences of data.
- Instruction finetuning: (instruction, response) pairs.
- Preference finetuning: (instruction, winning response, losing response) triples.
- Reward model training: either the preference format, or ((instruction, response), score) with a score annotated per example.

Training data must show the behaviors you want the model to learn. Annotation is always hard, and harder for complex behaviors such as chain-of-thought (CoT) reasoning and tool use (PDF p. 698).

## How it works: two hard-to-annotate behaviors

### Chain-of-thought
- CoT prompting (from Chapter 5) pushes a model to reason step by step before answering; to teach this, finetuning data must contain CoT responses. The "Scaling Instruction-Finetuned Language Models" study (cited as "Chun et al., 2024" in the book, both in the text and on the rendered page; the actual paper's first author is spelled Chung, UNVERIFIED against the book itself) reports that adding step-by-step responses to finetuning data greatly boosts models of various sizes on CoT tasks, with accuracy nearly doubling on some (PDF pp. 698-699).
- Multi-step responses are tedious and slow to write, since explaining a math solution is much harder than stating the answer. Two examples from that paper illustrate it. Without CoT: the question about nitrogen's boiling point is answered with "-320.4F". With CoT: the cafeteria question (23 apples, 20 used, 6 bought) is answered with the reasoning 23 - 20 = 3, then 3 + 6 = 9 (PDF pp. 699-700).
- Consequently CoT datasets are less common than other instruction datasets (PDF p. 700).

### Tool use
- Models may already know how to use some tools from pre-training, but showing tool-use examples improves the ability (PDF pp. 700-701).
- Domain experts commonly create the data: each prompt is a task needing tools, the response is the actions to perform it. For a personal-assistant model, you might ask professional assistants which tasks they do, how, and with which tools (PDF p. 701).
- Experts asked to explain their work may skip steps through faulty memory or because they think steps unimportant, so it is often necessary to watch them work (PDF p. 701).
- What is efficient for humans may not be for AI. A person may prefer a web interface while a model finds an API easier; a person opens a browser, pastes a query and clicks each result, whereas a model can call a search API and process all results at once. Human annotations may therefore be suboptimal for agents, which is why many turn to simulation and other synthetic generation, covered later in the chapter (PDF p. 701).
- Tool-use data can need special formats. Normal conversation has alternating turns of one message each, but tool use may need several messages per turn sent to different destinations, for example one to a code interpreter and one to the user. The Llama 3 authors designed a multi-message chat format with message headers naming source and destination, plus special termination tokens marking where human and AI turns begin (PDF pp. 701-702).

## Single-turn versus multi-turn
For conversational applications decide whether you need single-turn data, multi-turn data, or both. Single-turn data trains responses to individual instructions. Multi-turn data teaches the model to solve tasks, since real tasks involve back-and-forth: clarifying intent first, then accepting corrections or extra information. Single-turn data is simpler and easier to get; multi-turn data often needs purpose-built scenarios or more involved interactions (PDF p. 702).

## Curation also means removing data
- Curation includes deleting data so a model unlearns bad behavior (PDF pp. 702-703).
- Worked example: users complain a ChatGPT-like chatbot is arrogant and wastes tokens. Asked to verify a statement, it replies that the statement is correct but its style could be better, then rewrites it unasked. Investigation finds training annotations containing unsolicited suggestions. The fix is two requests: remove those examples, and acquire new examples that demonstrate fact-checking without unsolicited rewriting (PDF p. 703).

## The three criteria
Applications need different data and different training phases need different mixes, but at a high level curation follows three criteria: data quality, data coverage and data quantity (PDF p. 703). The cooking analogy: data is the ingredients. Quality is whether the ingredients are spoiled, coverage is having the right mix (not too much or too little sugar), and quantity is how many ingredients you have (PDF p. 703).

## Relations
Quality is C08-003 and coverage is C08-004; quantity follows in later rows of the chapter. Synthetic generation of tool-use data is taken up later in the chapter. The chapter framing is C08-001.
