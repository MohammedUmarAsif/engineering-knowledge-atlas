---
id: rag-generation-evidence-citations
title: Generation, Evidence, and Citations
level: L2-L4
status: maintained
last_reviewed: 2026-08-27
prerequisites: [advanced-rag-patterns]
---

# Generation, Evidence, and Citations

## Evidence contract

The generator should receive evidence as addressable records, not anonymous prose:

```text
source_id, document_version, page/region, authority, effective_date, content
```

The application (not the model) resolves source IDs into links and checks access.

## Claim discipline

An answer contains claims. Each consequential factual claim should be:

- directly supported by cited evidence;
- clearly inferred from cited evidence;
- identified as general model knowledge when permitted;
- or withheld when support is insufficient.

Groundedness asks whether claims follow from context. Correctness asks whether they are true relative to the task/world. A faithfully repeated outdated document can be grounded but wrong for the current question.

## Conflicts

When sources disagree:

1. preserve both rather than averaging them;
2. compare authority, scope, jurisdiction, version, and effective date;
3. state the conflict visibly;
4. ask for missing context or escalate when policy cannot resolve it.

## Citation generation

Safer pattern:

1. provide stable evidence IDs;
2. require claims to reference only supplied IDs;
3. parse and validate every referenced ID;
4. verify that cited evidence supports the claim;
5. render human-readable citations in application code.

This prevents plausible fabricated URLs, but claim-support validation is still required.

## Abstention

Define explicit conditions:

- no authorized evidence;
- insufficient retrieval confidence under a validated policy;
- conflicting authority;
- required source unavailable;
- high-risk request requiring human review.

Do not ask the model to invent a numeric confidence unless that score is calibrated against observed outcomes.

## Game transfer

For lore-aware dialogue, evidence might be canon events, character knowledge, or player-specific history. The character should not cite documents to the player, but the development/debugging system should retain provenance so writers can inspect why dialogue was produced.

## Interview scenario

An answer is factually correct but cites an irrelevant page. Explain why answer accuracy alone would miss this failure and how claim-level citation evaluation works.
