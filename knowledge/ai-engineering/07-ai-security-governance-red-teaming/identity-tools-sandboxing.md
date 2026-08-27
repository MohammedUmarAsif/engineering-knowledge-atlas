---
id: ai-identity-tools-sandboxing
title: Identity, Tools, Sandboxes, and Least Agency
level: L3-L5
status: maintained
last_reviewed: 2026-08-27
prerequisites: [ai-prompt-injection, agent-tools-mcp]
---

# Identity, Tools, Sandboxes, and Least Agency

## Authentication is not authorization

Authentication establishes an identity. Authorization decides whether that principal may perform a specific action on a specific resource under current conditions. A valid API key or OAuth token does not prove user intent or justify every capability it technically enables.

## Identity propagation

Preserve the originating user/service identity and tenant through gateway, workflow, queue, retrieval, tools, and audit. Avoid replacing all downstream calls with one omnipotent service identity.

Where delegation is necessary, record:

- Actor and delegating principal.
- Requested action and target.
- Scope, audience, purpose, and expiry.
- Approval/policy decision.
- Execution and effect identifiers.

## Least agency

OWASP frames excessive agency through excessive functionality, permissions, and autonomy. Reduce all three:

- Functionality: expose only necessary tools.
- Permissions: narrow credential/resource scope.
- Autonomy: require approval or fixed workflow where judgment is not justified.

Also limit duration, concurrency, volume, recipients, money, environments, and reachable networks.

## Capability design

A capability grants authority by possession. Short-lived, narrowly scoped capabilities can be safer than ambient global credentials. Bind them to an exact audience and operation where infrastructure permits.

Do not put bearer credentials in model context. The executor holds credentials; the model proposes typed intent.

## Approval integrity

Bind approval to a canonical action hash containing tool, arguments, target, actor, relevant state version, and expiry. If any material field changes, approval is invalid.

Show the user consequences and transmitted data. “Allow agent to continue?” is not informed approval.

## Sandboxing boundaries

A sandbox restricts execution through process/VM isolation, filesystem mounts, network policy, resources, syscalls, credentials, and lifetime. It does not automatically prevent:

- Exfiltration through allowed network endpoints.
- Abuse of credentials deliberately mounted inside.
- Harmful but authorized API calls.
- Side channels.
- Vulnerabilities in the sandbox/runtime.
- Poisoned artifacts returned to the host.

Treat outputs as untrusted and scan/validate them at egress.

## Tool contracts

Classify tools by read/write/destructive, internal/external, data sensitivity, reversibility, and open-world behavior. Enforce:

- Input/output schemas and size limits.
- Domain invariants.
- Current authorization.
- Idempotency and reconciliation.
- Time/resource budgets.
- Egress allowlists.
- Auditable effect identifiers.

Server or MCP annotations can inform UI and routing but cannot substitute for host policy.

## Multi-agent privilege

Agents should not launder authority through peers. A low-privilege researcher cannot delegate a restricted deployment to a high-privilege operator without an explicit policy transition. Propagate origin and purpose through handoffs.

## Game example

A narrative agent may read approved lore and propose quest text. It cannot directly grant inventory, ban players, spend store currency, publish builds, or read private chat. Those are separate services with deterministic policy and human or game-rule authority.

## Failure exercise

An agent receives permission to update one issue but writes to ten repositories. Identify failures in functionality exposure, scope, target validation, approval binding, effect limits, and anomaly detection.
