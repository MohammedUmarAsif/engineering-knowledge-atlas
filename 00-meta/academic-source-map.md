# Academic Benchmarks and Source Map

## Purpose and limits

This map makes academic influence inspectable. It identifies what each external reference contributes, where that contribution appears, and what must **not** be inferred from it.

The atlas is independently maintained. Referencing a curriculum or course does not imply affiliation, endorsement, enrollment, completion, credit, or equivalence to a university programme. Course availability and syllabi can change; links below were checked on 2026-08-27.

## Durable curriculum and professional coverage

| Reference | What it contributes | How the atlas uses it | Important limit |
|---|---|---|---|
| [ACM/IEEE-CS/AAAI Computer Science Curricula 2023](https://csed.acm.org/final-report/) | Contemporary undergraduate CS knowledge areas and competency framing | Checks that pathways preserve durable systems, data, security, software and human-context foundations | The atlas does not reproduce a degree or force repetition of already-mastered BSc material |
| [IEEE SWEBOK v4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering) | Professional software-engineering knowledge areas | Informs requirements, design, construction, testing, operations, maintenance and engineering-management lenses | A body of knowledge is neither a production architecture nor a certification |
| Official specifications and standards | Normative behavior, shared terminology and governance expectations | Used for changing interfaces and assurance boundaries; versions and review dates are recorded | Conformance to one standard does not establish total correctness, security or compliance |

Existing undergraduate knowledge is tested through diagnostics. A reader who can explain the mechanism, assumptions, trade-offs and failure modes can skip forward; the source map is a coverage audit, not a command to start again from zero.

## Selected university references

### Harvard

| Reference | Atlas use | Boundary |
|---|---|---|
| [CS50's Introduction to Artificial Intelligence with Python](https://cs50.harvard.edu/ai/) | A clear baseline for search, knowledge, uncertainty, optimization, learning, neural networks and language; also a reference for approachable Python-first sequencing | Used as a diagnostic floor, not the depth ceiling. Production architecture, LLM application engineering, operations and research criticism require additional sources |

Harvard's influence is strongest where a hard concept needs a clean entry point before the atlas develops modern system and production consequences.

### MIT

| Reference | Atlas use | Boundary |
|---|---|---|
| [Computer Science and Engineering, Course 6-3](https://catalog.mit.edu/degree-charts/computer-science-engineering-course-6-3/) | A breadth check across algorithms, software, systems, computation structures, probability and AI choices | The atlas borrows the principle of connected breadth, not MIT degree requirements or assessment |
| [6.5840 Distributed Systems, Spring 2026](https://pdos.csail.mit.edu/6.5840/) | A graduate systems benchmark for replication, fault tolerance, consistency, concurrency and reasoning from papers and implementations | It informs the future full-stack/backend and AI system-design material; it is not summarized as a substitute for taking the subject |
| [6.S191 Introduction to Deep Learning](https://introtodeeplearning.com/) | A current implementation-oriented refresher connecting deep-learning mechanisms with active applications | It complements mathematical, systems and research sources; a short intensive course alone does not establish deep-learning mastery |

MIT's influence is used mainly to keep mechanisms, implementation and systems consequences connected.

### Oxford

The [Oxford Computer Science course catalogue for 2026–27](https://www.cs.ox.ac.uk/teaching/courses/2026-2027/) provides an advanced-subject benchmark. Particularly relevant references include:

- [Machine Learning](https://www.cs.ox.ac.uk/teaching/courses/2026-2027/ml);
- [Uncertainty in Deep Learning](https://www.cs.ox.ac.uk/teaching/courses/2026-2027/UDL);
- [Geometric Deep Learning](https://www.cs.ox.ac.uk/teaching/courses/2026-2027/geodl);
- [Databases](https://www.cs.ox.ac.uk/teaching/courses/2026-2027/databases);
- [Computer-Aided Formal Verification](https://www.cs.ox.ac.uk/teaching/courses/2026-2027/computeraidedverification);
- [Computer Security](https://www.cs.ox.ac.uk/teaching/courses/2026-2027/security); and
- [Advanced Security](https://www.cs.ox.ac.uk/teaching/courses/2026-2027/advsec).

These references help calibrate prerequisites, mathematical maturity, uncertainty, verification, security and research-facing depth. They are selected comparisons rather than a claim that the atlas covers Oxford's programmes or assessments.

## Depth interpretation

| Atlas depth | Expected evidence of understanding | Academic relationship |
|---|---|---|
| L0 Orientation | Locate the concept and its neighbors | Survey or prerequisite map |
| L1 Foundation | Explain the mechanism precisely | Durable undergraduate foundation |
| L2 Application | Connect components and implement a bounded example | Applied advanced-undergraduate work |
| L3 Production | Reason about failure, security, latency, cost and operation | Professional systems practice |
| L4 Senior | Defend architecture and organizational trade-offs under constraints | Integrative engineering judgment |
| L5 Research | Critique evidence, uncertainty, baselines, ablations, external validity and open questions | Research preparation and research-style reasoning |

The labels describe the demanded reasoning, not the reader's degree level. A topic may require an L5 critique while still relying on an L1 mechanism that needs repair.

## How a source becomes atlas material

1. Record the canonical source, type, license, redistribution status and check date.
2. Extract the durable concept separately from the current implementation or tool.
3. Compare independent evidence where a claim is empirical or contested.
4. State prerequisites and construct a diagnostic before adding a reading sequence.
5. Explain mechanism, trade-offs, failure modes and production consequences.
6. Add research questions only when the uncertainty is real and source-supported.
7. Recheck volatile claims and record the review in Git history.

The [source and copyright policy](source-and-copyright-policy.md) controls what may be stored locally. The [teaching and depth standard](teaching-and-depth-standard.md) controls how a source is transformed into instruction.
