---
id: retrieval-implementation-patterns
title: Retrieval Mechanics in Python and C++
level: L1-L3
status: maintained
last_reviewed: 2026-08-27
prerequisites: [retrieval-models]
---

# Retrieval Mechanics in Python and C++

## Purpose

Frameworks make retrieval look like one function call. These paired standard-library examples expose the data structures and scoring underneath:

- tokenization;
- an inverted index;
- lexical overlap scoring;
- dense-vector cosine similarity;
- ranked result fusion;
- metadata filtering before ranking.

They are educational baselines, not production search engines.

## Runnable files

- [Python retrieval example](../../../examples/document-intelligence-retrieval/python/retrieval.py)
- [C++ retrieval example](../../../examples/document-intelligence-retrieval/cpp/retrieval.cpp)

## Follow one query

The query `refund timeout` takes two routes:

1. Lexical search looks up the exact terms in an inverted index and accumulates document scores.
2. Dense search compares a query vector with document vectors using cosine similarity.
3. Rank fusion rewards documents appearing near the top of either list.
4. Tenant filtering happens before candidates can be returned.

The vectors are deliberately supplied rather than generated. An embedding model would create them in a real system; the index and ranking concerns remain visible here.

## Python learning focus

- dictionaries and sets model postings and authorization filters;
- list comprehensions express candidate transformations;
- runtime checks protect vector dimensions and zero norms;
- sorting with key functions produces ranked results.

## C++ learning focus

- `std::unordered_map` implements expected constant-time term lookup;
- `std::vector` stores contiguous scores and embeddings with strong cache locality;
- references avoid unnecessary copies without transferring ownership;
- `std::span` provides a non-owning view over contiguous vectors;
- explicit types make document identity and tenant filtering visible.

## Important correction about data structures

A hash table is excellent for term-to-posting lookup, but it is not “your best friend for memory.” Hash tables usually spend extra memory on buckets and have weaker locality than contiguous arrays. Here:

- hash table: term → postings;
- vector/array: dense embedding and score list;
- sorted vector: final ranked output;
- database/filter index: production authorization and metadata.

The access pattern chooses the structure.

## What production adds

- BM25 term frequency, inverse document frequency, and length normalization;
- stemming, language analysis, spelling, synonyms, and exact fields;
- learned embedding models;
- ANN indexes such as HNSW or IVF;
- durable storage and incremental updates;
- distributed shards and replicas;
- policy-aware metadata filtering;
- reranking;
- evaluation and telemetry.

## Prediction questions

Before running the examples:

1. Which document wins lexical search?
2. Which wins dense search?
3. Why might fusion change the winner?
4. What happens if tenant filtering is applied after ranking?
5. What would a zero vector do to cosine similarity?
