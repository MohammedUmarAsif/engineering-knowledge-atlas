---
id: ai-production-research-frontier
title: Production AI Research Frontier and Game Live Operations
level: L4-L5
status: maintained
last_reviewed: 2026-08-27
prerequisites: [ai-continuous-evaluation, ai-cost-engineering]
---

# Production AI Research Frontier and Game Live Operations

## Operations produces research questions

Production traces reveal failures, distribution shifts, human adaptation, and resource constraints absent from static benchmarks. They are also biased observational data shaped by routing, policy, sampling, and who chose to use the product.

Do not confuse large telemetry volume with experimental validity.

## Semantic reliability

Ordinary services often define success through protocol and state. AI outcomes can be graded, delayed, subjective, or unknowable at response time.

Open questions:

- How should semantic uncertainty enter SLOs and error budgets?
- Can sampled quality estimates support fast burn-rate alerts?
- How do evaluator errors propagate into release decisions?
- Which product signals best approximate usefulness without rewarding manipulation?

## Adaptive routing

Routing models by predicted task difficulty, risk, deadline, and budget resembles a contextual decision problem. Research must account for selective labels: only the chosen model’s outcome is observed.

Compare adaptive policies against transparent rules under matched cost and safety. Use exploration cautiously because users bear the experiment.

## Efficient serving under heterogeneous demand

Real workloads mix long and short contexts, interactive and batch deadlines, adapters, modalities, and priority classes. Scheduling can optimize throughput while creating unfair tails.

Study Pareto frontiers across quality, TTFT, throughput, energy, cost, fairness, and availability, not one throughput maximum.

## Evaluation under change

Benchmarks, judge models, providers, corpora, and user distributions evolve. Research questions include version-robust evaluation, contamination detection, causal monitoring, uncertainty-aware judges, and representative sampling under privacy constraints.

## Agent operations

Long-running agents introduce delayed effects, growing state, human approvals, and path-dependent failures. Needed work includes trajectory anomaly detection, authority-aware scheduling, safe resumption across model changes, and reliable accounting for speculative branches.

## Game live-operations program

### Latency versus believability

**Hypothesis:** a hybrid system using immediate authored acknowledgement plus delayed generated continuation improves perceived responsiveness without reducing character coherence.

Randomize at session level; measure perceived latency, coherence, abandonment, fallback detection, and compute.

### Designed degradation

**Question:** Which fallback preserves player trust during inference failure: authored lines, local small models, delayed dialogue, or transparent unavailability?

Test by context and player expectation. Concealing a fallback may harm trust if behavior changes sharply.

### Cost-aware narrative allocation

**Question:** Can high-cost generation be reserved for narratively important moments using a learned or authored value estimator?

Compare player outcomes and author review under a fixed inference budget; guard against concentrating quality only on already-engaged players.

### Drift in persistent characters

**Question:** How do model or prompt upgrades change a character across months, and which continuity metrics match player perception?

Use frozen scenario suites, longitudinal playtests, canon constraints, and change-point analysis.

### Privacy-preserving learning from play

**Question:** What minimal telemetry supports dialogue improvement without retaining raw sensitive conversation?

Compare aggregates, local processing, redacted samples, and consented research cohorts for utility and privacy risk.

## Experiment standard

State hypothesis, population, unit of randomization, treatment, baseline, outcome, safety guardrails, power/uncertainty, stopping rule, privacy basis, and rollout reversal. Report operational cost and failure slices alongside average quality.
