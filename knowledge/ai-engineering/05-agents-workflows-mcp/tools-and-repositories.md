---
id: agent-tools-repositories
title: Agent and MCP Tool Map
level: L2-L5
status: maintained
last_reviewed: 2026-08-27
prerequisites: [agent-tools-mcp]
---

# Agent and MCP Tool Map

## Selection rule

Choose a framework after drawing the desired state machine and trust boundaries. Otherwise, its abstractions silently become the architecture.

Stars below are volatile adoption signals, not quality scores. Verify current release, license, security posture, and migration status before committing.

## Protocol and SDKs

- [MCP specification](https://modelcontextprotocol.io/specification/2026-07-28/): source of truth for protocol behavior; read the changelog, architecture, versioning, transports, authorization, primitives, extensions, and security guidance.
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk): official Python client/server implementation. Pin a stable major because the SDK has active version transitions.
- [MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk): official TypeScript packages for clients, servers, and transports.
- [MCP Inspector](https://github.com/modelcontextprotocol/inspector): interactive protocol testing. It helps inspect behavior; it does not replace automated contract or security tests.
- C++ currently has no SDK in the official tier list. Treat community implementations as third-party dependencies and assess conformance, maintainership, revision support, and security before adoption; protocol understanding and generated schemas can outlast a specific SDK.

## Agent runtimes

- [LangGraph](https://github.com/langchain-ai/langgraph): graph-based, stateful orchestration with durable execution and human-in-the-loop facilities. Useful when explicit state graphs matter; abstraction and ecosystem complexity require discipline.
- [OpenAI Agents SDK for Python](https://github.com/openai/openai-agents-python): compact primitives for agents, tools, handoffs, guardrails, sessions, and tracing. Provider alignment can be helpful; isolate application contracts from vendor-specific runtime APIs.
- [Microsoft Agent Framework](https://github.com/microsoft/agent-framework): successor direction combining Microsoft’s agent-framework work; verify migration guidance if evaluating older AutoGen or Semantic Kernel material.
- [AutoGen](https://github.com/microsoft/autogen): influential event-driven and multi-agent project. Read its architecture and research, while checking current maintenance and framework-transition status.
- [smolagents](https://github.com/huggingface/smolagents): deliberately small code-agent and tool-calling framework. Excellent for reading implementation ideas; generated-code execution demands genuine sandboxing.
- [PydanticAI](https://github.com/pydantic/pydantic-ai): typed Python agent application patterns. Useful when schema and dependency injection fit the codebase.
- [CrewAI](https://github.com/crewAIInc/crewAI): role-oriented agent and workflow abstractions. Evaluate against a simpler single-agent or graph baseline rather than assuming roles add capability.

## Durable workflow systems

- [Temporal](https://github.com/temporalio/temporal): general durable execution platform, not an AI framework. Strong when long-running state, retries, timers, and recovery are core.
- [Prefect](https://github.com/PrefectHQ/prefect) and [Dagster](https://github.com/dagster-io/dagster): data/workflow orchestration ecosystems that may fit deterministic AI pipelines better than an agent-specific runtime.

## Evaluation and observability

- [Langfuse](https://github.com/langfuse/langfuse): open-source tracing and evaluation platform for LLM applications.
- [Arize Phoenix](https://github.com/Arize-ai/phoenix): observability and evaluation for AI traces and retrieval.
- [OpenTelemetry](https://github.com/open-telemetry/opentelemetry-specification): vendor-neutral telemetry concepts; use stable semantic conventions where available and retain domain-specific fields.
- [Inspect AI](https://github.com/UKGovernmentBEIS/inspect_ai): evaluation framework designed for model and agent assessments, including tools and sandboxes.

## Sandboxes

- [E2B](https://github.com/e2b-dev/E2B): managed isolated execution environments.
- [gVisor](https://github.com/google/gvisor) and [Firecracker](https://github.com/firecracker-microvm/firecracker): lower-level isolation technologies; operating them safely is infrastructure work, not a library toggle.

## Reading repositories like a senior engineer

Inspect:

1. Core loop and state representation.
2. Tool validation and error paths.
3. Persistence and crash recovery.
4. Cancellation semantics.
5. Trace schema and redaction.
6. Security policy and dependency graph.
7. Tests for duplicate execution and partial failure.
8. Release cadence, breaking changes, and migration documentation.

Build one small agent without a framework first. Then you can identify which framework features remove real engineering burden and which merely rename the loop.
