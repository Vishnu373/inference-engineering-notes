## KV Cache

## Why It's Needed

Problem: redundant computation across steps.

Example:

- Prompt: "The cat sat on the"
- Model predicts: "mat."
- Model computes K and V for every token in the prompt

Follow-up: "Why did the cat?"

- Model recomputes K and V for all previous tokens (prompt + generated tokens)
- The values are identical — same tokens, same weights

## Solution

Cache K and V for all past tokens in memory.
On each new step, only compute K and V for the new token, then append to the cache.

- Q is never cached — only the current token's Q is needed at each step
- See [attention.md](attention.md) for how K, Q, V are calculated
