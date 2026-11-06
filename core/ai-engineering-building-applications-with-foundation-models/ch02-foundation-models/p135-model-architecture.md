---
id: C02-005
title: Model Architecture
source_pages: "135-150"
chapter: 2
concepts: [transformer, seq2seq, attention-mechanism, prefill-decode, multi-head-attention, transformer-block, state-space-models, mamba, jamba, rwkv]
related: [C02-006, C02-011, C09-002, C09-006]
time_sensitive: true
---
# Model Architecture
(Source: PDF pp. 135-150)

## What the section covers
This opens the "Modeling" part of Chapter 2. Before training, developers must settle what the model looks like: its architecture and its parameter count. These choices shape capabilities and also downstream usability; for instance a 7B-parameter model is far easier to deploy than a 175B one, and optimizing a transformer for latency differs from optimizing a different architecture (PDF p. 135). The section analyses the transformer and its alternatives, and the author warns it is technically dense and may be skipped where it gets too deep (PDF p. 135).

## Meaning

**Transformer.** The dominant architecture for language foundation models at the time of writing (Vaswani et al., 2017), built on the attention mechanism. It fixed many weaknesses of earlier architectures, though it has its own limitations (PDF p. 135).

**Seq2seq.** The predecessor that the transformer rose after. Introduced in 2014, it improved machine translation and summarization markedly; Google put it in Google Translate in 2016 and claimed the "largest improvements to date for machine translation quality" (PDF p. 136). It has an encoder that reads the input and a decoder that produces the output, both sequences of tokens, and both implemented as RNNs. In the basic form the encoder consumes input tokens one after another and emits a final hidden state representing the whole input; the decoder then emits output tokens one at a time, conditioned on that final hidden state and the previously generated token (PDF p. 136).

**Attention.** A mechanism letting the model weigh the importance of different input tokens while generating each output token (PDF p. 138).

**Prefill and decode.** The two steps of transformer-based language model inference (PDF pp. 138-139).

## Why it matters
Architecture determines how costly it is to run a model and how well it handles long inputs. The parallel nature of prefill and the sequential nature of decode motivate many techniques that make inference cheaper and faster, covered in Chapter 9 (PDF p. 139). The memory needed for key and value vectors is one reason it is hard to extend context length for transformers (PDF p. 141). And model dimensions (layers, hidden size, feedforward size, vocabulary) determine model size (PDF p. 145).

## How it works

### Problems with seq2seq that the transformer addresses
1. The vanilla decoder generates outputs from only the final hidden state of the input. The book likens this to answering questions about a book using just its summary, which limits output quality (PDF p. 137).
2. RNN encoder and decoder both work sequentially, so processing is slow for long sequences: with a 200-token input, each token must finish before the next starts (PDF p. 137).

The transformer answers both with attention: like answering by consulting any page of the book (PDF p. 138). Figure 2-4 contrasts seq2seq (top) and transformer (bottom); for the transformer, arrows show which tokens the decoder attends to when producing each output token (PDF p. 137). In the rendered figure both halves translate "How are you ?" into Spanish ("¿ Como estas ?"). In the seq2seq half the input tokens are chained left to right into a single "Final hidden state" box, and every output token is fed from that one box. In the transformer half there is no such bottleneck: the output tokens receive differently coloured arrows from different input tokens (for example "How" feeds "Como" and "¿"), so each output token draws on selected inputs (PDF p. 137).

Note from the book: attention predates the transformer by three years and can be used with other architectures; Google used it with seq2seq in 2016 for GNMT. It took off only after the transformer paper showed attention works without RNNs (PDF p. 138).

The transformer drops RNNs entirely, so input tokens can be processed in parallel, greatly speeding input processing. Yet autoregressive transformer language models keep a sequential output bottleneck (PDF p. 138).

### Inference in two steps
- **Prefill:** the model processes input tokens in parallel, building the intermediate state needed to produce the first output token. That state includes the key and value vectors for all input tokens (PDF pp. 138-139).
- **Decode:** the model generates one output token at a time (PDF p. 139).

### Attention mechanism: Q, K, V
Attention uses query, key and value vectors (PDF p. 139):
- The query vector (Q) is the decoder's current state at each decoding step; in the book analogy it is the person looking for information to write a summary (PDF p. 139).
- Each key vector (K) represents a previous token, like a page number. Previous tokens include both input tokens and tokens already generated (PDF pp. 139-140).
- Each value vector (V) is the actual content of a previous token as learned by the model, like the page's content (PDF p. 140).

