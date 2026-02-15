from __future__ import annotations

from typing import List

from .models import Action, BoardState, Character


def _character_attack_value(attacker: Character, defenders: List[Character]) -> Action:
    beatable = [d for d in defenders if attacker.power >= d.power]
    if beatable:
        target = min(beatable, key=lambda d: d.power)
        value = 2 + max(0, (attacker.power - target.power) // 1000)
        return Action(
            type="attack_character",
            target=target.name,
            expected_value=value,
            reason=f"{attacker.name} can clear {target.name} and gain board control.",
        )

    return Action(
        type="attack_leader",
        target="opponent_leader",
        expected_value=1,
        reason=f"{attacker.name} cannot clear board, so pressure life.",
    )


def suggest_best_action(state: BoardState) -> Action:
    available_attackers = [c for c in state.my_characters if not c.rested]
    if not available_attackers:
        return Action(
            type="pass",
            target="none",
            expected_value=0,
            reason="No active attackers available.",
        )

    scored = [_character_attack_value(attacker, state.opp_characters) for attacker in available_attackers]
    return max(scored, key=lambda action: action.expected_value)
