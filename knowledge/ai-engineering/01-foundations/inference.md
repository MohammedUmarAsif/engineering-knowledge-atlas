---
id: inference-and-generation
title: Inference and Generation
level: L2-L3
status: maintained
last_reviewed: 2026-08-27
---

# Inference and Generation

## Diagnostic

Skip to [Limitations and Failure Modes](failure-modes.md) if you can explain sampling, temperature, top-p, deterministic constraints, streaming, caching, and the main latency/cost drivers.

## Generation controls

The model produces scores for possible next tokens. A decoding policy transforms those scores into a selection.

- **Temperature** rescales relative token probabilities. It changes distribution sharpness; it is not a truth or creativity dial.
- **Top-p** limits sampling to a probability mass of likely candidates.
- **Maximum output** bounds generation but can truncate an otherwise correct response.
- **Stop conditions** terminate on specified patterns or protocol events.
- **Structured decoding** constrains the allowed output form, improving parseability but not factual correctness.

## Latency

Separate:

- request and queue time;
- input processing/prefill;
- time to first output token;
- per-token generation time;
- tool and retrieval latency;
- validation and post-processing.

Streaming improves perceived responsiveness but does not reduce total computation and complicates moderation, cancellation, and rollback.

## Cost

Cost can include input tokens, output tokens, cached tokens, retrieval, reranking, tool calls, retries, storage, observability, and human review. Optimize the whole task, not only the model call.

## Reliability controls

- schema constraints;
- validation against authoritative systems;
- bounded retries with classified errors;
- timeouts and cancellation;
- idempotency for side effects;
- model fallback with compatibility tests;
- confidence policies based on evidence, not self-reported certainty.

## Interview check

An AI endpoint is slow and expensive. Explain how you would locate the bottleneck before changing models.
