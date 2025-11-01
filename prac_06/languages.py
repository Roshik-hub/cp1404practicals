"""
CP1404/CP5632 Practical - Using the ProgrammingLanguage class

Estimate: 15 minutes
Actual: 15 minutes
"""

from programming_language import ProgrammingLanguage

# Create programming language objects
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

# Test __str__ method
print(python)
print(ruby)
print(visual_basic)

# Create a list of languages
languages = [python, ruby, visual_basic]

# Print names of dynamically typed languages
print("\nThe dynamically typed languages are:")
for language in languages:
    if language.is_dynamic():
        print(language.name)
