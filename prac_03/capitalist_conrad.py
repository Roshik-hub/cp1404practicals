"""
CP1404/CP5632 - Practical
Capitalist Conrad stock price simulator.

"""

import random

# Constants
MAX_INCREASE = 0.175  # 17.5%
MAX_DECREASE = 0.05   # 5%
MIN_PRICE = 1.0
MAX_PRICE = 100.0
INITIAL_PRICE = 10.0
FILENAME = "capitalist_conrad_output.txt"

price = INITIAL_PRICE
day = 0

out_file = open(FILENAME, 'w')  # Open file for writing

print(f"Starting price: ${price:,.2f}", file=out_file)

while MIN_PRICE <= price <= MAX_PRICE:
    day += 1
    if random.randint(1, 2) == 1:
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        price_change = random.uniform(-MAX_DECREASE, 0)

    price *= (1 + price_change)
    print(f"On day {day} price is: ${price:,.2f}", file=out_file)

out_file.close()
