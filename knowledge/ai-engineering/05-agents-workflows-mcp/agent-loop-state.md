---
id: agent-loop-state
title: Agent Loops, State, and Durable Execution
level: L3-L5
status: maintained
last_reviewed: 2026-08-27
prerequisites: [agent-workflow-architecture]
---

# Agent Loops, State, and Durable Execution

## The minimum honest agent

An agent runtime needs only:

1. State and a goal.
2. A set of permitted action descriptions.
3. A model that proposes the next action or completion.
4. A validator and policy layer.
5. An executor.
6. An observation recorder.
7. A bounded loop.

Frameworks add persistence, graph orchestration, tracing, integrations, deployment, and ergonomics. Learn the loop first so abstractions remain inspectable.

## Separate proposed action from executed action

```text
model proposal ≠ authorization ≠ execution ≠ confirmed effect
```

A proposal may be malformed. A valid proposal may be unauthorized. An authorized call may time out. A timeout may conceal a completed write. These are four different states and must not collapse into “tool failed.”

## ReAct and its durable lesson

[ReAct](https://arxiv.org/abs/2210.03629) interleaves reasoning and environment actions. Its lasting architectural insight is feedback: the system can revise behavior after external observations. Production systems need not expose private reasoning traces. Store compact decisions, tool inputs, results, and state transitions that operators can inspect without depending on unrestricted hidden thought.

## State categories

- Control state: current node, attempts, deadlines, stop reason.
- Domain state: order, document, player, repository, or research objects.
- Working state: current plan, intermediate artifacts, unresolved questions.
- Security context: principal, scopes, tenant, approvals, policy version.
- Accounting state: tokens, cost, tool calls, elapsed time.
- Event history: append-only record of what happened.

Version state schemas. A run resumed after deployment may encounter newer code; define migration or pin the runtime version.

## Budgets are independent

- Step budget prevents loops.
- Token budget caps inference expansion.
- Cost budget catches expensive models and tools.
- Time budget establishes a deadline.
- Authority budget limits effect size: number of files, refund amount, recipients, environments.
- Context budget controls what the model sees.

A run can remain under ten steps yet exceed financial or authority limits. “Maximum iterations” is not a complete safety policy.

## Stopping is a classification problem plus policy

Possible stop conditions:

- Goal verified.
- Agent claims completion but verifier rejects it.
- More user input is required.
- Approval is required.
- Budget exhausted.
- Repeated state/no-progress detected.
- Irrecoverable failure.
- User cancellation.

Never accept textual confidence as proof of completion. Verify external postconditions: tests pass, record exists, cited facts resolve, game state respects invariants.

## Durable execution

Persist at safe boundaries:

```text
load checkpoint → decide → record intent → execute → record result → checkpoint
```

The dangerous interval lies between external execution and recording success. Use idempotency keys, transactional outboxes, read-after-write reconciliation, or tool-specific status queries to resolve ambiguous completion.

Exactly-once delivery is generally an application illusion constructed from durable state and deduplication. Networks naturally give you loss, delay, and duplication.

## Concurrency

Parallel workers can read the same old state and issue conflicting writes. Defenses include:

- Optimistic version checks.
- Resource locks with leases.
- Single-writer ownership.
- Commutative operations.
- Merge functions with explicit conflict policy.

Do not let a language model improvise concurrency control.

## Plan handling

A plan is a hypothesis, not a contract. Replanning is justified when observation invalidates an assumption. Constant replanning wastes tokens and destabilizes execution; never replanning makes the system brittle.

Track why a plan changed. If the reason is absent, evaluation cannot distinguish adaptation from wandering.

## Failure signatures

- Looping: repeated action/state pair.
- Thrashing: alternation between incompatible approaches.
- Premature completion: success claimed without postcondition.
- Context drift: original constraint disappears from working context.
- Tool fixation: familiar tool chosen despite poor fit.
- Error laundering: tool error summarized as successful progress.
- Zombie run: user cancelled, but background worker continues.

Each signature should have a detector, not just a prompt warning.

## Game-system transfer

Game loops already separate simulation state, inputs, decisions, and effects. Apply the same discipline to AI characters. An NPC model proposes an intent; deterministic gameplay code validates range, cooldown, inventory, animation state, and world rules before applying an action. Replay logs should capture seeds, model/version, observations, and accepted actions.
