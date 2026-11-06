---
name: data-review
mode: review-test
rows: [C08-003, C08-004, C08-005, C08-006, C08-013, C08-014, C08-015, C08-016, C03-016]
---
# Data review

## When to use
The project has datasets used for finetuning, for retrieval (the corpus behind an index), or for evaluation (test sets, golden sets). Route here from `routing.md` for "Review data quality" and alongside `retrieval-review.md` for RAG corpora. For an evaluation set, the same quality, coverage, duplication and contamination rules apply; leakage between it and training or prompt examples is the main extra concern.

## Inputs needed
- Dataset locations, formats and size; what each is used for (finetune, retrieval index, evaluation); who produced it and how (own application data, public data, purchased, annotated, synthetic). Discovery (`../discovery.md`) covers location; ask the rest (`../architect/intake.md`).
- The task the data serves and the user mix it should represent. Without them, relevance and coverage can only be `unverified`.
- Annotation guidelines, if annotators or an AI labeller produced the labels.
- Applicable policies (privacy, licences, copyright). If unknown, compliance checks are `BLOCKED` for want of the policy, not `PASSED`.
- For run checks: read access to a copy of the data (not production writes), permission to run scripts locally. Never copy rows containing personal data into evidence; store aggregates and redacted examples only.

## Modules to load
| Row | Module | Why it is needed here |
|---|---|---|
| C08-003 | [Data quality](../../core/ai-engineering-building-applications-with-foundation-models/ch08-datasets/p704-data-quality.md) | Six characteristics of good data |
| C08-004 | [Data coverage](../../core/ai-engineering-building-applications-with-foundation-models/ch08-datasets/p707-data-coverage.md) | Diversity relative to real usage; data mix |
| C08-005 | [Data quantity](../../core/ai-engineering-building-applications-with-foundation-models/ch08-datasets/p712-data-quantity.md) | How much, scaling experiments, diversity, budget |
| C08-006 | [Acquisition and annotation](../../core/ai-engineering-building-applications-with-foundation-models/ch08-datasets/p721-data-acquisition-and-annotation.md) | Sources, licences, guidelines |
| C08-013 | [Inspect data](../../core/ai-engineering-building-applications-with-foundation-models/ch08-datasets/p756-inspect-data.md) | Statistics, breakdowns, manual inspection |
| C08-014 | [Deduplicate data](../../core/ai-engineering-building-applications-with-foundation-models/ch08-datasets/p759-deduplicate-data.md) | Duplicate definition and methods, contamination |
| C08-015 | [Clean and filter data](../../core/ai-engineering-building-applications-with-foundation-models/ch08-datasets/p763-clean-and-filter-data.md) | Markup, policy violations, low quality, budget filtering |
| C08-016 | [Format data](../../core/ai-engineering-building-applications-with-foundation-models/ch08-datasets/p764-format-data.md) | Training format matching serving format |
| C03-016 | [Limitations of AI as a Judge](../../core/ai-engineering-building-applications-with-foundation-models/ch03-eval-methodology/p281-limitations-of-ai-as-a-judge.md) | The book's limits of AI judges (inconsistent scores, unstandardized criteria, cost, biases), relevant when an AI judge or AI labeller rates data. The skill's `probable` cap for judge-only findings is INTERPRETATION built on them |

## Procedure
Follow the book's processing order: inspect, deduplicate, clean and filter, format. Judge quality, coverage and quantity against the use. Record each answer with its evidence.