How much attention a token receives is computed as a dot product between the query vector and that token's key vector. A high score means more of that token's value vector is used in the output (PDF p. 140). Figure 2-5 shows an example where the query seeks information from the previous tokens "How, are, you, ?, ¿" to produce the next token, beside the well-known diagram from "Attention Is All You Need" (PDF pp. 140-141). In the rendered figure, the left panel is the paper's block diagram (Q and K go into a MatMul, then Scale, optional Mask, SoftMax, and a final MatMul that also takes V). The right panel shows the previous tokens producing a row of value vectors (V1..Vt-1) and a row of key vectors (K1..Kt-1); the query vector Q_t is multiplied with the keys, the result is multiplied with the values, and the output is the next token "Como" (PDF p. 141).

Since every previous token has its own key and value vector, longer sequences need more of them computed and stored, which is a reason context length is hard to extend. Efficient computation and storage of these vectors returns in Chapters 7 and 9 (PDF p. 141).

**Computing the vectors.** Given input x, with W_K, W_V, W_Q the key, value and query matrices (PDF pp. 141-142):

    K = x W_K
    V = x W_V
    Q = x W_Q

These matrices match the model's hidden dimension. In Llama 2-7B the hidden dimension is 4096, so each matrix is 4096 x 4096 and each resulting K, V, Q vector has dimension 4096 (PDF p. 142).

**Multi-head attention.** Attention is almost always multi-headed, which lets the model attend to different groups of previous tokens at once. Q, K and V are split into smaller vectors, one per head. Llama 2-7B has 32 heads, so each of K, V, Q is split into 32 vectors of dimension 128, because 4096 / 32 = 128 (PDF p. 142).

**Attention function** (as printed and read from the rendered page):

    Attention(Q, K, V) = softmax( Q K^T / sqrt(d) ) V

Here K^T is the transpose of K. The book does not define d anywhere on this page (the rendered page shows only the formula, with sqrt(d) under QK^T). The surrounding text only says the vectors are split into per-head vectors of dimension 128 in Llama 2-7B (PDF p. 142).
INTERPRETATION: d is the per-head key dimension (128 in the Llama 2-7B example), following the usual convention; this is not stated by the book.

Outputs of all heads are concatenated; an output projection matrix then applies a further transformation before the result goes to the next computation step. The output projection matrix has the same dimension as the model's hidden dimension (PDF pp. 142-143).

### Transformer block
A transformer is a stack of transformer blocks. Contents vary by model, but generally each block holds an attention module and an MLP (multi-layer perceptron) module (PDF p. 143):
- **Attention module:** four weight matrices: query, key, value and output projection (PDF p. 143).
- **MLP module:** linear layers separated by nonlinear activation functions. Each linear layer is a weight matrix doing a linear transformation (also called a feedforward layer); the activation lets the layers learn nonlinear patterns (PDF p. 143). Common activations named are ReLU (Agarap, 2018) and GELU (Hendrycks and Gimpel, 2016); the book's sentence says GELU "was used by GPT-2 and GPT-3, respectively", which is worded oddly for a single function and is reported as printed (PDF p. 143). ReLU simply turns negative values into 0: ReLU(x) = max(0, x) (PDF p. 144).

The number of blocks is usually called the model's number of layers (PDF p. 144). Two modules sit outside the blocks (PDF p. 144):
- **Embedding module (before the blocks):** an embedding matrix and a positional embedding matrix, converting tokens and their positions to embedding vectors. Naively, the number of position indices fixes maximum context length (a model tracking 2,048 positions has a 2,048 maximum context), though techniques exist that extend context without adding position indices (PDF p. 144).
- **Output layer (after the blocks):** maps output vectors to token probabilities used to sample outputs (sampling is discussed later in the chapter). Typically one matrix, called the unembedding layer; some call it the model head, as the last layer before generation (PDF p. 144).

