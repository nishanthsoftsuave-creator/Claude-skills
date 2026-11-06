---
id: C04-009
title: Model Build Versus Buy
source_pages: "359-376"
chapter: 4
concepts: [build-vs-buy, open-source-models, open-weight, model-licenses, model-api, inference-service, data-privacy, data-lineage, logprobs, self-hosting, on-device]
related: [C04-007, C04-008, C04-010, C04-006, C05-017, C07-002, C08-011, C09-002]
time_sensitive: true
---
# Model Build Versus Buy
(Source: PDF pp. 359-376)

## What the section covers
Part of the model selection discussion in Chapter 4. Because few companies train foundation models from scratch, "build versus buy" becomes: call a commercial model API, or host an open source model yourself. The answer can shrink the candidate pool a lot (PDF p. 359). The section first clarifies open source, open weight and licensing, then explains inference services and model APIs, and then compares the two options along seven axes: data privacy, data lineage, performance, functionality, cost, control, and on-device deployment. A summary table closes it (PDF pp. 359-377).

## Meaning
- Open source (original use): any model people can download and use. For many use cases, downloadability is enough (PDF p. 359).
- Dissenting view: since performance depends mostly on training data, a model is truly open only if its data is public too. Open data allows retraining from scratch with changes to architecture, training process or data, makes the model easier to understand, and supports audits (for example, checking for compromised or illegally acquired data) (PDF pp. 359-360).
- Vocabulary: "open weight" = weights released without open data; "open model" = weights released with open data. Some argue "open source" should be reserved for fully open models. The author uses "open source" for any model whose weights are public, whatever the data availability or license (PDF p. 360).
- Most open source models today are open weight only. Developers may hide data information on purpose, since it invites public scrutiny and lawsuits (PDF p. 360).
- Inference service: the service that hosts the model, receives queries, runs the model and returns responses. Its interface is the model API (Figure 4-6). Other APIs exist too, such as finetuning and evaluation APIs. Inference optimization is covered in Chapter 9 (PDF p. 362).
- "Restricted weight" is sometimes used for open models with restrictive licenses; the author finds it ambiguous because all sensible licenses restrict something, for example you should not be allowed to use a model to commit genocide (PDF p. 362).

## Model licenses
- Open source licensing was already confusing (MIT, Apache 2.0, GPL, BSD, Creative Commons), and models made it worse because many carry unique licenses: Meta's Llama 2 and Llama 3 community license agreements, Hugging Face's BigCode Open RAIL-M v1. Google's Gemma and Mistral-7B use Apache 2.0. The author hopes the community converges on standard licenses (PDF pp. 360-361).
- Each license has its own conditions, so you must evaluate each one. Three questions everyone should ask (PDF p. 361):
  1. Does it allow commercial use? The first Llama release was noncommercial.
  2. If so, what restrictions apply? Llama 2 and Llama 3 require a special license from Meta for applications with more than 700 million monthly active users.
  3. Can the model's outputs be used to train or improve other models? Synthetic data is an important training source (Chapter 8), and distillation (a smaller student mimicking a larger teacher) is one use. Mistral initially forbade this but later changed its license; at the time of writing the Llama licenses still forbid it.

## Open source models versus model APIs
- A developer can open source a model, serve it through an API, or both. Cohere and Mistral open source some models and offer APIs for others. OpenAI is known for commercial models but open sourced GPT-2 and CLIP. Typically providers open source weaker models and keep the best behind paywalls, through APIs or their own products (PDF p. 363).
- APIs come from model providers (OpenAI, Anthropic), cloud providers (Azure, GCP) or third parties (Databricks Mosaic, Anyscale). The same model can be offered through several APIs with different features, constraints and prices; GPT-4 is on both OpenAI and Azure. Performance can differ slightly because providers optimize differently, so test thoroughly when switching APIs (PDF p. 363).
- Commercial models are reachable only through APIs licensed by their developers. Open source models can be served by any provider, so you can pick the best one. Commercial providers compete on their models; API-only providers compete on their APIs, so they may be more motivated to offer better APIs and pricing (PDF pp. 363-364).
- Building scalable inference for big models is hard, which has produced many third-party inference and finetuning services over open source models. AWS, Azure and GCP all give API access to popular open source models, as do many startups (PDF p. 364).
- Note: some commercial providers deploy inside your private network; the book treats these like self-hosted models (PDF p. 364).
- The decision depends on the use case and can change over time for the same use case. The seven axes follow (PDF p. 364).

