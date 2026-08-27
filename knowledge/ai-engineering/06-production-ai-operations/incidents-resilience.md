---
id: ai-incidents-resilience
title: Resilience and Incident Response
level: L3-L5
status: maintained
last_reviewed: 2026-08-27
prerequisites: [ai-observability-slos, ai-continuous-evaluation]
---

# Resilience and Incident Response

## Failure is expected; uncontrolled failure is not

Resilience is the ability to preserve critical outcomes or recover safely when components fail. High availability is one possible result; resilience also includes degraded operation, data reconciliation, communication, and learning.

## Dependency failure patterns

- Timeouts stop waiting; they do not stop remote work.
- Retries recover transient failures but can amplify overload.
- Circuit breakers contain repeated failure but can open on a mischosen signal.
- Bulkheads reserve capacity so one workload cannot sink another.
- Fallbacks preserve service only when their semantics remain acceptable.
- Load shedding sacrifices low-priority work to protect critical work.
- Checkpoints permit resumption but require compatible state and idempotency.

Patterns interact. A timeout plus automatic retry plus provider failover can triple cost and still deliver three late responses.

## Failure injection

Test model/provider errors, slow streams, truncated output, schema drift, retrieval outage, stale index, tool timeout, duplicate job delivery, expired credentials, full queue, GPU loss, control-plane misconfiguration, and telemetry outage.

The expected result is not always success. Safe rejection, visible degradation, or human escalation can be correct.

## Incident phases

1. Detect user impact.
2. Establish incident command, operations, and communication roles.
3. Bound scope and protect evidence.
4. Mitigate: halt rollout, disable route/tool, shed load, restore known-good bundle.
5. Reconcile partial or ambiguous effects.
6. Recover and verify user outcomes.
7. Communicate status and residual risk.
8. Write a blameless, causal postmortem with owned actions.

Google SRE emphasizes actionable symptom-based alerts, clear incident roles, communication, and learning rather than heroics.

## AI-specific incident classes

- Quality regression without transport errors.
- Unsafe or policy-violating output.
- Cross-tenant retrieval or data disclosure.
- Provider/model behavior change.
- Runaway agents or tool misuse.
- Prompt injection campaign.
- Cost spike or capacity exhaustion.
- Index corruption or stale evidence.
- Evaluator failure masking regressions.

Each needs distinct containment. Turning off telemetry does not stop a disclosure; switching models does not repair tenant filtering.

## Runbooks

A useful runbook contains symptom, user impact, dashboards/queries, recent changes, owner, immediate safe mitigations, rollback procedure, verification, escalation, communications template, and hazards.

Runbooks must be executable by someone other than the author. Exercise them through game days before an incident.

## Postmortem causality

Avoid “the model hallucinated” as root cause. Ask why the product accepted, displayed, or acted on unsupported output; why evaluation missed it; why blast radius was large; and why detection was late.

Classify contributing factors across specification, design, implementation, review, testing, rollout, monitoring, and response. Assign actions that change the system, not vague reminders to “be careful.”

## Recovery objectives

RTO describes acceptable recovery time. RPO describes acceptable data loss interval. Agent checkpoints, conversations, indexes, evaluation results, and audit trails can have different objectives. Backups are not recovery until restoration is tested.

## Game live-ops scenario

If generated NPC dialogue becomes unsafe after a provider change, disable the affected route with a flag, serve authored fallback, preserve sampled evidence under privacy policy, identify exposed players, verify moderation and route configuration, communicate internally, and add regression cases before staged restoration.
