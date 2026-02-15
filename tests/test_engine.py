import unittest

from optcg_advisor.engine import suggest_best_action
from optcg_advisor.models import BoardState, Character, Leader


class EngineTests(unittest.TestCase):
    def test_prefers_clearing_character_when_possible(self) -> None:
        state = BoardState(
            my_leader=Leader(name="Luffy", power=5000),
            my_characters=[Character(name="Zoro", power=6000, rested=False)],
            opp_leader=Leader(name="Kid", power=5000),
            opp_characters=[Character(name="Blocker", power=5000, rested=False)],
            don_available=0,
        )

        action = suggest_best_action(state)

        self.assertEqual(action.type, "attack_character")
        self.assertEqual(action.target, "Blocker")

    def test_passes_when_no_active_characters(self) -> None:
        state = BoardState(
            my_leader=Leader(name="Luffy", power=5000),
            my_characters=[Character(name="Zoro", power=6000, rested=True)],
            opp_leader=Leader(name="Kid", power=5000),
            opp_characters=[],
            don_available=0,
        )

        action = suggest_best_action(state)

        self.assertEqual(action.type, "pass")


if __name__ == "__main__":
    unittest.main()
