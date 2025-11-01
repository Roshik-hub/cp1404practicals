"""
CP1404/CP5632 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.
"""

from car import Car

# 1. Create a new Car object called "limo" with 100 fuel
limo = Car(name="Limo", fuel=100)

# 2. Add 20 more units of fuel to limo
limo.add_fuel(20)

# 3. Print the amount of fuel in limo
print(f"Fuel in {limo.name}: {limo.fuel} units")

# 4. Attempt to drive the car 115 km
distance_driven = limo.drive(115)
print(f"Distance actually driven by {limo.name}: {distance_driven} km")

# 5. Print the car object to test __str__ method
print(limo)

# Optional: create another car with a name to test multiple cars
my_car = Car(name="MyCar", fuel=50)
print(my_car)
my_car.drive(30)
print(my_car)
