# Inference Engineering Notes

A comprehensive guide to understanding **inference engineering** — the science and practice of deploying AI models efficiently in production at scale.

## 📝 Credits

[Baseten](https://www.baseten.co/inference-engineering/)

I am preparing these notes by going through the inference engineering book by Philip Kiely @ Baseten and using AI to summarize/simplify and prepare cheatsheets.

## 📚 Contents

- **[basics.md](basics.md)** - Core concepts, techniques, and frameworks for inference engineering
- **[prerequistes.md](prerequistes.md)** - 5 critical questions to ask before building inference systems
- **[fine_tuning.md](fine_tuning.md)** - Adapting pre-trained models for specific use cases
- **[distillation.md](distillation.md)** - Teaching smaller models to behave like larger ones
- **[llm_performance_metrics.md](llm_performance_metrics.md)** - TTFT, TPS, percentiles, and end-to-end latency metrics
- **[neural_networks.md](neural_networks.md)** - How neural networks work: layers, weights, biases, forward pass, and backpropagation
- **[matrix_multiplication.md](matrix_multiplication.md)** - How matrix multiplication works and why it is the core operation behind every neural network layer
- **[activation_function.md](activation_function.md)** - ReLU, Sigmoid, Tanh, and Softmax — what they do, where to use them, and their tradeoffs
- **[llm_inference_mechanism.md](llm_inference_mechanism.md)** - Tokens, tokenization, and how LLMs process and generate text step by step
- **[llm_architecture.md](llm_architecture.md)** - LLM phases, model name breakdown and llm model layers
- **[attention.md](attention.md)** - How attention works: relevance scores, queries, keys, values, and multi-head attention
- **[kv_cache.md](kv_cache.md)** - How the KV cache works: storing past key-value pairs to avoid recomputing attention on every token
- **[mixture_of_experts_models.md](mixture_of_experts_models.md)** - MoE architecture: sparse expert routing, gating networks, and why MoE models are efficient at scale
- **[model_evaluation.md](model_evaluation.md)** - Evaluating model intelligence: correctness, consistency, and reliability for your use case
- **[image_generation_models.md](image_generation_models.md)** - How image generation models work: diffusion pipeline, latent space, guidance scale, and LLM-style generation
- **[inference_bottlenecks.md](inference_bottlenecks.md)** - Compute-bound vs memory-bound workloads, batching, GPU ops:byte ratio, and arithmetic intensity

## 🧪 Hands-on

- **[hands-on/llm-performance-metrics/](hands-on/llm-performance-metrics/)** - Measure real TTFT and total latency against a live LLM, then visualize P50/P90/P95/P99 percentiles across short and medium prompts
- **[hands-on/matrix-multiplication/](hands-on/matrix-multiplication/)** - Multiply two matrices using NumPy and verify output dimensions

## ⚙️ Setup

### matrix-multiplication

```bash
cd hands-on/matrix-multiplication

python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS / Linux

pip install -r requirements.txt
python matmul.py
```

### llm-performance-metrics

Requires a virtual environment, dependencies, and an OpenRouter API key:

```bash
cd hands-on/llm-performance-metrics

python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # macOS / Linux

pip install -r requirements.txt
```

Add your API key to a `.env` file in the same folder:

```
OPENROUTER_API_KEY=your_key_here
```

Then run:

```bash
python measure.py     # collect latency data → results.csv
python visualize.py   # plot histograms and CDFs
```
