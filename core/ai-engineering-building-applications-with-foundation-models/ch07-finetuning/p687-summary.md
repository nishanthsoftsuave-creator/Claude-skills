---
id: C07-016
title: Chapter 7 Summary and Endnotes
source_pages: "687-693"
chapter: 7
concepts: [finetuning-summary, peft, quantized-training, lora, model-merging, finetune-vs-rag, endnotes, mixed-precision]
related: [C07-001, C07-006, C07-013, C07-014, C08-001]
time_sensitive: true
---
# Chapter 7 Summary and Endnotes
(Source: PDF pp. 687-693. The top of PDF p. 687 holds the end of the Finetuning Tactics section, which belongs to C07-015; the Summary starts part-way down that page. The following page begins Chapter 8 and is not covered here.)

## What the section covers
The chapter wrap-up and the endnotes that accompany Chapter 7. The summary recaps the chapter's themes; the notes add asides and pointers.

## Summary content
- The author calls finetuning the hardest chapter to write apart from the evaluation chapters, because it spans old concepts (transfer learning) and new ones (PEFT), fundamental (low-rank factorization) and experimental (model merging), mathematical (memory calculation) and tactical (hyperparameter tuning). Fitting them into an accessible, coherent structure was difficult (PDF pp. 687-688).
- The process of finetuning is not hard; frameworks run the training and can even propose common methods with sensible default hyperparameters. The surrounding context is the complex part, starting with whether to finetune at all (PDF p. 688).
- The chapter began with reasons for and against finetuning, and with a question the author is often asked: when to finetune and when to use RAG (PDF p. 688).
- Early finetuning resembled pre-training in updating all weights, but as models grew, full finetuning became impractical for most practitioners. More parameters to update means more memory, and most lack the hardware, time and data for full finetuning of foundation models (PDF p. 688).
- Many techniques share one motivation: strong performance with a small memory footprint. PEFT reduces memory by cutting the number of trainable parameters; quantized training reduces memory by using fewer bits per value (PDF pp. 688-689).
- After the PEFT overview the chapter examined LoRA: why and how it works. Beyond being parameter- and data-efficient, it is modular, which makes serving and combining multiple LoRA models easier (PDF p. 689).
- That modularity led to model merging, whose goal is one model better than its constituents separately. The chapter covered use cases from on-device deployment to model upscaling, plus general merging approaches (PDF p. 689).
- A frequent remark from practitioners is that finetuning is easy but getting finetuning data is hard, especially high-quality annotated instruction data. The next chapter takes up those challenges (PDF p. 689).

## Endnotes (what each records)
Note numbers are not preserved reliably in the extracted text, so notes are given in the order printed.
- Some call the phenomenon of capability loss an "alignment tax" (Bai et al., 2020), but that term can be confused with penalties against human-preference alignment (PDF p. 689).
- Many businesses resist replacing technology they consider good enough; otherwise fax machines would be obsolete (PDF p. 689).
- Some engineers know finetuning is not strictly necessary but insist on it to learn how. The author sympathizes, but a leader may struggle to tell need from want (PDF p. 690).
- The "0314" in a GPT-4 name is a date stamp (March 14, 2024, as printed), and it matters because versions differ significantly in performance (PDF p. 690).
  SUPPLEMENTARY: GPT-4-0314 was released in March 2023, so the printed year 2024 looks like a slip in the book.
