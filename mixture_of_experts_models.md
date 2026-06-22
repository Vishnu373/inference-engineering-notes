# Mixture of Experts (MoE)

## Overview

- Large model = multiple small "expert" sub-networks + a router
- Router selects which expert(s) to activate for each incoming token/request
- Only selected experts are active at a time; the rest stay idle

## Scale

- Common in 100B+ parameter models; smaller variants (20B, 30B) also exist

## Inference Considerations

- Local single-request inference -> only a small subset of experts active
- Production servers -> different requests activate different experts, so most parameters end up active across the batch
  - Solution: expert parallelism

## Expert parallelism
- spread experts across multiple GPUs for high-throughput inference.
- Best for large batches of requests.
- Scale: More GPUs = more experts = larger model capacity, without any single GPU being overloaded.
- Trade-offs:
  - If batch is small, only a handful of experts will be activated (corresponding GPUs) while rest will be idle.
  - All-to-all communication. The router runs on every GPU. However, for the incoming request the expert lives on only one GPU. So, GPU-1 processes the request -> token gets routed to the correct expert, assume it might be GPU-5.
    - Adds extra time to find the expert.