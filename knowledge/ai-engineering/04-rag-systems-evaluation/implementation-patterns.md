---
id: rag-implementation-patterns
title: RAG Evidence Contracts in Python and C++
level: L2-L4
status: maintained
last_reviewed: 2026-08-27
prerequisites: [rag-generation-evidence-citations]
---

# RAG Evidence Contracts in Python and C++

## Purpose

The paired examples implement the most important boundary after retrieval: claims may cite only supplied evidence, every citation must resolve, and unsupported text is rejected by a deliberately simple validator.

- [Python example](../../../examples/rag-systems-evaluation/python/evidence_contract.py)
- [C++ example](../../../examples/rag-systems-evaluation/cpp/evidence_contract.cpp)

The validator is intentionally lexical and conservative. Production semantic entailment requires stronger methods and human calibration; the simple mechanism remains useful because its assumptions are visible.

## Flow

1. Application retrieves authorized `Evidence` objects.
2. Generator returns structured `Claim` objects with evidence IDs.
3. Application rejects unknown citations.
4. Application checks a minimal support condition.
5. Renderer turns validated IDs into inspectable citations.

## Python versus C++

- Python dataclasses keep orchestration concise and are natural for evaluation experiments.
- C++ value types and `std::unordered_map` make ownership and lookup explicit for native/game systems.
- Both require runtime validation because external model output crosses a trust boundary.

## Game adaptation

Replace document evidence with canon events or character observations. A character dialogue claim may reference internal evidence IDs for debugging even if citations are not shown to the player. Access rules should prevent a character from “remembering” an event it never observed.

## Think before running

- Why should the model not generate arbitrary URLs?
- Why can lexical overlap reject a valid paraphrase?
- Why can it accept a misleading claim sharing the same words?
- Which deterministic checks remain useful even after adding a semantic evaluator?
