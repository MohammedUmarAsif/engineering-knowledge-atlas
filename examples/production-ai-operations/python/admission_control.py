"""Dependency-free admission control for bounded AI inference capacity."""

from __future__ import annotations

from contextlib import AbstractContextManager
from dataclasses import dataclass
from enum import Enum
from threading import Lock
from time import monotonic


class Rejection(str, Enum):
    EXPIRED = "expired"
    TOO_LARGE = "too_large"
    TENANT_BUSY = "tenant_busy"
    OVERLOADED = "overloaded"


@dataclass(frozen=True)
class Request:
    tenant: str
    input_tokens: int
    max_output_tokens: int
    deadline: float


@dataclass(frozen=True)
class Decision:
    lease: Lease | None = None
    rejection: Rejection | None = None

    @property
    def accepted(self) -> bool:
        return self.lease is not None


class Lease(AbstractContextManager["Lease"]):
    def __init__(self, controller: AdmissionController, tenant: str) -> None:
        self._controller = controller
        self._tenant = tenant
        self._released = False

    def release(self) -> None:
        if not self._released:
            self._controller._release(self._tenant)
            self._released = True

    def __exit__(self, *args: object) -> None:
        self.release()


class AdmissionController:
    def __init__(self, global_limit: int, tenant_limit: int, token_limit: int) -> None:
        if min(global_limit, tenant_limit, token_limit) <= 0:
            raise ValueError("limits must be positive")
        self.global_limit = global_limit
        self.tenant_limit = tenant_limit
        self.token_limit = token_limit
        self._global_in_flight = 0
        self._tenant_in_flight: dict[str, int] = {}
        self._lock = Lock()

    def admit(self, request: Request, now: float | None = None) -> Decision:
        current_time = monotonic() if now is None else now
        if request.deadline <= current_time:
            return Decision(rejection=Rejection.EXPIRED)
        if request.input_tokens + request.max_output_tokens > self.token_limit:
            return Decision(rejection=Rejection.TOO_LARGE)

        with self._lock:
            tenant_count = self._tenant_in_flight.get(request.tenant, 0)
            if tenant_count >= self.tenant_limit:
                return Decision(rejection=Rejection.TENANT_BUSY)
            if self._global_in_flight >= self.global_limit:
                return Decision(rejection=Rejection.OVERLOADED)
            self._global_in_flight += 1
            self._tenant_in_flight[request.tenant] = tenant_count + 1
            return Decision(lease=Lease(self, request.tenant))

    def _release(self, tenant: str) -> None:
        with self._lock:
            count = self._tenant_in_flight[tenant]
            if count == 1:
                del self._tenant_in_flight[tenant]
            else:
                self._tenant_in_flight[tenant] = count - 1
            self._global_in_flight -= 1


def main() -> None:
    controller = AdmissionController(global_limit=2, tenant_limit=1, token_limit=4_096)
    now = monotonic()
    first = controller.admit(Request("studio-a", 800, 500, now + 2), now)
    assert first.accepted and first.lease

    blocked = controller.admit(Request("studio-a", 200, 100, now + 2), now)
    print(f"second request: {blocked.rejection.value}")  # type: ignore[union-attr]

    with first.lease:
        print("first request: accepted")

    retried = controller.admit(Request("studio-a", 200, 100, now + 2), now)
    assert retried.lease
    with retried.lease:
        print("retry after release: accepted")


if __name__ == "__main__":
    main()
