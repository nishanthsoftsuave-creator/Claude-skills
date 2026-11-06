---
name: finetune-plan
mode: architect
rows: [C07-013, C07-014, C07-015, C08-003, C08-004, C08-005, C08-006, C08-016]
---
# Finetuning plan

## When to use
Run only after `finetune-decision.md` returned "finetune" and its memory feasibility check passed. This workflow chooses the method, data plan, hyperparameter starting points and run sequence. For synthetic data and distillation detail, also use `data-and-retrieval.md`.

## Inputs needed
From the decision record and `intake.md`; ask only what is missing:
- The behavior gap to close and the evaluation that measures it (baseline numbers).
- Base model candidates, licence, hardware memory (from the feasibility table), whether to use a finetuning API or own infrastructure.
- Data on hand: volume, quality, licence, sensitivity; annotation budget.
- How many task-specific models are needed and how they will be served; other tasks that must not regress.

## Modules to load
| Row | Module | Why it is needed here |
|---|---|---|
| C07-013 | [Parameter-Efficient Finetuning](../../core/ai-engineering-building-applications-with-foundation-models/ch07-finetuning/p639-parameter-efficient-finetuning.md) | Full vs partial vs PEFT, LoRA configuration, serving, QLoRA |
| C07-014 | [Model Merging and Multi-Task Finetuning](../../core/ai-engineering-building-applications-with-foundation-models/ch07-finetuning/p664-model-merging-and-multi-task-finetuning.md) | Multi-task strategies, merging approaches |
| C07-015 | [Finetuning Tactics](../../core/ai-engineering-building-applications-with-foundation-models/ch07-finetuning/p680-finetuning-tactics.md) | Base model path, framework, hyperparameters |
| C08-003 | [Data Quality](../../core/ai-engineering-building-applications-with-foundation-models/ch08-datasets/p704-data-quality.md) | Six quality characteristics |
| C08-004 | [Data Coverage](../../core/ai-engineering-building-applications-with-foundation-models/ch08-datasets/p707-data-coverage.md) | Diversity and mix |
| C08-005 | [Data Quantity](../../core/ai-engineering-building-applications-with-foundation-models/ch08-datasets/p712-data-quantity.md) | Size, scaling experiments, budget |
| C08-006 | [Data Acquisition and Annotation](../../core/ai-engineering-building-applications-with-foundation-models/ch08-datasets/p721-data-acquisition-and-annotation.md) | Sourcing and guidelines |
| C08-016 | [Format Data](../../core/ai-engineering-building-applications-with-foundation-models/ch08-datasets/p764-format-data.md) | Chat template and train/serve format match |

## Procedure
1. **Choose full vs parameter-efficient.** `[C07-013]` `[C07-015]` `[C08-005]`

| Situation | Choice | Basis |
|---|---|---|
| A few hundred to a few thousand examples; consumer or mid-tier GPU; many task models to serve | PEFT, LoRA as default family | PEFT is sample-efficient; adapters let one base serve many models; full finetuning may not beat LoRA on a few hundred examples |
| Tens of thousands to millions of examples, best quality needed, memory available | Full finetuning (smaller base) | Best performance, but memory and data cost are highest |
| Memory is the binding constraint | QLoRA (4-bit base, NF4) | Saves memory (book: a 65B model on one 48 GB GPU); training may take longer from quantize and dequantize steps |
| Partial finetuning (train top layers only) | INTERPRETATION: avoid as a default | Parameter-inefficient: BERT-large needed roughly 25% of parameters to match full finetuning |

   Memory scale for full finetuning: a 7B model in 16-bit with Adam needs about 56 GB before activations (14 GB weights + 42 GB gradients and optimizer states) `[C07-013]`. Beginners should try LoRA first and full finetuning later. LoRA does not match full finetuning performance and needs framework support for the base model. `[C07-013]` `[C07-015]` Soft prompts and other adapter families (BitFit, IA3) exist but LoRA dominates in the book (time-sensitive). `[C07-013]`
2. **Configure LoRA** (starting points to validate, not rules): `[C07-013]`
   - Targets: the four attention matrices (query, key, value, output) are the common default; with a fixed budget, query and value are the best pair; adding feedforward layers often helps if memory allows.
   - Rank: 4 to 64 usually suffices; the sources disagree (one found no gain above a point, another found 256 best), so test.
   - Alpha: the update is W' = W + (alpha / r) x W_AB. Start with alpha:r between 1:8 and 8:1 and search the (r, alpha) pair.
   - Serving: merge adapters into the base for a single model (no added latency); keep adapters separate for many per-task or per-customer models on one base (smaller storage, faster switching, some added latency).
3. **Decide on multi-task handling.** If one model must do several tasks: `[C07-014]`
   - Simultaneous finetuning: one dataset of all tasks, more data and training.
   - Sequential finetuning: risks catastrophic forgetting of earlier tasks.
   - Finetune per task in parallel, then merge: less forgetting; merging needs no GPUs when not finetuning afterwards.
   - Merging approach: summing (linear combination, SLERP for two models) suits models from the same base and especially adapters; prune redundant task-vector parameters first when merging several (TIES, DARE); layer stacking changes size and needs further finetuning; concatenation is not recommended because it saves no memory. Many techniques are experimental and may be outdated. Compare with ensembling, which keeps models intact but needs several inference calls per request.
