---
id: C07-013
title: Parameter-Efficient Finetuning
source_pages: "639-663"
chapter: 7
concepts: [parameter-efficient-finetuning, peft, full-finetuning, partial-finetuning, adapters, soft-prompts, lora, low-rank-factorization, qlora, multi-lora-serving]
related: [C07-010, C07-011, C07-012, C07-014]
time_sensitive: true
---
# Parameter-Efficient Finetuning
(Source: PDF pp. 639-663; the lead-in text above the "Parameter-Efficient Finetuning" heading on PDF p. 639 belongs to C07-012)

## What the section covers
Why full finetuning is too costly for most people, how partial finetuning falls short, and how parameter-efficient finetuning (PEFT) fixes this. It surveys the two PEFT families (adapter-based and soft-prompt-based), then goes deep on LoRA: the mechanics and formulas, why low-rank adaptation works, how to configure it (which matrices, which rank, which alpha), how to serve LoRA models, and its quantized variant QLoRA.

## Meaning
- Full finetuning: early models were small enough to finetune entirely; the number of trainable parameters equals the total number of parameters. It resembles training, except that training starts from random weights while finetuning starts from previously trained weights (PDF pp. 639-640).
- Partial finetuning: only some parameters are updated, e.g. freezing the first nine of ten layers and training the last, leaving 10% of the parameters trainable (PDF p. 641).
- Parameter-efficient finetuning: methods that get performance close to full finetuning with far fewer trainable parameters. There is no formal threshold; generally a method counts as parameter-efficient if it approaches full-finetuning quality with several orders of magnitude fewer trainable parameters (PDF p. 642).
- Adapter-based (additive) methods add modules to the model's weights. Soft prompt-based methods add special trainable tokens that alter how the model processes input (PDF pp. 645-646).

## Why it matters
- Full finetuning is memory-hungry. Worked example for a 7B model: weights in 16-bit (FP16) take 14 GB; full finetuning with the Adam optimizer, also 16-bit, needs an extra 7B x 3 x 2 bytes = 42 GB (gradients plus optimizer states); total 14 + 42 = 56 GB. That exceeds typical consumer GPUs (12-24 GB, top-end up to 48 GB), and the figure still excludes activation memory (PDF p. 640).
- Full finetuning, especially supervised and preference finetuning, also usually needs a lot of high-quality annotated data that most people cannot afford (PDF p. 641).
- PEFT lets finetuning run on cheaper hardware, so many more developers can do it. PEFT methods are usually sample-efficient too: full finetuning may need tens of thousands to millions of examples for notable gains, while some PEFT methods perform strongly with a few thousand (PDF p. 644).
- Note on hardware: to fit a model, either shrink its footprint (quantization, PEFT) or use hardware memory better, e.g. CPU offloading of excess memory, as shown by DeepSpeed (Rasley et al., 2020) (PDF p. 640).

## How it works

### Why partial finetuning is not enough
It reduces memory but is parameter-inefficient. Houlsby et al. (2019) found that for BERT large you must update roughly 25% of parameters to match full finetuning on the GLUE benchmark (PDF p. 641). Figure 7-7 (PDF p. 642) plots accuracy delta (%, relative to full finetuning, y-axis from -25 to 5) against the number of trainable parameters per task (log scale, 10^5 to 10^9). The "fine-tune top layers" curve (blue) sits far below zero with few parameters (about -9.5 near 10^6, about -8 near 10^7 and -5 near 3x10^7, with a wide uncertainty band) and only reaches about zero near 10^8 parameters and above. The "adapters" curve (orange) stays within about 1 point of zero across the whole range from roughly 3x10^5 to 5x10^7 parameters. These numbers are estimates read from the chart.

