## LLM Phases

- Prefill -> process each input token and store its attention in KV cache | parallel operation, compute-bound
- Decode -> generate output tokens autoregressively | sequential operation, memory-bound

Definitions:
- Autoregressive -> predicting each token based on all preceding tokens
- Compute-bound -> GPU/CPU processing power is the bottleneck (calculations are the slow step)
- Memory-bound -> reading data from VRAM is the bottleneck (data transfer speed is the slow step)

## Model Name Breakdown

- Family name -> e.g. Qwen, Gemma, Llama
- Version number -> e.g. Qwen3 = version 3, Gemma4 = version 4
- Model size -> e.g. 8B = 8 billion parameters
- Architecture type
  - Dense -> all parameters active for every token
  - MoE -> mixture of experts, only a subset of parameters active per token
- Fine-tune variant
  - base -> pretrained only, no instruction tuning
  - instruct -> tuned to follow instructions
  - chat -> tuned for conversation
  - quantized -> compressed for memory efficiency

## LLM Model Layers

- Embedding layer -> converts tokens into vectors
- Transformer layer -> processes and contextualizes token representations
  - Attention -> lets each token attend to other tokens in context
  - Feed-forward network -> per-token transformation after attention
  - Normalization -> stabilizes training and activations
- Output layer (LM head) -> converts final hidden state into logits over the vocabulary
