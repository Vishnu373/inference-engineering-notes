## LLM Phases

- Prefill -> process each input token and store its attention in KV cache. | Parallel operation
- Decode -> generate output tokens autoregressively. | Sequential operation

Note: Autoregressive -> predicting each token based on preceding tokens.

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

## Attention
- Mechanism by which each token computes a weighted sum over all other tokens.
 - where the weights determine how relevant each token is to the current one.

Attention takes in 3 inputs:
- Queries (Q) -> 
- Keys (K) ->
- Values (V) -> 

Two main types of attention:
- Self attention ->
- Cross attention -> 