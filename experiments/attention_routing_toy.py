"""Toy attention-routing calculation.

This script builds intuition for how attention weights mix value information.
It is not a real transformer model and does not inspect model activations.
"""

from __future__ import annotations

from math import exp


TOKENS = ["The", "cat", "sat", "because", "it", "was", "tired", "."]
FEATURES = ["animal", "action", "state", "syntax"]

# Hand-written toy value vectors. These labels are for the toy calculation only.
VALUE_VECTORS = {
    "The": {"animal": 0.0, "action": 0.0, "state": 0.0, "syntax": 0.2},
    "cat": {"animal": 1.0, "action": 0.0, "state": 0.0, "syntax": 0.1},
    "sat": {"animal": 0.0, "action": 0.8, "state": 0.0, "syntax": 0.1},
    "because": {"animal": 0.0, "action": 0.0, "state": 0.0, "syntax": 0.8},
    "it": {"animal": 0.2, "action": 0.0, "state": 0.0, "syntax": 0.1},
    "was": {"animal": 0.0, "action": 0.1, "state": 0.1, "syntax": 0.5},
    "tired": {"animal": 0.0, "action": 0.0, "state": 1.0, "syntax": 0.1},
    ".": {"animal": 0.0, "action": 0.0, "state": 0.0, "syntax": 0.6},
}


def softmax(scores: list[float]) -> list[float]:
    max_score = max(scores)
    exponentials = [exp(score - max_score) for score in scores]
    total = sum(exponentials)
    return [value / total for value in exponentials]


def weighted_update(weights: list[float]) -> dict[str, float]:
    update = {}

    for feature in FEATURES:
        update[feature] = sum(
            weight * VALUE_VECTORS[token][feature]
            for token, weight in zip(TOKENS, weights, strict=True)
        )

    return update


def print_case(name: str, scores: list[float]) -> None:
    weights = softmax(scores)
    update = weighted_update(weights)
    ranked_weights = sorted(
        zip(TOKENS, weights, strict=True),
        key=lambda item: item[1],
        reverse=True,
    )

    print(name)
    print("=" * len(name))
    print("Top attention weights:")
    for token, weight in ranked_weights[:4]:
        print(f"- {token}: {weight:.3f}")

    print()
    print("Weighted value update:")
    for feature, value in update.items():
        print(f"- {feature}: {value:.3f}")
    print()


def main() -> None:
    print("Toy sentence: The cat sat because it was tired.")
    print("Destination token: it")
    print()
    print("Note: value-vector labels are hand-written for this toy example.")
    print("They are not evidence about a trained model.")
    print()

    print_case(
        "Case 1: focused attention toward cat",
        [0.1, 2.6, 0.2, 0.1, 0.0, 0.0, 0.3, 0.0],
    )
    print_case(
        "Case 2: mixed attention toward cat and tired",
        [0.1, 2.2, 0.2, 0.1, 0.0, 0.0, 2.0, 0.0],
    )

    print("Observation")
    print("===========")
    print("The attention weights show where value information is read from.")
    print("The weighted update shows one simple way that information can mix.")
    print("The weights alone do not prove what information was moved or used later.")


if __name__ == "__main__":
    main()