4. **Select the base model and path.** Apply Chapter 4 selection criteria (size, licence, benchmark performance). Data volume interacts with base size: with little data use PEFT on a stronger base; with a lot of data full finetuning on a smaller base can match it; with millions of examples, smaller models are prone to ossification, so test whether starting from scratch is worth evaluating `[C08-005]`. Start feasibility with the strongest affordable model; then follow the progression path (test code on the cheapest model, test data on a mid-range model, push the best model, then map the price-performance frontier) or the distillation path (best model on small data, generate more data, train a cheaper model; check the teacher's licence). `[C07-015]`
5. **Choose the tooling.** A finetuning API is easiest but limits base models and knobs; open frameworks give control and need compute provisioning; multi-machine work needs distributed-training frameworks. The book's named tools are examples and time-sensitive. `[C07-015]`
6. **Set the data targets.** For each of the six quality traits (relevant, aligned with task requirements, consistent, correctly formatted, sufficiently unique, compliant) write a pass rule (INTERPRETATION); a small, consistent, high-quality set is the goal, since 10K crafted examples beat far more noisy ones and 1,000 curated examples gave a usable but not product-grade model `[C08-003]`. Check duplicates (contamination) and compliance (PII) before training. `[C08-003]` Coverage: include the length, typo, language and topic variety real users show; mirror real usage for the mix, or run small-model scaling experiments. `[C08-004]`
7. **Set the data quantity by experiment.** Hand-craft about 50 examples and finetune; expect visible gains within 50-100. If none, check learning rate, data quality and prompts before giving up. Then train on 25%, 50% and 100% of the data and plot the curve. The three factors that move the required amount are the method (full needs far more than PEFT), task complexity, and how close the base model already is. Add task diversity before more of the same data. Stage training (self-supervised or synthetic first, real later) only if you can manage the handoff. Cap the target by annotation budget. `[C08-005]`
8. **Plan acquisition and annotation.** INTERPRETATION: own application data first (flywheel), then checked public datasets with licence and provenance traced (never fully trust them), then manual annotation and synthesis (see `data-and-retrieval.md`). Write annotation guidelines early (what a good response is, what separates scores); they can be reused from evaluation. Expect rounds of revision and fact-checking. `[C08-006]`
9. **Format the data.** Use the exact chat template of the target model. Convert few-shot prompts into one training example per shot and drop the task description and examples from the instruction once enough data exists (this shortens inference prompts). Generate training and serving prompts from one template function so they cannot drift; test format variants because format changes performance. `[C08-016]` The shared-function advice is the module's `INTERPRETATION`.
10. **Set hyperparameter starting points and read the curves.** `[C07-015]`

| Setting | Starting point | How to adjust |
|---|---|---|
| Learning rate | Within 1e-7 to 1e-3; or the end-of-pretraining rate times 0.1-1 | Raise while the loss curve stays stable; large fluctuation means too high, slow stable fall means too low |
| Batch size | Avoid under 8 | Larger is steadier but memory-bound; use gradient accumulation when memory limits it |
| Epochs | 1-2 for millions of examples; 4-10 for thousands | Training and validation loss both falling: continue; validation rising: overfitting, fewer epochs |
| Prompt loss weight | Default about 10% | 0% learns from responses only; 100% weights prompt and response equally |

11. **Write the run sequence and the stop rules.** Follow the book's progression path (cheapest model for a code smoke test, mid-range model as the data test where falling loss shows the data is sound, best model for the quality run, then scale-up across models); re-evaluate after each against the baseline and against other tasks to catch regression; precision changes require re-evaluation (see `finetune-decision.md`). `[C07-015]`

## Evidence and exit gate
Exit when: method, rank/alpha or full-finetune settings, base model and path are recorded with reasons; data targets for quality, coverage and quantity are written with the experiments that will confirm them; sources and licences are listed; format and template are fixed; hyperparameter starting points and stop rules are written; the evaluation set and baseline from `finetune-decision.md` are linked, and regression checks for other tasks are included. Values taken from the book (rank ranges, learning rates, epochs) are labelled starting points, not results. Clipped book tables (the LoRA rank comparison) cannot support a rank claim; do not cite them for one.

## Outputs
[../../templates/decision-record.md](../../templates/decision-record.md) for method, base model and data plan; thresholds and regression checks into [../../templates/eval-plan.md](../../templates/eval-plan.md).

## Pitfalls
- Jumping to full finetuning with a few hundred examples. `[C07-015]` `[C08-005]`
- Assuming a higher LoRA rank always helps, or copying one paper's rank. `[C07-013]`
- Separate adapters served without planning for the added latency. `[C07-013]`
- Sequential task finetuning that erases earlier tasks. `[C07-014]`
- Merging models with mismatched scales or architectures without rescaling or projection. `[C07-014]`
- Wrong chat template or a serving prompt that differs from training. `[C08-016]`
- Noisy, duplicated, inconsistent or non-compliant data. `[C08-003]`
- Data that lacks the variety users show. `[C08-004]`
- Judging finetuning from a tiny run with a poor learning rate. `[C08-005]`
- Unvetted public data and abandoned annotation guidelines. `[C08-006]`
- Treating named frameworks and merged-model results as current. `[C07-015]` `[C07-014]`
