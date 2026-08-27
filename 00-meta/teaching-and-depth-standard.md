# Teaching and Depth Standard

## Goal

Every page should leave the reader with a usable mental model, not merely exposure to terminology. Concision means removing low-value words—not removing causal explanation.

## The explanation ladder

Teach important concepts in this order:

1. **Concrete intuition:** a physical, visual, product, or game example.
2. **Precise model:** correct the simplifications required by the intuition.
3. **Mechanism:** follow the data, control, memory, or decision path step by step.
4. **Why it exists:** identify the earlier limitation or failure that created the need.
5. **Where it appears:** AI, full stack, games, research, and infrastructure.
6. **Choice:** compare alternatives and state when not to use it.
7. **Failure:** show common production and conceptual mistakes.
8. **Modern form:** current standards, tools, and active research.
9. **Transfer:** connect it explicitly to earlier and later modules.

## Intuition must graduate into precision

Useful simplifications must be labelled and then refined.

Examples:

- A bit can be introduced as two distinguishable states, often written `0` and `1`; physical implementations use voltage ranges and tolerate noise rather than requiring a perfect literal switch.
- Eight bits form a byte on modern general-purpose systems, but a byte is a unit of addressable storage—not a universal guarantee about every data type.
- A C++ `int` is commonly four bytes, but the language standard does not require one universal size. Use `sizeof` or fixed-width integer types when representation matters.
- A pointer stores an address. It enables indirection and efficient access patterns but also adds lifetime, ownership, locality, and safety concerns. It is not inherently a memory optimization.
- A hash table gives expected constant-time lookup under suitable assumptions, but arrays, sorted vectors, trees, sparse sets, component storage, or databases can be better for cache locality, ordering, range queries, persistence, or scale.

The atlas must never trade correctness for a memorable sentence.

## Cross-domain transfer

Where true and useful, every foundational page should include:

- **AI application:** how the concept affects models, retrieval, agents, or evaluation;
- **full stack:** how it appears in web services, databases, APIs, cloud, or operations;
- **games:** how it affects engines, entities, assets, networking, performance, design, or Game AI;
- **research:** what assumptions remain open, contested, or experimentally testable.

Do not force irrelevant connections.

## Tool treatment

Tools are taught as implementations of concepts:

1. problem before tool;
2. durable concept;
3. tool architecture;
4. strengths and limits;
5. failure and operational model;
6. alternatives;
7. maintenance, license, and ecosystem signals;
8. current official documentation.

Git, containers, Docker, CI/CD, cloud platforms, observability, and security are not vocabulary lists. Their interactions should be traced through one delivery lifecycle: source → review → build → test → artifact → deploy → observe → recover.

## Repository selection

GitHub popularity is a discovery signal, not proof of correctness. Before recommending a repository, record:

- official or community status;
- license;
- current stars as a dated snapshot when useful;
- release/commit activity;
- maintainer and contributor health;
- documentation quality;
- security posture;
- production adoption evidence;
- overlap and alternatives;
- exact role in this curriculum.

Prefer a small, annotated shortlist over a giant “awesome” list.

## Research treatment

Separate:

- established result;
- recent peer-reviewed result;
- preprint;
- implementation report;
- benchmark claim;
- repository marketing claim;
- this atlas's inference.

For a research frontier, state what is known, what remains uncertain, what evidence would resolve it, and why the question matters for products or a potential PhD.

## Engagement devices

Use only devices that improve understanding:

- “follow one request” traces;
- game and product scenarios;
- prediction questions before an explanation;
- misconceptions and corrections;
- incident reconstructions;
- decision tables;
- diagrams;
- paired Python/C++ examples;
- interview answers at 30-second, 3-minute, and design-review depth;
- research questions worth pursuing.
