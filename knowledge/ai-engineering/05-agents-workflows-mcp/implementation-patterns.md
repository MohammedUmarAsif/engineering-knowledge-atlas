---
id: agent-implementation-patterns
title: Bounded Agent Loops in Python and C++
level: L2-L4
status: maintained
last_reviewed: 2026-08-27
prerequisites: [agent-loop-state, agent-tools-mcp]
---

# Bounded Agent Loops in Python and C++

## Purpose

The paired examples implement the runtime underneath frameworks: typed action proposals, an allowlisted tool registry, argument validation, read/write classification, approval, idempotency, step budgets, state transitions, and explicit stop reasons.

- [Python example](../../../examples/agents-workflows-mcp/python/bounded_agent.py)
- [C++ example](../../../examples/agents-workflows-mcp/cpp/bounded_agent.cpp)

Neither example calls a model. A deterministic policy emits proposals so orchestration can be tested without network keys or stochastic inference. Replace that policy with a model adapter only after the runtime invariants pass.

## Execution phases

```text
proposal
  → schema validation
  → tool lookup
  → policy/approval
  → idempotency check
  → execution
  → observation
  → checkpoint-ready state
```

## Why Python and C++ differ

Python is concise for model adapters, schema libraries, evaluation, and service orchestration. C++ makes ownership, variants, and runtime integration explicit, which is useful for engines and native systems.

The examples preserve the same conceptual contracts rather than forcing identical syntax.

## What is deliberately missing

- Persistent database checkpoints.
- Cryptographic identity and authorization.
- Distributed locks.
- A real sandbox.
- MCP transport and capability negotiation.
- Semantic completion verifier.
- Production telemetry and secret redaction.

Missing features are named because a tutorial loop must not be mistaken for a safe autonomous runtime.

## MCP adaptation

The internal `ToolSpec` resembles a discovered tool but is not an MCP implementation. An adapter would:

1. Select the modern or legacy compatibility path and optionally call `server/discover`.
2. Attach the selected protocol version, client capabilities, and identity to every modern request.
3. Convert discovered tool schemas into internal capabilities.
4. Apply host policy independent of server annotations.
5. Send validated calls over `stdio` or Streamable HTTP.
6. Parse `complete` versus `input_required`, structured content, and tool-level errors.
7. Bound result size and preserve provenance.

Keep application policy outside the adapter so changing protocols cannot bypass authority checks.

## Exercises to think through: not necessarily run here

1. Crash after the write tool commits but before state records success. How does the idempotency key help, and what remains unresolved?
2. Add a deadline budget independent of step count.
3. Make approval bind to an exact tool name, argument hash, principal, and expiry.
4. Record an append-only event before and after every effect.
5. Add a `WAITING_FOR_INPUT` state without keeping a process alive.
6. Make two workers race on the same game entity version and reject the stale write.

## Interview translation

If asked to design an AI agent, begin with goal, action space, state, verifier, and authority. Then derive the loop, persistence, retries, and observability. Mention a framework only after the system contract is clear.
