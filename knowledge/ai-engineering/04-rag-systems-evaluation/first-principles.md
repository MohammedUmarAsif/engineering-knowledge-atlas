---
id: rag-first-principles
title: RAG from First Principles
level: L2-L4
status: maintained
last_reviewed: 2026-08-27
prerequisites: [document-intelligence-retrieval]
---

# RAG from First Principles

## Why RAG exists

Model weights are expensive to update, difficult to inspect, and not a reliable database. Many applications need changing private policies, product inventories, user documents, research papers, or evidence with citations.

The original RAG work combined a sequence generator with explicit retrieved memory, addressing knowledge access, provenance, and update limitations. Today's application-level RAG often uses independently built retrievers and general models rather than the paper's exact jointly trained architecture.

## Intuition

Think of the model as a capable analyst taking an open-book examination. Retrieval chooses which pages reach the desk. Context assembly arranges them. The model writes the response. Evaluation checks whether the pages were correct and whether the response used them faithfully.

A brilliant analyst with the wrong pages still fails.

## When RAG is appropriate

- private or rapidly changing knowledge;
- large evidence collections;
- citations and auditability;
- tenant-specific information;
- long-tail facts;
- configurable product knowledge.

## When not to use it

- deterministic calculation: use code;
- exact structured records: query the database/API;
- tiny stable context: provide it directly;
- simple document discovery: return search results;
- behavioural/style change: prompting or fine-tuning may fit better;
- no authoritative corpus: retrieval cannot create evidence;
- high-stakes decision without acceptable validation/human process.

## Failure decomposition

### Knowledge failure

The corpus lacks correct, current, authorized evidence.

### Ingestion failure

The evidence exists but parsing/chunking destroys or omits it.

### Retrieval failure

Relevant evidence is indexed but not returned.

### Ranking/context failure

Evidence is retrieved but buried, truncated, duplicated, or stripped of exceptions.

### Generation failure

Correct evidence is present but ignored, distorted, or supplemented with unsupported claims.

### Citation failure

The answer may be correct even though its citations do not support the claims. The citations may also be fabricated.

### Product failure

The user cannot inspect, contest, or act safely on the result.

## Baseline architecture

Begin with:

1. validated source corpus;
2. simple structure-aware chunks;
3. lexical or hybrid retrieval;
4. metadata authorization;
5. optional reranker;
6. concise evidence context;
7. answer with verified citations and abstention;
8. labelled evaluation by layer.

Earn additional complexity through measured failure.

## Game transfer

RAG can supply lore, quests, rules, historical player events, support knowledge, or design documentation. Runtime game state should usually remain structured authoritative data; retrieving prose is not a substitute for the simulation.

## Primary source

- [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401)
