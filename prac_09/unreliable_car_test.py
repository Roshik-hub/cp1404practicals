from unreliable_car import UnreliableCar

def main():
    car = UnreliableCar("Dodgey", 100, 30)

    drives = 0
    for _ in range(100):
        if car.drive(1) > 0:
            drives += 1

    print(f"Car succeeded driving {drives} out of 100 attempts (approx 30 expected)")


main()
