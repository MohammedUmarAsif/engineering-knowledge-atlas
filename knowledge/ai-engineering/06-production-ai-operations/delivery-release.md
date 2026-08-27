---
id: ai-delivery-release
title: Versioning, Delivery, and Safe Release
level: L3-L5
status: maintained
last_reviewed: 2026-08-27
prerequisites: [production-system-map]
---

# Versioning, Delivery, and Safe Release

## An AI release is a behavior bundle

Traditional CI may compile code and run tests. AI delivery must also bind prompts, policies, schemas, retrieval configuration, evaluation sets, model routes, and data migrations into an auditable release description.

Do not let a mutable dashboard prompt change production behavior outside the delivery record.

## Pipeline

```text
change → static checks → unit/contract tests → offline evals → security tests
       → immutable artifact/config → staging → shadow → canary → promote
                                                        └────→ rollback
```

Each gate targets a different failure class. Offline evaluation cannot prove production capacity; a canary cannot efficiently rediscover schema errors that unit tests should catch.

## Test pyramid for AI systems

- Deterministic unit tests: parsing, policy, routing, budgets, citations, state transitions.
- Contract tests: provider, tool, MCP, index, and schema compatibility using controlled doubles plus limited live checks.
- Component evaluations: retrieval, classification, generation, safety.
- End-to-end scenarios: representative user tasks and effects.
- Load and failure tests: queue, timeout, partial failure, cancellation, failover.
- Production observation: sampled quality, user outcomes, incidents.

Keep deterministic assertions deterministic. Do not replace exact invariants with a model judge.

## Immutable artifacts

Build once and promote the same artifact. Record hashes for containers, prompt bundles, policies, evaluation datasets, and indexes where feasible. Rebuilding “the same commit” later may resolve different dependencies or base images.

Pin dependencies, generate provenance, scan artifacts, and separate secrets from builds. A secret embedded in an image remains in its layers even after a later deletion.

## Rollout strategies

- Shadow: new route receives copied traffic but cannot affect the user. Useful for compatibility and performance; be careful about duplicate cost and personal-data processing.
- Canary: small real population receives new behavior. Detects production interactions but needs guardrails and statistically meaningful evaluation.
- Blue/green: old and new stacks coexist; switching is fast but data/schema compatibility matters.
- Feature flag: decouples activation from deployment. Flags are control-plane code and need owners, expiry, and audit.
- A/B test: estimates product impact. It is not primarily a safety mechanism.

## Rollback is a designed capability

Rollback may involve code, prompt, route, model, policy, index, or schema. A database or index migration can make old code incompatible. Prefer expand–migrate–contract changes, dual reads/writes only when justified, and explicit compatibility windows.

Define automatic halt conditions before rollout: safe-success regression, latency tail, cost per success, policy violations, or provider errors. Avoid deciding thresholds while emotionally defending a release.

## Model changes

A model alias may move without your deployment. Prefer pinned snapshots where providers expose them; otherwise run scheduled sentinels and treat provider changes as external releases.

Changing to a “better” model can alter tool selection, refusal behavior, formatting, latency, tokenization, and cost. Re-run system evaluation, not only a generic benchmark.

## Evaluation-set governance

Version test cases, expected behavior, rubric, evaluator, and adjudication notes. Protect holdout tasks from prompt tuning. Add incident regressions without allowing the suite to become a pile of near-duplicates.

## Senior review

Ask what exact behavior bundle is shipping, what evidence supports it, what population first receives it, what signal stops it, and whether rollback restores the entire compatible bundle.
