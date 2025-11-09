"""
CP1404 Practical 07
Represents a project with name, start date, priority, cost estimate, and completion.
"""

from datetime import datetime, date


class Project:
    """Store information about a project."""

    def __init__(self, name: str, start_date: date, priority: int, cost_estimate: float, completion: int):
        self.name = name
        self.start_date = start_date
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion = int(completion)

    def __str__(self):
        """Readable string for printing."""
        start = self.start_date.strftime("%d/%m/%Y")
        return (f"{self.name}, start: {start}, priority {self.priority}, "
                f"estimate: ${self.cost_estimate:,.2f}, completion: {self.completion}%")

    def __repr__(self):
        """Developer-friendly representation."""
        return (f"Project({self.name!r}, {self.start_date!r}, {self.priority}, "
                f"{self.cost_estimate}, {self.completion})")

    def is_complete(self):
        """Return True if the project is 100% complete or more."""
        return self.completion >= 100

    def to_file_line(self):
        """Return tab-separated string suitable for saving to a file."""
        return f"{self.name}\t{self.start_date.strftime('%d/%m/%Y')}\t{self.priority}\t{self.cost_estimate}\t{self.completion}"

    @classmethod
    def from_file_line(cls, line: str):
        """
        Create a Project object from a tab-separated line.
        Raises ValueError if the line does not have exactly 5 fields.
        """
        parts = line.strip().split('\t')
        if len(parts) != 5:
            raise ValueError("Invalid project line format")

        name = parts[0]
        # Convert string to date object
        start_date = datetime.strptime(parts[1], "%d/%m/%Y").date()
        priority = int(parts[2])
        cost_estimate = float(parts[3])
        completion = int(parts[4])
        return cls(name, start_date, priority, cost_estimate, completion)
