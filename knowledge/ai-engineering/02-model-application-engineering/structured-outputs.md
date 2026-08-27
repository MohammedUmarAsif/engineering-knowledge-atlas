---
id: structured-outputs-and-validation
title: Structured Outputs and Validation
level: L2-L4
status: maintained
last_reviewed: 2026-08-27
prerequisites: [inference-and-generation]
---

# Structured Outputs and Validation

## Diagnostic

Skip to [Tool Calling and Side Effects](tool-calling.md) if you can distinguish syntactic, schema, semantic, authorization, and business validation.

## Mental model

Structured generation constrains representation. It does not establish that a value is true, authorized, safe, current, or sensible.

## Five validation layers

1. **Transport:** a complete response arrived and belongs to the expected request.
2. **Syntax:** the payload parses.
3. **Schema:** types, required properties, enumerations, and shapes match.
4. **Semantic:** values correspond to source evidence and domain meaning.
5. **Business/policy:** the requested result is allowed in the current state for this user.

Only the first three are primarily formatting problems.

## Contract design

Prefer small, explicit schemas:

- stable field names;
- descriptions that explain meaning, not only type;
- enumerations for closed decisions;
- explicit nullable/optional semantics;
- bounded arrays and strings;
- schema version;
- a place for evidence or abstention when appropriate.

Avoid asking the model to manufacture authoritative IDs, timestamps, prices, permissions, or calculated totals when conventional code can provide them.

## JSON Schema reality

JSON Schema Draft 2020-12 is the current published specification, but model providers commonly support only subsets. Treat the provider's supported dialect as a capability and validate the result again with your own runtime validator.

## Repair and retry

Use a bounded policy:

- deterministic repair for superficial serialization defects when meaning is unambiguous;
- regeneration when the response violates a recoverable schema constraint;
- explicit failure or human review when semantic meaning is uncertain;
- no blind retry for forbidden or dangerous content.

Store the original output when policy permits so repairs remain auditable.

## Versioning

Schema changes are API changes. Use additive evolution where possible, version consumers, test older stored responses, and ensure fallbacks support the same contract.

## Structured output versus tool call

- Use **structured output** when the final answer must feed a renderer, classifier, extractor, or downstream deterministic computation.
- Use **tool calling** when the model proposes that application code obtain information or perform an operation.

A tool's arguments may themselves use a schema, but the security and lifecycle implications differ.

## Senior questions

- Which fields are model judgments versus authoritative facts?
- Can the consumer tolerate unknown enum members?
- What happens to partially streamed JSON?
- How are evidence and provenance represented?
- What is the safe behavior when validation fails repeatedly?

## Interview scenario

A model returns a schema-valid refund object for an ineligible order. Identify which validation layers passed, which failed, and where the refund decision must live.

## Primary source

- [JSON Schema specification](https://json-schema.org/specification)
