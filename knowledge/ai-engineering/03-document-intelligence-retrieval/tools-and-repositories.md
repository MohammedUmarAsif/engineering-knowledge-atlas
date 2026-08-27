---
id: document-retrieval-tools-repositories
title: Document Intelligence and Retrieval Tools
level: L2-L4
status: maintained
last_reviewed: 2026-08-27
prerequisites: [retrieval-evaluation-security-operations]
---

# Tools and Repository Map

GitHub stars below are approximate discovery snapshots checked on 2026-08-27. They do not establish correctness, safety, or suitability.

## Document conversion and understanding

### [Docling](https://github.com/docling-project/docling)

- Role: structured conversion of PDF, office, web, image, and other formats for AI pipelines.
- Signals: approximately 58k stars reported by GitHub; MIT; active 2026 development; LF AI & Data project; Python with a C++ parsing component.
- Learn from it: canonical document representation, layout-aware parsing, modular format/OCR backends.
- Watch: model licenses and optional dependency footprint still require review.

### [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR)

- Role: multilingual OCR, document parsing, layout/table recognition, and vision-language document models.
- Signals: 70k+ stars; Apache-2.0; active 2026 releases; broad language and deployment support.
- Learn from it: OCR is now an ecosystem spanning recognition, structure, VLMs, browser/edge, and serving.
- Watch: benchmark claims require independent validation on your documents.

### [Unstructured](https://github.com/Unstructured-IO/unstructured)

- Role: ingestion and preprocessing across many document formats and connectors.
- Signals: approximately 15k stars; Apache-2.0 for the main library; active releases.
- Learn from it: connector-rich document ETL and partitioning abstractions.
- Watch: distinguish open-source library capabilities from hosted/enterprise platform features.

## Search and vector indexing

### [Faiss](https://github.com/facebookresearch/faiss)

- Role: exact and approximate dense-vector similarity search and clustering.
- Signals: approximately 40k stars; MIT; C++ core with Python wrappers; CPU/GPU implementations.
- Learn from it: vector indexes expose explicit speed, recall, memory, training, and update trade-offs.
- Best fit: embedded/library-level search or experimentation where you own surrounding persistence and authorization.

### [pgvector](https://github.com/pgvector/pgvector)

- Role: vector similarity inside PostgreSQL.
- Signals: approximately 22.6k stars; actively maintained; exact search plus HNSW and IVFFlat.
- Learn from it: vectors can coexist with transactions, joins, metadata, and conventional application data.
- Best fit: systems already centred on Postgres where scale and workload fit; do not add a separate vector database without need.

### [Qdrant](https://github.com/qdrant/qdrant)

- Role: dedicated vector search/database with filtering and hybrid-search features.
- Signals: approximately 33k stars; Apache-2.0; Rust; active clients and operations ecosystem.
- Learn from it: production vector search includes filtering, sharding, persistence, APIs, and operations, not only nearest-neighbour math.

## Evaluation and emerging retrieval

### [BEIR](https://github.com/beir-cellar/beir)

- Role: heterogeneous information-retrieval benchmark and evaluation framework.
- Signals: approximately 2.2k stars; Apache-2.0; research/community maintained.
- Learn from it: evaluate across varied domains and report effect sizes/slices rather than one flattering dataset.
- Watch: public benchmark results do not replace evaluation on your own corpus and permissions.

### [ColPali](https://github.com/illuin-tech/colpali)

- Role: late-interaction retrieval directly over document-page images using vision-language models.
- Signals: MIT; active research implementation associated with the ColPali paper.
- Learn from it: visually rich documents can be retrieved without forcing all meaning through OCR and plain text first.
- Watch: multi-vector storage/compute, model evolution, and domain-specific evaluation.

## Selection rule

Start with the smallest architecture that meets measured requirements:

- simple text extraction before VLM parsing;
- lexical search before a vector database when queries are exact;
- existing Postgres before another distributed service;
- exact vector search before ANN tuning;
- labelled evaluation before framework selection.

Frameworks that connect everything can accelerate prototypes, but the atlas teaches each boundary so convenience does not hide failure.
