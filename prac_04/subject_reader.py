"""
CP1404 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Read subject data and display it nicely."""
    subjects = read_subjects_from_file(FILENAME)
    display_subject_details(subjects)


def read_subjects_from_file(filename):
    """
    Read data from file formatted like: subject_code,lecturer,num_students.
    Return a list of subjects, where each subject is [code, lecturer, num_students].
    """
    subjects = []
    with open(filename, "r") as input_file:
        for line in input_file:
            line = line.strip()  # Remove newline character
            parts = line.split(',')  # Split by comma
            parts[2] = int(parts[2])  # Convert number of students to int
            subjects.append(parts)  # Add to list
    return subjects


def display_subject_details(subjects):
    """Display subject details in a readable format."""
    for subject in subjects:
        code, lecturer, num_students = subject
        print(f"{code} is taught by {lecturer} and has {num_students} students")


main()
