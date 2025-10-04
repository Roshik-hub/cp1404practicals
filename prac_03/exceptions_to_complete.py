"""
CP1404/CP5632 - Practical
Program to get a valid integer from the user using exception handling.
"""

is_valid_input = False

while not is_valid_input:
    try:
        number = int(input("Enter a number: "))
        is_valid_input = True
    except ValueError:
        print("Invalid input; please enter a valid integer.")

print(f"You entered: {number}")