### The original adapter method (Houlsby et al., 2019)
- The idea of PEFT is credited to this paper: insert extra parameters in the right places and train only those (PDF p. 643).
- They inserted two adapter modules into every transformer block of BERT (PDF p. 643). Figure 7-8 (PDF p. 643) zooms in: in each transformer layer an adapter sits after the multi-headed attention plus feedforward block and another after the two-feedforward block, each followed by a residual addition and layer norm. An adapter is a feedforward down-projection to a narrow representation, a nonlinearity, then a feedforward up-projection back to full width, with a skip connection around it.
- The original parameters stay frozen; trainable parameters are those in the adapters. On GLUE they came within 0.4% of full finetuning using 3% of the trainable parameters; the orange line in Figure 7-7 shows the delta for different adapter sizes (PDF p. 644).
- Downside: the extra layers add computation to the forward pass and increase inference latency of the finetuned model (PDF p. 644).

### PEFT technique families (PDF pp. 645-648)
- The book says the field falls into two buckets, adapter-based and soft prompt-based, and that new buckets may appear (PDF p. 645).
- Adapter-based (also "additive") methods: LoRA (Hu et al., 2021) is by far the most popular at the time of writing. BitFit (Zaken et al., 2021) appeared around the same time. IA3 (Liu et al., 2022) has an efficient mixed-task batching strategy that suits multi-task finetuning and is reported to beat LoRA, even full finetuning, in some cases. LongLoRA (Chen et al., 2023) is a LoRA variant that adds attention modifications to extend context length (PDF p. 645).
- Soft prompt-based methods insert special trainable tokens fed in alongside the input tokens (PDF p. 645). They are "soft" prompts versus ordinary "hard" prompts. Two differences: hard prompts are human-readable discrete tokens, while soft prompts are continuous embedding-like vectors that are not readable; hard prompts are static and untrainable, while soft prompts are optimized by backpropagation for a task (PDF p. 646). Some call soft prompting a crossover between prompt engineering and finetuning (PDF p. 646).
- Figure 7-9 (PDF p. 647) shows a hard prompt ("Summarize the book XYZ") passing through the embedding weights, a soft prompt (blocks of numeric vectors) joined to the embedded tokens, and the combination entering the rest of the model's weights to produce output: the two kinds of prompt can be combined.
- Named soft-prompt techniques: prefix-tuning (Li and Liang, 2021), P-Tuning (Liu et al., 2021) and prompt tuning (Lester et al., 2021). They differ mainly in where soft prompts go: prefix tuning prepends soft tokens at every transformer layer; prompt tuning prepends them only to the embedded input. Many PEFT frameworks implement them out of the box (PDF p. 647).
- Popularity analysis: in October 2024 the author examined over 1,000 open issues in the huggingface/peft GitHub repository, assuming users of a technique are likelier to report issues about it ("P-Tuning" searched via "p_tuning" and "p tuning") (PDF pp. 647-648). Figure 7-10 (PDF p. 648) is a bar chart; LoRA has roughly 700 issues, QLoRA roughly 65, prompt tuning about 30, P-Tuning about 28 and prefix-tuning about 20 (estimates from the chart). Conclusion: LoRA dominates; soft prompts are less common but interest is growing among people wanting more customization than prompt engineering without committing to finetuning (PDF p. 648).

### LoRA (Low-Rank Adaptation)
- The book frames the LoRA deep dive as one that solves the problem of early adapter methods (inference latency) and, even for readers who never use LoRA, as a framework for exploring other finetuning methods (PDF pp. 648-649).
- Unlike the original adapters, LoRA adds parameters without extra inference latency: its modules can be merged back into the original layers instead of adding layers (PDF p. 649).
- It is applied to individual weight matrices: decompose into the product of two smaller matrices, update those, and merge back (PDF p. 649).
- Procedure for a weight matrix W of dimension n x m (PDF pp. 649-650):
  1. Choose r, the LoRA rank. Build A (n x r) and B (r x m). Their product W_AB = A x B has the same dimension as W (n x m).
  2. Add W_AB to W to form W': W' = W + (alpha / r) * W_AB, where alpha is a hyperparameter controlling how much W_AB contributes. W' replaces W in the model. (As printed on PDF p. 650 the left side renders as a garbled "W" followed by "a" with a circumflex, and the right side as W + (alpha/r) W_AB; the same formula on p. 657 prints it likewise.) INTERPRETATION: the garbled left side is read as the new matrix W' that the prose of step 2 describes ("the new matrix"), not as a separate symbol. Symbols: W = original n x m weight matrix; A, B = the two low-rank factors; r = rank; alpha = contribution-scaling hyperparameter; W_AB = the product of A and B (n x m).
  3. During finetuning, update only A and B; W stays intact.
