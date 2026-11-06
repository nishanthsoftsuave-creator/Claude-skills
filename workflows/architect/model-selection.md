---
name: model-selection
mode: architect
rows: [C02-003, C02-004, C02-005, C02-006, C02-008, C02-009, C03-019, C03-020, C04-008, C04-009, C04-010]
---
# Model selection

## When to use

After `use-case-and-requirements.md`. Use it to choose one model or a short list, and to decide build versus buy (commercial API or self-hosted open model). Also use it when a user asks "which model" or "should we self-host". Model names, prices, licenses and leaderboards in the modules are time-sensitive; treat them as examples and re-check current data.

## Inputs needed

Hard requirements and ideals for cost, scale and latency, the quality criteria and usefulness threshold, languages and domains served, data sensitivity and residency rules, hosting options, team capacity to operate models. These come from `use-case-and-requirements.md` and `intake.md`; ask only for what is missing.

## Modules to load

| Row | Module | Why it is needed here |
|---|---|---|
| C02-003 | [Multilingual Models](../../core/ai-engineering-building-applications-with-foundation-models/ch02-foundation-models/p124-multilingual-models.md) | Language fit, token cost and latency by language |
| C02-004 | [Domain-Specific Models](../../core/ai-engineering-building-applications-with-foundation-models/ch02-foundation-models/p131-domain-specific-models.md) | Whether training data covers your domain |
| C02-005 | [Model Architecture](../../core/ai-engineering-building-applications-with-foundation-models/ch02-foundation-models/p135-model-architecture.md) | Architecture limits on cost and context |
| C02-006 | [Model Size](../../core/ai-engineering-building-applications-with-foundation-models/ch02-foundation-models/p151-model-size.md) | Parameters, MoE, memory and cost reading |
| C02-008 | [Supervised Finetuning](../../core/ai-engineering-building-applications-with-foundation-models/ch02-foundation-models/p173-supervised-finetuning.md) | What instruction-tuned models already received |
| C02-009 | [Preference Finetuning](../../core/ai-engineering-building-applications-with-foundation-models/ch02-foundation-models/p179-preference-finetuning.md) | What preference tuning does and its limits |
| C03-019 | [Challenges of Comparative Evaluation](../../core/ai-engineering-building-applications-with-foundation-models/ch03-eval-methodology/p302-challenges-of-comparative-evaluation.md) | Limits of arena-style rankings |
| C03-020 | [The Future of Comparative Evaluation](../../core/ai-engineering-building-applications-with-foundation-models/ch03-eval-methodology/p308-the-future-of-comparative-evaluation.md) | Where comparative rankings are still useful |
| C04-008 | [Model Selection Workflow](../../core/ai-engineering-building-applications-with-foundation-models/ch04-eval-systems/p356-model-selection-workflow.md) | The four-step selection loop |
| C04-009 | [Model Build Versus Buy](../../core/ai-engineering-building-applications-with-foundation-models/ch04-eval-systems/p359-model-build-versus-buy.md) | Seven axes, licenses, API versus self-hosting |
| C04-010 | [Navigate Public Benchmarks](../../core/ai-engineering-building-applications-with-foundation-models/ch04-eval-systems/p377-navigate-public-benchmarks.md) | Shortlisting from benchmarks, contamination |

## Procedure

1. **Split attributes into hard and soft.** Hard attributes are impossible or impractical for you to change (license, training data, model size, your privacy policy, control needs). Soft attributes can be improved (accuracy, toxicity, factual consistency). The split depends on the use case: latency is soft if you host and can optimize, hard if someone else hosts. Estimate improvability realistically; the book saw accuracy rise from about 20% to 70% by splitting a task into two steps, and also a model that stayed unusable after weeks of tweaking. `[C04-008]`
2. **Filter by hard attributes (build versus buy).** Few teams train foundation models, so the choice is a commercial API or hosting an open model. Walk the seven axes and record the verdict for each. `[C04-009]`

   | Axis | Rule from the book | 
   |---|---|
   | Data privacy | Strict no-external-data policy or cross-border limits rule out external APIs; check whether the provider may train on your data (policies change); models can memorize training data |
   | Data lineage and copyright | Provider contracts can offer some protection; open data is hard to inspect at scale; IP-heavy firms may hesitate |
   | Performance | The strongest model is likely closed; the best open model likely lags; many use cases do not need the strongest |
   | Functionality | APIs more likely give scaling, function calling, structured outputs, guardrails; self-hosting gives logprobs and intermediate outputs. Finetuning of an API model only if the provider allows it; open models can be finetuned or quantized if the license allows |
   | Cost | API per-token cost versus engineering talent, time, maintenance and API reliability (SLA); re-check at scale |
   | Control and access | Rate limits, silent model changes, over-censoring and loss of access (APIs) versus frozen, inspectable models you must then serve and maintain (self-hosted). Prefer a standard API so models can be swapped, and models with community support |
   | On-device | Third-party APIs cannot run offline or on device |

   Also ask the three license questions for every open model: commercial use allowed, what restrictions apply, and can outputs be used to train or improve other models. `[C04-009]`
