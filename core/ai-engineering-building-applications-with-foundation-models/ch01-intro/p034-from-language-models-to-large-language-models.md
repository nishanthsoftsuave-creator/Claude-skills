---
id: C01-002
title: From Language Models to Large Language Models
source_pages: "34-43"
chapter: 1
concepts: [language-model, token, tokenization, vocabulary, masked-language-model, autoregressive-language-model, completion, self-supervision, supervision, llm-scale]
related: [C01-001, C01-003, C01-004]
time_sensitive: true
---
# From Language Models to Large Language Models
(Source: PDF pp. 34-43; the closing paragraphs of the section sit on PDF p. 44)

## What the section covers
The first part of "The Rise of AI Engineering". It explains what a language model is, tokens and vocabularies, the two kinds of language model (masked and autoregressive), the completion view of language models, and why self-supervision let language models scale up into LLMs, including how "large" is defined and why larger models need more data.

## Framing
Foundation models grew out of LLMs, which grew out of language models. Products like ChatGPT and GitHub Copilot look sudden but are the culmination of decades of progress, with the first language models appearing in the 1950s (PDF p. 34). Language models have existed for a long time; they reached today's scale only thanks to self-supervision. The author says readers already familiar with these ideas may skip ahead (PDF p. 34).

## Meaning: language models
- A language model encodes statistical information about one or more languages, essentially how likely a word is to appear in a given context. Given "My favorite color is __", a model of English should predict "blue" more often than "car" (PDF p. 34).
- Historical roots: the statistical nature of language was noticed centuries ago. In the 1905 story "The Adventure of the Dancing Men", Sherlock Holmes decodes stick figures by reasoning that the most frequent figure stands for E, the most common English letter. Claude Shannon later applied more sophisticated statistics to decipher enemy messages in the Second World War, and his 1951 paper "Prediction and Entropy of Printed English" introduced concepts, entropy among them, still used in language modeling (PDF p. 35).
- Early models covered a single language; today a language model can involve several (PDF p. 35).

## Meaning: tokens, tokenization, vocabulary
- The basic unit of a language model is the token, which may be a character, a word or a part of a word such as "-tion", depending on the model (PDF p. 35).
- Example (Figure 1-1): GPT-4 splits a short phrase about building AI applications into nine tokens, with "can't" becoming two tokens, "can" and "'t". The rendered figure actually shows the phrase as "I can't wait to build awesome AI applications" (nine tokens when counted), whereas the running text quotes it without "awesome", a minor inconsistency in the book (PDF p. 35). The book also points to OpenAI's website for seeing how different OpenAI models tokenize text (PDF p. 35).
- Tokenization is the process of breaking text into tokens. For GPT-4 an average token is about three quarters of a word, so 100 tokens is roughly 75 words (PDF p. 36).
- The model's vocabulary is the set of all tokens it can work with. A small number of tokens can build many words, like letters in an alphabet. Mixtral 8x7B has a vocabulary of 32,000 and GPT-4 of 100,256. Model developers choose the tokenization method and vocabulary size (PDF p. 36).
- Why tokens instead of words or characters (PDF p. 36):
  1. Unlike characters, tokens let a model split words into meaningful parts; "cooking" becomes "cook" and "ing", each carrying part of the meaning.
  2. There are fewer unique tokens than unique words, which shrinks the vocabulary and makes the model more efficient (the book defers detail to Chapter 2).
  3. Tokens help with unknown words; an invented word like "chatgpting" could split into "chatgpt" and "ing", exposing its structure.
  Tokens thus sit between words (fewer units than words) and characters (more meaning than single characters).

## Meaning: two types of language model
Both differ in which context they may use to predict a token (PDF pp. 36-37).
- Masked language model: trained to predict missing tokens anywhere in a sequence using context from both sides, in effect fill-in-the-blank. Given "My favorite __ is blue" it should say "color". BERT (Devlin et al., 2018) is the well-known example. At the time of writing, masked models are commonly used for non-generative tasks like sentiment analysis and text classification, and for tasks needing overall context, such as code debugging, where a model must read both the code before and after to find errors (PDF p. 37).
- Autoregressive language model: trained to predict the next token using only the preceding tokens, e.g. what follows "My favorite color is __". It can keep generating one token after another. Today autoregressive models are the choice for text generation and are far more popular than masked models (PDF pp. 37-38).
- Figure 1-2 shows both: the autoregressive model, given "Why does the chicken cross the", predicts the next token from a context labelled "previous tokens only", while the masked model, given "Why does the [prediction] cross the road", predicts the blank in the middle from a context labelled "surrounding tokens", i.e. both sides (PDF p. 38).
- Convention: unless stated otherwise, the book uses "language model" to mean an autoregressive model (PDF p. 38).
- Output is open-ended: with a fixed, finite vocabulary a model can build infinitely many outputs. A model that can produce open-ended outputs is called generative, hence generative AI (PDF p. 38).

