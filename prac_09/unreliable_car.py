import random
from car import Car


class UnreliableCar(Car):
    """Car that sometimes fails to drive based on reliability %."""

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        if random.uniform(0, 100) < self.reliability:
            return super().drive(distance)
        return 0
