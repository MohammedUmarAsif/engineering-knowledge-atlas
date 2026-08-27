---
id: production-system-map
title: The Production AI System Map
level: L2-L5
status: maintained
last_reviewed: 2026-08-27
prerequisites: [production-ai-operations]
---

# The Production AI System Map

## Follow the outcome, not the model call

Suppose a user asks an assistant to explain an invoice. A complete path may include authentication, rate limits, tenant lookup, document retrieval, reranking, prompt construction, model routing, provider inference, tool calls, validation, streaming, storage, analytics, and UI rendering.

The model can be perfect while the product fails because the wrong tenant document was retrieved. HTTP can return `200` while the answer invents a charge. “API uptime” is therefore not the product reliability definition.

## Planes of the system

- Experience plane: UI, streaming, cancellation, feedback, accessibility.
- Application plane: orchestration, policy, validation, business logic.
- Knowledge plane: source data, ingestion, indexes, retrieval, provenance.
- Model plane: gateway, provider, inference runtime, tokenizer, adapters.
- Action plane: tools, credentials, approvals, effects.
- State plane: conversations, workflow checkpoints, caches, artifacts.
- Operations plane: delivery, configuration, telemetry, alerts, incident controls.
- Governance plane: ownership, risk, privacy, retention, audit, compliance.

These are logical responsibilities, not necessarily separate services. Prematurely splitting them into microservices adds failure modes without adding clarity.

## Version every behavior-changing input

A reproducible run may require:

```text
application commit
workflow/prompt version
model provider + model identifier + snapshot if exposed
generation parameters
tool and policy versions
retrieval corpus/index/embedding versions
feature flags and route
evaluation rubric version
runtime/container/dependency artifact
```

“Same prompt” is not reproduction when any other component changed. Conversely, logging every raw input forever can violate privacy. Preserve minimal identifiers and approved artifacts; apply retention and access policy to content.

## Control plane versus data plane

The data plane handles user requests. The control plane changes how those requests are handled: configuration, model routes, prompts, feature flags, access policy, rollout weights, and evaluation thresholds.

A control-plane bug can affect all requests instantly. Protect configuration changes with review, validation, version history, staged rollout, and rollback just like code.

## Ownership map

Every dependency needs:

- Owner and escalation path.
- Contract and version policy.
- Health and user-impact signals.
- Timeout and retry policy.
- Failure mode and fallback.
- Data classification.
- Cost attribution.

Third-party model providers are dependencies, not magical infrastructure. Their status page cannot tell you whether your particular model-region-route is producing acceptable answers.

## Failure domains

Separate failures by where isolation can contain them:

- Request: one malformed or adversarial input.
- Tenant: quota exhaustion or corrupted index.
- Model route: degraded snapshot or provider region.
- Tool: downstream outage or permissions change.
- Deployment cell: bad artifact or exhausted GPU pool.
- Global control plane: invalid policy or routing configuration.

Design blast-radius boundaries before the incident. Per-tenant quotas and cellular deployment can stop one workload from consuming all capacity.

## Product invariants

Examples:

- A response never cites evidence from another tenant.
- A write occurs only under authenticated, current authority.
- Every charged generation maps to a trace and product feature.
- Cancellation prevents unstarted effects.
- A rollout can be halted without shipping new code.
- When evidence is insufficient, the system abstains or asks a question instead of fabricating.

Metrics observe invariants imperfectly; runtime checks enforce those that can be enforced.

## Game transfer

A live game may use an offline content pipeline, an online dialogue service, local deterministic behavior, telemetry, safety moderation, and fallback authored dialogue. The game loop must not wait indefinitely for a cloud model. Separate slow creative intelligence from frame-critical simulation.

## Architecture exercise

Draw a complete request path for a coding assistant. Mark trust transitions, queues, persistent state, external dependencies, user-visible deadlines, and every place a version change can alter behavior. If one box is labeled simply “AI,” decompose it.
