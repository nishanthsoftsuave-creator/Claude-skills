---
id: C09-001
title: Inference Optimization Chapter Introduction
source_pages: "773-774"
chapter: 9
concepts: [inference-optimization, latency, cost, model-level-optimization, hardware-level-optimization, service-level-optimization, trade-offs]
related: [C09-002, C09-003, C09-006, C09-007, C09-008]
time_sensitive: false
---
# Inference Optimization Chapter Introduction
(Source: PDF pp. 773-774, tail PDF p. 775)

## What the section covers
The opening of Chapter 9. It states why speed and cost matter, names the three levels at which inference can be optimized, says who works on the problem, and tells the reader what the chapter will and will not cover and why it is worth reading even without building an inference service.

## Why it matters
- Models change constantly, but the book says that making them better, cheaper and faster stays relevant (PDF p. 773). Earlier chapters were about making models better; this chapter is about making them faster and cheaper (PDF p. 773).
- A strong model can still fail in practice. If it is too slow, users lose patience or the predictions lose their value; the book's example is a next-day stock price predictor that needs two days per output (PDF p. 773).
- If a model costs too much to run, the return on investment may not justify it (PDF p. 773).

## Meaning: the three levels of optimization
(PDF p. 773)
- Model level: shrink a trained model, or design a more efficient architecture. The example given is an architecture without the computational bottleneck of the attention mechanism that transformer models commonly use.
- Hardware level: design more powerful hardware.
- Service level: the inference service runs the model on given hardware to handle user requests. It can apply techniques that tune a model for particular hardware, and it must also take usage and traffic patterns into account so that resources are allocated in a way that lowers latency and cost.

## Who works on it
Because the levels interlock, inference optimization is described as interdisciplinary, with collaboration among model researchers, application developers, system engineers, compiler designers, hardware architects and even data center operators (PDF p. 774).

## Scope of the chapter
- It covers the bottlenecks of AI inference and techniques to overcome them, concentrating on the model and service levels and giving an overview of AI accelerators (PDF p. 774).
- It also covers performance metrics and trade-offs (PDF p. 774).

## Alternatives and trade-offs
- Sometimes one technique improves speed and cost together. Reducing numerical precision is the example: the model becomes smaller and faster (PDF p. 774).
- Often there is a trade-off. The best hardware may make the model faster but cost more (PDF p. 774).

## When and how to apply
- More open source models are available, so more teams build their own inference services (PDF p. 774).
- Even teams that never implement these techniques benefit from knowing them, because that knowledge helps them judge inference services and frameworks (PDF p. 774).
- If an application suffers from latency or cost problems, the chapter is offered as a way to diagnose causes and find possible fixes (PDF p. 774).

## Lead-in to "Understanding Inference Optimization" (tail page)
The text at the top of PDF p. 775, above the "Inference Overview" heading, belongs to this row.
- Two distinct phases make up a model's lifecycle: training, which is the process of building a model, and inference, which is the process of using a model to compute an output for a given input. Unless you train or finetune a model, you will mostly care about inference (PDF p. 775).
- The section opens with an overview of inference that sets up shared vocabulary for the rest of the chapter; readers already familiar with those concepts may skip to the part they need (PDF p. 775).

## Relations
The next row, C09-002, defines the vocabulary (inference server, bottlenecks, online versus batch APIs); C09-003 covers the metrics; C09-006 and C09-007 cover the model-level and service-level techniques.
