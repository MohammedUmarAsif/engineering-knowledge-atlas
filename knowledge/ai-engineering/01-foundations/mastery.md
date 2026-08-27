---
id: ai-foundations-mastery
title: AI Foundations Mastery Review
level: L3-L4
status: maintained
last_reviewed: 2026-08-27
---

# AI Foundations Mastery Review

## Explain in 30 seconds

- Language model
- Token and context window
- Embedding
- Transformer
- Inference
- Retrieval
- Fine-tuning
- Hallucination

## Explain in three minutes

1. Why an LLM is useful despite not being a database.
2. The difference between model capability and application reliability.
3. How context, retrieval, tools, and model weights play different roles.
4. Why structured output improves integration but does not prove correctness.

## Production scenarios

### Incorrect policy answer

Determine whether the authoritative document was available, parsed, indexed, retrieved, included, followed, and cited. Then inspect whether the response validator could have rejected unsupported claims.

### Latency doubled

Separate queue time, prefill, generation, retrieval, tools, retries, and network latency. Compare changes in context length, output length, traffic, provider, and orchestration.

### Cross-customer information leak

Treat as a security incident. Stop exposure, preserve evidence, identify the failed authorization boundary, assess affected data, rotate credentials if needed, notify appropriate owners, and add tenant-isolation tests.

## Exit diagnostic

You have mastered this module when you can:

- draw an end-to-end AI application and assign responsibility to each component;
- classify realistic failures without blaming the model generically;
- describe how to observe and evaluate the system;
- identify where deterministic software should constrain probabilistic behaviour;
- state what you do not yet know without disguising uncertainty.
