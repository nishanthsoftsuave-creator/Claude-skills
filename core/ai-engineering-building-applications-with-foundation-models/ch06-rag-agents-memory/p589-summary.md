---
id: C06-013
title: Chapter 6 Summary and Notes
source_pages: "589-593"
chapter: 6
concepts: [rag-summary, agent-summary, retriever-quality, term-based-retrieval, embedding-based-retrieval, vector-search, prompt-based-methods, chapter-endnotes]
related: [C06-011, C06-012]
time_sensitive: false
---
# Chapter 6 Summary and Notes
(Source: PDF pp. 589-593; the first lines of p. 589 above the Summary heading finish the memory section and belong to C06-012. Chapter 7 begins on the next page.)

## What the section covers
The chapter wrap-up on RAG, agents and memory, followed by the chapter's endnotes (PDF pp. 591-593).

## Summary content

### RAG
- Readers told the author this was the chapter they were most excited about, given the popularity of RAG and agent potential (PDF p. 589).
- RAG came first. Many tasks need background knowledge that exceeds the context window: code copilots may need whole codebases, research assistants may need to analyze several books. RAG was originally created to get around context limits, but it also uses information more efficiently, improving response quality and cutting cost. It was seen from the start as hugely valuable and has been adopted widely in consumer and enterprise settings (PDF p. 589).
- RAG is a two-step process: retrieve relevant information from external memory, then use it to generate more accurate responses. Its success hinges on the retriever's quality. Term-based retrievers (Elasticsearch, BM25) are much lighter to implement and make strong baselines. Embedding-based retrievers cost more computation but may outperform term-based ones (PDF p. 590).
- Embedding-based retrieval rests on vector search, which also underpins internet applications such as search and recommender systems, so many vector search algorithms built for those can be reused for RAG (PDF p. 590).

### Agents
- RAG can be viewed as a special case of an agent whose retriever is a tool the model can use. Both help a model get past its context limit and stay current, but agents can do more (PDF p. 590).
- An agent is defined by its environment and the tools it can access. In an AI-powered agent, the AI is the planner: it analyzes the task, weighs solutions and selects the most promising. Complex tasks need many steps, hence a strong planning model. Planning can be strengthened with reflection and a memory system that tracks progress (PDF p. 590).
- More tools mean more capabilities and harder solvable tasks, but the more automated the agent, the more catastrophic its failures can be. Tool use brings the security risks of Chapter 5, so real-world agents need rigorous defenses (PDF pp. 590-591).

### Memory and what comes next
- RAG and agents both handle information that often surpasses the model's maximum context length, which calls for a memory system to manage it; the chapter ended with a short look at that component (PDF p. 591).
- Both are prompt-based methods: they affect quality only through inputs, leaving the model unchanged. Changing the model itself opens further possibilities, which is the topic of the next chapter (PDF p. 591).

## Endnotes (as recorded in the book)
- Note 1: the model used in the early retrieval-augmented work was an LSTM (Long Short-Term Memory) recurrent network, the dominant deep learning architecture for NLP until the transformer took over in 2018 (PDF p. 591).
- Note 2: around the same time another Facebook paper, "How Context Affects Language Models' Factual Predictions" (Petroni et al., May 2020), showed that adding a retrieval system to a pretrained language model can greatly improve its performance on factual questions (PDF p. 591).
- Note 3: the author credits Chetan Tekur for an example (PDF p. 591).
- Note 4: Parkinson's Law, "Work expands so as to fill the time available", has an analogue in the author's theory that an application's context expands to fill whatever context limit the model supports (PDF p. 592).
- Note 5: information retrieval dates to the 1920s, to Emanuel Goldberg's patents for a "statistical machine" that searched documents on film; the source cited is Sanderson and Croft, "The History of Information Retrieval Research" (Proceedings of the IEEE, April 2012) (PDF p. 592).
- Note 6: for BM25, the author recommends Robertson and Zaragoza, "The Probabilistic Relevance Framework: BM25 and Beyond" (Foundations and Trends in Information Retrieval, 2009) (PDF p. 592).
- Note 7: Aravind Srinivas, Perplexity's CEO, tweeted that genuinely improving on BM25 or full-text search is hard (PDF p. 592).
- Note 8: a RAG retrieval workflow shares many steps with a traditional recommender system (PDF p. 592).
- Note 9: some teams told the author their retrieval works best when data is organized as question-and-answer pairs (PDF p. 592).
- Note 10: Artificial Intelligence: A Modern Approach (1995) defines an agent as anything viewed as perceiving its environment via sensors and acting on it via actuators (PDF p. 592).
- Note 11: an early complaint was that agents were only good for burning through API credits (PDF p. 592).
- Note 12: since most agentic workflows are complex enough to involve several components, most agents are multi-agent (PDF p. 592).
- Note 13: Chameleon (Lu et al., 2023) calls the translator a program generator (PDF p. 592).
- Note 14: this resembles the actor-critic (AC) agent method (Konda and Tsitsiklis, 1999) from reinforcement learning (PDF p. 593).
- Note 15: for human conversations the opposite of the FIFO assumption might hold if the first few messages are pleasantries (PDF p. 593).
- Note 16: usage-based strategies, such as removing the least frequently used information, are harder, since you need a way to know when the model uses a given piece of information (PDF p. 593).
Anchoring of the notes: notes 15 and 16 have visible superscripts on the rendered pages of the memory section (15 after the FIFO paragraph's closing sentence, 16 after the sentence that FIFO can lose track of important information; both sit on the last two pages of the memory section, before this row's range), so they annotate the FIFO strategy covered in C06-012. Notes 1-14 annotate passages in earlier sections of the chapter, outside this row's range; the rendered summary pages (589-591) carry no legible superscripts and the note numbers on p. 591-593 are not matched to body text by the PDF.
UNVERIFIED: which exact earlier-chapter passage each of notes 3-14 is attached to was not read from superscripts in this row's pages; only the note contents above are certain.

## Relations
Recaps the agent evaluation (C06-011) and memory (C06-012) sections. Chapter 7 on finetuning follows, introduced as adapting a model by adjusting its weights, in contrast to the prompt-based methods of Chapters 5 and 6.
