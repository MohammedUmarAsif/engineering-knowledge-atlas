---
id: model-application-reliability-security
title: Reliability, Security, and Operations
level: L3-L4
status: maintained
last_reviewed: 2026-08-27
prerequisites: [multimodal-model-applications]
---

# Reliability, Security, and Operations

## Diagnostic

Skip to [Mastery Review](mastery.md) if you can define SLOs, telemetry, threat boundaries, degradation, rollout, rollback, retention, and incident evidence for an AI feature.

## Reliability model

An AI request can fail at transport, provider, model, context, retrieval, tool, validation, policy, storage, or presentation boundaries. Define success at the user-task level, then assign signals to each boundary.

## Service objectives

Possible indicators include:

- task completion rate;
- grounded/cited answer rate;
- critical-error rate;
- schema-valid and semantically valid rate;
- tool success and duplicate-action rate;
- abstention/escalation accuracy;
- time to first useful output and total latency;
- cost per successful task;
- user correction or reversal rate.

Token count and model latency are diagnostic metrics, not sufficient product outcomes.

## Telemetry

Correlate:

- request and workflow IDs;
- user/tenant pseudonymous identifiers where appropriate;
- application, prompt, policy, model, tool, and schema versions;
- context size and source identifiers;
- retrieval candidates and ranks;
- tool proposals, approvals, results, and timing;
- validation outcomes;
- provider usage and finish reason;
- user-visible result and feedback, subject to privacy policy.

Redact secrets and minimize raw content. Observability must not become a second data leak.

## Threat boundaries

Use the current OWASP GenAI guidance as a threat catalogue, then model the specific system. Important classes include prompt injection, sensitive disclosure, unsafe output consumption, poisoning, excessive agency, denial of wallet/service, supply-chain compromise, misinformation, and unbounded resource use.

Controls belong at several layers:

- input and file validation;
- identity and tenant isolation;
- least-privilege tools;
- network and execution sandboxing;
- deterministic authorization;
- output encoding and validation;
- human confirmation;
- quotas and budgets;
- provenance and citations;
- adversarial evaluation;
- audit and incident response.

## Deployment

Version prompts, policies, tools, models, schemas, and evaluation sets independently. Use offline evaluation before deployment, shadow or sampled comparison where lawful, gradual rollout, slice-level monitoring, and a tested rollback/degradation path.

## Degradation

Possible modes:

- disable side-effect tools but retain read-only answers;
- fall back to search or deterministic workflows;
- use a compatible approved model;
- queue non-urgent work;
- present sources without generated synthesis;
- fail visibly with a recovery path.

Do not conceal degraded quality behind fluent output.

## Incident response

1. Contain the unsafe capability or data path.
2. Preserve privacy-appropriate evidence and versions.
3. Identify the earliest violated boundary.
4. Assess users, tenants, data, actions, and duration affected.
5. Remediate the responsible layer.
6. Add a regression evaluation and operational signal.
7. review whether incentives, ownership, or rollout allowed the incident.

## Senior questions

- Which errors are tolerable, visible, reversible, or catastrophic?
- Who owns quality when model and application metrics disagree?
- Can the feature be disabled independently?
- How are vendor data retention and regional constraints verified?
- How will costs be bounded during loops, retries, or abuse?

## Interview scenario

An assistant sent duplicate customer refunds during a provider timeout. Walk through containment, reconciliation, root cause, idempotency, telemetry, user communication, and prevention.

## Primary source

- [OWASP Top 10 for Large Language Model Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