- Figure 7-11 (PDF p. 650): the previous layer feeds W' (R^(n x m)), which feeds the next layer. W' is the sum of W (R^(n x m)) and W_AB (dashed, R^(n x m)). W_AB is the product of A (R^(n x r)) and B (R^(r x m)); both "r" dimensions are labelled "r-rank".
- Background note on low-rank factorization (PDF p. 651): a long-standing dimensionality-reduction idea; factor a big matrix into two smaller ones to cut parameters, computation and memory. Example: a 9 x 9 matrix (81 parameters) can be the product of 9 x 1 and 1 x 9 matrices (18 parameters total). The book states the number of columns of the first factor and of the second factor corresponds to the rank (as printed; the usual statement would be columns of the first and rows of the second). The original matrix is full-rank; the small ones form a low-rank approximation. Factorization is lossy, and a higher rank preserves more of the original information.
- Like adapters, LoRA is parameter- and sample-efficient. For GPT-3, the LoRA paper reported comparable or better performance than full finetuning on several tasks using about 4.7M trainable parameters, 0.0027% of full finetuning (PDF p. 651).

### Why LoRA works (PDF pp. 651-654)
- The puzzle: if learning behaviors in pre-training takes many parameters and (millions to billions of) examples, why do finetuning changes need few parameters and only hundreds or thousands of examples? (PDF pp. 651-652)
- Answer offered: many papers (Li et al., 2018; Aghajanyan et al., 2020; Hu et al., 2021) argue LLMs, despite their size, have very low intrinsic dimension. Pre-training implicitly minimizes it, and larger models tend to have lower intrinsic dimension after pre-training. So pre-training acts as a compression framework for downstream tasks: the better trained the model, the easier to finetune with few parameters and little data (PDF p. 652).
- Why not low-rank pre-training too? It would cut pre-training time and cost (PDF p. 652). In the 2010s many tried low-rank networks (Sainath et al., 2013; Povey et al., 2018; Jaderberg et al., 2014) (PDF p. 653). It works at smaller scale: SqueezeNet (Iandola et al., 2016), using strategies like replacing 3x3 convolutions with 1x1, matched AlexNet-level ImageNet accuracy with 50 times fewer parameters (PDF p. 653). Recent LLM attempts: ReLoRA (up to 1.3B parameters) and GaLore (comparable to full-rank at 1B, promising at 7B) (PDF p. 653).
- The author speculates low-rank pre-training may scale some day, but if Aghajanyan et al. are right that pre-training compresses intrinsic dimension, full-rank pre-training is still needed first to bring the dimension low enough for low-rank methods; how much full-rank training is needed is an open question (PDF pp. 653-654).

