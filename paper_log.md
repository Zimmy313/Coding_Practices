# Paper Log

> One entry per paper. Fill every field — even one line is fine. Consistency beats depth.

---

## How to Fill Each Entry

1. **Before reading** — write the "Problem it solves" line first, from what you already know
2. **While reading** — annotate only key idea, method, one limitation
3. **After reading** — fill the 5 bullets in your own words. No copy-paste.
4. **Connect** — one line linking it to your project or a previous paper
5. **Confidence** — honest self-assessment. Revisit all `Shaky` entries before interviews.

---

## Entries

### [Week 1] BERT (2018)
**Date read:** 27 May 2026
**Block:** Block 1 — Transformer Foundations
**Link:** [arxiv](https://arxiv.org/abs/1810.04805)

**Problem it solves** 
> Addresss unidirectional pretraining by using bidirectional encoder representation. Previous work like ELMo was a shallow concatenation of left and right attention.

**5 key bullets**
1. Trained using Masked language model(MLM): mask out % of words using `[MASK]`.
2. Next Sentence Prediction(NSP): to learn relationships between sentences
   1. Binarised prediction: Sentences A and B and for 50% chance, B is the next sentence.
3. Fine-tuning based model. Model is pre-trained using unlabelled data and then used for all down stream task.
   1. We then fine-tune it using task-specific data. Note that this changes all model parameters.
4. BERT sums 3 embeddings for input: token + segment(A/B) + positional. `[CLS]` indicates the start of the sequence and its final hidden state is used for classification tasks.
   1. BERT can take in a single or a pair of sentences unambiguously. `[SEP]` is used to split the 2 segments. This then gives rise to the segment encoding described above. This format allows BERT to address a range down-stream tasks. 
   2. If there is only one sentence, there will still be a `[SEP]` at the end.

**One limitation or open question**
> Mismatch between pre-trainning and fine-tuning as `[MASK]` do not appear in fine-tuning. Solution is to replace a certain percentage of `[MASK]` using a random token, original or `[MASK]` itself(the percentage is 10, 10, 80 accordingly in the paper).

**Connection**
> Build upon transformer architecture but trained using a new objective function. It uses only the encoder stack.

**Confidence:** `Okay`

### [Week 2] GPT-1 & GPT-2
**Date read:** 3 June 2026
**Block:** Block 1 — Transformer Foundations
**Link:** [paper](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf)

**Problem it solves** 
> GPT-1 shows that a Transformer language model can first be trained on large unlabeled text using a language modelling
> objective, then adapted to supervised downstream task through fine-tuning(with a new objective function). GPT-2 shows 
> that by scaling the model and dataset, the language model can perform many downstream tasks in a zero-shot setting by
> conditioning on natural-language context, without task-specific fine-tuning(Note it does not reject the idea of fine-tuning).

**5 key bullets**
1. Uses multi-layer decoder-only Transformer architecture.
2. BPE for tokenization, balancing word-level efficiency and character-level flexibility **HOW???**
3. GPT-2 shows that a single language model trained only on next-token prediction can perform many downstream tasks zero-shot, when the task is expressed through context or natural-language prompts.
   1. $P(u_i \mid u_{i-k}, \ldots, u_{i-1}; \Theta)$
4. GPT-1 uses supervised fine-tuning after pretraining. Its fine-tuning objective combines the supervised task loss with an auxiliary language modeling loss: $L3 = L2 + λL1$. 
   1. Note that L1 is language modelling(point 3.1) while L2 is task specific objective function.
5. GPT-1: self-supervised pretraining + supervised fine-tuning; GPT-2: self-supervised language modeling(mordern terminology) + zero-shot downstream evaluation.

**One limitation or open question**
> GPT-2 performs relatively poorly on the 1 Billion Word Benchmark because the benchmark is heavily preprocessed and sentence-shuffled, removing long-range context that GPT-2 is designed to exploit.

**Connection**
> GPT-1 connects Transformer decoders to transfer learning in NLP. GPT-2 connects scaling language models with zero-shot multitask behavior, showing that many supervised tasks can be reframed as conditional text generation.

**Confidence:** `Okay`


--- 

## Questions
> what is the difference between encoder and decoder archetecure in terms of functionality. Why GPT uses only decoder?

Encoder:

- Every token can attend to every other token, both left and right.
- Designed for understanding - you have the full input, you want the richest representation possible. 
- Sees the whole sentence at onece, nothing to predict next.

Decoder:

- Only knows the previous/past words and predict the next one.
- Mordern GPT's are almost exclusively decoder only.
- Scales much better.
