---
name: finetune-decision
mode: architect
rows: [C07-002, C07-004, C07-005, C07-006, C07-008, C07-009, C07-010, C07-011]
---
# Finetune decision and feasibility

## When to use
Run when the design weighs finetuning against prompting and RAG, or when a failure analysis points to a behavior gap. Run before `finetune-plan.md`; do not plan a finetune that fails the decision gate or the memory feasibility check below. Pair with `solution-pattern.md` (which chooses the overall pattern).

## Inputs needed
From discovery and `intake.md`; ask only what is missing:
- Evidence of what is failing now: prompt experiments run, with representative examples and defined metrics, and what the failures look like (wrong facts vs wrong form).
- Candidate base model and its parameter count; open-weight or API-only (API-only may limit finetuning access).
- Available data (volume, quality), training skill, serving capability, budget, and a model-refresh policy.
- Hardware memory (GPU GB) and whether training will be full or parameter-efficient.
- Other tasks the same model must keep serving.

## Modules to load
| Row | Module | Why it is needed here |
|---|---|---|
| C07-002 | [Finetuning Overview](../../core/ai-engineering-building-applications-with-foundation-models/ch07-finetuning/p596-finetuning-overview.md) | What finetuning is, variants, who does it |
| C07-004 | [Reasons to Finetune](../../core/ai-engineering-building-applications-with-foundation-models/ch07-finetuning/p602-reasons-to-finetune.md) | Positive cases |
| C07-005 | [Reasons Not to Finetune](../../core/ai-engineering-building-applications-with-foundation-models/ch07-finetuning/p604-reasons-not-to-finetune.md) | Costs, regressions, prompting first |
| C07-006 | [Finetuning and RAG](../../core/ai-engineering-building-applications-with-foundation-models/ch07-finetuning/p611-finetuning-and-rag.md) | Information vs behavior failures, adaptation workflow |
| C07-008 | [Backpropagation and Trainable Parameters](../../core/ai-engineering-building-applications-with-foundation-models/ch07-finetuning/p620-backpropagation-and-trainable-parameters.md) | Why trainable parameters drive memory |
| C07-009 | [Memory Math](../../core/ai-engineering-building-applications-with-foundation-models/ch07-finetuning/p622-memory-math.md) | Inference and training memory formulas |
| C07-010 | [Numerical Representations](../../core/ai-engineering-building-applications-with-foundation-models/ch07-finetuning/p627-numerical-representations.md) | Bytes per value, formats |
| C07-011 | [Quantization](../../core/ai-engineering-building-applications-with-foundation-models/ch07-finetuning/p631-quantization.md) | Reducing precision to cut memory |

## Procedure
### A. Should we finetune at all
1. **Name the variant.** Finetuning is transfer learning on a base model; the book distinguishes self-supervised (continued pre-training), supervised, infilling, preference and long-context finetuning (harder than the others and the model may get worse on shorter sequences). Most application developers finetune an already post-trained model, and the closer it is to the task, the less adaptation is needed. `[C07-002]`
2. **Classify the failure.** `[C07-006]`

| Failure | Typical cause | Lever |
|---|---|---|
| Wrong, missing or outdated facts; private knowledge absent | Information-based | RAG (see `data-and-retrieval.md`) |
| Facts right but irrelevant, wrong format or style, unsafe, weak on a rare syntax or dialect | Behavior-based | Finetuning |
| Both | Mixed | Start with RAG; it needs no training data or model hosting |

   The book's summary is "finetuning is for form, RAG is for facts." In Ovadia et al., RAG beat finetuning on current-events and MMLU questions for the three 7B models tested, and RAG on the base model beat RAG on finetuned models; adding RAG to a finetuned model helped 43% of the time. Low-quality finetuning data can worsen hallucination. `[C07-006]`
