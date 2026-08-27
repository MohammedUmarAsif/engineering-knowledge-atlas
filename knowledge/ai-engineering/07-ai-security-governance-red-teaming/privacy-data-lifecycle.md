---
id: ai-privacy-data-lifecycle
title: Privacy and the AI Data Lifecycle
level: L3-L5
status: maintained
last_reviewed: 2026-08-27
prerequisites: [ai-data-model-supply-chain-security, ai-governance-security]
---

# Privacy and the AI Data Lifecycle

## Privacy is more than secrecy

Confidentiality asks whether unauthorized parties access data. Privacy also asks whether collection, inference, use, combination, retention, and decisions are appropriate, expected, contestable, and lawful in context.

Publicly accessible data is not automatically unrestricted training, profiling, or permanent-memory data.

## Map the complete lifecycle

For every data class:

```text
source/consent → collection → classification → transformation
→ model/retrieval/tool processing → telemetry/evaluation → sharing
→ storage/backups → retention → deletion/rights response
```

Include derived data: embeddings, summaries, inferred preferences, labels, caches, fine-tuned weights, evaluation fixtures, and moderation records.

## Data minimization

Collect and expose only what is necessary for a specified purpose. Minimize at several boundaries:

- Before prompt construction.
- Before retrieval results enter context.
- Before tool arguments leave the application.
- Before telemetry export.
- Before human/model evaluation.
- Before long-term memory.

Redaction after a provider call is too late for provider disclosure.

## Purpose and scope

Data collected to answer a user request is not automatically approved for product analytics, training, advertising, or research. Record purpose and compatible uses. Separate operational telemetry from optional improvement programs where required.

## Inference privacy

AI systems can infer sensitive attributes never explicitly provided. An inferred health condition or vulnerability can matter as much as a stored declaration. Govern outputs, downstream use, and retention of inferences.

## Tenant and user boundaries

Enforce isolation at source connector, ingestion, index, retrieval filter, cache key, prompt assembly, tool, memory, trace, evaluator, and support access. Test with adversarial cross-tenant fixtures.

Pseudonymization reduces direct identifiability but is not anonymization when records can be re-linked.

## Retention and deletion

Define purpose-specific retention. Deletion must propagate through primary stores, caches, indexes, derived memories, evaluation sets, and provider processes, while accounting for legitimate audit or backup constraints.

Keep a deletion state machine and evidence. “Deleted from the UI” is not proof.

Model unlearning may be technically uncertain or infeasible for a particular deployed model. Avoid promising exact removal from weights without verified capability; prevent unnecessary inclusion first.

## Telemetry choices

Prefer metadata and sampled, access-controlled content. Redact secrets before export. Audit evaluator and support access. Apply region and subprocessors policy. Test redaction on multilingual text, structured fields, images, audio transcripts, and tool results.

## Privacy evaluation

- Canary secrets that should never surface.
- Cross-user and cross-tenant isolation tests.
- Membership/inference risk assessment where relevant.
- Data-flow and retention verification.
- Access-log review.
- Provider contract/configuration verification.
- Human review for contextual privacy harms.

Absence of a known leak in a finite test is not proof of privacy.

## Game and research

Voice chat, child accounts, social graphs, behavioral telemetry, inferred emotion, and accessibility data demand special care. Separate ordinary game operation from research participation. Consent must be meaningful, withdrawal usable, and experimental datasets access-controlled and minimized.

## Design question

Can the desired feature work with on-device processing, transient context, aggregates, synthetic data, or user-controlled memory instead of raw centralized retention?
