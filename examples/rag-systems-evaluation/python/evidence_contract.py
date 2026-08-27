"""Minimal evidence/citation contract. Python 3.12+, standard library only."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Evidence:
    id: str
    source: str
    text: str


@dataclass(frozen=True)
class Claim:
    text: str
    evidence_ids: tuple[str, ...]


def terms(text: str) -> set[str]:
    return {word.strip(".,:;!?()[]").lower() for word in text.split() if len(word) > 3}


def validate_claim(claim: Claim, evidence: list[Evidence]) -> None:
    by_id = {item.id: item for item in evidence}
    if not claim.evidence_ids:
        raise ValueError("factual claim has no evidence")
    missing = set(claim.evidence_ids) - by_id.keys()
    if missing:
        raise ValueError(f"unknown evidence ids: {sorted(missing)}")
    support_text = " ".join(by_id[item_id].text for item_id in claim.evidence_ids)
    if len(terms(claim.text) & terms(support_text)) < 2:
        raise ValueError("claim lacks minimal lexical support")


def render(claim: Claim, evidence: list[Evidence]) -> str:
    validate_claim(claim, evidence)
    by_id = {item.id: item for item in evidence}
    citations = ", ".join(by_id[item_id].source for item_id in claim.evidence_ids)
    return f"{claim.text} [{citations}]"


def main() -> None:
    evidence = [Evidence("e1", "Policy p.4", "Refunds require manager approval.")]
    claim = Claim("A refund requires manager approval.", ("e1",))
    print(render(claim, evidence))


if __name__ == "__main__":
    main()
