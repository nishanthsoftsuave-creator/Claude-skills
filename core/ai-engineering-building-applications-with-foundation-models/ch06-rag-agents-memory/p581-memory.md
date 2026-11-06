---
id: C06-012
title: Memory
source_pages: "581-588"
chapter: 6
concepts: [memory-system, internal-knowledge, short-term-memory, long-term-memory, memory-management, fifo-eviction, summarization, reflection-memory, redundancy-removal]
related: [C06-011, C06-013]
time_sensitive: false
---
# Memory
(Source: PDF pp. 581-588; the paragraph at the top of p. 581 before the Memory heading belongs to C06-011. The section's last lines, about contradictory information, are at the top of the following page, before the Summary heading, and are described near the end below without a page cite.)

## What the section covers
What a memory system is for an AI model, the three memory mechanisms (internal knowledge, short-term and long-term memory), why to add a memory system, and how memory management works: what to add, what to delete, and strategies such as FIFO, summarization and reflection.

## Meaning
- Memory means mechanisms that let a model retain and use information. It is especially useful in knowledge-rich applications such as RAG and multi-step applications such as agents (PDF p. 581).
- A RAG system depends on memory for its augmented context, which grows over turns as more is retrieved. An agent needs memory for instructions, examples, context, tool inventories, plans, tool outputs, reflections and more (PDF p. 581).
- RAG and agents demand more of memory, but any application that must retain information benefits (PDF pp. 581-582).

### The three mechanisms (PDF pp. 582-583)
- Internal knowledge: the model itself, which keeps what it learned from its training data. It does not change unless the model is updated, and it is available to every query.
- Short-term memory: the model's context. Earlier messages in a conversation can be put in context so they inform later answers. It is called short-term because it does not persist across tasks (queries). Access is fast but capacity is limited, so it holds what matters most for the current task.
- Long-term memory: external data the model reaches through retrieval, as in RAG. It persists across tasks. Unlike internal knowledge, its contents can be deleted without updating the model.

The book offers a human analogy (PDF p. 583): how to breathe is internal knowledge; the name of someone you just met sits in short-term memory; long-term memory is extended with books, computers and notes.

### Deciding where data goes (PDF p. 583)
The choice depends on how often the information is used. Information essential for every task should be built into the model's internal knowledge by training or finetuning. Rarely needed information belongs in long-term memory. Short-term memory is for immediate, context-specific information.

Figure 6-16 (PDF p. 584), "The hierarchy of information for an agent", is a diagram. Context (short-term memory) feeds directly into the Model. External memory (long-term memory) feeds the model through a Retriever. Training data (internal knowledge) feeds the model too. Dotted arrows run from Context to the external memory labelled "Info less frequently used", and from Context to the training data labelled "Info essential for multiple tasks", showing where information migrates according to how often it is needed.

## Why it matters
Developers found quickly that memory is as important for AI models as for humans, and many memory management tools exist, with some model providers building in external memory (PDF p. 584). Benefits listed by the book:
- Manage information overflow within a session. During a task an agent collects new information that can exceed its maximum context length; the excess can go into long-term memory (PDF pp. 584-585).
- Persist information between sessions. An AI coach would be useless if you had to retell your life story each time, and an assistant that forgets your preferences would be annoying. With conversation history an agent can personalize; if it remembers you loved The Three-Body Problem, it can recommend similar books (PDF p. 585).
- Boost consistency. Just as a person is likelier to give the same rating to a joke twice if they remember the first rating, a model that can see its earlier answers can stay consistent with them (PDF p. 585).
- Maintain structural integrity of data. Text is unstructured, so data in a text model's context is too. You can paste a table in line by line but nothing guarantees the model treats it as a table. A memory system that stores structured data preserves structure; for example, an agent hunting sales leads can keep them in an Excel sheet, and a queue can hold the sequence of actions to perform (PDF pp. 585-586).

## How it works

### Two functions (PDF p. 586)
A memory system typically has memory management (deciding what to store in short-term and long-term memory) and memory retrieval (pulling task-relevant information from long-term memory). Retrieval resembles RAG retrieval, since long-term memory is an external data source; the book concentrates on management.

Management has two operations, add and delete. Deletion may be unnecessary when storage is not constrained, which often holds for long-term memory because external storage is cheap and easy to extend. Short-term memory is bounded by the model's maximum context length, so it needs a policy for what to add and delete (PDF p. 586).

### Overflow from short to long-term (PDF p. 587)
Long-term memory can absorb short-term overflow. The model's context for a query combines short-term memory and information retrieved from long-term memory, so short-term capacity depends on how much of the context is reserved for retrieved content. For instance, reserving 30% leaves at most 70% of the context limit for short-term memory; when that limit is reached, the overflow can be moved to long-term memory.

### Strategies
Memory management is not unique to AI; it has long been central to data systems, and many efficient strategies exist (PDF p. 587).
- FIFO (first in, first out): the earliest items in short-term memory are the first moved out. As a conversation grows, API providers such as OpenAI may drop the start of the conversation, and frameworks such as LangChain can keep the last N messages or N tokens. It assumes early messages matter less to the current discussion, which the book says can be "fatally wrong": early messages may carry the most information, especially if they state the conversation's purpose (PDF p. 587). It is easy to implement but can make the model lose key information (PDF p. 588). Two endnotes hang on this passage (printed with the chapter endnotes, recorded in C06-013): one remarks that in human conversations the opposite of the FIFO assumption could hold if the first messages are only pleasantries; the other says usage-based strategies, such as dropping the least frequently used information, are harder because you need a way to tell when the model actually uses a piece of information.
- Redundancy removal: human language is redundant for clarity and to cover misunderstandings, so automatically detecting redundancy could shrink the memory footprint a lot (PDF p. 588).
- Summarization: a summary of the conversation, produced by the same or another model, removes redundancy. Summarization combined with tracking named entities "can take you a long way" (PDF p. 588).
- Bae et al. (2022) went further: after getting a summary, they built a new memory by merging the existing memory with key information the summary missed, using a classifier that decides, for each memory sentence and each summary sentence, whether only one, both or neither should enter the new memory (PDF p. 588).
- Liu et al. (2023) used reflection: after each action the agent reflects on the information just generated, then decides whether the new information should be inserted into memory, merged with existing memory, or replace other information, especially when that other information is outdated and contradicts the new (PDF p. 588; the sentence finishes at the top of the next page).

### Contradictions
This closing point continues onto the next page. When pieces of information contradict one another, some people keep the newer item and some ask an AI model to decide which to keep. The right handling depends on the use case. Contradictions can confuse an agent but can also let it draw on different perspectives.

## When and how to apply
INTERPRETATION: sort each piece of information by frequency of use, using the book's rule: always needed goes into the model (training or finetuning), rarely needed goes to retrieval-backed long-term memory, immediate details stay in context. Reserve a fraction of the context window for retrieved memory and spill the rest, choosing the eviction policy by checking whether early messages in your use case carry the task's purpose.

## Limitations and failure modes
- FIFO can discard the very messages that define the conversation's goal (PDF p. 587).
- Short-term memory is limited by context length (PDF p. 586).

## Relations
Follows the agent failure-mode section (C06-011); the chapter closes with its summary (C06-013), which restates why a memory system is needed for RAG and agents.
