---
id: agent-workflow-architecture
title: Workflow Architecture
level: L2-L5
status: maintained
last_reviewed: 2026-08-27
prerequisites: [agent-first-principles]
---

# Workflow Architecture

## Workflows encode known structure

In a workflow, code controls the major path and models solve bounded semantic steps. This is often the production default because state transitions, retry policy, and failure ownership remain visible.

## Core patterns

### Prompt chaining

Output from one step becomes validated input to the next:

```text
extract requirements → draft design → check constraints → render answer
```

Use it when the decomposition is stable and each boundary can reject bad output. Its weakness is upstream error propagation. A fluent final stage may conceal a faulty extraction.

### Routing

A classifier chooses a specialized path:

```text
request → billing | technical | safety | unknown
```

Routing improves focus and can choose different models or policies. It fails at ambiguous boundaries. Include confidence-independent escape routes such as `unknown`, human review, or a conservative default; model confidence is not calibrated merely because it is numeric.

### Parallelization

Independent workers run concurrently, then code aggregates:

- Sectioning: split independent subtasks.
- Voting: solve the same task multiple ways.
- Perspective sampling: request security, product, and performance analyses.

Parallelism reduces wall-clock latency only when tasks are truly independent and infrastructure supports concurrency. Voting does not remove correlated bias when all workers share the same model, prompt, and evidence.

### Orchestrator–worker

A model or program creates subtasks, workers execute them, and an orchestrator integrates results. This fits tasks whose decomposition varies—such as investigating an unfamiliar repository.

The hard problem is not delegation. It is specifying interfaces and proving coverage. Workers may duplicate effort, omit a global constraint, or produce mutually inconsistent assumptions.

### Evaluator–optimizer

One component drafts; another evaluates against a rubric; the producer revises:

```text
candidate → critique → revision → bounded stop
```

Use it when feedback is actionable and evaluation is meaningfully easier than generation. Avoid endless self-polishing. The evaluator may share the producer’s blind spot, and style scores can improve while factual quality declines.

## Workflows are graphs, not chains

Represent a production workflow as a directed graph:

- Node: a typed operation.
- Edge: an explicit transition condition.
- State: versioned data carried between nodes.
- Terminal state: completed, failed, cancelled, or awaiting input.

Cycles require a decreasing budget or progress measure. Without one, “retry” is an infinite loop wearing an AI label.

## Design the state before prompts

Example state:

```json
{
  "run_id": "r-104",
  "goal": "prepare migration plan",
  "phase": "risk_review",
  "artifacts": [{"id": "inventory-v2", "version": 2}],
  "attempts": {"risk_review": 1},
  "approvals": [],
  "budget": {"steps_left": 8, "cost_left_usd": 1.20}
}
```

Do not store the only truth inside a transcript. A transcript is an event record and model context candidate; it is not a normalized state model.

## Failure semantics

For each node, decide:

- Retryable: transient network failure, rate limit, unavailable dependency.
- Non-retryable: schema violation after bounded repair, authorization denial, invalid request.
- Ambiguous: timeout after sending a write; the server may have committed it.
- Compensatable: a completed effect can be counteracted by a defined operation.

Retries require idempotency. Attach a stable operation key to a logical write so repeating transport does not repeat the business effect.

## Saga intuition

A multi-step workflow rarely has a database transaction across every service. A saga records completed steps and invokes compensating actions when later work fails. Compensation is not time travel: a refund can reverse money, but cannot make a customer forget an email.

## Decision table

| Uncertainty | Path known? | Verification | Architecture |
|---|---:|---:|---|
| low | yes | deterministic | normal code |
| semantic step only | yes | strong | fixed workflow |
| branch selection | mostly | strong | routed workflow |
| decomposition varies | no | strong | orchestrator–worker |
| path and outcome uncertain | no | weak | do not automate yet |

## Senior design review

Ask:

1. Which decisions require a model?
2. Which decisions can be normal code?
3. What data crosses every node boundary?
4. Can the run resume after each node?
5. How is duplicate execution prevented?
6. What does the user see while work is pending?
7. Which metric would prove the extra stage helped?

## Game example

A quest planner can use deterministic gates for canon and player progression, a model to propose dialogue beats, parallel critics for tone and lore, and an approval gate before content becomes persistent. An unconstrained agent should not directly mutate quest completion flags merely because a generated story implies success.
