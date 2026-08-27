---
id: retrieval-evaluation-security-operations
title: Evaluation, Security, and Operations
level: L3-L5
status: maintained
last_reviewed: 2026-08-27
prerequisites: [reranking-context-assembly]
---

# Evaluation, Security, and Operations

## Diagnostic principle

An answer can be wrong because parsing failed, evidence was absent, retrieval missed it, reranking buried it, context omitted it, or generation ignored it. One end-to-end score cannot tell you which system to fix.

## Evaluation layers

### Parsing

- text/character accuracy by document class;
- reading order;
- layout element detection;
- table structure and cell relations;
- page/region provenance;
- high-risk field accuracy.

### Retrieval

- Recall@k: did relevant evidence enter the candidate set?
- Precision@k: how much retrieved evidence was relevant?
- MRR: how early was the first relevant result?
- nDCG: was graded relevance ordered well?
- latency, memory, freshness, and cost.

### Context

- evidence coverage;
- duplicate rate;
- conflict preservation;
- citation resolvability;
- token utilization.

### Answer

- correctness;
- groundedness/entailment;
- completeness;
- citation support;
- abstention and escalation;
- harmful or unauthorized disclosure.

## Build the evaluation set

Sample actual document and query classes, then add designed edge cases:

- exact identifiers;
- paraphrases;
- tables and figures;
- scanned/multilingual pages;
- temporal conflicts;
- revoked permissions;
- no-answer queries;
- adversarial instructions;
- long and duplicated documents.

Label evidence, not only final answers. Split results by document type, language, risk, and query pattern.

## Security

- enforce access before retrieval and again before presentation;
- bind chunks to tenant and source policy;
- prevent filter bypass through query rewriting;
- treat document text as untrusted prompt content;
- isolate parsers and OCR workloads;
- limit decompression, pages, pixels, time, and model spend;
- prevent source existence leakage through scores or errors;
- propagate deletion to all derivatives;
- protect embeddings: they can leak information and remain personal data.

## Operations

Track document lifecycle, queue lag, parse failures, index freshness, query latency, empty-result rate, retrieval drift, cost, access denials, and deletion completion. Version parser, OCR, chunker, embedder, index, reranker, and evaluation set.

## Change management

When replacing a component:

1. reprocess a representative shadow corpus;
2. compare each evaluation layer;
3. inspect regressions by slice;
4. measure storage, latency, and cost;
5. dual-read or canary where appropriate;
6. retain rollback until the new index is proven;
7. record the decision and evidence.

## Senior interview answer

When asked “How do you improve RAG accuracy?”, do not answer “use a better embedding model.” Start by locating the failing layer with labelled evidence and traces.
