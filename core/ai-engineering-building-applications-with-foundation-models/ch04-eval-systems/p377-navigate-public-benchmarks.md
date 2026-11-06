---
id: C04-010
title: Navigate Public Benchmarks
source_pages: "377-392"
chapter: 4
concepts: [public-benchmarks, evaluation-harness, leaderboard, benchmark-correlation, mean-win-rate, data-contamination, n-gram-overlap, custom-leaderboard]
related: [C04-008, C04-009, C04-011, C03-007]
time_sensitive: true
---
# Navigate Public Benchmarks
(Source: PDF pp. 377-392)

## What the section covers
How to use publicly available benchmark results to narrow a list of candidate models: the sheer number of benchmarks, evaluation harnesses, how public leaderboards choose and aggregate benchmarks (and where that falls short), how to build your own private leaderboard from public benchmarks, and the widespread problem of data contamination with ways to detect and handle it. The section closes by handing off to the custom evaluation pipeline.

## Context: after build versus buy
The opening lines of p. 377 are the tail of the build-versus-buy table covered in C04-009; the book then says that decision should already narrow the options and that the next refinement is to use public performance data (PDF p. 377).

## Meaning
- There are thousands of benchmarks, each probing different capabilities. Google's BIG-bench (2022) alone contains 214 benchmarks (PDF p. 377).
- The count keeps rising along with the number of AI use cases. Also, as models improve, older benchmarks saturate, so new ones must be introduced (PDF p. 377).
- An evaluation harness is a tool that runs a model across many benchmarks (PDF p. 378). At the time of writing, EleutherAI's lm-evaluation-harness supported more than 400 benchmarks, and OpenAI's evals could run roughly 500 existing benchmarks and let you register new ones for OpenAI models. These span math, puzzles, and even recognising ASCII art that depicts words (PDF p. 378).
- Aggregating benchmark results to rank models produces a leaderboard (PDF p. 378).

## Why it matters
Benchmark results help identify promising models for your use case (PDF p. 378). Two questions follow: which benchmarks go into the leaderboard, and how the results are combined to rank models. It is impossible to look at every benchmark. The book illustrates the tension: if model A beats B on a coding benchmark but loses on a toxicity benchmark, or wins one coding benchmark and loses another, which is chosen? (PDF p. 378).

## How public leaderboards work
Public leaderboards rank models by aggregated performance on a subset of benchmarks. They are very helpful but not comprehensive (PDF p. 379).

### Why they are incomplete
- Compute constraints: running a benchmark costs compute, so most leaderboards include few. HELM Lite omitted the information retrieval benchmark MS MARCO because it is expensive. Hugging Face skipped HumanEval because it needs many generated completions (PDF p. 379).
- Small sets: Hugging Face's Open LLM Leaderboard launched in 2023 with four benchmarks and grew to six by the end of that year. The book says so few benchmarks cannot represent the broad capabilities and failure modes of foundation models (PDF p. 379).
- Opaque selection: leaderboard builders are thoughtful, but users often cannot see how benchmarks were chosen, and different leaderboards end up with different benchmarks, making rankings hard to compare (PDF pp. 379-380).

### The Hugging Face leaderboard (late 2023)
Ranked models by the average of six benchmarks (PDF p. 380):
1. ARC-C: grade-school-level complex science questions.
2. MMLU: knowledge and reasoning in 57 subjects, such as elementary math, US history, computer science, and law.
3. HellaSwag: predicting how a sentence or scene in a story or video continues, testing common sense about everyday activities.
4. TruthfulQA: producing responses that are accurate, truthful, and not misleading, focused on factual understanding.
5. WinoGrande: hard pronoun-resolution problems that need commonsense reasoning.
6. GSM-8K: grade-school math problems (OpenAI, 2021).

### The HELM leaderboard (around the same time)
Stanford's HELM used ten benchmarks, only two (MMLU and GSM-8K) shared with Hugging Face. The other eight: competitive math (MATH); legal (LegalBench); medical (MedQA); translation (WMT 2014); two reading-comprehension benchmarks (NarrativeQA, OpenBookQA); and two general QA settings of Natural Questions, with and without Wikipedia pages in the input (PDF p. 381).

Hugging Face said it picked benchmarks that "test a variety of reasoning and general knowledge across a wide variety of fields" (PDF p. 381). HELM said its list was inspired by the simplicity of the Hugging Face one but with a wider set of scenarios (PDF p. 381).

### Coverage versus count
Leaderboards try to balance coverage against the number of benchmarks, usually picking a small set that spans reasoning, factual consistency, and domain skills like math and science (PDF p. 381). The book points out there is no clarity about what "coverage" means or why lists stop at six or ten. Why are medical and legal included in HELM Lite but not general science? Why two math tests but no coding? Why does neither have summarization, tool use, toxicity detection, or image search? (PDF pp. 381-382). These are not criticisms but illustrations that benchmark selection is hard; if leaderboard authors cannot explain it, that may be why (PDF p. 382).

