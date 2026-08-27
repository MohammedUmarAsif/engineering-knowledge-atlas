---
id: chunking-metadata-indexing
title: Chunking, Metadata, and Indexing
level: L2-L4
status: maintained
last_reviewed: 2026-08-27
prerequisites: [ocr-layout-tables]
---

# Chunking, Metadata, and Indexing

## Intuition

Retrieval cannot search an entire library as one object, so documents are divided into addressable evidence units. The unit must be small enough to find and large enough to understand.

## Why fixed windows exist

Fixed token or character windows are simple, fast, reproducible, and format-agnostic. They are defensible baselines. They fail when boundaries separate a heading from its paragraph, a rule from its exception, a table header from its row, or code from its explanation.

## Strategies

- fixed size with overlap;
- paragraph or sentence boundaries;
- heading/section hierarchy;
- layout element groups;
- table-aware segments;
- semantic boundary detection;
- parent-child retrieval;
- query-time dynamic expansion;
- page-image or region retrieval without early text chunking.

Chunking is an information-retrieval design decision, not housekeeping.

## Metadata

Each evidence unit should carry:

- stable chunk and document IDs;
- tenant/owner and access policy reference;
- document version and checksum;
- page and region;
- heading ancestry;
- element type and language;
- validity/effective dates;
- parser, chunker, and embedding versions;
- source URL or object key;
- neighbouring/parent identifiers.

Metadata enables authorization, filtering, citation, reprocessing, deletion, and evaluation.

## Indexes

One corpus may have several synchronized indexes:

- inverted lexical index;
- dense vector index;
- sparse learned-vector index;
- metadata/database index;
- graph or relationship index;
- page-image multi-vector index.

The source document registry (not a vector index) should own document lifecycle truth.

## Updates and deletion

Use explicit states such as received, parsed, indexed, active, superseded, failed, and deleted. Make ingestion idempotent. A new document version should not expose a half-updated mixture of old and new chunks.

Deletion must propagate to every derivative: parsed text, images, embeddings, lexical index, caches, evaluation samples, and provider files where applicable.

## Game analogy

A game engine does not scan every asset file whenever it needs a texture. Importers create canonical assets plus metadata and indexes. Version mismatches produce missing or stale resources. Document retrieval has the same lifecycle shape.

## Misconceptions

- More overlap does not automatically improve retrieval; it increases duplicates and context competition.
- Smaller chunks do not automatically improve precision; they may remove meaning.
- A vector database is not the source of truth for permissions or document lifecycle.

## Senior questions

- Which query classes require different segment granularity?
- How can a parser or embedding migration occur without downtime?
- How are duplicates and near-duplicates handled?
- Can every indexed object be traced, revoked, and reproduced?
