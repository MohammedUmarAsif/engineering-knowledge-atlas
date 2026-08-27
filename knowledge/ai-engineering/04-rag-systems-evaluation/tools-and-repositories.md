---
id: rag-tools-repositories
title: RAG Tools and Repository Map
level: L2-L4
status: maintained
last_reviewed: 2026-08-27
prerequisites: [rag-security-production]
---

# Tools and Repository Map

Stars are approximate snapshots checked on 2026-08-27 and are not quality guarantees.

## [LlamaIndex](https://github.com/run-llama/llama_index)

- Approximately 51k stars; MIT; broad connectors, indexes, retrievers, workflows, and integrations.
- Learn from its modular data/retrieval abstractions and integration ecosystem.
- Its security policy makes clear that web validation, authorization, prompt injection, unbounded inputs, and many integration risks remain responsibilities of the hosting application.
- Use after understanding the underlying pipeline so default behaviour remains visible.

## [Microsoft GraphRAG](https://github.com/microsoft/graphrag)

- Approximately 35.5k stars; MIT; modular graph-based RAG research project.
- Learn graph extraction, community summaries, local/global query modes, and indexing migration concerns.
- The project explicitly identifies itself as research and warns of configuration evolution. Evaluate graph quality and cost before adoption.

## [RAGFlow](https://github.com/infiniflow/ragflow)

- Large, actively developed end-to-end RAG/document platform with deep parsing, retrieval, workflows, and citations.
- Learn how production systems connect document processing, search, model orchestration, UI, and operations.
- Its breadth means significant dependencies and attack surface; review releases and security advisories rather than equating feature count with safety.

## [Ragas](https://github.com/explodinggradients/ragas)

- Evaluation framework for RAG/agent applications.
- Learn dataset-driven experiments and component metrics.
- Treat metric names as operational definitions, not universal scientific truths; validate model-based evaluators against domain experts.

## Supporting components

Reuse the annotated retrieval tools from [Document Intelligence and Retrieval](../03-document-intelligence-retrieval/tools-and-repositories.md): Docling, PaddleOCR, Unstructured, Faiss, pgvector, Qdrant, BEIR, and ColPali.

## Framework selection checklist

- Does it expose each stage for evaluation?
- Can authorization be enforced before retrieval?
- Are data retention and telemetry controllable?
- Can components be versioned and replaced?
- Are retries, caches, and background jobs observable?
- Does it support your document/query languages and scale?
- Is the dependency and security burden justified?
- Can the team operate it during an incident?

Build the smallest measurable pipeline before adopting the largest framework.
