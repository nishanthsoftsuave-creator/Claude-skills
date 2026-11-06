---
id: C07-015
title: Finetuning Tactics
source_pages: "680-686"
chapter: 7
concepts: [finetuning-tactics, base-model-selection, progression-path, distillation-path, finetuning-frameworks, learning-rate, batch-size, gradient-accumulation, epochs, prompt-loss-weight]
related: [C07-013, C07-014, C07-016, C04-001]
time_sensitive: true
---
# Finetuning Tactics
(Source: PDF pp. 680-686; the section's last paragraphs, on prompt loss weight, run onto PDF p. 687 above the Summary heading)

## What the section covers
The practical side of finetuning: choosing a base model, a finetuning method and a framework, and tuning the commonly encountered hyperparameters (learning rate, batch size, number of epochs, prompt loss weight). The book frames the actual finetuning process as more straightforward than the hard surrounding questions (whether to finetune, getting data, maintaining models) (PDF p. 680).

## How it works

### Base models
- Chapter 4's selection criteria (model size, license, benchmark performance) apply to both prompting and finetuning (PDF p. 680).
- At the start of a project, while checking feasibility, begin with the most powerful model you can afford. If it struggles, weaker models will do worse; if it succeeds, explore weaker ones using it as the comparison benchmark (PDF p. 680).
- OpenAI's finetuning best-practices document gives two development paths (PDF p. 681).
  - Progression path: (1) test the finetuning code on the cheapest, fastest model to confirm the code works; (2) test the data by finetuning a mid-range model, since training loss that does not fall with more data suggests something is wrong; (3) run more experiments with the best model to see how far performance goes; (4) once results are good, train with all models to map the price/performance frontier and choose the one that fits your use case.
  - Distillation path: (1) train the best possible model on a small dataset using the strongest model affordable; a strong base needs less data; (2) use that finetuned model to generate more training data; (3) train a cheaper model on this new dataset.
- Since finetuning usually follows prompt-engineering experiments, you should already understand how different models behave and plan your path accordingly (PDF pp. 681-682).

### Finetuning methods
- Adapter techniques such as LoRA are cost-effective but usually do not match full finetuning performance. Beginners are advised to try LoRA first and attempt full finetuning later (PDF p. 682).
- Data volume matters: full finetuning typically needs at least thousands of examples, often many more, while PEFT methods can do well with far less. With a few hundred examples, full finetuning may not beat LoRA (PDF p. 682).
- Consider how many finetuned models you need and how you will serve them. Adapter methods let you serve a single full base model with many adapters, whereas full finetuning needs several full models served (PDF p. 682).

### Finetuning frameworks
- Easiest route: a finetuning API where you upload data, choose a base model, and receive a finetuned model. Providers can be model makers, cloud providers or third parties. Limits: only supported base models, and not all useful knobs may be exposed. Good for quick, easy work, frustrating for customization (PDF p. 683).
- Alternatively use frameworks such as LLaMA-Factory, unsloth, PEFT, Axolotl and LitGPT, which support many methods, especially adapter-based ones. For full finetuning, many base models publish open-source training code to clone and run on your data. The book points to Llama Police for a current list of frameworks and model repositories (PDF p. 683; time-sensitive).
- Doing it yourself gives flexibility but you must provision compute. Adapter-only finetuning may need just a mid-tier GPU for most models; for more, pick a framework that integrates with your cloud provider (PDF p. 683).
- Multi-machine finetuning needs distributed-training frameworks such as DeepSpeed, PyTorch Distributed and ColossalAI (PDF p. 684).

### Finetuning hyperparameters
Hyperparameters depend on the base model and method; consult the model or framework documentation. The book covers a few that appear often (PDF p. 684).

**Learning rate.** It sets how fast parameters change per step; think of it as step size toward a goal. Too small takes too long; too big overshoots and may prevent convergence. No universal optimum exists; try values typically between 1e-7 and 1e-3. A common practice is to take the learning rate at the end of pretraining and multiply by a constant between 0.1 and 1 (PDF p. 684). The loss curve hints at the right value: large fluctuation suggests too high; stable but slow decrease suggests too low. Raise the rate as high as the loss curve stays stable (PDF p. 685). Rates can vary during training, larger early and smaller late; algorithms that set this are learning rate schedules (PDF p. 685).

**Batch size.** The number of examples used per weight update. Very small batches (under eight) can make training unstable; larger batches aggregate signals from different examples and give steadier, more reliable updates. Larger batches also process the data faster but need more memory, so hardware caps the size. This is a cost versus efficiency trade-off: pricier compute allows faster finetuning (PDF p. 685). The book notes compute is still a bottleneck: models are so large and memory so constrained that only small batches are possible. Remedy: gradient accumulation, which accumulates gradients across several batches and updates the weights only once enough reliable gradient has built up. When compute cost is not the main concern, try different batch sizes and pick the best-performing one (PDF p. 686).

**Number of epochs.** An epoch is one pass over the training data. Small datasets may need more epochs: with millions of examples, 1 to 2 epochs may suffice, while thousands of examples may keep improving through 4 to 10 epochs (PDF p. 686). Compare training and validation loss: if both still fall steadily, more epochs (and data) can help; if training loss falls while validation loss rises, the model is overfitting and fewer epochs may help (PDF pp. 686-687).

**Prompt loss weight.** In instruction finetuning each example has a prompt and a response, both of which can contribute to the training loss. At inference users supply prompts and the model only produces responses, so response tokens should count more than prompt tokens in the loss. The prompt (loss) weight sets how much prompts count relative to responses: 100% means equal contribution, 0% means learning from responses only. The usual default is 10%, so the model learns a little from prompts and mostly from responses (PDF p. 687).

## When and how to apply
Start with the strongest affordable model to judge feasibility, use a cheap model to debug code, a mid model to validate data, then scale. Try LoRA before full finetuning, especially with few examples or many models to serve. Use an API for speed, a framework for control. Read the loss curves (stability for learning rate, train versus validation for epochs) to tune.

## Relations
Applies the methods from C07-013 and C07-014; model selection criteria come from Chapter 4 (C04-001 is that chapter's start). The chapter closes with C07-016.

## Time-sensitive statements
Named frameworks, the Llama Police list and the typical default of 10% for prompt weight reflect the date of writing.
