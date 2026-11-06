---
id: C07-014
title: Model Merging and Multi-Task Finetuning
source_pages: "664-679"
chapter: 7
concepts: [model-merging, multi-task-finetuning, catastrophic-forgetting, ensembling, linear-combination, task-vectors, slerp, ties-dare-pruning, layer-stacking, model-upscaling, concatenation]
related: [C07-013, C07-012, C07-015, C07-011]
time_sensitive: true
---
# Model Merging and Multi-Task Finetuning
(Source: PDF pp. 664-679)

## What the section covers
Model merging: building a custom model by combining several models instead of altering just one. The section explains the goals and use cases (better quality, smaller memory, multi-task finetuning, on-device deployment, federated learning), contrasts merging with ensembling, and then walks through three families of merging approaches: summing (linear combination, SLERP, pruning of redundant task-vector parameters), layer stacking (frankenmerging, MoE upcycling, depthwise upscaling) and concatenation.

## Meaning
- Finetuning changes one model; merging combines multiple models. You may finetune any or all constituents before merging, and you may finetune the merged result afterwards, which often helps, but you do not have to (PDF p. 664).
- Without finetuning, merging needs no GPUs, which makes it attractive for indie model developers short on compute (PDF p. 664).
- Ensembling is the older idea of combining models for better predictive performance. Merging typically mixes the parameters of the constituents; ensembling typically keeps each model intact and combines only their outputs (PDF p. 667).
- Task vector (also called delta parameters): finetune a model for a task, subtract the base model from it, and the difference captures the essence of that task. If you finetuned with LoRA, the task vector can be built from the LoRA weights (PDF p. 671).

## Why it matters
- The aim is one model that delivers more value than all constituents used separately (PDF p. 664).
- Value can be better performance. Illustration: one model answers the first 60% of questions, another the last 60%; combined they might answer about 80% (PDF p. 664).
- Value can be a smaller memory footprint and so lower cost: two models for different tasks merge into one model doing both with fewer parameters. This is especially appealing for adapter-based models; two adapters finetuned on the same base model can become a single adapter (PDF pp. 664-665).
- Multi-task finetuning (below), on-device deployment, and federated learning are the main use cases the book names (PDF pp. 665-667).

## How it works

### Multi-task finetuning without merging, and its problems
- Simultaneous finetuning: build one dataset containing examples of every task and train on it. Learning several skills at once is harder, so this typically needs more data and more training (PDF p. 665).
- Sequential finetuning: finetune on task A, then task B, and so on, assuming one task at a time is easier. Neural networks suffer catastrophic forgetting: training on a new task can make the model forget an earlier one and sharply lower earlier-task performance (PDF p. 665).
- Merging alternative: finetune on each task separately but in parallel, then merge. Each task is learned better in isolation, and with no sequential learning there is less risk of catastrophic forgetting (PDF p. 666).

### On-device deployment and federated learning
- Devices such as phones, laptops, cars, smartwatches and warehouse robots have limited memory. Rather than squeezing several task models onto the device, merge them into one multi-task model needing much less memory (PDF p. 666).
- On-device deployment is required when data cannot leave the device (often for privacy) or internet access is limited or unreliable, and it can cut inference cost because computation is shifted from data centers to user devices (PDF p. 666).
- Merging is one way to do federated learning: copies of model X deployed to many devices each keep learning from local data; later the copies are merged into a new base model holding what all of them learned (PDF pp. 666-667).

### Ensembling versus merging
- Ensembling example: three models answer one query; a final answer is made from the three, by simple majority vote or a trainable ML module. It generally improves performance but costs more at inference because each request needs several model calls (PDF p. 667).
- Figure 7-13 (PDF p. 668) shows the difference. In ensembling, the input goes to Model 1, 2 and 3 in parallel, each yields an output, and a Combine step produces one final output. In merging, the three models are combined first into a single merged model (which can be further finetuned), and the input then goes through that one model to produce the output.
- Just as ensembles once dominated leaderboards, many top models on Hugging Face's Open LLM Leaderboard are merged models (PDF p. 667; time-sensitive).
- The author warns that many merging techniques are experimental and may be outdated as theory improves, so the book covers high-level approaches rather than individual techniques (PDF p. 668).

