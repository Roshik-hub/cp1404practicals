"""
CP1404/CP5632 Practical - ProgrammingLanguage class

Estimate: 20 minutes
Actual: 25 minutes
"""

class ProgrammingLanguage:
    """Represent a programming language with typing, reflection, and year info."""

    def __init__(self, name, typing, reflection, year):
        """
        Initialise a ProgrammingLanguage instance.

        name: str - the name of the language
        typing: str - 'Static' or 'Dynamic'
        reflection: bool - True if language supports reflection
        year: int - year the language first appeared
        """
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Return True if the language is dynamically typed, else False."""
        return self.typing.lower() == "dynamic"

    def __str__(self):
        """Return a string representation of the language."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
