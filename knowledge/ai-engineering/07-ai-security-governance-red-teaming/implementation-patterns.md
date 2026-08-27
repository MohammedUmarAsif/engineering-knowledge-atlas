---
id: ai-security-implementation-patterns
title: Effect Authorization in Python and C++
level: L2-L4
status: maintained
last_reviewed: 2026-08-27
prerequisites: [ai-identity-tools-sandboxing]
---

# Effect Authorization in Python and C++

## Purpose

The paired examples implement the boundary prompt injection must not cross. A model proposes an effect, but code authorizes it using authenticated principal, tenant, allowed tool, exact target, risk level, approval binding, and expiry.

- [Python example](../../../examples/ai-security-governance-red-teaming/python/effect_policy.py)
- [C++ example](../../../examples/ai-security-governance-red-teaming/cpp/effect_policy.cpp)

No model, credential, network, or real external effect is involved.

## Policy flow

```text
untrusted model proposal
  → validate typed fields
  → match capability to principal + tenant + tool + target
  → check expiry
  → require action-bound approval for high-risk effect
  → allow executor or return explicit denial
```

## Why target binding matters

Permission to update `repo/game-docs` is not permission to update every repository. Wildcard capabilities expand blast radius. The examples use exact targets so the policy is easy to audit.

## Why approval is hashed

Approval binds to the canonical material action. If a model changes amount, recipient, tool, or target after the user reviews it, the computed binding changes and authorization fails.

The tutorial uses a non-cryptographic demonstration hash. Production approval requires canonical serialization, collision-resistant cryptography, authenticated approver identity, integrity-protected storage, nonce/replay handling, and policy/version context.

## Python versus C++

- Python dataclasses and enums express policy records concisely.
- C++ value types and `std::optional` make absence and ownership explicit.
- Both treat model output as data, never as executable policy.
- Both return structured denial reasons so telemetry can distinguish expiry, scope, approval, and tenant failure.

## Missing production controls

- Identity-provider token verification.
- Distributed revocation and freshness.
- Cryptographic approval signatures.
- Hierarchical resources and policy composition.
- Purpose limitation and attribute-based policy.
- Rate/financial/effect budgets.
- Tamper-resistant audit storage.
- Race-free check-and-execute transaction.

The final item is crucial: authorization can become stale between checking and effect. Revalidate at execution and use resource versions or transactional enforcement.

## Exercises

1. Add an approval expiry shorter than the capability expiry.
2. Bind approval to resource version and policy version.
3. Prevent replay after one successful effect.
4. Add a per-tenant amount budget.
5. Test that malicious document text cannot create a capability.
6. Add a low-risk read that needs no approval but remains tenant-scoped.

## Game transfer

An NPC may propose `grant_quest_hint` for its current player and quest. It must never mint inventory or affect another player merely because dialogue context instructed it to do so.
