---
id: rag-query-retrieval-orchestration
title: Query and Retrieval Orchestration
level: L2-L4
status: maintained
last_reviewed: 2026-08-27
prerequisites: [rag-first-principles]
---

# Query and Retrieval Orchestration

## The query is not always the information need

“Can I cancel it?” lacks object, jurisdiction, date, and user context. Retrieval orchestration resolves or requests missing information before searching.

## Query stages

1. authenticate user and tenant;
2. classify intent and risk;
3. resolve conversation references from trusted state;
4. identify required filters and authority;
5. decide whether retrieval is needed;
6. formulate one or more retrieval queries;
7. retrieve, merge, rerank, and assess evidence;
8. continue, clarify, search another source, or abstain.

## Query rewriting

Rewriting may normalize spelling, resolve acronyms, add domain vocabulary, translate, or convert conversational requests into standalone queries.

Risks:

- intent drift;
- invented entities or constraints;
- removal of exact identifiers;
- security-filter bypass;
- loss of negation;
- hidden dependence on conversation summaries.

Preserve the original query and evaluate rewritten queries as retrieval components.

## Multi-query retrieval

Generate several interpretations or facets, retrieve for each, then fuse. This improves recall for ambiguous or multi-part questions but increases cost, duplicate candidates, and the chance of invented intent.

## Decomposition

Complex questions may require subquestions, such as comparing two policies across dates. Decomposition helps only when answers can be recomposed without losing dependencies. Do not split tightly coupled reasoning into independent searches blindly.

## Routing

Choose sources by intent:

- SQL/API for structured facts;
- lexical search for identifiers;
- dense/hybrid retrieval for prose;
- graph traversal for explicit relationships;
- web search for approved current external evidence;
- no retrieval for conversational or transformative tasks.

Routing can be deterministic, model-assisted, or learned. High-risk source selection should remain bounded by policy.

## Iterative retrieval

The system may retrieve, inspect missing information, generate a refined query, and retrieve again. Bound the loop by step count, cost, time, source policy, and evidence progress. Repetition without new evidence is a termination signal.

## Senior question

Which decisions can be evaluated independently? If routing, rewriting, retrieval, and generation are one opaque agent loop, diagnosing regression becomes expensive.

## Interview scenario

A conversational assistant performs well on standalone questions but fails after pronouns, corrections, and topic changes. Design query resolution without treating the entire transcript as a trustworthy search query.
