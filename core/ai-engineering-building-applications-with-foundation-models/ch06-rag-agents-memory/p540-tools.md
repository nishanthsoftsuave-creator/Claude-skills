---
id: C06-009
title: Agent Tools
source_pages: "540-545"
chapter: 6
concepts: [agent-tools, tool-inventory, read-only-actions, write-actions, knowledge-augmentation, capability-extension, web-browsing, code-interpreter, function-calling, chameleon]
related: [C06-008, C06-010, C06-011]
time_sensitive: false
---
# Agent Tools
(Source: PDF pp. 540-545, plus the first part of the tail page, PDF p. 546, that precedes the "Planning" heading. The lines at the very top of PDF p. 540, about higher stakes and the cost of multi-step tasks, close the previous section and are not covered here.)

## What the section covers
The "Tools" part of the Agents chapter: why external tools matter to an agent, the idea of a tool inventory, three categories of tools (knowledge augmentation, capability extension, and tools that let the agent write to its environment), the risks of write actions, and a closing remark that tool use is now offered by model providers as function calling. It sets up the next section, which explains how a planner decides when and how to use tools.

## Meaning
- The book frames an agent's success in an environment as depending on two things: the tool inventory it can use and the strength of its AI planner (PDF p. 540).
- A system does not strictly need tools to count as an agent, but without them it is limited. A bare model typically does one kind of thing: an LLM generates text, an image generator generates images. External tools make an agent far more capable (PDF p. 540).
- Tools serve two roles. Actions that let the agent perceive its environment are read-only actions; actions that let it change its environment are write actions (PDF p. 540).
- The set of tools an agent can use is its tool inventory (PDF p. 541).

## Why it matters
- The inventory defines what the agent can do, so deciding which tools to provide, and how many, is a core design decision. More tools mean more capability, but also make it harder for the agent to understand and use them well. The right set has to be found by experimentation, which the book takes up under "Tool selection" (PDF p. 541).
- Tool use can beat plain prompting or even finetuning. In Chameleon (Lu et al., 2023), a GPT-4 agent given 13 tools outperformed GPT-4 on its own on several benchmarks. The tools included knowledge retrieval, a query generator, an image captioner, a text detector and Bing search. On ScienceQA, a science question answering benchmark, it improved the best published few-shot result by 11.37%; on TabMWP (Tabular Math Word Problems), it improved accuracy by 17% (PDF p. 544).

## How it works: three categories of tools

### 1. Knowledge augmentation (context construction)
- These tools give the agent the context it needs for good answers, a theme the book has stressed throughout. Already covered examples are the text retriever, image retriever and SQL executor. Others mentioned: internal people search, an inventory API returning product status, Slack retrieval, an email reader (PDF p. 541).
- Many of these expose the organization's private processes and information, but tools can also reach public information, especially from the internet (PDF p. 542).
- Web browsing was among the earliest and most anticipated chatbot capabilities. It stops a model from going stale, meaning its training data has become outdated. A model with a cutoff last week cannot answer questions about this week's weather, news, events, stock prices or flight status unless that information is placed in context (PDF p. 542).
- The author uses "web browsing" as an umbrella for every tool that touches the internet: browsers plus specific APIs such as search, news, GitHub, and social media APIs (X, LinkedIn, Reddit) (PDF p. 542).
- Benefit: up-to-date information gives better responses and fewer hallucinations. Risk: exposure to the "cesspools of the internet", so internet APIs should be chosen carefully (PDF p. 542).

### 2. Capability extension
- These tools patch inherent weaknesses of models and are an easy way to boost performance. Models are poor at arithmetic; asked for 199,999 divided by 292 a model will probably fail, whereas a calculator makes it trivial. Giving the model a tool is more resource-efficient than training it to be good at arithmetic (PDF p. 543).
- Other simple boosters: calendar, timezone converter, unit converter (for example lbs to kg), and a translator for languages the model handles badly (PDF p. 543).
- Code interpreters are more complex but powerful. Rather than training a model to understand code, let it run code, return results or analyze failures. This turns agents into coding assistants, data analysts and research assistants that write code to run experiments and report results. The caveat is the risk of code injection attacks (covered in "Defensive Prompt Engineering"), so proper security measures are essential (PDF p. 543).
- External tools can make a single-modality model multimodal (PDF p. 544):
  - A text-only generator can call a text-to-image model; the agent's AI planner decides whether to call text generation, image generation, or both. ChatGPT producing text and images by using DALL-E is the book's example.
  - Agents can use a code interpreter for charts and graphs, a LaTeX compiler to render math, or a browser to render HTML.
  - A text-only-input model can use an image captioning tool for images, a transcription tool for audio, and OCR to read PDFs.

### 3. Write actions
- Read-only tools read from data sources; write actions change them. A SQL executor can retrieve a table but also alter or delete it; an email API can read an email and also reply; a banking API can return a balance and also start a transfer (PDF p. 545).
- Write actions let a system automate a whole workflow. The book's example is customer outreach: research prospects, find contacts, draft and send first emails, read replies, follow up, extract orders, and update databases with new orders (PDF p. 545).

## Limitations and failure modes (risks of write actions)
- Letting AI alter things automatically is frightening. The book's analogy: you would not give an intern authority to delete the production database, and likewise should not let an unreliable AI start bank transfers. Trust in both the system's capabilities and its security is crucial, including protection from bad actors who try to manipulate it into harmful actions (PDF p. 545).
- A common objection when the author discusses autonomous agents is self-driving cars being hacked. The book's reply: harm does not need a physical presence. An AI system can manipulate the stock market, steal copyrights, violate privacy, reinforce biases, and spread misinformation and propaganda (see "Defensive Prompt Engineering") (PDF pp. 545-546).

## When and how to apply
- Organizations using AI must take safety and security seriously, yet that should not mean AI is never allowed to act in the real world. The author hopes that, as people trust machines to go to space, security measures will one day justify trusting autonomous AI systems; humans also fail, and the author says they would trust a self-driving car over the average stranger as a driver (PDF p. 546).
- Tools make models far more productive in the way Excel or cranes do for people. Many model providers already support tool use, often called function calling, and the author expects function calling with a wide set of tools to become common across most models (PDF p. 546). The mechanics of function calling are in the Planning section (C06-010).

## Relations
Follows the Agents overview (C06-008). Feeds Planning, which explains plan generation, function calling and tool selection (C06-010), and the agent failure modes and evaluation section (C06-011).