## Axis 1: Data privacy
- Externally hosted APIs are out for organizations with strict policies against sending data out. Early example: Samsung employees pasted proprietary information into ChatGPT, leaking secrets; Samsung banned ChatGPT in May 2023. It is unclear how the leak was found or exploited (PDF pp. 364-365).
- Some countries forbid sending certain data across borders; an API provider serving them must set up servers there (PDF p. 365).
- Risk that the provider trains on your data. Most claim they do not, but policies change: in August 2023 Zoom drew backlash after quietly changing its terms to allow use of service-generated data (usage and diagnostics) for AI training (PDF p. 365).
- Why it matters: models can memorize training samples. Hugging Face's StarCoder was found to memorize 8% of its training set. Memorized samples can leak accidentally or be exploited by attackers (shown in Chapter 5) (PDF p. 365).

## Axis 2: Data lineage and copyright
- These concerns can push a company toward open models, toward proprietary ones, or away from both (PDF pp. 365-366).
- Transparency about training data is usually poor. Google's Gemini technical report detailed performance but said about data only that enrichment workers are paid at least a local living wage; OpenAI's CTO could not give a satisfactory answer about training data (PDF p. 366).
- IP law is evolving. The USPTO said in 2024 that AI-assisted inventions are not categorically unpatentable; patentability depends on whether the human contribution is significant enough. It is unclear whether you can defend your product's IP if the model was trained on copyrighted data. Companies that live on IP, such as game and movie studios, hesitate to use AI in production until laws clarify (PDF p. 366).
- Fully open models attract some companies because the community can inspect the data, but in practice thoroughly inspecting a dataset of foundation-model size is very hard for any company (PDF pp. 366-367).
- Many companies pick commercial models instead. Open source models have limited legal resources; if one infringes copyright, the injured party is more likely to pursue you than the developers. Contracts with commercial providers can potentially protect you from lineage risk (PDF p. 367).

## Axis 3: Performance
- Benchmarks show the gap between open source and proprietary models closing; Figure 4-7 shows this on MMLU over time (image by Maxime Labonne). Many infer that an open model will eventually match or beat the strongest proprietary one (PDF pp. 367-368).
- What Figure 4-7 shows (rendered p. 368): a scatter of 5-shot MMLU scores against release date, from about April 2022 to mid-2024, with the y-axis running from roughly 42% to 90%. Closed-source models are red points and open-weight models green points; a dashed red curve traces the closed-source frontier and a dashed green curve the open-weight frontier, with the shaded region between them narrowing over time. Early on, closed models such as PaLM and Chinchilla sit near the high 60s while the open-weight line starts far lower (Flan-T5 11B near the mid-50s). GPT-4 (about 86%) is well above any open model in early 2023. By mid-2024 the two frontiers nearly meet near the high 80s: Claude 3.5 Sonnet and GPT-4o at the top, Llama 3.1 405B just below. Values are approximate readings from the chart (PDF p. 368).
- The author doubts incentives allow this: a company with the strongest model would rather monetize it than give it away, so strongest models stay behind APIs and weaker ones get open sourced. The best open model will likely trail the best proprietary models for the foreseeable future, though for many use cases that do not need the strongest model, open source may suffice (PDF pp. 367-368).
- Another cause of lag: open source developers get no user feedback, since after release they do not know how the model is used or how well it works in the wild (PDF p. 368).

## Axis 4: Functionality
- Functionality needed around a model includes: scalability (traffic at acceptable latency and cost), function calling (tool use, essential for RAG and agents, Chapter 6), structured outputs such as JSON, and output guardrails (for example against racist or sexist output). These are hard and slow to build, so many companies buy them from API providers (PDF p. 369).
- Downside: you are limited to what the API offers. Logprobs help with classification, evaluation and interpretability, but providers may hide them for fear of replication, so many APIs expose none or only limited logprobs (PDF p. 369).
- Finetuning: you can finetune a commercial model only if the provider allows it. If you have maxed out prompting and the provider has no finetuning API, you are stuck. With open source you can use a finetuning service or do it yourself. Several types exist (partial, full; Chapter 7) and a commercial provider may support only some (PDF p. 370).

## Axis 5: API cost versus engineering cost
- APIs charge per usage and can become prohibitive at heavy use; at some scale hosting your own may make sense. But self-hosting takes time, talent and engineering: optimizing the model, scaling and maintaining the inference service, and building guardrails. "APIs are expensive, but engineering can be even more so" (PDF p. 370).
- Using an API also means depending on its SLA (service-level agreement). Unreliable APIs, common with early startups, force you to spend engineering effort on guardrails around them (PDF p. 370).
- General preference: a model that is easy to use and manipulate. Proprietary models are usually easier to start with and scale; open models may be easier to manipulate because their components are accessible. Either way, prefer a standard API so models are easy to swap; many developers mimic the most popular API, and many providers currently mimic OpenAI's (PDF p. 371).
- Prefer models with good community support: more capabilities mean more quirks, and a large user base means others may already have hit and solved your problem (PDF p. 371).

