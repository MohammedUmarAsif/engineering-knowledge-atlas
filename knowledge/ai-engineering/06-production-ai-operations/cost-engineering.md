---
id: ai-cost-engineering
title: Cost Engineering and FinOps
level: L3-L5
status: maintained
last_reviewed: 2026-08-27
prerequisites: [ai-gateway-routing, ai-observability-slos]
---

# Cost Engineering and FinOps

## Optimize cost per useful outcome

Token price is an input cost. The product metric is closer to:

```text
cost_per_success = total_variable_and_allocated_cost / verified_successes
```

A smaller model may be cheaper per call but require more retries, human correction, or escalations. A larger model may reduce total workflow steps. Measure the system.

## Cost map

Include:

- Model input, output, reasoning, cache, batch, and fine-tuning charges.
- Embeddings, reranking, OCR, search, and storage.
- GPU/CPU/memory, idle capacity, networking, and observability.
- Tools and third-party APIs.
- Human evaluation, moderation, support, and incident labor.
- Engineering and on-call ownership.

Self-hosting moves spend between categories; it does not eliminate it.

## Unit economics

Allocate by tenant, feature, task, model route, and outcome. Use a stable request/run ID to join billing and product events. Show both direct usage and allocated shared infrastructure.

Useful ratios:

- Cost per active user with successful AI outcome.
- Cost per resolved support case.
- Cost per accepted code change.
- Cost per approved game asset or dialogue minute.
- Wasted cost from retries, cancellations, expired jobs, and rejected output.

## Primary levers

1. Do not call a model when deterministic logic suffices.
2. Route by task requirement.
3. Reduce irrelevant context while protecting recall.
4. Bound output length and agent steps.
5. Cache stable prefixes or exact results safely.
6. Batch offline work.
7. Reduce retries by fixing causal failures.
8. Improve serving utilization without violating latency.
9. Move low-value work to cheaper schedules or models.
10. Delete telemetry and indexes beyond their value/retention window.

## Context has compound cost

Long context increases provider charges or prefill compute, raises latency, consumes KV-cache memory, and may reduce attention to relevant instructions. Retrieval quality and context construction are financial controls as well as quality controls.

## Budgets

Use hierarchical budgets:

- Per request/run.
- Per user or tenant.
- Per feature.
- Per day/month.
- Per experiment.

Define behavior when a budget approaches exhaustion: warn, route, degrade optional work, queue, require approval, or reject. Never surprise the user with an unlimited autonomous loop.

## Forecasting

Forecast using distributions of input/output lengths, model mix, retries, cache hit rate, concurrency, growth, and peak/average ratio. Include confidence ranges and provider price-change scenarios.

For self-hosting, model warm idle capacity and failure redundancy. Average GPU utilization can appear low because spare capacity is deliberately buying latency and availability.

## Cost incidents

Alert on spend velocity, route shifts, token distribution changes, cache collapse, retry storms, runaway agents, abusive tenants, and orphaned batch jobs. Provide kill switches that preserve critical traffic.

## False economies

- Removing evaluation to save judge cost while shipping costly failures.
- Aggressive truncation that loses required evidence.
- Cross-user semantic caching that violates privacy.
- Scaling to zero when cold start destroys interactive SLOs.
- One cheap global model that fails specialized tasks.

## Senior answer

State the outcome metric, cost attribution model, workload distribution, current bottleneck, proposed lever, expected quality/latency effect, experiment, and rollback threshold. “Use a cheaper model” is not cost engineering.
