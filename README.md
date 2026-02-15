# OPTCG Move Advisor (Starter)

This repository now contains a minimal Python starter app that can recommend a single tactical action from a simplified OPTCG board state.

## Why this is useful
- Gives you a baseline rules engine you can improve incrementally.
- Lets you test recommendation logic against deterministic board snapshots.
- Sets you up to integrate with OPTCG sim data capture later.

## Current project layout
- `optcg_advisor/models.py`: board-state and action data models.
- `optcg_advisor/engine.py`: simple heuristic recommender.
- `optcg_advisor/main.py`: CLI entrypoint.
- `examples/sample_state.json`: sample input.
- `tests/test_engine.py`: unit tests.

## Quick start
```bash
python -m unittest discover -s tests
python -m optcg_advisor.main examples/sample_state.json
```

## Suggested next steps for a real assistant
1. Expand state representation (leader effects, DON!! attachments, counters in hand, blockers, events).
2. Enumerate legal actions per phase instead of one-step heuristics.
3. Add a search strategy (beam search / minimax with stochastic counter model).
4. Build an adapter for OPTCG sim logs/snapshots to auto-generate board states.
5. Add evaluation metrics: win probability estimate + confidence.

If you want, next I can implement **phase-aware legal move generation** and a **multi-action turn planner**.
