"""
CP1404 Practical 07
Read and display programming languages from a CSV file.
"""

import csv
from programming_language import ProgrammingLanguage

def main():
    languages = load_languages()  # Load languages from CSV
    if not languages:
        print("No languages loaded.")
        return

    for language in languages:
        print(language)

def load_languages(filename="languages.csv"):
    languages = []

    try:
        with open(filename, newline='', encoding='utf-8') as in_file:
            reader = csv.reader(in_file)
            next(reader, None)  # Skip header row

            for row in reader:
                if not row:
                    continue  # Skip empty rows

                # Convert string values from CSV into appropriate types
                name = row[0].strip()
                typing = row[1].strip()
                reflection = row[2].strip().lower() == "yes"  # Convert 'yes'/'no' to boolean
                year = int(row[3].strip())

                # Pointer arithmetic column is optional
                pointer_arithmetic = len(row) >= 5 and row[4].strip().lower() == "yes"

                # Create ProgrammingLanguage object and add to list
                language = ProgrammingLanguage(name, typing, reflection, year, pointer_arithmetic)
                languages.append(language)

    except FileNotFoundError:
        print(f"File not found: {filename}")

    return languages

main()
