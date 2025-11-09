"""
CP1404 Practical 07
Represents programming language information.
"""

class ProgrammingLanguage:
    """Store information about a programming language."""

    def __init__(self, name, typing, reflection, year, pointer_arithmetic=False):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year
        self.pointer_arithmetic = pointer_arithmetic

    def __repr__(self):
        """Developer-friendly representation."""
        return (f"ProgrammingLanguage({self.name!r}, {self.typing!r}, "
                f"{self.reflection}, {self.year}, {self.pointer_arithmetic})")

    def __str__(self):
        """Readable string for printing."""
        reflection_str = "Yes" if self.reflection else "No"
        pointer_str = "Yes" if self.pointer_arithmetic else "No"
        return (f"{self.name}, {self.typing} Typing, Reflection={reflection_str}, "
                f"Pointer Arithmetic={pointer_str}, First appeared in {self.year}")

    def is_dynamic(self):
        """Check if language is dynamically typed."""
        return self.typing.lower() == "dynamic"

    def supports_pointer_arithmetic(self):
        """Check if pointer arithmetic is supported."""
        return self.pointer_arithmetic


def run_tests():
    """Demo/test of ProgrammingLanguage class."""

    # Create sample language objects
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    cpp = ProgrammingLanguage("C++", "Static", False, 1983, True)

    languages = [ruby, python, cpp]

    # Display all languages
    for lang in languages:
        print(lang)

    # List dynamically typed languages
    print("\nDynamically typed languages:")
    for lang in languages:
        if lang.is_dynamic():
            print(f"- {lang.name}")
