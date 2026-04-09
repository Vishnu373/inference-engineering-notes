# Inference Engineering Fundamentals

**Inference** is when an AI model actually responds to a user. Not training, not research — just the model doing its job in production. Turns out, doing this at scale is genuinely hard. Here's everything that goes into it.

## The 3 Layers

Running AI in production needs 3 things working together:

- **Runtime** → one machine working well
- **Infrastructure** → many machines working well together  
- **Tooling** → engineers can manage it all easily

Miss one, the whole system struggles.

## Model Performance Techniques

### 1. Batching

Don't serve one user at a time when you can serve 100 together. It's the bus strategy — don't run a taxi for every passenger. Fill the bus, drive once.

### 2. Caching (KV Cache for LLMs)

Every time an LLM generates a new word, it needs context of ALL previous words.

- **Without KV Cache** → recompute everything from scratch at every single step
- **With KV Cache** → store the Key/Value vectors of previous tokens, only compute the new one

Like writing notes while reading a book instead of re-reading from page 1 every time you turn a page.

### 3. Quantization

`fp32 → fp16 → int8` — Slightly rounding the model's numbers.

Does it make the model dumber? Not really. Models learn patterns, not exact values. Like teaching a kid HOW to add rather than memorizing every sum. Rounding π from 3.14159 to 3.14 still works for most real world use.

**Benefit:** 2-4x faster, less memory, runs on cheaper hardware. Tiny quality loss.

### 4. Speculative Decoding

LLMs generate one token at a time. Slow.

**Fix:** a small junior model quickly drafts the next 4-5 tokens. The big model verifies them in one shot.

- Guesses right → saved 4-5 steps
- Guesses wrong → discard, retry

Junior drafts. Senior approves. Two separate models, not one inside the other.

### 5. Parallelism

Big model. Can't fit on one GPU. Split it across multiple GPUs.

Does splitting make it dumber? No. GPUs are connected via high speed links (NVLink). They constantly talk to each other. Same model, just physically distributed. Full intelligence intact.

### 6. Disaggregation

LLM inference has 2 phases:

- **Prefill** → process the entire input prompt. Compute heavy.
- **Decode** → generate output tokens one by one. Memory heavy.

Different problems, different resource needs. So put them on separate machines: Prefill machines process → hand off to decode machines → decode generates the final answer.

## The Framework Stack

1. **CUDA** → the language that tells GPUs what to do, how, and when. Runs in parallel across thousands of GPU cores simultaneously.
2. **PyTorch** → general purpose workshop. Great for building and experimenting with models.
3. **vLLM** → production inference engine. Star feature: PagedAttention. Best for single model, high volume, lots of users.
4. **SGLang** → built for complex multi-step workflows. Agents, chained prompts, multi-model calls.
5. **TensorRT-LM** → NVIDIA's own engine built on top of CUDA. Maximum performance, tuned specifically for their hardware.

### Stack Hierarchy

```
CUDA (foundation) 
  ↓
PyTorch (build) 
  ↓
vLLM / SGLang / TensorRT-LM (production)
```

### When to Use What

| Use Case | Framework |
|----------|-----------|
| Single model + lots of users | vLLM |
| Complex agents / multi-step workflows | SGLang |
| NVIDIA hardware, maximum performance | TensorRT-LM |
| Building / experimenting | PyTorch |

## High Level Working of Inference

### 1. Multi-cloud

Run the same application across AWS + GCP + Azure.

- **Benefit:** Redundancy against one provider going down
- **Examples:** Netflix, Uber, Spotify — run across multiple clouds
- **Also:** Most big banks and healthcare companies (regulatory reasons force redundancy)

### 2. Edge Inference

AI inference is dynamic — computed on the fly, can't be pre-cached. Deploy actual inference servers in multiple regions. Same idea as CDN, but servers are actively running the model.

### 3. Managing Multi-cloud

- **Terraform** → provisions infrastructure across multiple clouds from one config file
- **Kubernetes** → orchestrates where workloads run, regardless of which cloud is underneath

Together they act as a unified control layer — no manual management per cloud.

### Inference-as-a-Service

Companies like **Together AI** and **Fireworks AI** handle multi-cloud + Kubernetes + Terraform underneath. Developer just hits one API endpoint, gets a response. No idea which cloud, region, or server handled it. Pure abstraction.
