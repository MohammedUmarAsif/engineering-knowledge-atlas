---
id: llm-failure-modes
title: LLM and AI Application Failure Modes
level: L2-L4
status: maintained
last_reviewed: 2026-08-27
---

# LLM and AI Application Failure Modes

## Diagnostic

Skip to [Mastery Review](mastery.md) if you can classify an AI failure as model, context, retrieval, tool, orchestration, policy, data, evaluation, or user-interface failure and propose evidence for that classification.

## Failure taxonomy

### Model

Capability gap, hallucination, poor instruction following, bias, unstable formatting, weak calibration.

### Context

Missing evidence, excessive noise, conflict, truncation, incorrect priority, prompt injection.

### Retrieval

Bad parsing, bad chunks, missing recall, poor ranking, stale index, authorization leak.

### Tool

Wrong tool selection, invalid arguments, stale tool description, timeouts, partial side effects, excessive permissions.

### Orchestration

Infinite loops, retry storms, lost state, duplicate actions, race conditions, incompatible fallback models.

### Evaluation

Unrepresentative test data, contaminated benchmarks, weak metrics, evaluator bias, no regression baseline.

### Product and human factors

Users overtrust fluent output, cannot inspect evidence, cannot correct errors, or misunderstand automation boundaries.

## Diagnostic sequence

1. Preserve the exact input, effective context, model/version, parameters, retrieval results, tool events, and output.
2. Reproduce where possible.
3. Locate the earliest incorrect boundary.
4. Separate deterministic application defects from probabilistic variation.
5. Measure frequency and impact on representative tasks.
6. Fix the smallest responsible layer.
7. add a regression case and operational signal.

## Senior principle

Do not ask “Why did the AI fail?” as one question. Ask which boundary first violated an explicit expectation and why the system allowed that violation to reach the user.
