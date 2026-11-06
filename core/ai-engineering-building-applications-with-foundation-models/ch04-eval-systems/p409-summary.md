---
id: C04-014
title: Chapter 4 Summary
source_pages: "409-415"
chapter: 4
concepts: [chapter-summary, evaluation-pipeline, model-selection, public-benchmarks, host-vs-api, contamination, private-leaderboard]
related: [C04-012, C04-013]
time_sensitive: true
---
# Chapter 4 Summary
(Source: PDF pp. 409-415)

## What the section covers
The closing summary of Chapter 4 (PDF pp. 409-411), plus the chapter's footnotes (PDF pp. 411-415). The first lines of p. 409 finish the "Iterate" discussion of the previous section (C04-013); that content is recorded below because C04-013 ends on the preceding page. The chapter's next topic, prompt engineering, starts after this row.

## End of the Iterate discussion (top of p. 409)
- If the evaluation process changes constantly, you cannot use its results to guide application development (PDF p. 409).
- While iterating on the pipeline, do proper experiment tracking: log every variable that could change in an evaluation run, including but not limited to the evaluation data, the rubric, and the prompt and sampling configuration of any AI judge (PDF p. 409).

## Summary content
- The author calls this one of the hardest and, she believes, most important topics she has written about. Lacking a reliable evaluation pipeline is among the biggest blocks to AI adoption. Evaluation takes time, but a reliable pipeline lets you reduce risk, find ways to improve performance and benchmark progress, saving time later (PDF p. 409).
- With so many foundation models available, most application developers face the challenge of selecting a model, not building one. The chapter covered criteria used to evaluate models for applications and how each is evaluated, including domain-specific capabilities and generation capabilities such as factual consistency and safety. Many criteria came from traditional NLP, including fluency, coherence and faithfulness (PDF pp. 409-410).
- To decide between hosting a model and using a model API, the chapter weighed pros and cons on seven axes, including data privacy, data lineage, performance, functionality, control and cost. As with any build-versus-buy decision, the answer is unique to each team and depends on what the team wants as well as needs (PDF p. 410).
- On public benchmarks: they help weed out bad models but not find the best one for your application. They are likely contaminated because their data is in many models' training data. Leaderboards aggregate several benchmarks to rank models, yet how benchmarks are chosen and aggregated is unclear. Lessons from leaderboards help model selection, since selection amounts to building a private leaderboard that ranks models by your needs (PDF p. 410).
- The chapter ended with using the evaluation techniques and criteria to build an evaluation pipeline. No perfect method exists: a high-dimensional system cannot be captured by one or a few scores, and modern AI evaluation has many limitations and biases. That is no reason not to evaluate; combining methods mitigates many problems (PDF pp. 410-411).
- Evaluation recurs later: Chapter 6 covers evaluating retrieval and agentic systems; Chapters 7 and 9 cover computing memory usage, latency and cost; Chapter 8 covers data quality verification; Chapter 10 covers user feedback for evaluating production applications. The next chapter moves to model adaptation, beginning with prompt engineering (PDF p. 411).

## Footnotes (as recorded in the book)
- Recommendations can increase purchases, but not all increased purchases stem from good recommendations; promotions and launches also matter, so A/B testing is needed to separate impact (PDF p. 411).
- GPT-2's buzz in 2019 came partly from text notably more fluent and coherent than earlier language models. A prompt shown in the chapter contains a typo copied from the Liu et al. (2023) paper, illustrating how easily humans err in prompts (PDF p. 411).
- Textual entailment is also called natural language inference (NLI). Anthropic has a tutorial on using Claude for content moderation. Structured outputs are covered in Chapter 2 (PDF p. 412).
- Few comprehensive studies exist on the distribution of instructions people give foundation models. LMSYS studied one million Chatbot Arena conversations, but these are not grounded in real applications (PDF p. 412).
- Roleplay evaluation: a model playing Jackie Chan must not say things he does not know (for instance, speaking Vietnamese if he does not). This "negative knowledge" check matters in gaming so an NPC does not leak spoilers (PDF p. 412).
- Electricity cost can vary with usage. An argument for public training data is that models are trained on web data created by the public (PDF p. 412).
- Some licenses bar offering the open source model as a hosted competing service, in spirit like the Elastic License. A model's outputs may be unusable to improve other models even if its own license permits it: model X trained on ChatGPT outputs may breach ChatGPT's terms, which is why data lineage matters (PDF p. 412).
- As of writing, GPT-4 models were reachable only via OpenAI or Azure; some argue offering services on OpenAI's proprietary models was a key reason Microsoft invested (PDF pp. 412-413).
- Some companies with strict data privacy rules still accept data going to models hosted on GCP, AWS or Azure, because for them privacy is about which services they trust. A reported incident involved Samsung workers misusing ChatGPT (April 2023). Auditable model and training data requirements may grow with regulation, and commercial models may offer certifications (PDF p. 413).
- Open source incentives: many companies profit from inference and finetuning services on open models, raising the question of why developers would invest heavily; the author notes Meta may support open source to check competitors, and Mistral and Cohere compete with services built on their own models. She hopes societal benefit and goodwill sustain open source (PDF p. 413).
- Companies hit hardest by API costs are probably not the largest, which can negotiate terms. Preferring popular, widely tested tools mirrors a software infrastructure habit (PDF p. 413).
- Hugging Face's Lewis Tunstall said their leaderboard benchmarks were guided by those used by then-popular models. Leaderboards have since become more transparent; Hugging Face published an analysis of benchmark correlation (2024) (PDF p. 414).
- Benchmarks shifted from grade-level to graduate-level questions in a couple of years. The author suggests a "neverending benchmark" that procedurally generates harder problems as models improve, like neverending games (PDF p. 414).
- The same model update can hurt some applications and help others: moving from GPT-3.5-turbo-0301 to GPT-3.5-turbo-1106 cut Voiceflow's intent classification by 10% but improved GoDaddy's support chatbot. Check how reliable any public score is (PDF p. 414).
- HELM reported a total cost of $38,000 for commercial APIs and 19,500 GPU hours for open models; at $2.15 to $3.18 per GPU hour, roughly $80,000 to $100,000 overall. A friend's quip: a benchmark stops being useful once it is public. The 3.3 factor in the sample-size rule is the square root of 10 (PDF p. 414).
- If two benchmarks (say translation and math) are uncorrelated, you may infer that improving one capability does not affect the other (PDF p. 415).

## Time-sensitive statements
GPT-4 availability (OpenAI or Azure only), the HELM cost estimate and GPU prices, the GPT-3.5 version migration anecdote, and the leaderboard transparency note reflect the date of writing (PDF pp. 412-414).

## Relations
Wraps up the pipeline steps in C04-012 and C04-013.