### What sets model size
Figure 2-6 shows the weight composition of a transformer: input goes to an embedding module (with a positional embedding feeding in), then N transformer blocks (each an Attention part with Q, K, V and O matrices and an MLP part with two feedforward matrices FF1 and FF2), then the output layer. Its legend gives the weight shapes: Q, K, V, O are d_model x d_model; FF1 is d_model x d_ff; FF2 is d_ff x d_model; embedding is V x d_model; positional embedding is C x d_model; output is d_model x V, where d_model is the hidden size, d_ff the feedforward dimension, V the vocabulary size and C the number of position indices tracked (PDF p. 145). Size depends on (PDF p. 145): the model dimension (sizes of key, query, value and output projection matrices); the number of transformer blocks; the feedforward layer dimension; and the vocabulary size. Larger values mean larger models (PDF p. 146). Context length affects memory footprint but not the total parameter count (PDF p. 146).

Table 2-4 (PDF p. 146) lists transformer blocks / model dim / feedforward dim / vocabulary (the last column header is clipped to "Voca" in the rendered page, and the "128K" cells are clipped at the edge; UNVERIFIED: the header is read as vocabulary size, inferred from the vocabulary-size item in the preceding list and the 32K/128K values; the figures themselves are legible):
- Llama 2-7B: 32 / 4,096 / 11,008 / 32K
- Llama 2-13B: 40 / 5,120 / 13,824 / 32K
- Llama 2-70B: 80 / 8,192 / 22,016 / 32K
- Llama 3-7B: 32 / 4,096 / 14,336 / 128K
- Llama 3-70B: 80 / 8,192 / 28,672 / 128K
- Llama 3-405B: 126 / 16,384 / 53,248 / 128K

(The book labels the first Llama 3 row "Llama 3-7B" as printed.)

## Alternatives and trade-offs: other architectures
Since AlexNet revived deep learning in 2012, architectures have come and gone. Seq2seq was in the spotlight for four years (2014-2018); GANs a bit longer (2014-2019). The transformer has lasted since 2017 (PDF pp. 146-147). Displacing it is hard because it has been heavily optimized since 2017; a challenger must perform at the scale and on the hardware people care about (PDF p. 147). Still, several alternatives are gaining traction (PDF p. 147):

- **RWKV** (Peng et al., 2023): an RNN-based model that can be parallelized for training. Being an RNN, it theoretically lacks the transformer's context length limit, but having no limit does not guarantee good long-context performance (PDF p. 147).
- **State space models (SSMs)** (Gu et al., 2021a): modelling long sequences is a core LLM challenge, and SSMs show promise for long-range memory. Since 2021 various techniques made them more efficient, better with long sequences and scalable (PDF pp. 147-148):
  - **S4** (Gu et al., 2021b): made SSMs more efficient (PDF p. 148).
  - **H3** (Fu et al., 2022): adds a mechanism to recall early tokens and compare tokens across sequences, similar in purpose to attention but more efficient (PDF p. 148).
  - **Mamba** (Gu and Dao, 2023): scales SSMs to 3 billion parameters. Mamba-3B beats same-size transformers and matches ones twice its size on language modelling. Inference computation scales linearly with sequence length, versus quadratic for transformers, and performance improves on real data up to million-length sequences (PDF p. 148).
  - **Jamba** (Lieber et al., 2024): interleaves transformer and Mamba blocks to scale further. The released mixture-of-experts model has 52B total parameters (12B active), designed to fit one 80 GB GPU. It does well on standard benchmarks and long-context evaluations up to 256K tokens, with a small memory footprint relative to vanilla transformers (PDF pp. 148-149).

Figure 2-7 (PDF p. 150) shows, in panel (a), a Jamba block that stacks, from bottom to top, Mamba, Mamba MoE, Mamba, Mamba MoE, Transformer, Mamba MoE, Mamba, Mamba MoE layers (one transformer layer among seven Mamba-type layers); panel (b) shows four layer types (Transformer layer, Attention MoE layer, Mamba layer, Mamba MoE layer), each built from RMSNorm, then Attention or Mamba, then MLP or MoE, with residual (skip) connections around each sub-step. Panel contents were read from the rendered page.

## Relations and implications
Given the transformer's many limitations, there is strong incentive to beat it. If another architecture overtakes it, some adaptation techniques in the book could change; but just as moving from ML engineering to AI engineering left many things unchanged, a new underlying architecture would not alter the fundamental approaches (PDF p. 149).

Related sections: model size (C02-006), sampling and the output layer (C02-011), inference and its optimization (C09-002, C09-006).

## Time-sensitive statements
"Dominant architecture" status of the transformer, the list of emerging alternatives (RWKV, S4, H3, Mamba, Jamba), their reported scale and results, and the Llama model dimension values in Table 2-4 reflect the date of writing (PDF pp. 135, 147-149, 146).
