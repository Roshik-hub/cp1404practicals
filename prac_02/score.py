"""
CP1404- Practical
Refactored: Determine score status using functions
"""

import random

def main():
    score = float(input("Enter score: "))
    result = determine_score_result(score)
    print(result)

    # Generate random score and show result
    random_score = random.uniform(0, 100)
    print(f"\nRandom score: {random_score:.2f}")
    print(determine_score_result(random_score))


def determine_score_result(score):
    """Determine the status/result based on the score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
