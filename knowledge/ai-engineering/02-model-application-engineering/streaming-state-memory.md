---
id: streaming-state-and-memory
title: Streaming, State, and Memory
level: L2-L4
status: maintained
last_reviewed: 2026-08-27
prerequisites: [tool-calling-and-side-effects]
---

# Streaming, State, and Memory

## Diagnostic

Skip to [Multimodal Applications](multimodal.md) if you can distinguish transcript, workflow state, provider state, cache, retrieval memory, and user profile—and define retention for each.

## Streaming

Streaming exposes incremental events before the complete response is known. It improves perceived latency and enables progress updates, but creates new state transitions.

Handle:

- event ordering and correlation;
- partial text or structure;
- cancellation and client disconnect;
- late safety or validation failure;
- tool-call events interleaved with text;
- duplicate/replayed events;
- usage arriving after content;
- resumption or restart behavior.

Never assume every provider stream is a sequence of text fragments. Normalize provider events into application events.

## State taxonomy

### User-visible transcript

What participants saw. It supports continuity and audit but may require editing, deletion, or legal retention controls.

### Effective model context

What was actually sent for a particular inference. It may differ from the visible transcript due to policy, summaries, retrieval, truncation, and tools.

### Workflow state

Steps, approvals, tool results, pending actions, errors, and checkpoints. Store this explicitly; do not reconstruct it from prose.

### User memory/profile

Durable preferences or facts. Require provenance, user control, correction, expiry, and clear scope.

### Provider-managed state

Remote conversation or response objects. Convenient, but subject to provider retention, regional, deletion, and migration constraints.

### Cache

Reusable computation or prompt prefixes. Caching affects privacy, staleness, observability, cost, and compatibility.

## Memory design

Ask before storing:

- Is it necessary?
- Did the user request or expect it?
- Is it fact, inference, preference, or temporary state?
- What is its source and confidence?
- Who may read it?
- When does it expire?
- How can the user inspect, correct, or delete it?

More memory is not automatically a better assistant.

## Summarization

Summaries reduce context cost but are lossy derived state. Preserve critical structured facts separately, record source ranges when possible, and regenerate summaries after corrections. Do not allow an old summary to override a newer authoritative event.

## Senior questions

- Which store is the source of truth?
- How does deletion propagate to caches and providers?
- Can a conversation be moved between providers?
- What happens when two devices update state concurrently?
- How are partial streams represented in the user experience and audit log?

## Interview scenario

Design conversation memory for a health assistant. Separate temporary dialogue, user preferences, clinical facts, inferred information, consent, retention, correction, and provider-managed state.
