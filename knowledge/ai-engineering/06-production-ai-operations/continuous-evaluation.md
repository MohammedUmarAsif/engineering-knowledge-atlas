---
id: ai-continuous-evaluation
title: Continuous Evaluation and Drift
level: L3-L5
status: maintained
last_reviewed: 2026-08-27
prerequisites: [ai-observability-slos, rag-evaluation-science]
---

# Continuous Evaluation and Drift

## Evaluation is a release control loop

Production AI evaluation answers three different questions:

1. Did this proposed change improve the controlled test distribution?
2. Is the deployed system behaving within expected boundaries?
3. Did the real user and environment distribution change?

One benchmark cannot answer all three.

## Gate by lifecycle stage

### Before merge

Run cheap deterministic tests, schema/property tests, prompt-policy linting, focused regression cases, and small component evaluations. Feedback must be fast enough that developers use it.

### Before deployment

Run broader frozen suites, safety/adversarial tests, dependency contract checks, load tests, and cost/latency comparisons against the current release.

### During canary

Compare matched traffic segments for operational regressions, route changes, sampled quality, policy violations, and cost per success. Protect users with hard runtime invariants even when statistical evidence is incomplete.

### In production

Sample representative and high-risk traces, monitor feedback and business outcomes, investigate distribution changes, and send adjudicated failures back to regression suites.

## Drift taxonomy

- Input drift: language, length, topics, user mix, adversarial patterns.
- Data drift: corpus, metadata, freshness, label or policy changes.
- Retrieval drift: index, embedding, ranking, access-filter behavior.
- Model drift: provider updates, snapshot behavior, refusal or formatting change.
- Tool drift: schema, permission, latency, or downstream semantics.
- Evaluator drift: judge model or rubric changes alter measured score.
- Concept drift: the mapping from inputs to correct behavior changes.

Detecting a distribution difference does not prove user harm. Link drift alerts to outcome changes and diagnostic slices.

## Paired comparisons

Where privacy and cost allow, replay a controlled sample through old and candidate systems. Hold inputs and evaluator constant. Randomize presentation for human/model judges and hide system identity.

Counterfactual replay cannot reproduce changed external tools or interactive branches perfectly. Label it offline evidence.

## Evaluator calibration

For semantic judgments:

- Define rubric with positive and negative examples.
- Collect expert labels and disagreement.
- Measure judge agreement by slice.
- Recalibrate after judge or rubric changes.
- Keep raw evidence for adjudication where policy permits.
- Combine judges with deterministic verification.

Quality metrics are measurements with error bars, not truth emitted by another model.

## Feedback

Thumbs-up/down is selected, sparse, and ambiguous. Users may reward tone while missing falsehood, or downvote a correct refusal. Combine explicit feedback with task completion, edits, retries, escalation, abandonment, and expert review.

Never train directly on unfiltered feedback without abuse, privacy, representativeness, and causal analysis.

## Regression ownership

Each evaluation failure needs category, severity, owner, adjudication, and expected fix layer. If a retrieval failure is “fixed” by prompt wording, the causal layer remains broken.

Retire obsolete or duplicate cases. Track suite coverage across task, risk, language, tenant, tool, and failure class.

## Game evaluation

Offline dialogue scores cannot establish player enjoyment. Combine automated canon/safety/style checks with playtests, retention-sensitive experiments, qualitative interviews, and telemetry on repetition, latency, overrides, and narrative outcomes.

## Research discipline

Whenever a dashboard score moves, ask whether the system changed, the population changed, the evaluator changed, or sampling changed. A metric without measurement lineage cannot support a causal claim.
