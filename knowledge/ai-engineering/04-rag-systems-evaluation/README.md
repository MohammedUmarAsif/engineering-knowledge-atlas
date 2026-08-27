---
id: rag-systems-evaluation
title: RAG Systems and Evaluation
level: L2-L5
status: maintained
last_reviewed: 2026-08-27
prerequisites: [document-intelligence-retrieval, model-application-engineering]
---

# RAG Systems and Evaluation

## First principle

Retrieval-augmented generation combines a generator's parametric capability with external, inspectable evidence. It is useful when the task depends on knowledge that must be current, private, attributable, replaceable, or too large to place permanently in model weights.

RAG does not make a model truthful. It creates an evidence path that can be engineered and evaluated.

## Diagnostic: skip only if you can answer all of these aloud

1. What is parametric versus non-parametric memory in the original RAG formulation?
2. When should a product use search without generation, long context, tools, fine-tuning, or a database query instead of RAG?
3. Separate ingestion, retrieval, context, generation, and citation failures.
4. How would you decide whether retrieval is necessary for a request?
5. What can query rewriting improve, and how can it destroy intent?
6. Why can increasing retrieval recall reduce answer quality?
7. Compare single-pass, multi-query, iterative, corrective, hierarchical, and graph-based RAG.
8. What assumption does a retrieval evaluator make in corrective RAG?
9. Why does GraphRAG require evaluating graph construction separately from answer quality?
10. Distinguish groundedness, correctness, relevance, completeness, and citation support.
11. How do you create a representative evaluation set without leaking the test answers into development?
12. What are the privacy and prompt-injection boundaries in a RAG pipeline?
13. How should a system answer when the corpus contains conflicting or insufficient evidence?
14. What evidence would convince you that a complex RAG architecture beats a simple hybrid baseline?

If any answer is vague, begin with [RAG from First Principles](first-principles.md). If all are precise, continue to [Agents, Workflows, and MCP](../05-agents-workflows-mcp/README.md).

## System equation

For query `q`, retriever `R` selects evidence `z` from corpus `D`; generator `G` produces answer `y` conditioned on the query and evidence:

```text
z = R(q, D)
y = G(q, z)
```

Production RAG adds authorization, query policy, reranking, context construction, citation binding, state, evaluation, and operations around that compact idea.

## Reading order

1. [RAG from First Principles](first-principles.md)
2. [Query and Retrieval Orchestration](query-retrieval-orchestration.md)
3. [Advanced RAG Patterns](advanced-patterns.md)
4. [Generation, Evidence, and Citations](generation-evidence-citations.md)
5. [Evaluation Science](evaluation-science.md)
6. [Security and Production Operations](security-production.md)
7. [Tools and Repository Map](tools-and-repositories.md)
8. [Research Frontier and PhD Questions](research-frontier.md)
9. [Python and C++ Implementation Mechanics](implementation-patterns.md)
10. [Mastery and Interview Review](mastery.md)
