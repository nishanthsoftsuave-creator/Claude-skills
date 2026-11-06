---
id: C02-006
title: Model Size, Scaling Laws and Scaling Limits
source_pages: "151-168"
chapter: 2
concepts: [model-size, parameters, sparse-model, mixture-of-experts, training-tokens, flops, utilization, chinchilla-scaling-law, compute-optimal, scaling-extrapolation, scaling-bottlenecks, inverse-scaling]
related: [C02-007, C02-005, C03-007]
time_sensitive: true
---
# Model Size, Scaling Laws and Scaling Limits
(Source: PDF pp. 151-168)

## What the section covers
How a foundation model's scale is described and budgeted: parameter count (including sparse and mixture-of-experts models), dataset size measured in tokens, compute measured in FLOPs, a worked training-time and cost estimate, the inverse scaling findings, the Chinchilla compute-optimal scaling law, hyperparameter extrapolation, and the two bottlenecks the book sees for further scaling (training data and electricity). The section closes with a one-line hand-off from "architecture and scale" to post-training (PDF p. 169).

## Meaning
- **Number of parameters.** Usually appended to a model name, e.g. Llama-13B has 13 billion parameters (PDF p. 151). More parameters generally mean more capacity to learn and a better model within one family: the 13B version is likely to beat the 7B one (PDF p. 151).
- **Generation matters too.** Better understanding of training means newer models beat older ones of the same size; Llama 3-8B (2024) outperforms Llama 2-70B (2023) on MMLU (PDF p. 151).
- **Sparse model.** One with a large share of zero-valued parameters. A 7B model that is 90% sparse has only 700 million non-zero parameters. Sparsity makes storage and computation more efficient, so a large sparse model can need less compute than a small dense one (PDF p. 152).
- **Mixture-of-experts (MoE).** A popular sparse type (Shazeer et al., 2017): parameters are split into groups, each an expert, and only a subset of experts is active for each token (PDF p. 152).
- **Dataset size.** Counting training samples works for some models (Flamingo used datasets of 1.8 billion and 312 million image-text pairs) but is poor for language models, because a sample may be a sentence, a Wikipedia page, a conversation or a whole book. Tokens are a better measure (PDF p. 153). Tokens are imperfect, since tokenizers differ and the same data yields different token counts per model, but a token is the unit the model works on, so it shows how much the model can potentially learn; words or letters do not (PDF p. 153).
- **Training tokens versus dataset tokens.** The number of training tokens counts tokens actually trained on. One trillion tokens trained for two epochs (an epoch is one pass over the data) gives 2 trillion training tokens (PDF p. 154).
- **FLOP** is a floating point operation and a standardized unit of compute for a task, as opposed to counting machines (GPUs, CPUs, TPUs) whose capacities and costs differ, e.g. A10 versus H100 versus an Intel Core Ultra (PDF pp. 155-156). FLOPs (plural) is the compute a task needs; FLOP/s is floating point operations per second, a machine's peak performance (PDF p. 156).
- **Utilization.** The fraction of a machine's maximum compute capacity you actually use (PDF p. 157).

## How it works
### Memory from parameter count (PDF p. 151)
Parameter count lets you estimate resources. A 7B model with each parameter stored in 2 bytes (16 bits) needs at least 14 GB of GPU memory for inference (7 billion x 2 bytes = 14 billion bytes).

### MoE worked example: Mixtral 8x7B (PDF p. 152)
Eight experts of 7 billion parameters would naively be 8 x 7 = 56 billion if nothing were shared; because some parameters are shared the real count is 46.7 billion. At each layer, for each token, only two experts are active, so 12.9 billion parameters are active per token. Cost and speed therefore match a 12.9B model even though the model holds 46.7B parameters.

### Data size examples (PDF pp. 153-155)
- Datasets for LLMs are now in the trillions of tokens. Meta's Llama models used 1.4 trillion tokens (Llama 1), 2 trillion (Llama 2) and 15 trillion (Llama 3) (PDF pp. 153-154).
- Together's open dataset RedPajama-v2 has 30 trillion tokens, said to equal 450 million books or 5,400 times Wikipedia; but it is indiscriminate content, so high-quality data is much less (PDF p. 154).
- A 13B model trained only on the sentence "I like pineapples" would do much worse than a far smaller model trained on more data, showing that a bigger model can underperform if data is insufficient (PDF pp. 152-153).
- Table 2-5 (from the DeepMind Chinchilla paper) lists parameters versus training tokens: LaMDA 137B parameters / 168B tokens; GPT-3 175B / 300B; Jurassic 178B / 300B; Gopher 280B / 300B; MT-NLG 530B / 270B; Chinchilla 70B / 1.4T tokens (PDF p. 155).
- Quantity is not the only factor: quantity, quality and diversity are the "three golden goals" of training data, covered in Chapter 8 (PDF p. 155).

