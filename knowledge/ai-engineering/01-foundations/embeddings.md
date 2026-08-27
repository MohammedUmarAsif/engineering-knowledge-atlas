---
id: embeddings
title: Embeddings
level: L1-L3
status: maintained
last_reviewed: 2026-08-27
---

# Embeddings

## Diagnostic

Skip to [Transformer and LLM Lifecycle](transformer-lifecycle.md) if you can explain what embeddings encode, why similarity depends on the model and corpus, how retrieval quality is evaluated, and when keyword search beats vectors.

## Mental model

An embedding maps an input into a numeric vector whose geometry is useful for a model-defined notion of relatedness. Nearby vectors are not automatically factually equivalent, causally related, safe to substitute, or relevant to a particular user question.

## Uses

- semantic retrieval;
- clustering and deduplication;
- recommendations;
- classification features;
- anomaly detection;
- matching across modalities when supported by the model.

## Retrieval mechanism

1. Split or otherwise identify retrievable units.
2. Produce embeddings with a chosen model.
3. Store vectors with identifiers and metadata.
4. Embed the query.
5. retrieve candidates by a similarity measure.
6. Filter or rerank candidates.
7. evaluate whether the returned evidence supports the task.

## Failure modes

- chunks destroy necessary context;
- the query and document use incompatible language;
- semantically similar content is not answer-relevant;
- exact identifiers are handled poorly;
- stale or unauthorized documents are retrieved;
- model changes invalidate comparisons;
- approximate indexes trade recall for speed;
- top-k retrieval hides the correct evidence.

## Senior judgment

Use lexical search for exact names, identifiers, and rare terms; embeddings for semantic variation; hybrid retrieval when both matter. Add reranking when first-stage recall is acceptable but ordering is weak. Measure retrieval separately from answer generation.

## Interview check

Design an experiment that distinguishes a retrieval failure from a generation failure.
