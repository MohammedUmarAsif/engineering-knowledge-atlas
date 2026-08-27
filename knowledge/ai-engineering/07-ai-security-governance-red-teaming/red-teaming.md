---
id: ai-red-teaming
title: Red Teaming and Security Evaluation
level: L3-L5
status: maintained
last_reviewed: 2026-08-27
prerequisites: [ai-threat-modeling, ai-prompt-injection, ai-identity-tools-sandboxing]
---

# Red Teaming and Security Evaluation

## Purpose

Red teaming is authorized adversarial testing intended to discover how a system can fail under realistic opposition and to improve defenses. It complements threat modeling and routine evaluation; it does not replace secure design or prove the absence of vulnerabilities.

## Distinguish activities

- Vulnerability assessment: systematic identification and prioritization of weaknesses.
- Penetration test: authorized attempt to demonstrate exploitability and impact within scope.
- Adversarial evaluation: measurement under challenging or malicious inputs.
- Red team: goal-oriented emulation that may combine technical and human pathways.
- Audit: assessment against defined criteria and evidence requirements.
- Bug bounty: governed external reporting program with explicit scope and terms.

## Rules of engagement

Before testing, define:

- Written authorization and owners.
- Systems, tenants, models, data, tools, and environments in scope.
- Allowed techniques and prohibited actions.
- Test accounts and synthetic data.
- Rate/cost limits.
- Privacy and evidence handling.
- Safety stop conditions and emergency contacts.
- Reporting, remediation, retest, and disclosure process.

Never use production customer data or real external targets merely to make a test realistic.

## Hypothesis-driven tests

Weak: “try to jailbreak it.”

Strong: “Given attacker-controlled retrieved text and a normal user session, the system must never execute a write tool outside the user-approved target set.”

The strong form states attacker capability, entry point, asset, boundary, and observable failure.

## Layered outcomes

Record separately:

1. Model produced policy-violating content.
2. Model proposed unauthorized action.
3. Policy or approval rejected it.
4. Executor attempted it.
5. External effect occurred.
6. Monitoring detected it.
7. Response contained and recovered.

This prevents a blocked model proposal from being reported as a catastrophic breach—or a successful harmful effect from being hidden by average refusal scores.

## Test corpus

Cover direct and indirect influence, multiple modalities/languages, retrieval and memory poisoning, tool-result manipulation, role/identity boundaries, output rendering, resource exhaustion, dependency failure, data leakage, unsafe actions, and legitimate difficult requests that must still work.

Use safe canaries and simulators. Avoid storing reusable harmful payload libraries without access controls and purpose.

## Metrics

- Attack success by threat scenario and layer.
- Unauthorized-effect rate.
- Detection and containment rate/time.
- False-positive and benign-task regression.
- Cost, attempts, and attacker access assumptions.
- Coverage across assets, entry points, and control layers.
- Fix validation and recurrence.

One successful attack is sufficient to disprove a universal safety claim. Many failed attacks do not prove the claim true.

## Automation and human creativity

Automated tools improve breadth, regression, and repeatability. Human testers reason across interfaces, organizational behavior, ambiguous requirements, and novel chains. Use both and preserve reproducible transcripts, versions, seeds/configuration, and environment state.

## Findings

A finding should include title, severity rationale, affected asset, prerequisites, safe reproduction, observed evidence, impact, violated invariant, causal control gap, remediation options, residual risk, owner, and retest result.

Rank by demonstrated or plausible impact under explicit assumptions—not by how dramatic generated text appears.

## Purple teaming

Red testers and defenders collaborate: execute an authorized scenario, inspect whether telemetry observed each step, tune controls, rerun, and add regression coverage. The output is improved prevention and detection, not a scoreboard.

## Game scenario

Use a closed test world with synthetic players, fake inventory, isolated moderation, and no public publishing. Test whether user-generated text can influence NPC memory or actions beyond authored boundaries while measuring false positives on creative player expression.