### Compute numbers and notation (PDF p. 156; exponents confirmed on the rendered page)
- Google's largest PaLM-2 was trained with 10^22 FLOPs; GPT-3-175B with 3.14 x 10^23 FLOPs. (The PaLM-2 figure is printed as just 10 with superscript 22.)
- An NVIDIA H100 NVL delivers at most 60 TeraFLOP/s = 6 x 10^13 FLOPs per second = 5.2 x 10^18 FLOPs per day.
- Warning on notation: FLOP/s is often written FLOPS, which looks like FLOPs. OpenAI and others use FLOP/s-day: 1 FLOP/s-day = 60 x 60 x 24 = 86,400 FLOPs. The book uses FLOPs for operation counts and FLOP/s for rate.

### Training time and cost for GPT-3-175B (PDF p. 157)
- Time at perfect use: with 256 H100s at maximum capacity and no mistakes, (3.14 x 10^23) / (256 x 5.2 x 10^18) is about 236 days, roughly 7.8 months.
- Utilization rules of thumb: 50% of advertised performance is "okay", above 70% is "great", and this should not stop you aiming higher; it depends on model, workload and hardware. Chapter 9 covers hardware metrics and utilization.
- Cost: at 70% utilization and $2 per H100-hour, training GPT-3-175B costs over $4 million. The formula is printed as $2/H100/hour x 256 H100 x 24 hours x 256 days / 0... and is cut off at the page edge in the PDF itself. UNVERIFIED: the divisor is presumably 0.7 for 70% utilization, but the printed line is truncated and the rendered page does not show it. INTERPRETATION: with 0.7, the arithmetic gives about $4.5 million, consistent with "over $4 million". The prose gives ~236 days for the full-capacity run (rendered page agrees), while the cost formula uses 256 days; this is as printed and the book does not explain the difference.

### Three numbers that signal scale (PDF p. 158)
Parameters are a proxy for learning capacity; training tokens are a proxy for how much was learned; FLOPs are a proxy for training cost.

### Inverse scaling (PDF p. 159)
- In 2022 Anthropic found that more alignment training can make models align less with human preference (Perez et al., 2022); the quoted examples include models more likely to express specific political and religious views, claim conscious experience and moral self-worth, and want not to be shut down.
- In 2023 mostly NYU researchers ran the Inverse Scaling Prize ($5,000 per third prize, $20,000 per second, $100,000 for one first). Of 99 submissions, 11 won third prizes. Larger models were sometimes (only sometimes) worse on tasks needing memorization and tasks with strong priors. No second or first prizes were awarded, because submitted tasks failed on small test sets but none showed real-world failures.

### The Chinchilla scaling law (PDF pp. 159-161)
- Rationale: performance depends on model and dataset size; both need compute; compute costs money. So start from a budget, not an arbitrary model size. Compute is often the limiting factor (expensive and hard to set up), so teams start with a compute budget: for a fixed FLOP budget, what model and dataset size perform best? The best such model is compute-optimal (PDF pp. 159-160).
- The Chinchilla paper (DeepMind, 2022) trained 400 language models of 70 million to over 16 billion parameters on 5 to 500 billion tokens. Finding: for compute-optimal training, training tokens should be about 20 times the model size, so a 3B model needs about 60B tokens. Model size and token count scale together: doubling model size means doubling tokens (PDF pp. 160-161).
- Figure 2-8 (rendered): three panel plots of training loss versus parameters for several FLOP budgets (one curve per FLOP budget from 6e18 to 3e21, each with a minimum), optimal parameters versus FLOPs, and optimal tokens versus FLOPs, each following a roughly straight line on log scales; the two right panels carry reference markers for one example budget (about 63B parameters and 1.4T tokens, as legible). The book frames this as how far the field has come from treating training like alchemy. Point made: the optimal parameters and tokens for a FLOP budget, and the expected loss, can be predicted (PDF p. 161).
- Assumption: the calculation presumes data is much cheaper than compute; the paper gives another calculation for when data cost is nontrivial (PDF p. 161).
- Scope: developed for dense models trained mostly on human-generated data; adapting it to sparse (MoE) models and synthetic data is active research (PDF p. 161).

## Why it matters
- Quality is not the only production criterion. Llama authors could have chosen bigger, better-performing models for their compute budget but chose smaller ones that are easier to work with and cheaper at inference, aiding adoption. Sardana et al. (2023) modified the Chinchilla law to find optimal parameter and data size while accounting for inference demand (PDF p. 162).
- Cost of a given performance is falling: on ImageNet, the cost to reach 93% accuracy halved from 2019 to 2021 (AI Index Report 2022) (PDF p. 162).
- Improvement stays expensive, a "last mile" effect like Chapter 1: 90 to 95% accuracy costs more than 85 to 90%. Per Meta's data-pruning paper, a 2% error rate model might need an order of magnitude more data, compute or energy than a 3% one (PDF p. 162).
- In language modeling, dropping cross-entropy loss from about 3.4 to 2.8 nats takes 10 times more training data (nats are covered in Chapter 3). For large vision models, going from 1 to 2 billion training samples adds only a few points of ImageNet accuracy (PDF p. 163).
- Yet small changes in loss or accuracy can mean big downstream quality differences; moving from loss 3.4 to 2.8 is noticeable (PDF p. 163).

