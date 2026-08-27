"""Small retrieval mechanics demo. Python 3.12+, standard library only."""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from math import sqrt


@dataclass(frozen=True)
class Document:
    id: str
    tenant: str
    text: str
    embedding: tuple[float, ...]


def tokenize(text: str) -> list[str]:
    return [token.strip(".,:;!?()[]").lower() for token in text.split() if token]


def build_inverted_index(documents: list[Document]) -> dict[str, set[str]]:
    postings: dict[str, set[str]] = defaultdict(set)
    for document in documents:
        for term in set(tokenize(document.text)):
            postings[term].add(document.id)
    return dict(postings)


def lexical_search(
    query: str,
    documents: list[Document],
    postings: dict[str, set[str]],
    tenant: str,
) -> list[tuple[str, float]]:
    allowed = {document.id for document in documents if document.tenant == tenant}
    scores: dict[str, float] = defaultdict(float)
    for term in tokenize(query):
        for document_id in postings.get(term, set()) & allowed:
            scores[document_id] += 1.0
    return sorted(scores.items(), key=lambda item: (-item[1], item[0]))


def cosine(left: tuple[float, ...], right: tuple[float, ...]) -> float:
    if len(left) != len(right):
        raise ValueError("vector dimensions differ")
    dot = sum(a * b for a, b in zip(left, right, strict=True))
    left_norm = sqrt(sum(value * value for value in left))
    right_norm = sqrt(sum(value * value for value in right))
    if left_norm == 0.0 or right_norm == 0.0:
        raise ValueError("cosine similarity is undefined for a zero vector")
    return dot / (left_norm * right_norm)


def dense_search(
    query_embedding: tuple[float, ...],
    documents: list[Document],
    tenant: str,
) -> list[tuple[str, float]]:
    scored = [
        (document.id, cosine(query_embedding, document.embedding))
        for document in documents
        if document.tenant == tenant
    ]
    return sorted(scored, key=lambda item: (-item[1], item[0]))


def reciprocal_rank_fusion(
    rankings: list[list[tuple[str, float]]], constant: int = 60
) -> list[tuple[str, float]]:
    fused: dict[str, float] = defaultdict(float)
    for ranking in rankings:
        for rank, (document_id, _) in enumerate(ranking, start=1):
            fused[document_id] += 1.0 / (constant + rank)
    return sorted(fused.items(), key=lambda item: (-item[1], item[0]))


def main() -> None:
    documents = [
        Document("d1", "tenant-a", "Refund requests must be idempotent", (0.9, 0.2)),
        Document("d2", "tenant-a", "Timeouts need reconciliation before retry", (0.8, 0.5)),
        Document("d3", "tenant-b", "Private refund escalation policy", (1.0, 0.1)),
    ]
    postings = build_inverted_index(documents)
    lexical = lexical_search("refund timeout", documents, postings, "tenant-a")
    dense = dense_search((0.85, 0.35), documents, "tenant-a")
    fused = reciprocal_rank_fusion([lexical, dense])

    print("lexical", lexical)
    print("dense", dense)
    print("fused", fused)


if __name__ == "__main__":
    main()