3. **Check language fit.** If users are not mostly English speakers, look up the model's results in that language. English is almost half of Common Crawl, under-represented languages score lower, and the same text can need many more tokens (the book's example: median 7 tokens in English versus 72 in Burmese), which raises cost and latency about proportionally. Translating through English is not a clean fix (needs a model that understands the language; loses information). INTERPRETATION: test safety behaviour per language rather than assuming English results carry over (the book reports one model refusing misinformation requests in English but not in Chinese). `[C02-003]`
4. **Check domain fit.** A general model does well where its training data is dense and poorly on specialised data that is rarely public (protein, medical imaging, similar). If the domain is niche, list it as a risk, plan domain evaluation, and consider whether a domain model exists or data must be curated. `[C02-004]`
5. **Use architecture and size as constraints, not scores.** Read parameters with sparsity: for a mixture-of-experts model cost and speed follow active parameters, not total (Mixtral 8x7B: 46.7B total, 12.9B active). Estimate inference memory as parameters times bytes per parameter (7B at 16 bits needs at least 14 GB). Newer generations can beat larger older ones. Architecture drives long-context cost: key and value vectors grow with sequence length, and prefill is parallel while decode is sequential. `[C02-005]` `[C02-006]`
6. **Read the post-training level.** Pre-trained models complete text; supervised finetuning on demonstration data teaches conversation; preference finetuning shapes what to say, and its demonstration and comparison data are costly and may carry labeler bias. INTERPRETATION: use this to judge whether a candidate is an instruction-following model or a base model that you would have to tune yourself. `[C02-008]` `[C02-009]`
7. **Shortlist with public information.** Build a private leaderboard: list benchmarks that match your required capabilities, prefer recent ones, check each one's reliability, and weight them by your priorities. Avoid plain averaging, which treats all benchmarks and difficulties as equal (HELM used mean win rate instead); correlated benchmarks exaggerate bias; leaderboards cover few benchmarks and cannot cover your task. Where a model has no public score, running it yourself costs money, so get approval and a spend cap first. Public benchmarks filter out bad models; they do not find the best one. When switching between APIs serving the same model, retest, since performance can differ slightly. `[C04-010]` `[C04-009]`
8. **Weigh comparative rankings carefully.** Arena-style rankings reflect broad human preference and are hard to game, so they add signal beyond benchmarks. But they use unstandardized prompts and voters, assume transitivity that may not hold, and say which model is better, not whether it is good enough or worth twice the cost (a 51% win rate does not convert into tickets resolved). Combine them with absolute metrics on your own task (INTERPRETATION). `[C03-019]` `[C03-020]`
9. **Run your own evaluation on the shortlist.** Use the evaluation set from `eval-plan.md`, balance quality, latency, cost and ease of use, and pick the model with the best performance for the money among those meeting every hard requirement. Treat public scores as possibly contaminated (the model may have trained on the benchmark). Detection heuristics: n-gram overlap (more accurate, needs the training data) and unusually low perplexity on the benchmark (cheaper, less accurate, needs model access); ask for the share of the benchmark found in training data and the score on clean samples where available. `[C04-008]` `[C04-010]`
10. **Plan monitoring and revisit triggers.** The loop is iterative; later evidence can overturn earlier steps (for example, open models fail your bar and you move to an API). The book's step 4 is continual production monitoring (feedback and failures). INTERPRETATION: record revisit triggers such as a provider price cut, a new model release, a license change or a failure-rate threshold. `[C04-008]` `[C04-009]`

## Evidence and exit gate

- Each hard requirement has a verdict per candidate with its source (policy, license text, provider documentation, or measurement).
- INTERPRETATION: at least two candidates were evaluated on your own data, or the gap is recorded as an assumption with a plan to close it.
- The decision record names the deciding criteria and the revisit trigger.
- No claim rests only on a public leaderboard or an arena rank.

## Outputs

[decision-record.md](../../templates/decision-record.md): one record for build versus buy, one for the model choice. Feed section 3 (Model(s)) of [architecture-design.md](../../templates/architecture-design.md) and the methods and data sections of [eval-plan.md](../../templates/eval-plan.md).

## Pitfalls

- Choosing by leaderboard rank, or by an average that weights unrelated benchmarks equally. `[C04-010]`
- Training-on-the-test-set effects hiding in a strong public score. `[C04-010]`
- Assuming English performance holds in other languages, and missing the token-cost multiplier. `[C02-003]`
- Reading total parameters of a sparse model as its cost. `[C02-006]`
- Building a model in-house because it looks cheaper, then finding providers halved prices; or tailoring infrastructure around a provider that fails. `[C04-009]`
- Treating an API model as frozen: providers update models, sometimes without notice, so prompts can silently stop working; build versioning and evaluation. `[C04-009]`
- Treating a pairwise win rate as absolute quality. `[C03-019]`
- Assuming the best overall model is best for your application, or that a provider's update only helps: behaviour shifted between versions on some tasks in the book's study. `[C04-010]`
- Taking a crowd-sourced ranking at face value: voters may favour fluent but wrong answers and prompts are unstandardized. `[C03-019]`
