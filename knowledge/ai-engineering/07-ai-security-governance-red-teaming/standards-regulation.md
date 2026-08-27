---
id: ai-standards-regulation
title: Standards, Regulation, and Assurance Evidence
level: L3-L5
status: maintained
last_reviewed: 2026-08-27
prerequisites: [ai-governance-risk-management]
---

# Standards, Regulation, and Assurance Evidence

## Read each instrument by function

Do not treat frameworks as competing universal checklists.

| Instrument | Primary role | Important limit |
|---|---|---|
| NIST AI RMF + GenAI Profile | voluntary risk-management structure and actions | not a certification or law |
| NIST AI 100-2e2025 | adversarial ML terminology and taxonomy | not a complete product control framework |
| MITRE ATLAS | living adversary tactics, techniques, mitigations, cases | threat coverage does not establish compliance |
| OWASP GenAI/Agentic Top 10 | prioritized application-risk awareness and mitigations | generic categories need system-specific modeling |
| ISO/IEC 42001:2023 | requirements for an organizational AI management system | does not prove every AI system is safe |
| EU AI Act | binding risk-based legal obligations within scope | applicability depends on role, system, use, region, and dates |

## Current EU timeline snapshot

As of 27 August 2026, prohibited-practice and AI-literacy provisions have applied since February 2025; general-purpose AI obligations since August 2025; Commission/national enforcement powers and Article 50 transparency duties began applying on 2 August 2026. Official EU guidance states adjusted future dates for high-risk rules, including December 2027 and August 2028 categories.

This is time-sensitive and simplified. Verify the official regulation, Commission guidance, role definitions, exceptions, and current amendments with qualified counsel before implementation.

## Transparency is a system feature

Relevant systems may need to tell users they interact with AI, label or machine-mark generated/manipulated content, communicate limitations, or preserve documentation. Implement disclosure consistently across UI, APIs, exports, and downstream content, not as one footer.

Disclosure does not cure an otherwise prohibited or harmful system.

## Provider versus deployer

Obligations can differ for entities developing/placing a system or model and those deploying it. Open-source, downstream modification, import/distribution, general-purpose models, and high-risk integrations add role complexity.

Maintain a responsibility map across model provider, application provider, deployer, customer, tool provider, and data source. Contracts do not automatically transfer statutory responsibility.

## Standards use

ISO standards are often copyrighted and full text may require purchase. This atlas links to official summaries and does not redistribute protected standards. If an organization claims conformity or certification, work from legitimately obtained normative text and competent auditors.

## Control crosswalks

A crosswalk maps evidence across instruments to reduce duplication. It must preserve semantic differences. One access-control test may support several requirements, but similar labels do not imply identical scope.

Example evidence object:

```text
control: execute_tool_authorization
owner: identity-platform
implementation: policy version/hash
test: cross-tenant and expired-delegation suite
monitoring: denied/allowed effects and anomaly alert
mapped obligations: internal risk + selected framework references
limitations: cannot detect misuse within permitted purpose
last evidence / next review / exceptions
```

## Assurance case

An assurance case connects a claim to argument and evidence:

```text
Claim: cross-tenant document disclosure risk is acceptably controlled.
Argument: identity is propagated; filters enforce ownership at retrieval and assembly;
          caches are tenant/version scoped; adversarial isolation tests and monitoring exist.
Evidence: architecture, policy, tests, canary incidents, production metrics, review record.
Residual risk: privileged insider/control-plane compromise; separately treated.
```

This is stronger than a checklist tick because assumptions and evidence are inspectable.

## Legal humility

Engineers should understand the architecture implications of regulation, preserve accurate evidence, and escalate uncertainty. They should not invent universal legal conclusions from summaries. Jurisdiction, sector, contracts, intellectual property, employment, consumer, accessibility, privacy, and child-safety law may all matter.