### LoRA configurations (PDF pp. 654-657)
- Decisions: which weight matrices get LoRA and what rank each gets. Efficiency depends on both the chosen matrices and the model architecture (PDF p. 654).
- LoRA has been used mostly with transformers (some CNN examples exist: Dutt et al., 2023; Zhong et al., 2024; Aleem et al., 2024). Most commonly it targets the four attention weight matrices: query (W_q), key (W_k), value (W_v) and output projection (W_o), applied uniformly to all matrices of a type across the model (PDF p. 654).
- With a fixed budget of trainable parameters you must choose. Hu et al. (2021) set an 18M budget for GPT-3 175B (0.01% of parameters), which allows: one matrix at rank 8; two matrices at rank 4; or all four matrices at rank 2 (PDF p. 655).
- Arithmetic check from the book: GPT-3 175B has 96 layers and model dimension 12,288. Rank 2 on four matrices gives (12,288 x 2 x 2) x 4 = 196,608 parameters per layer, 18,874,368 for the whole model (PDF p. 655).
- Result: all four matrices at rank 2 gave the best results on WikiSQL and MultiNLI; if only two attention matrices can be chosen, query and value generally work best (PDF p. 655).
- Table 7-5 (PDF p. 656) is clipped at the right edge. Legible part (budget 18M; rank 8 for all four single-matrix cases): WikiSQL (+/-0.5%) is 70.4 for W_q, 70.0 for W_k, 73.0 for W_v, 73.2 for W_o; MultiNLI (+/-0.1%) is 91.0, 90.8, 91.0, 91.3 respectively. UNVERIFIED: the remaining columns (such as combined-matrix settings at rank 4 and rank 2) and the end of the caption are cut off in the PDF, so the table cannot confirm the text's claim about rank 2 on all four matrices. Note also that in the visible columns the single W_o column scores highest.
- Empirically, applying LoRA to more matrices, including feedforward ones, helps. Databricks found the biggest boost from LoRA on all feedforward layers (Sooriyarachchi, 2023). Fomenko et al. (2024): feedforward LoRA complements attention LoRA, though attention LoRA usually gives more efficacy under memory constraints (PDF p. 656).
- Rank: performance depends on rank, but a small r (4 to 64) usually suffices; smaller r means fewer parameters and less memory (PDF p. 656).
- The LoRA authors were surprised that raising r did not improve finetuning performance; Databricks reported similarly that raising r beyond a point may give no discernible quality gain. Some argue higher r can hurt through overfitting. But sometimes high rank is needed: Raschka (2023) found r = 256 best on his tasks (PDF p. 657).
- Alpha: the hyperparameter in W' = W + (alpha / r) * W_AB. In the author's experience alpha is often chosen so alpha:r is between 1:8 and 8:1, with the optimum varying: smaller r may call for larger alpha, larger r for smaller alpha. Experiment to find the best (r, alpha) pair (PDF p. 657).

### Serving LoRA adapters (PDF pp. 657-660)
LoRA's modularity also simplifies serving many models (PDF p. 657). Two ways to serve:
1. Merge A and B into the base weight ahead of time to make W'. No extra computation at inference, so no added latency (PDF p. 658).
2. Keep W, A and B separate; merging happens at inference, adding latency (PDF p. 658).
Option 1 is generally better with a single LoRA model; option 2 is generally better for multi-LoRA serving, several LoRA models sharing one base model (PDF p. 658). Figure 7-12 (PDF p. 658) shows one shared W branching to separate adapter pairs (A1, B1) and (A2, B2).
- Storage example (PDF p. 659): finetune one model per customer for 100 customers. Take W as 4096 x 4096 (16.8M parameters) and LoRA rank 8, so A and B hold 4096 x 8 x 2 = 65,536 parameters. Option 1 stores 100 full matrices: 16.8M x 100 = 1.68B parameters. Option 2 stores one W plus 100 (A, B) sets: 16.8M + 65,536 x 100 = 23.3M parameters.
- Option 2 also switches tasks faster: moving from customer X to Y means loading only Y's adapter rather than a whole weight matrix. Optimization techniques can reduce the extra latency of keeping adapters separate; the book's GitHub repository has a walkthrough (PDF p. 659).
- Multi-LoRA makes it easy to combine specialized models: one adapter per task instead of one big model. Apple used multiple LoRA adapters on a single 3B-parameter base model for different iPhone features (2024), with quantization shrinking base and adapters so all could be served on-device (PDF p. 660).
- Adapters can be shared and reused, like pre-trained models, e.g. on Hugging Face or AdapterHub (PDF p. 660).

### The catch with LoRA (PDF p. 660)
It does not match full finetuning in performance. It is also harder to implement than full finetuning because it requires modifying the model implementation, which needs knowledge of the architecture and coding skill; the book says this is usually a problem only for less popular base models, since PEFT frameworks (Hugging Face PEFT, Axolotl, unsloth, LitGPT) likely support LoRA for popular models out of the box.

