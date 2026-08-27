"""Authorize model-proposed effects using explicit capabilities and approvals."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from hashlib import sha256


class Risk(str, Enum):
    LOW = "low"
    HIGH = "high"


class Denial(str, Enum):
    IDENTITY = "identity_mismatch"
    TENANT = "tenant_mismatch"
    SCOPE = "outside_capability"
    EXPIRED = "capability_expired"
    APPROVAL = "approval_missing_or_stale"


@dataclass(frozen=True)
class Effect:
    principal: str
    tenant: str
    tool: str
    target: str
    payload: str
    risk: Risk

    def binding(self) -> str:
        material = "\x1f".join(
            (self.principal, self.tenant, self.tool, self.target, self.payload, self.risk.value)
        )
        return sha256(material.encode()).hexdigest()


@dataclass(frozen=True)
class Capability:
    principal: str
    tenant: str
    tool: str
    target: str
    expires_at: int


@dataclass(frozen=True)
class Approval:
    action_binding: str


@dataclass(frozen=True)
class Decision:
    allowed: bool
    denial: Denial | None = None


def authorize(
    effect: Effect,
    capability: Capability,
    now: int,
    approval: Approval | None = None,
) -> Decision:
    if effect.principal != capability.principal:
        return Decision(False, Denial.IDENTITY)
    if effect.tenant != capability.tenant:
        return Decision(False, Denial.TENANT)
    if effect.tool != capability.tool or effect.target != capability.target:
        return Decision(False, Denial.SCOPE)
    if now >= capability.expires_at:
        return Decision(False, Denial.EXPIRED)
    if effect.risk is Risk.HIGH and (
        approval is None or approval.action_binding != effect.binding()
    ):
        return Decision(False, Denial.APPROVAL)
    return Decision(True)


def main() -> None:
    capability = Capability("user-7", "studio-a", "publish_note", "repo/game-docs", 200)
    proposed = Effect(
        "user-7", "studio-a", "publish_note", "repo/game-docs", "Review draft", Risk.HIGH
    )

    denied = authorize(proposed, capability, now=100)
    print(f"without approval: {denied.denial.value}")  # type: ignore[union-attr]

    approval = Approval(proposed.binding())
    print(f"exact approved effect: {authorize(proposed, capability, 100, approval).allowed}")

    changed = Effect(
        "user-7", "studio-a", "publish_note", "repo/game-docs", "Changed after review", Risk.HIGH
    )
    stale = authorize(changed, capability, 100, approval)
    print(f"changed payload: {stale.denial.value}")  # type: ignore[union-attr]


if __name__ == "__main__":
    main()
