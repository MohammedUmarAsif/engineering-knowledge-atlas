---
id: ai-governance-risk-management
title: Governance and Risk Management
level: L3-L5
status: maintained
last_reviewed: 2026-08-27
prerequisites: [ai-assurance-foundations, ai-red-teaming]
---

# Governance and Risk Management

## Governance makes decisions repeatable

Governance connects organizational objectives and values to inventories, roles, risk tiers, controls, evidence, release gates, monitoring, incident response, and continual improvement.

Its purpose is not maximum paperwork. It is to ensure consequential decisions are explicit, owned, reviewable, and revisited when context changes.

## NIST AI RMF loop

- Govern: policies, accountability, culture, inventory, oversight.
- Map: context, purpose, stakeholders, impacts, dependencies.
- Measure: evaluations, monitoring, uncertainty, control effectiveness.
- Manage: prioritize, treat, accept, communicate, and monitor risk.

Govern is cross-cutting. Measurement without context produces irrelevant scores; management without governance produces ownerless actions.

## AI management system

ISO/IEC 42001 specifies requirements for establishing and continually improving an AI management system. Its Plan–Do–Check–Act structure operates at organizational level. It does not certify that each model output is correct or replace product-specific security testing.

## Inventory and classification

Maintain systems—including unofficial “shadow AI”—with owner, purpose, affected users, model/provider, data, tools, autonomy, regions, risk tier, legal basis, evaluations, deployment, and review date.

Classification dimensions:

- Decision consequence and reversibility.
- Population and vulnerable groups.
- Data sensitivity.
- Autonomy and reachable authority.
- External visibility and deception risk.
- Scale and systemic dependence.
- Human oversight and contestability.

## Roles

- Product owner defines intended outcome and accepts product tradeoffs.
- Engineering owns implementation and operational controls.
- Security models adversaries and validates protection.
- Privacy/legal interpret applicable obligations.
- Safety/responsible-AI specialists assess broader harms.
- Domain experts define valid behavior and affected stakes.
- Independent reviewers challenge evidence where risk warrants.
- Executives or named risk owners accept material residual risk.

Separation of duties reduces self-approval, but unclear veto/escalation creates paralysis. Define decision rights.

## Evidence package

For a release or review, include:

- Intended use and excluded use.
- System/data-flow and model/tool inventory.
- Risk and impact assessments.
- Threat model and control mapping.
- Evaluation/red-team results with limitations.
- Privacy/data lifecycle.
- Human oversight and user disclosure.
- Operations, incidents, fallback, and decommissioning.
- Residual risks, approvals, owners, and expiry.

Evidence should be generated from delivery and operations where possible, not assembled manually once per audit.

## Control effectiveness

Track whether a control prevents or detects the actual scenario, its coverage, false positives, bypass assumptions, owner, dependencies, test frequency, and last evidence. “Policy exists” measures implementation presence, not effectiveness.

## Appeals and recourse

When AI materially affects people, provide understandable notice, correction, human review, appeal, and remediation appropriate to context. Human-in-the-loop is not meaningful if reviewers lack time, authority, information, or independence.

## Change triggers

Reassess when intended use, model, data, population, autonomy, region, provider, tool, law, threat evidence, or incident history changes. Periodic annual review alone is too slow for mutable AI systems.

## Anti-patterns

- Ethics principles without engineering gates.
- A committee with no system inventory.
- A model card used as full product assurance.
- Compliance treated as maximum acceptable safety.
- Risk accepted indefinitely without owner or expiry.
- Red team findings closed by prompt edits without causal retest.

## Research transfer

For a PhD study involving players, governance includes ethics review, consent, recruitment fairness, data minimization, preregistration where useful, adverse-event handling, withdrawal, reproducibility, and honest reporting—not only institutional paperwork.
