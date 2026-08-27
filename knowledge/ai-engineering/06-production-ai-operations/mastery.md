---
id: ai-production-mastery
title: Production AI Operations Mastery Defense
level: L3-L5
status: maintained
last_reviewed: 2026-08-27
prerequisites: [ai-production-research-frontier, ai-production-implementation-patterns]
---

# Production AI Operations Mastery Defense

## Rule

Answer without notes. Every strong response connects user outcome, mechanism, failure, metric, mitigation, and evidence. Tool names without operational semantics do not pass.

## System and delivery

1. Trace a RAG agent request across all logical planes and trust boundaries.
2. Specify the behavior bundle required to reproduce a run.
3. Explain control-plane blast radius and how to release configuration safely.
4. Design unit, contract, component, end-to-end, load, and production checks for one feature.
5. Compare shadow, canary, blue/green, feature flags, and A/B tests.
6. Roll back a model plus index migration while preserving compatibility.

## Routing and serving

7. Design model routing using capability, risk, residency, deadline, and budget.
8. Explain when failover silently violates semantics.
9. Compare retry, failover, hedging, caching, circuit breaking, and load shedding.
10. Trace queue, prefill, TTFT, decode, and end-to-end latency.
11. Explain continuous batching and KV-cache pressure.
12. Choose among tensor, pipeline, and data parallelism for a stated workload.
13. Use Little’s Law to challenge a capacity proposal, then name its limitations.
14. Explain why GPU utilization and maximum tokens/second are insufficient product metrics.

## Async systems and reliability

15. Choose synchronous, queued, or durable workflow execution.
16. Explain at-least-once delivery and build an idempotent handler.
17. Diagnose a retry storm and design a retry budget.
18. Handle expired, cancelled, dead-lettered, and ambiguously completed work.
19. Design priority isolation for interactive, batch, and safety-critical traffic.

## Observability and evaluation

20. Define an AI product SLI that includes semantic quality.
21. Explain error budgets and why global aggregation can hide harm.
22. Design a trace without leaking prompts or exploding metric cardinality.
23. Separate input, data, retrieval, model, tool, evaluator, and concept drift.
24. Calibrate a model judge and describe its uncertainty.
25. Convert one production incident into a non-duplicative regression case.

## Cost, security, and incidents

26. Calculate cost per successful outcome and list hidden cost categories.
27. Compare managed and self-hosted inference with total operational ownership.
28. Design hierarchical budgets and cost kill switches.
29. Apply govern, map, measure, and manage to a concrete agent feature.
30. Lead an incident involving unsafe output after a silent provider change.
31. Explain why “the model hallucinated” is not a sufficient root cause.
32. Decommission an AI feature without leaving data, credentials, or routes behind.

## Production design scenario

Design a multi-tenant AI research assistant serving interactive questions and long-running reports.

Your defense must include:

- System planes, ownership, data classification, and versions.
- Interactive and queued request contracts.
- Routing, deadlines, quotas, and fallback semantics.
- Managed versus self-hosted inference decision.
- Capacity model, autoscaling signal, and load shedding.
- SLI/SLO and error-budget policy.
- Continuous evaluation and drift diagnosis.
- Cost allocation and budget enforcement.
- Release, rollback, incident, and decommission procedures.

## Game live-ops scenario

Operate generated companion dialogue for a global live game. Address frame independence, latency, regional privacy, child safety, fallback behavior, model continuity, player experiments, peak launches, moderation incidents, and cost per valuable narrative interaction.

## Pass criterion

You pass when you can show how the service stays useful, safe, explainable, and economically sustainable under change—not merely how it runs during a demo.
