# LLM Performance Metrics

Two metrics that measure LLM performance:

## 1. TTFT — Time to First Token

How long before the user sees the first word appear. Driven by the **prefill phase** — processing your entire input prompt before generating anything. Lower TTFT = feels more responsive.

## 2. TPS — Tokens Per Second

How fast tokens stream to the user after the first one. Driven by the **decode phase**. Higher TPS = feels faster to read.

### Why TPS Is Confusing

It means two different things:

- **Per user (latency)** → how fast one user receives tokens. Called **Perceived TPS**.
- **Entire system (throughput)** → total tokens the inference service generates per second across all users. Called **Total TPS**.

Most people mean per-user when they say TPS.

**The precise terms:**

- **Perceived TPS** → tokens per second per user (latency)
- **Total TPS** → tokens per second across entire service (throughput)
- **ITL (Inter-token Latency)** → time gap between each token. ITL of 10ms = 100 tokens per second per user. Just another way to express the same thing as TPS.

## Use Cases

In a chatbot, individual tokens are useful as they stream — the user is reading along word by word.

But when an AI agent makes a tool call (like calling a weather API or running a SQL query), it needs the complete response before it can do anything with it. Token by token streaming is meaningless here — the agent can't act on half an answer.

So instead of measuring TTFT and TPS, you just measure total time from request to complete response.

**In short:**

- **TTFT** → prefill phase performance
- **TPS** → decode phase performance
- Both together define how "fast" the model feels to a user

## Measuring Latency — Percentiles

**What is a percentile?**

A way of ranking data. P90 means 90% of requests were faster than this value, 10% were slower. It tells you where X% of your data falls.

**Why average is misleading?**

9 requests take 1 second, 1 takes 10 seconds. Average = 1.9 seconds. Looks fine. But that 1 user had a terrible experience. Percentiles expose what average hides.

**Percentiles:**

- **P50** → 50% of requests are faster. Typical user experience.
- **P90** → 90% faster. 1 in 10 users is slower.
- **P99** → 99% faster. 1 in 100 users is slower.

**Why P99 matters at scale?**

1 in 100 sounds rare. But 1 million daily requests = 10,000 users having a bad experience every day.

**What to measure?**

Take percentiles of both TTFT and TPS — not their averages. That gives the full picture of real user experience.

**How to calculate the percentile:**

- Collect all your response times. Say 100 requests.
- Sort them from fastest to slowest.
- P50 = the value at position 50. P90 = position 90. P99 = position 99.

In practice you don't do this manually — monitoring tools like Grafana, Datadog, Prometheus calculate and visualize it automatically, often as a graph over time.

## End-to-End Metrics

Two metrics:

- **Inference time** → on-GPU time only. Tells you how effective your model performance optimizations are.
- **End-to-end time** → inference + network latency + queue time. What the user actually experiences.

**How to use them together:**

- **Inference slow + end-to-end slow** → fix model performance (runtime layer)
- **Inference fast + end-to-end slow** → fix infrastructure (network, queuing)