### The three approaches
Approaches differ in how constituent parameters are combined: summing, layer stacking, concatenation (PDF p. 668). Figure 7-14 (PDF p. 669) shows two models drawn as three rows of small blocks each (3, 4 and 3 blocks per row, one model blue, one yellow). Summing yields one same-shaped model (drawn in a third colour) whose rows are blends of the two. Layer stacking interleaves rows taken from the two models into a new stack (in the drawing, four rows alternating between the two models, with differing row widths). Concatenation places the two models' layers side by side, giving wider layers. The approaches can be mixed, for example summing some layers and stacking others (PDF p. 669).

## Approach 1: Summing
Add the weight values of the constituent models. Two methods are covered: linear combination and spherical linear interpolation. If the models' parameters sit on different scales (one model's values much larger), rescale them first so the values share a range (PDF p. 669).

### Linear combination
- Covers both a plain average and a weighted average. For models A and B: Merge(A, B) = (w_A * A + w_B * B) / (w_A + w_B), where w_A and w_B are the weights given to each model (formula read from the rendered page) (PDF p. 670).
- Figure 7-15 (PDF p. 670) shows two small layers with w_A = w_B = 1; each merged parameter is simply the mean of the corresponding pair. Examples visible in the figure: 0.4 and 0.2 give 0.3; -0.5 and 0.1 give -0.2; -0.3 and 0.8 give 0.25; 0.05 and 0.01 give 0.03; 0.1 and 0.9 give 0.5; -0.5 and 0.3 give -0.1; 0.04 and 0.6 give 0.32.
- It works surprisingly well for something so simple. The idea dates to the early 1990s (Perrone, 1993) and is often used in federated learning (PDF p. 670).
- You can combine whole models or parts. Model soups (Wortsman et al., 2022) averaged the full weights of several finetuned models and improved accuracy without increasing inference time. More commonly, specific components such as adapters are combined (PDF p. 670).
- It is most effective for models finetuned from the same base model, where it can be read through task vectors (PDF p. 671).
- Task arithmetic (Ilharco et al., 2022): add two task vectors to combine capabilities, or subtract a task vector to reduce a capability. Subtraction can remove undesirable behaviors, such as invasive capabilities like facial recognition, or biases acquired in pre-training (PDF p. 671).
- It is easiest when components share architecture and size, but can work otherwise, for instance by projecting one or both layers to a common dimension (PDF p. 671).
- Some proposals align models before averaging so functionally related parameters are averaged together (Model Fusion via Optimal Transport; Git Re-Basin; Merging by Matching Models in Task Parameter Subspaces). Aligning is hard, so this is less common than naive linear combination (PDF pp. 671-672).

### Spherical linear interpolation (SLERP)
- SLERP is another common summing method, named after the operator. Interpolation means estimating unknown values from known ones; here the unknown is the merged model and the knowns are the constituents. Linear combination is one interpolation technique, SLERP another (PDF p. 672).
- The book skips the formula (tools implement it). Intuition: treat each component vector as a point on a sphere, draw the shortest path along the surface between two points (like the shortest route between two cities on Earth), and the merged vector is a point on that path (PDF p. 672).
- The position is set by an interpolation factor between 0 and 1. Values below 0.5 pull the result toward the first vector (the first task vector contributes more); 0.5 picks the exact midpoint (PDF pp. 672-673). Figure 7-16 (PDF p. 673) shows vectors t1 and t2, the red shortest path on the sphere, and the blue midpoint vector for factor 0.5.
- SLERP is defined for only two vectors. To merge more, apply it sequentially: A with B, then that result with C (PDF p. 673).

### Pruning redundant task-specific parameters
- During finetuning many parameters change, but most changes are minor and add little on the task; these are redundant (PDF p. 674).
- Yadav et al. (TIES-Merging, 2023) showed that a large share of task-vector parameters can be reset with minimal loss. Resetting returns a finetuned parameter to its base-model value, setting the task-vector entry to zero (PDF p. 674).
- Figure 7-17 (PDF p. 674) plots average performance against the percentage of top-K task-vector parameters kept. Performance is about 54 when keeping 0%, jumps to roughly 71-72 at 10-20%, and stays around 73-75 from there to 100%, so keeping the top 20% matches keeping all (values are estimates read from the chart).
- Redundant parameters may be harmless in one model but harmful once merged. TIES and DARE (Yu et al., 2023) prune them from the task vectors first, and both papers found this notably improves merged quality (PDF p. 675).
- Pruning matters more as more models are merged, because there are more chances for one task's redundant parameters to interfere with others (PDF p. 675).

