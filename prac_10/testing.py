"""
Practical 10 - Testing
"""

import doctest


def repeat_string(s, n):
    """Repeat string s n times."""
    return s * n


# Fix Car class test section
class Car:
    """Simple Car class for testing."""

    def __init__(self, fuel=0):
        self.fuel = fuel


# Assertions for Car fuel tests
car1 = Car(10)
assert car1.fuel == 10, "Fuel should be set correctly in constructor"

car2 = Car(0)
assert car2.fuel == 0, "Fuel should allow zero value"

car3 = Car(50)
assert car3.fuel == 50, "Fuel should store given integer amount"


def is_long_word(word, length=5):
    """
    Return True if word is at least as long as the length.

    >>> is_long_word("Python")
    True
    >>> is_long_word("cat")
    False
    >>> is_long_word("hello", 5)
    True
    """
    return len(word) >= length


def format_sentence(phrase):
    """
    Return phrase formatted as a sentence:
    - Capital first letter
    - Ends with one period

    >>> format_sentence("hello")
    'Hello.'
    >>> format_sentence("hello.")
    'Hello.'
    >>> format_sentence("this is good")
    'This is good.'
    >>> format_sentence("Already good.")
    'Already good.'
    """
    phrase = phrase.strip()
    phrase = phrase.capitalize()
    if not phrase.endswith('.'):
        phrase += '.'
    return phrase


# Run doctests
if __name__ == "__main__":
    doctest.testmod()
    print("All tests completed.")