## Axis 6: Control, access and transparency
- A 2024 a16z study found control and customizability to be the two key reasons enterprises care about open source (Figure 4-8). From the rendered figure: across all reasons cited, control 37%, customizability 37%, cost 26%; as the primary reason cited, control 60%, customizability 30%, cost 10% (PDF pp. 371-372).
- With a third-party service you are subject to its terms and rate limits and can reach only what it exposes, so you may not be able to tweak the model (PDF p. 372).
- Providers add safety guardrails (blocking racist jokes or images of real people) to protect users and themselves from lawsuits. Proprietary models tend to over-censor. Fine for most uses, but limiting for some: an application needing real faces (say, for a music video) fails if the model refuses. Convai, a company the author advises that builds interactive 3D AI characters, kept getting "As an AI model, I don't have physical abilities" from commercial models and ended up finetuning open source ones (PDF pp. 372-373).
- Risk of losing access: you cannot freeze a commercial model as you can an open one. Historically providers have been opaque about changes, versions and roadmaps; models are updated often, not always announced, so prompts may silently stop working. Such unpredictability makes commercial models unusable for strictly regulated applications. The author suspects the opacity is an unintentional side effect of a fast-growing industry and hopes it improves (PDF p. 373).
- Rarer risks: a provider may drop support for your use case, industry or country; your country may ban the provider (Italy briefly banned OpenAI in 2023); or the provider may go out of business (PDF p. 373).

## Axis 7: On-device deployment
Third-party APIs are impossible for on-device use. Reasons to run locally: the target area lacks reliable internet, or privacy, for example giving an assistant access to all your data without it leaving the device (PDF p. 374).

## Summary table (Table 4-4)
The table compares using model APIs with self-hosting (PDF pp. 375-377, rendered p. 376-377 checked); cons are italicized in the original.
- Data: APIs require sending data to providers, so your team can accidentally leak confidential information; there are also fewer checks on data lineage and copyright. Self-hosting keeps data internal.
- Performance: the best-performing model is likely closed source; the best open models likely lag a bit.
- Functionality: APIs more likely support scaling, function calling and structured outputs but less likely expose logprobs. Self-hosting has no or limited function calling and structured output support, but gives access to logprobs and intermediate outputs, useful for classification, evaluation and interpretability.
- Cost: API cost versus the talent, time and engineering effort to optimize, host and maintain (mitigable with model hosting services).
- Finetuning: APIs allow it only for models providers permit. Self-hosting can finetune, quantize and optimize (if licenses allow) but it can be hard.
- Control, access, transparency: APIs bring rate limits, risk of losing access, and a lack of transparency in changes and versioning. Self-hosting makes it easier to inspect changes and lets you freeze a model, though you are then responsible for building and maintaining the model APIs (PDF pp. 376-377).
- Edge use cases: APIs cannot run on a device without internet access. Self-hosting can run on device, though, again, this might be hard to do (PDF p. 377).
- Closing remark: the pros and cons should help decide between a commercial API and self-hosting, and this decision should considerably narrow the options; the next step is refining the choice with publicly available model performance data (PDF p. 377).

## When and how to apply
INTERPRETATION: treat the seven axes as a checklist for each use case and revisit it over time, since the book says the answer can change. The book's own cues: strict privacy or cross-border data rules and on-device needs rule out external APIs; need for logprobs, finetuning or fine control favors open models; need for the strongest model, scalability, function calling and structured outputs out of the box favors commercial APIs; review each model's license against the three questions above before adopting it.

## Time-sensitive statements
Licensing terms (Llama's 700 million user threshold, the Llama restriction on using outputs for training, Mistral's license change), Zoom and Samsung incidents dates, the USPTO 2024 position, the Italy ban, which providers expose logprobs, OpenAI API mimicry, and the open versus proprietary MMLU gap are all as of the book's writing.

## Relations
Continues model selection in Chapter 4: C04-007 (lead-in) and C04-008 (selection workflow) precede it, C04-006 covers cost and latency criteria, and C04-010 (public benchmarks) follows. Inference services (Chapter 9), memorization and attacks (Chapter 5), tool use (Chapter 6), finetuning types (Chapter 7) and data synthesis/distillation (Chapter 8) are developed in later chapters.