3. **Check the reasons for.** A gap shown by evaluation that prompting has not closed: uncommon SQL dialect or customer-specific queries, strict output structure, bias to counteract with curated data, or a small cheap model (often distilled, see `data-and-retrieval.md`; the book's example is a finetuned Flan-T5 beating a GPT-3 variant while 60 times smaller). Open-weight models have made finetuning more viable. `[C07-004]`
4. **Check the reasons against.** Do not finetune until each is answered: `[C07-005]`
   - Prompting was tried systematically (varied prompts, representative examples, defined metrics). The book reports that "prompting does not work" usually meant minimal experiments.
   - Finetuning for one task can degrade others; the remedies are training on all needed tasks, separate models, or merging (see `finetune-plan.md`).
   - Data, training know-how, serving capability and a policy for when to switch to a newer base model all exist.
   - A newer general model may overtake a specialised one (the BloombergGPT case; figures are time-sensitive).
   - The token-saving argument is weak with prompt caching, but finetuning still has no cap on example count, unlike in-prompt examples.
5. **Apply the book's adaptation order.** Define evaluation first, then: prompt alone; add 1-50 examples; add simple term-based retrieval if information is missing; then branch (advanced RAG for persisting information failures, finetuning for persisting behavior failures); then combine. Embedding retrieval complicates inference; finetuning complicates development but leaves inference unchanged. `[C07-006]`
6. **Decision gate.** The gate criteria are INTERPRETATION built from the book's own checklist. Proceed to B only if: evaluation shows a behavior gap, prompt and retrieval options were tried or ruled out in writing, and the "against" checks pass or have owners. Otherwise record "do not finetune yet" with the next experiment. `[C07-005]` `[C07-006]`

### B. Memory feasibility check (worked procedure)
Variables: N = parameters, M = bytes per value, trainable parameters T. Formulas are the book's back-of-the-napkin estimates. `[C07-009]`
7. **Pick bytes per value M.** FP32 = 4, FP16 or BF16 = 2, INT8 = 1, INT4 = 0.5 (bits divided by 8; the division is `INTERPRETATION`). Use the format the model was released in: the book's Llama 2 example was released in BF16 but many loaded it as FP16 and saw degraded quality. BF16 keeps FP32's range with less precision; FP16 overflows large values. Choose by value range, sensitivity and hardware. `[C07-010]`
8. **Inference memory** = N x M x 1.2 (the 1.2 assumes activations plus key-value vectors are about 20% of weights; long contexts or big batches exceed it). Example: 13B at 2 bytes gives 26 GB weights, 31.2 GB total; 70B at 2 bytes needs 140 GB for weights alone. If the figure exceeds the chip's memory (30 GB will not run on 24 GB), reduce M or choose a smaller model. INTERPRETATION arithmetic for lower precision: 70B at INT8 is 70 GB of weights and at INT4 35 GB; the 1.2 factor was stated for the book's 2-byte case, and if weights are quantized while activations and key-value vectors stay at 16 bits it may understate the overhead, so treat it as a floor. `[C07-009]`
9. **Training memory** = weights + activations + gradients + optimizer states. Per trainable parameter: one gradient, plus optimizer state of 0 (vanilla SGD), 1 (momentum) or 2 (Adam) values. Gradient and optimizer memory = T x (1 + states) x M. Example with Adam at 2 bytes: all 13B trainable gives 13B x 3 x 2 = 78 GB; 1B trainable gives 6 GB. Add the weights (step 8 without the 20% term) and an activation allowance. INTERPRETATION worked sums for 13B at 2 bytes with Adam: full finetune is 26 + 78 = 104 GB plus activations; with 1B trainable it is 26 + 6 = 32 GB plus activations (frozen weights still occupy memory). `[C07-008]` `[C07-009]` Activations can dwarf weights when stored for gradients (the book's Figure 7-5 shows this for Megatron models; its values are estimates). Gradient checkpointing lowers activation memory at the cost of longer training. `[C07-009]` `[C07-010]`
10. **Apply levers, cheapest first (INTERPRETATION ordering).** Quantize: 10B parameters need 40 GB at 32 bits and 20 GB at 16. Post-training quantization is the common route for developers and is easy, but it reduces inference memory of a trained model; savings in training memory need lower-precision or mixed-precision training or fewer trainable parameters; weight quantization is steadier than activation quantization. Conversions change values slightly and out-of-range values can become infinity, so re-run the evaluation after any precision change. Quantization-aware training and low-precision training are harder; mixed precision keeps sensitive parts in higher precision. Finetuning in lower precision than the original training is common. Then cut trainable parameters (parameter-efficient methods, see `finetune-plan.md`). `[C07-011]` `[C07-008]`
11. **Report feasibility** as a small table: format, N, inference GB, training GB for full vs parameter-efficient, hardware GB, verdict (fits, fits only with levers X, does not fit). Mark the 20% overhead and any activation allowance as assumptions. `[C07-009]` Re-derive the arithmetic when inputs change; do not reuse book numbers for other models.

## Evidence and exit gate
Exit when: the failure is classified with evidence from the user's own outputs; every "against" item is answered; the adaptation order is documented; the feasibility table is filled with stated assumptions; the verdict is one of {no finetune, RAG first, finetune with plan}. A verdict of "finetune" without a baseline evaluation is capped at a recommendation. Where evidence is thin, list the cheapest experiment (better prompts, 50-example finetune per `finetune-plan.md`).

## Outputs
[../../templates/decision-record.md](../../templates/decision-record.md) (prompt vs RAG vs finetune, with options, criteria and revisit triggers such as a new base model beating the target on your eval). Feed the evaluation baseline to [../../templates/eval-plan.md](../../templates/eval-plan.md).

## Pitfalls
- Finetuning to inject fresh facts instead of using RAG. `[C07-006]`
- Concluding prompting failed after unsystematic trials. `[C07-005]`
- Improving one task and silently regressing others. `[C07-005]`
- No policy for adopting newer base models; specialised model overtaken. `[C07-005]`
- Loading a model in the wrong numerical format. `[C07-010]`
- Treating the 1.2 factor as exact, or forgetting activations in training memory. `[C07-009]`
- Quantizing without re-evaluating quality. `[C07-011]`
- Rushing to finetune a model that is already near the target. `[C07-002]` `[C07-004]`
