# Curriculum Quality Review

## Purpose

This atlas is reviewed as a learning system, not merely a folder of correct pages. A module should strengthen the mental model established before it, avoid hidden prerequisite gaps, distinguish durable concepts from volatile tools, and make claims proportionate to evidence.

## Automated checks

Run:

```bash
python3 scripts/validate_repository.py
```

The validator checks:

- internal Markdown targets;
- required topic metadata;
- unique topic IDs;
- resolved prerequisites;
- prerequisite cycles;
- navigation coverage for every knowledge page;
- duplicate resource-manifest IDs;
- diagnostics and reading orders in AI module overviews.

Python examples are compiled and executed when the runtime is available. C++ examples are compiled when Apple Command Line Tools or another C++20 compiler is installed.

## Manual learning review

For every module, inspect:

1. Progression: does it use only concepts already introduced or explicitly linked?
2. Precision: are memorable intuitions refined before they become misconceptions?
3. Mechanism: can the reader follow data, control, memory, authority, or failure end to end?
4. Choice: are alternatives and “do not use” conditions present?
5. Failure: are symptoms separated from causal layers?
6. Evidence: are benchmark, repository, vendor, standard, and atlas-inference claims distinguished?
7. Currency: are evolving specifications versioned and maturity/deprecation stated?
8. Transfer: are Python, C++, full-stack, games, and research connections used only where meaningful?
9. Mastery: do diagnostics and defenses test explanation and design rather than recall?
10. Cognitive load: is repetition purposeful reinforcement rather than duplicated reading?

## Review record — 2026-08-27

The review performed while adding Production AI Operations found and repaired:

- two unresolved Module 05 prerequisite IDs;
- three earlier overview pages that called already-built modules “future”;
- missing automated checks for prerequisite integrity, cycles, navigation, and manifest uniqueness;
- an RAII example whose destructor could indirectly throw;
- stale tool-status context for Text Generation Inference;
- the relocation and development status of OpenTelemetry GenAI semantic conventions.

The conceptual progression was checked across Modules 02, 05, and 06. Module 02 introduces application-level reliability contracts; Module 05 applies them to autonomous state and effects; Module 06 develops the surrounding delivery, serving, observability, evaluation, cost, governance, and incident systems. Repeated concepts such as idempotency and fallback are retained because each module examines a different boundary.

## Review record — Module 07: AI Security, Governance, and Red Teaming

The Module 07 review checked both technical correctness and learning safety:

- security, safety, privacy, reliability, ethics, governance, and compliance are separated before their overlaps are discussed;
- the threat model starts from assets, trust boundaries, identities, authority, and effects rather than from a generic attack checklist;
- prompt injection is treated as an influence-to-authority path, so model refusal rates are not confused with end-to-end protection;
- red-team guidance is restricted to authorized systems, declared rules of engagement, synthetic or approved data, and reversible effects;
- attack evaluation distinguishes what a model proposes from what the surrounding system actually authorizes and executes;
- current standards and regulation pages state their date, jurisdiction, role, and limits instead of presenting a framework as proof of security or legal compliance;
- the C++ approval-token example labels `std::hash` as a teaching placeholder, not a cryptographic production primitive;
- controls introduced in the RAG, agent, and operations modules are linked as prerequisites and revisited only where the security boundary changes their meaning.

The module was checked against NIST AI RMF and adversarial-ML guidance, MITRE ATLAS, the OWASP 2026 GenAI and agentic risk lists, ISO/IEC 42001, and official EU AI Act implementation material current on 2026-08-27. These sources provide complementary lenses; none is treated as a complete assurance argument.

## Review record — v0.1.1 presentation

The recruiter-facing presentation review applied the same evidence discipline used inside the modules:

- completed, next, scaffolded and long-term work are visibly separated;
- repository metrics are derived from the release contents and used as scope indicators, not as proof of mastery;
- selected deep links let a reviewer inspect reasoning instead of relying on self-description;
- personal goals explain prioritization without being presented as completed expertise;
- Harvard, MIT and Oxford references link to an explicit source map that states their influence and limitations;
- university references are not described as standards, affiliations, credentials or degree equivalence;
- L0–L5 labels describe the demanded reasoning rather than claiming that every page is graduate or PhD level;
- badges are limited to validation, release, licensing and review currency.
- CI actions are pinned to reviewed release commits, and the validation badge now covers repository structure, executed Python examples, C++20 syntax compilation and a strict documentation build.

## Review discipline

A passing validator establishes structural consistency, not truth. Current specifications, regulations, prices, model behavior, repository status, and tool APIs require source review at the time of study or implementation.
