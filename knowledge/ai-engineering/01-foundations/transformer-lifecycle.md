---
id: transformer-lifecycle
title: Transformer and LLM Lifecycle
level: L1-L2
status: maintained
last_reviewed: 2026-08-27
---

# Transformer and LLM Lifecycle

## Diagnostic

Skip to [Inference and Generation](inference.md) if you can distinguish architecture, training objective, adaptation, alignment, inference, and application orchestration.

## Transformer mental model

Transformer layers repeatedly transform token representations using attention and learned feed-forward computation. Attention allows a representation to incorporate information from other positions. It does not itself provide truth, goals, memory, or permission boundaries.

## Lifecycle

### Pretraining

Learns broad statistical structure from large datasets through a prediction objective. Its outputs are model weights, not a searchable copy of the training corpus.

### Adaptation

Instruction tuning, supervised fine-tuning, preference optimization, domain adaptation, and related techniques shape behaviour. They differ in data requirements, cost, stability, and what they can reliably change.

### Inference

Runs fixed model weights against current input and generation settings. Retrieval and prompts influence the computation without normally changing the weights.

### Application orchestration

Code selects models, constructs context, invokes tools, validates output, stores state, enforces permissions, and handles failure. This is where much of production reliability must be engineered.

## Common category mistakes

- treating retrieval as training;
- treating a prompt as durable memory;
- treating fluency as calibrated confidence;
- treating alignment as factual verification;
- treating an agent framework as additional model intelligence;
- treating benchmark performance as application performance.

## Interview check

A company wants its model to answer from frequently changing internal policy documents. Compare prompting, retrieval, fine-tuning, and continued pretraining.
