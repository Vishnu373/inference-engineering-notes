Tokens:
A token is the basic unit of text that an LLM processes. Not exactly a word — more like a chunk of text.
Examples:

"hello" → 1 token
"inference" → 1 token
"unbelievable" → might be 3 tokens (un, believ, able)
" the" → 1 token (space included)

Rule of thumb: 1 token ≈ 0.75 words. So 100 words ≈ 133 tokens.


Three main approaches:

BPE (Byte Pair Encoding) → used by GPT models
WordPiece → used by BERT
SentencePiece → used by LLaMA, T5

All three do roughly the same thing — build a vocabulary of subword chunks from training data. The difference is in how they decide which chunks to merge.

Tokenizer:-
A tokenizer is just a simple lookup table with two operations:

Encode → text to IDs
Decode → IDs back to text

No neural network, no learning. Just string-to-integer mapping.


Inference involves two or three sequences of tokens:
**Input sequence** → everything you send to the model. Your prompt, chat history, system instructions, available tools. All gets tokenized and fed in.

**Reasoning sequence** → only in reasoning models (like DeepSeek R1, o1). The model thinks out loud internally before answering. You sometimes see this as the "thinking" block. Optional — not all models do this.

**Output sequence** → the actual response generated back to you. What you see as the final answer.

So the context window is the total budget for all three sequences combined.

Input + Reasoning + Output must all fit within that limit. If your input is huge, you have less room for output. max_tokens is just an extra cap specifically on the output sequence — a way to control cost and response length per request.

Primary phases of inference:
Prefill → process the entire input sequence at once, calculate attention for all input tokens, store in KV cache
Decode → generate output tokens one by one using those cached values.

Example:-

Query: "What is the capital of France?"

**Prefill:**
Model reads your entire question, understands it, saves that understanding in KV cache.

**Decode — generating "Paris":**
- Step 1 → model looks at cached understanding of your question, predicts first token "Par"
- Step 2 → model looks at cache + "Par", predicts "is"
- Step 3 → model looks at cache + "Paris", predicts end of sentence

Each step it reads from cache instead of re-reading your original question from scratch. Cache = saved understanding of everything that came before.