## How it works: completion
- A language model can be seen as a completion machine: given text (the prompt), it tries to complete it. Prompt "To be or not to be" yields a completion like ", that is the question." (PDF p. 39).
- Completions are predictions based on probabilities and are not guaranteed correct. This probabilistic nature is what makes the models both exciting and frustrating; it is explored further in Chapter 2 (PDF p. 39).
- Many tasks can be framed as completion: translation, summarization, coding, math. A prompt such as "How are you in French is ..." might be completed with "Comment ça va", which is translation (PDF p. 39). A prompt asking whether an email is spam, followed by the email and "Answer:", might be completed with "Likely spam", turning the model into a spam classifier (PDF pp. 39-40).
- Caveat: completion is not conversation. Asked a question, a pure completion machine may add another question rather than answer. The book defers how to make a model respond properly to a request to its post-training discussion (PDF p. 40).

## Why self-supervision matters
- Language modeling is only one of many ML algorithms (others cover object detection, topic modeling, recommenders, weather forecasting, stock prediction). Language models became the center of the scaling approach behind the ChatGPT moment because they can be trained with self-supervision, whereas many other models need supervision (PDF p. 40).
- Supervision means training on labeled data, which is expensive and slow to obtain. Self-supervision removes this labeling bottleneck, allowing much larger datasets and therefore scale (PDF p. 40).
- With supervision you label examples to show desired behavior and train on them; a fraud detector learns from transactions labeled fraud or not fraud and then predicts on new ones (PDF pp. 40-41).
- Supervision drove 2010s successes. AlexNet (Krizhevsky et al., 2012), which began the deep learning revolution, was supervised: trained on ImageNet to sort over 1 million images into 1,000 categories such as car, balloon or monkey (PDF p. 41).
- Labeling cost example: at 5 cents per image, labeling a million images costs $50,000; having two people label each image for cross-checking doubles it. Scaling to 1 million categories would raise labeling cost alone to $50 million. Everyday-object labeling needs no training and is cheap, but other tasks are harder: Latin translations for an English-to-Latin model cost more, and labeling CT scans for cancer would be astronomical (PDF p. 41).
- In self-supervision the model infers labels from the input itself. Language modeling qualifies because each sequence provides both the labels (tokens to predict) and the contexts used to predict them (PDF p. 42).
- Worked example (Table 1-1): the sentence "I love street food." yields six training samples. Contexts grow step by step from <BOS> alone (output "I"), then <BOS>, I (output "love"), and so on until the context <BOS>, I, love, street, food, "." (output <EOS>). <BOS> and <EOS> mark sequence beginning and end, are needed so a model can handle multiple sequences, and are typically each one special token. The end marker is especially important because it tells the model when to stop its response (PDF pp. 42-43). The six samples correspond to the six rows of the table.
- Self-supervision is not unsupervision: in self-supervised learning labels are inferred from the input, while in unsupervised learning no labels are needed at all (PDF p. 43).
- Because text is everywhere (books, blogs, articles, Reddit comments), enormous training sets can be built without labeling, letting language models scale into LLMs (PDF p. 43).

## Meaning: what counts as "large"
- "LLM" is hardly a scientific term; what is large today may be tiny tomorrow (PDF p. 43).
- Size is usually measured in parameters, variables in an ML model updated during training. Generally, though not always, more parameters mean more capacity to learn desired behavior (PDF p. 43).
- Time-sensitive examples: OpenAI's first GPT in June 2018 had 117 million parameters, considered large; GPT-2 in February 2019 had 1.5 billion, making 117 million look small. At the time of writing, 100 billion parameters counts as large, and this may one day look small (PDF pp. 43-44).

## Why larger models need more data
Larger models have more capacity to learn and therefore need more data to reach their best performance. Training a large model on a small dataset is possible but wastes compute, since a smaller model could achieve similar or better results on that data (PDF p. 44).

## Time-sensitive statements
- Masked models "as of writing" are used mainly for non-generative tasks (PDF p. 37).
- Vocabulary sizes of Mixtral 8x7B and GPT-4, and the ~3/4 words per GPT-4 token (PDF p. 36).
- Parameter-count thresholds for "large" and the GPT and GPT-2 sizes (PDF pp. 43-44).

## Relations
Follows the chapter framing in C01-001 and leads directly into C01-003 (extending LLMs to multiple modalities and foundation models). Tokens and probabilistic outputs are developed further in the book's Chapter 2, and post-training (making models answer requests) later on; C01-004 continues Chapter 1.
