---
id: ai-queues-backpressure
title: Queues, Backpressure, and Durable Work
level: L3-L5
status: maintained
last_reviewed: 2026-08-27
prerequisites: [ai-serving-capacity, agent-loop-state]
---

# Queues, Backpressure, and Durable Work

## A queue changes the product contract

Moving work to a queue does not make it faster. It converts immediate completion into accepted work that may finish later. The user needs a job ID, visible state, cancellation, result retention, and failure semantics.

Use synchronous handling when the work fits a firm interactive deadline. Use queued jobs for expensive, bursty, retryable, or batch work. Use a durable workflow when work spans multiple stateful steps, timers, approvals, or compensations.

## Backpressure

Backpressure tells producers that consumers cannot keep up. Without it, queues grow until deadlines expire, memory fills, or cost becomes unbounded.

Controls include:

- Bounded queue size.
- Admission rejection.
- Per-tenant quotas.
- Producer rate limits.
- Consumer concurrency limits.
- Priority classes.
- Deadline-aware dropping.
- Dynamic degradation.

An unbounded queue is delayed failure.

## Delivery semantics

Most practical brokers provide at-least-once delivery: a message may be processed more than once. Design handlers to be idempotent using stable logical operation IDs and a durable result/deduplication record.

At-most-once can lose work. “Exactly once” is scoped and usually constructed through transactions or deduplication; confirm which boundary the guarantee covers.

## Retry policy

Retry only errors likely to change with time. Use exponential backoff with jitter to avoid synchronized clients. Bound attempts, elapsed time, and total retry traffic.

A retry budget caps retries as a fraction of normal traffic. Without it, one dependency failure multiplies load and delays recovery.

Permanent failures move to a terminal state or dead-letter process with ownership. A dead-letter queue without alerting and replay policy is a graveyard.

## Deadlines and stale work

Carry enqueue time and deadline. A request that waited ten minutes should not spend expensive GPU time generating an answer whose user already left. Expiration is different from cancellation: both need explicit states and cleanup.

## Ordering

Global ordering destroys parallelism. Request the smallest necessary ordering key, such as per conversation or document. Even ordered delivery does not prevent concurrent external mutations unless consumers coordinate state versions.

## Queue metrics

Measure:

- Arrival and completion rates.
- Queue depth and age of oldest item.
- Wait-time percentiles.
- Processing time and attempts.
- Expired, cancelled, failed, and dead-lettered jobs.
- Cost and success by priority/tenant.

Queue depth alone is ambiguous: 1,000 tiny jobs and 1,000 long-context generations are different workloads.

## Game example

Generate optional player recaps or localization suggestions asynchronously. Keep combat, movement, and authoritative economy synchronous and deterministic. If generation falls behind, drop stale cosmetic work before critical live-service operations.

## Design scenario

Traffic spikes tenfold after a launch. Decide which requests receive immediate capacity, which wait, which degrade, and which reject. Then explain how a user distinguishes “accepted,” “running,” “waiting for approval,” “failed,” and “completed.”
