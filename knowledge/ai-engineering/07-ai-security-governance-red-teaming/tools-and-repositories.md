---
id: ai-security-tools-repositories
title: AI Security and Assurance Tool Map
level: L2-L5
status: maintained
last_reviewed: 2026-08-27
prerequisites: [ai-security-detection-response]
---

# AI Security and Assurance Tool Map

## Use tools to test hypotheses

No scanner establishes that an AI system is secure. Select tools based on threat model, interface, reproducibility, evaluator trust, deployment constraints, and remediation workflow.

## Knowledge bases and standards

- [MITRE ATLAS](https://atlas.mitre.org/): living tactics, techniques, mitigations, and case studies across predictive, generative, and agentic AI. Map credible adversary paths; do not chase every technique equally.
- [OWASP GenAI Top 10 2026](https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/): current application-risk categories and mitigations.
- [OWASP Agentic Top 10 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/): agent-focused risks.
- [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework) and [NIST AI 100-2e2025](https://doi.org/10.6028/NIST.AI.100-2e2025): risk process plus adversarial ML terminology.
- [ISO/IEC 42001](https://www.iso.org/standard/42001): official standard page for AI management systems; normative text is copyrighted.

## Evaluation and red teaming

- [Promptfoo](https://github.com/promptfoo/promptfoo): configurable prompt/application evaluation and red-team workflows. Review generated probes, data handling, evaluator dependence, and CI thresholds.
- [Garak](https://github.com/NVIDIA/garak): LLM vulnerability scanner with probe/detector architecture. Results identify candidates for investigation, not automatic production severity.
- [Inspect AI](https://github.com/UKGovernmentBEIS/inspect_ai): evaluation framework supporting agents, tools, sandboxes, datasets, and scorers.
- [PyRIT](https://github.com/Azure/PyRIT): Microsoft-originated framework for generative-AI risk identification and red teaming. Use only against authorized targets and control sensitive result data.
- [Giskard](https://github.com/Giskard-AI/giskard): testing/evaluation capabilities across ML and LLM applications; assess open-source versus platform boundaries.

## Traditional application and supply-chain security

- [Semgrep](https://github.com/semgrep/semgrep), [CodeQL](https://github.com/github/codeql), and language-native analyzers: generated code still needs static analysis and review.
- [Trivy](https://github.com/aquasecurity/trivy): vulnerability and misconfiguration scanning for repositories, images, and infrastructure artifacts.
- [Syft](https://github.com/anchore/syft) and [Grype](https://github.com/anchore/grype): SBOM generation and vulnerability matching.
- [Sigstore Cosign](https://github.com/sigstore/cosign): signing and verification for supply-chain artifacts.
- [Open Policy Agent](https://github.com/open-policy-agent/opa): deterministic policy enforcement; keep policy inputs minimal, authoritative, and versioned.

## Isolation and runtime

- [Firecracker](https://github.com/firecracker-microvm/firecracker), [gVisor](https://github.com/google/gvisor), and container security controls provide different isolation/performance tradeoffs.
- [Falco](https://github.com/falcosecurity/falco): runtime detection for host/container activity; AI-specific semantic misuse still needs application signals.
- Egress proxies, secrets managers, identity platforms, and SIEM/SOAR remain core infrastructure even when they are not branded “AI security.”

## Repository review

Record official/community status, license, active maintenance, security policy, threat model, supported interfaces, evaluator/provider dependencies, telemetry and content retention, false-positive methodology, reproducibility, and how findings map to remediation.

## Safe lab rule

Run probes against local fixtures, synthetic tenants, mock tools, fake secrets, and isolated sandboxes. Explicitly authorize any shared or production-like environment. Rate-limit tests and define emergency stop.

## Selection exercise

For an agent using browser, email, and filesystem tools, begin with a threat model and effect-level invariant tests. Then choose one automated scanner for breadth, one evaluation framework for regression, ordinary code/supply-chain scanners, runtime isolation, and trace-based detection. Explain what each cannot see.
