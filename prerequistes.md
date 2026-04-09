# Prerequisites for Inference Engineering

Before diving into inference engineering, you need to ask yourself 5 critical questions:

## 1. Which Model to Run?

The AI model itself — Llama, Mistral, GPT, etc. Open source or proprietary. **Not your application.**

Choose based on:
- Model size and capabilities needed
- Open source vs. proprietary trade-offs
- License and usage restrictions
- Community support and documentation

## 2. Application Interface

How input arrives and how output should come back.

**Input options:** text, image, voice, or multimodal?

**Output formats:** plain text, JSON, structured data, or streaming?

💡 A chatbot, coding assistant, and document summarizer all have different input/output expectations. Design this carefully.

## 3. Latency Budget

End-to-end, **how fast does your product need to respond?** This drives a lot of infrastructure decisions downstream.

- Real-time interactive applications → milliseconds
- Batch processing → seconds to minutes
- Asynchronous workflows → flexible

The latency requirement determines:
- Which optimization techniques you'll use
- How much hardware you'll need
- Whether you can use caching strategies

## 4. Unit Economics

Cost per request, per user, or per month. **Is it financially sustainable?**

$0.10 per request sounds fine until you have 1 million daily users. That's $100,000 per day.

Consider:
- Model inference cost
- Infrastructure and compute costs
- Operational overhead
- Profit margin requirements

## 5. Usage Patterns

Estimated before deployment, observed after.

**Key insights:**
- If 90% of traffic comes during business hours, scale down at night instead of running full capacity 24/7
- Seasonal patterns affect server provisioning
- User behavior often differs from predictions

**Impact:** Directly affects how many servers you provision and when.

# Scale and Specialization

### Shared vs Dedicated Inference

**1. Shared inference**

Call a public API (OpenAI, Anthropic, Gemini, Together AI). They handle everything. Pay per million tokens — meaning you pay for what you use, not a flat fee.

**2. Dedicated deployment**

Rent GPUs from a cloud provider or buy physical hardware yourself (on-premises) and run inference exclusively for your app. You expose it to users via your own API. You own the setup, you manage it.

### The Tradeoff

- **Shared** → zero setup, no control, expensive at scale
- **Dedicated** → full control, cheaper at scale, you manage everything

### When to Shift from Shared Inference to Dedicated Deployment

- **Scale** → volume is high enough that per-GPU pricing beats per-token pricing
- **Specialization** → you have a custom/fine-tuned model or strict latency/uptime needs
- **Orchestration** → you're chaining multiple models together and shared APIs add too much network overhead