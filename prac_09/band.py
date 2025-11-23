class Band:
    """Band class representing a collection of Musicians."""

    def __init__(self, name):
        self.name = name
        self.musicians = []

    def add(self, musician):
        self.musicians.append(musician)

    def __str__(self):
        musician_str = ", ".join(str(m) for m in self.musicians)
        return f"{self.name} ({musician_str})"

    def play(self):
        for musician in self.musicians:
            musician.play()
