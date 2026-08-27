---
id: ai-observability-slos
title: Observability, SLIs, SLOs, and Traces
level: L3-L5
status: maintained
last_reviewed: 2026-08-27
prerequisites: [ai-queues-backpressure, agent-evaluation-observability]
---

# Observability, SLIs, SLOs, and Traces

## Telemetry answers questions

Metrics summarize trends, logs record discrete events, traces connect operations across a request, and profiles explain resource consumption. Collecting all four without diagnostic questions creates cost, not observability.

## From user journey to SLI

An SLI is a measured signal. An SLO is a target for that signal over a window. An SLA is an external agreement and may have contractual consequences.

For an AI support answer:

```text
valid events = eligible user requests
good events  = completed within 8 s
               AND passed deterministic policy checks
               AND had no unsupported high-risk claim
SLI = good_events / valid_events
SLO = SLI >= 99.0% over 28 days
```

The semantic condition may require sampled evaluation and arrives later than latency. Maintain separate fast operational and slower quality indicators rather than pretending one number is perfect.

## Error budgets

An error budget is the allowed fraction of non-good events: `1 - SLO`. It converts “reliability matters” into a release and investment policy. An SLO without consequences for budget consumption is decorative.

Segment results. A global SLO can hide complete failure for one language, tenant tier, region, or accessibility path.

## Golden signals, expanded

Traditional latency, traffic, errors, and saturation remain necessary. AI systems add:

- Input/output tokens and context size.
- Queue, prefill, TTFT, decode, tool, and end-to-end timing.
- Route, fallback, cache, retry, and cancellation.
- Schema validity, groundedness, citation support, task success, safety.
- Model/prompt/index/policy versions.
- Cost and energy proxies where available.

## Trace design

Use one trace across edge, application, retrieval, gateway, provider, tools, and workflow. Represent retries and parallel calls without overwriting the original attempt. Link asynchronous jobs when a single parent-child trace would be misleading.

OpenTelemetry provides common telemetry concepts, but GenAI semantic conventions remain an evolving area. Pin a convention version and retain your domain fields instead of renaming dashboards on every draft change.

## Cardinality

Putting user IDs, prompts, document IDs, or arbitrary error text in metric labels can explode time-series cardinality and cost. Metrics use bounded dimensions; traces/logs hold sampled detail under access control.

## Content and privacy

Prompts, completions, tool arguments, and retrieved passages can contain secrets or personal data. Default to metadata, hashes, classifications, and opt-in sampled content. Apply redaction before export, retention limits, encryption, regional controls, and auditable access.

“Do not log” must be enforced in instrumentation, not left to dashboard users.

## Alerting

Alert on actionable user symptoms and fast budget burn. Dashboard internal causes for investigation. Alerts need owner, severity, runbook, and a condition that clears.

Useful examples:

- Safe-success SLO burns too quickly.
- Oldest interactive job exceeds deadline.
- Cross-tenant policy check fires once.
- Fallback route grows while primary appears superficially healthy.

Avoid paging on every model-provider 500 if retries hide all user impact—unless the pattern threatens imminent exhaustion.

## Structured event minimum

Record IDs and versions, authenticated tenant scope, route and stage durations, token/cost accounting, tool effect IDs, validation result, user-visible outcome, and stop reason. Never use raw generated text as the only explanation of what happened.

## Game live operations

Measure player-experienced dialogue wait, fallback frequency, safety interventions, narrative repetition, and session abandonment. Infrastructure health is only a proxy for whether AI improves the game.
