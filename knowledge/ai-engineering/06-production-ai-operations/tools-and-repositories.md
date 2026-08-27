---
id: ai-production-tools-repositories
title: Production AI Operations Tool Map
level: L2-L5
status: maintained
last_reviewed: 2026-08-27
prerequisites: [ai-governance-security]
---

# Production AI Operations Tool Map

## Selection principle

Choose tools after defining the operating problem, ownership, failure model, and exit strategy. GitHub stars indicate adoption interest, not fitness, security, or manageable complexity.

## Reliability and telemetry

- [OpenTelemetry](https://github.com/open-telemetry/opentelemetry-collector): vendor-neutral collection and propagation for traces, metrics, and logs. GenAI conventions moved to a [dedicated development-status repository](https://github.com/open-telemetry/semantic-conventions-genai); pin versions rather than assuming draft names are stable.
- [Prometheus](https://github.com/prometheus/prometheus): metrics and alerting ecosystem. Excellent for bounded numeric dimensions; raw prompts do not belong in labels.
- [Grafana](https://github.com/grafana/grafana): dashboards and exploration across data sources. A dashboard is not an SLO or an on-call policy.
- [Langfuse](https://github.com/langfuse/langfuse), [Phoenix](https://github.com/Arize-ai/phoenix), and [MLflow](https://github.com/mlflow/mlflow): AI tracing/evaluation ecosystems with different deployment, storage, evaluator, and commercial boundaries. Compare using your trace schema and privacy policy.

## Gateways

- [LiteLLM](https://github.com/BerriAI/litellm): widely adopted multi-provider SDK/proxy with routing, accounting, and policy features. Its breadth is useful but creates a critical dependency; pin, test, and isolate provider-specific semantics.
- [Envoy AI Gateway](https://github.com/envoyproxy/ai-gateway): AI traffic management built around the Envoy/Gateway API ecosystem. Assess maturity and operational fit.
- Cloud/provider gateways can reduce ownership; verify portability, data processing, policy depth, and failure isolation.

## Serving

- [vLLM](https://github.com/vllm-project/vllm): high-throughput LLM inference with continuous batching and KV-cache-oriented serving. Benchmark the exact model/hardware/workload.
- [Hugging Face Text Generation Inference](https://github.com/huggingface/text-generation-inference): influential production server now explicitly in maintenance mode. Study its architecture and existing deployments, but prefer actively recommended engines such as vLLM or SGLang for a new platform unless requirements justify it.
- [llama.cpp](https://github.com/ggml-org/llama.cpp): native C/C++ inference across local hardware, valuable for game/native and edge experimentation.
- [KServe](https://github.com/kserve/kserve): CNCF-incubating Kubernetes inference platform with routing, autoscaling, canary, and multiple runtimes. It is platform infrastructure, not a first deployment requirement.
- [Ray Serve](https://github.com/ray-project/ray): distributed Python serving and composition, including LLM deployments. Understand cluster startup, object/state, and failure semantics.
- [BentoML](https://github.com/bentoml/BentoML): packaging and serving ecosystem for AI applications and inference.

## Queues and workflows

- [Temporal](https://github.com/temporalio/temporal): durable workflow execution with retries, timers, and recovery semantics.
- [Kafka](https://github.com/apache/kafka), [RabbitMQ](https://github.com/rabbitmq/rabbitmq-server), and cloud queues: different ordering, retention, throughput, and operational models. “We need a queue” does not select one.
- [KEDA](https://github.com/kedacore/keda): event-driven Kubernetes autoscaling using external workload signals.

## Delivery and policy

- [Kubernetes](https://github.com/kubernetes/kubernetes): orchestration platform. Adopt when organizational scale justifies operating it, not because AI uses GPUs.
- [Argo CD](https://github.com/argoproj/argo-cd) and [Argo Rollouts](https://github.com/argoproj/argo-rollouts): GitOps delivery and progressive rollout patterns.
- [Open Policy Agent](https://github.com/open-policy-agent/opa): policy-as-code for deterministic authorization/validation decisions.
- [Sigstore](https://github.com/sigstore/cosign): artifact signing and verification in software supply chains.

## Standards and guidance

- [Google SRE resources](https://sre.google/): SLIs/SLOs, error budgets, incident response, capacity, and toil.
- [NIST AI RMF GenAI Profile](https://doi.org/10.6028/NIST.AI.600-1): risk-management guidance across the AI lifecycle.
- [OWASP GenAI Security](https://genai.owasp.org/): current threat and mitigation guidance.
- [OpenTelemetry semantic conventions](https://opentelemetry.io/docs/specs/semconv/): versioned telemetry meanings; verify stability status by domain.

## Repository review checklist

Inspect releases, license, security policy, governance, dependency and image provenance, upgrade path, conformance tests, failure semantics, observability, benchmarks, production adopters, and operational burden. Then run a failure-oriented proof of concept, not only a happy-path quickstart.