### Benchmark correlation
An often overlooked aspect: if two benchmarks are perfectly correlated you do not need both, and strongly correlated benchmarks can exaggerate biases (PDF p. 382). Table 4-5 gives Pearson correlations among the six Hugging Face benchmarks, computed in January 2024 by Balázs Galambosi (PDF p. 383). Values visible on the rendered page (PDF p. 383): ARC-C vs HellaSwag 0.4812; ARC-C vs MMLU 0.8672; ARC-C vs TruthfulQA 0.4809; ARC-C vs WinoGrande 0.8856; ARC-C vs GSM-8K 0.7438; HellaSwag vs MMLU 0.6105; HellaSwag vs TruthfulQA 0.4228; HellaSwag vs WinoGrande 0.4842; HellaSwag vs GSM-8K 0.3547; MMLU vs TruthfulQA 0.5507; MMLU vs WinoGrande 0.9011; MMLU vs GSM-8K 0.7936. The table clips at the right edge in the PDF itself: the TruthfulQA column shows only truncated values (about 0.480, 0.480, 0.550, 1.000, 0.455, 0.500 for the ARC-C, HellaSwag, MMLU, TruthfulQA, WinoGrande, GSM-8K rows) and the WinoGrande and GSM-8K columns are not shown. UNVERIFIED: the clipped digits of the TruthfulQA column, and the WinoGrande vs GSM-8K value, which is not visible anywhere.
- WinoGrande, MMLU, and ARC-C are strongly correlated, sensible since all test reasoning (PDF p. 383).
- TruthfulQA is only moderately correlated with the others, suggesting that better reasoning and math do not always bring better truthfulness (PDF p. 383).

### Aggregation: averaging versus mean win rate
- Hugging Face averages scores across all benchmarks. That treats an 80% on TruthfulQA the same as an 80% on GSM-8K even though the former may be much harder, and it gives every benchmark equal weight even when truthfulness matters far more than grade-school math for a given task (PDF pp. 383-384).
- HELM avoided averaging and used mean win rate, defined as "the fraction of times a model obtains a better score than another model, averaged across scenarios" (PDF p. 384).

### Caveat on reading rankings
Understand which capabilities a leaderboard captures. A top-ranked model will likely, but far from always, do well for your application. If you need code generation and the leaderboard has no code benchmark, it helps less (PDF p. 384).

### Note: leaderboards changed quickly
In June 2024, under a year after the last revamp, Hugging Face replaced its benchmark set with harder, more practical ones. GSM-8K became MATH lvl 5 (the hardest questions of MATH), MMLU became MMLU-PRO, and GPQA (graduate-level Q&A), MuSR (chain-of-thought multistep reasoning), BBH (BIG-bench Hard, reasoning), and IFEval (instruction following) were added (PDF p. 382). The author expects these to saturate soon too, but older examples remain useful for learning how to evaluate and interpret benchmarks (PDF p. 382).

## When and how to apply: custom leaderboards from public benchmarks
- Evaluating models for a specific application means building a private leaderboard ranked by your own criteria (PDF p. 384).
- Step one: list benchmarks measuring capabilities your application needs. A coding agent calls for code benchmarks; a writing assistant calls for creative-writing benchmarks (PDF pp. 384-385).
- Look for the latest benchmarks, since new ones appear and old ones saturate (PDF p. 385).
- Check how reliable each benchmark is. Anyone can publish one, so many may not measure what you expect (PDF p. 385).
- Not every model has public scores on your chosen benchmark. Then you must run it yourself, ideally with an evaluation harness (PDF p. 387). This can be costly: Stanford spent roughly $80,000-$100,000 to evaluate 30 models on the full HELM suite, and cost grows with more models and benchmarks (PDF p. 387).
- Scores are on different scales (accuracy, F1, BLEU), so weigh each benchmark's importance to you when aggregating (PDF p. 387).
- The goal is only to shortlist a few models for more rigorous experiments with your own benchmarks and metrics, because public benchmarks rarely match your needs and are likely contaminated (PDF p. 388).