### Quantized LoRA and QLoRA (PDF pp. 661-663)
- Many LoRA variants try to cut trainable parameters further, but LoRA adapter memory is already tiny next to the weights, so this saves little overall (PDF p. 661).
- Table 7-6 (PDF p. 661; r = 2 on query and key matrices as printed; 16-bit): Llama 2 (13B): weights 26 GB, LoRA trainable params 3.28M, adapter memory 6.55 MB. GPT-3 (175B): weights 350 GB, 18.87M params, 37.7 MB. Note the header says query and key matrices, whereas the p. 655 note derives the identical 18,874,368 figure for rank 2 on all four attention matrices; the two statements differ and are recorded as printed. The takeaway is unchanged: adapter memory is a tiny fraction of the weights.
- A more effective saving is quantizing weights, activations and/or gradients during finetuning. QLoRA (Dettmers et al., 2023) was an early promising version. Original LoRA stores weights in 16 bits; QLoRA stores them in 4 bits and dequantizes to BF16 for the forward and backward passes (PDF pp. 661-662).
- QLoRA's 4-bit format is NF4 (NormalFloat-4), which quantizes based on the observation that pre-trained weights roughly follow a normal distribution centered on zero. It also uses paged optimizers that move data automatically between CPU and GPU when GPU memory runs out, notably with long sequences. Together these let a 65B model be finetuned on a single 48 GB GPU (PDF p. 662).
- The authors finetuned several models, including Llama 7B to 65B, in 4-bit; the family is called Guanaco, with competitive benchmark and comparative-evaluation results. Table 7-7 (PDF p. 663) gives Elo ratings from GPT-4 as judge, May 2023: GPT-4 1348; Guanaco 65B (41 GB) 1022; Guanaco 33B (21 GB) 992; Vicuna 13B (26 GB) 974; ChatGPT 966; Guanaco 13B (10 GB) 916; Bard 902; Guanaco 7B (6 GB) 879 (each with +/-1). Guanaco 65B did not beat GPT-4 but was often preferred to ChatGPT (PDF pp. 662-663).
- Main limitation: NF4 quantization is expensive; QLoRA saves memory but may lengthen training because of quantization and dequantization steps. Other quantized-LoRA works: QA-LoRA, ModuLoRA and IR-QLoRA (PDF p. 663).

## When and how to apply
- INTERPRETATION: Use PEFT when full finetuning's memory or data demands are out of reach. Treat LoRA as the default family to try first, because the book reports it as the most widely used method; merge adapters for single-model serving and keep them separate for many task-specific or per-customer models on a shared base. The book does not issue this as advice.
- INTERPRETATION: Tune rank in the 4-64 range first, apply LoRA broadly (attention plus feedforward) if memory allows, and experiment with (r, alpha). Consider QLoRA when GPU memory is the binding constraint and extra training time is acceptable.
- INTERPRETATION: because the book reports mixed evidence on rank (diminishing returns versus r = 256 helping), treat rank as an empirical setting to validate on your own task rather than a fixed rule.

## Alternatives and trade-offs
- INTERPRETATION (summary of the book's comparisons; the book says only that LoRA does not match full finetuning): Full finetuning: best quality, highest memory and data cost. Partial finetuning: lower memory but needs many trainable parameters. Adapters: efficient but add inference latency. LoRA: no added latency when merged, modular and shareable, weaker than full finetuning and more involved to implement. Soft prompts: lighter touch between prompt engineering and finetuning, less common. QLoRA: more memory savings, slower training.

## Limitations and failure modes
Latency of original adapters; LoRA's performance ceiling versus full finetuning; extra latency when LoRA adapters are kept separate; QLoRA training-time cost; the clipped Table 7-5 limits verification of some numbers.

## Relations
Builds on the memory math and quantization (C07-010, C07-011) and the section lead-in (C07-012). Model merging, introduced as the complementary technique, follows in C07-014.

## Time-sensitive statements
LoRA's status as "by far the most popular", the October 2024 GitHub issue counts, the May 2023 Elo ratings, Apple's 2024 on-device use, and the named frameworks and low-rank pre-training results (ReLoRA, GaLore) reflect the date of writing.
