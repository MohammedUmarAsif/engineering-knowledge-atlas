---
id: multi-agent-systems
title: Multi-Agent Systems
level: L3-L5
status: maintained
last_reviewed: 2026-08-27
prerequisites: [agent-loop-state]
---

# Multi-Agent Systems

## Begin with the null hypothesis

Assume one agent or workflow is sufficient until evidence rejects that assumption. Multiple agents add communication, duplicated context, coordination failures, larger cost, and harder attribution.

The question is not “which roles can we invent?” It is “which separable capabilities or information boundaries require independent decision-makers?”

## When decomposition can help

- Parallel independent research with measurable coverage.
- Specialists needing different tools, context, policies, or models.
- An adversarial reviewer whose rubric differs from the producer’s objective.
- Distributed environments where no participant has all observations.
- Simulation of strategic or social interaction as the research object.

Role names alone do not create diversity. Five agents using the same model, evidence, and prompt style can produce five correlated variants of one mistake.

## Architectures

### Supervisor and workers

A supervisor decomposes, delegates, and integrates. It centralizes global constraints but may become a bottleneck or single point of semantic failure.

### Pipeline of specialists

Typed handoffs move work through specialist stages. It is inspectable but propagates early errors and can resemble an overcomplicated workflow.

### Peer collaboration

Agents exchange proposals or critiques. This supports negotiation but risks chatter, convergence on persuasive errors, and unclear completion authority.

### Blackboard

Participants write structured findings to shared state. This reduces repeated message copying and gives an auditable artifact, but needs ownership, conflict resolution, and schema discipline.

### Market or auction

Agents bid for tasks or resources. Useful for allocation research; often unnecessary for ordinary applications where code can schedule work more predictably.

## Communication is lossy computation

Each handoff should specify:

- What claim or artifact is transferred?
- What evidence supports it?
- Which assumptions remain unresolved?
- What can the recipient modify?
- What acceptance test applies?

Natural-language conversation without structured artifacts makes coordination appear intelligent while hiding missing work.

## Credit assignment

If a team succeeds, which agent or interaction caused success? If it fails, which decision should change? End-to-end score alone cannot answer.

Use ablations:

- Remove one role.
- Replace its output with a deterministic baseline.
- Hold token budget constant.
- Swap model assignments.
- Block communication edges.
- Measure outcome and cost changes.

Without matched budgets, a multi-agent system may win simply because it spent more inference.

## Failure modes

- Cascade: one false premise spreads.
- Groupthink: agents reinforce shared bias.
- Deadlock: each waits for another.
- Livelock: messages continue without state progress.
- Delegation loop: task bounces between agents.
- Responsibility diffusion: no component verifies the final artifact.
- Context explosion: coordination consumes more tokens than solving.
- Authority escalation: one agent routes a dangerous request through a more privileged peer.

## Game and PhD relevance

Game AI is a natural multi-agent laboratory: cooperation, competition, partial observability, communication, emergent conventions, and human-agent interaction are core phenomena. Yet an entertainment game also needs frame budgets and authored experiences. Use fast deterministic or learned policies in the real-time loop; reserve language-agent deliberation for slower planning, dialogue, simulation, or offline content workflows.

Potential research contrasts:

- Centralized training versus decentralized execution.
- Explicit communication versus inferred coordination.
- Believable bounded rationality versus optimal play.
- Human enjoyment versus win rate.
- Emergence under shared versus heterogeneous models.

## Adoption gate

Approve multiple agents only when a single-agent baseline, equal-compute comparison, per-role ablation, coordination metric, and failure-containment design exist.
