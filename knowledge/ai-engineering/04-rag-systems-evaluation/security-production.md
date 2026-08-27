---
id: rag-security-production
title: RAG Security and Production Operations
level: L3-L5
status: maintained
last_reviewed: 2026-08-27
prerequisites: [rag-evaluation-science]
---

# RAG Security and Production Operations

## Threat surfaces

- malicious uploads and parser exploits;
- direct and indirect prompt injection;
- cross-tenant retrieval;
- embedding/index poisoning;
- unauthorized source connectors;
- stale or revoked documents;
- source-existence leakage;
- sensitive information in embeddings, logs, caches, and evaluations;
- denial of wallet through large files, query expansion, loops, or reranking;
- compromised models, packages, or checkpoints.

## Authorization architecture

Bind every source and derived chunk to immutable ownership/policy metadata. Enforce authorization before candidate retrieval where the store supports it, verify again before context assembly, and never rely on the generator to hide forbidden content.

## Prompt injection

Retrieved text is untrusted data even when it came from an internal repository. It may contain malicious instructions accidentally or deliberately. Delimit sources, minimize tool authority, validate outputs, and keep consequential actions behind deterministic authorization and approval.

## Production lifecycle

### Ingestion SLOs

Time to index, parse failure rate, backlog, freshness, deletion completion, and unsupported-format rate.

### Query SLOs

Authorized retrieval success, evidence recall, citation support, no-answer handling, latency percentiles, and cost per successful task.

### Versioning

Record corpus, parser, chunker, embedding, index, retriever, reranker, prompt, generator, evaluator, and policy versions for every evaluated/deployed configuration.

## Caching

Cache only with explicit keys that include relevant tenant, permissions, corpus/index version, query normalization, model/prompt version, and policy. Cache invalidation is a correctness and privacy problem, not only performance.

## Failure and degradation

- retrieval unavailable: return search/source links, queue, or fail visibly;
- generator unavailable: return ranked evidence when useful;
- stale index: disclose freshness or disable high-risk answers;
- evaluator unavailable: do not silently bypass required quality gates;
- conflicting evidence: present conflict or escalate;
- security anomaly: disable affected connectors/tools and preserve evidence.

## Incident example

If a user receives another tenant's policy excerpt:

1. contain retrieval and caches;
2. preserve request, filters, index and versions;
3. identify whether metadata, filter construction, cache key, or presentation failed;
4. assess affected sources and users;
5. repair and reindex/invalidate as needed;
6. add isolation tests and monitoring;
7. examine why end-to-end evaluation lacked adversarial tenant cases.

## Senior principle

The vector store is not a security boundary merely because it supports filters. Application identity, source ownership, query construction, caches, and presentation must agree on the same authorization model.