1. **Provenance and acquisition.** For each dataset, record source, licence, processing history and prior uses. The book's advice is to use available data but never trust it fully: inspect and validate it, check licences and try to trace origin, since a commercially licensed set can contain a non-commercial part. Application data is the most relevant source and may feed a flywheel; check privacy handling of user-generated data. Decision rule: unknown licence or origin is a `risk`, and a stated licence conflict is `probable` until the licence text is read. `[C08-006]`
2. **Annotation.** If labels were written by people or AI, check for written guidelines that say what a good response is, whether a correct answer can still be unhelpful, and what separates adjacent scores. Check that second-pass fact-checking exists where facts matter, and that annotation was not abandoned partway in the hope the model will work it out. Guidelines for training data and for evaluation data are the same kind of document. `[C08-006]`
3. **Quality, six characteristics.** Per dataset: relevant to the task; aligned with task requirements (not merely accurate); consistent across examples and annotators; correctly formatted (no stray markup, whitespace, casing or numeric-format noise); sufficiently unique; compliant with policy. The book reports a small curated set beating a large noisy one (examples are time-sensitive), so do not argue for more data before these pass. "Sufficiently" unique means some use cases tolerate more duplication than others; judge against the use. `[C08-003]`
4. **Inspection.** Plot token, input-length and response-length distributions; topic and language distributions and their relevance; breakdowns by source, time and annotator. Look for outlier annotators (very short answers, score skew), check score distributions per annotator when scores should be normal, compute inter-annotator disagreement and read the conflicting examples. Then read examples by hand: annotate a few queries yourself and compare, fact-check responses, check for shared query with different responses and the reverse. The book reports that about 15 minutes of looking usually pays off. Creative statistics are welcome (the book compares verb-noun pair and length distributions between sources). Do this before cleaning so findings inform filters. `[C08-013]`
5. **Coverage.** Compare the dataset's distribution (topics, formats, lengths, languages, styles, typos) to real or expected usage. Rule: a mix should reflect real usage, or be chosen by experiment (small models predicting large-model performance per mix is the book's example). More heterogeneous data does not always help. Missing an expected user pattern is a coverage gap; list the patterns the data lacks. Book figures such as Llama 3's mix are time-sensitive examples, not targets. `[C08-004]`
6. **Quantity.** There is no single number. Factors: finetuning technique (few hundred or thousand examples suit PEFT; tens of thousands to millions suit full finetuning), task difficulty, and base-model strength. Test small first: about 50 carefully crafted examples should usually show visible gains (the book says 50-100); if no gain, check learning rate, data quality and prompts before concluding anything. To estimate returns, train on 25%, 50%, 100% subsets and read the curve (steep slope: more data helps; plateau: little gain). Diminishing returns apply to same-kind data; task diversity keeps helping longer. Larger base models need fewer finetuning examples, and with abundant data full finetuning of a small pre-trained model can underperform (ossification). Annotation budget caps the target. These experiments need the user's training pipeline and spend approval; otherwise report the dataset size against the guidance and mark the effect `unverified`. `[C08-005]`
7. **Deduplication.** Fix the definition first: level (document, paragraph, sentence, token), exact versus approximate overlap, order sensitivity. Check all three forms (whole, within-document, across-document). Duplicates skew the distribution, can bias the model and waste compute. Deduplicate before splitting into train and test, otherwise twins land on both sides (contamination); INTERPRETATION: for an evaluation set also check overlap with training data and with few-shot examples. Method by scale: pairwise comparison, hashing in buckets, or dimensionality reduction then comparison. `[C08-014]`
8. **Cleaning and filtering.** Check for leftover markup, and for policy-violating content (PII, sensitive, copyrighted, toxic) and fields that should not be used. Check low-quality filtering rules and whether they came from inspection. Be aware that annotation quality can drop late in a session (fatigue). If data exceeds budget, filtering by example importance (active learning, importance sampling) depends on having a scoring method; ask what it is. Treat PII as a hard safety concern: report location and count only. `[C08-015]`
9. **Formatting.** Confirm data match the model's tokenizer and chat template; for supervised finetuning, instruction-response pairs; finetuning instructions usually drop task descriptions and few-shot examples once enough examples exist. Training and serving prompts must match exactly: extra spaces, prefixes or missing end markers can cause problems. INTERPRETATION: generating both from one template function removes drift. `[C08-016]`
10. **Compare with retrieval use.** For a retrieval corpus, the same checks apply with chunk-level duplication and markup residue taking priority; coordinate with `retrieval-review.md`. `[C08-013]` `[C08-014]`

## Checks
Run commands as `python scripts/run_check.py --case <ID> --evidence-dir <run>/evidence -- <command>`. Commands are the project's scripts or small scripts the user approves, run on a data copy.

