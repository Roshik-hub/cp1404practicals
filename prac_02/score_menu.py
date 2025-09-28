"""
CP1404 - Practical
Menu-based program to work with a score
"""

def main():
    score = get_valid_score()

    MENU = "\n(G)et valid score\n(P)rint result\n(S)how stars\n(Q)uit"
    print(MENU)
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            result = determine_score_result(score)
            print(f"Result: {result}")
        elif choice == "S":
            print_stars(score)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()

    print("Farewell!")


def get_valid_score():
    """Prompt the user for a valid score between 0 and 100."""
    score = float(input("Enter a valid score (0-100): "))
    while score < 0 or score > 100:
        print("Invalid score. Must be between 0 and 100.")
        score = float(input("Enter a valid score (0-100): "))
    return score


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


def print_stars(score):
    """Print as many stars as the score (rounded to int)."""
    print("*" * int(score))

main()
