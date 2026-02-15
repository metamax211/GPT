from __future__ import annotations

from dataclasses import dataclass, field
from typing import List


@dataclass
class Character:
    name: str
    power: int
    rested: bool = False


@dataclass
class Leader:
    name: str
    power: int


@dataclass
class Action:
    type: str
    target: str
    expected_value: int
    reason: str


@dataclass
class BoardState:
    my_leader: Leader
    my_characters: List[Character] = field(default_factory=list)
    opp_leader: Leader = field(default_factory=lambda: Leader(name="Unknown", power=5000))
    opp_characters: List[Character] = field(default_factory=list)
    don_available: int = 0

    @classmethod
    def from_dict(cls, payload: dict) -> "BoardState":
        return cls(
            my_leader=Leader(**payload["my_leader"]),
            my_characters=[Character(**card) for card in payload.get("my_characters", [])],
            opp_leader=Leader(**payload["opp_leader"]),
            opp_characters=[Character(**card) for card in payload.get("opp_characters", [])],
            don_available=payload.get("don_available", 0),
        )
