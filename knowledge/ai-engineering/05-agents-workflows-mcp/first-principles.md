---
id: agent-first-principles
title: Agency from First Principles
level: L2-L5
status: maintained
last_reviewed: 2026-08-27
prerequisites: [tool-calling-and-side-effects]
---

# Agency from First Principles

## Agency is delegated control

A calculator call does not make a system an agent. Agency appears when a model chooses what to do next and that choice changes the future action path.

Consider a refund system:

- Deterministic program: always fetch order, test policy, calculate amount, ask for approval, issue refund.
- Workflow with model step: code fixes the path, but a model classifies the complaint.
- Agent: the model may inspect the order, search policy, ask the customer, escalate, or propose a refund based on observations.

The useful variable is **decision authority**, not marketing vocabulary.

## A compact formalization

At time `t`, the system has state `s_t`, receives observation `o_t`, and selects action `a_t` under policy `pi`:

```text
a_t ~ pi(a | goal, s_t, o_t, available_actions)
s_(t+1) = transition(s_t, a_t, result_t)
```

For an LLM agent, `pi` is partly represented by model weights and partly shaped by instructions, context, tool definitions, decoding, and runtime policy. The transition function must not be surrendered to generated prose. Application code validates the proposed action and records the real result.

## The autonomy ladder

Use the lowest rung that meets the requirement:

1. Deterministic code.
2. One model call producing bounded output.
3. Fixed workflow containing model calls.
4. Model-routed workflow with bounded branches.
5. Agent loop with read-only tools.
6. Agent with reversible writes and approvals.
7. Agent with narrowly scoped autonomous writes.
8. Open-ended, long-running or multi-agent system.

Each rung increases the reachable state space. More paths can solve unusual cases, but more paths can also fail, cost money, leak data, or become impossible to reproduce.

## Why loops help—and hurt

A single inference cannot observe the consequence of an action. A loop can:

```text
hypothesis → experiment/tool → observation → revised hypothesis
```

That is the source of agentic power. It is also error amplification. If a wrong observation enters state, later decisions may build a coherent but false world model. Long trajectories multiply exposure to model, tool, network, authorization, and state failures.

If each independent step succeeds with probability `p`, an oversimplified `n`-step trajectory succeeds with probability `p^n`. At `p = 0.98`, twenty steps yield about `0.67`, before accounting for recovery or correlated errors. The equation is not a real estimator; it reveals why “good per-step accuracy” is insufficient.

## Agent, workflow, search, and script

Choose an agent when all are substantially true:

- The correct sequence cannot be enumerated cheaply in advance.
- Intermediate observations determine future actions.
- The environment exposes useful, bounded actions.
- Success can be verified or judged.
- The value of flexibility exceeds added latency, cost, and risk.

Avoid an agent when:

- Business rules already determine the path.
- Exact reproducibility is mandatory.
- The system cannot verify progress or completion.
- One mistaken action creates irreversible harm.
- “Reasoning” compensates for a missing API, bad data model, or unclear product requirement.

## The thermostat intuition

A thermostat is a feedback controller: measure temperature, compare with target, actuate heating, repeat. An agent is a richer controller with a learned policy and a much larger action space. Control theory therefore supplies useful instincts:

- Observability: can the system infer relevant state from available signals?
- Controllability: can available actions actually move the environment toward the goal?
- Stability: do repeated corrections converge or oscillate?
- Delay: does the effect of an action arrive after the agent has already acted again?
- Noise: are observations reliable enough to support a decision?

An agent repeatedly sending “please retry” to a slow service is an unstable controller with delayed feedback.

## The implementation contract

Before implementation, write:

- Goal: what externally observable condition defines success?
- Environment: what state exists outside the model?
- Actions: which operations are allowed?
- Observations: what feedback does each action return?
- Invariants: what must always remain true?
- Budgets: when must execution stop?
- Authority: which actions need user or policy approval?
- Recovery: what happens after timeout, crash, or ambiguous completion?

If these cannot be stated, adding an agent framework only hides the uncertainty.

## Transfer lenses

**Full stack:** an agent is a stateful distributed workflow behind a user experience. HTTP timeouts do not imply work stopped; UI state must represent running, waiting, failed, and completed execution.

**Games:** an NPC action selector resembles an agent, but player-facing systems require bounded latency, believable imperfection, authored constraints, and reproducibility for debugging. The strongest action is not always the most enjoyable one.

**Research:** ask which component caused improvement. A larger model, more tokens, better tools, extra retries, or privileged observations can masquerade as a superior agent algorithm.

## Checkpoint

Explain why a five-step fixed workflow can be more sophisticated engineering than an open agent loop. Then name one task where model-controlled iteration is genuinely necessary.
