---
id: ai-security-detection-response
title: Detection, Response, and Recovery
level: L3-L5
status: maintained
last_reviewed: 2026-08-27
prerequisites: [ai-red-teaming, ai-incidents-resilience]
---

# Detection, Response, and Recovery

## Assume some prevention fails

Detection asks whether the system can recognize attack progress or harmful effects early enough to contain impact. AI behavior is variable, so detection combines deterministic security events, behavioral signals, semantic evaluation, and business invariants.

## Signal layers

- Identity: unusual principals, scopes, token audiences, approval patterns.
- Input: repeated transformations, suspicious carriers, abnormal upload/source patterns.
- Retrieval/memory: cross-boundary access, poisoned-source indicators, unusual write/read relationships.
- Model: policy-violating outputs or sudden behavior shifts.
- Tools: unexpected tool, target, argument, recipient, data volume, or sequence.
- Infrastructure: queue/cost spikes, model extraction patterns, sandbox/network anomalies.
- Outcome: unauthorized effect, disclosure canary, player/user report, reversal or complaint.

Model-level anomaly signals are weaker than confirmed effect telemetry. Prioritize alerts by asset impact and confidence.

## Canary assets

Synthetic secrets, records, documents, or tool targets can reveal unauthorized access or disclosure. They must not resemble real credentials that could cause external harm. Track exactly where canaries are placed so alerts remain interpretable.

## Behavioral baselines

Compare tool sequences, data volume, recipients, failure/retry patterns, and route changes against role and workload. Attackers can mimic normality; novel users can look anomalous. Use baselines to prioritize investigation, not automatically punish users.

## Security trace

Preserve actor, tenant, delegated authority, data provenance, model/prompt/policy/tool versions, proposals, approvals, execution decisions, effect IDs, external targets, and result. Protect content through minimization, redaction, retention, and restricted access.

Audit logs need integrity controls. An agent should not be able to delete the only evidence of its own action.

## Response playbooks

Prepare containment at narrow scopes:

- Disable a tool or MCP server.
- Revoke credential or delegation.
- Block a source/connector and reindex.
- Isolate tenant or route.
- Stop agent runs or queued jobs.
- Roll back prompt/model/policy/index bundle.
- Disable generated output while serving safe fallback.

Global shutdown remains necessary for catastrophic uncertainty, but fine-grained controls reduce harm from response itself.

## Reconciliation

After containment, determine what data was accessed, what outputs were shown, what external effects committed, which users/tenants were affected, whether caches or memories persisted content, and which credentials require rotation.

An AI incident can have semantic impact without obvious database corruption. Review user-visible answers and downstream decisions under authorized evidence handling.

## Post-incident improvement

Map the earliest violated assumption, missed prevention, detection delay, blast-radius control, response friction, and governance decision. Add regression tests and detection validation. Update threat model and residual-risk acceptance.

Do not close an injection incident solely by adding the observed phrase to a blocklist.

## Metrics

- Mean time to detect, contain, reconcile, and recover.
- Unauthorized proposals versus effects.
- Detection coverage by ATLAS/abuse scenario.
- False-positive burden and analyst time.
- Repeat incident class.
- Control-test freshness.
- Percentage of critical actions with attributable approval/effect IDs.

## Game live incident

If a coordinated group manipulates NPCs into disclosing other players’ memories, disable shared-memory retrieval, preserve tenant/player isolation evidence, invalidate caches, identify exposed sessions, provide authored fallback, notify responsible teams and affected users as required, then retest with synthetic worlds before gradual restoration.
