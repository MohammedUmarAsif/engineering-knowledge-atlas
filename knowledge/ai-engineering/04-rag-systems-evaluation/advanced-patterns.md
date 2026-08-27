---
id: advanced-rag-patterns
title: Advanced RAG Patterns
level: L3-L5
status: maintained
last_reviewed: 2026-08-27
prerequisites: [rag-query-retrieval-orchestration]
---

# Advanced RAG Patterns

Advanced patterns solve particular baseline failures. They are hypotheses to test, not maturity badges.

## Adaptive retrieval

Retrieve only when the task needs external evidence. This avoids unnecessary latency/noise but adds a routing decision that can incorrectly skip retrieval.

## Corrective RAG

CRAG evaluates retrieved evidence and chooses corrective actions, such as refining documents or expanding search. It targets the case where initial retrieval is unreliable.

Hidden assumption: the retrieval evaluator must recognize good and bad evidence accurately. A weak evaluator merely moves the failure.

Primary source: [Corrective Retrieval Augmented Generation](https://arxiv.org/abs/2401.15884).

## Self-RAG

Self-RAG trains a model to retrieve adaptively and generate reflection tokens that critique relevance, support, and generation quality.

Important precision: Self-RAG is not simply prompting any model to “reflect.” The paper's method trains a model with specific control/reflection behaviour.

Primary source: [Self-RAG](https://arxiv.org/abs/2310.11511).

## Hierarchical retrieval and RAPTOR

RAPTOR clusters and recursively summarizes document chunks into a tree, allowing retrieval across levels of abstraction. It targets questions requiring holistic information beyond a local passage.

Costs and risks include indexing expense, summary information loss, summary hallucination, update complexity, and difficult provenance across abstraction layers.

Primary source: [RAPTOR](https://arxiv.org/abs/2401.18059).

## GraphRAG

Graph-based RAG extracts entities and relations, constructs graph structures, and retrieves communities, paths, or summaries. It can help global or relationship-heavy questions that flat chunks answer poorly.

Evaluate separately:

- entity/relation extraction;
- entity resolution;
- graph completeness and contradiction;
- community detection/summarization;
- incremental updates;
- query routing;
- final answer support.

Microsoft explicitly labels its GraphRAG implementation a research project. A graph is not automatically more accurate than text retrieval.

## Long-context RAG

Retrieve larger parent sections or many candidates into a long context. This reduces boundary loss but increases cost, latency, noise, conflict, and attention-position sensitivity.

## Agentic RAG

An agent chooses sources, issues queries, reads results, and iterates. Useful when information needs are genuinely dynamic and multi-source. Dangerous when a bounded pipeline would be sufficient: more decisions create more evaluation and failure surfaces.

## Decision table

| Observed failure | Candidate response |
|---|---|
| Many queries need no external facts | Adaptive routing |
| Initial evidence often irrelevant | Reranking or corrective retrieval |
| Questions span an entire long document | Hierarchical/parent retrieval |
| Questions depend on relationships/global themes | Graph-based retrieval |
| Ambiguous multi-facet questions | Multi-query or decomposition |
| Corpus is tiny and context fits | Direct long context may be simpler |

## PhD habit

For each method, state baseline, intervention, assumed mechanism, measurable prediction, confounders, and falsification condition before implementation.
