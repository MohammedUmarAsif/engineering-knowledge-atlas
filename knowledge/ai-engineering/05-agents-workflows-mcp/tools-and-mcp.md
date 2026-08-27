---
id: agent-tools-mcp
title: Tools, Contracts, and Model Context Protocol
level: L2-L5
status: maintained
last_reviewed: 2026-08-27
prerequisites: [agent-loop-state, tool-calling-and-side-effects]
---

# Tools, Contracts, and Model Context Protocol

## A tool is an effectful boundary

A tool turns a model proposal into a request against an external capability. The tool description influences model choice; the schema constrains syntax; application policy determines authority; the implementation produces effects.

Good tool design makes the correct action easy to select and the dangerous action hard to express.

## Contract anatomy

Define:

- Semantic name and one-purpose description.
- Typed input and output schemas.
- Preconditions and authorization rules.
- Read/write/destructive classification.
- Idempotency behavior.
- Timeout, cancellation, and retry policy.
- Error taxonomy.
- Provenance and audit fields.
- Maximum result size and redaction policy.

Prefer `issue_refund(order_id, amount, reason)` to `run_sql(query)`. The first exposes domain intent that policy can understand. The second transfers nearly unlimited authority through text.

## Why descriptions affect reasoning

The model does not inspect your implementation. It sees names, descriptions, and schemas. Overlapping tools create an ambiguous action space. Missing constraints cause invalid plans. Giant toolsets consume context and reduce selection precision.

Treat tool discovery like information retrieval: shortlist capabilities relevant to the current goal, while ensuring the router cannot hide a necessary tool.

## MCP in one sentence

The [Model Context Protocol](https://modelcontextprotocol.io/specification/2026-07-28/) standardizes how an AI application discovers and exchanges capabilities and context with external servers. It does not decide the agent loop, grant trust, or prove a server is safe.

## Architecture

```text
user
  │
  ▼
host application
  ├── MCP client A ↔ server A
  ├── MCP client B ↔ server B
  └── model + policy + UI + agent runtime
```

- Host: user-facing application coordinating models, permissions, and clients.
- Client: protocol participant maintaining a connection to one server.
- Server: exposes capabilities.

Keeping these roles separate prevents the common misconception that “the MCP server talks directly to the model and owns the agent.” The host remains responsible for orchestration and user control.

## Server primitives

- Tools are model-invocable operations, usually with potential computation or effects.
- Resources are application-controlled context identified by URIs.
- Prompts are user-controlled reusable templates or workflows exposed by a server.

The control labels are conceptual defaults, not excuses to omit policy. A resource can still contain malicious instructions; a read-only tool can still leak sensitive information.

MCP also defines client-side features such as sampling and elicitation. In the 2026-07-28 revision, servers request such input through a multi-round-trip result: the server returns `input_required`, and the client retries the original request with responses. Sampling and Roots are now deprecated for new implementations; learn them for compatibility, not as default architecture. These capabilities enlarge the trust surface even when transport direction is request/response.

## Wire mechanics

MCP uses JSON-RPC messages and capability negotiation. The current `2026-07-28` specification defines `stdio` and Streamable HTTP bindings. With `stdio`, a client launches a subprocess and exchanges framed messages. Streamable HTTP supports remote interaction and requires appropriate transport and authorization handling.

The modern protocol is stateless: there is no initialization handshake or protocol session. Every request carries protocol version, client capabilities, and normally client identity in `_meta`; servers must implement `server/discover` for supported versions, capabilities, and identity. Older revisions are handshake-based, so dual-era implementations need explicit compatibility logic. Never assume every peer supports every feature.

Example conceptual tool definition:

```json
{
  "name": "read_game_lore",
  "description": "Return approved canon entries by stable ID; no player-private state",
  "inputSchema": {
    "type": "object",
    "properties": {"ids": {"type": "array", "items": {"type": "string"}}},
    "required": ["ids"]
  },
  "annotations": {"readOnlyHint": true, "openWorldHint": false}
}
```

Annotations are hints, not enforceable permissions. The host must apply policy independently.

## Transport is not trust

`stdio` reduces network exposure but executes a local process with operating-system privileges. Remote HTTP introduces authentication, token, origin, session, and network risks. In either case:

- Pin or review server code and dependencies.
- Isolate processes and filesystems.
- Pass minimum credentials.
- Scope access per user and tenant.
- Log tool intent and confirmed effects without leaking secrets.
- Require approval for consequential operations.

For HTTP authorization, follow the current MCP OAuth requirements, including protected-resource discovery, issuer validation, and resource/audience binding. Token passthrough is prohibited because a server must not reuse a token intended for another downstream service.

## MCP versus adjacent concepts

| Concept | Solves | Does not solve |
|---|---|---|
| Function/tool calling | model emits structured action | cross-application interoperability |
| MCP | capability/context protocol | agent planning, trust, business authorization |
| Agent framework | loop/state/orchestration | universal external capability protocol |
| OpenAPI | HTTP API description | AI host lifecycle and bidirectional features |
| Plugin/extension | packaged integration | necessarily portable protocol semantics |

## Version and maturity discipline

Protocol evolution is active. The July 2026 revision removed protocol-level sessions, made capabilities per-request, introduced `server/discover`, moved Tasks into an opt-in official extension, and deprecated Roots, Sampling, Logging, legacy HTTP+SSE, and Dynamic Client Registration for new implementations. It also defines extensions including Tasks, Skills over MCP, and MCP Apps. Pin SDK majors, record the protocol revision on every trace, and separate stable concepts from volatile syntax.

## Build-versus-use decision

Build an MCP server when multiple compatible hosts should reuse a capability, discovery matters, or protocol-level integration reduces custom adapters. Use an internal function when one application owns both sides and portability adds no value. Do not wrap every helper in a server merely to appear “agent native.”

## Deep checkpoint

An MCP server advertises a tool as read-only, but its implementation sends analytics containing document text. Identify the failures at the semantic, policy, privacy, and protocol-assumption layers.
