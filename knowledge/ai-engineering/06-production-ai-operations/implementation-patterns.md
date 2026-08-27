---
id: ai-production-implementation-patterns
title: Admission and Load Shedding in Python and C++
level: L2-L4
status: maintained
last_reviewed: 2026-08-27
prerequisites: [ai-serving-capacity, ai-queues-backpressure]
---

# Admission and Load Shedding in Python and C++

## Purpose

The paired examples implement a small but foundational production boundary: admit work only when tenant quota, global capacity, request-size limits, and deadline allow it. Accepted work receives a lease; releasing the lease returns capacity.

- [Python example](../../../examples/production-ai-operations/python/admission_control.py)
- [C++ example](../../../examples/production-ai-operations/cpp/admission_control.cpp)

This is not a distributed rate limiter. It makes the policy mechanics visible before Redis, a gateway, or a serving platform hides them.

## Invariants

- In-flight capacity never exceeds the global limit.
- One tenant never exceeds its concurrency allocation.
- Expired requests do not consume inference.
- Oversized requests are rejected before expensive work.
- Every accepted request must release exactly one lease.
- Rejection includes a machine-readable reason.

## Why concurrency rather than requests per second?

Inference requests occupy scarce memory and scheduling capacity for highly variable durations. A request-per-second limit can admit many long generations simultaneously. Concurrency is still incomplete (token and memory estimates improve it) but it maps more directly to occupied work.

## Python versus C++

- Python uses a context manager so normal and exceptional exits release the lease.
- C++ uses RAII: the lease destructor releases capacity, and move semantics preserve single ownership.
- Both need a lock because admission and release mutate shared counters.
- A distributed version needs atomic state in a shared service and must handle worker death, usually through expiring leases and reconciliation.

## Failure extensions

1. Add weighted capacity based on estimated input plus maximum output tokens.
2. Add a monotonic lease expiry and a reaper for crashed workers.
3. Separate interactive and batch pools.
4. Add queue admission without allowing expired work to execute.
5. Export bounded metrics without tenant IDs as high-cardinality labels.
6. Test cancellation during streaming and verify release.

## MCP and agent transfer

Admission applies to tool calls and agent runs too. Bound concurrent tool effects, steps, tokens, and tenant spend before execution. A model cannot be trusted to self-limit because capacity protection must work even when model behavior regresses.

## Game transfer

Use separate pools for player-visible dialogue, background NPC planning, and offline content. Under overload, reject or defer background work first and preserve deterministic fallback for the live game loop.