- The Llama 3.1 authors hold the principle that post-training should align the model to know what it knows rather than add knowledge (PDF p. 690).
- Besides backpropagation, evolutionary strategies (for example random search with surrogate gradients, Maheswaranathan et al.) and direct feedback alignment (Nokland, 2016) are promising training approaches (PDF p. 690).
- A non-trainable parameter needs no update, so no gradient is computed for it (PDF p. 690).
- A joke that you are not doing AI until you have seen "CUDA out of memory" (PDF p. 690).
- Pointers: Carol Chen's "Transformer Inference Arithmetic" and kipply's blog for inference memory; EleutherAI's "Transformer Math 101" for training memory (PDF p. 690).
- Google introduced BFloat16 as the secret to high performance on Cloud TPUs. Integer formats are also called fixed-point formats (PDF p. 690).
- Range bits are called exponents; precision bits are called significands (PDF p. 691).
- TF32 actually uses 19 bits, not 32; the author guesses the name signals functional compatibility with FP32 and relays an NVIDIA ex-coworker's guess that a 19-bit name would seem unfriendly (PDF p. 691).
- FP16 versus BF16 confusion continued with Llama 3.1; the note lists social-media discussions and benchmarks and write-ups (llama.cpp, Bloke, Raschka) (PDF p. 691).
- Designing numerical formats is fascinating; a lower-precision format without quality loss makes systems cheaper and faster (PDF p. 691).
- Another major memory contributor in transformers is the KV cache, discussed in Chapter 9 (PDF p. 691).
- The smallest float size following all IEEE principles is 4-bit (PDF p. 691).
- The Xnor-Net authors spun off Xnor.ai, a model-compression startup that Apple reportedly acquired in early 2020 for about $200M (PDF p. 691).
- In training, weights update over many steps, so small rounding changes compound, and loss values need precise computation because small errors can point updates the wrong way (PDF p. 691).
- Personal anecdote: much of the author's NVIDIA team's work was mixed-precision training (the author et al., 2018 NVIDIA blog on OpenSeq2Seq) (PDF p. 691).
- In partial finetuning it is common to finetune layers nearest the output, since they are more task-specific while earlier layers capture general features (PDF p. 692).
- The author has never met anyone who could explain on the spot the differences among the PEFT techniques (PDF p. 692).
- Using LoRA well requires understanding the model's architecture; Chapter 2 covers weight composition for some transformers, and the model's paper gives exact composition (PDF p. 692).
- Some frameworks (Fireworks is named) cap LoRA rank at 32, probably from hardware memory limits rather than performance (PDF p. 692; time-sensitive).
- Search for adapters by tags "adapter", "peft" or "LoRA" (PDF p. 692).
- QLoRA is not the only quantized LoRA work; many labs work on it without public discussion (PDF p. 692).
- The author's book Designing Machine Learning Systems covers "ML on the Cloud and on the Edge" and ensemble methods (PDF p. 692).
- Averaging works for embeddings too: averaging word embeddings gives a sentence embedding. The author still finds it magical that averaging works (PDF p. 692).
- Assumption behind pruning by magnitude: the parameters that change most in finetuning matter most for the target task (PDF p. 692).
- TIES abbreviates "TrIm, Elect Sign, and merge"; DARE abbreviates "Drop And REscale" (PDF p. 693).
- Pruned task vectors become sparse, but the finetuned model does not; here pruning is meant to improve performance, not memory or latency (PDF p. 693).
- The author debated including concatenation and kept it for completeness (PDF p. 693).
- Anecdote: a model trained overnight crashed after eight hours because the checkpoint was saved to a nonexistent folder (PDF p. 693).
- The author could not find a good explanation for why small batches destabilize training and invites references (PDF p. 693).
- Gradient accumulation's first paper could not be found; deep-learning use is mentioned in 2016 (Ako, Watcharapichat et al.), and the idea seems to come from distributed training where gradients from different machines are accumulated (PDF p. 693).

## Relations
Recaps C07-001 through C07-015 (RAG question: C07-006; PEFT and LoRA: C07-013; merging: C07-014). Chapter 8 (C08-001) follows with dataset engineering.

## Time-sensitive statements
The Fireworks LoRA rank cap of 32 (PDF p. 692) is a statement about frameworks at the time of writing and may have changed. The reported Apple acquisition of Xnor.ai for about $200M (PDF p. 691) and the Llama 3.1 FP16/BF16 discussion (PDF p. 691) are also dated.
