# Distillation

Teaching a smaller model how to behave like a larger model.

**Teacher** (large model) → generates responses → **Student** (small model) → trains on those responses.

## Fine-Tuning vs Distillation

When an LLM generates a response, it doesn't just pick one word — it calculates a probability for **every possible next token**.

For example, given "The sky is...":
- "blue" → 60%
- "clear" → 25%
- "dark" → 10%
- everything else → 5%

**Fine-tuning on synthetic data** only shows the student the **final answer** ("blue"). It throws away all that probability information.

**Distillation** shows the student the **entire probability distribution** — so the student also learns that "clear" was a close second, "dark" was possible, etc. Much richer signal than just the final answer.

## Caveat: Distillation Is Rarely Used in Practice

**Why? Bias transfer.**

- If you distill a small model from a large one, the small model inherits the large model's biases, blind spots, and limitations.
- The small model gets artificially capped — it can never be better than the large model in any area.
- Training independently gives the small model a chance to develop differently and sometimes even outperform in certain areas.

**When is distillation actually useful?**

- When a lab only has a large model and wants to make it more accessible/cheaper to run.
- e.g. Deepseek R1 (671B) large model was distilled into smaller base models (Llama and Qwen).
