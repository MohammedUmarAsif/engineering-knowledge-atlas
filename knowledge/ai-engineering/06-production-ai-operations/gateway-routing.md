---
id: ai-gateway-routing
title: Model Gateways, Routing, and Dependency Policy
level: L3-L5
status: maintained
last_reviewed: 2026-08-27
prerequisites: [ai-delivery-release]
---

# Model Gateways, Routing, and Dependency Policy

## Why a gateway exists

Applications need a stable internal contract while model providers, credentials, quotas, APIs, prices, and capabilities change. A gateway can centralize authentication, routing, quotas, telemetry, redaction, caching, and provider adaptation.

It also becomes a high-blast-radius dependency. A gateway is justified by shared policy and operational leverage—not merely a universal-looking endpoint.

## Request policy

Route using explicit requirements:

- Required modality, context size, structured output, or tools.
- Data residency and provider eligibility.
- Quality tier and task risk.
- Latency deadline.
- Tenant budget and quota.
- Model health and capacity.
- Experiment assignment.

Do not route solely by the cheapest token price. A cheaper model requiring retries or producing fewer successful outcomes may cost more.

## Fallback semantics

Fallback is safe only if the alternative preserves necessary capabilities and policy. A model without reliable schema support is not a valid fallback for an effectful tool workflow. A provider outside the approved region is not a valid fallback for restricted data.

Record the route and fallback reason. Silent fallback makes quality changes appear random.

## Failover versus retry

- Retry repeats against the same logical dependency after a likely transient failure.
- Failover chooses another region, deployment, provider, or model.
- Hedging sends a second request before the first finishes and accepts one result.

Hedging can reduce tail latency but duplicates cost and processing, may violate data policy, and is dangerous for effectful requests. Canceling the losing request does not guarantee the provider stopped computing.

## Time budgets

Propagate a deadline, not independent timeouts. If the user deadline is five seconds, retrieval cannot consume four seconds and still give inference a fresh five-second timeout.

```text
remaining = deadline - now
stage_timeout = min(configured_stage_limit, remaining - reserved_cleanup)
```

Reserve time to validate, render a fallback, and cancel downstream work.

## Quotas and fairness

Apply limits at several dimensions: tenant, user, feature, model, tokens, concurrent requests, and spend. Concurrency limits protect scarce inference slots better than requests-per-minute when request sizes vary.

Use weighted fairness where premium, interactive, batch, and safety-critical traffic have different service objectives. Prevent one tenant’s enormous contexts from creating head-of-line blocking for everyone.

## Caching

Cache only when the key includes every behavior-relevant input: normalized request, model/version, parameters, prompt/policy version, relevant user/tenant scope, and data version.

Semantic caches trade exact identity for similarity and can return unsafe or stale answers across subtly different intent. Begin with deterministic caches for stable, non-personal, idempotent operations.

## Circuit breakers and load shedding

A circuit breaker stops calls to a dependency showing sustained failure, allowing recovery and preventing resource pileups. Load shedding rejects or degrades low-priority work before overload collapses all requests.

Possible degradation ladder:

1. Disable expensive optional enrichment.
2. Reduce candidate or generation budgets.
3. Serve safe cached/static results.
4. Move batch work to a queue.
5. Reject with retry guidance.

Do not degrade away correctness or safety requirements.

## Gateway observability

Measure route decisions, provider/model/version, request and token sizes, queue time, TTFT, completion latency, errors by stage, retries, fallback, cache status, estimated cost, cancellation, and final application outcome. Redact content by default.

## Game transfer

Route live player dialogue differently from offline quest generation. Interactive traffic needs firm latency and safe fallback; offline content can spend more compute and await human review. Never allow batch generation to starve gameplay inference.
