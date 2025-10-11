import random

NUMBERS_PER_PICK = 6
MIN_NUMBER = 1
MAX_NUMBER = 45

def main():
    how_many = int(input("How many quick picks? "))
    for _ in range(how_many):
        quick_pick = generate_quick_pick()
        quick_pick.sort()
        print_quick_pick(quick_pick)

def generate_quick_pick():
    numbers = []
    while len(numbers) < NUMBERS_PER_PICK:
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        if number not in numbers:
            numbers.append(number)
    return numbers

def print_quick_pick(numbers):
    # Print numbers right aligned, width 2, separated by spaces
    print(" ".join(f"{num:2}" for num in numbers))

main()
