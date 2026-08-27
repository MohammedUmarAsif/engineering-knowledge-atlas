---
id: agent-evaluation-observability
title: Agent Evaluation and Observability
level: L3-L5
status: maintained
last_reviewed: 2026-08-27
prerequisites: [agent-loop-state, rag-evaluation-science]
---

# Agent Evaluation and Observability

## Evaluate systems, not demos

An agent demo selects a favorable task and celebrates completion. Evaluation samples a task distribution, freezes relevant versions, defines success independently, records trajectories, and measures uncertainty.

## Five layers

### Outcome

Did the environment reach the desired state? Prefer deterministic tests, database checks, simulator state, or expert judgment over the agent’s own completion message.

### Trajectory

Was the path valid and efficient? Measure invalid calls, redundant steps, recovery, plan changes, tool selection, evidence use, and policy violations. Do not require one golden trajectory when several are valid.

### Safety and authority

Did the system remain within permissions, respect approvals, protect data, and avoid forbidden effects? A successful outcome obtained through an unauthorized path is a failure.

### Efficiency

Track model tokens, calls, tool compute, wall time, monetary cost, and human review time. Report distributions and tail latency, not only averages.

### Robustness and recovery

Inject tool errors, delays, malformed outputs, duplicate delivery, stale state, adversarial content, and crashes. Measure whether the agent recovers, safely stops, or compounds the fault.

## Evaluation unit

Define the unit precisely:

- Single model decision.
- Tool-use episode.
- Complete task run.
- Multi-session user objective.
- Team of agents in an environment.

Mixing units creates misleading claims. High tool-call accuracy does not imply long-horizon task success.

## Dataset construction

Sample real task shapes across complexity, ambiguity, permissions, and failure conditions. Include:

- Routine cases.
- Boundary and rare cases.
- Tasks requiring user clarification.
- Impossible tasks where abstention is correct.
- Adversarial and untrusted inputs.
- Changed environments to test brittleness.

Keep development and final test suites separate. Record task provenance and expected environment version. Dynamic websites and APIs can invalidate repeatability; use controlled snapshots where appropriate.

## Metrics

Useful metrics include:

```text
task_success_rate
safe_success_rate = safe_and_successful / all_runs
conditional_cost = total_cost / successful_runs
excess_steps = executed_steps - minimal_valid_steps
recovery_rate = recovered_faults / injected_faults
approval_precision = justified_approval_requests / all_approval_requests
```

`minimal_valid_steps` may be unknown, so compare against a strong reference workflow or best observed valid path.

## Model judges

Model evaluators scale semantic review but inherit bias, prompt sensitivity, and model knowledge limits. Calibrate them against expert labels, blind conditions, randomize order, measure agreement, and keep deterministic checks for schemas, effects, citations, and policy.

Never let the same unconstrained model generate, judge, and declare production readiness without independent evidence.

## Benchmarks as instruments

[AgentBench](https://arxiv.org/abs/2308.03688) spans multiple interactive environments. [OSWorld](https://arxiv.org/abs/2404.07972) studies multimodal computer-use agents. [SWE-bench](https://www.swebench.com/) evaluates repository issue resolution. Each measures capability under a constructed environment; none directly predicts your product distribution.

Benchmark scores depend on scaffold, tool interface, allowed compute, contamination, environment health, and grading. Audit the instrument before treating a leaderboard as model truth.

## Traces

A useful trace records:

- Run, parent, and correlation IDs.
- Model/provider/version and configuration.
- State transition names and versions.
- Tool proposals, validated arguments, approvals, and results.
- Timing, retries, token/cost accounting.
- Artifact hashes and external effect IDs.
- Stop reason and verifier outcome.

Redact secrets and minimize personal data. Observability that leaks credentials is a security defect.

## Debugging method

1. Reproduce or capture the failing trace.
2. Find the first divergence from a valid trajectory.
3. Classify: observation, model decision, validation, policy, tool, state, or environment.
4. Fix the earliest causal boundary.
5. Add a regression task.
6. Run matched evaluation, including safety and cost.

Prompt edits made from the final bad sentence often treat symptoms rather than causes.

## Research standard

Report confidence intervals or repeated-run variability, exact budgets, model and scaffold versions, failure taxonomy, and negative results. Agent systems are stochastic systems interacting with changing environments; one successful run is an anecdote.