## Approach 2: Layer stacking
- Take layers from one or more models and stack them, for example layer one from model 1 and layer two from model 2. Also called passthrough or frankenmerging. It can produce unusual architectures and parameter counts. Unlike summing, stacked models usually need further finetuning to perform well (PDF p. 675).
- Early success: Goliath-120B, merged from two finetuned Llama 2-70B models (Xwin and Euryale), taking 72 of 80 layers from each (PDF p. 675; time-sensitive example).
- MoE via stacking (Sparse Upcycling, Komatsuzaki et al., 2022): instead of training a mixture-of-experts from scratch, copy certain layers or modules of a pre-trained model several times, add a router that sends each input to the most suitable copy, and train the merged model plus router further (PDF p. 676). Figure 7-18 (PDF p. 677) shows an original dense block (layer norm, attention, layer norm, MLP). In the upcycled block the layer norms and attention are copied; the MLP is replaced by E MLP copies, a router initialized from scratch, and a weighted sum of expert outputs.
- Komatsuzaki et al. found stacked models can beat MoE models trained from scratch. Together AI mixed six weaker open-source models into Mixture-of-Agents, matching OpenAI's GPT-4o on some benchmarks (PDF p. 676; time-sensitive).

### Model upscaling and depthwise scaling
- Model upscaling studies how to build larger models with fewer resources. Example: a model sized for a 40 GB GPU, but you now have an 80 GB machine; layer stacking can make a bigger model without training from scratch (PDF p. 677).
- Depthwise scaling (Kim et al., 2023) created SOLAR 10.7B from a 7B model with 32 layers (PDF p. 677). Procedure: (1) copy the pre-trained model; (2) merge the two copies by summing some layers (two layers become one) and stacking the rest, with the summed layers chosen to hit the target size, for SOLAR 16 summed layers leaving 32 x 2 - 16 = 48 layers; (3) continue training the upscaled model toward target performance (PDF p. 678).
- Figure 7-19 (PDF p. 678) shows Step 1, depthwise scaling: copy the 32-layer model; take 24 layers from the lower copy and 24 layers from the upper copy while merging 8 layers from each; then Step 2, continued pretraining of the resulting 48-layer model.

## Approach 3: Concatenation
- Concatenate parameters rather than adding them; the merged component's parameter count equals the sum of the constituents'. Two LoRA adapters of ranks r1 and r2 yield an adapter of rank r1 + r2 (PDF p. 679). Figure 7-20 (PDF p. 679) shows A1 and A2 placed side by side and B1 and B2 stacked, giving a rank r1+r2 adapter.
- The book does not recommend it: it does not shrink memory compared with serving the models separately. It might perform better, but the gain may not justify the extra parameters (PDF p. 679). The author notes in a footnote that this technique was included for completeness (see the chapter summary row).

## When and how to apply
- Use merging for multi-task finetuning when sequential finetuning risks forgetting and simultaneous finetuning needs too much data.
- Prefer summing for models finetuned from the same base, especially adapters; prune task vectors first when merging several.
- Use layer stacking when you need a different size or an MoE, and plan to finetune afterwards.
- INTERPRETATION: because merging needs no GPUs, it is a cheap first experiment when you already hold several finetuned checkpoints or adapters.

## Alternatives and trade-offs
Ensembling keeps models intact but needs several inference calls per request; merging produces one model with single-call cost (PDF p. 667). Summing preserves size; stacking changes size and needs finetuning; concatenation grows parameters without saving memory (PDF pp. 675, 679).

## Limitations and failure modes
Many techniques are experimental and may become outdated (PDF p. 668). Mismatched scales or architectures require rescaling or projection; alignment is hard (PDF pp. 669, 671-672). Redundant parameters can interfere across merged tasks (PDF p. 675). SLERP handles two vectors at a time (PDF p. 673).

## Relations
Builds on LoRA and adapters from parameter-efficient finetuning (C07-013), which feed adapter merging and task vectors; follows the section lead-in (C07-012); practical tactics follow in C07-015.

## Time-sensitive statements
Leaderboard observations (Open LLM Leaderboard), Goliath-120B, SOLAR 10.7B and Together AI's Mixture-of-Agents versus GPT-4o results reflect the date of writing; the claim that techniques are experimental may age.
