---
id: ai-security-mastery
title: AI Security, Governance, and Red Teaming Mastery Defense
level: L3-L5
status: maintained
last_reviewed: 2026-08-27
prerequisites: [ai-security-research-frontier, ai-security-implementation-patterns, ai-standards-regulation]
---

# AI Security, Governance, and Red Teaming Mastery Defense

## Rule

Answer aloud without notes. Name system boundary, attacker capability, affected asset, causal pathway, control layer, evidence, residual risk, and owner. Listing risk names does not pass.

## Foundations and threat modeling

1. Separate security, safety, privacy, reliability, ethics, governance, and compliance using one scenario.
2. Define vulnerability, threat, risk, control, residual risk, and assurance.
3. Build an attacker model for a public RAG assistant with authenticated tools.
4. Draw a data/control-flow threat pathway from poisoned webpage to external effect.
5. Apply ordinary web security and AI-specific analysis without replacing either.
6. Explain how OWASP, MITRE ATLAS, and NIST AML taxonomy complement one another.

## Injection, data, and authority

7. Explain why delimiters and hidden prompts are not hard security boundaries.
8. Design defense in depth for indirect prompt injection.
9. Separate model compromise, unauthorized proposal, attempted execution, and confirmed effect.
10. Compare poisoning, evasion, privacy, misuse, and availability attacks.
11. Secure a model/data/software artifact lineage.
12. Explain hallucinated-package supply-chain risk and prevention.
13. Apply least functionality, permission, and autonomy to an email agent.
14. Bind approval to an immutable action and explain time-of-check/time-of-use risk.
15. State what a sandbox contains and what it cannot contain.

## Privacy and red teaming

16. Map deletion through raw data, embeddings, memories, traces, evaluations, providers, and backups.
17. Distinguish pseudonymization, anonymization, minimization, and purpose limitation.
18. Write rules of engagement for an authorized agent red team.
19. Turn “jailbreak the assistant” into a falsifiable effect-level hypothesis.
20. Design a test corpus with adversarial and difficult benign cases.
21. Interpret one successful attack and one thousand failed attacks without overclaiming.
22. Write a finding that developers can causally remediate and retest.

## Governance and standards

23. Apply Govern, Map, Measure, and Manage to a game dialogue feature.
24. Explain what ISO/IEC 42001 certification would and would not establish.
25. Build a control evidence object reusable across frameworks.
26. Explain the current dated EU AI Act timeline without presenting legal advice.
27. Design meaningful human oversight, appeal, and recourse.
28. Name change events that force risk reassessment.

## Detection and research

29. Detect an attack chain using identity, retrieval, tool, and outcome signals.
30. Design narrow kill switches and post-incident reconciliation.
31. Explain why blocking the incident phrase is not causal remediation.
32. Critique a paper claiming 95% prompt-injection prevention.
33. Propose a Game AI security or safety hypothesis with affected-player utility metrics.

## System-design defense

Secure a multi-tenant assistant that reads private documents, browses public sites, executes approved code in sandboxes, and can email reports.

Your defense must include:

- Assets, actors, trust boundaries, and attacker capabilities.
- Data provenance and tenant isolation.
- Direct/indirect injection pathway.
- Identity propagation, tool scope, approval binding, and egress.
- Sandbox and artifact handling.
- Privacy lifecycle and deletion.
- Red-team scope, cases, metrics, and safe fixtures.
- Prevention, detection, containment, response, and recovery.
- Governance roles, evidence, residual risk, and reassessment.
- Simpler design choices that remove authority or data.

## Pass criterion

You pass when you can convert broad risk language into a specific, testable, owned assurance argument—and explain honestly what remains uncertain.
