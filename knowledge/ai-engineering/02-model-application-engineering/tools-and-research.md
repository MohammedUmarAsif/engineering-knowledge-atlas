---
id: model-application-tools-research
title: Model Application Tools and Research Map
level: L2-L5
status: maintained
last_reviewed: 2026-08-27
prerequisites: [model-application-engineering]
---

# Model Application Tools and Research Map

## Selected repositories

### [OpenAI Cookbook](https://github.com/openai/openai-cookbook)

- Approximately 75k stars; MIT; official examples and guides, primarily Python.
- Use it for current API patterns and concrete experiments.
- Examples are provider-specific starting points, not an application architecture or security policy.

### [Pydantic](https://github.com/pydantic/pydantic)

- Approximately 28k stars; MIT; mature Python validation based on type hints.
- Use it to distinguish deserialization and schema validation from semantic and business validation.

### [Instructor](https://github.com/567-labs/instructor)

- Approximately 11k stars reported by its documentation; MIT; structured extraction across multiple providers.
- Study typed extraction, retries, streaming, and validation feedback.
- Automatic retry can multiply cost or repeat a bad policy; keep retry classification and limits explicit.

### [PydanticAI](https://github.com/pydantic/pydantic-ai)

- MIT; typed Python agent/application framework with provider integrations, tools, MCP, evaluation, and observability integrations.
- Study how type-safe application patterns extend to tools and workflows.
- Adopt only after understanding the underlying model, tool, state, and authorization boundaries described in this module.

## Framework rule

Do not begin an architecture discussion with LangChain, PydanticAI, an SDK, or any other framework. Begin with the domain contract and failure model, then decide whether a framework removes more complexity than it introduces.

## Current engineering directions

### Typed generation

Provider-native constrained decoding and schema-aware libraries are replacing “ask for JSON and parse whatever arrives.” The frontier is semantic validation: structure can be guaranteed more easily than truth, evidence, authorization, or business validity.

### Durable agents

Long-running work increasingly separates model decisions from durable workflow state, checkpoints, queues, approvals, and idempotent activities. This connects AI engineering to workflow engines and distributed-systems practice.

### Context compilation

Prompt text is evolving into a compiled context assembled from policies, state, retrieval, tools, memory, and modality-specific sources. Research and tooling increasingly focus on automatic optimization, caching, compression, and evaluation; security boundaries must remain explicit.

### Protocol-based tools

MCP and related interoperability efforts reduce bespoke integration glue. A standard connection format does not solve authorization, trust, tool quality, state, or prompt injection. Those remain application concerns.

### Agentic development

AI systems can inspect repositories, execute tools, propose changes, and coordinate workflows. The production question is not “Can the agent act?” but “Which actions are bounded, observable, reversible, attributable, and economically justified?”

## Forward-deployed and game transfer

Forward-deployed engineering rewards rapid integration plus strong product, data, security, and operational judgment. Agent orchestration can help integrate heterogeneous customer systems, but requires disciplined boundaries.

In games, similar orchestration may coordinate dialogue, planning, asset pipelines, QA agents, player-support systems, or research simulations. Runtime gameplay often requires tighter latency, determinism, safety, and creative control than enterprise automation.

## Research questions

- How should agent reliability compose across multiple probabilistic steps?
- When does an orchestrator-of-agents outperform a simpler workflow after accounting for cost and failure?
- How can tool descriptions and permissions be verified automatically?
- Which forms of memory improve tasks without creating privacy and behavioural instability?
- How should human approval be optimized without becoming meaningless click-through?
