---
id: agent-research-frontier
title: Agent Research Frontier and Game AI Questions
level: L4-L5
status: maintained
last_reviewed: 2026-08-27
prerequisites: [agent-evaluation-observability, multi-agent-systems]
---

# Agent Research Frontier and Game AI Questions

## Read claims causally

Agent research bundles model, prompt, scaffold, tools, memory, search, compute, and evaluator into one system. When performance rises, ask which intervention caused it and what resource increased.

A research claim should specify:

- Task distribution and environment.
- Observation and action space.
- Model and inference budget.
- Scaffold and tool interface.
- Success verifier.
- Baselines under matched resources.
- Variance across runs.
- Failure taxonomy and limitations.

## Test-time compute and search

Agents can spend additional inference exploring, critiquing, or revising. More attempts may improve pass rate while raising latency and cost. Key questions:

- Does search discover genuinely different strategies or paraphrases?
- Can a value model predict success before expensive execution?
- How should compute adapt to task difficulty?
- Does performance saturate or degrade through context pollution?

Report success as a function of compute, not a single point.

## Process supervision and verifiers

Outcome supervision judges the final state. Process supervision evaluates intermediate decisions. Dense feedback can improve diagnosis but risks enforcing one preferred reasoning style or rewarding legible steps rather than correct internal computation.

Strong verifiers change the architecture: when actions can be cheaply tested, an agent can explore safely. Where truth is subjective or delayed, evaluator error becomes a central research problem.

## World models and partial observability

Agents act from incomplete observations. Memory and planning implicitly construct a world model, but language summaries can omit uncertainty. Research opportunities include belief-state representations, calibrated uncertainty, active information gathering, and detection of observations that contradict the current plan.

This connects directly to partially observable Markov decision processes, though LLM-agent environments often have vast textual state and non-stationary tools.

## Long-horizon credit assignment

A final failure may originate many actions earlier. Token-level training signals, trajectory-level rewards, and post-hoc textual reflections assign credit differently. Research should distinguish:

- Which decision was causally wrong?
- Was required information observable then?
- Could recovery have succeeded later?
- Did the tool interface make the correct action expressible?

## Multi-agent emergence

Interesting phenomena include conventions, specialization, deception, coalition formation, and communication protocols. But apparent emergence may arise from prompt roles or evaluator interpretation. Compare against deterministic coordination and matched-compute single-agent baselines.

## Human-agent systems

The objective is often team performance, not autonomous success. Study:

- When the agent asks versus assumes.
- Whether explanations improve calibrated trust.
- How approvals affect attention and fatigue.
- Whether users can recover control after an error.
- How expertise changes delegation behavior.

An agent that achieves high task success while training users to overtrust it may be socially unsafe.

## Game AI research program

### Believable bounded agents

**Question:** Can an agent preserve character goals and memory while remaining intentionally imperfect and fun?

Compare optimal-task reward with player-rated believability, surprise, fairness, and narrative coherence. Use authored constraints and deterministic world validation.

### NPC memory under conflicting testimony

**Question:** How should characters update beliefs when observations, rumors, and canon conflict?

Represent source, confidence, time, relationship, and accessibility. Evaluate downstream decisions and human perception, not only memory retrieval accuracy.

### Hierarchical planning across time scales

**Question:** Can language models propose long-term strategies while behavior trees, planners, or learned policies execute real-time actions?

Measure plan usefulness, repair frequency, runtime cost, and robustness to player disruption.

### Multi-agent social simulation

**Question:** Which social patterns are robust across seeds, prompts, models, and population sizes?

Pre-register metrics. Guard against interpreting entertaining anecdotes as stable emergent behavior.

### Designer-agent co-creation

**Question:** Can an agent expose design alternatives, constraints, and provenance without replacing authorial control?

Evaluate creative breadth, edit distance to accepted artifact, designer workload, ownership, and homogenization.

### MCP for game-development tooling

**Question:** Can standardized capability interfaces let assistants inspect assets, lore, builds, tests, and telemetry without acquiring broad editor or machine access?

Study permission ergonomics, latency, protocol overhead, discoverability, and containment of malicious project content.

## Paper-reading template

For each paper, write:

1. Problem and why prior methods fail.
2. Exact intervention.
3. Information and compute advantages over baselines.
4. Evaluation validity.
5. Strongest alternative explanation.
6. Ablation that would change your belief.
7. Reproduction obstacles.
8. Production and game-system transfer.
9. New falsifiable question.

## PhD-level standard

“This is promising” is not a conclusion. State a calibrated belief: under which environment, budget, and assumptions the method appears to help; which evidence is missing; and what experiment would most efficiently reduce uncertainty.
