"""
CP1404 Practical 07
Custom project management software: load, display, add, update, and save projects.
"""

from project import Project
from datetime import datetime
import os

DEFAULT_FILE = "projects.txt"

def main():
    filename = DEFAULT_FILE
    projects = load_projects(filename)
    print(f"Loaded {len(projects)} projects from {filename}")

    menu = ("- (L)oad projects\n"
            "- (S)ave projects\n"
            "- (D)isplay projects\n"
            "- (F)ilter projects by date\n"
            "- (A)dd new project\n"
            "- (U)pdate project\n"
            "- (Q)uit\n")

    running = True
    while running:
        print(menu)
        choice = input(">>> ").strip().lower()
        if choice == 'l':
            fname = input("Filename to load: ").strip()
            if fname:
                projects = load_projects(fname)
            else:
                print("No filename entered.")
        elif choice == 's':
            fname = input("Filename to save to (leave blank for default): ").strip()
            save_projects(projects, fname if fname else filename)
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            filter_projects_by_date(projects)
        elif choice == 'a':
            add_new_project(projects)
        elif choice == 'u':
            update_project(projects)
        elif choice == 'q':
            ans = input(f"Would you like to save to {filename}? ").strip().lower()
            if ans in ('y', 'yes'):
                save_projects(projects, filename)
            print("Thank you for using custom-built project management software.")
            running = False
        else:
            print("Invalid option.")

def load_projects(filename=DEFAULT_FILE):
    """Load projects from a file. Skips malformed lines."""
    projects = []
    if not os.path.exists(filename):
        print(f"File not found: {filename}. Starting with empty project list.")
        return projects
    with open(filename, encoding='utf-8') as in_file:
        header = in_file.readline()  # skip header line
        for line in in_file:
            line = line.strip()
            if not line:
                continue
            try:
                projects.append(Project.from_file_line(line))
            except Exception as e:
                print(f"Skipping bad line: {line} -> {e}")
    return projects

def save_projects(projects, filename=DEFAULT_FILE):
    """Save all projects to a file with header."""
    with open(filename, "w", encoding='utf-8') as out_file:
        out_file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for p in projects:
            out_file.write(p.to_file_line() + "\n")
    print(f"Saved {len(projects)} projects to {filename}.")

def display_projects(projects):
    """Display incomplete and complete projects sorted by priority."""
    incomplete = sorted([p for p in projects if not p.is_complete()], key=lambda x: x.priority)
    complete = sorted([p for p in projects if p.is_complete()], key=lambda x: x.priority)

    if incomplete:
        print("Incomplete projects:")
        for p in incomplete:
            print(f"  {p}")
    else:
        print("No incomplete projects.")

    if complete:
        print("Completed projects:")
        for p in complete:
            print(f"  {p}")
    else:
        print("No completed projects.")

def filter_projects_by_date(projects):
    """Show projects starting after a given date."""
    date_str = input("Show projects that start after date (dd/mm/yyyy): ").strip()
    try:
        target_date = datetime.strptime(date_str, "%d/%m/%Y").date()
    except ValueError:
        print("Invalid date format.")
        return
    filtered = sorted([p for p in projects if p.start_date >= target_date], key=lambda x: x.start_date)
    for p in filtered:
        print(p)

def add_new_project(projects):
    """Add a new project interactively."""
    print("Let's add a new project")
    name = input("Name: ").strip()
    if not name:
        print("Project must have a name.")
        return
    date_str = input("Start date (dd/mm/yyyy): ").strip()
    try:
        start_date = datetime.strptime(date_str, "%d/%m/%Y").date()
    except ValueError:
        print("Invalid date format. Project not added.")
        return
    try:
        priority = int(input("Priority: ").strip())
        cost = float(input("Cost estimate: ").strip())
        completion = int(input("Percent complete: ").strip())
    except ValueError:
        print("Invalid numeric input. Project not added.")
        return
    projects.append(Project(name, start_date, priority, cost, completion))
    print("Project added.")

def update_project(projects):
    """Update priority and completion percentage of a selected project."""
    if not projects:
        print("No projects to update.")
        return
    for i, p in enumerate(projects):
        print(f"{i} {p}")
    try:
        idx = int(input("Project choice: ").strip())
        project = projects[idx]
    except (ValueError, IndexError):
        print("Invalid choice.")
        return

    new_completion = input("New Percentage: ").strip()
    new_priority = input("New Priority: ").strip()
    if new_completion:
        try:
            project.completion = int(new_completion)
        except ValueError:
            print("Invalid completion percent. Not changed.")
    if new_priority:
        try:
            project.priority = int(new_priority)
        except ValueError:
            print("Invalid priority. Not changed.")
    print("Project updated.")

main()
