---
id: ai-serving-capacity
title: Inference Serving, Capacity, and Performance
level: L3-L5
status: maintained
last_reviewed: 2026-08-27
prerequisites: [ai-gateway-routing, inference-and-generation]
---

# Inference Serving, Capacity, and Performance

## Latency is a timeline

For streaming generation:

```text
arrival → admission → queue → prefill → first token → decode tokens → validation → done
```

- Queue time measures capacity pressure.
- Time to first token (TTFT) includes queue and prefill from the user’s perspective.
- Inter-token latency or time per output token affects stream smoothness.
- End-to-end latency includes every application stage.

A single “model latency” average hides the mechanism.

## Prefill and decode

Prefill processes input tokens and can exploit parallel matrix operations. Decode produces tokens sequentially, repeatedly reading model weights and KV-cache state. Long inputs stress prefill and memory; long outputs occupy decode capacity and concurrency slots.

This is why tokens per second, concurrent sequences, TTFT, and queue depth matter alongside GPU utilization.

## Batching

Batching shares expensive model execution across requests and raises throughput. Waiting to form a batch adds latency. Continuous batching admits and removes sequences over time, improving utilization for requests of different lengths.

Larger batches are not universally better: memory limits, tail latency, fairness, and long-sequence interference constrain them.

## KV cache

Attention keys and values from processed tokens are cached so decoding does not recompute the entire prefix. The KV cache grows with sequence length, layers, hidden dimensions, precision, and concurrency. It can dominate serving memory even when model weights fit.

Prefix caching reuses common prefixes, but hit rate depends on exact or implementation-defined matching and stable prompt prefixes. Place invariant instructions early when consistent with semantics; measure real hits rather than assuming savings.

## Parallelism

- Tensor parallelism partitions operations across devices and pays communication each layer.
- Pipeline parallelism assigns layer stages and can create pipeline bubbles.
- Data parallelism replicates models for independent traffic.
- Expert parallelism distributes mixture-of-experts components.

The right topology depends on model size, interconnect, request shape, and availability goals. More GPUs can reduce capacity when communication dominates.

## Quantization

Lower-precision weights reduce memory and may increase throughput. Quality and kernel support vary by model, hardware, method, and workload. Evaluate system tasks, especially tool arguments, multilingual text, long context, and safety—not perplexity alone.

## Autoscaling

CPU utilization is often a poor leading signal for GPU inference. Useful signals include queue depth, waiting tokens, active sequences, request concurrency, cache pressure, and deadline risk.

Autoscaling reacts after measurement and provisioning delay. GPU nodes, model downloads, compilation, memory profiling, and warmup can take far longer than ordinary web pods. Maintain warm capacity for interactive SLOs, forecast known peaks, and bound the queue.

Kubernetes HPA can use custom and external metrics, but the metric must decrease as replicas add useful capacity. Stabilization and readiness matter; scaling rapidly on noisy queue signals can oscillate.

## Capacity model

Little’s Law gives a first approximation for a stable system:

```text
concurrency ≈ arrival_rate × average_time_in_system
```

It does not capture heavy tails, variable token lengths, batching, priority, or saturation, but it catches impossible plans. At 20 requests/second and five-second mean time, roughly 100 requests are in flight on average.

## Benchmark correctly

Specify input/output length distributions, concurrency, arrival pattern, model revision, quantization, hardware, engine version, warmup, sampling, and SLO. Report TTFT and end-to-end percentiles, throughput, errors, power/cost, and quality.

Offline maximum tokens/second is not interactive capacity if TTFT violates the product objective.

## Admission control

Reject or defer work before memory exhaustion. Estimate cost from input length, requested output, tool path, and priority. Enforce maximums below the model. Load shedding is a reliability feature: a clear refusal preserves capacity for work the system can complete.

## Managed versus self-hosted

Managed APIs reduce infrastructure burden and can provide strong model access and elasticity. Self-hosting offers control over model, data path, hardware, and unit economics at sufficient scale—but transfers capacity, security, upgrades, and on-call ownership to your team.

Compare total cost and operational capability, not GPU rental versus token price alone.
