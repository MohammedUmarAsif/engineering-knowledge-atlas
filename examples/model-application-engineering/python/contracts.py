"""Provider-neutral model and tool contracts. Python 3.12+, standard library only."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True)
class GenerationRequest:
    task: str
    user_input: str
    tenant_id: str


@dataclass(frozen=True)
class ModelResult:
    text: str
    model: str
    finish_reason: str


class ModelAdapter(Protocol):
    def generate(self, request: GenerationRequest) -> ModelResult: ...


class FakeModelAdapter:
    """Deterministic adapter used for architecture tests."""

    def generate(self, request: GenerationRequest) -> ModelResult:
        return ModelResult(
            text=f"Summary: {request.user_input.strip()}",
            model="fake-model-v1",
            finish_reason="stop",
        )


def validate_answer(result: ModelResult) -> str:
    """Validate application invariants, not merely response syntax."""
    if result.finish_reason != "stop":
        raise ValueError(f"incomplete generation: {result.finish_reason}")
    answer = result.text.strip()
    if not answer.startswith("Summary:"):
        raise ValueError("result violates the domain response contract")
    if len(answer) > 500:
        raise ValueError("result exceeds the product limit")
    return answer


@dataclass(frozen=True)
class ToolProposal:
    name: str
    order_id: str
    idempotency_key: str


class RefundExecutor:
    """Demonstrates authorization and deduplication outside the model."""

    def __init__(self) -> None:
        self._completed: set[str] = set()

    def execute(
        self,
        proposal: ToolProposal,
        *,
        authenticated_tenant: str,
        order_tenant: str,
        approved: bool,
    ) -> str:
        if proposal.name != "refund_order":
            raise ValueError("unsupported tool")
        if authenticated_tenant != order_tenant:
            raise PermissionError("cross-tenant access denied")
        if not approved:
            raise PermissionError("refund requires approval")
        if proposal.idempotency_key in self._completed:
            return "already_completed"

        # A real implementation would use a database transaction and a unique key.
        self._completed.add(proposal.idempotency_key)
        return f"refunded:{proposal.order_id}"


def main() -> None:
    adapter: ModelAdapter = FakeModelAdapter()
    request = GenerationRequest(
        task="summarize",
        user_input="A model proposal is not authorization.",
        tenant_id="tenant-a",
    )
    print(validate_answer(adapter.generate(request)))

    executor = RefundExecutor()
    proposal = ToolProposal("refund_order", "order-42", "refund-order-42-v1")
    print(
        executor.execute(
            proposal,
            authenticated_tenant="tenant-a",
            order_tenant="tenant-a",
            approved=True,
        )
    )
    print(
        executor.execute(
            proposal,
            authenticated_tenant="tenant-a",
            order_tenant="tenant-a",
            approved=True,
        )
    )


if __name__ == "__main__":
    main()
