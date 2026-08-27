---
id: ai-data-model-supply-chain-security
title: Data, Model, and Supply-Chain Security
level: L3-L5
status: maintained
last_reviewed: 2026-08-27
prerequisites: [ai-threat-modeling, document-intelligence-retrieval]
---

# Data, Model, and Supply-Chain Security

## The artifact lineage

```text
sources → dataset → preprocessing → training/fine-tuning → model artifact
       → packaging/runtime → deployment → prompts/retrieval/tools → outputs
```

Every arrow can introduce error or adversarial manipulation. Preserve provenance, approvals, versions, hashes, and evaluation evidence proportionate to risk.

## Poisoning

Poisoning manipulates training, fine-tuning, retrieval, feedback, memory, or evaluation data to alter future behavior. Goals can include broad degradation, targeted backdoors, misinformation, or hiding another weakness.

Defenses:

- Source authentication and reputation.
- Immutable raw-data lineage.
- Schema, distribution, duplication, and outlier checks.
- Restricted write paths and review.
- Canary examples and slice evaluations.
- Comparison against known-good data/model versions.
- Rapid revocation, reindexing, and rollback.

Outlier removal can itself erase rare but legitimate populations. Review controls for fairness and representativeness.

## Evasion and adversarial inputs

Evasion changes inference-time input to cause misclassification or bypass policy. Robustness depends on attacker knowledge, perturbation constraints, modality, and distribution. Claims like “adversarially robust” must specify the threat model and evaluated attack family.

For generative systems, jailbreaks and prompt transformations are forms of adversarial interaction, but system impact still depends on downstream authority and output consumption.

## Privacy and extraction

Threats include model inversion, membership inference, sensitive memorization, system-prompt extraction, retrieval leakage, and model stealing through repeated queries or artifact access.

Rate limits and output filtering may raise attacker cost but are not proofs of privacy. Training-data governance, minimization, access isolation, privacy evaluation, and deployment controls remain necessary.

## Model files are executable-adjacent

Some serialization formats can invoke code during loading. Prefer safer formats, isolate conversion, verify origin and hash/signature, scan artifacts, and load with minimum permissions. A model repository can also contain custom code, configuration, tokenizer logic, or templates that alter execution.

## Software and AI bill of materials

Track:

- Code packages, containers, base images, and build tools.
- Models, tokenizers, adapters, datasets, and licenses.
- Prompt/policy bundles and evaluation assets.
- MCP servers, plugins, tools, and external APIs.
- Owners, versions, provenance, vulnerabilities, and usage locations.

An SBOM alone does not capture data/model lineage; extend inventory without inventing false certainty.

## Dependency confusion and hallucinated packages

Generated code may import a nonexistent or attacker-controlled package. Validate dependencies against approved registries, lock files, signatures/provenance, and review. Never install a package merely because a model named it.

## Model registry controls

- Approved source and use case.
- License and data restrictions.
- Artifact hash/signature.
- Evaluation and red-team record.
- Known limitations and intended users.
- Deployment locations.
- Revocation and end-of-life status.

“Open weights” describes access, not safety, license simplicity, or provenance quality.

## Game pipeline

Treat generated meshes, textures, scripts, shaders, localization, mods, and model artifacts as untrusted build inputs. Validate formats, isolate converters, scan scripts, preserve source attribution, and require human review before publishing to players.

## Research question

How can poisoning detection distinguish malicious coordinated changes from legitimate cultural or language distribution shifts without systematically discarding minority data?
