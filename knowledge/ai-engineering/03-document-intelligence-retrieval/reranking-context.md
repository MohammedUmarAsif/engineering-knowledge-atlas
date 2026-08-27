---
id: reranking-context-assembly
title: Reranking and Context Assembly
level: L2-L4
status: maintained
last_reviewed: 2026-08-27
prerequisites: [retrieval-models]
---

# Reranking and Context Assembly

## Intuition

Retrieval creates a candidate pool. Reranking decides which evidence deserves scarce context space. Context assembly decides how that evidence is presented without hiding provenance or contradictions.

## Candidate pipeline

1. Apply authorization and hard metadata filters.
2. Retrieve lexical, dense, or multimodal candidates.
3. Merge and deduplicate.
4. Rerank against the actual query/task.
5. diversify when repeated chunks crowd out coverage.
6. expand parent or neighbouring context where needed.
7. enforce token and source budgets.
8. serialize with stable source identifiers.

Authorization must not be delegated to reranking. Forbidden documents should not become candidates.

## Rerankers

- cross-encoders score a query and candidate jointly;
- late-interaction models retain fine-grained representations;
- LLM rerankers can reason over complex criteria but add latency, cost, variance, and prompt risk;
- deterministic business rules handle authority, date, jurisdiction, and required document classes.

Use the cheapest stage capable of enforcing each criterion.

## Context assembly

Preserve:

- source ID and title;
- page/section/region;
- document version/effective date;
- exact evidence boundaries;
- neighbouring definitions or exceptions;
- conflict between sources;
- trust and authority level.

Do not silently blend conflicting sources into a synthetic consensus.

## Lost-in-the-middle and competition

Adding more evidence can reduce performance when relevant passages compete with noise or duplicated chunks. Order, delimit, and label evidence; test where critical facts are placed; prefer diversity and sufficient context over raw top-k.

## Citations

A citation should support the specific claim, resolve to inspectable evidence, and remain stable across reprocessing. Citation correctness is its own evaluation target. A generated citation string is not provenance unless the application can verify it against supplied evidence.

## Senior questions

- Is the reranker optimizing relevance, authority, freshness, or answerability?
- How are conflicts and missing evidence represented?
- Can context be reproduced after a model or index update?
- Which evidence was available but omitted?

## Interview scenario

The correct clause is retrieved at rank 8 but never reaches the model because five near-duplicate chunks consume the budget. Diagnose and redesign the candidate-to-context path.
