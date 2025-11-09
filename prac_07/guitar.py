"""
CP1404 Practical 07
Represents a guitar with name, year, and cost.
"""

from datetime import datetime

class Guitar:
    """Store information about a guitar."""

    def __init__(self, name: str, year: int, cost: float):
        self.name = name
        self.year = int(year)
        self.cost = float(cost)

    def __str__(self):
        """Human-friendly string representation."""
        return f"{self.name}, {self.year}, ${self.cost:,.2f}"

    def __repr__(self):
        """Developer-friendly representation."""
        return f"Guitar({self.name!r}, {self.year}, {self.cost})"

    def is_vintage(self):
        """Return True if guitar is older than 30 years."""
        current_year = datetime.now().year
        return (current_year - self.year) >= 30

    def __lt__(self, other):
        """Compare guitars by year (oldest first) for sorting."""
        return self.year < other.year
