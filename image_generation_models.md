# Image Generation Models

## Pipeline - Core Components (Base)

- Text Encoder -> converts the text prompt into a format the denoising model can use as conditioning
- Denoising Model -> iteratively refines the noisy latent space into a coherent image over 30-50 steps
- VAE (Variational Autoencoder) -> converts the finished latent space matrix back into pixel space

## Pipeline - Extended Components

- LoRAs -> lightweight fine-tunes applied on top of the base model to shift style or enhance quality; don't change the architecture, just adjust weights
- ControlNets -> feed in outlines, edges, or depth maps to steer the spatial layout of the output; useful when the image must match a specific shape or composition

## How It Works

- Latent space starts as pure random noise, refined over 30-50 steps into a coherent image
- Operates entirely in latent space (e.g., 128x128 instead of 1024x1024) — running attention over ~1M pixels per step is computationally infeasible; VAE handles pixel conversion in/out
- Built on diffusion transformers — the latent is split into 2x2 or 4x4 patches, each treated as a token; same attention mechanism as LLMs
- Each step runs 2 forward passes (conditioned + unconditioned), blended via guidance scale — 50 steps = 100 total forward passes
  - Conditioned -> "given this prompt, what should the image look like?"
  - Unconditioned -> "with no prompt, what would the image look like?"
  - Guidance scale -> controls how strictly the model follows the prompt vs. its own judgment
    - Low (~1-2) -> more creative, less faithful
    - High (>15) -> over-saturated, unnatural artifacts
    - Sweet spot -> ~4-7 for most use cases
  - formula: result = unconditioned + guidance_scale x (conditioned - unconditioned)

Note: Latent space is what you get when you squeeze out the redundancy and keep only the essential structure of the image — encoded as a much smaller matrix of numbers (e.g., 128x128).

## Inference Arguments (Runtime Controls)

- Prompt -> describes what the image should look like
- Negative prompt -> explicitly describes what to exclude (styles, objects, artifacts)
- Number of steps -> 30-50 for quality; directly trades off speed vs. quality
- Guidance scale -> ~4-7; low = more creative/less faithful, high = more prompt-adherent
- Image size -> fixed menu of resolutions/aspect ratios (not arbitrary dimensions)

These are configured per request — applies for ComfyUI, the diffusers library, or any image generation API.

## Few-Step Image Generation

- 8 or fewer denoising steps -> 80-90% faster, some quality tradeoff
- Two approaches: latent consistency vs. distillation (distillation more common)
- Relevant for latency-sensitive workloads

Note: Latent consistency -> a training approach where the model learns to predict the final clean image latent directly from any noisy step, enabling high-quality generation in fewer steps.

## LLM-Style Image Generation

- Direction: blending diffusion transformer architecture with LLM architecture
- Anything tokenizable can be modeled as an LLM

Key advantages over diffusion:

- Diffusion = fixed output size; LLMs = variable-length autoregressive output
- Diffusion = up to 100 forward passes; LLMs = single forward pass per token
- LLMs have baked-in text understanding, reducing reliance on a separate encoder
