---
id: agent-mastery
title: Agents, Workflows, and MCP Mastery Defense
level: L3-L5
status: maintained
last_reviewed: 2026-08-27
prerequisites: [agent-security-production, agent-research-frontier, agent-implementation-patterns]
---

# Agents, Workflows, and MCP Mastery Defense

## Rule

Answer aloud without notes. A strong answer states assumptions, contrasts alternatives, traces a failure through boundaries, and proposes evidence. Vocabulary without mechanism does not pass.

## First-principles defense

1. Define agency using control flow, not anthropomorphic language.
2. Derive an agent loop from state, observation, action, transition, and stop condition.
3. Explain why long-horizon reliability cannot be inferred from per-step accuracy.
4. Give a case where an agent is inferior to a fixed workflow.
5. Relate agent behavior to observability, controllability, feedback delay, and stability.

## Architecture defense

6. Choose among chaining, routing, parallelization, orchestrator-worker, and evaluator-optimizer for a document migration project.
7. Design state that can survive process failure and software deployment.
8. Handle a timeout after sending a non-idempotent write.
9. Explain why “exactly once” usually depends on deduplication and reconciliation.
10. Design independent step, time, cost, context, and authority budgets.
11. Detect looping, thrashing, premature completion, and zombie runs.

## MCP defense

12. Draw host, client, and server boundaries for an editor connected to three MCP servers.
13. Distinguish tools, resources, prompts, multi-round-trip input, and opt-in extensions such as Tasks; explain current deprecations.
14. Compare `stdio` and Streamable HTTP risks.
15. Explain stateless per-request capabilities, `server/discover`, protocol-version selection, and legacy handshake compatibility.
16. Why are tool annotations hints instead of authorization?
17. Explain token audience binding and why token passthrough is dangerous.
18. When is a normal internal function better than an MCP server?

## Evaluation and security defense

19. Build an evaluation suite for a repository-maintenance agent.
20. Separate outcome, trajectory, safety, efficiency, and recovery metrics.
21. Diagnose why a benchmark improvement may result only from extra test-time compute.
22. Trace an indirect prompt-injection attack from webpage to email tool.
23. Design a meaningful approval screen and explain approval fatigue.
24. Specify sandbox boundaries for generated code.
25. Design shadow-mode and gradual-autonomy rollout criteria.

## Multi-agent and research defense

26. Provide evidence that two agents outperform one under equal resources.
27. Explain correlated error, communication loss, and credit assignment.
28. Design an ablation for a supervisor-worker architecture.
29. Critique a paper showing five successful social-simulation anecdotes.
30. Propose a falsifiable Game AI hypothesis involving NPC memory or hierarchical planning.

## Production scenario

Design an agent that reviews customer incident reports, gathers logs, proposes remediation, and may execute a rollback.

Your answer must include:

- Deterministic versus model-controlled decisions.
- State schema and durable checkpoints.
- Read and write tool contracts.
- Tenant and environment isolation.
- Prompt-injection defenses.
- Approval and rollback policy.
- Duplicate and ambiguous execution handling.
- Evaluation dataset and metrics.
- Trace fields, redaction, kill switch, and incident response.
- A simpler baseline and evidence required to exceed it.

## Game AI scenario

Design a companion NPC that remembers shared events, plans assistance, and speaks in character without cheating.

Defend:

- Canonical world state versus character belief.
- Observation permissions and intentional forgetting.
- Real-time fallback and latency budget.
- Deterministic action validation.
- Narrative constraints and player control.
- Enjoyment, believability, safety, and gameplay metrics.
- Reproducibility and research ablations.

## Pass criterion

You pass when you can explain not merely how to build an agent, but why each autonomous decision exists, what constrains it, how its effect is verified, how it fails, and what evidence justifies the complexity.
