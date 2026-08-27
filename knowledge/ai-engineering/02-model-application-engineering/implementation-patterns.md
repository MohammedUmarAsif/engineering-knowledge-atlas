---
id: model-application-implementation-patterns
title: Model Application Engineering in Python and C++
level: L2-L4
status: maintained
last_reviewed: 2026-08-27
prerequisites: [model-application-engineering]
---

# Model Application Engineering in Python and C++

## Purpose

See the same architecture expressed in both priority languages. The examples avoid a particular model provider so the domain boundary remains stable.

Runnable files are under:

- [Python contracts example](../../../examples/model-application-engineering/python/contracts.py)
- [C++ contracts example](../../../examples/model-application-engineering/cpp/contracts.cpp)

## Shared design

Both programs implement:

1. a domain request;
2. a normalized model result;
3. an adapter interface;
4. deterministic validation after generation;
5. a tool executor with authorization and idempotency;
6. a fake adapter so the architecture is testable without credentials.

## Python view

Python makes the orchestration compact. Dataclasses and protocols express useful contracts, but runtime validation remains necessary because type hints do not enforce external data.

```python
class ModelAdapter(Protocol):
    def generate(self, request: GenerationRequest) -> ModelResult: ...

result = adapter.generate(request)
answer = validate_answer(result)
```

Focus on:

- `dataclass` for value objects;
- `Protocol` for structural interfaces;
- explicit exceptions at trust boundaries;
- immutable/frozen objects for stable request data;
- dependency injection for tests.

## C++ view

C++ makes ownership, value movement, and the adapter boundary more explicit. The compiler enforces more of the internal shape, but external model responses still require runtime parsing and validation.

```cpp
class ModelAdapter {
public:
    virtual ~ModelAdapter() = default;
    virtual ModelResult generate(const GenerationRequest& request) = 0;
};

const auto result = adapter.generate(request);
const auto answer = validate_answer(result);
```

Focus on:

- value types and `const` correctness;
- virtual interface ownership;
- exceptions versus an explicit result type;
- RAII for network/resources in real adapters;
- avoiding raw owning pointers.

## What the comparison teaches

| Concern | Python | C++ |
|---|---|---|
| Interface | Structural `Protocol` | Explicit abstract base class |
| Data shape | Type hints plus runtime checks | Compile-time structure plus runtime parsing |
| Ownership | Managed references/GC | Values, RAII, smart pointers |
| Errors | Exceptions are common | Exceptions or explicit result types |
| Ecosystem | Strong direct AI SDK support | Often HTTP/REST or community SDK integration |
| Typical role | AI orchestration and evaluation | Engines, native clients, performance-critical systems |

The security rule is identical: neither language's type system proves that model output is truthful or authorized.

## Provider integration boundary

When adding a live provider:

- keep credentials outside source control;
- translate the domain request inside one adapter;
- normalize finish reason, usage, errors, and tool events;
- record provider/model version;
- validate output after deserialization;
- place retry and timeout policy around the adapter;
- never embed authorization decisions in the prompt.

## Practice without busywork

Run both examples, then explain:

1. Which checks happen at compile time?
2. Which checks can only happen at runtime?
3. Where would HTTP and JSON parsing belong?
4. Where would retries be dangerous?
5. How would an actual database replace the in-memory idempotency set?
