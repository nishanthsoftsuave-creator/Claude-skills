---
id: C07-008
title: Backpropagation and Trainable Parameters
source_pages: "620-621"
chapter: 7
concepts: [trainable-parameters, frozen-parameters, backpropagation, forward-pass, backward-pass, loss, gradient, optimizer, adam, sgd]
related: [C07-007, C07-009]
time_sensitive: false
---
# Backpropagation and Trainable Parameters
(Source: PDF pp. 620-621; the top of PDF p. 620 holds the last two key takeaways of the lead-in, which belong to C07-007. Figure 7-4, announced at the end of p. 621, is printed on the next page and is described in C07-009's range.)

## What the section covers
Why trainable parameters drive finetuning memory, and how backpropagation (two phases per training step: forward and backward pass) produces the extra values, gradients and optimizer states, that must be stored.

## Meaning
- A trainable parameter is one that can be updated during finetuning. In pre-training all parameters are updated; in inference none are; in finetuning some or all may be. Parameters kept unchanged are frozen parameters (PDF p. 620).
- The memory each trainable parameter needs follows from how models are trained. At the time of writing, neural networks are typically trained with backpropagation, where every training step has two phases (PDF p. 620):
  1. Forward pass: computing the output from the input.
  2. Backward pass: updating the model's weights using the aggregated signals from the forward pass.
- Inference runs only the forward pass; training runs both (PDF p. 621).

## How it works: the backward pass
1. Compare the computed output with the expected output (ground truth). A difference means the model erred and its parameters need adjusting; that difference is the loss (PDF p. 621).
2. Work out how much each trainable parameter contributed to the mistake. That quantity is the gradient, computed mathematically as the derivative of the loss with respect to each trainable parameter. There is one gradient value per trainable parameter. A high gradient means the parameter contributes a lot to the loss and should be adjusted more (PDF p. 621).
3. Adjust the trainable parameters using their gradients. How much to move each parameter for a given gradient is decided by the optimizer. Common optimizers are SGD (stochastic gradient descent) and Adam; for transformer-based models Adam is by far the most widely used (PDF p. 621).

The book illustrates the forward and backward pass with a deliberately tiny network (three parameters and one nonlinear activation function) in Figure 7-4, which sits on the following page.

## Why it matters
Because each trainable parameter carries its gradient and its optimizer states during the backward pass, more trainable parameters means more memory to store these extra values (stated on the next page, where the figure appears). This is why reducing the number of trainable parameters reduces finetuning memory, the motivation for PEFT noted in C07-007.

## Relations
Feeds the training-memory formula in C07-009 and the PEFT techniques discussed later in the chapter.
