---
id: retrieval-models
title: Lexical, Dense, Hybrid, and Late-Interaction Retrieval
level: L2-L5
status: maintained
last_reviewed: 2026-08-27
prerequisites: [chunking-metadata-indexing, embeddings]
---

# Lexical, Dense, Hybrid, and Late-Interaction Retrieval

## Begin with the question

What makes a document relevant: exact identifier, shared terminology, equivalent meaning, visual layout, temporal validity, authority, or a combination?

## Lexical retrieval

Inverted indexes map terms to documents. BM25-style ranking rewards term matches while accounting for frequency and document length.

Strong for:

- names, codes, error messages, citations, and rare terms;
- transparent matching;
- efficient mature infrastructure.

Weak when query and document use different vocabulary.

## Dense retrieval

An encoder maps query and document into vectors; similarity ranks candidates.

Strong for semantic paraphrases and conceptual similarity. Weak for exactness, domain shift, numerical distinctions, or concepts collapsed by the representation.

Cosine similarity is geometry produced by a model—not a calibrated probability of relevance or correctness.

## Sparse learned retrieval

Learned sparse representations retain vocabulary-addressable dimensions while expanding or weighting terms. They can combine semantic matching with inverted-index infrastructure, at additional model and operational complexity.

## Hybrid retrieval

Combine lexical and semantic candidates, often using normalized scores or rank fusion. Hybrid is valuable because the methods fail differently. It is not automatically superior: fusion weights, candidate depth, filters, and corpus determine the result.

## Reranking

A first-stage retriever emphasizes recall and speed. A slower reranker examines query-candidate pairs more deeply and improves ordering. This is often a better use of compute than applying an expensive model to the whole corpus.

## Late interaction

Single-vector retrieval compresses a document into one representation. Late-interaction methods retain multiple token or region vectors and compare them at query time, preserving finer-grained matching with more storage and computation.

ColBERT popularized token-level late interaction. ColPali extends the idea to page images using vision-language representations, allowing retrieval over visual document structure without requiring all meaning to survive OCR and text linearization.

## Exact versus approximate vector search

Exact search compares against every candidate and provides a quality baseline. Approximate nearest-neighbour indexes trade recall for lower latency and resource use.

Measure:

- recall relative to exact search;
- latency distribution;
- memory and build cost;
- update behavior;
- filtering interaction;
- index parameter sensitivity.

Do not evaluate an ANN index using only end-answer quality; generator behavior can hide missing evidence.

## Selection table

| Need | Strong starting point |
|---|---|
| Exact product/error code | Lexical |
| Semantic FAQ matching | Dense or hybrid |
| Mixed identifiers and natural language | Hybrid |
| Fine-grained passage matching | Late interaction/reranker |
| Visually rich pages | Layout-aware text plus multimodal/page retrieval |
| Small corpus and strict recall | Exact search baseline |
| Existing relational system and moderate scale | Postgres plus vector extension may be sufficient |

## Cross-domain transfer

- **Full stack:** search is a product with relevance, freshness, permissions, and latency requirements.
- **Games:** entity lookup, spatial indexes, asset registries, and matchmaking demonstrate the same lesson: choose a data structure based on access pattern, not fashionable complexity.
- **Game AI research:** retrieval can support long-term agent memory, case-based reasoning, lore consistency, adaptive dialogue, or similarity search over trajectories—but relevance evaluation is domain-specific.

## Interview scenario

Users say semantic search misses invoice numbers while keyword search misses paraphrased policy questions. Design a hybrid pipeline and evaluation that exposes each failure class.
