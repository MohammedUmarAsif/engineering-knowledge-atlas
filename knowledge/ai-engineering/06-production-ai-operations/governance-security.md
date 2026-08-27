---
id: ai-governance-security
title: Governance, Privacy, and Operational Security
level: L3-L5
status: maintained
last_reviewed: 2026-08-27
prerequisites: [ai-incidents-resilience, agent-security-production]
---

# Governance, Privacy, and Operational Security

## Governance is decision infrastructure

Governance defines who may introduce risk, who reviews it, what evidence is required, who accepts residual risk, and how decisions are revisited. A policy document without operational gates is not governance.

The NIST Generative AI Profile organizes risk work through govern, map, measure, and manage. Use it as a risk-management frame, then translate relevant actions into owners, controls, tests, telemetry, and incident procedures for the product context.

## System inventory

Maintain an inventory of:

- Models, providers, versions, licenses, and approved purposes.
- Training/fine-tuning/evaluation data provenance where applicable.
- Prompts, policies, tools, MCP servers, and retrieval corpora.
- Regions, subprocessors, retention, and data flows.
- Owners, risk tier, deployment status, and expiration/review date.

Unknown systems cannot be governed or patched.

## Data lifecycle

For each data class, state:

```text
collection purpose → legal/organizational basis → minimization → processing
→ storage/access → sharing → retention → deletion → audit
```

Provider “zero retention” does not erase copies in your traces, queues, backups, browser analytics, or evaluation datasets. Deletion must cover derived artifacts and indexes according to policy.

## Threat modeling

Model assets, actors, trust boundaries, entry points, authority, and credible abuse cases. Include prompt injection, sensitive disclosure, supply-chain compromise, model theft, insecure output handling, excessive agency, denial of service, misinformation, and evaluation manipulation.

OWASP’s current GenAI guidance is a threat-discovery aid, not a substitute for product-specific analysis.

## Secrets and identities

Use workload identity or short-lived credentials where possible. Store secrets outside code and prompts, scope them narrowly, rotate them, and prevent logging. Authenticate services and authorize every sensitive resource/action based on current principal and tenant.

An API key proves possession, not user intent.

## Auditability

Record policy and approval decisions, actor, target, configuration version, effect ID, and outcome. Protect audit integrity and access. Do not claim explainability merely because a chain-of-thought transcript was stored; operational accountability comes from observable decisions and effects.

## Risk-tier autonomy

Classify actions by reversibility, scope, external visibility, financial effect, privacy, and physical/safety impact. Map tiers to:

- Allowed models and tools.
- Evaluation thresholds.
- Human approval.
- Sandbox and network constraints.
- Rollout population.
- Logging/audit requirements.
- Kill-switch and incident severity.

Review the classification when capabilities or use change.

## Responsible decommissioning

Retiring a feature requires disabling routes and credentials, ending queued work, preserving required records, deleting data under policy, removing stale flags and dashboards, notifying owners/users where needed, and verifying no shadow integration remains.

## Game considerations

Player chat, voice, biometrics, child accounts, user-generated content, and behavioral telemetry can be highly sensitive. Separate safety moderation from creative generation, constrain retention, provide reporting and appeal paths, and respect platform/region requirements. Research consent is not implied by ordinary gameplay telemetry.

## Review question

For any proposed logging or memory feature, ask: what decision needs this data, what is the least data that supports it, who can access it, when is it deleted, and how will deletion be verified?
