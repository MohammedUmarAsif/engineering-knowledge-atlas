---
id: ai-security-governance-red-teaming
title: AI Security, Governance, and Red Teaming
level: L2-L5
status: maintained
last_reviewed: 2026-08-27
prerequisites: [production-ai-operations, agent-security-production]
---

# AI Security, Governance, and Red Teaming

## First principle

AI assurance is the disciplined production of evidence that a particular system, used by particular people under stated conditions, keeps risk within an explicitly accepted boundary.

A “safe model” does not imply a safe product. Security and harm emerge from the model’s data, instructions, interfaces, authority, environment, users, operators, and failure handling.

## Diagnostic — skip only if every distinction is defensible

1. Separate security, safety, privacy, reliability, ethics, governance, and compliance.
2. Define asset, threat actor, vulnerability, threat, risk, control, residual risk, and assurance evidence.
3. Why is an OWASP list a discovery aid rather than a complete threat model?
4. Model direct versus indirect prompt injection as data and authority flow.
5. Explain why system-prompt secrecy is not a security boundary.
6. Compare poisoning, evasion, privacy, misuse, supply-chain, and availability attacks.
7. How can an agent be overprivileged even when every tool call is authenticated?
8. Which controls prevent, detect, contain, recover, and compensate?
9. Design tenant isolation across ingestion, retrieval, caching, generation, tools, and logs.
10. When does sandboxing help, and what escapes its boundary through network or credentials?
11. Define a red-team scope, authorization, rules of engagement, stop condition, and evidence standard.
12. Why does one jailbreak success neither prove total insecurity nor permit dismissal as an edge case?
13. Distinguish vulnerability discovery, adversarial evaluation, penetration testing, and a compliance audit.
14. How do NIST AI RMF, NIST AML taxonomy, MITRE ATLAS, ISO/IEC 42001, and OWASP serve different purposes?
15. What changed in EU AI Act application and transparency enforcement by August 2026?
16. How would you evaluate harm to players without equating moderation score with game safety or enjoyment?

If any answer is vague, begin with [Security, Safety, Privacy, and Governance](assurance-foundations.md). If all are strong, attempt the [Mastery Defense](mastery.md).

## Assurance loop

```text
context → assets/actors → threats → risk → controls → tests/evidence
    ▲                                                    │
    └──── monitor ← incidents/changes ← residual risk ──┘
```

The loop restarts when the model, data, tools, users, law, threat landscape, or intended use changes.

## Reading order

1. [Security, Safety, Privacy, and Governance](assurance-foundations.md)
2. [Threat Modeling AI Systems](threat-modeling.md)
3. [Prompt Injection and the Confused Deputy](prompt-injection.md)
4. [Data, Model, and Supply-Chain Security](data-model-supply-chain.md)
5. [Identity, Tools, Sandboxes, and Least Agency](identity-tools-sandboxing.md)
6. [Privacy and the Data Lifecycle](privacy-data-lifecycle.md)
7. [Red Teaming and Security Evaluation](red-teaming.md)
8. [Governance and Risk Management](governance-risk.md)
9. [Standards, Regulation, and Evidence](standards-regulation.md)
10. [Detection, Response, and Recovery](detection-response.md)
11. [Tools and Repository Map](tools-and-repositories.md)
12. [Research Frontier and Game AI Safety](research-frontier.md)
13. [Python and C++ Policy Mechanics](implementation-patterns.md)
14. [Mastery and Interview Defense](mastery.md)

## Safe-use boundary

Red-team material here is defensive and controlled. It teaches scoping, test design, measurement, and remediation—not instructions for attacking systems you do not own or have explicit authorization to assess.
