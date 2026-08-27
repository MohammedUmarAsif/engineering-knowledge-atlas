---
id: model-api-architecture
title: API Architecture and Model Selection
level: L2-L4
status: maintained
last_reviewed: 2026-08-27
prerequisites: [ai-foundations]
---

# API Architecture and Model Selection

## Diagnostic

Skip to [Instructions and Context Construction](instructions-and-context.md) if you can design a provider-neutral boundary, define a workload-specific model evaluation, and explain fallback compatibility.

## Mental model

Treat a model provider like any consequential external dependency: capabilities vary, contracts evolve, calls fail, latency fluctuates, data policies matter, and apparently compatible models behave differently.

## Separate four layers

### Domain contract

What the application actually needs: classify a case, draft an answer with evidence, extract an invoice, or propose an action. This contract should use product language rather than provider terminology.

### Orchestration

Builds context, selects policies, controls retries, invokes tools, validates results, stores state, and emits telemetry.

### Model adapter

Translates the domain request into a provider request and normalizes responses, usage, errors, tool events, and finish reasons.

### Provider SDK

Authentication, transport, serialization, streaming protocol, and provider-specific features.

Do not let provider response objects flow through the whole codebase. They turn migration into a rewrite and make tests depend on unstable details.

## Capability registry

Record capabilities as data rather than assumptions:

- supported input modalities;
- context and output limits;
- structured-output dialect;
- tool and parallel-call behavior;
- streaming event types;
- state and retention behavior;
- regional availability;
- safety controls;
- latency and price observations;
- approved data classifications.

Never infer capability from a model name alone.

## Model selection

Choose against a representative workload and explicit constraints:

1. Define task success and unacceptable failures.
2. Build a versioned evaluation set from realistic traffic or carefully designed cases.
3. Measure quality by slice, not only as one average.
4. Measure latency distributions, not only the mean.
5. Include token, tool, retrieval, retry, and review cost.
6. Test schema adherence, refusals, adversarial inputs, and long-context behavior.
7. Evaluate operational constraints: rate limits, retention, regions, quotas, and incident history.

The “best model” is a property of a workload, policy, time, and budget.

## Fallbacks

A fallback must preserve the application contract. Check:

- schema and tool compatibility;
- different safety/refusal behavior;
- prompt sensitivity;
- context limits;
- multimodal support;
- data policy;
- output quality on critical slices.

A model switch that returns a response while violating the product contract is not successful degradation.

## Failure handling

Classify errors before retrying:

- invalid request: fix; do not retry unchanged;
- authentication/authorization: fail closed;
- rate limit: respect retry hints and apply bounded backoff;
- timeout/transient server fault: retry within a latency budget;
- safety refusal: follow product policy rather than retrying until compliance;
- invalid output: repair only when safe, otherwise regenerate or fail visibly;
- ambiguous side-effect status: reconcile by idempotency key before retrying.

## Senior questions

- What is the cost of provider dependence relative to premature abstraction?
- Which capabilities are essential and which are convenient?
- Can traffic be replayed safely against a candidate model?
- What is the degradation mode when no approved model is available?
- How will model changes be rolled out, compared, and rolled back?

## Interview scenario

Two models score similarly, but one is cheaper and slower while the other is faster with worse performance on rare high-risk cases. Explain the decision process without collapsing it into a single benchmark score.
