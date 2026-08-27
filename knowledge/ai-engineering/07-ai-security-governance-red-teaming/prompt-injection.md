---
id: ai-prompt-injection
title: Prompt Injection and the Confused Deputy
level: L3-L5
status: maintained
last_reviewed: 2026-08-27
prerequisites: [ai-threat-modeling, instructions-and-context-construction]
---

# Prompt Injection and the Confused Deputy

## The root ambiguity

Language models process instructions and data through the same token channel. A retrieved webpage can contain text that resembles a developer instruction. Delimiters and labels help the model reason about provenance, but do not create the hard separation that memory protection creates in an operating system.

## Direct and indirect injection

- Direct: the interacting user supplies conflicting or malicious instruction.
- Indirect: attacker-controlled content enters through a document, webpage, email, tool result, image, metadata, memory, or peer agent.

Indirect injection is particularly dangerous when the victim user legitimately authorizes access and the attacker controls only the content being processed.

## Confused deputy

The deputy has authority. The attacker tricks it into using that authority for the attacker’s purpose.

```text
attacker content ──influences──► model decision
user authority ───enables──────► tool
model proposal ───weak check───► effect on protected asset
```

Fixing the problem requires separating influence from authority. The model may suggest an action; deterministic policy must decide whether the authenticated principal intended and may perform that exact action on that exact target.

## System prompts are policy hints

A hidden system prompt may improve behavior, but secrecy is fragile: outputs can reveal fragments, integrations can leak it, and models may follow conflicting content. Never store secrets there or rely on concealment to protect permissions.

## Control stack

### Reduce exposure

- Retrieve only necessary content.
- Strip active content and dangerous file forms where appropriate.
- Separate instructions from quoted data with provenance.
- Avoid feeding irrelevant tool descriptions or credentials.

### Reduce authority

- Give the run only required tools and scopes.
- Separate read from write.
- Bind actions to user, tenant, resource, purpose, and time.
- Constrain filesystem and network egress.

### Validate intent and action

- Require structured action proposals.
- Apply deterministic authorization below the model.
- Verify arguments against business invariants.
- Require meaningful approval for consequential effects.
- Re-check policy at execution time.

### Detect and contain

- Record provenance and influence paths.
- Detect unusual tool/target combinations and data movement.
- Limit rate, volume, recipients, and effect size.
- Provide kill switches and reconciliation.

No one layer guarantees prevention. The goal is to prevent untrusted text from becoming unconstrained authority.

## Why input/output filters are insufficient

An injected instruction can be semantically subtle, multilingual, encoded in an image, or expressed through apparently legitimate data. A tool request can also be harmful while containing no prohibited words. Filters remain useful for known patterns and policy classes, but authorization and containment protect assets when classification fails.

## Safe testing

Use synthetic documents in an isolated environment that request benign canary actions the system should never perform, such as accessing a fake forbidden record. Test multiple carriers and transformations without using real credentials or external targets.

Measure:

- Attack task success.
- Unauthorized proposal rate.
- Unauthorized execution rate—the critical boundary.
- Benign-task degradation.
- Detection and approval behavior.
- Cost and latency.

An agent can remain susceptible at the model layer yet safe at the effect layer if proposals are contained. Report both.

## Game transfer

A player names an item with text designed to influence an NPC assistant. Treat the name as quoted world data. The NPC may reference it in dialogue but cannot gain economy, moderation, file, or account authority. Deterministic game code validates every state mutation.

## Interview answer

Prompt injection is not fully solved by better prompting because instructions and data share a semantic channel. Reduce exposure, isolate provenance, minimize authority, authorize below the model, validate effects, monitor anomalies, and assume the model-level defense can fail.
