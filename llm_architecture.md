## LLM Phases

- Prefill -> process each input token and store its attention in KV cache. | Parallel operation, Compute bound
- Decode -> generate output tokens autoregressively. | Sequential operation, Memory bound

Note: 
Autoregressive -> predicting each token based on preceding tokens.
Compute-bound -> CPU or GPU is the bottleneck | it does the calculations.
Memory-bound -> Reading data from memory (system RAM or VRAM) is the bottleneck. | data transfer.

## Model Name Breakdown

- Model family name (e.g. Qwen, Gemma, Llama)
- Version number (e.g. Qwen3 = version 3, Gemma4 = version 4)
- Model size (e.g. 8B = 8 billion parameters, 12B = 12 billion)
- Architecture type/variant
  - Type: MoE (mixture of experts), Dense
  - Variant/fine-tune intent: base (pretrained, no fine-tuning), instruct (follows instructions), chat (conversation), quantized (compressed for efficiency)

## LLM Model Layers

- Embedding layer -> converts tokens into vectors
- Transformer layer -> processes and contextualizes token representations
  - Attention
  - Feed forward network
  - Normalization
- Output layer (LM head) -> converts transformer hidden states into a vector of logits for each token
