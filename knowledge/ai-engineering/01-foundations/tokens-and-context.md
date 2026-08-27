---
id: tokens-and-context
title: Tokens and Context
level: L1
status: maintained
last_reviewed: 2026-08-27
---

# Tokens and Context

## Diagnostic

Skip to [Embeddings](embeddings.md) if you can explain tokenization, context limits, positional information, prompt injection, and why long context is not equivalent to durable memory.

## Mental model

A language model repeatedly estimates a probability distribution over the next token, selects a token according to the decoding strategy, appends it, and repeats. Tokens are model-specific units, not reliably words, characters, or semantic concepts.

## Context

The context is the sequence available during the current inference operation. It may contain system instructions, conversation history, retrieved passages, tool results, images represented through model-specific mechanisms, and the partially generated response.

Context does not:

- retrain the model;
- guarantee that every included fact is used;
- create reliable long-term memory;
- establish that included information is true;
- neutralize conflicting or malicious instructions.

## Why more context can hurt

- Relevant evidence becomes harder to locate among noise.
- Conflicting passages increase ambiguity.
- Important information may be poorly positioned.
- Latency and cost rise.
- Attack surface grows.
- The application may truncate content unpredictably.

The engineering objective is not maximum context. It is the smallest sufficient, trustworthy context.

## Senior questions

- Who is allowed to add each part of the context?
- Which instructions outrank which data?
- What happens at the context limit?
- Can secrets or data from another tenant enter the prompt?
- Can retrieved content manipulate tool use?
- How will the exact effective context be inspected during an incident?

## Interview check

Explain why chat history, retrieval, tool state, and durable user memory are four different concerns.
