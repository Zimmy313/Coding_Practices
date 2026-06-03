# MLE Paper Reading List
> One paper per week. After each paper: write 5 bullets in your own words, note one limitation, connect it to your project or a prior paper.

---

## Block 1 — Transformer Foundations (Weeks 1–6)

| Week | Paper | Core Takeaway | Link |
|------|-------|---------------|------|
| 1 | Attention is All You Need (2017) | Transformer architecture cold — attention as soft lookup over learned key-value store | [arxiv](https://arxiv.org/abs/1706.03762) |
| 2 | BERT (2018) | Pretraining paradigms, bidirectionality, masked language modeling | [arxiv](https://arxiv.org/abs/1810.04805) |
| 3 | GPT-2 (2019) | Autoregressive language modeling, zero-shot task transfer | [paper](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) |
| 4 | GPT-3 (2020) | Scale, in-context learning, emergence at scale | [arxiv](https://arxiv.org/abs/2005.14165) |
| 5 | Chinchilla (2022) | Compute-optimal training, scaling laws for model and data size | [arxiv](https://arxiv.org/abs/2203.15556) |
| 6 | FlashAttention (2022) | Memory-efficient attention, IO complexity, hardware-aware algorithms | [arxiv](https://arxiv.org/abs/2205.14135) |
| 6b | FlashAttention-2 (2023) | Parallelism improvements, ~2x speedup over v1, now the de facto standard in most training stacks | [arxiv](https://arxiv.org/abs/2307.08691) |

---

## Block 2 — Alignment and Fine-tuning (Weeks 7–12)

| Week | Paper | Core Takeaway | Link |
|------|-------|---------------|------|
| 7 | InstructGPT / RLHF (2022) | Full alignment pipeline — SFT, reward modeling, PPO loop | [arxiv](https://arxiv.org/abs/2203.02155) |
| 8 | PPO — Proximal Policy Optimization (2017) | Policy gradient stabilization via clipping objective | [arxiv](https://arxiv.org/abs/1707.06347) |
| 8b | GRPO — Group Relative Policy Optimization (2024) | PPO alternative used in DeepSeek-R1; eliminates critic model, uses group reward baseline — increasingly common in open-source RLHF pipelines | [arxiv](https://arxiv.org/abs/2402.03300) |
| 9 | DPO — Direct Preference Optimization (2023) | Why it replaces RLHF, simpler alignment without reward model | [arxiv](https://arxiv.org/abs/2305.18290) |
| 10 | LoRA (2021) | Parameter-efficient fine-tuning via low-rank decomposition | [arxiv](https://arxiv.org/abs/2106.09685) |
| 11 | QLoRA (2023) | Quantized fine-tuning, 4-bit precision, practical PEFT on consumer hardware | [arxiv](https://arxiv.org/abs/2305.14314) |
| 12 | LLaMA 3 technical report (2024) | Updated open-source reference architecture — training data quality at scale, GQA, extended context, instruction tuning decisions end to end | [arxiv](https://arxiv.org/abs/2407.21783) |

---

## Block 3 — Retrieval and Agents (Weeks 13–18)

| Week | Paper | Core Takeaway | Link |
|------|-------|---------------|------|
| 13 | RAG — Retrieval-Augmented Generation (2020) | Grounding generation in retrieved documents, dense passage retrieval | [arxiv](https://arxiv.org/abs/2005.11401) |
| 13b | Chain-of-Thought Prompting (2022) | Emergent reasoning via intermediate steps — foundational for everything in the reasoning/agents space that follows | [arxiv](https://arxiv.org/abs/2201.11903) |
| 14 | ReAct (2022) | Reasoning + acting loop, interleaving chain-of-thought with tool use — foundational pattern, though modern agents have moved well beyond this | [arxiv](https://arxiv.org/abs/2210.03629) |
| 15 | Self-Consistency (2022) | Ensemble reasoning via majority vote over multiple samples, consistency as a signal | [arxiv](https://arxiv.org/abs/2203.11171) |
| 16 | Toolformer (2023) | How models learn to use APIs/tools in a self-supervised way | [arxiv](https://arxiv.org/abs/2302.04761) |
| 17 | HyDE (2022) | Hypothetical document embeddings — generate then retrieve, improves retrieval quality | [arxiv](https://arxiv.org/abs/2212.10496) |
| 18 | REALM (2020) | Retrieval during pretraining, deeper theoretical grounding for RAG | [arxiv](https://arxiv.org/abs/2002.08909) |

---

## Block 4 — Evaluation (Weeks 19–24)
> Most directly relevant to your wiki grading project.

| Week | Paper | Core Takeaway | Link |
|------|-------|---------------|------|
| 19 | LLM-as-a-Judge (2023) | Using LLMs for evaluation, positional bias, verbosity bias, failure modes | [arxiv](https://arxiv.org/abs/2306.05685) |
| 20 | Prometheus (2023) | Specialized open-source eval model, fine-tuned for rubric-based scoring | [arxiv](https://arxiv.org/abs/2310.08491) |
| 21 | RAGAS (2023) | RAG evaluation framework — faithfulness, answer relevancy, context precision | [arxiv](https://arxiv.org/abs/2309.15217) |
| 22 | BERTScore (2019) | Semantic similarity for text evaluation using contextual embeddings | [arxiv](https://arxiv.org/abs/1904.09675) |
| 23 | On Calibration of Modern Neural Networks (2017) | Confidence vs accuracy, temperature scaling, when to trust model scores | [arxiv](https://arxiv.org/abs/1706.04599) |
| 24 | FActScore (2023) | Factual precision in long-form generation, atomic fact checking | [arxiv](https://arxiv.org/abs/2305.14251) |

---

## Block 5 — Production and Systems (Weeks 25–32)

| Week | Paper | Core Takeaway | Link |
|------|-------|---------------|------|
| 25 | Megatron-LM (2019) | Tensor parallelism, how large models are split across GPUs | [arxiv](https://arxiv.org/abs/1909.08053) |
| 26 | DeepSpeed ZeRO (2020) | Memory optimization via partitioning, distributed training foundations | [arxiv](https://arxiv.org/abs/1910.02054) |
| 27 | vLLM / PagedAttention (2023) | Production serving, KV cache management, throughput at scale | [arxiv](https://arxiv.org/abs/2309.06180) |
| 28 | Speculative Decoding (2023) | Inference speedup via draft-then-verify, latency reduction | [arxiv](https://arxiv.org/abs/2302.01318) |
| 29 | GPTQ (2022) | Post-training quantization to 4-bit, accuracy-efficiency tradeoff | [arxiv](https://arxiv.org/abs/2210.17323) |
| 30 | Switch Transformer / Mixtral (2021/2024) | Mixture of Experts architecture, sparse computation, routing | [Switch](https://arxiv.org/abs/2101.03961) / [Mixtral](https://arxiv.org/abs/2401.04088) |
| 31 | Orca — Continuous Batching (2022) | Iteration-level scheduling, serving throughput optimization | [usenix](https://www.usenix.org/conference/osdi22/presentation/yu) |
| 31b | Scaling LLM Test-Time Compute (2024) | The theoretical grounding for o1/o3-style reasoning — spending more compute at inference rather than training, best-of-N, process reward models | [arxiv](https://arxiv.org/abs/2408.03314) |
| 32 | Hidden Technical Debt in ML Systems (Google, 2015) | Production ML reality — entanglement, pipeline debt, monitoring | [paper](https://papers.nips.cc/paper_files/paper/2015/hash/86df7dcfd896fcaf2674f757a2463eba-Abstract.html) |

---

## Block 6 — Frontier / Electives (Week 33+)
> Choose based on where your interests land by this point.

| Paper | Direction | Link |
|-------|-----------|------|
| **DeepSeek-R1 (2025)** ⭐ | Reasoning models, GRPO in practice, open-source o1 equivalent — the most important 2025 paper to read | [arxiv](https://arxiv.org/abs/2501.12948) |
| Mamba — Linear-Time Sequence Modeling (2023) | If transformer limitations interest you — SSMs as alternative *(intellectually interesting but hasn't displaced transformers in practice; treat as truly optional)* | [arxiv](https://arxiv.org/abs/2312.00752) |
| CodeBERT (2020) | If coding/software engineering applications interest you | [arxiv](https://arxiv.org/abs/2002.08155) |
| CLIP (2021) | If multimodal / vision-language interests you | [arxiv](https://arxiv.org/abs/2103.00020) |
| LLaVA (2023) | Multimodal instruction tuning, visual + language | [arxiv](https://arxiv.org/abs/2304.08485) |
| Constitutional AI (Anthropic, 2022) | Deeper alignment theory, self-critique and revision | [arxiv](https://arxiv.org/abs/2212.08073) |
| AlphaCode (2022) | LLMs for competitive programming, code generation at scale | [arxiv](https://arxiv.org/abs/2203.07814) |

---

## How to Read Each Paper

1. **Before** — one sentence: what problem does this claim to solve?
2. **During** — annotate key idea, method, one limitation only
3. **After** — 5 bullets in your own words into your paper log
4. **Connect** — one line: how does this relate to your project or a prior paper?

> Your paper log (80 papers × 5 bullets) becomes your interview revision sheet. Reviewable in 2 hours before any interview.