| check | what is checked | how | evidence produced | type | criterion | how a failure is judged |
|---|---|---|---|---|---|---|
| DR-01 | Provenance and licence recorded per dataset | Read data docs, manifests, licence files | `DR-01-notes.md` | review | C08-006 | Unknown origin or conflicting licence: `risk`; a read licence that forbids the use: `probable` (legal confirmation is the user's) |
| DR-02 | Annotation guidelines exist and cover quality rules | Read guidelines; compare to samples | `DR-02-notes.md` | review | C08-006 | No guideline with human or AI labels in use: `probable` consistency risk |
| DR-03 | Quality characteristics: relevance, alignment, formatting noise | Manual sample (record sample size and method) plus script for formatting residue | `DR-03.exec.json`, `DR-03-notes.md` | run | C08-003 | Examples violating a characteristic are listed with ids; rate reported with the sample size. No book threshold |
| DR-04 | Consistency across annotators | Script computing inter-annotator disagreement and per-annotator distributions | `DR-04.exec.json`, disagreement table | run | C08-013, C08-003 | High disagreement or an outlier annotator: `probable` quality issue; skipped (`SKIPPED`) if single annotator or no annotator field |
| DR-05 | Distributions: tokens, input and output length, topics, languages | Script producing statistics, broken down by source and time | `DR-05.exec.json`, summary tables | run | C08-013 | Anomalies need a concrete example; otherwise `unverified` |
| DR-06 | Manual inspection and fact-check of a sample | Reviewer reads a sample; self-annotates a few items against given labels | `DR-06-notes.md` (ids, no personal data) | review | C08-013 | Wrong or unhelpful labels found: `probable`; found in more than isolated cases: `confirmed` with ids |
| DR-07 | Coverage against expected usage | Compare distribution (DR-05) to usage logs or stated user patterns | `DR-07-notes.md` | review | C08-004 | Expected pattern absent from data: `recommendation` (gap); `unverified` if usage unknown |
| DR-08 | Quantity versus technique and task | Compare size to finetuning method and difficulty | `DR-08-notes.md` | review | C08-005 | Size far outside the guidance for the technique with no experiment: `recommendation` |
| DR-09 | Scaling experiment (25/50/100%) or small-first run | User's training pipeline on subsets (needs approval and spend cap) | `DR-09.exec.json`, performance-vs-size table | run | C08-005 | Plateau or no gain is reported with hyperparameters; no gain on small data is not a verdict until data, learning rate and prompt are checked |
| DR-10 | Duplicates under the chosen definition | Script using exact, n-gram or hashed comparison; report cluster counts | `DR-10.exec.json`, cluster ids | run | C08-014 | Duplicates present: `confirmed` with count and examples, weighed against what the use tolerates; effect on performance is `unverified` unless measured |
| DR-11 | Train/test and few-shot overlap (contamination) | Compare evaluation items to training items and prompt examples with the DR-10 method | `DR-11.exec.json` | run | C08-014 | Any train/test overlap: `confirmed` contamination of that evaluation; few-shot-example overlap is INTERPRETATION (same method, same finding); results are untrustworthy until fixed |
| DR-12 | Markup residue and extraneous formatting tokens | Script counting HTML, Markdown or boilerplate patterns | `DR-12.exec.json` | run | C08-015 | Residue present where not wanted: `confirmed` with counts |
| DR-13 | Policy-violating content (PII, sensitive, copyrighted, toxic) | Approved detector or pattern script on a copy; report counts and fields only | `DR-13.exec.json` (counts, no raw values) | run | C08-015 | Hits in data barred by policy: `confirmed` and major; detector limits are stated, absence of hits is not proof (`PASSED` means the script ran clean, no more) |
| DR-14 | Filtering logic and budget fit | Read filter code and rationale | `DR-14-notes.md` | review | C08-015 | Filters unrelated to inspection findings, or example scoring undefined: `recommendation` |
| DR-15 | Training-format and serving-prompt match | Read both templates; run both builders on the same item and diff the strings | `DR-15.exec.json`, diff | run | C08-016 | Any whitespace, prefix or marker difference: `confirmed` |
| DR-16 | Chat template and tokenizer match the target model | Review preprocessing code against model documentation | `DR-16-notes.md` | review | C08-016 | Unverified template: `risk`; documented mismatch: `probable` |

## Evidence and exit gate
- Run checks have exec records; sample sizes and sampling method are written down; no raw personal data in evidence.
- Statements about performance impact are made only where an experiment measured it (DR-09); otherwise the effect is `unverified`.
- A finding from an AI judge's reading of data quality is capped at `probable` (`[C03-016]`).
- Exit gate: every check has a status with reason, and `python scripts/validate_report.py <run_dir>` prints 0 problems.

## Outputs
Results data and findings report (`../../templates/findings-report.md`). Per dataset, a short table of the six quality characteristics with status and evidence ids.

## Pitfalls
- Chasing quantity before quality. `[C08-003]`
- Trusting a public dataset's licence or provenance. `[C08-006]`
- Deduplicating after splitting. `[C08-014]`
- Skipping manual reading because statistics look fine. `[C08-013]`
- Declaring finetuning useless after a small run with poor hyperparameters. `[C08-005]`
- Training format that drifts from serving prompts. `[C08-016]`
- Using the book's dataset counts and model mixes as current norms; they are time-sensitive. `[C08-004]` `[C08-006]`