## Sidebar: are OpenAI's models getting worse?
People complain after each update that models seem worse. A Stanford and UC Berkeley study (Chen et al., 2023) found GPT-3.5 and GPT-4 changed significantly on many benchmarks between March 2023 and June 2023 (PDF p. 386). Figure 4-9 shows bar charts of such shifts. From the rendered page: on a code generation and formatting task (n=50, measured as directly executable output) GPT-4 went from 52.0% to 10.0% and GPT-3.5 from 22.0% to 2.0%; on the OpinionQA survey GPT-4's response rate went from 97.6% to 23.4% while GPT-3.5 went from 94.3% to 96.7%; on a LangChain HotpotQA agent GPT-4 exact match rose from 1.2% to 37.8% while GPT-3.5 fell from 22.8% to 14.0%; on answering sensitive questions GPT-4's response rate fell from 21.0% to 5.0% while GPT-3.5 rose from 2.0% to 8.0% (PDF p. 386, read from the figure). Assuming OpenAI does not deliberately ship worse models, one explanation is that evaluation is hard and nobody knows for sure whether a model is improving; the author doubts OpenAI is entirely blind. The other explanation is that the best model overall may not be best for your application, as changes help some uses and hurt others (PDF p. 387).

## Data contamination
### Meaning
Data contamination (also called data leakage, training on the test set, or cheating) occurs when a model was trained on the data it is evaluated on. It may simply memorize answers, scoring higher than it should. A model trained on MMLU can score high on MMLU without being useful (PDF p. 388). Rylan Schaeffer's satirical 2023 paper "Pretraining on the Test Set Is All You Need" showed this: a one-million-parameter model trained only on benchmark data got near-perfect scores and beat much larger models (PDF p. 388).

### How it happens
- Mostly unintentional: models trained on scraped internet data can pick up public benchmark data. Benchmark data published before training is likely in the training set. This is one reason benchmarks saturate so fast and developers keep creating new ones (PDF p. 389).
- Indirect: training and evaluation data from the same source, such as math textbooks used both for training and for building a benchmark (PDF p. 389).
- Intentional for good reasons: a developer first excludes benchmark data and picks the best model on it, then keeps training that model on the high-quality benchmark data before release. The released model is contaminated and users cannot evaluate it on those benchmarks, yet this may still be the right call (PDF pp. 389-390).

### Why it matters
It undermines trust in benchmarks. High bar-exam performance does not prove good legal advice; the model may have seen many bar questions (PDF p. 390).

### Detecting contamination
First detect, then decontaminate. Two heuristics (PDF p. 390):
- N-gram overlap: if, for instance, a sequence of 13 tokens in an evaluation sample also appears in the training data, the model has likely seen the sample, which is then called dirty.
- Perplexity: perplexity measures how hard a text is for a model to predict (see C03-007). Unusually low perplexity on evaluation data suggests the model may have seen it in training.

Trade-off: n-gram overlap is more accurate but slow and costly, since each benchmark example is compared with the whole training set, and it is impossible without access to the training data. Perplexity is less accurate but far cheaper (PDF p. 391).

### Handling it
- Older ML textbooks advised removing evaluation samples from training data to keep benchmarks standardized. With foundation models most people do not control training data. Even those who do may not want to drop all benchmark data since it can improve the model, and benchmarks created after training will always be contaminated (PDF p. 391).
- Common developer practice: remove the benchmarks you care about from training data before training (PDF p. 391).
- Ideal reporting: disclose the percentage of the benchmark found in training data and give performance on both the full benchmark and its clean samples. Because detection and removal take effort, many skip it (PDF p. 391).
- OpenAI's GPT-3 analysis found 13 benchmarks with at least 40% of their data in the training set (Brown et al., 2020). Figure 4-10 is a table showing, per benchmark, total, dirty and clean counts, clean percentage, and the relative difference between clean-only and whole-benchmark performance. Examples from the rendered table: Quac +20%, DROP -21%, SQuADv2 -2%, Winograd -3%, WSC +3%, and the rest within about 1% of zero; the share of each benchmark that is clean ranges from 1% (Quac) to 60% (WSC) (PDF p. 392).
- Leaderboard hosts such as Hugging Face plot standard deviations of model performance on a benchmark to spot outliers. Public benchmarks should keep part of their data private and offer a tool to automatically evaluate models on the private hold-out (PDF p. 392).

## Limitations and failure modes
- Leaderboards cover few benchmarks and have unexplained selection (PDF pp. 379-382).
- Correlated benchmarks inflate bias (PDF p. 382); simple averaging ignores difficulty and task importance (PDF pp. 383-384).
- Contamination makes public scores less trustworthy (PDF p. 390).
- Public benchmarks "will help you filter out bad models, but they won't help you find the best models" for your application (PDF p. 392). After narrowing, run your own evaluation pipeline (PDF p. 392).

## Relations
Follows model selection workflow (C04-008) and build versus buy (C04-009); leads to designing your own evaluation pipeline (C04-011). Perplexity as a contamination signal ties to C03-007.

## Time-sensitive statements
Leaderboard compositions (Hugging Face's six, then June 2024 replacement set; HELM's ten), harness benchmark counts (400+, about 500), the Stanford cost estimate, the March-June 2023 GPT behavior changes, and the Table 4-5 correlations from January 2024 are dated to the book's writing (PDF pp. 378, 380-383, 386-387).
