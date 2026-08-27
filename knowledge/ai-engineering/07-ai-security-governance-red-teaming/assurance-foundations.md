---
id: ai-assurance-foundations
title: Security, Safety, Privacy, and Governance
level: L2-L5
status: maintained
last_reviewed: 2026-08-27
prerequisites: [ai-security-governance-red-teaming]
---

# Security, Safety, Privacy, and Governance

## Different questions

- Security: can an adversary violate confidentiality, integrity, or availability?
- Safety: can operation cause unacceptable harm, including without an adversary?
- Privacy: are data collection, inference, use, disclosure, retention, and rights appropriately controlled?
- Reliability: does the system provide the intended outcome under expected conditions?
- Ethics: what ought the system do, whom does it benefit or burden, and which values conflict?
- Governance: who decides, owns, reviews, evidences, and corrects these matters?
- Compliance: which binding obligations and chosen standards apply, and can conformance be demonstrated?

The categories overlap without collapsing. A perfectly available surveillance system can be privacy-invasive. A secure model can produce systematically harmful decisions. A compliant process can still leave material residual risk.

## Core vocabulary

- Asset: something valuable—data, identity, money, model, service, trust, player experience.
- Threat actor: entity capable of causing harm, intentionally or accidentally.
- Vulnerability: weakness that can be exploited or triggered.
- Threat: plausible event or action capable of harm.
- Impact: consequence if it occurs.
- Likelihood: context-dependent estimate of occurrence or exploitation.
- Risk: uncertainty about objectives, often analyzed through likelihood and impact.
- Control: measure that modifies risk.
- Residual risk: risk remaining after controls.
- Assurance: justified confidence supported by evidence.

A risk matrix is a decision aid, not physics. Ordinal “high × medium” arithmetic can conceal uncertainty and stakeholder disagreement.

## System versus model assurance

Model evaluations probe capabilities and behavior under a test interface. System assurance additionally covers authentication, retrieval, prompts, tools, rendering, storage, users, monitoring, and response.

Example: a model emits unsafe HTML. If the UI escapes it, the product prevents script execution. If the UI renders it directly, ordinary insecure output handling converts model text into a web vulnerability.

## Controls by function

- Prevent: eliminate capability or block entry.
- Deter: increase perceived consequence.
- Detect: reveal attempted or actual violation.
- Contain: limit blast radius.
- Respond: coordinate immediate action.
- Recover: restore safe service and reconcile effects.
- Compensate: reduce risk when a preferred control is infeasible.

Defense in depth requires controls that fail differently. Five prompt instructions are not five independent layers.

## Risk acceptance

Not every risk can be eliminated. Acceptance should record owner, affected stakeholders, rationale, evidence, constraints, monitoring, expiry/review date, and conditions that force reconsideration.

Engineers identify and communicate risk; accountable leaders accept business risk. Neither should silently push the decision onto end users through vague terms.

## Misuse versus malfunction

- Misuse: system works as designed for a harmful purpose.
- Malfunction: system fails to meet intended behavior.

Controls differ. Better accuracy may worsen misuse capability. A moderation model may reduce prohibited content but not prevent authorized tools from enabling an abusive objective.

## Sociotechnical boundary

People adapt to systems. Operators may overtrust fluent output, users may learn to game decisions, reviewers may experience fatigue, and organizations may route around slow controls. Assurance must examine incentives, interfaces, training, staffing, appeals, and power—not only code.

## Game transfer

Safety in a game includes account/data security, child protection, harassment, economic integrity, accessibility, psychological experience, authored boundaries, and platform obligations. A dialogue filter is one control within this larger system.

## Checkpoint

A companion NPC reveals a private player conversation in public dialogue. Classify the event across security, privacy, safety, reliability, governance, and compliance. Explain why several classifications can simultaneously be true.
