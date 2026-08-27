"""A dependency-free, bounded agent runtime with visible safety contracts."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Callable


class RunStatus(str, Enum):
    RUNNING = "running"
    WAITING_APPROVAL = "waiting_approval"
    COMPLETED = "completed"
    FAILED = "failed"
    BUDGET_EXHAUSTED = "budget_exhausted"


@dataclass(frozen=True)
class Proposal:
    tool: str
    arguments: dict[str, str]
    idempotency_key: str


@dataclass(frozen=True)
class ToolSpec:
    name: str
    required_arguments: frozenset[str]
    writes: bool
    execute: Callable[[dict[str, str]], str]


@dataclass
class RunState:
    goal: str
    steps_left: int
    status: RunStatus = RunStatus.RUNNING
    observations: list[str] = field(default_factory=list)
    completed_keys: set[str] = field(default_factory=set)
    pending: Proposal | None = None


class Runtime:
    def __init__(self, tools: list[ToolSpec]) -> None:
        self.tools = {tool.name: tool for tool in tools}

    def apply(self, state: RunState, proposal: Proposal, approved: bool = False) -> None:
        if state.status not in {RunStatus.RUNNING, RunStatus.WAITING_APPROVAL}:
            raise RuntimeError(f"run is terminal: {state.status}")
        if state.steps_left <= 0:
            state.status = RunStatus.BUDGET_EXHAUSTED
            return

        tool = self.tools.get(proposal.tool)
        if tool is None:
            self._fail(state, f"unknown tool: {proposal.tool}")
            return

        missing = tool.required_arguments - proposal.arguments.keys()
        if missing:
            self._fail(state, f"missing arguments: {sorted(missing)}")
            return

        if proposal.idempotency_key in state.completed_keys:
            state.observations.append("duplicate logical operation ignored")
            state.status = RunStatus.RUNNING
            state.pending = None
            return

        if tool.writes and not approved:
            state.status = RunStatus.WAITING_APPROVAL
            state.pending = proposal
            return

        state.steps_left -= 1
        try:
            result = tool.execute(proposal.arguments)
        except Exception as exc:  # A real runtime uses a typed error taxonomy.
            self._fail(state, f"tool error: {type(exc).__name__}: {exc}")
            return

        state.completed_keys.add(proposal.idempotency_key)
        state.observations.append(f"{tool.name}: {result}")
        state.pending = None
        state.status = RunStatus.RUNNING

    @staticmethod
    def complete(state: RunState, verifier: Callable[[RunState], bool]) -> None:
        state.status = RunStatus.COMPLETED if verifier(state) else RunStatus.FAILED

    @staticmethod
    def _fail(state: RunState, message: str) -> None:
        state.observations.append(message)
        state.pending = None
        state.status = RunStatus.FAILED


def read_lore(arguments: dict[str, str]) -> str:
    return f"canon[{arguments['entry_id']}] = The bridge opens at dawn"


def record_note(arguments: dict[str, str]) -> str:
    return f"stored note: {arguments['text']}"


def main() -> None:
    runtime = Runtime([
        ToolSpec("read_lore", frozenset({"entry_id"}), False, read_lore),
        ToolSpec("record_note", frozenset({"text"}), True, record_note),
    ])
    state = RunState(goal="read canon and record a verified note", steps_left=3)

    runtime.apply(state, Proposal("read_lore", {"entry_id": "bridge"}, "read-bridge-1"))
    write = Proposal("record_note", {"text": "The bridge opens at dawn"}, "note-bridge-1")
    runtime.apply(state, write)
    assert state.status is RunStatus.WAITING_APPROVAL

    runtime.apply(state, state.pending, approved=True)  # type: ignore[arg-type]
    runtime.apply(state, write, approved=True)  # Duplicate is safely ignored.
    runtime.complete(state, lambda run: any("stored note" in item for item in run.observations))

    print(state.status.value)
    for observation in state.observations:
        print(f"- {observation}")


if __name__ == "__main__":
    main()
