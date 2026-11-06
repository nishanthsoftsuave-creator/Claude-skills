---
id: C07-009
title: Memory Math
source_pages: "622-626"
chapter: 7
concepts: [memory-math, inference-memory, training-memory, activations, kv-cache, gradients, optimizer-states, adam, gradient-checkpointing, activation-recomputation]
related: [C07-007, C07-008, C07-010, C07-011]
time_sensitive: false
---
# Memory Math
(Source: PDF pp. 622-626; the top of PDF p. 622 shows Figure 7-4, which illustrates the previous subsection, C07-008. Figure 7-5, referenced at the end of this row, is printed on the first page of the next row and is described in C07-010.)

## What the section covers
Back-of-the-napkin formulas for how much memory a model needs for inference and for training, worked numeric examples, and a caveat about activation memory and gradient checkpointing.

## Figure 7-4 (context from the previous subsection)
The diagram on PDF p. 622 shows an input fanning out to three parameters w1, w2, w3. Each passes through an activation function f to give activations a1, a2, a3; these feed an output, then a loss (the difference between predicted and actual output). Solid arrows are the forward pass. Dotted arrows are the backward pass, carrying gradients (written with a delta, "gradient w.r.t. x") back to each activation (delta a1..a3) and each parameter (delta w1..w3). The text beneath it states that each trainable parameter gets extra values in the backward pass, its gradient and optimizer states, so more trainable parameters need more memory (PDF p. 622).

## Why it matters
Knowing a model's memory need tells you which hardware is right. Often the hardware is fixed and you must check whether a model fits: a model needing 30 GB for inference will not run on a 24 GB chip (PDF p. 622). Footprint depends on the model, the workload and the optimization techniques used, so the book gives only approximate formulas for a rough idea of what is needed for inference and training (PDF p. 623). A note in the book says that inference and training having distinct memory profiles is one reason chips for training and inference diverge (discussed in Chapter 9) (PDF p. 623).

## How it works

### Memory for inference
Inference runs only the forward pass. Symbols: N = number of parameters; M = memory per parameter (bytes).
- Weights: `N x M` (PDF p. 623).
- The forward pass also needs memory for activation values, and transformers need memory for the attention key-value vectors. Both grow linearly with sequence length and batch size (PDF p. 623).
- For many applications, activations plus key-value vectors can be assumed to be 20% of the weight memory. Footprint then is `N x M x 1.2`. A longer context or bigger batch makes the real number higher (PDF p. 624).
- Example (checked): 13B parameters at 2 bytes each: 13B x 2 bytes = 26 GB for weights; x 1.2 = 31.2 GB total for inference (PDF p. 624).
- Memory grows fast with size: a 70B model at 2 bytes per parameter needs 140 GB for the weights alone (70B x 2 = 140) (PDF p. 624).

### Memory for training
Training needs the weights and activations (above) plus gradients and optimizer states, which scale with the number of trainable parameters (PDF p. 624):
`Training memory = model weights + activations + gradients + optimizer states` (PDF p. 625).

Per trainable parameter in the backward pass: one gradient value plus zero to two optimizer-state values depending on the optimizer (PDF p. 625):
- Vanilla SGD: no state.
- Momentum optimizer: one value per trainable parameter.
- Adam: two values per trainable parameter.

Examples (checked), assuming Adam and 2 bytes per value, so 3 values (gradient + two states) per trainable parameter (PDF p. 625):
- Updating all 13B parameters: 13 billion x 3 x 2 bytes = 78 GB for gradients and optimizer states.
- Only 1B trainable parameters: 1 billion x 3 x 2 bytes = 6 GB.
INTERPRETATION: The gap illustrates why finetuning methods that train fewer parameters save so much memory.

### Activation memory can dominate
The formula above assumes activation memory is smaller than weight memory. In reality it can be much larger when activations are stored for gradient computation and can dwarf the weights (PDF p. 626). The book points to Figure 7-5 (from Korthikanti et al. 2022, "Reducing Activation Recomputation in Large Transformer Models"), which compares activation memory with weight memory for Megatron models of various scales (PDF p. 626); the figure itself is on the next page.

### Gradient checkpointing
One way to lower activation memory is not to store activations and instead recompute them when needed. This is called gradient checkpointing or activation recomputation. It cuts memory but lengthens training because of the recomputation (PDF p. 626).

## Assumptions and limitations
- The 20% overhead for activations and key-value vectors is an assumption for "many applications", not a rule; long contexts and large batches exceed it (PDF p. 624).
- The training formula's example numbers cover only gradients and optimizer states; they do not include the weights or activations and ignore the large-activation case (PDF pp. 625-626).
- The 2-bytes-per-value assumption is revisited in the next section on numerical representations (C07-010).

## Relations
Builds on backpropagation and trainable parameters (C07-008); the bytes-per-value variable M is explained by numerical formats (C07-010) and reduced by quantization (C07-011).
