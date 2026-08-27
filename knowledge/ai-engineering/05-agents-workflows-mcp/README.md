---
id: agents-workflows-mcp
title: Agents, Workflows, and MCP
level: L2-L5
status: maintained
last_reviewed: 2026-08-27
prerequisites: [model-application-engineering, rag-systems-evaluation]
---

# Agents, Workflows, and MCP

## First principle

An agent is not an intelligent object. It is a software control loop in which a model chooses some future actions from bounded options, observes their results, updates state, and eventually stops or asks for help.

The model supplies probabilistic judgment. Code must still supply authority, invariants, budgets, persistence, validation, and accountability.

## Diagnostic — skip only if you can defend every answer

1. Where exactly does control move from deterministic code to a model in an agent loop?
2. When is one model call better than a workflow, and when is a workflow better than an agent?
3. Compare prompt chaining, routing, parallelization, orchestrator-worker, and evaluator-optimizer patterns.
4. Why are tool schemas part of the reasoning environment rather than mere API documentation?
5. Separate a plan, a task graph, runtime state, memory, and an execution trace.
6. What makes a tool call retry-safe? Explain idempotency keys and ambiguous completion.
7. How do step, token, time, money, and authority budgets constrain an agent differently?
8. What must survive a process crash for durable execution to resume correctly?
9. Distinguish MCP hosts, clients, and servers; then distinguish tools, resources, and prompts.
10. Why is MCP an interoperability protocol, not an agent framework or security boundary?
11. When do multiple agents improve a system, and when do they merely multiply correlated errors?
12. How would you evaluate task outcome, trajectory quality, safety, cost, and recovery independently?
13. How can an untrusted webpage or retrieved document cause an agent to misuse an authorized tool?
14. What evidence would justify autonomous writes instead of human-approved writes?
15. How would an NPC agent differ from a business-process agent in latency, determinism, world knowledge, and player experience?

If any answer is vague, begin with [Agency from First Principles](first-principles.md). If every answer is precise, attempt the [Mastery Defense](mastery.md) without notes.

## The control loop

```text
goal + state + observations + allowed actions
                    │
                    ▼
              model decision
                    │
          validate / authorize / execute
                    │
                    ▼
            result + updated state
                    │
          stop, pause, fail, or repeat
```

Every arrow is an engineering boundary. If the system cannot explain who owns that boundary, it is not production-ready.

## Reading order

1. [Agency from First Principles](first-principles.md)
2. [Workflow Architecture](workflow-architecture.md)
3. [Agent Loops, State, and Durable Execution](agent-loop-state.md)
4. [Tools, Contracts, and Model Context Protocol](tools-and-mcp.md)
5. [Context, Memory, and Learning](context-memory-learning.md)
6. [Multi-Agent Systems](multi-agent-systems.md)
7. [Evaluation and Observability](evaluation-observability.md)
8. [Security and Production Operations](security-production.md)
9. [Tools and Repository Map](tools-and-repositories.md)
10. [Research Frontier and Game AI Questions](research-frontier.md)
11. [Python and C++ Implementation Mechanics](implementation-patterns.md)
12. [Mastery and Interview Defense](mastery.md)

## Outcome

After this module, “use an agent” should never be your first architectural answer. You should be able to derive the smallest sufficient control system, state its assumptions, instrument its failures, and justify each degree of autonomy.
