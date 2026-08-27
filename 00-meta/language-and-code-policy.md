# Language and Code Policy

## Priorities

- **Python first:** immediate AI engineering, interview preparation, data, evaluation, automation, and research.
- **C++ first:** long-term game development, performance, systems, memory, engine architecture, and advanced programming concepts.

## Paired-example rule

When code materially improves understanding, provide:

1. a primary implementation in the pathway's main language;
2. a companion implementation in the other language when the pattern transfers cleanly;
3. an explanation of differences in ownership, typing, errors, concurrency, dependencies, and ergonomics.

Do not translate code mechanically. A Pythonic implementation and an idiomatic C++ implementation may have different shapes while preserving the same contract.

## Exceptions

Use only the necessary language when:

- an official SDK does not support the companion language well;
- browser code requires JavaScript/TypeScript;
- shaders require a shading language;
- engine scripting requires its native language;
- translating would hide the important concept behind setup noise.

In those cases, include a language-neutral sequence or interface and explain how Python or C++ would integrate at the boundary.

## Code standard

Examples should be:

- small enough to understand in one sitting;
- complete enough to run when labelled runnable;
- explicit about dependencies and language version;
- typed where practical;
- safe by default;
- accompanied by expected behavior and failure cases;
- separated from secrets, credentials, and live side effects;
- validated in automation when the required runtime is available.

## Learning comparison

Every paired example should call out at least one useful contrast:

- dynamic versus static typing;
- exceptions versus explicit result/error types;
- garbage collection versus ownership/lifetime;
- duck typing versus concepts/interfaces;
- async runtime versus threads/coroutines;
- package ecosystem and foreign-function boundaries.