## Scaling extrapolation (PDF pp. 163-165)
- Performance depends heavily on hyperparameters. With small models you train repeatedly with different settings and keep the best; for large models one training run is already draining, so often there is one shot at the right set (PDF pp. 163-164).
- Definitions: a parameter is learned during training; a hyperparameter is set by users. Configuration hyperparameters include number of layers, model dimension and vocabulary size; learning-control ones include batch size, epochs, learning rate and per-layer initial variance (PDF p. 164).
- Scaling extrapolation (also hyperparameter transferring) predicts good hyperparameters for a large model by studying their effect on much smaller models and extrapolating. A 2022 Microsoft and OpenAI paper transferred hyperparameters from a 40M model to a 6.7B model (PDF p. 164).
- Still niche: few people have the experience and resources, and it is hard. Ten hyperparameters mean 1,024 combinations, studied singly, in pairs, in triples and so on (PDF pp. 164-165).
- Emergent abilities (Wei et al., 2022), present only at scale and not seen in smaller models trained on less data, make extrapolation less accurate (PDF p. 165). The book points to Luke Metz's 2022 blog post on the difficulty of extrapolation.

## Scaling bottlenecks (PDF pp. 165-168)
- History: each order of magnitude in size has so far improved performance. GPT-2 (1.5B) has an order of magnitude more parameters than GPT-1 (117M); GPT-3 (175B) two more than GPT-2: three orders of magnitude from 2018 to 2021. Three more would mean 100-trillion-parameter models. Whether performance plateaus is unknown; two bottlenecks are visible (PDF p. 165).
- **Training data.** There is realistic concern of running out of internet data within a few years; dataset sizes grow much faster than new data is produced (Villalobos et al.). Figure 2-9 (rendered): effective stock of data (tokens; stock line roughly 2-7 x 10^14, uncertainty band about 6 x 10^13 to 10^15 and above, estimates) against a steeply rising projection of dataset sizes from 2020 with points such as GPT-3, PalM, FLAN, Falcon-180B, DBRX, Llama 3; the projection meets the stock around 2027-2028 (median full-use dates, with one earlier line for 5x overtraining) (PDF pp. 165-166).
- Anything you put online should be assumed to be or become training data, with or without consent, like being indexed by Google (PDF p. 166).
- Some people publish text hoping to steer future models; bad actors can use the same route for prompt injection (Chapter 5) (PDF pp. 166-167).
- Open question: how to make a model forget specific learned information, e.g. a deleted blog post it might still reproduce (PDF p. 167).
- AI-generated data is filling the internet. In December 2023 Grok refused a request citing OpenAI's use policy, prompting speculation it trained on ChatGPT output; developer Igor Babuschkin said the web is full of ChatGPT outputs. Researchers worry (Shumailov et al., 2023) that recursively training on AI data makes models forget original patterns and degrade; the book says the real impact is more nuanced and is covered in Chapter 8 (PDF p. 167).
- Once public data runs out, proprietary data (copyrighted books, translations, contracts, medical records, genome sequences) becomes the main source of more human data and a competitive advantage; OpenAI struck deals with Axel Springer and the Associated Press. Reddit and Stack Overflow changed data terms to block scraping. Longpre et al. (2024) found restrictions rendered over 28% of the most critical C4 sources fully restricted, and 45% of C4 is now restricted (PDF p. 168).
- **Electricity.** Less obvious but more pressing. Data centers use an estimated 1-2% of global electricity, projected 4-20% by 2030 (Patel, Nishball and Ontiveros, 2024). Absent new energy production, data centers can grow at most about 50 times, under two orders of magnitude, raising fears of power shortage and higher electricity cost (PDF p. 168).

## When and how to apply
- INTERPRETATION: when sizing or choosing models, read parameter count together with sparsity/MoE (active versus total parameters decide cost and speed), training tokens and FLOPs; and budget memory as parameters x bytes per parameter.
- Start from a compute budget and use the roughly 20 tokens per parameter rule, scaling tokens with size, as a compute-optimal starting point; adjust for inference demand if serving cost matters (PDF pp. 160-162).

## Limitations and failure modes
- Parameter count misleads for sparse models (PDF p. 152); bigger is not better if under-trained (PDF pp. 152-153); token counts differ across tokenizers (PDF p. 153).
- Chinchilla assumes cheap data, dense models and human-generated data (PDF p. 161).
- Extrapolation of hyperparameters is hard and hurt by emergent abilities (PDF p. 165).

## Relations
Leads into post-training (C02-007). Cross entropy and nats are in Chapter 3 (see C03-007 for perplexity). Training-data quality and AI-generated data are in Chapter 8; hardware utilization in Chapter 9; prompt injection in Chapter 5.

## Time-sensitive statements
Model examples and scores (Llama 3-8B vs Llama 2-70B on MMLU), token counts for Llama 1-3 and RedPajama-v2, FLOP figures for PaLM-2 and GPT-3, H100 throughput and the $2/hour price and $4 million cost, C4 restriction percentages, electricity share estimates, and the data-exhaustion projections all reflect the time of writing.
