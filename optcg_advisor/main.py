from __future__ import annotations

import argparse
import json

from .engine import suggest_best_action
from .models import BoardState


def main() -> None:
    parser = argparse.ArgumentParser(description="OPTCG move advisor (MVP)")
    parser.add_argument("state_file", help="Path to a JSON board-state file")
    args = parser.parse_args()

    with open(args.state_file, "r", encoding="utf-8") as f:
        payload = json.load(f)

    state = BoardState.from_dict(payload)
    recommendation = suggest_best_action(state)

    print("Recommended action:")
    print(f"- type: {recommendation.type}")
    print(f"- target: {recommendation.target}")
    print(f"- score: {recommendation.expected_value}")
    print(f"- reason: {recommendation.reason}")


if __name__ == "__main__":
    main()
