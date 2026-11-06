---
id: C01-015
title: Use Case Evaluation
source_pages: "79-84"
chapter: 1
concepts: [use-case-evaluation, build-vs-buy, critical-vs-complementary, reactive-vs-proactive, dynamic-vs-static, human-in-the-loop, crawl-walk-run, defensibility, moats]
related: [C01-014, C01-016, C01-017, C01-005]
time_sensitive: true
---
# Use Case Evaluation
(Source: PDF pp. 79-84)

## What the section covers
The first planning question: why build this application. It covers three levels of motivating risk, the build-versus-buy consideration, the roles AI and humans play in the product, and how defensible a standalone AI product is.

## Why build: risks and opportunities, high to low
Building an AI application is often a response to risks and opportunities (PDF p. 79). The book orders three situations from high risk to low:
1. Competitors with AI can make you obsolete. If AI is an existential threat, adopting it must be top priority. In the 2023 Gartner study, 7% cited business continuity as their reason for adopting AI. This is common for document processing and information aggregation businesses (financial analysis, insurance, data processing) and for creative work (advertising, web design, image production). The 2023 OpenAI study "GPTs are GPTs" (Eloundou et al., 2023) ranks industries by exposure to AI (PDF p. 79).
2. You will miss chances to raise profit and productivity. Most companies adopt AI for opportunity. It can lower user-acquisition cost through better copy, product descriptions and promotional visuals; raise retention through better support and personalization; and help with lead generation, internal communication, market research and competitor tracking (PDF p. 79).
3. You are unsure where AI fits but do not want to be left behind. Companies should not chase every hype train, yet many failed by waiting too long (Kodak, Blockbuster, BlackBerry are named). Investing to understand how a transformational technology could affect the business is reasonable if affordable; in big companies it can sit in R&D (PDF p. 80).

## Build or buy
If AI is an existential threat, consider doing it in-house rather than outsourcing to a competitor. If AI is for profit and productivity, there may be plenty of buy options that save time and money and perform better (PDF p. 80).

## The role of AI and humans in the application
The AI's role shapes development and requirements. The book draws on an Apple document describing ways AI is used in products and takes three dimensions from it (PDF p. 80).

### Critical or complementary
- If the app still works without AI, AI is complementary. Face ID does not work without AI face recognition (critical); Gmail still works without Smart Compose (complementary) (PDF pp. 80-81).
- The more critical AI is, the more accurate and reliable it must be. People tolerate mistakes more when AI is not core (PDF p. 81).

### Reactive or proactive
- A reactive feature responds to user requests or actions (a chatbot); a proactive feature responds when an opportunity arises (Google Maps traffic alerts) (PDF p. 81).
- Reactive features usually, but not always, need to be fast. Proactive ones can be precomputed and shown opportunistically, so latency matters less (PDF p. 81).
- Users did not ask for proactive features and may find low-quality ones intrusive or annoying, so proactive predictions and generations typically face a higher quality bar (PDF p. 81).

### Dynamic or static
- Dynamic features update continually with user feedback; static ones update periodically. Face ID must keep up as faces change; object detection in Google Photos is probably updated only when the app is upgraded (PDF pp. 81-82).
- For AI, dynamic can mean a model per user, continually finetuned on their data, or other personalization such as ChatGPT's memory feature that remembers preferences. Static features may use one model for a group of users and update only when that shared model does (PDF p. 82).

### Role of humans
Decide whether AI supports humans in the background, makes decisions directly, or both. For a support chatbot the options are: AI shows several candidate responses that human agents consult to write faster; AI answers only simple requests and routes complex ones to humans; or AI answers everything directly (PDF p. 82). Involving humans in AI's decisions is called human-in-the-loop (PDF p. 82).

Microsoft (2023) proposed the Crawl-Walk-Run framework for gradually increasing automation (PDF p. 83):
1. Crawl: human involvement is mandatory.
2. Walk: AI can interact directly with internal employees.
3. Run: more automation, possibly including AI interacting directly with external users.

The human role can shrink as quality improves. Example: start by generating suggestions for human agents; if the acceptance rate is high (the book gives 95% of AI-suggested responses to simple requests used verbatim), let customers interact with the AI directly for those simple requests (PDF p. 83).

## AI product defensibility
- For standalone AI products, defensibility matters. A low entry barrier is a blessing and a curse: if it is easy for you to build, it is easy for competitors. What moats do you have? (PDF p. 83)
- An application is a layer over foundation models, so if the models gain capability, the layer can be subsumed and the app obsolete. Example: a PDF-parsing app built on the assumption that ChatGPT parses PDFs poorly or cannot do it at scale weakens once that assumption fails. Even then it may still make sense if built on open source models for users who want to host in-house (PDF pp. 83-84).
- A VC general partner told the author many startups have products that could be a feature of Google Docs or Microsoft Office; what would stop those firms from assigning three engineers to copy them in two weeks? (PDF p. 84)
- Three kinds of competitive advantage: technology, data, and distribution (getting the product in front of users). With foundation models most companies' core technology will be similar, and distribution likely favors big companies. Data is more nuanced: big companies have more existing data, but a startup that reaches market first and collects enough usage data to keep improving can make data its moat. Even where user data cannot be used for training directly, usage information gives insight into user behavior and product shortcomings that can guide data collection and training (PDF p. 84).
- The counterpoint (successful companies that began as features of bigger products) opens the next row (C01-016).

## Relations
Follows the planning lead-in (C01-014); next comes setting expectations (C01-016) and milestone planning (C01-017). The use cases motivating these decisions were surveyed in C01-005.

## Time-sensitive statements
The Gartner 2023 figure, the OpenAI 2023 study, product examples (Face ID, Smart Compose, ChatGPT memory, Google Maps) and the ChatGPT PDF-parsing example reflect the time of writing.
