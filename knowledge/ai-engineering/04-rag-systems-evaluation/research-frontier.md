---
id: rag-research-frontier
title: RAG Research Frontier and PhD Questions
level: L5
status: maintained
last_reviewed: 2026-08-27
prerequisites: [rag-tools-repositories]
---

# Research Frontier and PhD Questions

## Established foundation

Retrieval can provide external memory, improve access to changing/long-tail knowledge, and enable provenance. These benefits depend on corpus and retrieval quality; RAG is not a general proof against hallucination.

## Active directions

### Adaptive and self-correcting systems

Systems decide whether to retrieve, judge evidence, refine queries, or critique answers. The research challenge is evaluator calibration: an unreliable controller can amplify cost and error while appearing sophisticated.

### Hierarchical and graph retrieval

These address multi-scale and relationship-heavy questions. Open problems include lossy summaries, graph construction error, temporal updates, contradiction, provenance, and fair comparison with strong hybrid/long-context baselines.

### Multimodal RAG

Retrieval and generation across text, page images, diagrams, audio, video, and structured state. Research needs claim-level provenance across modalities and evaluation that respects spatial/temporal evidence.

### Retrieval for agents

Agents retrieve not only facts but instructions, tools, prior trajectories, and memories. Relevance must include action utility, safety, recency, and user intent—not semantic similarity alone.

### Continual and temporal RAG

Corpora change. Open questions include valid-time retrieval, retractions, conflicting versions, embedding migrations, cached derived knowledge, and evaluation under evolving truth.

## Game AI PhD directions

### Agent memory

How should a game agent retrieve past experiences to improve strategy while remaining believable and computationally bounded?

Possible experiment: compare episodic retrieval strategies on task reward, behavioural diversity, player perception, latency, and memory growth.

### Narrative consistency

Can provenance-aware retrieval preserve global canon while allowing local improvisation and player agency?

Key tension: rigid retrieval may reduce creativity; loose retrieval may violate character knowledge or world state.

### Player-adaptive teaching

Retrieve similar player mistakes, tutorial interventions, or demonstrations. Evaluate learning, frustration, retention, and fairness—not only immediate success.

### Multimodal game-state retrieval

Retrieve strategically similar states from screenshots, symbolic state, trajectories, or maps. Study what representation transfers across levels, art styles, rules, and player skill.

### Multi-agent shared memory

How should agents share, withhold, forget, or contest retrieved memories? This connects information retrieval with theory of mind, communication, imperfect information, and social believability.

## Research design template

1. Define the missing knowledge and why it matters.
2. State a falsifiable hypothesis.
3. Choose a strong simple baseline.
4. Isolate the intervention.
5. Define task, human, system, and cost outcomes.
6. Test distribution shift and failure slices.
7. publish negative results and artifacts where permitted.

## Core papers

- [Original RAG](https://arxiv.org/abs/2005.11401)
- [Self-RAG](https://arxiv.org/abs/2310.11511)
- [Corrective RAG](https://arxiv.org/abs/2401.15884)
- [RAPTOR](https://arxiv.org/abs/2401.18059)
