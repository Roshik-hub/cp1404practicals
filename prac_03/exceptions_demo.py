"""
CP1404/CP5632 - Practical
Exceptions demo with questions answered.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    # To avoid ZeroDivisionError, check denominator before dividing
    if denominator == 0:
        print("Cannot divide by zero!")
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")

"""
Questions:
1. When will a ValueError occur?
   - When the user inputs something that cannot be converted to an integer, 
     such as a string with letters or special characters instead of a number.

2. When will a ZeroDivisionError occur?
   - When the user inputs 0 as the denominator, causing division by zero.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
   - Yes, by checking if the denominator is zero before performing the division,
     and handling that case separately, as done in the code above.
"""
