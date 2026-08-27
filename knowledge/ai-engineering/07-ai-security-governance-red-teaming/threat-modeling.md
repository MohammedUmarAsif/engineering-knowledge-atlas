---
id: ai-threat-modeling
title: Threat Modeling AI Systems
level: L3-L5
status: maintained
last_reviewed: 2026-08-27
prerequisites: [ai-assurance-foundations, production-system-map]
---

# Threat Modeling AI Systems

## Begin with the system diagram

Threat modeling is structured reasoning about what can go wrong, who can cause it, how, why it matters, and which evidence supports controls. Start from the real data/control-flow diagram—not a generic list of AI risks.

Mark:

- Assets and sensitive decisions.
- Actors and identities.
- Trust boundaries.
- Data stores and flows.
- Model, retrieval, tool, and human interfaces.
- External dependencies and control planes.
- Authority changes and irreversible effects.

## Attacker model

State capabilities:

- Can submit direct prompts or upload files.
- Can control content later retrieved by another user.
- Has a valid low-privilege account.
- Can publish packages, models, datasets, or MCP servers.
- Can observe only outputs, or access gradients/weights/training.
- Can repeat queries at scale.
- Controls a tool result or external webpage.
- Is an insider with configuration or data access.

Security claims are meaningless without an attacker model. A defense against naive direct prompts may not address a patient attacker controlling retrieved content.

## Threat pathways

Trace attacker-controlled influence to an asset:

```text
untrusted document → retrieval → model interprets instruction
→ proposes privileged tool → weak authorization → external disclosure
```

The model’s susceptibility is one link. Breaking the pathway at tool scope, authorization, approval, network egress, or output policy can contain impact even when injection succeeds.

## Traditional and AI-specific analysis

Apply ordinary application security first: identity, access control, injection, SSRF, XSS, secrets, dependency compromise, deserialization, isolation, logging, and availability remain relevant.

Then examine AI-specific or amplified surfaces:

- Prompt and context instruction/data ambiguity.
- Training, fine-tuning, retrieval, and memory poisoning.
- Model extraction and privacy leakage.
- Adversarial inputs and evasion.
- Unsafe generated output consumed as code or instructions.
- Excessive agency and long-horizon effect composition.
- Hallucinated dependencies or entities exploited through the supply chain.
- Unbounded token, tool, and compute consumption.

## Taxonomies are maps

- OWASP GenAI Top 10 prioritizes common application risk categories.
- OWASP Agentic Top 10 focuses on autonomous systems.
- MITRE ATLAS models adversary tactics and techniques across predictive, generative, and agentic systems.
- NIST AI 100-2e2025 supplies adversarial ML taxonomy and terminology.

Map findings to them for communication and coverage, but do not force a product-specific threat into one label.

## Risk analysis

For each scenario record:

- Preconditions and attacker effort.
- Exposed population and blast radius.
- Confidentiality, integrity, availability, safety, financial, legal, and trust impact.
- Existing controls and evidence.
- Detectability and recovery.
- Uncertainty and assumptions.
- Owner and treatment decision.

Prioritize plausible high-impact paths, not the largest number of theoretical findings.

## Abuse cases

Write misuse stories from goals rather than payloads:

- A user tries to make the assistant reveal another tenant’s documents.
- A content publisher plants instructions intended for downstream agents.
- A compromised dependency changes model-loading behavior.
- A player coordinates many accounts to exhaust dialogue inference capacity.

For each, define observable success and safe test fixtures.

## Control validation

“We sanitize input” is not evidence. State the transformation, covered syntax/medium, bypass assumptions, unit/property tests, adversarial cases, telemetry, and residual risk. Input filtering rarely solves authority misuse on its own.

## Game example

For a mod-enabled game, treat mods, save files, player names, chat, community wikis, asset metadata, and remote content as untrusted. Trace whether any can influence an assistant with filesystem, account, economy, moderation, or publishing authority.

## Deliverable

A useful threat model produces a diagram, prioritized scenarios, control map, test plan, residual-risk decisions, and owners. A threat-model meeting without durable artifacts is a conversation, not an assurance process.
