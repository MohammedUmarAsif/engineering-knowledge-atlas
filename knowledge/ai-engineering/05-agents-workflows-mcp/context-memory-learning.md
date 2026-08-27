---
id: agent-context-memory-learning
title: Context, Memory, and Learning
level: L3-L5
status: maintained
last_reviewed: 2026-08-27
prerequisites: [agent-loop-state, rag-systems-evaluation]
---

# Context, Memory, and Learning

## Memory is not one database

“Give the agent memory” hides several distinct requirements:

- Working context: information needed for the current decision.
- Episodic memory: prior events and trajectories.
- Semantic memory: durable facts and concepts.
- Procedural memory: instructions, policies, or learned skills.
- Environment state: authoritative external truth.
- User profile: preferences with consent, provenance, and deletion rules.

A transcript is episodic evidence. It is not automatically authoritative truth.

## Write policy matters more than storage technology

For each candidate memory, decide:

1. Why will this help a future decision?
2. Is it fact, inference, preference, or instruction?
3. Who said it, and when?
4. What scope may retrieve it?
5. When does it expire or become invalid?
6. How can a user inspect, correct, or delete it?

Without provenance and lifecycle, memory turns temporary model guesses into durable misinformation.

## Context engineering

The goal is not maximum context. It is the smallest sufficient decision state.

Construct context from:

- Stable system and policy instructions.
- Current goal and explicit constraints.
- Relevant state fields.
- Selected observations and evidence.
- Available actions.
- Compact progress and unresolved questions.

Long raw histories increase cost and can bury constraints. Summaries save space but are lossy transformations; preserve links to source events and regenerate when policy or task changes.

## Retrieval for agents

Agent retrieval differs from question-answering retrieval. The needed item may be a past failed action, a tool precondition, a policy exception, or a partially completed artifact, not just text similar to the user’s latest sentence.

Retrieval keys can include goal, current state, entity IDs, time, failure type, tool, and causal relation. Evaluate whether retrieved memory changes decisions correctly, not merely whether it resembles a reference passage.

## Reflection is not learning by default

An agent may summarize a failure into a “lesson.” That changes future context but not model weights. Call it memory-assisted adaptation, not learning, unless an explicit update process changes a policy, program, or trained parameters.

Self-generated lessons can reinforce false causal stories. Validate them against traces, outcomes, counterexamples, and human review before promoting them to durable procedural memory.

## Skill libraries

A reusable skill is a versioned procedure with trigger conditions, inputs, outputs, permissions, and tests. It can reduce repeated reasoning and improve consistency. It can also fossilize outdated assumptions.

Manage skills like software:

- Owners and versions.
- Evaluation fixtures.
- Changelog and deprecation.
- Least-privilege dependencies.
- Clear conflict/precedence rules.
- Telemetry showing whether invocation helps.

## Forgetting is a feature

Good systems intentionally forget:

- Secrets and unnecessary personal data.
- Stale preferences.
- Superseded summaries.
- Low-confidence inferences.
- Data beyond retention policy.

Memory growth without deletion degrades retrieval, increases privacy risk, and makes behavior harder to explain.

## Game AI transfer

Separate what the world knows, what the player has revealed, what an NPC observed, and what an NPC merely believes. Memory can support believable character continuity, but perfect recall may make characters unnatural. Designed forgetting, rumor propagation, and biased belief can improve narrative, provided canonical simulation state remains separate.

## Research questions

- What memory item causally improved a trajectory rather than correlating with success?
- Can a system estimate the value of storing an episode before future tasks are known?
- How should contradictory memories be consolidated without erasing minority evidence?
- What is the optimal forgetting policy under privacy, compute, and task-performance constraints?
